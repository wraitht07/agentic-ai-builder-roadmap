# Project 05 — Database / Knowledge Query Agent (Hello-Agents style)

Inspired by the co-creation project `939147533-DatabaseAgent` in hello-agents and the ReAct pattern from Chapter 4.

## Goal

Build a small agent that can answer natural-language questions about a local SQLite (or CSV) dataset representing a realistic MSME / plant scenario, using tool calling only.

## Suggested domain (India / Tamil Nadu)

- Inventory of a small chemical-plant store (item, quantity, reorder level, location)
- Or MSME order book (customer, product, quantity, status, delivery date)

## Required deliverables

1. **PRD** (1 page): problem, users, success criteria, out-of-scope
2. **Spec**: list of tools the agent may call (e.g. `list_tables`, `run_select_query`, `get_schema`)
3. **Safety constraints**: only SELECT, no DROP/UPDATE, parameterised queries
4. **Agent loop**: reuse or adapt `code/react_skeleton.py`
5. **Eval set**: 8–10 questions with expected answers or acceptance checks
6. **Demo script**: how a non-technical plant supervisor would ask questions

## Success criteria

- Agent never executes destructive SQL
- Answers cite the tool observation (grounded)
- At least 7/10 eval questions pass
- You can explain every tool call the agent made

## Why this project

It forces the three skills that matter most for real deployments:
- tool schema design
- grounding (no hallucinated numbers)
- human-readable constraints and evals

After finishing, map the same pattern onto a real company SOP or inventory sheet.
