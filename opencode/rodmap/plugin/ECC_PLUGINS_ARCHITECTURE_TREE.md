# Архитектурное дерево ECC Plugins

## Структура папок и файлов плагина ECC
```
📁 .opencode/
├── 📄 package.json
│   └── Описание: Зависимости плагина
│   └── Путь: .opencode/package.json
├── 📄 tsconfig.json
│   └── Описание: Конфигурация TypeScript
│   └── Путь: .opencode/tsconfig.json
├── 📄 opencode.json
│   └── Описание: Главная конфигурация OpenCode
│   └── Путь: .opencode/opencode.json
├── 📄 index.ts
│   └── Описание: Точка входа плагина (экспорт ECCHooksPlugin)
│   └── Путь: .opencode/index.ts
├── 📁 plugins/
│   ├── 📄 index.ts
│   │   └── Описание: Экспорт плагинов
│   │   └── Путь: .opencode/plugins/index.ts
│   ├── 📄 ecc-hooks.ts
│   │   └── Описание: Основная логика ECC хуков
│   │   └── Путь: .opencode/plugins/ecc-hooks.ts
│   └── 📁 lib/
│       └── 📄 changed-files-store.ts
│           └── Описание: Хранилище измененных файлов
│           └── Путь: .opencode/plugins/lib/changed-files-store.ts
├── 📁 tools/
│   ├── 📄 index.ts
│   │   └── Описание: Экспорт инструментов
│   │   └── Путь: .opencode/tools/index.ts
│   ├── 📄 changed-files.ts
│   │   └── Описание: Инструмент для работы с измененными файлами
│   │   └── Путь: .opencode/tools/changed-files.ts
│   ├── 📄 run-tests.ts
│   │   └── Описание: Инструмент запуска тестов
│   │   └── Путь: .opencode/tools/run-tests.ts
│   ├── 📄 check-coverage.ts
│   │   └── Описание: Инструмент проверки покрытия
│   │   └── Путь: .opencode/tools/check-coverage.ts
│   ├── 📄 security-audit.ts
│   │   └── Описание: Инструмент аудита безопасности
│   │   └── Путь: .opencode/tools/security-audit.ts
│   ├── 📄 format-code.ts
│   │   └── Описание: Инструмент форматирования кода
│   │   └── Путь: .opencode/tools/format-code.ts
│   ├── 📄 lint-check.ts
│   │   └── Описание: Инструмент проверки линтером
│   │   └── Путь: .opencode/tools/lint-check.ts
│   └── 📄 git-summary.ts
│       └── Описание: Инструмент git сводки
│       └── Путь: .opencode/tools/git-summary.ts
└── 📁 instructions/
    └── 📄 INSTRUCTIONS.md
        └── Описание: Инструкции для AI
        └── Путь: .opencode/instructions/INSTRUCTIONS.md
```
---

## Инструкция по копированию в другой проект

### Шаг 1: Создать структуру папок
Создать следующую структуру в корне целевого проекта:
```
.opencode/
├── plugins/
│   └── lib/
├── tools/
└── instructions/
```

