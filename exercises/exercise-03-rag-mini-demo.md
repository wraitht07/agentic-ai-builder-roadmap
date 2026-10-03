# Exercise 03: RAG Mini-Demo

**Linked stage**: Stage 6

## Goal

Build the smallest possible RAG pipeline and measure whether retrieval actually helps.

## Instructions

1. Collect 4–6 short paragraphs that represent real domain knowledge (plant SOP, leave policy, GST note, local service process, etc.).
2. Chunk them simply (by paragraph or fixed size).
3. Use either:
   - a free embedding model + vector store, or
   - keyword / BM25 search for the absolute minimum version.
4. At query time retrieve the top-2 or top-3 chunks and put only those into the prompt.
5. Ask the same questions with and without retrieval; compare answers.

## Questions to reflect on

- Did retrieval improve factual accuracy?
- Did noisy extra context ever make the answer worse?
- How many tokens did the retrieved context add?

## Deliverable

- Working retrieve → prompt → answer script
- Side-by-side comparison of at least two questions (with vs without RAG)
- Short note on when you would choose RAG vs pure prompting

## Success criteria

- [ ] Retrieval is actually used in the prompt
- [ ] At least one clear improvement is demonstrated
- [ ] You can state a rule for “when to retrieve”
