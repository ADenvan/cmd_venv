# Анализ промпта: C++ Reviewer

## Описание

Промпт для code review C++ кода с акцентом на memory safety, concurrency и modern C++ best practices. Использует `clang-tidy` и `cppcheck` для статического анализа. Структурирован по приоритетам: CRITICAL (memory safety, security) → HIGH (concurrency, code quality) → MEDIUM (performance, best practices).

---

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Узко специализированный |
| **Задача** | Code Review (C++) |
| **Целевой язык** | C++ |
| **Совместимость с Python** | **~5%** (только security базовые) |

---

## Технологии

| Инструмент | Назначение |
|------------|------------|
| `clang-tidy` | C++ статический анализ |
| `cppcheck` | Легковесный C++ анализатор |
| `git diff` | Выбор C++ файлов |
| CMake | Build система |

---

## Совместимость с Python

### ❌ Минимальная совместимость (~5%)

| C++ специфика | Python эквивалент | Совместимость |
|---------------|-------------------|---------------|
| Raw new/delete | Garbage collection | ❌ Разные парадигмы |
| Buffer overflows | Нет (безопасные списки) | ❌ Не актуально |
| Use-after-free | Нет (GC) | ❌ Не актуально |
| RAII | Context managers | ⚠️ Похожая концепция |
| Concurrency (mutex, threads) | `threading`, `asyncio` | ⚠️ Принципы похожи |
| Const correctness | Нет | ❌ Python динамический |
| Move semantics | Нет | ❌ Не применимо |
| Include guards | Модули | ❌ Разная система |
| Hardcoded secrets | Аналогично | ✅ Security общий |
| Integer overflow | Нет (unbounded int) | ❌ Разные типы |

### Что можно переиспользовать:

| Элемент | Переиспользование |
|---------|-------------------|
| Security (hardcoded secrets) | ✅ Да |
| Git diff workflow | ✅ Да (заменить паттерны файлов) |
| 3-уровневая приоритизация | ✅ Да (CRITICAL/HIGH/MEDIUM) |
| Approval criteria | ✅ Да (Approve/Warning/Block) |
| Формат output | ✅ Да |
| Memory safety checks | ❌ Нет (Python managed) |
| RAII → Context managers | ⚠️ Концептуально похоже |
| Concurrency checks | ⚠️ Частично (data races, deadlocks) |

---

## Когда использовать

| Сценарий | Полезность |
|----------|------------|
| C++ code review | ⭐⭐⭐⭐⭐ |
| Проверка modern C++ practices | ⭐⭐⭐⭐⭐ |
| Memory safety audit | ⭐⭐⭐⭐⭐ |
| Concurrency review | ⭐⭐⭐⭐ |
| Python code review | ❌ Не применимо |
| Mixed C++/Python (pybind11) | ⭐⭐ (только для C++ части) |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (C++) | 10/10 |
| Компактность | 9/10 (65 строк) |
| Универсальность | 1/10 (только C++) |
| **Совместимость с Python** | **1/10** |

### Рекомендация:

✅ **Для C++**: Отличный, компактный промпт. Memory safety + concurrency + modern C++ — полный набор.

❌ **Для Python**: Не использовать. Security только пересекается (~5%). Использовать `code-reviewer.txt` (адаптированный ~25%).

⚠️ **Mixed проекты**: Для C++ части (pybind11, ctypes extensions).

---

*Дата анализа: 10.04.2026*
