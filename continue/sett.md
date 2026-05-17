# Локальная установка config.json

```json
{
    "models": [
        {
            "title": "Ollama - Qwen 2.5 Coder 7b",
            "model": "qwen2.5-coder:7b",
            "provider": "ollama"
        },
        {
            "apiKey": " { MY_API_KEY } ",
            "title": "Mistral - Codestral",
            // "model": "codestral-latest",
            "model": "ministral-8b-2410",
            "provider": "mistral"
        }
    ],
    "allowAnonymousTelemetry": false
}
```

# Настройка автозаполнение
```json
{
    "tabAutocompleteModel": {
        "title": "Mistral - Codestral",
        "provider": "mistral",
        "model": "codestral-latest",
        "apiKey": " { MY_API_KEY }",
        "completionOptions": {
            "temperature": 0.2,
            "maxTokens": 128
        }
    },
}
```
#
```json
{
    "tabAutocompleteModel": {
        "apiKey": "http://localhost:11434",
        "title": "Ollama - Qwen 2.5 Coder 7b",
        "provider": "ollama",
        "model": "qwen2.5-coder:7b",
        // "model": "deepseek-r1:8b",
        "completionOptions": {
            "temperature": 0.1,
            "maxTokens": 128
        },
    }
}
```


# LM Studio
1. НЕ ПРОВЕРЕННО
```json
{
    "models": [
        {
            "title": "LM Studio Local json",
            "provider": "openai-compatible",
            "model": "openai/gpt-oss-20b",
            "apiBase": "http://127.0.0.1:1234",
            "contextLength": 4096,
            "completionOptions": {
                "temperature": 0.7,
                "maxTokens": 1024
            }
        }
    ],
    "tabAutocompleteModel": {
        "title": "LM Studio Auto - json",
        "provider": "openai-compatible",
        "model": "openai/gpt-oss-20b",
        "apiBase": "http://127.0.0.1:1234"
    },
}
```