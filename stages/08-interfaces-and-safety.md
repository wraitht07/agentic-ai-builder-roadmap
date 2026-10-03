# Stage 8 — Interfaces and Safety

Goal: decide how users (or other systems) will interact with your agent, and lock down the safety boundaries.

## Learning Goals

- Choose an appropriate interface (CLI, chat UI, API, IDE plugin, batch job)
- Define clear permission boundaries and threat models
- Handle secrets, rate limits and cost controls
- Know what must remain human-owned

## Interface options

| Interface | Best for | Notes |
|-----------|----------|-------|
| Terminal / CLI | Developers, power users, Track A | Fast iteration |
| Chat UI (Streamlit, Gradio, web) | Non-technical users, demos | Add approval buttons |
| REST / FastAPI service | Integration into existing systems | Stateless + session store |
| IDE / editor plugin | Coding agents | Tight file & git integration |
| Batch / scheduled | Overnight reports, data pipelines | Full logging required |

## Safety checklist (minimum)

- [ ] Secrets never appear in prompts or logs
- [ ] Tools are least-privilege by default (read-only first)
- [ ] Destructive actions require explicit human confirmation
- [ ] Max steps, max cost and timeouts are enforced
- [ ] Every run is logged with a trace ID
- [ ] You have a clear “this is outside the agent’s authority” list

## Hands-on Practice

1. Take one of your earlier agents.
2. Expose it through the simplest interface that matches the real user (CLI is fine).
3. Add the safety checklist items above.
4. Write a short threat model: who could misuse it and how you prevent it.

## Completion Check

- [ ] Interface is usable by the intended audience
- [ ] Safety checklist is fully implemented
- [ ] You can explain the residual risks in plain language

## Capstone direction

After Stage 8 you are ready for the projects in `/projects` or a personal graduation design (Hello-Agents Chapter 16 style) focused on a real MSME / plant / GovTech workflow.

## Deep dive

- Hello-Agents Chapters 10 (protocols) and 13–16 (case studies + graduation)
- MCP documentation for tool interoperability
