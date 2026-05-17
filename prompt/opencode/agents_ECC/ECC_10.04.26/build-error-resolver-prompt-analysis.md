# Анализ промпта: Build Error Resolver

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Узко специализированный |
| **Задача** | Исправление ошибок сборки |
| **Целевой язык** | TypeScript/JavaScript (из коробки) |

---

## Подходящие категории

- **Build/DevOps** — основное назначение
- **Code Quality** — исправление компиляционных ошибок
- **CI/CD Support** — разблокировка пайплайнов

---

## Четкость задачи

✅ **Высокая четкость**

Промпт имеет конкретную цель: исправить ошибки сборки минимальными изменениями. Четко определены:
- 6 core responsibilities
- 5 паттернов ошибок с примерами
- DO/DON'T списки
- Workflow с 4 этапами

---

## Адаптация под Python

### Оценка: ~45% необходимо переписать

| Компонент | Python-эквивалент | Объем изменений |
|-----------|-------------------|-----------------|
| **Diagnostic Commands** | `mypy`, `pyright`, `pylint`, `python -m py_compile` | 100% замена |
| **Error Patterns** | Type hints, Optional, Union | ~60% адаптации |
| **Build Tools** | `setuptools`, `poetry`, `pip`, `uv` | 100% замена |
| **Workflow** | Аналогичный | 0% изменений |
| **Minimal Diff Strategy** | Аналогичный | 0% изменений |

### Python-технологии для замены

```bash
# Type checking (вместо tsc)
mypy .
pyright
python -m mypy src/

# Linting (вместо eslint)
flake8
pylint
ruff check .

# Build (вместо npm run build)
python -m build
poetry build
pip install -e .

# Dependency check
pip check
poetry check
```

### Python Error Patterns

**Pattern 1: Type Annotation Missing**
```python
# ERROR: Missing type annotation
def add(x, y):
    return x + y

# FIX
from typing import Union
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y
```

**Pattern 2: Optional/None check**
```python
# ERROR: Item "None" has no attribute "name"
name = user.name.upper()

# FIX: Optional chaining via walrus или проверка
name = user.name.upper() if user else ""
```

---

## Что лишнее/требует адаптации

| Элемент | Статус | Примечание |
|---------|--------|------------|
| Next.js специфика | ❌ Убрать | Python-фреймворки (Django, FastAPI) |
| tsconfig.json | ❌ Заменить | `pyproject.toml`, `setup.py` |
| webpack | ❌ Заменить | `setuptools`, `poetry` |
| Import aliases (@/) | ⚠️ Адаптировать | Python packages, relative imports |
| node_modules | ❌ Заменить | `venv`, `poetry env` |
| JSX/TSX | ❌ Убрать | Python templates, API routes |

---

## Когда использовать

| Сценарий | Полезность |
|----------|------------|
| `mypy` показывает type errors | ⭐⭐⭐⭐⭐ |
| CI/CD build падает | ⭐⭐⭐⭐⭐ |
| Import/ModuleNotFoundError | ⭐⭐⭐⭐⭐ |
| Package version conflicts | ⭐⭐⭐⭐ |
| Рефакторинг архитектуры | ⭐ (не подходит) |
| Написание новых фич | ⭐ (не подходит) |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность | 9/10 |
| Компактность | 7/10 (233 строки) |
| Универсальность | 5/10 (жестко завязан на TS/JS) |
| Адаптируемость под Python | 6/10 (45% переписывания) |

**Рекомендация**: Промпт хорошо структурирован, но требует существенной адаптации для Python. Основная ценность — workflow и философия minimal changes — переносится без изменений. Технические детали (команды, паттерны) — полностью заменяются.

---

*Дата анализа: 10.04.2026*
