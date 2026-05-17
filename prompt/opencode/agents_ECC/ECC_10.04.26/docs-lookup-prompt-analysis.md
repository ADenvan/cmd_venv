# Анализ промпта: Docs Lookup

## Описание

Промпт для поиска документации библиотек и фреймворков через внешний инструмент **Context7 MCP**. Специализация: **универсальный documentation lookup** — не зависит от языка программирования. Использует external API для получения актуальной документации вместо training data.

---

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Универсальный |
| **Задача** | Documentation Lookup (library/framework/API) |
| **Направление** | External documentation retrieval |
| **Применимость к Python** | **~95%** (отличная) |

---

## Технологии

### Context7 MCP (Model Context Protocol)

| Компонент | Назначение |
|-----------|------------|
| **`resolve-library-id`** | Поиск library ID по названию |
| **`query-docs`** | Запрос документации по library ID |

### Как работает:

```
User Question → resolve-library-id → libraryId → query-docs → Documentation → Answer
```

**Ограничения workflow:**
- Максимум 3 вызова на запрос
- Fallback на training data если Context7 недоступен

---

## Python-специфика

### Применимость к Python: ~95%

| Аспект | Поддержка |
|--------|-----------|
| **Python stdlib** | ✅ Через Context7 (docs.python.org) |
| **PyPI packages** | ✅ Большинство популярных |
| **Python versions** | ✅ Конкретные версии библиотек |
| **Code examples** | ✅ Возвращаются с документацией |

### Python библиотеки (примеры):

| Библиотека | Context7 поддержка |
|------------|-------------------|
| Django | ✅ Высокая |
| Flask | ✅ Высокая |
| FastAPI | ✅ Высокая |
| SQLAlchemy | ✅ Высокая |
| requests | ✅ Высокая |
| numpy | ✅ Высокая |
| pandas | ✅ Высокая |
| pytest | ✅ Средняя |

---

## Универсальность

### Поддерживаемые языки и платформы:

| Категория | Примеры |
|-----------|---------|
| **Python** | Django, Flask, FastAPI, SQLAlchemy |
| **JavaScript/TypeScript** | Next.js, React, Express |
| **Go** | Gin, Echo, GORM |
| **Rust** | Axum, Actix, Tokio |
| **Java** | Spring, Hibernate |
| **Базы данных** | PostgreSQL, MongoDB, Redis |
| **Cloud** | AWS SDK, Supabase, Firebase |

### Оценка универсальности: **9/10**

| Критерий | Балл |
|----------|------|
| Языконезависимость | 10/10 |
| Платформонезависимость | 10/10 |
| Технология агностичность | 9/10 |
| Security awareness | 8/10 (prompt injection resistance) |

---

## Ограничения

### Контекст7 MCP:

| Ограничение | Описание |
|-------------|----------|
| **External dependency** | Требует работающего Context7 MCP сервера |
| **Library coverage** | Не все библиотеки проиндексированы |
| **Rate limiting** | 3 вызова максимум на запрос |
| **Offline mode** | Не работает без интернета/MCP |

### Fallback strategy:

Если Context7 недоступен → использует training data с оговоркой "docs may be outdated".

---

## Сравнение с аналогами

| Подход | Универсальность | Актуальность |
|--------|-----------------|--------------|
| **Context7 MCP** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ (real-time) |
| **Training data only** | ⭐⭐⭐⭐⭐ | ⭐⭐ (устаревает) |
| **Web search** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Local docs** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ (если обновлены) |

---

## Когда использовать

| Сценарий | Полезность |
|----------|------------|
| Вопросы про API библиотек | ⭐⭐⭐⭐⭐ |
| Актуальная документация (versions) | ⭐⭐⭐⭐⭐ |
| Code examples из docs | ⭐⭐⭐⭐⭐ |
| Сравнение library versions | ⭐⭐⭐⭐ |
| Offline development | ⭐⭐ (fallback на knowledge) |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность | 9/10 |
| Компактность | 9/10 (57 строк) |
| Универсальность | **9/10** |
| **Применимость к Python** | **9.5/10** |

### Рекомендация:

✅ **Отличный универсальный промпт**. Не требует адаптации под Python — Context7 MCP языконезависимый.

⚠️ **Зависимость от внешнего сервиса** — требует настройки Context7 MCP. Без него fallback на training data.

🎯 **Идеален для:** projects с множеством dependencies, где нужны актуальные API docs.

---

*Дата анализа: 10.04.2026*
