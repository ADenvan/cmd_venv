

# ПРАВИЛ Инициализировать (AGENTS.md)
- `https://opencode.ai/docs/ru/rules/`

- OpenCode — системные подсказки (prompts) и рекомендации для агентов.
    - `https://translated.turbopages.org/proxy_u/en-ru.ru.7abe7e0f-69d55b36-fe2e815d-74722d776562/https/github.com/bgauryy/open-docs/blob/main/docs/opencode/05-system-prompts.md`
- Набор правил для OpenCode.
    - `https://github.com/affaan-m/everything-claude-code/blob/main/RULES.md`

**В проекте** - через команду /init в корне проекта.
- /inti is analyzing yor codebase... учти правила @docs/architecture-rules.md
    - новый файл `AGENTS.md`, будет набор правил.

**Глобальный** - ` ~/.config/opencode/AGENTS.md`

--------------------------------------------


--------------------------------------------
# Агенты и СубАгенты.
- `https://opencode.ai/docs/ru/agents/#markdown`
- ![Subagent](rodmap\Отчёт_SubAgent_Субаген.md)
    - ![model](rodmap\Анализ_строки_модели.md)
    - ![api_key.json](rodmap\Отчёт_файл_api-key.md)

--------------------------------------------


--------------------------------------------
# Skill
- `https://opencode.ai/docs/ru/skills/`

**Конфигурация проекта:** - `.opencode/skills/<name>/SKILL.md`
**Глобальная конфигурация:** - `~/.config/opencode/skills/<name>/SKILL.md.`
- Определите повторно используемое поведение с помощью определений SKILL.md
    - Конфигурация проекта:
--------------------------------------------

--------------------------------------------
# Plugins
- ![clode_code_vs_opencode](rodmap\plugin\Plugin_OpenCode.md)

- Структура папок и файлов плагина ECC
- ![architecture_tree](rodmap\plugin\ECC_PLUGINS_ARCHITECTURE_TREE.md)
--------------------------------------------

--------------------------------------------
# auth.json
- `https://opencode.ai/docs/ru/providers/`
- ДЛЯ ВЕРСИИ DESKTOP путь
    - C:\Users\ArDen\.local\share\opencode\auth.json
```json
{
  "lmstudio": {
    "type": "api",
    "key": "my-api-key"
  }
}
```
--------------------------------------------

--------------------------------------------
# .config/opencode/opencode.json
- C:\Users\ArDen\.config\opencode\opencode.json
```json
{

}
```
--------------------------------------------


--------------------------------------------
# C:\Users\ArDen\AppData\Roaming\npm
- Установлен agentic
    - npm install -g agentic-cli
--------------------------------------------


--------------------------------------------

--------------------------------------------
--------------------------------------------
--------------------------------------------
