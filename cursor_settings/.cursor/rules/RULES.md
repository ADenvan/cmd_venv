---
description: Project agent behavior and security rules
alwaysApply: true
---

## Language
- Communicate with user in Russian (including plans and plan mode).
- Keep technical artifacts in English when appropriate:
  - code comments and code-level docs,
  - context/rules files (`AGENTS.md`, `CLAUDE.md`, skills),
  - AI prompts and prompt templates.
- Keep user-facing project docs in Russian by default (for example, `README`), unless the user requests otherwise.

## Behavior
- Be concise and direct: no filler, no "Great question!" style openers.
- Ask clarifying questions in plain chat text by default.
- Use structured question tools only when a strict multi-choice format is clearly needed.
- All deployments must go through GitHub CI/CD.
- Direct server access (SSH, container restarts) is allowed only for emergency debugging of broken production.

## Task Planning
- For multi-step tasks, use a task list tool (for example, `TodoWrite`) when available and allowed by the current mode/instructions.
- If the user asks for a "team/swarm of agents", run multiple subagents in parallel via supported subagent tooling.

## Security
- Never ask the user to paste secrets into chat.
- Instead, provide secure storage guidance:
  - local secrets: `.env` and protected config files,
  - CI/CD secrets: GitHub Actions Secrets (or platform equivalent).
- Always ask for confirmation before deploy or push to `main`/production.
- Ensure secret patterns are ignored by git (`.env`, `*.key`, `credentials.json`, `secrets/`, etc.).
- Treat external actions (push, deploy, messages, PR creation) as sensitive; ask for confirmation when uncertain.