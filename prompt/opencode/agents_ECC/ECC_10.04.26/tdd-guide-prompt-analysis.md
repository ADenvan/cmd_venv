# Анализ промпта: TDD Guide

## Описание

Промпт для **Test-Driven Development (TDD)** — разработка через тестирование. Специализация: **Red-Green-Refactor цикл** с обязательным покрытием 80%+. Фокус на test-first methodology.

---

## Направление задачи

### Core Responsibilities:

| Область | Задача |
|---------|--------|
| **TDD Enforcement** | Tests-before-code methodology |
| **Red-Green-Refactor** | Guiding через TDD цикл |
| **Coverage Target** | 80%+ test coverage (branches, functions, lines) |
| **Test Types** | Unit, Integration, E2E |
| **Edge Cases** | Null, empty, invalid, boundaries, errors |

### TDD Workflow (Red-Green-Refactor):

```
1. Write Test (RED)     → Тест падает (функция не реализована)
2. Run Test             → Verify FAILS
3. Minimal Code (GREEN) → Минимальная реализация
4. Run Test             → Verify PASSES
5. Refactor             → Улучшение без изменения поведения
6. Verify Coverage      → 80%+
```

---

## Применимость к задачам

### Когда использовать:

| Сценарий | Полезность |
|----------|------------|
| **Новая фича** | ⭐⭐⭐⭐⭐ Идеально для TDD |
| **Bug fix** | ⭐⭐⭐⭐⭐ Тест воспроизводит баг |
| **Refactoring** | ⭐⭐⭐⭐⭐ Тесты как safety net |
| **Legacy code** | ⭐⭐ Сложно применить TDD |
| **Hotfix** | ⭐ Давление времени, тесты после |
| **Spike/Research** | ⭐ Неизвестный scope |

### Test Types:

1. **Unit Tests** — обязательно (isolated functions)
2. **Integration Tests** — обязательно (API endpoints)
3. **E2E Tests** — critical flows (user journeys)

---

## Адаптация под Python

### Оценка: ~25% изменений

**Есть ли смысл адаптировать?** — ✅ **Да, TDD универсален!**

| TS/JS Концепция | Python Эквивалент | Изменения |
|-----------------|-------------------|-----------|
| **Test framework** | Jest → **pytest** | Синтаксис |
| **Coverage** | jest --coverage → **pytest-cov** | 10% |
| **Assertions** | `expect().toBe()` → `assert` | Синтаксис |
| **Mocking** | jest.mock → **unittest.mock** | 20% |
| **E2E** | Playwright → **pytest-playwright** | 10% |

### Python инструменты для TDD:

| Инструмент | Назначение | Команда |
|------------|------------|---------|
| **pytest** | Основной test framework | `pytest` |
| **pytest-cov** | Coverage measurement | `pytest --cov=src --cov-report=term-missing` |
| **unittest.mock** | Mocking (stdlib) | `from unittest.mock import Mock, patch` |
| **pytest-playwright** | E2E testing | `pytest --headed` |
| **pytest-asyncio** | Async test support | `@pytest.mark.asyncio` |

### Python TDD Workflow:

```bash
# 1. Write test first (RED)
# tests/test_calculator.py
def test_add():
    assert add(2, 3) == 5  # Функция не существует → FAIL

# 2. Run test → Verify FAILS
pytest tests/test_calculator.py -v
# FAILED - NameError: name 'add' is not defined

# 3. Write minimal code (GREEN)
# src/calculator.py
def add(a, b):
    return a + b

# 4. Run test → Verify PASSES
pytest tests/test_calculator.py -v
# PASSED

# 5. Refactor → Улучшение
# 6. Check coverage
pytest --cov=src --cov-report=term-missing
```

### Python Test Examples:

#### Unit Test:

