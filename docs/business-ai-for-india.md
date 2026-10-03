# Operational AI Patterns for Indian Businesses & Startups

Focus on patterns that transfer across MSME tools, manufacturing, retail, hospitality, logistics, business-automation startups, and selective GovTech modules.

## Where constrained agents create real value

High-frequency, structured-enough workflows:
- Document extraction and classification (invoices, POs, forms, compliance docs)
- Grounded knowledge lookup over SOPs, product catalogs, policy notes, manuals
- Triage and routing (support tickets, internal requests, escalations)
- Status and inventory queries with hard safety bounds
- Multi-step internal processes with explicit human gates (approvals, external messages, money movement)

These appear in almost every operational domain. Mastering the pattern is more valuable than domain-specific theatre.

## Sector mapping (same skills, different data)

| Pattern | MSME / Private business | Manufacturing / Chemical | Retail / Hospitality | Business automation startup / GovTech module |
|---------|-------------------------|---------------------------|----------------------|---------------------------------------------|
| Document agent | Invoice / PO processing | Safety / batch records | Order / reservation docs | Form extraction, circular lookup |
| Grounded Q&A | Internal SOPs, pricing | Equipment manuals, procedures | Product knowledge, house rules | Policy / scheme documents |
| Triage agent | Customer / vendor queries | Maintenance tickets | Guest / order issues | Service desk, grievance routing |
| Structured query | Inventory, orders | Spare parts, batch status | Stock, room availability | Case / application status |
| Workflow + gates | Purchase approval | Permit-to-work style checks | Exception handling | Multi-step citizen/business flows |

## Decision framework (use this every time)

- Deterministic validation / compliance → rules or code, not the LLM
- Needs company-specific knowledge → RAG or structured retrieval
- Needs to act on systems → tool calling with least privilege
- High-risk or irreversible → human approval gate + audit log
- Ambiguous or novel → escalate; do not let the agent freestyle

## What early-stage startups actually need

People who can:
1. Turn a messy operational description into a tight PRD and acceptance criteria
2. Design tools and constraints so the agent cannot wander
3. Ground outputs and detect when grounding failed
4. Ship a small, observable, evaluable workflow
5. Honestly state residual risks

They do not need another general-purpose chatbot.

## Practical starting rule

Pick one narrow workflow with measurable pain (time spent, error rate, or volume).  
Document current process → define must-not-do list → build constrained agent → evaluate → only then expand.

Autonomy is a cost, not a goal. Reliability and clear ownership are the goals.

## Next

- `docs/spec-driven-agent-workflows.md`
- Projects in `/projects` (all designed to be sector-agnostic evidence)
