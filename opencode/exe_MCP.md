# ГЛОБАЛЬНОЕ настройка MCP
- Путь к фаилу
    - C:\Users\ArDen\.opencode\
    - C:\Users\ArDen\AppData\Roaming\OpenCode\



# Как прописать MCP Server в проекте
## .opencode/opencode.json - Путь к файлу конфигурации

 - https://opencode.ai/docs/ru/mcp-servers/


--------------------------------------------
## Удаленные
- Добавьте удаленные серверы MCP, установив для type значение "remote".
    - https://huggingface.co/mcp - РАботает и LM Studio БЕСПЛАТНО
    - https://www.testsprite.com/dashboard/settings/apikey - ПЛАТНЫЙ СЕРВИС с

```json
"my-remote-mcp": {
      "type": "remote",
      "url": "https://huggingface.co/mcp",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer MY_API_KEY"
      }
    }
```
--------------------------------------------


--------------------------------------------
- https://context7.com/dashboard
- https://github.com/upstash/context7
    - Контекст7 извлекает актуальную, версионно-специфичную документацию и примеры кода непосредственно из источника — и размещает их прямо в вашем запросе.

```json
"context7": {
  "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
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
        "API_KEY": "sk-user-svJDGizWb2pzJTukkp2pVJXGBo-0xhWWdfSg0mZPNNVpnNgMKeThFF2l5nuNdjY4iNtVjZ1pzdF_T89INA9V6dA39W78HPesHjpve9dEsqyEQ6Uf8zK9Nm_tsLoZgi1IFnU",
      }
    }
  }
}
```
--------------------------------------------
