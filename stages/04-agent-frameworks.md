# Stage 4 — Agent Frameworks & Workflow Graphs

Goal: understand when to stay with a raw loop and when a framework (LangGraph, AutoGen, CrewAI, HelloAgents, etc.) saves time and complexity.

## Learning Goals

- Distinguish a simple ReAct loop from a graph-based workflow
- Know the main open-source agent frameworks and their strengths
- Implement a small stateful workflow with branching / human-in-the-loop
- Decide “build vs buy” for your own projects

## Key ideas

- **Raw loop** (Stage 3): maximum control, minimal magic, best for learning and narrow tools.
- **Framework**: state management, persistence, multi-agent patterns, streaming, observability out of the box.
- Popular options (2025–2026):
  - LangGraph – graph of nodes + state
  - AutoGen / AG2 – multi-agent conversation
  - CrewAI – role-based crews
  - HelloAgents – matches the Hello-Agents tutorial exactly
  - Lightweight alternatives (Smolagents, etc.)

## Hands-on Practice

1. Take the ReAct skeleton from Stage 3.
2. Re-implement the same task using one framework of your choice (LangGraph recommended for learning graphs).
3. Add one conditional branch (e.g. “if confidence low → ask human”).
4. Compare lines of code, debuggability and control.

## Completion Check

- [ ] You can draw a simple agent workflow as a graph (nodes = actions, edges = conditions)
- [ ] You have run the same task both with a raw loop and with a framework
- [ ] You can explain when a framework is overkill vs necessary

## Deep dive

- Hello-Agents Chapter 6 (framework practice) and Chapter 7 (build your own)
- Official LangGraph / AutoGen quickstarts

## Next

→ [Stage 5 — CLI Ecosystem](05-cli-ecosystem.md) (Track A) or [Stage 6 — Memory & RAG](06-memory-rag.md) (Track B)
