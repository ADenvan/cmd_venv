# ГЛОБАЛЬНОЕ настройка MCP
- Путь к фаилу
    - C:\Users\ArDen\.opencode\
    - C:\Users\ArDen\AppData\Roaming\OpenCode\



# Как прописать MCP Server в проекте
- `https://opencode.ai/docs/ru/mcp-servers/`
    - .opencode/opencode.json - Путь к файлу конфигурации


# Аутентификация
- `https://opencode.ai/docs/ru/mcp-servers/#%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F`

- Команда mcp auth откроет ваш браузер для авторизации. После того как вы авторизуетесь, opencode надежно сохранит токены в `~/.local/share/opencode/mcp-auth.json`.

1. Отладка
- Если удаленный сервер MCP не может аутентифицироваться, вы можете диагностировать проблемы с помощью:
```bash
opencode mcp auth list
opencode mcp debug my-oauth-server
```
- Команда mcp debug показывает текущий статус аутентификации, проверяет соединение HTTP и пытается выполнить поток обнаружения OAuth.





--------------------------------------------
## huggingface.com - Установка удаленного сервера MCP
- Добавьте удаленные серверы MCP, установив для type значение "remote".
    - https://huggingface.co/mcp - РАботает и LM Studio БЕСПЛАТНО
    - https://www.testsprite.com/dashboard/settings/apikey - ПЛАТНЫЙ СЕРВИС с

```json
{
"my-remote-mcp": {
    "type": "remote",
    "url": "https://huggingface.co/mcp",
    "enabled": true,
    "headers": {
      "Authorization": "Bearer MY_API_KEY"
    }
  }
}
```
--------------------------------------------


--------------------------------------------
# context7 - API + Регистрация
- https://context7.com/dashboard
- https://github.com/upstash/context7
    - Контекст7 извлекает актуальную, версионно-специфичную документацию и примеры кода непосредственно из источника — и размещает их прямо в вашем запросе.

```json
{
"context7": {
    "type": "remote",
    "url": "https://mcp.context7.com/mcp",
    "headers": {
      "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
    }
  }
}
```
--------------------------------------------


--------------------------------------------
# testsprite.com - ПЛАТНЫЙ СЕРВИС С 21-03-26 был БЕСПЛАТНЫМ
## Локальные серверы
- https://www.testsprite.com/dashboard/settings/apikey

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "TestSprite": {
      "type": "local",
      "command": ["npx", "-y", "@testsprite/testsprite-mcp@latest"],
      "enabled": true,
      "environment": {
        "API_KEY": "my-api-key",
      }
    }
  }
}
```
--------------------------------------------
# gh_grep

```json
{
  "gh_grep": {
      "type": "remote",
      "url": "https://mcp.grep.app"
    }
}
```
--------------------------------------------
--------------------------------------------
--------------------------------------------
