# Анализ промпта: Security Reviewer

## Описание

Промпт для **security review** web applications с фокусом на OWASP Top 10. Специализация: **vulnerability detection** — выявление и исправление уязвимостей до production. Очень JS/TS-ориентирован, но security концепции универсальны.

---

## Направление задачи

### Core Responsibilities:

| Область | Задача |
|---------|--------|
| **Vulnerability Detection** | OWASP Top 10 и другие уязвимости |
| **Secrets Detection** | Hardcoded API keys, passwords, tokens |
| **Input Validation** | Санитизация пользовательского ввода |
| **Auth/Authorization** | Проверка access controls |
| **Dependency Security** | Уязвимые npm/pip пакеты |
| **Secure Coding Patterns** | Best practices |

### OWASP Top 10 Coverage:

1. Injection (SQL, NoSQL, Command)
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Known Vulnerabilities
10. Insufficient Logging & Monitoring

---

## Технологии (из промпта)

### JS/TS инструменты:

| Инструмент | Назначение |
|------------|------------|
| **npm audit** | Уязвимые npm зависимости |
| **eslint-plugin-security** | Статический анализ security |
| **git-secrets** | Предотвращение коммита секретов |
| **trufflehog** | Поиск секретов в git history |
| **semgrep** | Pattern-based security scanning |

---

## Адаптация под Python

### Оценка: ~30% изменений

**Высокая применимость** — security концепции универсальны!

| JS/TS Инструмент | Python Эквивалент | Аналогичность |
|------------------|-------------------|---------------|
| **npm audit** | **safety** / **pip-audit** | ⭐⭐⭐⭐⭐ |
| **eslint-plugin-security** | **bandit** | ⭐⭐⭐⭐⭐ |
| **git-secrets** | **git-secrets** / **trufflehog** | ⭐⭐⭐⭐⭐ (те же инструменты) |
| **trufflehog** | **trufflehog** (универсален) | ⭐⭐⭐⭐⭐ |
| **semgrep** | **semgrep** (универсален) | ⭐⭐⭐⭐⭐ |

### Python инструменты для security:

| Инструмент | Назначение | Команда |
|------------|------------|---------|
| **bandit** | Python security linter | `bandit -r src/` |
| **safety** | Dependency vulnerability check | `safety check` |
| **pip-audit** | Alternative to safety | `pip-audit` |
| **trufflehog** | Secret detection | `trufflehog git file://.` |
| **semgrep** | Pattern-based scanning | `semgrep --config=auto src/` |
| **detect-secrets** | Alternative secret scanner | `detect-secrets scan` |

### Python Workflow (адаптация):

```bash
# 1. Check for vulnerable dependencies
safety check
# или
pip-audit

# 2. Static security analysis
bandit -r src/

# 3. Secret detection in git history
trufflehog git file://.

# 4. Pattern-based scanning
semgrep --config=auto src/
```

---

## Security Patterns — Python адаптация

### 1. Hardcoded Secrets (CRITICAL)

```python
# BAD: Hardcoded secrets
api_key = "sk-proj-xxxxx"
password = "admin123"

# GOOD: Environment variables
import os

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not configured")
```

### 2. SQL Injection (CRITICAL)

```python
# BAD: SQL injection vulnerability
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)

# GOOD: Parameterized queries (psycopg2)
cursor.execute(
    "SELECT * FROM users WHERE id = %s",
    (user_id,)
)

# GOOD: SQLAlchemy (ORM)
User.query.filter_by(id=user_id).first()

# GOOD: Django ORM
User.objects.filter(id=user_id).first()
```

### 3. Deserialization (Python-specific)

```python
# BAD: Insecure deserialization
import pickle
data = pickle.loads(user_input)  # Dangerous!

# GOOD: Safe alternatives
import json
data = json.loads(user_input)  # Safe for untrusted input

# For trusted data only
pickle.loads(trusted_data)
```

### 4. Race Conditions

