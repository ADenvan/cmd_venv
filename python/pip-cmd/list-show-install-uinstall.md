
# Проверка Python и пакетов
---

```bash
# или python -V, версия Python
python --version
# путь к установленному Python*
where python          
python -c "import sys; print(sys.executable)" # Путь
```
---
# list
```bash
# Стандартный список (как requirements.txt)
pip list
# С форматированием в таблицу (красиво)
pip list --format=columns
# Только устаревшие пакеты
pip list --outdated
# С информацией о версии и последней доступной
pip list --outdated --format=columns
```
---

```bash
# установлена ли конкретная библиотека (requests)
pip show requests
# установка конкретной версии пакета
pip install package_name==1.0.0 
# удаление пакета lxml
pip uninstall lxml -y
# Обновляй pip и инструменты
python -m pip install --upgrade pip setuptools wheel 
```
---