### Шаг 2: Скопировать файлы
Скопировать каждый файл в соответствующую папку:
1. **Корень .opencode/** (3 файла):
   - `package.json` → `.opencode/package.json`
   - `tsconfig.json` → `.opencode/tsconfig.json`
   - `opencode.json` → `.opencode/opencode.json`
   - `index.ts` → `.opencode/index.ts`

2. **Папка plugins/** (2 файла + 1 в подпапке):
   - `plugins/index.ts` → `.opencode/plugins/index.ts`
   - `plugins/ecc-hooks.ts` → `.opencode/plugins/ecc-hooks.ts`
   - `plugins/lib/changed-files-store.ts` → `.opencode/plugins/lib/changed-files-store.ts`

3. **Папка tools/** (8 файлов):
   - `tools/index.ts` → `.opencode/tools/index.ts`
   - `tools/changed-files.ts` → `.opencode/tools/changed-files.ts`
   - `tools/run-tests.ts` → `.opencode/tools/run-tests.ts`
   - `tools/check-coverage.ts` → `.opencode/tools/check-coverage.ts`
   - `tools/security-audit.ts` → `.opencode/tools/security-audit.ts`
   - `tools/format-code.ts` → `.opencode/tools/format-code.ts`
   - `tools/lint-check.ts` → `.opencode/tools/lint-check.ts`
   - `tools/git-summary.ts` → `.opencode/tools/git-summary.ts`

4. **Папка instructions/** (1 файл):
   - `instructions/INSTRUCTIONS.md` → `.opencode/instructions/INSTRUCTIONS.md`

### Шаг 3: Установить зависимости
В папке `.opencode/` выполнить:
```bash
npm install
```

### Шаг 4: Собрать проект
В папке `.opencode/` выполнить:
```bash
npm run build
```
В результате должна появиться папка `.opencode/dist/`.

### Шаг 5: Подключить плагин
В корневом файле `opencode.json` целевого проекта добавить:
```json
{
  "plugin": [
    "./.opencode/plugins"
  ]
}
```

---
## Полный список файлов плагина (15 файлов)
| № | Путь к файлу | Описание |
|---|--------------|----------|
| 1 | `.opencode/package.json` | Зависимости и метаданные |
| 2 | `.opencode/tsconfig.json` | Конфигурация TypeScript |
| 3 | `.opencode/opencode.json` | Главная конфигурация OpenCode |
| 4 | `.opencode/index.ts` | Точка входа плагина |
| 5 | `.opencode/plugins/index.ts` | Экспорт плагинов |
| 6 | `.opencode/plugins/ecc-hooks.ts` | Основная логика хуков |
| 7 | `.opencode/plugins/lib/changed-files-store.ts` | Хранилище измененных файлов |
| 8 | `.opencode/tools/index.ts` | Экспорт инструментов |
| 9 | `.opencode/tools/changed-files.ts` | Инструмент измененных файлов |
| 10 | `.opencode/tools/run-tests.ts` | Инструмент запуска тестов |
| 11 | `.opencode/tools/check-coverage.ts` | Инструмент проверки покрытия |
| 12 | `.opencode/tools/security-audit.ts` | Инструмент аудита безопасности |
| 13 | `.opencode/tools/format-code.ts` | Инструмент форматирования кода |
| 14 | `.opencode/tools/lint-check.ts` | Инструмент проверки линтером |
| 15 | `.opencode/tools/git-summary.ts` | Инструмент git сводки |
| 16 | `.opencode/instructions/INSTRUCTIONS.md` | Инструкции для AI |

---

## Зависимости (из package.json)
```json
{
  "peerDependencies": {
    "@opencode-ai/plugin": ">=1.0.0"
  },
  "devDependencies": {
    "@opencode-ai/plugin": "^1.0.0",
    "@types/node": "^20.0.0",
    "typescript": "^5.3.0"
  },
  "dependencies": {
    "@opencode-ai/plugin": "1.4.2"
  }
}
```

---
## Проверка после установки
После сборки в папке `.opencode/dist/` должны быть созданы следующие файлы:
```
.opencode/dist/
├── index.js
├── index.d.ts
├── plugins/
│   ├── index.js
│   ├── index.d.ts
│   ├── ecc-hooks.js
│   ├── ecc-hooks.d.ts
│   └── lib/
│       ├── changed-files-store.js
│       └── changed-files-store.d.ts
└── tools/
    ├── index.js
    ├── index.d.ts
    ├── changed-files.js
    ├── changed-files.d.ts
    ├── run-tests.js
    ├── run-tests.d.ts
    ├── check-coverage.js
    ├── check-coverage.d.ts
    ├── security-audit.js
    ├── security-audit.d.ts
    ├── format-code.js
    ├── format-code.d.ts
    ├── lint-check.js
    ├── lint-check.d.ts
    ├── git-summary.js
    └── git-summary.d.ts
```
