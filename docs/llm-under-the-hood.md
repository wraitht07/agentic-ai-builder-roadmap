# LLMs Under the Hood (Practical View)

When people say “LLMs are magic,” what they really mean is that large language models are extremely good at pattern recognition over massive text corpora. The important part is this: they do not “know” the world in a human sense. They predict the next likely token based on patterns they have seen.

## 1. What is a token?

A token is a small chunk of text, not always a word. It can be a piece of a word, a punctuation mark, or a common symbol sequence.

Why it matters:
- context windows are measured in tokens, not words
- token count affects cost and latency
- longer prompts use more tokens and can reduce clarity or increase noise

## 2. Context window

The context window is how much information the model can “see” at once.

Examples of the idea:
- a short prompt fits easily
- a long codebase or long conversation may exceed it
- once the model is near the limit, it may drop earlier context or behave worse

This is why context management matters.

## 3. Embeddings

Embeddings turn text into vectors, which are numerical representations that capture semantic similarity.

This helps with:
- search
- retrieval systems
- clustering related content
- nearest-neighbor lookup

The key idea: similar meaning tends to map to nearby vectors.

## 4. Attention

Attention is the mechanism that lets the model decide which part of the input is most relevant at each step while generating the next token.

At a practical level:
- the model is not reading every token equally
- it assigns relevance weights to nearby and relevant tokens
- as context gets too long or noisy, attention becomes harder to use well

This is one reason long prompts can degrade quality.

## 5. Generation and decoding

During generation, the model produces one token at a time.

The model chooses the next token using probability distributions. Parameters such as temperature and top-p affect how creative or conservative the output is.

Typical practical effects:
- low temperature: more deterministic outputs
- higher temperature: more creative but riskier outputs
- greedy decoding: safe but less varied
- sampling: more diverse but less predictable

## 6. Why hallucination happens

A hallucination is not always “the model is lying on purpose.” It often happens because:
- the model is trying to be useful and complete the answer
- it has incomplete or weak evidence
- the relevant context is missing or stale
- the user asks for something the model cannot verify
- it is producing the most likely continuation, not a grounded fact

Important: fluent output is not the same as verified truth.

## 7. What to remember as a builder

When building with LLMs, treat them as pattern engines that need structured inputs and validation.

A good mental model:
- model = pattern predictor
- prompt = task framing + constraints + context
- tool = grounded action
- validator = reality check

## 8. Practical learning checklist

- [ ] I know what a token is
- [ ] I understand context window limits
- [ ] I know that attention helps focus on relevant parts of the prompt
- [ ] I know why long noisy prompts can hurt quality
- [ ] I know that fluent answers are not guaranteed to be correct

## 9. Next steps

Read:
- docs/tool-calling-and-agents.md
- docs/context-window-and-token-optimization.md
- docs/hallucination-detection.md
