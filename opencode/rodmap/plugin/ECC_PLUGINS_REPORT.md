# Отчет: Плагины OpenCode (ECC - Everything Claude Code)

**Версия:** 1.10.0  
**Дата создания:** 2026-04-10  
**Автор:** OpenCode Analysis

---

## Содержание

1. [Общая архитектура](#1-общая-архитектура)
2. [Структура проекта](#2-структура-проекта)
3. [Основные компоненты](#3-основные-компоненты)
4. [Хуки (Events) и их назначение](#4-хуки-events-и-их-назначение)
5. [Управление профилями](#5-управление-профилями)
6. [Инструменты (Tools)](#6-инструменты-tools)
7. [Агенты (Agents)](#7-агенты-agents)
8. [Команды (Commands)](#8-команды-commands)
9. [План миграции](#9-план-миграции)

---

## 1. Общая архитектура

### 1.1. Что такое ECC?

**Everything Claude Code (ECC)** — это система автоматизации на основе хуков (hook-based automation), которая расширяет стандарт Claude Code с помощью более продвинутых возможностей OpenCode.

### 1.2. Сравнение: Claude Code vs OpenCode

| Функция | Claude Code | OpenCode |
|---------|-------------|----------|
| Фазы хуков | 3 (PreToolUse, PostToolUse, Stop) | **20+ типов событий** |
| Гибкость | Фиксированная | Высокая настраиваемость |
| Профили | Нет | minimal / standard / strict |
| Агенты | Ограничено | 22+ специализированных |
| Инструменты | Базовые | 8 кастомных |

### 1.3. Философия ECC

- **TDD**: write tests first, 80%+ coverage
- **Immutability**: never mutate, always return new copies
- **Security**: validate inputs, no hardcoded secrets

---

## 2. Структура проекта

```
📁 .opencode/
├── 📄 package.json              # Зависимости и метаданные
├── 📄 tsconfig.json            # Конфигурация TypeScript
├── 📄 opencode.json            # Главная конфигурация OpenCode (~462 строк)
├── 📄 index.ts                 # Точка входа плагина (~80 строк)
│
├── 📁 plugins/
│   ├── 📄 index.ts             # Экспорт плагинов (~12 строк)
│   ├── 📄 ecc-hooks.ts        # Основная логика хуков (~523 строки)
│   └── 📁 lib/
│       └── 📄 changed-files-store.ts  # Хранилище изменений (~98 строк)
│
├── 📁 tools/
│   ├── 📄 index.ts            # Экспорт инструментов
│   ├── 📄 changed-files.ts    # Инструмент для изменённых файлов (~83 строки)
│   ├── 📄 run-tests.ts        # Запуск тестов
│   ├── 📄 check-coverage.ts   # Проверка покрытия
│   ├── 📄 security-audit.ts   # Сканирование безопасности
│   ├── 📄 format-code.ts      # Форматирование кода
│   ├── 📄 lint-check.ts       # Проверка линтером
│   └── 📄 git-summary.ts      # Git сводка
│
├── 📁 commands/               # 31 Markdown-команда
│   ├── plan.md, tdd.md, security.md, ...
│
├── 📁 prompts/
│   └── 📁 agents/             # 22 агента (txt файлы)
│       ├── planner.txt, code-reviewer.txt, ...
│
├── 📁 instructions/
│   └── 📄 INSTRUCTIONS.md     # Инструкции для AI
│
└── 📁 skills/                 # 11 навыков (опционально)
```

---

## 3. Основные компоненты

### 3.1. ECC Hooks Plugin (`ecc-hooks.ts`)

**Назначение:** Переводит хуки Claude Code в систему плагинов OpenCode.

**Основные возможности:**
- Профили работы: `minimal`, `standard`, `strict`
- 11 типов хуков
- 8 кастомных инструментов
- Авто-определение технологий проекта

### 3.2. Changed Files Store (`lib/changed-files-store.ts`)

**Назначение:** Хранит информацию обо всех изменённых файлах с типами изменений.

**Типы изменений:**
- `added` - новые файлы
- `modified` - изменённые файлы
- `deleted` - удалённые файлы

**API:**
```typescript
initStore(worktree: string): void
recordChange(filePath: string, type: ChangeType): void
getChanges(): Map<string, ChangeType>
buildTree(filter?: ChangeType): TreeNode[]
clearChanges(): void
hasChanges(): boolean
```

---

## 4. Хуки (Events) и их назначение

### 4.1. Маппинг хуков Claude Code → OpenCode

| Claude Code | OpenCode |
|-------------|----------|
| PreToolUse | `tool.execute.before` |
| PostToolUse | `tool.execute.after` |
| Stop | `session.idle` / `session.status` |
| SessionStart | `session.created` |
| SessionEnd | `session.deleted` |

### 4.2. Хуки файловой системы

#### `file.edited`
**Триггер:** Файл отредактирован

**Действия:**
1. Добавляет файл в отслеживаемые (`editedFiles`)
2. Записывает изменение в хранилище
3. **Auto-format** для JS/TS (только `strict` профиль):
   ```typescript
   if (hookEnabled("post:edit:format", ["strict"])) {
     await $`prettier --write ${event.path}`
   }
   ```
4. **Предупреждение о console.log** (`standard` & `strict`):
   ```typescript
   if (hookEnabled("post:edit:console-warn", ["standard", "strict"])) {
     const result = await $`grep -n "console\.log" ${event.path}`
     if (result.trim()) {
       log("warn", `[ECC] console.log found in ${event.path}`)
     }
   }
   ```

#### `file.watcher.updated`
**Триггер:** Изменение через файловый watcher

**Действие:** Обновление трекинга изменений
```typescript
"file.watcher.updated": async (event: { path: string; type: string }) => {
  let changeType: "added" | "modified" | "deleted" = "modified"
  if (event.type === "create" || event.type === "add") changeType = "added"
  else if (event.type === "delete" || event.type === "remove") changeType = "deleted"
  recordChange(event.path, changeType)
}
```

### 4.3. Хуки инструментов

#### `tool.execute.before`
**Триггер:** Перед выполнением инструмента

**Действия:**
1. **Отслеживание write операций:**
   ```typescript
   if (input.tool === "write") {
     const filePath = getFilePath(input.args)
     if (filePath) {
       const type = fs.existsSync(absPath) ? "modified" : "added"
       pendingToolChanges.set(key, { path: filePath, type })
     }
   }
   ```

2. **Напоминание перед git push** (`strict`):
   ```typescript
   if (hookEnabled("pre:bash:git-push-reminder", "strict")) {
     if (input.tool === "bash" && args.includes("git push")) {
       log("info", "[ECC] Remember to review changes before pushing")
     }
   }
   ```

3. **Предупреждение о doc-файлах** (`standard` & `strict`):
   ```typescript
   if (filePath.match(/\.(md|txt)$/i) && 
       !filePath.includes("README") &&
       !filePath.includes("CHANGELOG")) {
     log("warn", `[ECC] Creating ${filePath} - consider if this documentation is necessary`)
   }
   ```

4. **Напоминание о длительных командах** (`strict`):
   ```typescript
   if (cmd.match(/^(npm|pnpm|yarn|bun)\s+(install|build|test|run)/) ||
       cmd.match(/^cargo\s+(build|test|run)/)) {
     log("info", "[ECC] Long-running command detected")
   }
   ```

#### `tool.execute.after`
**Триггер:** После выполнения инструмента

**Действия:**
1. **TypeScript проверка** (`strict`):
   ```typescript
   if (hookEnabled("post:edit:typecheck", ["strict"])) {
     try {
       await $`npx tsc --noEmit`
       log("info", "[ECC] TypeScript check passed")
     } catch (error) {
       log("warn", "[ECC] TypeScript errors detected")
     }
   }
   ```

2. **Логирование создания PR**:
   ```typescript
   if (input.tool === "bash" && args.includes("gh pr create")) {
     log("info", "[ECC] PR created - check GitHub Actions status")
   }
   ```

### 4.4. Хуки сессии

#### `session.created`
**Триггер:** Сессия создана

**Действия:**
- Загрузка проектного контекста из `CLAUDE.md`
- Приветственное сообщение
- Инициализация хранилища

```typescript
"session.created": async () => {
  log("info", `[ECC] Session started - profile=${currentProfile}`)
  
  const hasClaudeMd = await $`test -f ${worktree}/CLAUDE.md`
  if (hasClaudeMd.trim() === "yes") {
    log("info", "[ECC] Found CLAUDE.md - loading project context")
  }
}
```

#### `session.idle`
**Триггер:** Сессия простаивает (задача завершена)

**Действия:**
1. **Финальный аудит console.log:**
   ```typescript
   for (const file of editedFiles) {
     const result = await $`grep -c "console\.log" ${file}`
     const count = parseInt(result.trim(), 10)
     if (count > 0) {
       totalConsoleLogCount += count
       filesWithConsoleLogs.push(file)
     }
   }
   ```

2. **Desktop уведомление** (macOS):
   ```typescript
   await $`osascript -e 'display notification "Task completed!" with title "OpenCode ECC"'`
   ```

3. **Очистка трекинга:**
   ```typescript
   editedFiles.clear()
   ```

#### `session.deleted`
**Триггер:** Сессия удалена

**Действия:**
- Полная очистка состояния
- Удаление всех временных данных

```typescript
"session.deleted": async () => {
  log("info", "[ECC] Session ended - cleaning up")
  editedFiles.clear()
  clearChanges()
  pendingToolChanges.clear()
}
```

### 4.5. Специальные хуки OpenCode

#### `shell.env`
**Триггер:** Перед выполнением shell-команды

**Назначение:** Инжекция переменных окружения

```typescript
"shell.env": async () => {
  const env: Record<string, string> = {
    ECC_VERSION: "1.8.0",
    ECC_PLUGIN: "true",
    PROJECT_ROOT: worktree,
  }

  // Автоопределение package manager
  const lockfiles: Record<string, string> = {
    "bun.lockb": "bun",
    "pnpm-lock.yaml": "pnpm",
    "yarn.lock": "yarn",
    "package-lock.json": "npm",
  }
  for (const [lockfile, pm] of Object.entries(lockfiles)) {
    try {
      await $`test -f ${worktree}/${lockfile}`
      env.PACKAGE_MANAGER = pm
      break
    } catch {}
  }

  // Определение языков
  const langDetectors: Record<string, string> = {
    "tsconfig.json": "typescript",
    "go.mod": "go",
    "pyproject.toml": "python",
    "Cargo.toml": "rust",
    "Package.swift": "swift",
  }
  const detected: string[] = []
  for (const [file, lang] of Object.entries(langDetectors)) {
    try {
      await $`test -f ${worktree}/${file}`
      detected.push(lang)
    } catch {}
  }
  if (detected.length > 0) {
    env.DETECTED_LANGUAGES = detected.join(",")
    env.PRIMARY_LANGUAGE = detected[0]
  }

  return env
}
```

**Возвращаемые переменные:**
- `ECC_VERSION` - версия плагина
- `ECC_PLUGIN` - флаг активности
- `PROJECT_ROOT` - корневая директория
- `PACKAGE_MANAGER` - обнаруженный менеджер (npm/yarn/pnpm/bun)
- `DETECTED_LANGUAGES` - список языков через запятую
- `PRIMARY_LANGUAGE` - основной язык проекта

#### `experimental.session.compacting`
**Триггер:** Перед compaction (сжатием контекста)

**Назначение:** Сохранение важного контекста

```typescript
"experimental.session.compacting": async () => {
  const contextBlock = [
    "# ECC Context (preserve across compaction)",
    "",
    "## Active Plugin: Everything Claude Code v1.8.0",
    "- Hooks: file.edited, tool.execute.before/after, session.created/idle/deleted",
    "- Tools: run-tests, check-coverage, security-audit, format-code, ...",
    "- Agents: 13 specialized agents",
    "",
    "## Key Principles",
    "- TDD: write tests first, 80%+ coverage",
    "- Immutability: never mutate, always return new copies",
    "- Security: validate inputs, no hardcoded secrets",
    "",
  ]

  return {
    context: contextBlock.join("\n"),
    compaction_prompt: "Focus on preserving: 1) Current task status and progress, 2) Key decisions made, 3) Files created/modified, 4) Remaining work items, 5) Any security concerns flagged. Discard: verbose tool outputs, intermediate exploration, redundant file listings.",
  }
}
```

#### `permission.ask`
**Триггер:** Запрос разрешения

**Назначение:** Авто-одобрение безопасных операций

```typescript
"permission.ask": async (event: { tool: string; args: unknown }) => {
  log("info", `[ECC] Permission requested for: ${event.tool}`)

  // Auto-approve: read-only инструменты
  if (["read", "glob", "grep", "search", "list"].includes(event.tool)) {
    return { approved: true, reason: "Read-only operation" }
  }

  // Auto-approve: форматтеры
  if (event.tool === "bash" && /^(npx )?(prettier|biome|black|gofmt|rustfmt)/.test(cmd)) {
    return { approved: true, reason: "Formatter execution" }
  }

  // Auto-approve: тесты
  if (event.tool === "bash" && /^(npm test|npx vitest|pytest|go test|cargo test)/.test(cmd)) {
    return { approved: true, reason: "Test execution" }
  }

  // Всё остальное - на решение пользователя
  return { approved: undefined }
}
```

#### `todo.updated`
**Триггер:** Обновление todo-списка

**Назначение:** Отслеживание прогресса

```typescript
"todo.updated": async (event: { todos: Array<{ text: string; done: boolean }> }) => {
  const completed = event.todos.filter((t) => t.done).length
  const total = event.todos.length
  if (total > 0) {
    log("info", `[ECC] Progress: ${completed}/${total} tasks completed`)
  }
}
```

---

## 5. Управление профилями

### 5.1. Доступные профили

| Профиль | Уровень | Описание |
|---------|---------|----------|
| `minimal` | 0 | Минимальные проверки, базовый функционал |
| `standard` | 1 | Стандартный режим (по умолчанию) |
| `strict` | 2 | Максимальная строгость, все проверки |

### 5.2. Конфигурация через переменные окружения

```bash
# Выбор профиля
export ECC_HOOK_PROFILE=strict  # minimal | standard | strict

# Отключение конкретных хуков
export ECC_DISABLED_HOOKS="post:edit:format,pre:bash:tmux-reminder"
```

### 5.3. Матрица доступности хуков

| Хук ID | minimal | standard | strict |
|--------|---------|----------|--------|
| `post:edit:format` | ❌ | ❌ | ✅ |
| `post:edit:console-warn` | ❌ | ✅ | ✅ |
| `post:edit:typecheck` | ❌ | ❌ | ✅ |
| `post:bash:pr-created` | ❌ | ✅ | ✅ |
| `pre:bash:git-push-reminder` | ❌ | ❌ | ✅ |
| `pre:write:doc-file-warning` | ❌ | ✅ | ✅ |
| `pre:bash:tmux-reminder` | ❌ | ❌ | ✅ |
| `session:start` | ✅ | ✅ | ✅ |
| `session:end-marker` | ✅ | ✅ | ✅ |
| `stop:check-console-log` | ✅ | ✅ | ✅ |

### 5.4. Система проверки профилей

```typescript
const profileOrder: Record<HookProfile, number> = {
  minimal: 0,
  standard: 1,
  strict: 2,
}

const profileAllowed = (required: HookProfile | HookProfile[]): boolean => {
  if (Array.isArray(required)) {
    return required.some((entry) => profileOrder[currentProfile] >= profileOrder[entry])
  }
  return profileOrder[currentProfile] >= profileOrder[required]
}

const hookEnabled = (hookId: string, requiredProfile: HookProfile | HookProfile[] = "standard"): boolean => {
  if (disabledHooks.has(hookId)) return false
  return profileAllowed(requiredProfile)
}
```

---

## 6. Инструменты (Tools)

### 6.1. Список кастомных инструментов

| Инструмент | Файл | Назначение |
|------------|------|------------|
| `changed-files` | `tools/changed-files.ts` | Список изменённых файлов |
| `run-tests` | `tools/run-tests.ts` | Запуск тестов с автоопределением |
| `check-coverage` | `tools/check-coverage.ts` | Проверка покрытия кода |
| `security-audit` | `tools/security-audit.ts` | Сканирование уязвимостей |
| `format-code` | `tools/format-code.ts` | Форматирование кода |
| `lint-check` | `tools/lint-check.ts` | Проверка линтером |
| `git-summary` | `tools/git-summary.ts` | Git статистика |

### 6.2. Инструмент `changed-files`

**Описание:** Список файлов, изменённых агентами в текущей сессии, в виде навигационного дерева.

**Аргументы:**
```typescript
{
  filter?: "all" | "added" | "modified" | "deleted"  // По умолчанию: all
  format?: "tree" | "json"                            // По умолчанию: tree
}
```

**Индикаторы:**
- `+` - добавленные файлы
- `~` - изменённые файлы
- `-` - удалённые файлы

**Пример вывода:**
```
Changed files (3):

src/
  components/
    Button.tsx (~)
  utils/
    helper.ts (+)
tests/
  old.test.ts (-)

To view diff for a file:
  git diff src/components/Button.tsx
  git diff src/utils/helper.ts
```

### 6.3. Интеграция с плагином

```typescript
// ecc-hooks.ts
import changedFilesTool from "../tools/changed-files.js"

export const ECCHooksPlugin = async ({ client, $, directory, worktree }: PluginInput) => {
  // ... код плагина ...
  
  return {
    // ... хуки ...
    
    tool: {
      "changed-files": changedFilesTool,
    },
  }
}
```

---

## 7. Агенты (Agents)

### 7.1. Список агентов (22 специализированных)

#### Основные агенты разработки:

| Агент | Назначение | Модель | Режим |
|-------|------------|--------|-------|
| `build` | Основной агент разработки | claude-sonnet-4-5 | primary |
| `planner` | Планирование сложных задач | claude-opus-4-5 | subagent |
| `architect` | Архитектурные решения | claude-opus-4-5 | subagent |
| `code-reviewer` | Ревью кода | claude-opus-4-5 | subagent |
| `security-reviewer` | Проверка безопасности | claude-opus-4-5 | subagent |
| `tdd-guide` | TDD методология | claude-opus-4-5 | subagent |
| `build-error-resolver` | Исправление ошибок сборки | claude-opus-4-5 | subagent |
| `e2e-runner` | E2E тестирование (Playwright) | claude-opus-4-5 | subagent |
| `refactor-cleaner` | Рефакторинг и очистка | claude-opus-4-5 | subagent |
| `doc-updater` | Обновление документации | claude-opus-4-5 | subagent |

#### Специализированные агенты по языкам:

| Агент | Язык/Технология |
|-------|-----------------|
| `go-reviewer` | Go |
| `go-build-resolver` | Go сборка |
| `python-reviewer` | Python |
| `rust-reviewer` | Rust |
| `rust-build-resolver` | Rust сборка (Cargo) |
| `java-reviewer` | Java/Spring Boot |
| `java-build-resolver` | Java/Maven/Gradle |
| `kotlin-reviewer` | Kotlin/Android/KMP |
| `kotlin-build-resolver` | Kotlin/Gradle |
| `cpp-reviewer` | C++ |
| `cpp-build-resolver` | C++/CMake |
| `database-reviewer` | PostgreSQL/Supabase |

#### Служебные агенты:

| Агент | Назначение |
|-------|------------|
| `docs-lookup` | Поиск документации (Context7 MCP) |
| `harness-optimizer` | Оптимизация конфигурации |
| `loop-operator` | Управление автономными циклами |

### 7.2. Конфигурация агента

```json
{
  "agent": {
    "code-reviewer": {
      "description": "Expert code review specialist...",
      "mode": "subagent",
      "model": "anthropic/claude-opus-4-5",
      "prompt": "{file:prompts/agents/code-reviewer.txt}",
      "tools": {
        "read": true,
        "bash": true,
        "write": false,
        "edit": false
      }
    }
  }
}
```

---

## 8. Команды (Commands)

### 8.1. Список команд (31 команда)

#### Разработка:

| Команда | Агент | Описание |
|---------|-------|----------|
| `/plan` | planner | Создание плана реализации |
| `/tdd` | tdd-guide | TDD workflow с 80%+ покрытием |
| `/code-review` | code-reviewer | Ревью кода |
| `/security` | security-reviewer | Проверка безопасности |
| `/build-fix` | build-error-resolver | Исправление ошибок сборки |
| `/e2e` | e2e-runner | E2E тесты (Playwright) |
| `/refactor-clean` | refactor-cleaner | Очистка мёртвого кода |
| `/orchestrate` | planner | Оркестрация агентов |

#### Документация:

| Команда | Агент | Описание |
|---------|-------|----------|
| `/update-docs` | doc-updater | Обновление документации |
| `/update-codemaps` | doc-updater | Обновление кодмапов |

#### Go:

| Команда | Агент | Описание |
|---------|-------|----------|
| `/go-review` | go-reviewer | Go ревью |
| `/go-test` | tdd-guide | Go TDD |
| `/go-build` | go-build-resolver | Исправление Go ошибок |

#### Проверка и верификация:

| Команда | Описание |
|---------|----------|
| `/verify` | Запуск verification loop |
| `/eval` | Оценка по критериям |
| `/checkpoint` | Сохранение состояния |
| `/test-coverage` | Анализ покрытия |

#### Инстинкты и обучение:

| Команда | Описание |
|---------|----------|
| `/learn` | Извлечение паттернов |
| `/skill-create` | Создание skills из истории |
| `/instinct-status` | Просмотр инстинктов |
| `/instinct-import` | Импорт инстинктов |
| `/instinct-export` | Экспорт инстинктов |
| `/evolve` | Кластеризация в skills |
| `/promote` | Продвижение в global scope |
| `/projects` | Список проектов |

### 8.2. Структура команды

```json
{
  "command": {
    "tdd": {
      "description": "Enforce TDD workflow with 80%+ test coverage",
      "template": "{file:commands/tdd.md}\n\n$ARGUMENTS",
      "agent": "tdd-guide",
      "subtask": true
    }
  }
}
```

---

## 9. План миграции

### 9.1. Файлы для миграции

#### Обязательные (Core) - 15 файлов:

| # | Путь | Описание |
|---|------|----------|
| 1 | `.opencode/package.json` | Зависимости и метаданные |
| 2 | `.opencode/tsconfig.json` | Конфиг TypeScript |
| 3 | `.opencode/opencode.json` | Главная конфигурация |
| 4 | `.opencode/index.ts` | Точка входа |
| 5 | `.opencode/plugins/index.ts` | Экспорт плагинов |
| 6 | `.opencode/plugins/ecc-hooks.ts` | **Главный плагин** |
| 7 | `.opencode/plugins/lib/changed-files-store.ts` | Хранилище |
| 8 | `.opencode/tools/index.ts` | Экспорт инструментов |
| 9 | `.opencode/tools/changed-files.ts` | Инструмент изменений |
| 10 | `.opencode/tools/run-tests.ts` | Запуск тестов |
| 11 | `.opencode/tools/check-coverage.ts` | Проверка покрытия |
| 12 | `.opencode/tools/security-audit.ts` | Сканер безопасности |
| 13 | `.opencode/tools/format-code.ts` | Форматтер |
| 14 | `.opencode/tools/lint-check.ts` | Линтер |
| 15 | `.opencode/tools/git-summary.ts` | Git сводка |

#### Опциональные:

| # | Путь | Описание | Количество |
|---|------|----------|------------|
| 16 | `.opencode/instructions/INSTRUCTIONS.md` | Инструкции AI | 1 |
| 17 | `.opencode/commands/*.md` | Пользовательские команды | 31 |
| 18 | `.opencode/prompts/agents/*.txt` | Агенты | 22 |
| 19 | `.opencode/skills/**` | Навыки | 11 |

### 9.2. Пошаговая инструкция миграции

#### Шаг 1: Подготовка (Pre-migration)

**Проверки:**
- [ ] Убедиться, что целевой проект использует **OpenCode**
- [ ] Проверить версию Node.js (>=18.0.0)
- [ ] Проверить наличие TypeScript в проекте
- [ ] Сделать резервную копию существующей конфигурации

#### Шаг 2: Копирование файлов

```bash
# Создать структуру в целевом проекте
mkdir -p .opencode/plugins/lib
mkdir -p .opencode/tools
mkdir -p .opencode/commands
mkdir -p .opencode/prompts/agents
mkdir -p .opencode/instructions
mkdir -p .opencode/skills  # опционально

# Копировать обязательные файлы
cp package.json tsconfig.json opencode.json index.ts .opencode/
cp plugins/index.ts plugins/ecc-hooks.ts .opencode/plugins/
cp plugins/lib/changed-files-store.ts .opencode/plugins/lib/
cp tools/*.ts .opencode/tools/

# Копировать опциональные (рекомендуется)
cp -r commands/ .opencode/
cp -r prompts/agents/ .opencode/prompts/
cp instructions/INSTRUCTIONS.md .opencode/instructions/
```

#### Шаг 3: Установка зависимостей

```bash
cd .opencode
npm install
```

**Зависимости:**
- `@opencode-ai/plugin` (^1.0.0) - **Peer dependency**
- `typescript` (^5.3.0)
- `@types/node` (^20.0.0)

#### Шаг 4: Сборка

```bash
cd .opencode
npm run build
```

Проверить создание папки `dist/` с скомпилированными `.js` и `.d.ts` файлами.

#### Шаг 5: Настройка окружения (Опционально)

```bash
# Выбор профиля хуков
export ECC_HOOK_PROFILE=standard  # minimal | standard | strict

# Отключение конкретных хуков
export ECC_DISABLED_HOOKS="post:edit:format,pre:bash:tmux-reminder"
```

#### Шаг 6: Интеграция с корневым opencode.json

Если в целевом проекте уже есть `opencode.json` в корне, объединить конфигурации:

```json
{
  "plugin": [
    "./.opencode/plugins"
  ],
  "instructions": [
    ".opencode/instructions/INSTRUCTIONS.md"
  ],
  "agent": {
    // Все агенты из ECC
  },
  "command": {
    // Все команды из ECC
  }
}
```

### 9.3. Минимальный набор (Quick Start)

Если нужен только базовый функционал:

**Файлы (7 штук):**
```
.opencode/
├── package.json
├── tsconfig.json
├── index.ts
└── plugins/
    ├── index.ts
    ├── ecc-hooks.ts
    └── lib/
        └── changed-files-store.ts
```

**Команды:**
```bash
cd .opencode && npm install && npm run build
```

**В корневом opencode.json:**
```json
{
  "plugin": ["./.opencode/plugins"]
}
```

### 9.4. Возможные проблемы и решения

| Проблема | Решение |
|----------|---------|
| Конфликт `plugin` путей | Использовать массив и добавить пути |
| Конфликт `instructions` | Объединить массивы инструкций |
| Конфликт `agent` имён | Переименовать агентов (например, `ecc-planner`) |
| Конфликт `command` имён | Переименовать команды (например, `ecc-plan`) |
| Дублирование `tsconfig.json` | Использовать `extends` или отдельный конфиг |
| Ошибки сборки TypeScript | Проверить версию TS (>=5.3) и Node (>=18) |

### 9.5. Чеклист миграции

- [ ] Скопированы все обязательные файлы
- [ ] Установлены npm зависимости
- [ ] TypeScript успешно скомпилирован (`dist/` создана)
- [ ] Пути в `opencode.json` настроены корректно
- [ ] Проверена работа базового хука (`file.edited`)
- [ ] Проверена работа инструментов (`changed-files`, `run-tests`)
- [ ] Настроены переменные окружения (опционально)
- [ ] Создана резервная копка оригинальной конфигурации

---

## Преимущества системы

### Для разработчика:
- ✅ Автоматическое форматирование кода (Prettier)
- ✅ Раннее обнаружение `console.log`
- ✅ Проверка типов TypeScript
- ✅ Напоминания о code review
- ✅ Desktop уведомления о завершении задач

### Для проекта:
- ✅ Контроль качества кода
- ✅ Предотвращение ненужной документации
- ✅ Автоматический аудит перед коммитом
- ✅ Интеграция с GitHub Actions
- ✅ Отслеживание изменённых файлов

### Для AI-ассистента:
- ✅ Богатый контекст (языки, менеджер пакетов)
- ✅ Авто-одобрение безопасных операций
- ✅ Сохранение контекста при compaction
- ✅ Трекинг прогресса задач (todo)
- ✅ 22 специализированных агента

---

## Заключение

Система плагинов OpenCode (ECC) представляет собой **продвинутую систему автоматизации**, которая:

1. **Расширяет** возможности Claude Code с 3 до 20+ типов событий
2. **Адаптируется** к проекту через автоопределение технологий
3. **Контролирует** качество кода на каждом этапе
4. **Упрощает** работу с автоматическими одобрениями
5. **Сохраняет** контекст между сессиями
6. **Предоставляет** 22 специализированных агента
7. **Включает** 31 пользовательскую команду
8. **Имеет** 8 кастомных инструментов

Это мощный инструмент для поддержания высокого качества кода и автоматизации рутинных задач разработки.

---

**Статистика:**
- Файлов кода: ~800+ строк TypeScript
- Хуков: 11 типов событий
- Агентов: 22 специализированных
- Команд: 31
- Инструментов: 8
- Профилей: 3 (minimal/standard/strict)

---

*Отчет сгенерирован автоматически на основе анализа кодовой базы ECC v1.10.0*
