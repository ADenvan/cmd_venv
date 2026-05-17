# Анализ промпта: Python Reviewer

## Описание

Готовый **Python-specific code reviewer** с фокусом на Pythonic patterns, type hints, security и concurrency. Использует Python-специфичные инструменты: `ruff`, `mypy`, `bandit`, `black`.

---

## Направление задачи

### Основные области:

| Приоритет | Область | Примеры |
|-----------|---------|---------|
| **CRITICAL** | Security | SQL injection, command injection, path traversal |
| **CRITICAL** | Error Handling | Bare except, swallowed exceptions, missing context managers |
| **HIGH** | Type Hints | Missing annotations, using `Any`, nullable parameters |
| **HIGH** | Pythonic Patterns | List comprehensions, `isinstance()`, mutable defaults |
| **HIGH** | Code Quality | Functions >50 lines, deep nesting, magic numbers |
| **HIGH** | Concurrency | Shared state without locks, N+1 queries |
| **MEDIUM** | Best Practices | PEP 8, docstrings, `print()` vs `logging` |

### Под какие задачи применим:

- **Code Review** — основное назначение
- **Security Audit** — Python-specific vulnerabilities
- **Type Safety** — mypy compliance
- **Django/FastAPI/Flask** — framework-specific checks
- **Performance** — N+1 queries, concurrency

---

## Эффективность применения с другими языками

### Оценка: **~10%** (очень низкая)

| Концепция | Python | TypeScript/JavaScript | Совместимость |
|-----------|--------|----------------------|---------------|
| Bare except | ✅ Критично | ❌ Не применимо (нет аналога) | 0% |
| Mutable defaults | ✅ Python-specific | ❌ Не применимо | 0% |
| `isinstance()` vs `type()` | ✅ Pythonic | ❌ JS `typeof`/`instanceof` разные | 20% |
| Context managers | ✅ `with` statement | ⚠️ JS `try/finally` или RAII | 30% |
| SQL injection | ✅ Параметризация | ✅ Параметризация | 100% |
| Path traversal | ✅ `normpath` | ⚠️ `path.normalize` | 60% |
| Type hints | ✅ PEP 484 | ✅ TypeScript | 80% |
| Framework checks (Django/FastAPI/Flask) | ✅ Специфичны | ❌ React/Next.js другие | 0% |

---

## Сравнение с Code Reviewer

| Критерий | Python Reviewer | Code Reviewer (universal) | Эффективность |
|----------|-----------------|-------------------------|---------------|
| **Язык** | Python-only | Универсальный | Python reviewer лучше для Python |
| **Security** | Python-specific (YAML, pickle, eval) | Общие (XSS, CSRF, injection) | Python reviewer глубже |
| **Type Hints** | PEP 484, mypy | JSDoc, TypeScript | Одинаково хорошо |
| **Pythonic Patterns** | ✅ Полный охват | ❌ Нет | Python reviewer существенно лучше |
| **Concurrency** | threading, asyncio, GIL | Async/await, Promise | Python reviewer лучше для Python |
| **Framework** | Django, FastAPI, Flask | React, Express | Специфичны |
| **Инструменты** | ruff, mypy, bandit | ESLint, Prettier | Оба хороши |
| **Размер** | 85 строк (компактный) | 103 строки | Python reviewer лаконичнее |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (Python) | 10/10 |
| Компактность | 9/10 (85 строк) |
| Универсальность | **2/10** (только Python) |
| **Совместимость с другими языками** | **1/10** |

### Рекомендация:

✅ **Для Python проектов**: Отличный, специализированный промпт. Лучше универсального code-reviewer для Python.

❌ **Для других языков**: Не применим. Использовать language-specific reviewers.

⚖️ **Python Reviewer vs Code Reviewer для Python**:
- Python reviewer: 10/10 (Pythonic patterns, framework checks, concurrency)
- Code reviewer adapted: 7/10 (универсальные проверки, меньше Python-специфики)

---

### Уникальные Python-проверки (не в Code Reviewer):

1. **Bare except** — Python-specific
2. **Mutable default arguments** — `def f(x=[])`
3. **Context managers** — `with` statement
4. **Pythonic patterns** — list comprehensions, `isinstance()`, `Enum`
5. **GIL/Concurrency** — threading, asyncio patterns
6. **Framework checks** — Django ORM, FastAPI async, Flask CSRF

---

*Дата анализа: 10.04.2026*
