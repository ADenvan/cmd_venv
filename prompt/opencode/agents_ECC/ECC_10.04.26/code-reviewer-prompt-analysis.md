# Анализ промпта: Code Reviewer

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Универсальный |
| **Задача** | Code Review (качество, безопасность, производительность) |
| **Целевой язык (из коробки)** | TypeScript/JavaScript |
| **Адаптация под Python** | ~25% изменений |

---

## Подходящие категории

- **Code Quality** — основное назначение
- **Security Review** — критические проверки безопасности
- **Performance Review** — оптимизация алгоритмов
- **Best Practices** — соответствие стандартам

---

## Четкость задачи

✅ **Высокая четкость**

Промпт четко структурирован по приоритетам:
- Critical issues (must fix)
- High priority (should fix)
- Medium priority (consider improving)

Чеклист из 19 пунктов + 8 security checks. Формат обратной связи стандартизирован.

---

## Адаптация под Python

### Оценка: ~25% необходимо переписать

| Компонент | Python-эквивалент | Изменения |
|-----------|-------------------|-----------|
| **Security Checks** | Сохранить как есть | 0% (SQL injection, Path traversal, CSRF актуальны) |
| **Code Quality** | `print()` → `logging`, удалить React-специфику | ~30% |
| **Performance** | N+1 queries актуально для Django/SQLAlchemy | 10% |
| **Best Practices** | `JSDoc` → `docstrings`, `prettier` → `black`/`ruff` | ~40% |
| **Git workflow** | Оставить без изменений | 0% |

### Python-специфика замен

| Оригинал (TS/JS) | Python |
|------------------|--------|
| `console.log` | `print()`, `logging` |
| `JSDoc` | `docstrings` (PEP 257) |
| `prettier --write` | `black .`, `ruff format .` |
| `tsc --noEmit` | `mypy .`, `pyright` |
| React re-renders | **Удалить** (не применимо) |
| `try/catch` | `try/except` |
| Missing ARIA | **Удалить** (frontend-specific) |

---

## Что лишнее/требует адаптации

| Элемент | Статус | Примечание |
|---------|--------|------------|
| React re-renders | ❌ Удалить | Frontend-specific |
| ARIA labels | ❌ Удалить | Frontend accessibility |
| Bundle sizes | ❌ Удалить | JS-specific |
| Unoptimized images | ⚠️ Адаптировать | Можно заменить на "тяжелые библиотеки" |
| Project-Specific Guidelines | ❌ Пропустить | Плейсхолдер для пользователя |
| SQL injection | ✅ Оставить | Актуально для Python (psycopg2, SQLAlchemy) |
| Path traversal | ✅ Оставить | Актуально (os.path, pathlib) |
| N+1 queries | ✅ Оставить | Актуально для Django ORM |
| Time complexity | ✅ Оставить | Универсально |

---

## Когда использовать

| Сценарий | Полезность |
|----------|------------|
| После написания нового кода | ⭐⭐⭐⭐⭐ |
| Перед merge в main | ⭐⭐⭐⭐⭐ |
| Проверка PR от других разработчиков | ⭐⭐⭐⭐⭐ |
| Security audit кода | ⭐⭐⭐⭐⭐ |
| Проверка алгоритмической сложности | ⭐⭐⭐⭐ |
| Оценка лицензий зависимостей | ⭐⭐⭐⭐ |
| Рефакторинг архитектуры | ⭐⭐ (ограниченно) |

---

## Преимущества для Python

✅ **Сохраняется без изменений:**
- Security checks (8 пунктов)
- Git diff workflow
- 3-уровневая приоритизация
- Чеклист code quality (7 пунктов)
- Формат вывода (CRITICAL/HIGH/MEDIUM)
- Approval Criteria

⚠️ **Требует минимальной адаптации:**
- Post-review actions (замена инструментов)
- Best Practices (замена JSDoc → docstrings)

❌ **Удалить:**
- Frontend-specific пункты (3-4 пункта)

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность | 9/10 |
| Компактность | 8/10 (103 строки) |
| Универсальность | 8/10 (легко адаптировать) |
| **Адаптируемость под Python** | **8/10 (25% изменений)** |

**Рекомендация**: Отличный универсальный промпт для code review. Легко адаптируется под Python — достаточно заменить 3-4 frontend-specific пункта и адаптировать инструменты форматирования. Security и code quality checks универсальны и применимы к любому языку.

---

*Дата анализа: 10.04.2026*

Markdown
да