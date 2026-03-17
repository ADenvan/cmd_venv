# Выбор версии Django
![альтернативный текст](images\Django-version_.jpg)
-------------------------------------------



-------------------------------------------
# В терминале
```bash
django-admin               # Получаем список команд
django-admin startproject  # Создаем проект
django-admin startapp      # Создаем приложение
python manage.py runserver # Запускаем
```
-------------------------------------------



-------------------------------------------
# Управление миграциями Django ORM
```bash
.\manage.py makemigrations   # Создает файлы миграции
.\manage.py migrate          # Применяет миграции к базе данных
.\manage.py createsuperuser  # Создаем суперпользователя
```
-------------------------------------------





-------------------------------------------
# Создание доменного имени проекта.
```bash
django-admin startproject app # Создаем проект app
```
1. детекторе папки не зависит от названия app/app Это просто внешний каталог
2. Вариант с выбором виртуального окружения с уровня выше.
    - Open folder
![альтернативный текст](images\Django-venv-interpretator_.jpg)
```bash
python manage.py runserver # Запускаем сервер
```
-------------------------------------------



-------------------------------------------
# Создание приложение команда терминала.
- Модуль с конкретной логикой (например, "Блог", "Магазин", "Пользователи"). Один проект может содержать много приложений.
```bash
D:\Python-Project\Django\storehome_pyhs\config> python manage.py startapp main
```
```python
INSTALLED_APPS = [
    'main', # Регистрация нового приложения. Добавляем название приложение в список установленных приложений.
]
```
-------------------------------------------





-------------------------------------------

# Миграции
- Миграции позволяют вам изменять структуру базы данных, используя Python-код. Это облегчает управление изменениями в структуре базы данных и позволяет вам сосредоточиться на логике вашего приложения.

- Применяем миграции к базе данных. Это создает таблицы в базе данных на основе моделей Django.
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py migrate
```

1. Создаем новую миграцию после изменения модели. Это создает файл миграции, который можно применить к базе данных.
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py makemigrations
```
- Созданной фаил для миграции [0001_initial.py] можно смело удалять.
![альтернативный текст](images\Создание-Класса+Миграция.jpg)


2. После создания миграции, применяем её к базе данных.
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py migrate
```


3. Создание супер пользователя Django
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py createsuperuser
```
![альтернативный текст](images\Create-Super-User_.jpg)

-------------------------------------------


-------------------------------------------
# Фикстуры команды Django
- Фикстура в Python для тестирования — это специальная функция, которая помогает подготовить окружение для тестов и убрать тестовые данные после их выполнения. Например, фикстура может:
- Создавать тестовые данные в базе данных.
- Удалять тестовые данные после выполнения тестов.
- Подготавливать базу данных для тестов.
```bash
python manage.py loaddata    # Загружает фикстуры в базу данных
python manage.py dumpdata    # Экспортирует данные в JSON файл
```

1. Создаем папку `fixtures/goods/`
2. Командой в терминале создаем фаил `cats.json` и заполняем его данными в формате JSON.
    - Могут быть проблемы с кодировкой.
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py dumpdata goods.Categories > fixtures/goods/cats.json
```

- Может быть некорректно отображаться в терминале, если в JSON файле есть кириллица. Для этого используем команду с `Out-File` в PowerShell.
```bash
.\manage.py dumpdata goods.Categories | Out-File -FilePath fixtures/goods/cats.json -Encoding UTF8
```

3. Загружаем данные в базу данных
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py loaddata fixtures/goods/cats.json
```
-------------------------------------------


-------------------------------------------
# debug-toolbar
https://docs.djangoproject.com/en/6.0/ref/models/querysets/
- Управление базой данных через терминал.
- Позволяет выполнять SQL запросы и просматривать результаты в интерактивной оболочке.
```bash
D:\Python-Project\Django\storehome_pyhs\storehome> .\manage.py debugsqlshell
```
1. Импортирукм модель для работы с ней.
    - Выполняем SQL запросы и просматриваем результаты.
```bash
>>> from goods.models import Products
>>> Products.objects.all()              # Получаем все объекты модели.
>>> Products.objects.filter(id=2)       # Применение фильтрации.
>>> Products.objects.all().filter(id=2) # Двойное применение фильтрации.
>>> Products.objects.order_by('-price') # Сортировка по полю price в обратном порядке.

```
-------------------------------------------






