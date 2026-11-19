
## Workflow Orchestration

### 1. Plan Node Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately – don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One tack per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes – don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests – then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

---

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

---

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.



## Организация рабочего процесса

### 1. Обязательное планирование
- Переходите в режим планирования для ЛЮБОЙ нетривиальной задачи (3 и более шагов или архитектурные решения).
- Если что-то идет не так, НЕМЕДЛЕННО остановитесь и пересмотрите план — не пытайтесь «пробиться» напролом.
- Используйте режим планирования не только для реализации, но и для этапов проверки.
- Заранее составляйте подробные спецификации, чтобы исключить двусмысленность.

### 2. Стратегия использования субагентов
- Активно привлекайте субагентов, чтобы не перегружать основное окно контекста.
- Делегируйте субагентам задачи по исследованию, изучению и параллельному анализу.
- При решении сложных проблем задействуйте дополнительные вычислительные ресурсы через субагентов.
- Одна задача на одного субагента для обеспечения сфокусированного выполнения.

### 3. Цикл самосовершенствования
- После ЛЮБОГО замечания пользователя фиксируйте соответствующий паттерн в файле `tasks/lessons.md`.
- Формулируйте для себя правила, предотвращающие повторение той же ошибки.
- Бескомпромиссно дорабатывайте эти правила, пока частота ошибок не снизится.
- Просматривайте накопленный опыт (уроки) в начале работы над соответствующим проектом.

### 4. Проверка перед завершением
- Никогда не отмечайте задачу как выполненную, не убедившись в ее работоспособности.
- Сравнивайте поведение системы до и после внесенных изменений (diff), где это уместно.
- Задавайтесь вопросом: «Одобрил бы это ведущий инженер (staff engineer)?»
- Запускайте тесты, проверяйте логи, демонстрируйте корректность работы.

### 5. Стремление к элегантности (в разумных пределах)
- При внесении нетривиальных изменений остановитесь и спросите себя: «Есть ли более элегантное решение?»
- Если решение кажется «костыльным»: «Зная то, что я знаю сейчас, реализуй элегантный вариант».
- Пропускайте этот шаг для простых, очевидных исправлений — избегайте излишнего усложнения (over-engineering).
- Критически оценивайте свою работу перед тем, как представить ее.

### 6. Автономное исправление ошибок
- При получении отчета об ошибке: просто исправьте ее. Не ждите, что вас будут вести за руку
- Указывайте на логи, ошибки и упавшие тесты — а затем устраняйте их
- Не требуйте от пользователя переключения контекста
- Самостоятельно исправляйте упавшие CI-тесты без подсказок о том, как именно это сделать

---

## Управление задачами

1. **Сначала планирование**: Составьте план в файле `tasks/todo.md`, разбив его на пункты, которые можно отмечать как выполненные
2. **Согласование плана**: Зафиксируйте план (закоммитьте его) перед началом реализации
3. **Отслеживание прогресса**: Отмечайте пункты как выполненные по мере продвижения
4. **Пояснение изменений**: Кратко описывайте суть изменений на каждом этапе
5. **Документирование результатов**: Добавьте раздел с результатами проверки в `tasks/todo.md`
6. **Фиксация выводов**: Обновите `tasks/lessons.md` после внесения исправлений

---

## Основные принципы

- **Приоритет простоты**: Делайте каждое изменение максимально простым. Затрагивайте минимум кода.
- **Никакой лени**: Ищите первопричины. Избегайте временных «заплаток». Работайте по стандартам Senior-разработчика.
- **Минимальное вмешательство**: Изменения должны затрагивать только необходимое. Не допускайте появления новых ошибок.