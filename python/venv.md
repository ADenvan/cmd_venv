# Работа с виртуальным окружением Python (Windows)

## Изменение переменных среды вручную
1. Нажать **Win + R** → ввести `sysdm.cpl`
2. Открыть **Переменные среды**
3. В разделе **Системные переменные** найти переменную `Path`
4. Нажать **Изменить** и выбрать пути для добавления:
   - `C:\Program Files\Python313\Scripts\`
   - `C:\Program Files\Python313\`

---
## Проверка Python и пакетов

```bash
python --version      # или python -V, версия Python
where python          # путь к установленному Python
pip list              # список установленных пакетов
pip uninstall lxml -y # удаление пакета lxml
pip show requests     # установлена ли конкретная библиотека

-----------------------------------------------
## Работа с requirements.txt
pip freeze                   # список всех установленных пакетов
pip freeze > requirements.txt  # сохранить список в файл
pip install -r requirements.txt # установка пакетов из файла
python -m pip install --upgrade pip setuptools wheel # Обновляй pip и инструменты




-----------------------------------------------
## Создание и удаление виртуального окружения
python -m venv venv          # создать виртуальное окружение
rm -r .\venv\                # удалить окружение
C:\Python312\python.exe -m venv venv  # создать окружение с выбранным интерпретатором



-----------------------------------------------
## Активация и деактивация виртуального окружения.
.\venv\Scripts\activate.ps1  # активировать
deactivate                   # деактивировать


-----------------------------------------------
## Создание окружения с определённой версией Python
C:\Python313\python.exe -m venv .venv




-----------------------------------------------
## Использование virtualenv Для установки виртуального окружения с определённой версией Python необходимо установить библиотеку:
pip install virtualenv
python -m virtualenv -p "C:\Program Files\Python313\python.exe" my_second_env




-----------------------------------------------
## Возможные ошибки и их решение  Временное изменение политики выполнения (только для текущего терминала)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

## Постоянное решение (навсегда для пользователя)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

```
# Автоматическая активация окружения в VS Code
1. Открыть настройки **(settings.json)**
2. Включить опцию: **Python > Terminal: Activate Env in Current Terminal**
3. Будет создан .js-файл для автоактивации окружения.

# Работа с интерпретатором Python в VS Code
1. Выбор интерпретатора: **Python: Select Interpreter**
2. Создание нового окружения: **Python: Create Environment**