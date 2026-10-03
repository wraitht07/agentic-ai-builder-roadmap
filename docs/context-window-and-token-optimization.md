# Context Window and Token Optimization

The context window defines how much information the model can consider at once. Token optimization is the practice of making the model’s input smaller, more relevant, and more useful.

## 1. Why this matters

Even with large context windows, more context is not always better.

Problems with excessive context:
- higher cost
- slower latency
- more distraction for the model
- dilution of key facts
- failure to prioritize important instructions

## 2. Core techniques

### Chunking
Break large documents into manageable sections.

Best use:
- long PDFs
- large manuals
- internal doc stores
- knowledge-base retrieval

### Retrieval filtering
Instead of dumping everything into the prompt, retrieve only the most relevant items.

This is the basis of many practical RAG systems.

### Summarization
Summaries can preserve core meaning while reducing token count.

Use summaries for:
- long conversation histories
- stale background context
- repeated instructions
- older retrieved documents

### Structured prompts
Use clear sections and labels.

Good structure:
- objective
- constraints
- inputs
- output format
- validations

This helps the model focus on what matters.

## 3. Context trimming strategies

Use a few disciplined patterns:
- keep only relevant instructions
- remove duplicate context
- summarize older turns in a chat
- avoid repeating the same info across tool outputs
- store long context outside the active model call when possible

## 4. When more context can hurt

Large prompts can lead to:
- attention dilution
- conflicting instructions
- forgotten constraints
- lower signal-to-noise ratio

This is why a shorter, better-targeted prompt often wins over a massive “everything in one go” prompt.

## 5. Practical design rule

For any agent workflow, ask:
- What does the model actually need right now?
- What is irrelevant noise?
- What can be moved to retrieval or a database?
- What can be summarized instead of included verbatim?

## 6. Mini-checklist

- [ ] I know what context window means
- [ ] I know why long contexts can hurt model performance
- [ ] I can list at least 3 token optimization strategies
- [ ] I understand the difference between retrieval and prompt stuffing

## 7. Next steps

Read:
- docs/business-ai-for-india.md
- projects/project-02-rag-knowledge-assistant.md
- exercises/exercise-03-rag-mini-demo.md
