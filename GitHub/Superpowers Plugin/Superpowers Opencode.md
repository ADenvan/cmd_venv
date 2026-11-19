- Superpowers - [https://github.com/obra/superpowers/tree/main](https://github.com/obra/superpowers/tree/main)
- Superpowers Opencode - [https://github.com/obra/superpowers/blob/main/docs/README.opencode.md](https://github.com/obra/superpowers/blob/main/docs/README.opencode.md?spm=a2ty_o01.29997173.0.0.68eec921PwNVWr&file=README.opencode.md)

# для Windows, через npm

#### Вариант А: Локальная установка (только для проекта `test_opencode`)
**Основной способ (попытка автоматической установки OpenCode):**
```bash
# 1. Создаем папку проекта и переходим в нее
New-Item -ItemType Directory -Force -Path "D:\Python-Project\app_try\test_opencode" | Out-Null
Set-Location -Path "D:\Python-Project\app_try\test_opencode"

# 2. Создаем файл конфигурации с ссылкой на Git-репозиторий
Set-Content -Path "opencode.json" -Value '{ "plugin": ["superpowers@git+https://github.com/obra/superpowers.git"] }' -Encoding UTF8
```
#### План Б (Гарантированный для Windows, через npm):

```bash
Set-Location -Path "D:\Python-Project\app_try\test_opencode"
# Скачиваем плагин системным npm в папку проекта
npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "D:\Python-Project\app_try\test_opencode"
# Прописываем локальный путь в конфигурацию
Set-Content -Path "opencode.json" -Value '{ "plugin": ["./node_modules/superpowers"] }' -Encoding UTF8
```


#### Вариант Б: Глобальная установка (для всех проектов текущего пользователя)

Этот метод использует рекомендованный в README обходной путь через `npm`, чтобы избежать ошибок пути к `git.exe` в среде Bun на Windows. Права администратора **не требуются**.
```bash
# 1. Создаем глобальную директорию конфигурации OpenCode
New-Item -ItemType Directory -Force -Path "$HOME\.config\opencode" | Out-Null

# 2. Устанавливаем плагин через системный npm в эту директорию
npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "$HOME\.config\opencode"
# В среде Windows PowerShell переменная `$env:USERPROFILE` является самым надежным и "родным"
npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "$env:USERPROFILE\.config\opencode"

# 3. Автоматически создаем или обновляем глобальный opencode.json с правильным путем
$configPath = "$HOME\.config\opencode\opencode.json"
$pluginPath = "~/.config/opencode/node_modules/superpowers"

if (Test-Path $configPath) {
    $config = Get-Content $configPath -Raw | ConvertFrom-Json
    if (-not $config.plugin) { $config | Add-Member -NotePropertyName "plugin" -NotePropertyValue @() }
    if ($config.plugin -notcontains $pluginPath) { $config.plugin += $pluginPath }
    $config | ConvertTo-Json -Depth 10 | Set-Content -Path $configPath -Encoding UTF8
} else {
    @{ plugin = @($pluginPath) } | ConvertTo-Json -Depth 10 | Set-Content -Path $configPath -Encoding UTF8
}
```

### Схема файловой структуры (ASCII)
Ниже показано, как будут расположены файлы на вашем ПК после выполнения установок.
#### 🌍 Глобальная структура (Уровень пользователя Windows)
Располагается в профиле пользователя (например, `C:\Users\ВашеИмя\.config\opencode\`).
В чате OpenCode вы используете встроенный инструмент `skill`.
- Чтобы увидеть список: _"`use skill tool to list skills`"_
- Чтобы активировать конкретный навык: _"use skill tool to load brainstorming"_ или _"use skill tool to load code-review"_
```txt
%USERPROFILE% (или $HOME)
└── .config/
    └── opencode/
        ├── opencode.json                 <-- Глобальный конфиг. Содержит строку: 
        │                                   ["~/.config/opencode/node_modules/superpowers"]
        │
        └── node_modules/
            └── superpowers/              <-- Физические файлы плагина, скачанные через npm
                ├── package.json          <-- Метаданные пакета
                ├── index.js              <-- Точка входа плагина (регистрирует хуки)
                └── skills/               <-- Библиотека готовых навыков (Skills)
                    ├── brainstorming/
                    │   └── SKILL.md      <-- Инструкция для ИИ по мозговому штурму
                    ├── architecture/
                    │   └── SKILL.md      <-- Инструкция по проектированию архитектуры
                    ├── code-review/
                    │   └── SKILL.md      <-- Чек-лист для проверки кода
                    └── ... (другие навыки из репозитория)
```


#### 📁 Локальная структура (Уровень конкретного проекта)
Располагается в вашей рабочей директории.
```txt
D:\Python-Project\app_try\test_opencode\
│
├── opencode.json                         <-- Локальный конфиг проекта.
│                                           Приоритет выше глобального!
│                                           Содержит: ["superpowers@git+https://..."] 
│                                           (или ["./node_modules/superpowers"], если использовался План Б)
│
├── .opencode/                            <-- (Опционально) Папка для ВАШИХ собственных навыков
│   └── skills/
│       └── my-python-rules/              <-- Пример вашего кастомного навыка
│           └── SKILL.md                  <-- Ваши личные правила для ИИ в этом проекте
│
├── main.py                               <-- Ваши файлы проекта
└── requirements.txt
```

#### Примеры использования в реальном проекте:

1. **Начало новой фичи (Brainstorming/Architecture):**
    - _Действие:_ Вы пишете: "`use skill tool to load architecture`". Затем описываете: "Мне нужно добавить аутентификацию через JWT в мой Python-проект".
    - _Результат:_ ИИ не просто выдаст код, а задаст уточняющие вопросы о хранении токенов, сроках действия и структуре БД, следуя лучшим практикам, заложенным в скилле.
2. **Рефакторинг или Code Review:**
    - _Действие:_ "`use skill tool to load code-review`". Выделяете фрагмент кода и просите: "Проверь этот код на уязвимости и соответствие PEP-8".
    - _Результат:_ ИИ применит строгий чек-лист из скилла, а не даст поверхностный ответ.
3. **Написание тестов:**
    - _Действие:_ "`use skill tool to load testing`".
    - _Результат:_ ИИ сгенерирует тесты, покрывающие граничные случаи (edge cases), о которых вы могли забыть, потому что скилл содержит инструкцию "всегда проверять null, пустые строки и сетевые ошибки".



Так я не понимаю из кого инструмента устанавливать этой командой из vscode с правами доступа для запуска npm. если из vscode то какой командой лучше всего `npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "$env:USERPROFILE\.config\opencode"` или `npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "$HOME\.config\opencode"`