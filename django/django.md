# Структура проекта описание деректорскии проекта и файлов django project
my_project/                  # 📂 Корневая директория проекта
├── .env                     # 🔒 Секреты (SECRET_KEY, DB_PASSWORD)
├── .gitignore               # 🚫 Игнорирование мусора (venv, __pycache__, db.sqlite3)
├── manage.py                # ⚙️ Главная утилита управления Django
├── requirements.txt         # 📦 Зависимости (библиотеки)
├── db.sqlite3               # 💾 Файл базы данных (локально)
├── media/                   # 🖼️ Пользовательский контент (аватарки, загрузки)
├── static/                  # 🎨 Глобальная статика (CSS, JS, шрифты)
│
├── config/                  # ⚙️ Конфигурация ПРОЕКТА (настройки)
│   ├── __init__.py          # 📄 Делает папку пакетом Python
│   ├── asgi.py              # 🚀 Асинхронный сервер (WebSockets, HTTP2)
│   ├── settings.py          # 🧠 Настройки (БД, приложения, middleware)
│   ├── urls.py              # 🗺️ Главные маршруты (роутинг)
│   └── wsgi.py              # 🐍 Синхронный сервер (стандарт для продакшена)
│
└── main/                    # 📦 Приложение (Бизнес-логика)
    ├── __init__.py
    ├── admin.py             # 👤 Настройка админ-панели
    ├── apps.py              # 🏷️ Мета-данные приложения
    ├── models.py            # 🗄️ Модели данных (Таблицы БД)
    ├── views.py             # 👁️ Логика (Обработка запросов)
    ├── urls.py              # 🔗 Маршруты внутри приложения
    ├── tests.py             # 🧪 Автотесты
    ├── migrations/          # 📜 История изменений БД (автоматически)
    │   └── __init__.py
    └── templates/           # 📄 HTML-шаблоны (рекомендуется хранить тут)
        └── main/
            ├── index.html
            └── base.html

1. manage.py
- Утилита командной строки
    - Через него запускают сервер (runserver), миграции (migrate), создают суперпользователя. Не удалять!

2. .env
- Переменные окружения
    - Храните тут SECRET_KEY, пароли от БД, ключи API. Никогда не коммитьте в Git!

3. .gitignore
- Фильтр для Git
    - Обязательно добавьте: __pycache__/, *.pyc, .env, db.sqlite3, venv/.

4. requirements.txt
- Зависимости
    - Генерируется командой pip freeze > requirements.txt. Нужно для установки проекта на сервер.
Приложение vs Проект:

5. media/
- Пользовательские файлы
    - Сюда сохраняются файлы, загруженные через формы (фото профиля, документы).

6. static/
- Статика проекта
    - CSS, JS, изображения интерфейса, которые не меняются пользователями.



- Проект
    - (config/): Глобальные настройки, одна база данных, общие URL.
- Приложение
    - (main/): Модуль с конкретной логикой (например, "Блог", "Магазин", "Пользователи"). Один проект может содержать много приложений.





# Подробное описание Папка конфигурации (config/)
- Эта папка создается командой django-admin startproject config .. Она управляет всем проектом целиком.


## 1. __pycache__ - кэш файлы
- Директория __pycache__ содержит скомпилированные байт-код файлы. Она создается автоматически. Никогда не загружайте её в репозиторий. Убедитесь, что она есть в .gitignore.


## 2. __init__.py - инициализация пакета / Пакет связанных между собой фаилов.
- Пустой файл, который говорит Python, что эту папку следует рассматривать как пакет.


## 3. asgi.py - асинхронный сервер для взаимодействия с веб-сервером и приложением.
- ASGI (asgi.py): Стандарт для асинхронных серверов (Daphne, Uvicorn), необходим для WebSockets и async views.


## 4. settings.py - настройки проекта
```python
from pathlib import Path # Импортируем класс Path из модуля pathlib для работы с путями
BASE_DIR = Path(__file__).resolve().parent.parent # путь к папке проекта app. Путь к корневой папке проект
DEBUG = True # Для отморожение отладочной информации.
ALLOWED_HOSTS = ['*'] # Список разрешенных хостов для доступа к приложению. ['*'] -Данное приложение может работать на разных хостах.

INSTALLED_APPS = [ # Список подключенных приложений
    # Стандартные приложения Django
    'django.contrib.admin',       # Админ-панель
    'django.contrib.auth',        # Система аутентификации
    'django.contrib.contenttypes',# Система типов контента
    'django.contrib.sessions',    # Сессии
    'django.contrib.messages',    # Система сообщений
    'django.contrib.staticfiles',# Управление статикой

    # Сторонние библиотеки
    'rest_framework',             # Django REST Framework (если используется API)
    'rest_framework.authtoken',   # Токенная аутентификация

    # Ваши приложения
    'app',                        # Простое подключение
    # 'app.apps.AppConfig',      # Подключение через конфиг (рекомендуется для настройки)


]
MIDDLEWARE = [ #  Обработчики запросов/ответов
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', # Часто забываемый, но важный
    'django.middleware.csrf.CsrfViewMiddleware', # Защита от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'app.urls' # Указывает на файл URL-маршрутов для приложения
```


