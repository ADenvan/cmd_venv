
Убедиться что 
# Первые команды
### Локальные
```bash
# 1. Создать и перейти в каталог проекта
New-Item -ItemType Directory -Force -Path "D:\Python-Project\app_try\test_opencode"
Set-Location "D:\Python-Project\app_try\test_opencode"

# 2. Установить Graphify
uv tool install graphifyy
# Обновить
uv tool update-shell

# 3. Проверить установку
graphify --version

# 4. Зарегистрировать skill для OpenCode (проектно)
graphify install --platform opencode --project

# 5. Собрать граф
graphify extract .

# 6. Проверить результат
Get-ChildItem graphify-out
```

### Глобальные (если применимо)

```bash
# Только если OpenCode поддерживает ~/.agents/skills/
graphify install --platform agents
# Проверка
Test-Path "$env:USERPROFILE\.agents\skills\graphify\SKILL.md"
```
**Не выполняйте глобальную установку, пока не убедитесь, что OpenCode читает skills из `%USERPROFILE%\.agents\skills\`.**


### 8. Текстовые деревья ASCII

**Ожидаемое дерево после локальной установки и первого запуска** (в `D:\Python-Project\app_try\test_opencode`):
```txt
D:\Python-Project\app_try\test_opencode\
├── .agents\
│   └── skills\
│       └── graphify\
│           ├── SKILL.md
│           └── references\
├── AGENTS.md               (создан или обновлен для OpenCode, раздел "Make your assistant always use the graph")
└── graphify-out\           (появляется после выполнения "graphify .", раздел "Get started")
    ├── graph.html
    ├── GRAPH_REPORT.md
    └── graph.json
```

**Ожидаемое дерево после глобальной установки** (в профиле пользователя Windows):
```txt
%USERPROFILE%\.agents\skills\graphify\   (или аналогичный глобальный каталог для OpenCode)
├── SKILL.md
└── references\
```
_Обоснование:_ Раздел **Install** указывает, что глобальные установки нацелены на пользовательский каталог `~/.agents/skills/` (или специфичный для платформы глобальный конфиг).

**Контрольный список для локальной конфигурации:**

- `uv` установлен и доступен в PATH.
- `graphify --version` возвращает версию (например, `0.9.85`).
- В `D:\Python-Project\app_try\test_opencode` существует каталог `.agents\skills\graphify\` или файл `AGENTS.md`.
- Сгенерирована папка `graphify-out\` с файлом `graph.json`.

**Контрольный список для глобальной конфигурации:**

- Команда `graphify install --platform opencode` выполнена без ошибок.
- Навык доступен для OpenCode CLI в любом каталоге (файлы присутствуют в глобальном профиле пользователя, например, `%USERPROFILE%\.agents\skills\`).


### Активация и первый запуск
Откройте терминал VS Code (PowerShell) и убедитесь, что вы находитесь в `D:\Python-Project\app_try\test_opencode`.
```bash
/graphify .
```
**Пояснение:** Подтверждено разделом **Common commands** README (`/graphify . # build graph for current folder`). Символ `/` используется внутри AI-ассистента, а в терминале PowerShell вызывается непосредственно исполняемый файл `graphify` с указанием текущей директории `.`.  
**Ожидаемый результат проверки:** Создание директории `graphify-out/` с тремя файлами: `graph.html`, `GRAPH_REPORT.md` и `graph.json` (как описано в разделе **Get started**).