### конфигурации `opencode.jsonc`

```
```


[[permission]] - opencode использует конфигурацию `permission`, чтобы решить, должно ли данное действие выполняться автоматически, запрашивать вас или блокироваться.



```json
{
  // Указываем схему для валидации и автодополнения в редакторе
  "$schema": "https://opencode.ai/config.json",

  // Основная модель для сложных задач
  "model": "opencode-go/qwen3.7-plus",
  "model": "lmstudio/openai/gpt-oss-20b",
  // Агент по умолчанию
  "default_agent": "build",

  // Модель для легких задач (генерация заголовков, суммаризация)
  "small_model": "openai/gpt-5.1-mini",
  "small_model": "opencode-go/qwen3.7-plus",
  // механизм для внедрения общих правил и контекста для всех агентов
  "instructions": [
	"instructions/INSTRUCTIONS.md",
  ],


  // Пример настройки MCP-сервера
  "mcp": {
    "servers": {
      "my-local-mcp": {
        "type": "local",
        "command": ["npx", "-y", "@my-org/mcp-server"],
        "enabled": true
      }
    }
  }
}
```

subagent
[[mode]] -   `primary` — основной агент (используется через Tab)  `subagent` — субагент (вызывается через `@`)

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
        }
      },
      "temperature": 0.1
    }
  }
}
```

Plugin [[plugin]]

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [

  ],
}
```

[[provider]] - 

```json
{
  // Указываем схему для валидации и автодополнения в редакторе
  "$schema": "https://opencode.ai/config.json",
  // Подключение локальной модели через LM Studio
  "provider": {
    "lmstudio": {
      // Указываем, что используем OpenAI-совместимый API
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        // Адрес, на котором запущен локальный сервер LM Studio
        "baseURL": "http://127.0.0.1:1234/v1"
      }
      // Список моделей можно не указывать, если вы используете плагин для авто-обнаружения
    }
  },
}
```


```json
{
  "$schema": "https://opencode.ai/config.json",
  // Пример настройки MCP-сервера
  "mcp": {
    "servers": {
      "my-local-mcp": {
        "type": "local",
        "command": ["npx", "-y", "@my-org/mcp-server"],
        "enabled": true
      }
    }
  }
}
```

MCP 
```json
{
  "$schema": "https://opencode.ai/config.json",

  "mcp": {
    "my-remote-mcp": {
      "type": "remote",
      "url": "https://huggingface.co/mcp",
      "enabled": true,
      "headers": {
        "Authorization": "{env:HF_TOKEN}"
      }
    },
    "gh_grep": {
      "type": "remote",
      "url": "https://mcp.grep.app"
    },
    "context7": {
      "type": "local",
      "command": [
        "npx",
        "@upstash/context7-mcp"
      ],
      "enabled": true
    },
    "playwright": {
      "type": "local",
      "command": [
        "npx",
        "@playwright/mcp@latest"
      ],
      "enabled": true
    },
    "filesystem": {
      "type": "local",
      "command": [
        "npx",
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "."
      ],
      "enabled": true
    },
    "sequential-thinking": {
      "type": "local",
      "command": [
        "npx",
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ],
      "enabled": true
    }
  },
  "permission": {
    "filesystem_*": "allow",
    "my-remote-mcp_*": "allow",
    "context7_*": "allow",
    "gh_grep_*": "allow",
    "playwright_*": "allow",
    "sequential-thinking_*": "allow"
  },
  "command": {}
}
```


Глобальные opencode.jsonc
```json
{

  "$schema": "https://opencode.ai/config.json",

  // Основная модель для сложных задач

  "model": "opencode-go/qwen3.7-plus",

  "default_agent": "build",

  // Модель для легких задач (генерация заголовков, суммаризация)

  "small_model": "opencode-go/qwen3.7-plus",

  "instructions": [],

  "plugin": [

    "opencode-lmstudio@latest"

  ],

  "permission": {

    "edit": "ask",

    "bash": "ask",

    "read": "allow",

    "webfetch": "allow",

    "external_directory": "ask" // Важно для безопасности: запрашивать доступ к путям вне проекта

  },

  // Настройки агентов

  "agent": {

    "build": {

      "description": "Primary coding agent for Python development work",

      "mode": "primary",

      "permission": {

        "edit": "allow",

        "read": "allow",

        "bash": "allow"

      }

    },

    "plan": {

      "description": "Planning agent for analyzing and strategizing",

      "mode": "primary",

      "model": "opencode-go/qwen3.7-plus",

      "permission": {

        "edit": "deny",

        "bash": "ask",

        "read": "allow"

      }

    }

  },

  "command": {},

  // Пример настройки MCP-сервера

  "mcp": {},

  // Подключение локальной модели через LM Studio

  "provider": {

    "lmstudio": {

      // Указываем, что используем OpenAI-совместимый API

      "npm": "@ai-sdk/openai-compatible",

      "name": "LM Studio (local)",

      "options": {

        // Адрес, на котором запущен локальный сервер LM Studio

        // "baseURL": "http://127.0.0.1:1234/v1"

        "baseURL": "http://192.168.0.101:1234/v1"

      },

      "models": {

        "openai/gpt-oss-20b": {

          "name": "GPT OSS 20B (local)"

        }

      }

    }

  }

}
```