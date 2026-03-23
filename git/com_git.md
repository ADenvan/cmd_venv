-------------------------------------------------
-------------------------------------------------
# github
## git clone через git bash
```bash
git clone https://github.com/ADenvan/storehome_pyhs.git
git status
```
![альтернативный текст](images\git-bash-clone-com_.jpg)

-------------------------------------------------


Add new folder + opencode/... lm_studio/... prompt/...cherr_studio/


-------------------------------------------------
# Команды в терминале для VS Code регистрации репозитория

1. Настройка имени пользователя для этого репозитория по выбранному пути.
    - (.venv) PS D:\Python-Project\git_repositoy\cmd_venv>git config user.name "Vladislav"
    - (.venv) PS D:\Python-Project\git_repositoy\cmd_venv>git config user.email "vladislav@mail.ru"

2. Настройка имени пользователя для всех репозиториев на этом компьютере.`
    - (.venv) PS D:\Python-Project\git_repositoy\cmd_venv>git config --global user.name "Vladislav"
    - (.venv) PS D:\Python-Project\git_repositoy\cmd_venv>git config --global user.email "vladislav@mail.ru"


## - - - 1. Проверка статуса и просмотр изменений
```bash
git status # Проверить статус файлов
git diff # Просмотреть изменения в файлах (что конкретно изменилось)
git status -s # Просмотреть короткий статус
```

## - - - 2. Добавление файлов в staging area
```bash
git add . # Добавить все измененные файлы
git add имя_файла.расширение # Добавить конкретный файл
git add *.js # Добавить все файлы с определенным расширением
git add -A # Добавить все изменения (включая удаленные файлы)
```

## - - - 3. Проверка перед коммитом
```bash
git diff --staged # Показать, что будет закоммичено (отличия staged файлов)
git status # Проверить, какие файлы добавлены в staging
```

## - - - 4. Создание коммита
```bash
git commit -m "Ваше сообщение о изменениях" # Создать коммит с сообщением
git commit -am "Ваше сообщение" # Добавить и закоммитить за один шаг (только для отслеживаемых файлов)
```

## - - - 5. Проверка истории коммитов
```bash
git log # Показать историю коммитов все ветки
git log --oneline # Краткая история
git log --graph --oneline --all # История с графиком веток
```

## - - - 6. Отправка на GitHub через терминал
```bash
git push origin main # Отправить изменения в удаленный репозиторий
git push origin master # Или если ветка называется master
git push -f origin main # Принудительная отправка (осторожно!)
```

## - - - Проверка игнорируемых файлов
```bash
git check-ignore -v путь/к/файлу # Проверить, игнорируется ли файл
git config --list # Просмотр конфигурации / Проверить настройки Git
git remote -v # Проверить remote репозитории Git remote - это ссылка на удаленный репозиторий, который вы можете клонировать, отправлять изменения и т.д.
```

## - - - Полный рабочий процесс проверки
1. Проверить статус
> git status

2. Просмотреть изменения
> git diff

3. Добавить файлы
> git add .

4. Проверить staged файлы
> git diff --staged

5. Создать коммит
> git commit -m "Описание изменений"

6. Проверить историю
> git log --oneline -5

7. Отправить на GitHub
> git push origin main



-------------------------------------------------
## Выбор версии - получение списка всех версии - для выбора переключение на нужную версию - выход из режима выбора версии клавиша Q
```bash
git log  --graph --all --oneline # Просмотреть историю коммитов с ветками и графом.
git checkout 1234567 # Команда для перехода выбранной веси - Необходим номер хеша версии
git checkout main # Команда для выхода из режима выбора версии и возврата на основную ветку.
git filter-repo --path Parsing-Sc # Команда для удаления файла из истории коммитов
```
-------------------------------------------------





-------------------------------------------------
## gitignore Не отслеживать Файлы с ключами и учётными данными
```bash
creds.json # Файлы с ключами и учётными данными
secrets.json # Файлы с ключами и учётными данными
config/secret_key.txt # Файлы с ключами и учётными данными
config.json # Файлы с ключами и учётными данными
Parsing-Scraping/creds.json # Не отслеживать файл по данному пути.
vsCoding_settings/ # Не отслеживать папку
vsCoding_settings/vscode_fo_settings.txt  # отслеживать только этот файл в папке которое не отслеживает git.
```
-------------------------------------------------





-------------------------------------------------
## Как проверить размер проекта в терминале
```bash
git count-objects -vH # Эта команда покажет размер папки .git, где хранится вся история.
    - Ищите строку size-pack. Это размер упакованных данных, которые уйдут на сервер.
