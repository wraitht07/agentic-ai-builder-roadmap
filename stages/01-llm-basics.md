# Stage 1 — LLM Basics

Goal: understand what actually happens between your prompt and the model’s answer, without heavy math.

## Learning Goals

After this stage you can:

- Explain tokens, context windows, embeddings, attention and generation in plain language
- Estimate roughly how many tokens a prompt will cost
- Recognise why a fluent answer can still be wrong
- Make your first real LLM API call and inspect the raw response

## Core concepts (practical view)

1. **Token** – the unit the model reads and writes (not always a full word).
2. **Context window** – the maximum number of tokens the model can “see” at once.
3. **Embeddings** – numerical vectors that capture meaning; used for retrieval.
4. **Attention** – the mechanism that decides which parts of the input matter for the next token.
5. **Generation / decoding** – sampling the next token from a probability distribution (temperature, top-p, etc.).
6. **Hallucination** – the model producing a confident continuation that is not grounded in evidence.

Read the full practical explanation in `docs/llm-under-the-hood.md` and `docs/context-window-and-token-optimization.md`.

## Hands-on Practice

1. Choose one free or cheap path:
   - Ollama (local) + any small model, or
   - OpenAI / Anthropic / Google free tier / Gemini, or
   - any other provider you already have.
2. Write a 10-line Python script that:
   - sends a simple system + user prompt
   - prints the full response (including any usage / token counts if available)
3. Run the same prompt three times with different temperatures (0.0, 0.7, 1.2) and note the differences.
4. Deliberately ask a question that requires knowledge the model cannot have (e.g. “What is the exact stock price of company X right now?”) and observe the behaviour.

## Completion Check

- [ ] You can explain what a token is and why context windows are limited
- [ ] You have a working script that calls an LLM and prints the answer
- [ ] You have seen how temperature changes the output
- [ ] You can point to at least one clear hallucination or unsupported claim

## Deep dive

- Hello-Agents Chapter 3
- Official docs of the provider you chose

## Next

→ [Stage 2 — Prompt Engineering](02-prompt-engineering.md)
