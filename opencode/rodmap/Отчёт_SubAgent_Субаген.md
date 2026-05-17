## 📋 Отчёт: SubAgent (Субагент) в OpenCode
---
### 🎯 Что такое Субагент
**Субагенты** — это специализированные ИИ-помощники, которых первичные агенты могут вызывать для выполнения определённых задач. Субагенты работают как специализированные инструменты для конкретных сценариев.

**Ключевые особенности:**
-   Вызываются автоматически первичными агентами при необходимости
-   Могут быть вызваны вручную через упоминание с `@`
-   Работают в отдельных дочерних сессиях
-   Имеют специализированный доступ к инструментам

---

### 🚀 Зачем нужны Субагенты
| Сценарий | Пример субагента | Цель |
| --- | --- | --- |
| **Параллельная работа** | General | Запуск нескольких единиц работы одновременно |
| **Исследование кода** | Explore | Поиск файлов, анализ кода без изменений |
| **Безопасность** | Security Auditor | Поиск уязвимостей и безопасности |
| **Документация** | Docs Writer | Создание и поддержка документации |
| **Отладка** | Debugger | Исследование и анализ ошибок |

---

### 🛠️ Встроенные субагенты
- `https://opencode.ai/docs/ru/agents/#%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-general`

| Субагент | Режим | Доступ к инструментам | Назначение |
| --- | --- | --- | --- |
| **General** | subagent | Полный (кроме задач) | Многоэтапные задачи, параллельная работа |
| **Explore** | subagent | Только чтение | Быстрый поиск по кодовой базе |

---

### ⚙️ Как настроить Субагента
- `https://opencode.ai/docs/ru/agents/#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0`
#### Способ 1: JSON-конфигурация

**Файл:** `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "security-auditor": {
      "description": "Audit security and identify vulnerabilities",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "tools": {
        "write": false,
        "edit": false,
        "bash": "ask"
      },
      "permission": {
        "bash": {
          "*": "deny",
          "git diff": "allow",
          "git log*": "allow"
        }
      },
      "temperature": 0.1
    }
  }
}
```

#### Способ 2: Markdown-файл
- `https://opencode.ai/docs/ru/agents/#markdown`
**Глобальная папка:** `~/.config/opencode/agents/`

**Папка проекта:** `.opencode/agents/`

**Файл:** `review.md`

```markdown
---
description: "Reviews code for quality and best practices"
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
permission:
  edit: deny
  bash:
    "*": ask
    "git diff": allow
---
You are in code review mode. Focus on:
- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations
Provide constructive feedback without making direct changes.
```

**Имя файла = имя агента**<br>Например: `review.md` → агент `review`

---

### 📝 Основные параметры конфигурации

| Параметр | Тип | Описание |
| --- | --- | --- |
| **description** | required | Описание назначения агента (обязательно) |
| **mode** | primary / subagent / all | Определяет тип агента |
| **model** | string | Идентификатор модели (например, `anthropic/claude-sonnet-4-20250514`) |
| **temperature** | 0.0-1.0 | Случайность ответов (низкое = детерминированное) |
| **tools** | object | Доступ к инструментам (write, edit, bash, etc.) |
| **permission** | object | Разрешения на операции (ask/allow/deny) |
| **color** | string | Цвет отображения в UI |
| **hidden** | boolean | Скрыть из меню автозаполнения `@` |
| **steps** | number | Максимальное количество шагов |
| **reasoningEffort** | low/medium/high | Усилия рассуждения (для некоторых моделей) |

---

### 🔑 Ключевые параметры

#### `description` (обязательно)

Краткое описание того, что делает агент и когда его использовать.

```json
"description": "Performs security audits and identifies vulnerabilities"
```

#### `mode`
Определяет тип агента:
-   `primary` — основной агент (используется через Tab)
-   `subagent` — субагент (вызывается через `@`)
-   `all` — доступен как основной и субагент


#### `model`
Используемая модель ИИ:
```json
"model": "anthropic/claude-haiku-4-20250514"
```

По умолчанию субагенты используют модель основного агента.

#### `temperature` (0.0-1.0)
Контролирует случайность ответов:
-   **0.0-0.2** — детерминированные ответы (подходит для аудита безопасности)
-   **0.3-0.5** — сбалансированные (общие задачи разработки)
-   **0.6-1.0** — творческие (мозговой штурм, исследование)


