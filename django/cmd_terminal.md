# Выбор версии Django
![альтернативный текст](images\Django-version_.jpg)

# В терминале
```bash
django-admin               # Получаем список команд
django-admin startproject  # Создаем проект
django-admin startapp      # Создаем приложение
python manage.py runserver # Запускаем
```

# Создание доменного имени проекта.
```bash
django-admin startproject app # Создаем проект app
```
1. детекторе папки не зависит от названия app/app Это просто внешний каталог
2. Вариант с выбором виртуального окружения с уровня выше.
    - Open folder
![альтернативный текст](images\Django-venv-interpretator_.jpg)
```bash
python manage.py # Перечень команд для терминала в проекте
```

# Создание приложение команда терминала.
- Модуль с конкретной логикой (например, "Блог", "Магазин", "Пользователи"). Один проект может содержать много приложений.
```terminal
D:\Python-Project\Django\storehome_pyhs\config> python manage.py startapp main
```
```python
INSTALLED_APPS = [
    
    'main', # Регистрация нового приложения.
]
```
