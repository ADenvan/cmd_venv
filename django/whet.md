django templates
Контроллеры
Шаблоны
Шаблонные теги
Контекстные переменные
Наследование шаблонов
Разметка
Атрибут
В шаблоны Разметку
Создан суперпользователь
Фикстура
Теги включающиеся
Теги
Конвертеры
URL-Маршрутизация


Пространство имен
Сущность
Префикс
Статические фаилы
Фильтры
Контекст процессоры
Макросы
Кэширование
Ссылки
Формы
Модели
Миграции
Аутентификация
Сессии
Кросс-сайтовый скриптинг (XSS)
Кросс-сайтовый запрос межсайтового скриптинга (CSRF)



# -------------------------------------------
# Назначение фаилов в проекте
views.py: Обработка запросов и возвращение ответов.
urls.py: URL-маршруты проекта.
manage.py: Управление проектом (запуск сервера, миграции, создание приложений).
settings.py: Настройки проекта (база данных, приложения, middleware, шаблоны).
WSGI (wsgi.py): Стандарт для синхронных серверов (Gunicorn, uWSGI).
ASGI (asgi.py): Стандарт для асинхронных серверов (Daphne, Uvicorn), необходим для WebSockets и async views.
# -------------------------------------------


# -------------------------------------------
# Назначение папок в проекте
tamplatetags: Пользовательские теги шаблонов.
migrations: Миграции для базы данных.
templates: Шаблоны HTML.
static: Статические файлы (CSS, JS, изображения).
# -------------------------------------------



# -------------------------------------------
# Импорты в Django
```python
# folder urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# folder views.py
from django.http import HttpResponse
from django.shortcuts import render

# folder apps.py
from django.apps import AppConfig

# templatetags
from django import template

# from django.views.generic import ListView, DetailView
# from .models import Product
# from .forms import ProductForm

```
# -------------------------------------------




# -------------------------------------------
# Шаблоны Шаблоны используются для генерации HTML-кода на основе данных. Шаблоны в Django представлены в виде файлов с расширением .html. Шаблоны могут содержать HTML-разметку, а также специальные теги

Шаблонные теги {% url "index" %}
пространство имен {% url 'main:index' %}
Контекстные переменные {{}}
Наследование шаблонов {% block css %}{% endblock css %}
Расширение шаблонов {% extends "main/base.html" %}

```django
{%load static %}
{% static 'path/to/file' %}
{{ page_title }}

{% for link in footer_links %}
{% endfor %}

{% if is_authenticated %}
    {{ user }}
{% else %}
    {{ user }}
{% endif %}

{% block css %}{% endblock css %}

<p> {{ footer_links.0.name }} </p>
```



```html
{%load static %}
{% static 'path/to/file' %}
{{ page_title }}
<img src="{% static 'images/logo.png' %}" alt="Logo" />
<p> {{ footer_links.0.name }} </p>
```