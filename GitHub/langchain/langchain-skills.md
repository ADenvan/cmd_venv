
- [langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills)
*Доступные навыки (21) [langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills)*

#### Установите официальный скилл LangChain

Эта команда скачает инструкции по LangChain и привяжет их к OpenCode, используя безопасное копирование файлов (без проблем с правами на символы в Windows):

```bash
# Установить только один или несколько конкретных скиллов
npx skills add langchain-ai/langchain-skills --skill langchain-rag --agent opencode --copy -y
# Или используйте более компактный синтаксис (если имена скиллов не содержат пробелов):
npx skills add langchain-ai/langchain-skills --skill langchain-rag,eval-engineering,langchain-middleware-hitl --agent opencode --copy -y
```

**Разбор флагов:**

| Флаг/Аргумент      | Описание                                                                                                                                       |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `--agent opencode` | жестко указывает инструменту, что скиллы нужны именно для OpenCode (он положит их в правильную папку `.agents/skills/` внутри вашего проекта). |
| `--skill <name>`   | **ЧТО устанавливать** — выбирает конкретные скиллы из репозитория (если не указан, устанавливает все)                                          |
| `--copy`           | копирует файлы физически, а не создает ссылки. Это самый беспроблемный метод для Windows.                                                      |
| `-y` (или `--yes`) | автоматически отвечает "да" на все вопросы, делая установку неинтерактивной и мгновенной.                                                      |
| `--global, -g`     | Установить глобально вместо текущего каталога                                                                                                  |


```bash
# можете посмотреть список всех доступных скиллов в репозитории:
npx skills add langchain-ai/langchain-skills --list
# Выполните команду, чтобы увидеть список установленных скиллов для OpenCode в этой папке:
npx skills list --agent opencode
```





