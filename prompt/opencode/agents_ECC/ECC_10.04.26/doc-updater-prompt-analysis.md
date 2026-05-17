# Анализ промпта: Doc Updater

## Описание

Промпт для поддержания документации и codemap'ов в актуальном состоянии. Ориентация: **JavaScript/TypeScript проекты**. Использует AST analysis (TypeScript compiler API) для автоматического извлечения структуры из кода.

---

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Узко специализированный (JS/TS экосистема) |
| **Задача** | Documentation & Codemap Maintenance |
| **Целевая экосистема** | Node.js / TypeScript |
| **Применимость к Python** | **~60%** (хорошая, требует адаптации) |

---

## Технологии в промпте

### Текущие (JS/TS ориентация):

| Технология | Назначение | Python эквивалент |
|------------|------------|-------------------|
| **TypeScript compiler API** | AST analysis, структура кода | `ast`, `astor`, `libcst` |
| **JSDoc/TSDoc** | Извлечение документации из комментариев | `docstrings`, `sphinx`, `pydoc` |
| **package.json** | Метаданные проекта | `pyproject.toml`, `setup.py` |
| **npm** | Package manager | `pip`, `poetry`, `uv` |
| **Next.js patterns** | Framework detection | Django, FastAPI, Flask |

---

## Что есть в промпте (Python-специфика)

### Python-специфичные элементы:

| Элемент | JS/TS версия | Python адаптация | Оценка изменений |
|---------|--------------|-------------------|------------------|
| **Entry points** | `apps/*`, `packages/*` | `src/`, project root, `__main__.py` | 30% |
| **Module structure** | ES modules (import/export) | Python modules (import, `__init__.py`) | 40% |
| **Documentation extraction** | JSDoc/TSDoc parsing | `inspect`, `pydoc`, docstrings | 50% |
| **Framework detection** | Next.js, Node.js | Django, FastAPI, Flask | 30% |
| **Environment variables** | `.env.example` | `.env`, `python-dotenv` | 10% |
| **Package metadata** | `package.json` | `pyproject.toml`, `setup.cfg` | 40% |
| **Build commands** | `npm run build` | `python -m build`, `poetry build` | 40% |
| **Dev server** | `npm run dev` | `python manage.py runserver`, `uvicorn` | 40% |

---

## Python AST аналоги

### Замена TypeScript compiler API:

| Python библиотека | Назначение | Пример использования |
|-------------------|------------|---------------------|
| **`ast`** (stdlib) | Встроенный AST parser | `ast.parse(source_code)` |
| **`astor`** | AST to source code | `astor.to_source(tree)` |
| **`libcst`** | Concrete Syntax Tree (Facebook) | Сохраняет форматирование, комментарии |
| **`rope`** | Refactoring library | Анализ зависимостей |
| **`jedi`** | Autocompletion + static analysis | Импорты, определения |

### Пример Python AST:

```python
import ast

# Парсинг модуля
with open('module.py') as f:
    tree = ast.parse(f.read())

# Извлечение импортов
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for alias in node.names:
            print(f"Import: {alias.name}")
    elif isinstance(node, ast.ImportFrom):
        print(f"From {node.module} import {', '.join(n.name for n in node.names)}")

# Извлечение функций и классов
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"Function: {node.name}")
        print(f"Docstring: {ast.get_docstring(node)}")
    elif isinstance(node, ast.ClassDef):
        print(f"Class: {node.name}")
```

---

## Адаптация под Python

### Структура codemap для Python:

```
docs/CODEMAPS/
├── INDEX.md              # Overview
├── core.md               # Core modules
├── api.md                # API structure (FastAPI/Django)
├── database.md           # ORM models (SQLAlchemy/Django)
├── cli.md                # CLI commands (Click/Typer)
└── workers.md              # Background jobs (Celery/RQ)
```

### Python-specific шаблоны:

| JS/TS Pattern | Python Pattern |
|---------------|----------------|
| `src/app/*` routes | `urls.py` (Django), `@app.get()` (FastAPI) |
| `src/components/*` | `templates/` (Django), Jinja2 |
| `src/lib/*` | `utils/`, `helpers/` modules |
| Database models | `models.py` (Django), SQLAlchemy models |
| Workers | `tasks.py` (Celery), `rq` jobs |

---

## Когда использовать

| Сценарий | Полезность (JS/TS) | Полезность (Python) |
|----------|-------------------|---------------------|
| Генерация архитектурной документации | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ (требует адаптации) |
| Обновление README | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Проверка актуальности docs | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| AST analysis | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ (через `ast`, `libcst`) |
| Dependency mapping | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ (через `jedi`, `ast`) |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (JS/TS) | 10/10 |
| Компактность | 7/10 (192 строки) |
| Универсальность | 5/10 (привязан к JS/TS) |
| **Применимость к Python** | **6/10 (60%)** |

### Оценка адаптации под Python: ~40% изменений

**Что сохраняется без изменений:**
- Codemap структура (markdown, ASCII diagrams)
- README template (80% контента универсально)
- Quality checklist (universal)
- Best practices (single source of truth, timestamps)
- Workflow (extract → update → validate)

**Что требует адаптации:**
- AST analysis (TypeScript → Python ast/libcst)
- Documentation extraction (JSDoc → docstrings)
- Framework detection (Next.js → Django/FastAPI/Flask)
- Package metadata (package.json → pyproject.toml)
- Commands (npm → pip/poetry)

### Рекомендация:

✅ **Для JS/TS проектов**: Отличный промпт, структурированный workflow.

⚠️ **Для Python**: Хорошая база, но требует адаптации AST анализа и framework patterns. 40% изменений — в основном технические детали.

---

*Дата анализа: 10.04.2026*
