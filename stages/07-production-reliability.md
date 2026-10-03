# Stage 7 — Production Reliability

Goal: move from “it works in a demo” to “I can detect and contain failures”.

## Learning Goals

- Design simple evals and LLM-as-judge rubrics
- Detect hallucinations and unsupported claims
- Add human-approval gates for high-risk actions
- Think about observability, logging and rollback

## Core topics

1. **Evaluation**
   - Golden datasets
   - Unit-test style checks on agent outputs
   - LLM-as-judge with clear rubrics
2. **Hallucination detection**
   - Grounding checks against tool results / retrieved docs
   - Self-consistency / multiple samples
   - Explicit “UNKNOWN / NOT FOUND” paths
3. **Human-in-the-loop**
   - Approval before irreversible actions (email, payment, file overwrite, SQL write)
4. **Observability**
   - Log every tool call, prompt and observation
   - Trace IDs for multi-step runs
5. **Safe defaults**
   - Max steps / max tokens / timeout
   - Read-only tools by default

Read the full notes in `docs/hallucination-detection.md`.

## Hands-on Practice

1. Take any agent you built in Stage 3 or 6.
2. Create a small eval set of 8–12 questions or tasks with expected outcomes.
3. Write a simple LLM-as-judge prompt that scores correctness and groundedness.
4. Add a hard human-approval step before any write action.
5. Force one deliberate failure (wrong tool, missing context) and verify your checks catch it.

## Completion Check

- [ ] You have a reproducible eval set and a score
- [ ] You can show at least one failure that was caught by your checks
- [ ] High-risk actions require explicit human approval

## Deep dive

- Hello-Agents Chapter 12 (Evaluation)
- Anthropic / OpenAI eval guidance

## Next

→ [Stage 8 — Interfaces and Safety](08-interfaces-and-safety.md) or start a full project from `/projects`.
