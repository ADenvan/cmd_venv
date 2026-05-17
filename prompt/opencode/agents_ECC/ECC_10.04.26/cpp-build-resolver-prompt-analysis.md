# Анализ промпта: C++ Build Resolver

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Узко специализированный |
| **Задача** | Исправление ошибок сборки C++ |
| **Целевой язык** | C++ (из коробки) |
| **Совместимость с Python** | **0% — несовместимы** |

---

## Подходящие категории

- **Build/DevOps** — C++ специфика
- **Compiler/Linker** — низкоуровневые ошибки
- **CMake Configuration** — build system

---

## Четкость задачи

✅ **Высокая четкость**

Промпт четко определен для C++:
- 5 core responsibilities
- 10 паттернов ошибок с таблицей
- Diagnostic workflow (cmake → build → test)
- Stop conditions (3 правила)
- Формат output

---

## Технологии

### Из коробки поддерживает:

| Технология | Назначение |
|------------|------------|
| **CMake** | Build system |
| **clang-tidy** | C++ линтер |
| **cppcheck** | Статический анализ |
| **ctest** | Тестирование |
| **GCC/Clang linker** | Компиляция/линковка |

### C++-специфичные концепции:

- Templates instantiation errors
- Forward declarations
- Header guards / `#include`
- Undefined references (linker)
- Multiple definitions (ODR)
- `inline` functions
- Type casting

---

## Совместимость с Python

### ❌ Полная несовместимость (0%)

| C++ концепция | Python эквивалент | Проблема |
|---------------|-------------------|----------|
| CMake | `setuptools`, `poetry`, `pip` | Разные парадигмы |
| Linker errors | Нет (интерпретируемый) | Python не компилируется |
| Templates | Generics (typing) | Семантически разное |
| Header files | Модули/imports | Разная система |
| Undefined reference | ImportError | Диагностика отличается |
| Forward declaration | Не требуется | Python динамический |
| clang-tidy | `mypy`, `pylint`, `ruff` | Можно заменить, но паттерны ошибок другие |

### Почему несовместимо:

1. **C++ компилируется** → Python интерпретируется
2. **Linker этап** → в Python отсутствует
3. **Templates** → в Python generics (`typing` module)
4. **Header/Implementation** → в Python `.py` файлы
5. **CMake** → в Python `pyproject.toml`, `setup.py`

### Что можно переиспользовать:

| Элемент | Переиспользование |
|---------|-------------------|
| Workflow (4 этапа) | ✅ Да (диагностика → фикс → верификация) |
| "Surgical fixes only" | ✅ Да (философия minimal changes) |
| "One fix at a time" | ✅ Да (итеративный подход) |
| Output format | ✅ Да (стандартизированный отчет) |
| Stop conditions | ✅ Да (3 попытки, регрессия, scope) |
| Table of patterns | ❌ Нет (C++-специфичные ошибки) |
| Diagnostic commands | ❌ Нет (cmake, clang-tidy, cppcheck) |

---

## Когда использовать

| Сценарий | Полезность |
|----------|------------|
| C++ проект не собирается | ⭐⭐⭐⭐⭐ |
| CMake configuration errors | ⭐⭐⭐⭐⭐ |
| Linker undefined references | ⭐⭐⭐⭐⭐ |
| Template instantiation | ⭐⭐⭐⭐⭐ |
| Python build errors | ❌ Не применимо |
| Mixed C++/Python проект (pybind11, etc.) | ⭐⭐⭐ (только для C++ части) |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (C++) | 10/10 |
| Компактность | 9/10 (81 строка) |
| Универсальность | 2/10 (только C++) |
| **Совместимость с Python** | **0/10 (несовместимы)** |

### Рекомендация:

✅ **Для C++ проектов**: Отличный, компактный промпт. 10 паттернов ошибок, четкий workflow, surgical fixes философия.

❌ **Для Python**: Не использовать. Использовать `build-error-resolver.txt` (TypeScript-based) и адаптировать под Python с ~45% изменений.

⚠️ **Для mixed проектов** (C++ + Python): Использовать только для C++ части (например, pybind11, Cython extensions).

---

*Дата анализа: 10.04.2026*
