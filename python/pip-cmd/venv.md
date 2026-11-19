


# Создание и удаление виртуального окружения
```bash
# создать виртуальное окружение
python -m venv .venv
# удалить окружение      
rm -r .\venv\
# создать окружение с выбранным интерпретатором необходим абсолютный путь.
C:\Python311\python.exe -m venv .venv
C:\Python313\python.exe -m venv .venv
```

# Активация и деактивация виртуального окружения.
```bash
.\venv\Scripts\activate.ps1  # активировать
deactivate                   # деактивировать
```

# Использование virtualenv
- Для установки виртуального окружения с определённой версией Python необходимо установить библиотеку:
```bash
pip install virtualenv
python -m virtualenv -p "C:\Program Files\Python313\python.exe" my_second_env
```
---

# Возможные ошибки и их решение  Временное изменение политики выполнения (только для текущего терминала)
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

# Постоянное решение (навсегда для пользователя)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```


# Автоматическая активация окружения в VS Code
1. Открыть настройки **(settings.json)**
2. Включить опцию: **Python > Terminal: Activate Env in Current Terminal**
3. Будет создан .js-файл для автоактивации окружения.

# Работа с интерпретатором Python в VS Code
1. Выбор интерпретатора: **Python: Select Interpreter**
2. Создание нового окружения: **Python: Create Environment**


# Работа с виртуальным окружением Python (Windows)
## Изменение переменных среды вручную

![Логотип Markdown](images/Переменную_среду_Python_v.jpg)


1. Нажать **Win + R** → ввести sysdm.cpl
2. Открыть вкладку `Дополнительно` → вкладка `Переменные среды`
3. В разделе `Системные переменные` найти переменную `Path`
4. Нажать `Изменить` и выбрать пути для добавления:
   - C:\Program Files\Python313\Scripts\
   - C:\Program Files\Python313\