```python
# BAD: Race condition (Django example)
balance = Balance.objects.get(user_id=user_id)
if balance.amount >= amount:
    balance.amount -= amount
    balance.save()  # Another request could modify in between!

# GOOD: Atomic transaction with F()
from django.db.models import F
from django.db import transaction

with transaction.atomic():
    balance = Balance.objects.select_for_update().get(user_id=user_id)
    if balance.amount >= amount:
        balance.amount = F('amount') - amount
        balance.save()
```

### 5. YAML Loading (Python-specific)

```python
# BAD: Arbitrary code execution
import yaml
data = yaml.load(user_input, Loader=yaml.Loader)  # Dangerous!

# GOOD: Safe loading
data = yaml.safe_load(user_input)
```

### 6. Path Traversal

```python
import os
from pathlib import Path

# BAD: Path traversal vulnerability
file_path = f"/uploads/{user_input}"

# GOOD: Validate path
base_path = Path("/uploads").resolve()
user_path = (base_path / user_input).resolve()

if not str(user_path).startswith(str(base_path)):
    raise ValueError("Invalid path")
```

---

## Сравнение с Code Reviewer (Security)

### Security в Code Reviewer:

| Аспект | Code Reviewer | Security Reviewer |
|--------|---------------|-------------------|
| **Coverage** | Базовый (общие checks) | Полный (OWASP Top 10) |
| **OWASP** | ⚠️ Упоминает | ✅ Детальный разбор всех 10 |
| **Secrets** | ✅ Hardcoded credentials | ✅ + git-secrets, trufflehog |
| **SQL Injection** | ✅ Упоминает | ✅ + ORM examples |
| **XSS** | ✅ Упоминает | ✅ + DOMPurify, CSP |
| **Dependencies** | ⚠️ Упоминает | ✅ + npm audit, CVE monitoring |
| **Auth/Authz** | ✅ Упоминает | ✅ + JWT, sessions, MFA |
| **Race Conditions** | ❌ Нет | ✅ + Database locks |
| **Tools** | ❌ Нет | ✅ Полный набор |
| **Report Format** | ❌ Нет | ✅ Structured security report |

### Эффективность:

| Сценарий | Security Reviewer | Code Reviewer |
|----------|-------------------|---------------|
| **Security audit** | ⭐⭐⭐⭐⭐ Отлично | ⭐⭐⭐ Базово |
| **Quick PR review** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ Лучше (general) |
| **OWASP compliance** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Dependency audit** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Secrets detection** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **General code quality** | ⭐⭐ | ⭐⭐⭐⭐⭐ Лучше |

---

## Итоговая оценка

| Критерий | Балл |
|----------|------|
| Четкость цели | 10/10 |
| Практическая ценность | 10/10 |
| Компактность | 7/10 (207 строк) |
| Универсальность (security concepts) | **9/10** |
| **Применимость к Python** | **8/10** |

### Оценка адаптации под Python: **~30%**

**Что сохраняется (универсальное):**
- OWASP Top 10 (все концепции) ✅
- Secrets detection ✅
- Injection prevention ✅
- Race conditions ✅
- Tools (trufflehog, semgrep, git-secrets) ✅

**Что адаптируется:**
- npm audit → safety/pip-audit 🔧
- eslint-plugin-security → bandit 🔧
- JS examples → Python examples 📝
- XSS specifics → Python-specific (YAML, pickle) 📝

**Что добавляется для Python:**
- `pickle` / `yaml.load` vulnerabilities
- `eval()` / `exec()` risks
- Path traversal with `pathlib`
- Django/FastAPI/Flask security specifics

---

### Рекомендация:

✅ **Для Python security audit**: Отличная база с минимальной адаптацией (~30%). Security концепции универсальны.

✅ **Сравнение с Code Reviewer**: Security Reviewer — для глубокого security audit. Code Reviewer — для общего code review с базовыми security checks.

🎯 **Использовать вместе**: Code Reviewer для PR → Security Reviewer для security audit → python-reviewer для Python-specific patterns.

---

*Дата анализа: 10.04.2026*