#### `tools` Контроль доступных инструментов:
```json
"tools": {
  "write": false,
  "edit": false,
  "bash": true
}
```

#### `permission` Разрешения на операции:
-   `ask` — запросить подтверждение
-   `allow` — разрешить все операции
-   `deny` — отключить инструмент


---

### 🔐 Управление разрешениями

#### Разрешения bash
```json
"permission": {
  "bash": {
    "*": "ask",
    "git status*": "allow",
    "git push": "ask"
  }
}
```

Поддерживаются glob-паттерны для группирования команд.

#### Запрет выполнения операций
```json
"permission": {
  "edit": "deny"
}
```

#### Запрет запуска субагентов через инструмент задач
```json
"permission": {
  "task": {
    "*": "deny",
    "orchestrator-*": "allow",
    "code-reviewer": "ask"
  }
}
```

---

### 🎨 Визуализация и скрытие

#### Цвет отображения
```json
"color": "#FF5733"  // шестнадцатеричный цвет
"color": "primary"  // цвет темы
```

Возможные цвета: `primary`, `secondary`, `accent`, `success`, `warning`, `error`, `info`

#### Скрытие из меню @

```json
"hidden": true
```
Подходит для внутренних субагентов, которые должны вызываться только программно через инструмент Tasks.

---

### 🎯 Примеры использования

#### 1\. Агент документации
```json
{
  "agent": {
    "docs-writer": {
      "description": "Writes and maintains project documentation",
      "mode": "subagent",
      "tools": {
        "write": true,
        "bash": false
      }
    }
  }
}
```

#### 2\. Аудитор безопасности

```json
{
  "agent": {
    "security-auditor": {
      "description": "Performs security audits and identifies vulnerabilities",
      "mode": "subagent",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

#### 3\. Быстрый анализ кода

```json
{
  "agent": {
    "quick-thinker": {
      "description": "Fast reasoning with limited iterations",
      "prompt": "You are a quick thinker. Solve problems with minimal steps.",
      "steps": 5,
      "temperature": 0.3
    }
  }
}
```

---

### 📡 Взаимодействие

#### Автоматический вызов
Основной агент автоматически вызывает субагента при необходимости.

#### Ручной вызов
```text
@general help me search for this function
```

#### Навигация между сессиями
```text
<Leader>+Right  — переход к следующему (родитель → дочерний1 → дочерний2 → …)
<Leader>+Left   — переход к предыдущему (родитель ← дочерний1 ← дочерний2 ← …)
```

---

### 📌 Создание нового субагента

```bash
opencode agent create
```

Интерактивная команда, которая:
1.  Спрашивает, где сохранить агента (глобально или в проекте)
2.  Запрашивает описание назначения агента
3.  Создает системный промпт и идентификатор
4.  Позволяет выбрать доступные инструменты
5.  Создает файл Markdown с конфигурацией


---

### 🌐 Варианты использования

| Сценарий | Рекомендация |
| --- | --- |
| **Полная разработка** | Агент Build (все инструменты включены) |
| **Анализ без изменений** | Агент Plan (все инструменты disabled) |
| **Поиск файлов** | Субагент Explore |
| **Мультизадачность** | Субагент General |
| **Безопасность** | Отключить write/edit/bash |

---

### ⚠️ Важные примечания
1.  `description` **обязателен** — без описания агент не будет работать
2.  `hidden: true` применяется только к субагентам (`mode: subagent`)
3.  **Подстановочные знаки в разрешениях** — последнее правило имеет приоритет
4.  **Прямой вызов через** `@` — доступен всегда, даже если запретить через `permission.task`
5.  `reasoningEffort` — специфичен для моделей OpenAI
6.  **Поля** `maxSteps` **устарели** — используйте `steps`


---

### 🔗 Дополнительные ресурсы
-   [Документация OpenCode](https://opencode.ai)
-   [GitHub репозиторий](https://github.com/anomalyco/opencode)
-   [Discord сообщество](https://opencode.ai/discord)


---

**Дата создания отчёта:** 6 апреля 2026<br>**Версия документации:** Актуальная (2026)

🎉 Успешно создан отчёт по SubAgent в OpenCode!