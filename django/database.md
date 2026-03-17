# ORM Django
- ORM (Object-Relational Mapping) позволяет вам взаимодействовать с базой данных, используя Python-код, а не SQL-запросы. Это облегчает работу с базами данных и позволяет вам сосредоточиться на логике вашего приложения.

![альтернативный текст](images\ORM_DB_.png)

-------------------------------------------


-------------------------------------------
# Импорты для Django ORM

```python
from django.db import models

```
-------------------------------------------
## class models.Model
ChardField() - Поле для хранения текстовых данных. Опционально можно указать максимальную длину строки.
SlugField() - Поле для хранения URL-адресов. Опционально можно указать максимальную длину строки.
TextField() - Поле для хранения длинных текстовых данных.
IntegerField() - Поле для хранения целых чисел.
DecimalField() - Поле для хранения десятичных чисел.
PositiveIntegerField() - Поле для хранения положительных целых чисел.

-------------------------------------------



-------------------------------------------
# Регистрация в Админ панели
- Для того чтобы добавить модель в админ панель, нужно зарегистрировать модель в файле admin.py.
    - D:\Python-Project\Django\storehome_pyhs\storehome\goods\admin.py
```python
from django.contrib import admin
from goods.models import Categories, Products

# Регистрация модели Categories в админ-панели Django
# admin.site.register(Categories)
# admin.site.register(Products)

# Создание админ-класса для модели Categories
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name
```
-------------------------------------------



-------------------------------------------
# pip install django-debug-toolbar
https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
- необходимо установить как расширение для Django проекта.
    - Позволяет отображать полезную информацию о запросах, SQL-запросах и других метриках во время разработки.
1. Установить пакет:
2. Проверить `INSTALLED_APPS` в `settings.py:`
    ```python
    INSTALLED_APPS = [
        # ...
        "django.contrib.staticfiles",
        # ...
    ]
    ```
3. Добавьте параметр "debug_toolbar" в настройки `INSTALLED_APPS:`
    ```python
    INSTALLED_APPS = [
        # ...
        "debug_toolbar",
        # ...
    ]
    ```
4. Добавить URL-маршруты для панели инструментов отладки в `urls.py:`
    ```python
    from django.urls import include, path
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + debug_toolbar_urls()
    ```

5. Добавить в `MIDDLEWARE` параметр "DebugToolbarMiddleware":
    ```python
    MIDDLEWARE = [
        # ...
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # ...
    ]
    ```

6. Настройка отображения панели инструментов отладки для конкретных IP-адресов в `settings.py:`
    ```python
    INTERNAL_IPS = [
        # ...
        "127.0.0.1",
        # ...
    ]
    ```
-------------------------------------------