```python
# tests/test_utils.py
import pytest
from src.utils import calculate_similarity

class TestCalculateSimilarity:
    def test_identical_embeddings(self):
        """Returns 1.0 for identical embeddings."""
        embedding = [0.1, 0.2, 0.3]
        assert calculate_similarity(embedding, embedding) == 1.0

    def test_orthogonal_embeddings(self):
        """Returns 0.0 for orthogonal embeddings."""
        a = [1, 0, 0]
        b = [0, 1, 0]
        assert calculate_similarity(a, b) == 0.0

    def test_null_raises_error(self):
        """Raises error for null input."""
        with pytest.raises(ValueError):
            calculate_similarity(None, [])
```

#### Integration Test (FastAPI):

```python
# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

class TestMarketSearch:
    def test_search_returns_200(self):
        """Returns 200 with valid results."""
        response = client.get("/api/markets/search?q=trump")
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert len(data["results"]) > 0

    def test_missing_query_returns_400(self):
        """Returns 400 for missing query parameter."""
        response = client.get("/api/markets/search")
        assert response.status_code == 400
```

#### E2E Test (pytest-playwright):

```python
# tests/test_e2e.py
import pytest
from playwright.sync_api import Page, expect

def test_user_can_search_and_view_market(page: Page):
    """User can search and view market."""
    page.goto("/")
    
    # Search for market
    page.fill('input[placeholder="Search markets"]', "election")
    page.wait_for_timeout(600)  # Debounce
    
    # Verify results
    results = page.locator('[data-testid="market-card"]')
    expect(results).to_have_count(5, timeout=5000)
    
    # Click first result
    results.first.click()
    
    # Verify market page loaded
    expect(page).to_have_url(r".*\/markets\/.*")
    expect(page.locator("h1")).to_be_visible()
```

---

## Сравнение с Code Reviewer

### Что умеет Code Reviewer:

| Аспект | Code Reviewer | TDD Guide |
|--------|---------------|-----------|
| **TDD enforcement** | ⚠️ Упоминает "test coverage" | ✅ Red-Green-Refactor workflow |
| **Test writing** | ❌ Упоминает как check | ✅ Подробное руководство |
| **Test types** | ⚠️ Упоминает | ✅ Unit/Integration/E2E разбор |
| **Edge cases** | ✅ Упоминает | ✅ Систематический список (8 типов) |
| **Test smells** | ❌ Нет | ✅ Anti-patterns с примерами |
| **Coverage** | ✅ "80%+" | ✅ Конкретные thresholds |
| **Quality checklist** | ✅ Есть | ✅ Расширенный (тест-специфичный) |

### Эффективность:

| Сценарий | TDD Guide | Code Reviewer |
|----------|-----------|---------------|
| **Разработка новой фичи** | ⭐⭐⭐⭐⭐ Отлично | ⭐⭐⭐ Общие рекомендации |
| **Code review существующего** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ Лучше |
| **Обучение TDD** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Coverage audit** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Test maintenance** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Общий code quality** | ⭐⭐ | ⭐⭐⭐⭐⭐ Лучше |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (TDD) | 10/10 |
| Компактность | 7/10 (211 строк — подробно) |
| Универсальность (TDD концепции) | **9/10** |
| **Применимость к Python** | **8.5/10** |

### Оценка адаптации под Python: **~25%**

**Что сохраняется (универсальное):**
- Red-Green-Refactor workflow ✅
- TDD philosophy ✅
- Edge case patterns ✅
- Test smells / anti-patterns ✅
- Quality checklist ✅

**Что адаптируется:**
- Jest → pytest (синтаксис) 🔧
- TypeScript → Python (type hints) 📝
- `expect()` → `assert` 📝
- npm → pytest commands 📝

**Что добавляется для Python:**
- `@pytest.fixture` для setup
- `@pytest.mark.parametrize` для DRY
- `unittest.mock` для mocking
- Python async testing (`pytest-asyncio`)

---

### Рекомендация:

✅ **Для Python TDD**: Отличная база. pytest — мощный и гибкий framework, адаптация минимальна (~25%).

✅ **Сравнение с Code Reviewer**: TDD Guide — для процесса разработки (test-first). Code Reviewer — для review существующего кода. Использовать вместе.

🎯 **Python TDD рекомендация**: pytest + pytest-cov + unittest.mock — стандартный стек для Python TDD.

---

*Дата анализа: 10.04.2026*