du -sh . # Проверка размера текущей директории работает только git bash
du -sh * # Проверка размера папок в текущей директории
du -sh /path/to/directory # Проверка размера директории по указанному пути
```
![альтернативный текст](images\git-bash-du-sh-command_.jpg)
-------------------------------------------------



-------------------------------------------------
## Вариант 1: Удаление с помощью git filter-repo (рекомендуется) Убедись что установлен git-filter-repo:


pip install git-filter-repo

git filter-repo --path Parsing-Scraping/baza_knig_API/creds.json --invert-paths ,Удали файл из истории:
git push origin main --force ,Затем сделай force push:


,,,Вариант 2: Удаление файла и повтор коммита (если фильтр не установлен)
git rm --cached Parsing-Scraping/baza_knig_API/creds.json , Удали файл:

echo Parsing-Scraping/baza_knig_API/creds.json >> .gitignore ,Добавь .gitignore чтобы исключить этот файл в будущем:

git add .gitignore
git commit -m "Удалён файл с секретами и добавлен в .gitignore" ,Закоммить:


,,,✅ 1. Пример .gitignore Создай или обнови файл .gitignore в корне проекта:

# Секреты и конфиденциальные данные
*.env
*.key
*.pem
*.crt
*.p12
*.jks
*.pfx
*.keystore



# Логи и временные файлы
*.log
*.tmp
*.bak
*.swp
*.swo

# Python-артефакты
__pycache__/
*.pyc
*.pyo
*.pyd
.env/
.venv/
build/
dist/


,,,⚙️ 2. Скрипт clean_secrets.bat (для Windows/Visual Studio) Сохрани этот код в файл clean_secrets.bat в корне проекта:

@echo off
echo ================================================
echo Удаление файла с секретом из Git-репозитория...
echo ================================================

REM Удаляем файл из индекса, но не с диска
git rm --cached Parsing-Scraping/baza_knig_API/creds.json

REM Добавим .gitignore, если его нет
IF NOT EXIST ".gitignore" (
    echo .gitignore не найден. Создаю .gitignore...
    echo Parsing-Scraping/baza_knig_API/creds.json > .gitignore
) ELSE (
    echo Parsing-Scraping/baza_knig_API/creds.json>>.gitignore
)

REM Коммитим изменения
git add .gitignore
git commit -m "Удалён файл creds.json с секретами и добавлен в .gitignore"

echo ================================================
echo Если файл уже был в истории — очищаем историю...
echo ================================================
echo Убедитесь, что установлен git-filter-repo
echo Нажмите любую клавишу для продолжения...
pause

REM Очищаем историю (нужно установить git-filter-repo отдельно)
git filter-repo --path Parsing-Scraping/baza_knig_API/creds.json --invert-paths

echo ================================================
echo История очищена. Выполняется force push...
echo ================================================
git push origin main --force

echo ================================================
echo ✅ Завершено. Секрет удалён.
pause

,,,📥 Как использовать:
Сохрани .gitignore в корне проекта.

Сохрани clean_secrets.bat в том же каталоге.

Дважды кликни на clean_secrets.bat или запусти из Visual Studio в терминале:

./clean_secrets.bat