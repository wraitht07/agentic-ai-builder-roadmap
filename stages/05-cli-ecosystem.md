# Stage 5 — CLI Ecosystem (Track A – CLI Power User)

Goal: become highly effective with modern coding agents that live in the terminal or IDE (Claude Code, Codex, Cursor, OpenCode, Aider, etc.).

## Learning Goals

- Choose and configure one primary CLI / IDE agent
- Write effective PRDs and acceptance criteria that the agent can follow
- Use plan-mode / ask-mode before allowing edits
- Review every diff and force validation steps

## Recommended tools (pick 1–2 to master)

- Claude Code / Claude in Cursor
- OpenAI Codex / Codex CLI
- Cursor (with agent mode)
- OpenCode, Aider, Continue, etc.

## Core workflow for Track A

1. Write a clear PRD or task description (see `docs/spec-driven-agent-workflows.md`)
2. Ask the agent for a plan first
3. Approve or refine the plan
4. Allow only the minimum files to be edited
5. Require tests or manual checks after every meaningful change
6. Review the diff yourself before accepting

## Hands-on Practice

1. Pick a small real repository (or create one).
2. Give the agent a well-specified task that requires reading 2–3 files and making a focused change.
3. Force it to propose a plan first.
4. Deliberately give a vague task and observe how the agent goes wrong.
5. Add an explicit “never invent files or APIs” constraint and re-test.

## Completion Check

- [ ] You have a personal template for PRDs / task specs
- [ ] You can make an agent follow a plan instead of freelancing
- [ ] You catch at least one hallucinated file path or incorrect assumption in a real session

## Deep dive

- Official docs of the CLI agent you chose
- This repo’s `docs/spec-driven-agent-workflows.md` and `docs/hallucination-detection.md`

## Next

→ Stage 6 (Memory & RAG) if you need knowledge grounding, or jump to production practices in Stage 7.
