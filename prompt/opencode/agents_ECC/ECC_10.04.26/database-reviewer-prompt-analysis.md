# Анализ промпта: Database Reviewer

## Описание

Промпт для PostgreSQL database review с акцентом на query optimization, schema design, security (RLS) и performance. Включает Supabase best practices. Структурирован по паттернам: indexes, schema design, RLS, concurrency, data access.

---

## Общая характеристика

| Параметр | Оценка |
|----------|--------|
| **Специализация** | Узко специализированный (PostgreSQL) |
| **Задача** | Database Review (SQL) |
| **Целевой движок** | PostgreSQL (+ Supabase extensions) |
| **Применимость к Python** | **~85%** (отличная) |

---

## Технологии

| Технология | Назначение |
|------------|------------|
| **PostgreSQL** | Реляционная БД |
| **psql** | CLI клиент |
| **pg_stat_statements** | Monitoring |
| **Supabase RLS** | Row Level Security |
| **UUIDv7** | Distributed IDs |

---

## Совместимость с Python

### ✅ Отличная применимость (~85%)

Python широко использует PostgreSQL через различные библиотеки:

| Библиотека | Применимость промпта |
|------------|----------------------|
| **psycopg2/psycopg3** | ⭐⭐⭐⭐⭐ 100% (raw SQL) |
| **SQLAlchemy** | ⭐⭐⭐⭐ 80% (ORM + raw queries) |
| **Django ORM** | ⭐⭐⭐⭐ 75% (ORM abstracts SQL) |
| **asyncpg** | ⭐⭐⭐⭐⭐ 100% (async raw SQL) |
| **pg8000** | ⭐⭐⭐⭐⭐ 100% (pure Python driver) |

### Что переиспользуется с Python:

| Элемент | Python-применимость |
|---------|---------------------|
| Index patterns (B-tree, GIN, BRIN) | ✅ 100% (через DDL или Alembic) |
| Data type selection | ✅ 100% (SQLAlchemy types, Django fields) |
| RLS policies | ✅ 100% (raw SQL или sqlalchemy-rls) |
| N+1 elimination | ✅ 100% (ORM `select_related`, `prefetch_related`) |
| Cursor pagination | ✅ 100% (ручная реализация) |
| SKIP LOCKED | ✅ 100% (asyncpg, psycopg) |
| Connection pooling | ✅ 100% (psycopg2.pool, asyncpg pool) |
| EXPLAIN ANALYZE | ✅ 100% (все библиотеки поддерживают) |

### Ограничения с Python ORM:

| Концепция | ORM Limitation |
|-----------|----------------|
| Composite indexes | Django: поддерживается, SQLAlchemy: да |
| GIN indexes на JSONB | Django: `GinIndex`, SQLAlchemy: да |
| RLS policy syntax | Нужен raw SQL или extension |
| SKIP LOCKED | SQLAlchemy 1.4+, Django: raw SQL |
| Cursor pagination | Ручная реализация |

---

## Когда использовать с Python

| Сценарий | Полезность |
|----------|------------|
| Raw SQL queries (psycopg2/asyncpg) | ⭐⭐⭐⭐⭐ |
| SQLAlchemy Core (not ORM) | ⭐⭐⭐⭐⭐ |
| SQLAlchemy ORM queries | ⭐⭐⭐⭐ |
| Django ORM + raw SQL | ⭐⭐⭐⭐ |
| Django ORM only | ⭐⭐⭐ (ORM скрывает SQL) |
| Database schema design | ⭐⭐⭐⭐⭐ |
| Migration review (Alembic, Django) | ⭐⭐⭐⭐⭐ |
| Performance optimization | ⭐⭐⭐⭐⭐ |

---

## Другие технологии (краткая оценка)

| Технология | Совместимость | Примечание |
|------------|---------------|------------|
| **MySQL/MariaDB** | ⚠️ 40% | Синтаксис отличается (LIMIT vs FETCH, нет SKIP LOCKED) |
| **SQLite** | ⚠️ 50% | Нет RLS, BRIN, GIN, concurrency ограничена |
| **MongoDB** | ❌ 0% | NoSQL, документная модель |
| **Redis** | ❌ 0% | Key-value, другая парадигма |
| **Cassandra** | ❌ 0% | Wide-column, другая модель |
| **MS SQL** | ⚠️ 30% | Синтаксис сильно отличается |
| **Oracle** | ⚠️ 25% | Проприетарные фичи |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность (PostgreSQL) | 10/10 |
| Компактность | 7/10 (247 строк) |
| Универсальность (SQL) | 6/10 (только PostgreSQL) |
| **Применимость к Python** | **8.5/10** |

### Рекомендация:

✅ **Для Python + PostgreSQL**: Отличный промпт. 85% паттернов применимы напрямую. С ORM нужно знать когда ORM генерирует неоптимальный SQL.

⚠️ **Для других SQL БД**: Требует адаптации синтаксиса (~40% изменений для MySQL).

❌ **Для NoSQL**: Не применим.

---

*Дата анализа: 10.04.2026*
