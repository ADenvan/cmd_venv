










# Метрики
# SOLID/DRY как подключаемый слой

**Концепция:** Принципы усиливают ядро code-style и метрики качества

## Архитектура
- **Code-style Core** — База инженерных решений (центральное ядро)
- **SOLID** — Подключаемый слой (слева)
- **DRY** — Подключаемый слой (снизу)
- **GRASP** — Подключаемый слой (справа)

## Метрики качества
| Метрика | Значение |
|---------|----------|
| **Readability** | 79% |
| **Maintainability** | 76% |
| **Decision Speed** | 72% |






# Experts Принцип
**Принцип:** Reuse + customize вместо copy + trust
- ![programming_language](exemples\skills_programming_language.md)
# Скиллы под язык программирования
**Принцип:** Reuse + customize вместо copy + trust
## Процесс адаптации (3 этапа)

### 1. Готовый шаблон (Универсальный skill)
- ~~generic-framework-rules~~ ❌
- ~~default-checklist~~ ❌
- **common-terminology** ✅
- **base-structure** ✅

### 2. Этап адаптации
**Убрать лишнее (2 правила):**
- generic-framework-rules
- default-checklist

**Добавить контекст (4 правила):**
- + typescript-style-guide
- + domain-naming-rules
- + memory-bank-flow
- + repo-specific-constraints

### 3. Оптимизированный skill (Готов к проекту)
- typescript-style-guide
- domain-naming-rules
- memory-bank-flow
- repo-specific-constraints










# Debugging
- Методология описание 3 методов
    - ![Методология](debugging.md)
- ![ОРКЕСТРАТОР](exemples\skills_framework_orchestration.md)
    - `https://github.com/obra/superpowers`











# Minimalism principle Принцип минимализма решения
- ![principle](principle.md)

**Концепция:** На входе много кандидатов, на выходе только контекстно полезные скиллы
## Пул скиллов

| Скилл | Статус |
|-------|--------|
| auto-polish | — |
| debug-trace | — |
| prompt-linter | — |
| **api-docs-map** | ✅ Выделен |
| **ux-optimizer** | ✅ Выделен |
| full-rewriter | — |
| security-scan | — |
| **test-orchestrator** | ✅ Выделен |
| theme-generator | — |

## Принцип отбора
- **На входе:** 9 кандидатов
- **На выходе:** 3 контекстно полезных скилла (~33%)
- **Механизм:** Цветовое выделение (зеленая рамка = выбрано)

## Выбранные скиллы
1. **api-docs-map** — маппинг API документации
2. **ux-optimizer** — оптимизация UX
3. **test-orchestrator** — оркестрация тестирования













# Концептуальные скиллы и архитектура
- ![Концептуальные](exemples\conceptual_skills_architecture.md)
**Zoom-out:** file -&gt; service -&gt; module -&gt; system

## Иерархия уровней

| Уровень | Название | Содержимое |
|---------|----------|------------|
| 4 | SYSTEM | Вся система |
| 3 | MODULE BOUNDARY | Граница модуля |
| 2 | SERVICE LAYER | Сервисный слой |
| 1 | file.ts | Конкретный файл |

## Компоненты и интерфейсы

**Центр:** file.ts

**Модули:**
- **API module** — interface: request-contract
- **Data module** — interface: data-contract

## Принцип Zoom-out
file.ts → SERVICE LAYER → MODULE BOUNDARY → SYSTEM


# Поток архитектора через memory-bank
**Процесс:** Требования -&gt; план -&gt; memory-bank -&gt; реализация

## Этапы потока
| Этап | Действие | Описание |
|------|----------|----------|
| **1. Требования** | фиксируем цель | Сбор и формализация требований |
| **2. План** | строим структуру | Архитектурное планирование |
| **3. memory-bank** | сохраняем контекст | Запись контекста в memory-bank |
| **4. Реализация** | запускаем кодинг | Начало разработки |

## Центральный элемент
**memory-bank** — ключевой компонент, сохраняющий контекст между планированием и реализацией















