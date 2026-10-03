# Agentic AI Builder Roadmap

**Practical path from “I can call an LLM API” to “I can design, constrain, evaluate and ship reliable agent workflows that early-stage startups and operational businesses in India actually need.”**

This is not a “build your own MSME chatbot” guide.  
It is a skill-building roadmap for becoming useful to (and hireable by) early-stage startups working on business automation, MSME tools, manufacturing/chemical ops, retail, hospitality, logistics, and micro-modules of GovTech in the Indian ecosystem.

**Honest context (2025–2026):**
- ~75% of Indian AI startups are application-layer. Agentic AI funding and hiring are rising fast.
- Demand for people who can ship constrained, tool-using, evaluable agents is high; pure prompt jockeys and pure researchers are less scarce relative to need.
- Real value is in systems that integrate with messy data, legacy tools, WhatsApp/ERP/inventory systems, and keep humans in control of high-risk actions.
- Most production failures come from weak specs, missing evals, over-permissioned tools, and ignoring domain constraints — not from choosing the “wrong” framework.

**Core transferable outcome**
You will be able to:
- Explain LLM behaviour (tokens, context, attention, sampling, why fluent ≠ correct) well enough to debug agents
- Design tool schemas and agent loops that stay on task
- Ground agents with RAG or structured data so they stop inventing facts
- Write clear specs / acceptance criteria and review agent diffs
- Build simple evals and catch common failure modes
- Choose the right level of autonomy (rules vs tools vs RAG vs human approval)
- Ship small, observable workflows that map to real operational pain (inventory, document triage, support routing, compliance checks, order status, etc.)

These skills transfer across sectors. An inventory-aware agent or a document-processing agent is useful whether the company serves chemical plants, retail stores, hotels, or MSME software.

## Non-negotiable principles
1. Fundamentals and constraints before frameworks.
2. Official docs and primary sources over influencer content.
3. Every fluent answer is untrusted until grounded or verified.
4. High-risk decisions (money, legal, external communication, data deletion) stay with humans.
5. Prefer small, measurable workflows over ambitious multi-agent demos.
6. Domain reality > model cleverness. Messy Indian operational data is the norm.

## Learning path (tight and sequential)

### Phase 0 – Foundations
Python, Git, terminal, JSON/YAML, basic API calls.  
**Stage**: `stages/00-foundations.md`  
Skip only if you already do these comfortably.

### Phase 1 – LLM behaviour (not magic)
Tokens, context windows, embeddings, attention (practical view), decoding, temperature, why hallucination happens.  
**Stage**: `stages/01-llm-basics.md`  
**Docs**: `docs/llm-under-the-hood.md`, `docs/context-window-and-token-optimization.md`  
**Exercise**: `exercises/exercise-01-hello-llm.md`

### Phase 2 – Agents that act
Tool schemas, ReAct-style loops, Plan-and-Solve, basic reflection. Constraining the model.  
**Stages**: `stages/02-prompt-engineering.md` → `stages/03-tool-use-and-hello-agent.md`  
**Docs**: `docs/tool-calling-and-agents.md`  
**Code**: `code/react_skeleton.py`  
**Exercise**: `exercises/exercise-02-tool-use.md`

### Phase 3 – Grounding and memory
RAG vs stuffing, context hygiene, simple memory patterns.  
**Stage**: `stages/06-memory-rag.md`  
**Exercise**: `exercises/exercise-03-rag-mini-demo.md`

### Phase 4 – Making it reliable enough to ship
Evals, LLM-as-judge, hallucination checks, human approval gates, basic observability.  
**Stage**: `stages/07-production-reliability.md`  
**Docs**: `docs/hallucination-detection.md`  
**Exercise**: `exercises/exercise-04-agent-eval.md`

### Phase 5 – Spec-driven work and domain judgment
How to turn an operational problem into a constrained agent task. When to use rules vs tools vs RAG vs human.  
**Docs**: `docs/spec-driven-agent-workflows.md`, `docs/business-ai-for-india.md` (reframed for transferable operational patterns)

### Supporting stages
- `stages/04-agent-frameworks.md` — when a framework helps vs when a thin loop is better
- `stages/05-cli-ecosystem.md` — using Claude Code / Codex / Cursor effectively (high leverage for any builder)
- `stages/08-interfaces-and-safety.md` — CLI vs API vs simple UI, least-privilege tools, secrets, audit basics

## Two practical tracks

| Priority | Track | Focus |
|----------|-------|-------|
| Primary for most readers | **Builder** | Stages 3 → 4 → 6 → 7 → projects. Own the loop, tools, evals. |
| High-leverage parallel | **CLI Power User** | Stage 5 + heavy use of coding agents with strict specs. Speeds everything else. |

## Projects (portfolio pieces that transfer)

Build these as evidence. Each maps to multiple sectors.

1. **PRD → constrained agent** — take a real operational task, write a tight PRD + acceptance criteria, implement and evaluate.
2. **RAG knowledge assistant** — grounded Q&A over internal docs / SOPs / product catalogs (retail, hospitality, manufacturing manuals, GovTech circulars).
3. **Review / triage bot** — classifies or drafts responses with clear escalation rules (support tickets, purchase orders, compliance flags).
4. **Workflow assistant** — multi-step process with tool calls and human gates (order status, inventory check + alert, document extraction → structured data).
5. **Database / structured query agent** — natural language over a simple inventory / order / customer table with hard safety constraints (read-only or approved writes only).

These demonstrate the exact skills early-stage automation and vertical SaaS startups look for: tool design, grounding, constraints, evals, and domain-aware judgment.

## What early-stage startups actually pay for (pragmatic view)
- Ability to turn a messy workflow into a reliable agent loop
- Tool calling + schema discipline
- RAG that does not hallucinate on company data
- Basic eval harnesses and failure analysis
- Systems thinking (permissions, logging, cost, rollback)
- Communication: clear specs and honest assessment of what the agent can/cannot do

They do **not** primarily pay for knowing every framework or reciting transformer math.

## Repository layout
```
README.md                 ← this file
PROGRESS.md               ← personal checklist
docs/                     ← short practical explainers
stages/                   ← 00–08 sequential stages
exercises/                ← four progressive exercises
projects/                 ← five transferable portfolio projects
resources/                ← official docs, reading list, Hello-Agents map
code/react_skeleton.py    ← minimal reusable loop
```

## Success criteria (honest)
- [ ] Can explain why an agent produced a wrong answer and how to fix the root cause
- [ ] Can write a tool schema and force reliable use of it
- [ ] Can ground answers with retrieval and detect when grounding failed
- [ ] Can write acceptance criteria and a small eval set for an agent task
- [ ] Have shipped at least two small, constrained, observable agent workflows
- [ ] Can walk into an early-stage automation / vertical SaaS / ops-tech startup and contribute on day one to an agent feature

## External anchors (use these, don’t reinvent)
- Hello-Agents (Datawhale) for systematic depth: https://github.com/datawhalechina/hello-agents
- Official docs: Anthropic, OpenAI, Google AI, Ollama, Model Context Protocol
- Framework reference when needed: LangGraph (most common production choice for stateful agents)

## Final pragmatic note
The market rewards people who ship agents that stay within bounds, are evaluable, and solve a concrete operational problem.  
Autonomy theatre and demo-ware have short shelf lives.  
Build the skill of controlled, grounded, observable agency. That travels across MSME tools, manufacturing software, retail ops, hospitality systems, business automation startups, and selective GovTech modules.

Start with `PROGRESS.md` and `stages/00-foundations.md`.
