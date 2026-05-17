# Анализ промпта: Harness Optimizer

## Описание

Промпт для **оптимизации конфигурации агентских систем** (harness). Специализация: **meta-optimization** — улучшение работы самого агента, а не продукта. Использует внешний аудит `/harness-audit` для измерения качества.

---

## Конфигурация и направление

### Что оптимизируется:

| Компонент | Назначение |
|-----------|------------|
| **Hooks** | Pre/post-action обработчики |
| **Evals** | Метрики качества выполнения |
| **Routing** | Выбор подходящего агента для задачи |
| **Context** | Управление контекстом запроса |
| **Safety** | Безопасность выполнения |

### Workflow:

```
Baseline → Identify → Propose → Apply → Validate → Report
```

---

## Концепция Harness

### Harness — это:

**Инфраструктура управления агентами**, которая:
- Запускает агентов (runner/executor)
- Конфигурирует окружение (context, tools)
- Мониторит выполнение (evals, metrics)
- Обеспечивает безопасность (sandbox, constraints)

### Примеры Harness систем:

| Система | Тип |
|---------|-----|
| **OpenCode** | Local agent harness |
| **Claude Code** | Anthropic harness |
| **Cursor Agent** | IDE-integrated harness |
| **Codex CLI** | OpenAI harness |
| **Custom Python harness** | Самописный (CrewAI, AutoGen) |

---

## Универсальность

### Независимость от языка программирования: **10/10**

| Критерий | Оценка |
|----------|--------|
| Конфигурация vs Code | Конфигурация |
| Привязка к Python | Нет |
| Привязка к TypeScript | Нет |
| Cross-platform | Да |

**Этот промпт не связан с кодом продукта** — он работает на уровне инфраструктуры агентов.

---

## Применимость к Python разработке

### Польза в Python проектах:

| Сценарий | Полезность |
|----------|------------|
| **CrewAI / AutoGen** | ⭐⭐⭐⭐⭐ Конфигурация multi-agent systems |
| **LangChain агенты** | ⭐⭐⭐⭐⭐ Оптимизация tool selection |
| **LLM-based CLI tools** | ⭐⭐⭐⭐ Оптимизация контекста и routing |
| **Jupyter AI** | ⭐⭐⭐ Настройка контекста cells |
| **Обычная разработка** | ⭐ Минимальная (нет агентской инфраструктуры) |

### Python-специфичное применение:

```python
# Пример "harness" в Python (CrewAI)
from crewai import Agent, Task, Crew

# Агенты — аналог "subagents"
researcher = Agent(
    role='Researcher',
    goal='Find information',
    tools=[search_tool]
)

# Оптимизация harness = настройка:
# - context window
# - tool routing
# - eval metrics
# - safety constraints

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    # Harness config:
    process='sequential',  # routing
    memory=True,           # context
    max_rpm=10             # safety/rate limiting
)
```

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 9/10 |
| Практическая ценность (meta-level) | 9/10 |
| Компактность | 9/10 (27 строк — отлично) |
| Универсальность | **10/10** |
| **Применимость к Python** | **6/10** |

### Применимость к Python разработке: **6/10**

**Ограничения:**
- Требует агентской инфраструктуры (CrewAI, AutoGen, LangChain)
- Большинство Python проектов — не agent-based
- OpenCode/Claude Code harness — не Python-native

**Польза:**
- Если используются LLM-агенты в Python — высокая
- Для оптимизации AI assistants в Python codebase — применимо

---

### Рекомендация:

✅ **Для agent-based разработки** (CrewAI, AutoGen, LangChain): Отличный, компактный промпт для meta-optimization.

⚠️ **Для обычной Python разработки**: Промпт не применим — требует агентской инфраструктуры.

🎯 **Языконезависимый** — работает с любым harness (OpenCode, Claude Code, Cursor, Codex, CrewAI).

---

*Дата анализа: 10.04.2026*
