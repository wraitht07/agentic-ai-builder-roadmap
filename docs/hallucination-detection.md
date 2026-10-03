# Hallucination Detection and Risk Review

Hallucination is one of the most important topics in practical AI engineering. A model can sound highly confident while being wrong.

## 1. Types of hallucination

### Factual hallucination
The model states a fact that is not true.

### Context hallucination
The model invents details that are not present in the provided context.

### Tool hallucination
The model claims a tool or file exists, or indicates it performed actions that never happened.

### Schema hallucination
The model produces output that looks valid but does not match the required structure.

## 2. Why it happens

Common causes:
- weak or missing grounding
- noisy context
- model trying to complete a pattern instead of verify facts
- non-deterministic sampling
- missing validation step

## 3. Practical detection patterns

### a. Ground against source material
Ask: does the answer match the supplied source?

If the model is generating claims beyond the available evidence, this is a risk signal.

### b. Split output into claims
Break the answer into smaller statements and verify each one individually.

This is often more reliable than judging the whole paragraph at once.

### c. Use multiple passes
Ask the model to reason about uncertainty, provide evidence, and state unknowns.

A model that cannot admit uncertainty may be overconfident.

### d. Check tool output directly
When a model claims a file was read, patched, or tested, verify the actual result.

Do not trust the agent’s narrative alone.

### e. Use evals and rubric checks
Define scoring rules and run them systematically.

Examples:
- correctness of answer
- grounding in provided sources
- test pass/fail status
- number of unsupported claims

## 4. LLM-as-judge

LLM-as-judge means using one model or evaluation rubric to assess another model’s answer.

Useful when:
- you need fast comparative scoring
- there is a rubric and desired behavior
- manual review is too slow

Not enough by itself when the task is high-stakes. Use it as a layer, not a replacement for human review.

## 5. How to review an agent output

Ask these questions:
- What evidence supports this?
- What is missing?
- Did the agent actually validate the result?
- Did it use the correct tool and file?
- Did it modify anything outside the requested scope?
- Did it make assumptions not stated in the task?

## 6. Production mindset

If an agent is operating in a real workflow, you need:
- explicit approval gates
- test validation
- logging and traces
- rollback paths
- human intervention for high-risk actions

## 7. Practical rule

Never accept a strong-looking answer without strong evidence.

In real AI work, trust comes from validation, not from confidence.

## 8. Next steps

Read:
- docs/context-window-and-token-optimization.md
- projects/project-03-agent-review-bot.md
- exercises/exercise-04-agent-eval.md
