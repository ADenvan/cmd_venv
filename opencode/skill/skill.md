
## [Разместить файлы](https://opencode.ai/docs/ru/skills/#%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%81%D1%82%D0%B8%D1%82%D1%8C-%D1%84%D0%B0%D0%B9%D0%BB%D1%8B)

Создайте одну папку для каждого имени навыка и поместите в нее `SKILL.md`. opencode выполняет поиск в следующих местах:

- Конфигурация проекта: `.opencode/skills/<name>/SKILL.md`
- Глобальная конфигурация: `~/.config/opencode/skills/<name>/SKILL.md`.
- Совместимость с Project Claude: `.claude/skills/<name>/SKILL.md`
- Глобальная совместимость с Claude: `~/.claude/skills/<name>/SKILL.md`
- Совместимость с агентом проекта: `.agents/skills/<name>/SKILL.md`
- Совместимость с глобальным агентом: `~/.agents/skills/<name>/SKILL.md`

## [Настройка разрешений](https://opencode.ai/docs/ru/skills/#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B9)

Контролируйте, к каким навыкам агенты могут получить доступ, используя разрешения на основе шаблонов в `opencode.json`:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "skill": {
      "*": "allow",
      "pr-review": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

| Разрешение | Поведение                                                |
| ---------- | -------------------------------------------------------- |
| `allow`    | Навык загружается немедленно                             |
| `deny`     | Навык скрыт от агента, доступ запрещен                   |
| `ask`      | Перед загрузкой запрашивается подтверждение пользователя |