# Stage 2 — Prompt Engineering

Goal: move from “just ask” to structured, controllable prompts that reduce ambiguity and hallucinations.

## Learning Goals

- Write zero-shot, one-shot and few-shot prompts
- Use Chain-of-Thought and structured output formats
- Separate system instructions from user content
- Know the limits of prompt engineering alone

## Core patterns

| Pattern | When to use |
|---------|-------------|
| Zero-shot | Simple, well-understood tasks |
| One-shot / Few-shot | When format or style must be consistent |
| Chain-of-Thought | Multi-step reasoning |
| Structured output (JSON / XML) | When you will parse the answer programmatically |
| Role + constraints + examples | Most production agent prompts |

## Hands-on Practice

1. Take a realistic MSME task, e.g. “Extract invoice number, date, total and GST from this text”.
2. Write three versions:
   - free-form natural language
   - few-shot with 2 examples
   - strict JSON schema instruction
3. Compare accuracy, consistency and ease of downstream parsing.
4. Add a deliberate constraint (“Never invent numbers; say UNKNOWN if missing”) and test it.

## Completion Check

- [ ] You have at least one prompt that reliably produces parseable JSON
- [ ] You understand why “be helpful” is often weaker than explicit constraints
- [ ] You can explain when prompt engineering is not enough and tools/RAG become necessary

## Deep dive

- Hello-Agents Chapter 3 (prompt section)
- Official prompting guides from Anthropic / OpenAI / Google

## Next

→ [Stage 3 — Tool Use and First Agent Loop](03-tool-use-and-hello-agent.md)
