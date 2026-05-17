# 📊 Отчет: Плагины OpenCode (ECC - Everything Claude Code)
---
## 📋 Содержание
1. [Общая архитектура](#1-общая-архитектура)
2. [Структура плагинов](#2-структура-плагинов)
3. [Основные компоненты](#3-основные-компоненты)
4. [Хуки (Events) и их назначение](#4-хуки-events-и-их-назначение)
5. [Детальное описание каждого хука](#5-детальное-описание-каждого-хука)
6. [Управление профилями](#6-управление-профилями)
7. [Инструмент changed-files](#7-инструмент-changed-files)
8. [Преимущества системы](#8-преимущества-системы)
9. [Заключение](#9-заключение)
---

## 1. Общая архитектура
Плагины **OpenCode** представляют собой систему автоматизации на основе хуков (hook-based automation). Они являются расширением стандарта Claude Code, но с более продвинутыми возможностями.

### 🔄 Сравнение: Claude Code vs OpenCode
| Функция | Claude Code | OpenCode |
|---------|-------------|----------|
| **Фазы хуков** | 3 (PreToolUse, PostToolUse, Stop) | 20+ событий |
| **Гибкость** | Фиксированная | Настраиваемая через профили |
| **Профили** | ❌ Нет | ✅ minimal / standard / strict |
---

## 2. Структура плагинов
```
.opencode/plugins/
├── 📄 index.ts              # Главный экспорт
├── ⚙️  ecc-hooks.ts          # Основная логика плагина
└── 📁 lib/
    └── 💾 changed-files-store.ts  # Хранилище изменённых файлов
```
---

## 3. Основные компоненты
### 3.1. 🔌 ECC Hooks Plugin (`ecc-hooks.ts`)
**Назначение:** Переводит хуки Claude Code в систему плагинов OpenCode.
#### 📊 Профили работы:
| Профиль | Описание |
|---------|----------|
| `minimal` | Минимальные проверки |
| `standard` | Стандартный режим *(по умолчанию)* |
| `strict` | Максимальная строгость |

### 3.2. 💾 Changed Files Store (`lib/changed-files-store.ts`)
**Назначение:** Хранит информацию обо всех изменённых файлах с типами изменений:
| Тип | Описание |
|-----|----------|
| ➕ `added` | Новые файлы |
| 📝 `modified` | Изменённые файлы |
| 🗑️ `deleted` | Удалённые файлы |

#### 🔧 Основные функции:
| Функция | Описание |
|---------|----------|
| `initStore()` | Инициализация хранилища |
| `recordChange()` | Запись изменения |
| `buildTree()` | Построение древовидной структуры изменений |
| `getChanges()` | Получение списка изменений |
| `clearChanges()` | Очистка хранилища |
---

## 4. Хуки (Events) и их назначение
### 4.1. 📁 Хуки файловой системы
| Хук | Событие | Действие |
|-----|---------|----------|
| `file.edited` | Файл отредактирован | Форматирование Prettier, проверка `console.log` |
| `file.watcher.updated` | Изменение через watcher | Обновление трекинга изменений |

### 4.2. 🛠️ Хуки инструментов
| Хук | Событие |
|-----|---------|
| `tool.execute.before` | Перед выполнением инструмента |
| `tool.execute.after` | После выполнения инструмента |

### 4.3. 👤 Хуки сессии
| Хук | Событие | Действие |
|-----|---------|----------|
| `session.created` | Сессия создана | Загрузка контекста, приветствие |
| `session.idle` | Сессия простаивает | Аудит `console.log`, уведомления |
| `session.deleted` | Сессия удалена | Очистка состояния |

### 4.4. ✨ Специальные хуки OpenCode
| Хук | Назначение |
|-----|------------|
| `shell.env` | Инжекция переменных окружения (`PACKAGE_MANAGER`, `DETECTED_LANGUAGES`) |
| `experimental.session.compacting` | Управление compaction (сжатие контекста) |
| `permission.ask` | Авто-одобрение безопасных операций |
| `todo.updated` | Отслеживание прогресса задач |
---

## 5. Детальное описание каждого хука
### 5.1. 📝 `file.edited`
```typescript
"file.edited": async (event: { path: string }) => {
  // 1. Добавляет файл в отслеживаемые
  editedFiles.add(event.path);
  recordChange(event.path, "modified");

  // 2. Auto-format для JS/TS (только strict профиль)
  if (hookEnabled("post:edit:format", ["strict"])) {
    await $`prettier --write ${event.path}`;
  }

  // 3. Предупреждение о console.log (standard & strict)
  if (hookEnabled("post:edit:console-warn", ["standard", "strict"])) {
    // Проверяет наличие console.log в файле
  }
};
```

#### 🎯 Назначение:
- ✅ Автоматическое форматирование кода
- ⚠️ Раннее предупреждение о `console.log`
---

### 5.2. ✅ `tool.execute.after`
```typescript
"tool.execute.after": async (input, output) => {
  // Отслеживание изменений для edit/write
  if (input.tool === "edit" && filePath) {
    recordChange(filePath, "modified");
  }

  // TypeScript проверка (strict)
  if (hookEnabled("post:edit:typecheck", ["strict"])) {
    await $`npx tsc --noEmit`;
  }

  // Логирование создания PR
  if (input.tool === "bash" && args.includes("gh pr create")) {
    log("info", "[ECC] PR created");
  }
};
```

#### 🎯 Назначение:
- 📊 Отслеживание всех изменений файлов
- 🔍 Автоматическая проверка типов TypeScript
- 🔔 Мониторинг создания Pull Request
---

### 5.3. ⏳ `tool.execute.before`
```typescript
"tool.execute.before": async (input) => {
  // Отслеживание write операций
  if (input.tool === "write") {
    pendingToolChanges.set(key, { path: filePath, type });
  }

  // Напоминание перед git push (strict)
  if (input.tool === "bash" && args.includes("git push")) {
    log("info", "Remember to review changes before pushing");
  }

  // Предупреждение о doc-файлах
  if (input.tool === "write" && filePath.match(/\.(md|txt)$/)) {
    log("warn", "Consider if this documentation is necessary");
  }

  // Напоминание о длительных командах (strict)
  if (input.tool === "bash" && isLongRunningCommand(cmd)) {
    log("info", "Long-running command detected");
  }
};
```

#### 🎯 Назначение:
- 🔒 Предварительные проверки перед выполнением
- 🚫 Блокировка ненужной документации
- 👁️ Напоминания о code review
---

### 5.4. 🚀 `session.created`
```typescript
"session.created": async () => {
  log("info", `[ECC] Session started - profile=${currentProfile}`);

  // Проверка наличия CLAUDE.md
  const hasClaudeMd = await $`test -f ${worktree}/CLAUDE.md`;
  if (hasClaudeMd) {
    log("info", "[ECC] Found CLAUDE.md - loading project context");
  }
};
```

#### 🎯 Назначение:
- 🎬 Инициализация сессии
- 📖 Загрузка проектного контекста из `CLAUDE.md`
---

### 5.5. 💤 `session.idle`
```typescript
"session.idle": async () => {
  // Аудит console.log во всех отредактированных файлах
  for (const file of editedFiles) {
    const count = await $`grep -c "console\\.log" ${file}`;
    if (count > 0) {
      filesWithConsoleLogs.push(file);
    }
  }

  // Desktop уведомление (macOS)
  await $`osascript -e 'display notification "Task completed!"'`;

  // Очистка трекинга
  editedFiles.clear();
};
```

#### 🎯 Назначение:
- 🔍 Финальный аудит кода перед завершением
- 🔔 Уведомление пользователя о завершении задачи
- 🧹 Очистка временных данных
---

### 5.6. 🌍 `shell.env`
```typescript
"shell.env": async () => {
  const env = {
    ECC_VERSION: "1.8.0",
    PROJECT_ROOT: worktree,
    PACKAGE_MANAGER: detectedPM, // npm/yarn/pnpm/bun
    DETECTED_LANGUAGES: "typescript,go,python",
    PRIMARY_LANGUAGE: "typescript",
  };
  return env;
};
```

#### 🎯 Назначение:
- 📦 Автоматическое определение менеджера пакетов по lock-файлам
- 🌐 Определение используемых языков программирования
- 🔄 Передача контекста в shell-команды
---

### 5.7. 🧪 `experimental.session.compacting`
```typescript
"experimental.session.compacting": async () => {
  return {
    context: "# ECC Context...",
    compaction_prompt: "Focus on preserving: 1) Current task status...",
  };
};
```

#### 🎯 Назначение:
- 💾 Сохранение важного контекста при compaction
- 🤖 Указание AI, что сохранить при сжатии истории

---

### 5.8. 🔐 `permission.ask`

```typescript
"permission.ask": async (event) => {
  // Авто-одобрение read-only операций
  if (["read", "glob", "grep"].includes(event.tool)) {
    return { approved: true, reason: "Read-only operation" };
  }

  // Авто-одобрение форматтеров
  if (isFormatter(event.tool)) {
    return { approved: true, reason: "Formatter execution" };
  }

  // Авто-одобрение тестов
  if (isTestCommand(event.tool)) {
    return { approved: true, reason: "Test execution" };
  }

  // Остальное - на решение пользователя
  return { approved: undefined };
};
```

#### 🎯 Назначение:
- ✅ Автоматическое одобрение безопасных операций
- ⏱️ Сокращение необходимости ручных подтверждений

---

## 6. Управление профилями

### 🔧 Конфигурация через переменные окружения

```bash
# Выбор профиля
export ECC_HOOK_PROFILE=strict  # minimal | standard | strict

# Отключение конкретных хуков
export ECC_DISABLED_HOOKS="post:edit:format,pre:bash:tmux-reminder"
```

### 📊 Матрица доступности хуков

| Хук ID | minimal | standard | strict |
|--------|:-------:|:--------:|:------:|
| `post:edit:format` | ❌ | ❌ | ✅ |
| `post:edit:console-warn` | ❌ | ✅ | ✅ |
| `post:edit:typecheck` | ❌ | ❌ | ✅ |
| `pre:bash:git-push-reminder` | ❌ | ❌ | ✅ |
| `pre:write:doc-file-warning` | ❌ | ✅ | ✅ |
| `pre:bash:tmux-reminder` | ❌ | ❌ | ✅ |

---

## 7. Инструмент changed-files

Плагин предоставляет собственный инструмент для работы с изменёнными файлами:

```typescript
tool: {
  "changed-files": changedFilesTool
}
```

### 🚀 Возможности:

- 🌳 **Древовидное отображение** изменений
- 🔍 **Фильтрация по типу** (added/modified/deleted)
- 🔗 **Интеграция с git diff**

---

## 8. Преимущества системы

### 8.1. 👨‍💻 Для разработчика

| Преимущество | Описание |
|--------------|----------|
| ✅ | Автоматическое форматирование кода |
| ✅ | Раннее обнаружение `console.log` |
| ✅ | Проверка типов TypeScript |
| ✅ | Напоминания о code review |

### 8.2. 📁 Для проекта

| Преимущество | Описание |
|--------------|----------|
| ✅ | Контроль качества кода |
| ✅ | Предотвращение ненужной документации |
| ✅ | Автоматический аудит перед коммитом |
| ✅ | Интеграция с GitHub Actions |

### 8.3. 🤖 Для AI-ассистента

| Преимущество | Описание |
|--------------|----------|
| ✅ | Богатый контекст (языки, менеджер пакетов) |
| ✅ | Авто-одобрение безопасных операций |
| ✅ | Сохранение контекста при compaction |
| ✅ | Трекинг прогресса задач |

---

## 9. Заключение

Система плагинов **OpenCode** представляет собой продвинутую систему автоматизации, которая:

1. **🚀 Расширяет возможности** Claude Code с 3 до 20+ типов событий
2. **🔧 Адаптируется** к проекту через автоопределение технологий
3. **✅ Контролирует качество** кода на каждом этапе
4. **⚡ Упрощает работу** с автоматическими одобрениями
5. **💾 Сохраняет контекст** между сессиями

> 💡 **Это мощный инструмент для поддержания высокого качества кода и автоматизации рутинных задач разработки.**

---

*Документ сгенерирован для OpenCode ECC v1.8.0*
