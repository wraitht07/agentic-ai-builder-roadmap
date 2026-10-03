# Exercise 04: Agent Eval

**Linked stage**: Stage 7

## Goal

Create a small golden set and a simple LLM-as-judge (or rule-based) evaluation for an agent.

## Instructions

1. Take any agent you already built (Stage 3 or 6).
2. Write 8–12 test cases with:
   - input / user question
   - expected behaviour or key facts that must appear
   - optional “must not invent” constraints
3. Run the agent on the set and record results.
4. Optionally write an LLM-as-judge prompt that scores correctness (0–2) and groundedness (0–2).
5. Identify at least one failure mode and improve the prompt or tools to fix it.

## Questions to reflect on

- Which failures were silent (looked correct but were wrong)?
- Did the judge agree with your manual scoring?
- What is the cheapest check that catches the most common errors?

## Deliverable

- Eval set (markdown or CSV)
- Pass/fail or score table
- One concrete improvement you made after seeing the results

## Success criteria

- [ ] Reproducible eval set exists
- [ ] At least one failure was caught and fixed
- [ ] You can explain the residual risks
