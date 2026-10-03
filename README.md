# Agentic AI Builder Roadmap

**A single, practical path from “I can call an LLM” to “I can design, direct, and validate reliable agent systems for real Indian business / MSME / GovTech / plant workflows.”**

This repository unifies three sources and keeps only what a pre-final-year B.E. CSE learner in India/Tamil Nadu actually needs:

| Source | What was kept | What was stripped |
|--------|---------------|-------------------|
| **agentic-ai-builder-roadmap** (this repo) | India/MSME focus, PRD/spec workflow, hallucination & judgment emphasis, existing docs/exercises/projects | Nothing core |
| **awesome-agentic-ai-zh** | Staged learning path (Stage 0–8), hands-on practices, curated resource tables, Track A (CLI power-user) / Track B (Agent Builder) | Full multi-language mirrors, outreach files, maintainer checklists |
| **hello-agents** (Datawhale) | Core chapter map, classic paradigms (ReAct / Plan-and-Solve / Reflection), co-creation projects, PDF links, interview notes, context-engineering & evaluation depth | Pure Chinese-only narrative, low-code platform walkthroughs that are already covered elsewhere, redundant “what is an agent” intros |

**Core outcome**  
By the end you will be able to:
- Explain LLMs in practical terms (tokens, context, attention, generation, why fluency ≠ truth)
- Direct coding agents with clear PRDs, specs, constraints and acceptance checks
- Catch hallucinations, wrong tool calls, stale context and silent failures
- Choose correctly among rules / RAG / tool-calling / LLM-as-judge / human review
- Ship small, useful agent workflows for MSME operations, document handling, plant SOPs, local services and GovTech

## Learning principles (non-negotiable)
1. Fundamentals before frameworks  
2. Official docs > social-media loops  
3. Fluent answers are untrusted until verified  
4. Business logic and high-risk decisions stay with the human  
5. Prefer small, testable steps over big demos  
6. Hello-Agents is the canonical deep-dive reference; this repo is the map + practice layer

## Recommended learning path

### Phase 0 – Foundations (skip if already solid)
- Python + Git + terminal + JSON/YAML basics  
- Source: Stage 0 practice from awesome-agentic-ai-zh (kept & adapted)  
- Checkpoint: can fetch public API data, write a file, commit with Git

### Phase 1 – LLM Foundations
- Tokens, context windows, embeddings, attention, decoding, sampling  
- Why hallucination is a probability problem  
- Docs in this repo: `docs/llm-under-the-hood.md`, `docs/context-window-and-token-optimization.md`  
- Deep theory: Hello-Agents Chapter 3  
- Checkpoint: can explain why a long noisy prompt often hurts quality

### Phase 2 – Agents & Tool Use
- Tool schemas, ReAct / Plan-and-Solve / Reflection loops  
- Safe agent behavior and constraint design  
- Docs: `docs/tool-calling-and-agents.md`  
- Classic implementations: Hello-Agents Chapter 4  
- Hands-on: Stage 3 (first agent loop) from awesome  
- Checkpoint: can write a tool schema and force the model to use it

### Phase 3 – Context Engineering & Memory
- Context trimming, summarization, RAG vs prompt stuffing  
- Token budgeting and hygiene  
- Docs: `docs/context-window-and-token-optimization.md`  
- Deep dive: Hello-Agents Chapters 8 & 9  
- Checkpoint: can design a minimal RAG pipeline that actually improves answers

### Phase 4 – Production Reliability
- Evals, LLM-as-judge, hallucination detection, human-approval loops  
- Observability and rollback  
- Docs: `docs/hallucination-detection.md`  
- Hello-Agents Chapter 12 + Stage 7 from awesome  
- Checkpoint: can write an eval rubric and catch a known failure mode

### Phase 5 – Business & Domain Judgment (India focus)
- When to use deterministic rules vs RAG vs tools vs humans  
- PRD → Spec → Plan → Diff review workflow  
- Real domains: MSME ops, chemical-plant SOPs, local services, GovTech document flows  
- Docs: `docs/business-ai-for-india.md`, `docs/spec-driven-agent-workflows.md`  
- Projects: see `/projects`

## Two tracks (choose one primary)

| Goal | Track | Entry |
|------|-------|-------|
| Get work done with Claude Code / Codex / OpenCode / Cursor | **Track A – CLI Power User** | Stage 5 + A1–A3 style practices |
| Write your own agent loops, tools, workflows and services | **Track B – Agent Builder** | Stage 3 → 4 → 6 → 7 |

Both tracks share Phase 0–2. Everyday non-coding users can stop after Phase 1 + the everyday-user notes in the original awesome repo.

## Repository structure (unified)

```text
agentic-ai-builder-roadmap/
├── README.md                          ← you are here
├── docs/                              ← practical explainers (kept + enhanced)
│   ├── llm-under-the-hood.md
│   ├── tool-calling-and-agents.md
│   ├── context-window-and-token-optimization.md
│   ├── hallucination-detection.md
│   ├── spec-driven-agent-workflows.md
│   └── business-ai-for-india.md
├── stages/                            ← staged path adapted from awesome-agentic-ai-zh (English primary)
│   ├── 00-foundations.md
│   ├── 01-llm-basics.md
│   ├── 02-prompt-engineering.md
│   ├── 03-tool-use-and-hello-agent.md
│   ├── 04-agent-frameworks.md
│   ├── 05-cli-ecosystem.md
│   ├── 06-memory-rag.md
│   ├── 07-production-reliability.md
│   └── 08-interfaces-and-safety.md
├── exercises/                         ← small runnable checks
├── projects/                          ← portfolio-depth projects (India/MSME focus + selected hello-agents co-creation)
├── resources/
│   ├── official-docs.md
│   ├── curated-reading-list.md
│   ├── reference-links.md
│   └── hello-agents-map.md            ← chapter map + PDF links
├── code/                              ← minimal reusable snippets (ReAct skeleton, tool schema, etc.)
└── LICENSE
```

## Success checklist

- [ ] I can explain tokens, context windows and why attention degrades with noise
- [ ] I know why models hallucinate and how to detect it
- [ ] I can write a PRD + acceptance criteria for a coding agent
- [ ] I can force a model to use a tool schema correctly
- [ ] I know when to choose rules / RAG / tools / LLM-as-judge / human review
- [ ] I can validate agent output with tests, domain checks or LLM-as-judge
- [ ] I have shipped at least one small workflow useful for an MSME / plant / local service

## Key external anchors (do not reinvent)

- **Deep systematic tutorial**: [Hello-Agents](https://github.com/datawhalechina/hello-agents) (and its English README)  
- **PDF releases**: https://github.com/datawhalechina/hello-agents/releases/latest  
- **Official docs**: Anthropic, OpenAI, Google AI, Ollama, Model Context Protocol  
- **Self-built framework reference**: [HelloAgents](https://github.com/jjyaoao/helloagents) (matches the tutorial)

## Final note

The real skill is not sounding smart.  
It is deciding what should be automated, constraining the agent, validating every claim, and knowing when to stop and ask for human judgment.

That is what turns an LLM demo into a useful system for real Indian workflows.

Start at `stages/00-foundations.md` (or jump to Stage 1 if the four foundation checks already pass).
