# 📋 Отчёт: Конфигурационный файл `api-key.json`

---

## 📍 Где находится файл

**Путь:** `~/.config/opencode/api-key.json`

| Тип конфигурации | Путь |
| --- | --- |
| **Глобальная** | `~/.config/opencode/api-key.json` — доступно всем проектам |
| **Проектная** | `.opencode/api-key.json` — только для текущего проекта |
| **Локальная** | Можно создать вручную в любом месте, но **рекомендуется** использовать стандартный путь |

---

## 🤔 Автоматическое или ручное создание?

| Сценарий | Создаётся автоматически? |
| --- | --- |
| **Облачные API** (Anthropic, OpenAI, Google) | ✅ Да — при настройке внешнего API |
| **Локальные модели** (Ollama, LM Studio) | ❌ Нет — нужно создать вручную или указать в конфиге |
| **Без API** (локальные модели) | ⚠️ Можно не создавать — используйте пустой ключ |

---

## 📝 Структура файла (JSON)

### 1\. Для облачных API (Anthropic, OpenAI, Google)

```json
{
  "anthropic": "sk-anthropic-api-key-value",
  "openai": "sk-openai-api-key-value",
  "google": "google-gemini-api-key-value",
  "mistral": "mistral-api-key-value",
  "cohere": "cohere-api-key-value"
}
```

### 2\. Для локальных моделей (Ollama)

```json
{
  "anthropic": "http://localhost:11434/api/generate",
  "ollama": "http://localhost:11434"
}
```

**Или для LM Studio:**

```json
{
  "local": "http://localhost:1234/v1/chat/completions",
  "ollama": "http://localhost:11434"
}
```

---

## 🛠️ Как создать файл

### Способ 1: Автоматическое создание

```bash
# Первичный запуск OpenCode с настройкой внешнего API
opencode init
```

**В процессе настройки будет запросить API-ключи** для подключения к облачным моделям.

---

### Способ 2: Ручное создание

**Для облачных API:**

```bash
mkdir -p ~/.config/opencode
```

**Создайте файл:**

```bash
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "anthropic": "sk-1234567890abcdef",
  "openai": "sk-1234567890abcdef",
  "google": "gcp-gemini-key"
}
EOF
```

**Для локальных моделей (Ollama):**

```bash
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "anthropic": "http://localhost:11434/api/generate",
  "ollama": "http://localhost:11434"
}
EOF
```

**Для LM Studio:**

```bash
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "ollama": "http://localhost:1234/v1/chat/completions"
}
EOF
```

**Или пустой файл для локальных моделей без внешних API:**

```bash
cat > ~/.config/opencode/api-key.json << 'EOF'
{}
EOF
```

**Для локальных моделей (Ollama):**

```bash
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "ollama": "ollama:llama3"
}
EOF
```

---

## 🎯 Параметры для разных сценариев

### Сценарий 1: Только локальные модели (Ollama)

```json
{
  "ollama": "http://localhost:11434"
}
```

**Или:**

```json
{
  "ollama": "ollama:llama3",
  "local": true
}
```

---

### Сценарий 2: Локальные модели (LM Studio)

```json
{
  "ollama": "http://localhost:1234/v1/chat/completions"
}
```

---

### Сценарий 3: Смешанное использование

```json
{
  "anthropic": "sk-anthropic-key",
  "ollama": "http://localhost:11434",
  "openai": "sk-openai-key"
}
```

---

## 🔑 Обязательные параметры

| Параметр | Тип | Описание | Обязательно? |
| --- | --- | --- | --- |
| **Provider name** | string | Название провайдера (`anthropic`, `openai`, `ollama`, `google`) | ✅ Да |
| **API Key** | string | Ключ или URL для локального API | ❌ Нет |
| **Model name** | string | Имя модели для локального API | ❌ Нет |

---

## 📋 Примеры конфигураций

### Для Ollama (локальная работа)

```json
{
  "ollama": "ollama:llama3.2",
  "local": true
}
```

### Для LM Studio

```json
{
  "ollama": "http://localhost:1234/v1/chat/completions"
}
```

### Для внешних API

```json
{
  "anthropic": "sk-anthropic-api-key",
  "openai": "sk-openai-api-key",
  "google": "gcp-gemini-api-key",
  "mistral": "mistral-api-key"
}
```

---

## ⚙️ Настройка в агентах для локальных моделей

Если в `api-key.json` указан локальный адрес, то в конфигурации агентов:

```json
{
  "agent": {
    "local-model": {
      "mode": "subagent",
      "model": "ollama/llama3",
      "tools": {
        "write": true,
        "edit": true,
        "bash": "ask"
      },
      "temperature": 0.3
    }
  }
}
```

---

## 🔐 Безопасность

**Рекомендации:**

1.  **Добавьте файл в** `.gitignore`

    ```bash
    echo ".config/opencode/api-key.json" >> .gitignore
    ```

2.  **Используйте переменные окружения**

    ```bash
    cat > ~/.config/opencode/api-key.json << EOF
    {
      "anthropic": "\$ANTHROPIC_API_KEY"
    }
    EOF

    export ANTHROPIC_API_KEY=your-key-value
    ```

3.  **Правом доступа**

    ```bash
    chmod 600 ~/.config/opencode/api-key.json
    ```


---

## 📌 Практические примеры

### 1\. Быстрое создание для локальных моделей

```bash
mkdir -p ~/.config/opencode
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "ollama": "http://localhost:11434"
}
EOF
```

### 2\. Для LM Studio

```bash
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "ollama": "http://localhost:1234/v1/chat/completions"
}
EOF
```

### 3\. Пустой файл (без внешних API)

```bash
touch ~/.config/opencode/api-key.json
echo "{}" > ~/.config/opencode/api-key.json
```

---

## 🚀 Рекомендация

**Для локальных моделей (Ollama/LM Studio):**

1.  **Создайте файл** вручную в `~/.config/opencode/api-key.json`

2.  **Укажите URL** локального API или используйте пустой файл

3.  **Настройте агентов** с `model: "ollama/llama3"` или аналогичным

4.  **Используйте локальный режим** (`local: true`) в конфигурации


**Пример конфигурации:**

```bash
mkdir -p ~/.config/opencode
cat > ~/.config/opencode/api-key.json << 'EOF'
{
  "ollama": "http://localhost:11434"
}
EOF
```

---

**Дата создания отчёта:** 6 апреля 2026<br>**Версия документации:** Актуальная (2026)

🎉 Успешно создан отчёт по `api-key.json`!