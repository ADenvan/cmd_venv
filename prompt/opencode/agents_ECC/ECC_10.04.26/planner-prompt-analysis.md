# Анализ промпта: Planner

## Описание

Промпт для **планирования реализации фич** — создание детальных планов с разбивкой на шаги, анализом зависимостей и рисков. Специализация: **implementation planning** для software development.

---

## Направление задачи

### Основное назначение:

| Этап | Действие |
|------|----------|
| **Requirements Analysis** | Понимание требований, критерии успеха |
| **Architecture Review** | Анализ существующей кодовой базы |
| **Step Breakdown** | Детальная декомпозиция на шаги |
| **Implementation Order** | Приоритизация по зависимостям |

### Формат плана:

- Overview (2-3 предложения)
- Requirements (список)
- Architecture Changes (файлы + описание)
- Implementation Steps (по фазам)
- Testing Strategy
- Risks & Mitigations
- Success Criteria

---

## Специализация

| Параметр | Значение |
|----------|----------|
| **Тип** | Универсальный (language-agnostic) |
| **Фокус** | Planning & Architecture |
| **Применимость** | Любой software project |

---

## Адаптация под Python

### Оценка: ~15% изменений

| Элемент | TS/JS версия | Python версия | Изменения |
|---------|--------------|---------------|-----------|
| **File extensions** | `.ts`, `.tsx`, `.js` | `.py` | 100% замена |
| **Test files** | `*.spec.ts`, `*.test.ts` | `test_*.py`, `*_test.py` | 100% замена |
| **Project structure** | `src/`, `apps/`, `packages/` | `src/`, project root, `tests/` | 30% |
| **Entry points** | `index.ts`, `app.ts` | `__init__.py`, `__main__.py` | 50% |
| **Dependencies** | `package.json` imports | `import`, `from` | 20% |
| **Architecture patterns** | Components, Services, Hooks | Modules, Classes, Functions | 10% |

### Python-специфика в примерах:

#### План формат (Python адаптация):

```markdown
# Implementation Plan: [Feature Name]

## Overview
[2-3 sentence summary]

## Requirements
- [Requirement 1]
- [Requirement 2]

## Architecture Changes
- [Change 1: `src/models/user.py`]
- [Change 2: `src/services/user_service.py`]
- [Change 3: `tests/test_user_service.py`]

## Implementation Steps

### Phase 1: Models & Schema
1. **[Create User Model]** (File: `src/models/user.py`)
   - Action: Define SQLAlchemy/Django model with fields
   - Why: Core data structure for feature
   - Dependencies: None
   - Risk: Low

2. **[Add Database Migration]** (File: Alembic/Django migrations)
   - Action: Generate and apply migration
   - Why: Persist schema changes
   - Dependencies: Step 1
   - Risk: Medium (backup needed)

### Phase 2: Service Layer
3. **[Implement User Service]** (File: `src/services/user_service.py`)
   - Action: Create service class with CRUD operations
   - Why: Business logic abstraction
   - Dependencies: Steps 1-2
   - Risk: Low

### Phase 3: API Layer (if applicable)
4. **[Add API Endpoints]** (File: `src/api/users.py`)
   - Action: FastAPI/Django views for user operations
   - Why: External interface
   - Dependencies: Step 3
   - Risk: Medium (auth integration)

## Testing Strategy
- Unit tests: `tests/test_models/test_user.py`, `tests/test_services/test_user_service.py`
- Integration tests: `tests/test_api/test_users.py`
- E2E tests: User registration/login flow

## Risks & Mitigations
- **Risk**: Database migration conflicts
  - Mitigation: Test on staging, backup before apply
- **Risk**: Breaking changes to existing API
  - Mitigation: Version endpoints, backwards compatibility

## Success Criteria
- [ ] All CRUD operations working
- [ ] Tests passing (coverage >80%)
- [ ] API documentation updated
- [ ] Migration applied without errors
```

---

## Python Best Practices (адаптация)

### Red Flags (Python-специфичные):

| TS версия | Python версия |
|-----------|---------------|
| Large functions (>50 lines) | Large functions (>50 lines) ✅ same |
| Deep nesting (>4 levels) | Deep nesting (>4 levels) ✅ same |
| Missing error handling | Missing `try/except` или `raise` |
| Hardcoded values | Magic constants, no `environ` |
| Missing tests | Missing `pytest` tests |
| Performance bottlenecks | N+1 queries, blocking I/O |

### Дополнительные Python red flags:

- **Circular imports** — отсутствие `if TYPE_CHECKING`
- **Missing type hints** — функции без аннотаций
- **Mutable default arguments** — `def func(arg=[])`
- **Bare except** — `except:` вместо `except SpecificError:`
- **Global state** — изменение модулей на уровне импорта

---

## Когда использовать

| Сценарий | Полезность |
|----------|------------|
| Новая фича (medium/large) | ⭐⭐⭐⭐⭐ |
| Рефакторинг архитектуры | ⭐⭐⭐⭐⭐ |
| Breaking changes | ⭐⭐⭐⭐⭐ |
| Small bugfix | ⭐⭐ (overkill) |
| Documentation only | ⭐⭐⭐ |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность | 10/10 |
| Компактность | 8/10 (112 строк) |
| Универсальность | **9/10** |
| **Применимость к Python** | **8.5/10** |

### Оценка адаптации под Python: **~15%**

**Что сохраняется:**
- Planning workflow (4 этапа) ✅
- Plan format (markdown structure) ✅
- Best practices philosophy ✅
- Risk management approach ✅

**Что адаптируется:**
- File extensions (.ts → .py)
- Test file naming conventions
- Python-specific red flags
- Project structure patterns

**Что добавляется:**
- Python-specific anti-patterns (circular imports, mutable defaults)
- `__init__.py`, `__main__.py` patterns
- Migration tools (Alembic, Django migrations)

---

### Рекомендация:

✅ **Для любого software проекта**: Отличный, универсальный промпт.

✅ **Для Python**: Легкая адаптация (~15%). Все концепции применимы.

🎯 **Идеален для**: Medium/large features, refactoring, breaking changes.

---

*Дата анализа: 10.04.2026*
