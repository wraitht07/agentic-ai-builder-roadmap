# Stage 6 — Memory and RAG

After you have a working agent loop, the next bottleneck is almost always context.

## Learning Goals

- Distinguish short-term conversation history from long-term memory
- Build a minimal RAG pipeline (chunk → embed → retrieve → ground)
- Know when more context makes answers worse
- Apply token budgeting and context trimming

## Key ideas (from Hello-Agents Chapters 8 & 9)

- Memory systems: buffer, summary, vector store
- RAG vs raw prompt stuffing
- Context engineering = deciding what the model is allowed to see at each step

## Minimal RAG practice

1. Take 3–5 short SOPs or policy paragraphs relevant to an MSME or plant (e.g. leave policy, safety checklist).
2. Chunk them (simple fixed-size or by paragraph).
3. Use any free embedding model (or even keyword search for the first version).
4. At query time retrieve the top-k chunks and put only those into the prompt.
5. Compare answers with and without retrieval.

## Completion Check

- [ ] You can point to a case where retrieval improved the answer
- [ ] You can point to a case where noisy extra context hurt the answer
- [ ] You have a clear rule for “when to retrieve vs when to just prompt”

## Next

→ Stage 7 (Production Reliability) or start Project 02 (RAG Knowledge Assistant).

Deep dive: Hello-Agents Chapters 8–9 + this repo’s `docs/context-window-and-token-optimization.md`.
