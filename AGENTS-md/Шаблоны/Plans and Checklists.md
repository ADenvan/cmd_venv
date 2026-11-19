
# How to Create Plans and Checklists

Every plan for a new task must be delivered as highly detailed implementation and execution guidelines in Markdown format.

Plans are saved to `docs/plans/<date-time>/plan-<feature-name>.md` and their corresponding checklists to `docs/plans/<date-time>/checklist-<feature-name>.md`.

Each plan must include:
- Full context of the task
- Step-by-step execution instructions
- Implementation specifics and nuances

Each checklist must cover:
- A summary of what was implemented
- Detailed verification steps to confirm all implementation details are in place and consistent with the original plan and intent

If a plan spans multiple stages, create a separate plan and checklist file per stage so they can be executed one at a time. Each subsequent stage must reference and build on the previous one to maintain consistent context throughout the implementation.

After completing each stage, run the `/simplify` skill to optimize the implementation, then run the checklist to verify the results.



# Как создавать планы и чек-листы

План для каждой новой задачи должен быть оформлен в виде подробного руководства по реализации и выполнению в формате Markdown.

Планы сохраняются по пути `docs/plans/<date-time>/plan-<feature-name>.md`, а соответствующие им чек-листы — по пути `docs/plans/<date-time>/checklist-<feature-name>.md`.

Каждый план должен содержать:
- Полный контекст задачи
- Пошаговые инструкции по выполнению
- Особенности и нюансы реализации

Каждый чек-лист должен включать:
- Краткий обзор выполненной реализации
- Подробные шаги для проверки того, что все элементы реализации на месте и соответствуют исходному плану и замыслу

Если план охватывает несколько этапов, создавайте отдельные файлы плана и чек-листа для каждого этапа, чтобы их можно было выполнять последовательно. Каждый последующий этап должен ссылаться на предыдущий и опираться на него для сохранения целостности контекста в процессе реализации.

После завершения каждого этапа используйте команду `/simplify` для оптимизации реализации, а затем выполните проверку по чек-листу.

