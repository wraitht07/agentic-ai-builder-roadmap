# Exercise 01: Hello LLM

**Linked stage**: Stage 1

## Goal

Make your first real LLM call, inspect tokens/usage if available, and observe how temperature and phrasing change behaviour.

## Instructions

1. Choose one provider (Ollama local, OpenAI, Anthropic, Google AI, etc.).
2. Write a short Python script (or use the playground) that:
   - Sends a system message + user message
   - Prints the full response and any token/usage metadata
3. Run the same prompt at temperature 0.0, 0.7 and 1.2.
4. Ask a question that requires live or private knowledge the model cannot have.
5. Slightly rephrase the same question three times and note consistency.

## Questions to reflect on

- Did the model respond consistently across phrasings?
- Did higher temperature produce more creative but less reliable answers?
- Did the model invent details or admit uncertainty?
- How many tokens did the prompt + completion use?

## Deliverable

A short markdown note (5–10 lines) explaining:
- which provider/model you used
- what you observed about temperature and consistency
- one clear example of an unsupported claim (if any)

## Success criteria

- [ ] Working call to an LLM
- [ ] Temperature comparison completed
- [ ] Reflection note written
