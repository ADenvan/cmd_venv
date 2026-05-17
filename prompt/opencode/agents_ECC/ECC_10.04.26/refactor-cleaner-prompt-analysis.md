# Анализ промпта: Refactor Cleaner

## Описание

Промпт для **рефакторинга и удаления dead code**. Специализация: **codebase cleanup** — обнаружение и удаление неиспользуемого кода, дубликатов, зависимостей. Очень TS/JS-специфичен.

---

## Направление задачи

### Core Responsibilities:

| Область | Задача |
|---------|--------|
| **Dead Code Detection** | Неиспользуемые экспорты, файлы, зависимости |
| **Duplicate Elimination** | Консолидация дублирующегося кода |
| **Dependency Cleanup** | Удаление неиспользуемых npm/pip пакетов |
| **Safe Refactoring** | Обеспечение сохранности функциональности |
| **Documentation** | DELETION_LOG.md для отслеживания |

---

## Технологии (из промпта)

### TS/JS инструменты:

| Инструмент | Назначение |
|------------|------------|
| **knip** | Неиспользуемые файлы, экспорты, зависимости |
| **depcheck** | Неиспользуемые npm зависимости |
| **ts-prune** | Неиспользуемые TypeScript экспорты |
| **eslint** | Неиспользуемые переменные, disable-директивы |

---

## Адаптация под Python

### Оценка: ~35% изменений

**Есть ли смысл адаптировать?** — ✅ **Да, смысл есть.**

| TS/JS Инструмент | Python Эквивалент | Аналогичность |
|------------------|-------------------|---------------|
| **knip** | **vulture** | ⭐⭐⭐⭐ (оба находят dead code) |
| **depcheck** | **pipdeptree** / **pip-check-reqs** | ⭐⭐⭐ (разная функциональность) |
| **ts-prune** | **vulture** / **pylint** (unused-import) | ⭐⭐⭐⭐ |
| **eslint** | **pylint**, **flake8**, **ruff** | ⭐⭐⭐⭐⭐ |

### Python инструменты для dead code:

| Инструмент | Назначение | Команда |
|------------|------------|---------|
| **vulture** | Dead code detection | `vulture src/` |
| **pylint** | Unused imports, variables | `pylint --disable=all --enable=W0611 src/` |
| **ruff** | Fast Python linter | `ruff check src/ --select=E,W,F,RET` |
| **bandit** | Security (bonus) | `bandit -r src/` |
| **pipdeptree** | Dependency tree analysis | `pipdeptree --warn silence` |

### Python Workflow (адаптация):

```bash
# 1. Dead code detection
vulture src/ --min-confidence 80

# 2. Unused imports
ruff check src/ --select=F401

# 3. Unused variables
pylint src/ --disable=all --enable=W0613

# 4. Dependency check
pipdeptree --warn silence | grep -E "WARNING|Package"

# 5. Security scan (bonus)
bandit -r src/
```

---

## Сравнение с Code Reviewer

### Что умеет Code Reviewer:

| Область | Находит dead code? | Уровень |
|---------|-------------------|---------|
| **Unused variables** | ✅ | Medium |
| **Unused imports** | ✅ | Medium |
| **Dead code branches** | ✅ | Low |
| **Duplicate code** | ⚠️ Упоминает | Low |
| **Unused dependencies** | ❌ Нет | - |
| **Unused files** | ❌ Нет | - |
| **Unused exports** | ❌ Нет | - |

### Что умеет Refactor Cleaner (чего нет в Code Reviewer):

| Область | Refactor Cleaner | Code Reviewer |
|---------|------------------|---------------|
| **Dead files** | ✅ Полный поиск | ❌ Нет |
| **Unused dependencies** | ✅ Специализированный поиск | ❌ Нет |
| **Duplicate consolidation** | ✅ Workflow для объединения | ⚠️ Упоминает |
| **DELETION_LOG** | ✅ Формат документирования | ❌ Нет |
| **Risk assessment** | ✅ SAFE/CAREFUL/RISKY | ❌ Нет |
| **Git workflow** | ✅ Branch, commit strategy | ❌ Нет |
| **Recovery process** | ✅ Rollback procedures | ❌ Нет |

### Эффективность:

| Сценарий | Refactor Cleaner | Code Reviewer |
|----------|------------------|---------------|
| **Code review PR** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ Лучше |
| **Массовый cleanup** | ⭐⭐⭐⭐⭐ Отлично | ⭐⭐ |
| **Dependency audit** | ⭐⭐⭐⭐⭐ | ⭐ |
| **Duplicate removal** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Build optimization** | ⭐⭐⭐⭐⭐ | ⭐ |
| **Security review** | ⭐⭐ | ⭐⭐⭐⭐⭐ Лучше |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (TS/JS) | 10/10 |
| Компактность | 7/10 (241 строка — многословно) |
| Универсальность | **4/10** (TS/JS specific) |
| **Применимость к Python** | **6.5/10** |

### Оценка адаптации под Python: **~35%**

**Что сохраняется:**
- Workflow (Analysis → Risk Assessment → Removal) ✅
- Safety Checklist ✅
- DELETION_LOG format ✅
- Best Practices ✅

**Что адаптируется:**
- Инструменты (knip → vulture, depcheck → pipdeptree) 🔧
- File extensions (.ts/.tsx → .py) 📝
- Import patterns (ES modules → Python imports) 📝

**Что добавляется для Python:**
- `__pycache__`, `.pyc` cleanup
- Virtual environment (venv) considerations
- Python-specific imports (circular detection)

---

### Смысл адаптации: ✅ **Есть**

**Для кого полезен:**
- Python проекты с legacy codebase
- Миграция с многочисленными deprecated файлами
- Dependency audit перед релизом
- Bundle/package size optimization

**Python-альтернативы:**
- `vulture` — основной инструмент для dead code
- `pylint`/`ruff` — unused imports/variables
- `pipdeptree` — dependency analysis

---

*Дата анализа: 10.04.2026*