## 5. urls.py - Главный маршрутизатор. Распределяет запросы по приложениям.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ # Список маршрутов приложения
    path('admin/', admin.site.urls), # Маршрут для админ-панели
    path('', include('main.urls', namespace='main')) # namespace='main' для избежания конфликтов имен URL-адресов


]

```


## 6. wsgi.py - конфигурация WSGI для развертывания приложения на веб-сервере.
- WSGI (Web Server Gateway Interface) - стандарт взаимодействия между веб-сервером и веб-прилож

```python
application = get_wsgi_application() - создание приложения WSGI
```
-------------------------------------------




-------------------------------------------
# Подробное описание Папка приложения (main/)
![альтернативный текст](images\Машршрут-django.png)

- Приложения создаются командой python manage.py startapp main. Одно приложение = одна логическая единица (например: "Блог", "Магазин", "Пользователи").


## 1. migrations/ - миграции базы данных для приложения.
- Папка с историей изменений базы данных.
    - ⚠️ Важно: Никогда не редактируйте файлы внутри вручную (кроме сложных случаев). Они генерируются командой python manage.py makemigrations.
    - Файл __init__.py внутри обязателен, чтобы Python видел папку как пакет.

## 2. admin.py - настройка админ-п интерфейса для приложения.
- Необходим для регистрации админ панели. или настройки отображения моделей в админке.
- Регистрация моделей для управления через интерфейс /admin.
    - Зачем: Чтобы менеджеры могли добавлять товары/статьи без доступа к коду.

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
```


## 3. apps.py - конфигурация приложения конкретного приложения.
- Конфигурация приложения.
    - Зачем: Обычно здесь меняют только verbose_name (человекочитаемое имя приложения, которое видно в админке).


## 4. models.py - определение моделей базы данных для приложения.
- Создаются специальные классы то какие таблицы и какая информация в них хранится.
- Описание структуры базы данных на языке Python (ORM).
    - Зачем: Вы создаете классы, а Django сам создает таблицы в БД.

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```


## 5. tests.py - тесты для приложения.
- Тесты для проверки корректности работы приложения.
- Автотесты.
    - Зачем: Проверка логики перед выпуском. Позволяет избегать регрессий (когда новая функция ломает старую).
-------------------------------------------




-------------------------------------------
## 6. views.py - обработка HTTP-запросов и формирование ответов.
- Здесь происходит магия. Функция или класс, который принимает запрос и возвращает ответ.
    - Зачем: Получает данные из models, обрабатывает их и отдает в template.
    - Типы:
        - FBV (Function Based Views): Обычные функции.
        - CBV (Class Based Views): Классы (генерики), удобнее для CRUD операций.
```python
from django.http import HttpResponse
from django.shortcuts import render

