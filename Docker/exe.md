
# CMD

```bash
docker images        #
docker images --tree # Чтобы посмотреть все доступные образы (включая промежуточные слои):
docker ps            #
```


# Установка Ollama
https://hub.docker.com/r/ollama/ollama

1. Установил контейнер - Start the container
    - docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

```bash
docker exec ollama                           # Преходим в контейнер. модели
docker exec ollama ollama ls                 # Выводит список моделей, установленных в контейнере
docker exec ollama ollama run deepseek-r1:8b # Запускает контейнер с моделью.
docker exec ollama ollama run qwen2.5-coder:7b # Запускает контейнер с моделью.
```

- model
    - deepseek-r1:8b
    - qwen2.5-coder:7b

```bash
```


# Установка Open WebUI для использование UI
https://github.com/open-webui/open-webui

- Используем команду с поддержкой Nvidia GPU
    - docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda


# Векторная база данных
