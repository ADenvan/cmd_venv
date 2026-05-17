
1.
Плагины OpenCode представляют собой систему автоматизации на основе хуков (hook-based automation). Они являются расширением стандарта Claude Code, но с более продвинутыми возможностями.


2. Структура плагинов
.opencode/plugins/
├── index.ts              # Главный экспорт
├── ecc-hooks.ts          # Основная логика плагина
└── lib/
    └── changed-files-store.ts  # Хранилище изменённых файлов

собери весь Отчет: Плагины OpenCode (ECC - Everything Claude Code)
По всем пунктам с 1 по 9. создай фаил с Отчетам в корне проекта.


📦 План миграции ECC плагина в другой проект
Обзор структуры плагина
📁 .opencode/
├── 📄 package.json              # Зависимости и метаданные
├── 📄 tsconfig.json            # Конфигурация TypeScript
├── 📄 opencode.json            # Главная конфигурация OpenCode
├── 📄 index.ts                 # Точка входа плагина
│
├── 📁 plugins/
│   ├── 📄 index.ts             # Экспорт плагинов
│   ├── 📄 ecc-hooks.ts        # Основная логика хуков
│   └── 📁 lib/
│       └── 📄 changed-files-store.ts  # Хранилище изменений
│
├── 📁 tools/
│   ├── 📄 index.ts            # Экспорт инструментов
│   ├── 📄 changed-files.ts    # Инструмент для изменённых файлов
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
└── 📁 skills/                 # (опционально, 11 навыков)