# Контроллер главной страницы.
# Здесь можно добавить логику для обработки запроса на главную страницу.
def index(request):
    """
    request: Объект запроса, который содержит информацию о текущем HTTP-запросе, включая метод запроса, заголовки, данные и другие параметры.
    """
    context = { # Контекст для передачи данных в шаблон.
        'title': 'Главная страница', # Заголовок страницы.
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context) # Возвращаем шаблон главной страницы в ответ на запрос.
```
-------------------------------------------




-------------------------------------------
## 7. urls.py - (В приложении)
- Локальные маршруты.
    - Зачем: Чтобы не захламлять главный urls.py. Здесь описываются пути конкретно для этого приложения (например, /post/1/, /post/create/).
-------------------------------------------




-------------------------------------------
# 8. templates/ (Добавлено)
- Папка для HTML-файлов.
    - Структура: Рекомендуется создавать вложенную папку с именем приложения (templates/main/), чтобы имена шаблонов не конфликтовали между разными приложениями.
    - main Папка называется по имени проекта.

## Создание шаблонов.
- Создаем папку templates в корне приложения.
    - D:\Python-Project\Django\storehome_pyhs\storehome\main\templates\
- Создаем папку main по названию ПРИЛОЖЕНИЯ и создаем файлы шаблонов в ней.
- Добавляем файлы шаблонов в папку по пути templates\main\.
    - D:\Python-Project\Django\storehome_pyhs\storehome\main\templates\main\base.html
        - base.html - Хранит весь HTML-код, который будет повторяться на всех страницах сайта. Это основной шаблон.

    - D:\Python-Project\Django\storehome_pyhs\storehome\main\templates\main\index.html
        - index.html - Хранит HTML-код для главной страницы сайта. Это страница, которая будет наследоваться от base.html.

    - D:\Python-Project\Django\storehome_pyhs\storehome\main\templates\main\about.html
        - about.html - Хранит HTML-код для страницы "О нас описание". Это страница, которая будет наследоваться от base.html.
-------------------------------------------



-------------------------------------------
# Создание директория статических файлов.
- Создаем папку static в корне приложения.
    - D:\Python-Project\Django\storehome_pyhs\storehome\static\deps
- Добавляем файлы в папку static.
    - D:\Python-Project\Django\storehome_pyhs\storehome\static\deps\css\style.css
    - D:\Python-Project\Django\storehome_pyhs\storehome\static\deps\js\script.js
    -
- В settings.py добавляем путь к статическим файлам. Корневой папке проекта BASE_DIR

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static' # Дополнительные директории, в которых Django будет искать статические файлы.
]
```
-------------------------------------------



-------------------------------------------
# Создание медия фаилов.
https://docs.djangoproject.com/en/4.2/howto/static-files/
- Создаем папку media в корне приложения.
    - D:\Python-Project\Django\storehome_pyhs\storehome\media\images

```python
from django.conf import settings # Для работы с медиа-файлами (изображения, видео и т.д.)
from django.conf.urls.static import static # Для работы с медиа-файлами (изображения, видео и т.д.)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),

    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Добавляем маршруты для отображения медиа-файлов в режиме разработки. settings.MEDIA_URL - URL для доступа к медиа-файлам, settings.MEDIA_ROOT - путь к директории с медиа-файлами.
```
-------------------------------------------



-------------------------------------------
# Создаем ТЕГ ШАБЛОН ДЛЯ ВЫВОДА КАТЕГОРИЙ из базы данных в шаблоне Django.
1. Создаем файл `goods_tags.py` в папке `templatetags`. В этом файле мы будем определять наши теги.
    - D:\Python-Project\Django\storehome_pyhs\storehome\goods\templatetags\goods_tags.py
```python
from django import template
from goods.models import Categories

# Необходимо зарегистрировать теги в шаблоне, чтобы они могли быть использованы в шаблонах.
register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
```

2. Включаем теги в шаблон.
    - D:\Python-Project\Django\storehome_pyhs\storehome\main\templates\main\base.html
    - В файле `base.html` мы должны подключить наши теги, чтобы они были доступны для использования. Для этого добавляем следующую строку в секцию `{% load goods_tags %}`:
```python
{% load goods_tags %}

    {% tag_categories as categories %}
    {% for category in categories %}
        <li><a class="dropdown-item text-white" href="{% url "catalog:index" %}">{{ category.name }}</a></li>
    {% endfor %}
```

-------------------------------------------



-------------------------------------------
# Указываем URL-маршруты в файле urls.py + Указываем шаблоны в файле views.py + Указываем шаблоны в файле product.html
1. URL-маршруты в файле urls.py
    - D:\Python-Project\Django\storehome_pyhs\storehome\goods\urls.py
```python
urlpatterns = [ # Список маршрутов приложения

    path('product/<int:product_id>/', views.product, name='product'), # Добавляем URL-маршрутизацию для страницы.
]
```

2. Указываем шаблоны в файле views.py
    - D:\Python-Project\Django\storehome_pyhs\storehome\goods\views.py
```python
# Страница товаров
def product(request, product_id):
    product = Products.objects.get(id=product_id) # Получаем товар по его ID из базы данных.

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)
```

3. Указываем функцию обратное разрешение URL-адресов в шаблоне catalog.html
    - D:\Python-Project\Django\storehome_pyhs\storehome\goods\templates\goods\catalog.html
![альтернативный текст](images\Обратное-разрешение-URL-адресов_.png)

```python
<div class="card-body">
    <a href="{% url "catalog:product" product.id %}">
        <p class="card-title">{{ product.name }}</p>
    </a>
```
-------------------------------------------