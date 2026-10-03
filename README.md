# Agentic AI Builder Roadmap

A practical, beginner-friendly roadmap for learning how LLMs and coding agents actually work, how to use them safely, and how to apply them to real business and operational problems in India, Tamil Nadu, MSME, GovTech, chemical plants, and local service workflows.

This repository is designed for:
- pre-final-year B.E. CSE learners
- students with little native programming depth
- builders who want to understand AI deeply without drowning in heavy math
- people who want to direct coding agents with clarity and control
- people who want to spot hallucinations, bad tool calls, and broken systems

## Core outcome

By the end of this roadmap, you should be able to:
- explain LLMs in practical terms
- understand tokens, context windows, embeddings, attention, and generation
- know why agents hallucinate
- know how to detect bad agent decisions
- write PRDs, specs, and acceptance criteria for coding agents
- use coding agents to do small, useful tasks in a real codebase
- decide what belongs to humans and what belongs to agents
- choose between rules, RAG, tool calling, and LLM-as-judge
- apply this to real-world small-business and public-service workflows

## Learning principles

1. Learn fundamentals before shiny systems
2. Prefer official docs over hype
3. Validate outputs with tests, checks, and domain reasoning
4. Treat fluent answers as untrusted until verified
5. Keep business logic, constraints, and judgment with the human
6. Avoid Instagram/Reddit as primary learning sources

## Source policy

Prioritize:
- Anthropic docs
- OpenAI docs
- Google AI docs
- Ollama docs
- official SDK docs
- Hello-Agents as a canonical learning reference
- evaluation and engineering resources

Avoid as primary sources:
- social media loops
- vague hype tutorials
- “AI influencer” advice without validation

## Recommended learning path

### Phase 1: LLM foundations
Start with:
- tokens and context
- embeddings and retrieval intuition
- attention in plain language
- decoding and generation
- sampling and uncertainty
- why hallucination is a probability problem, not just a prompt problem

### Phase 2: Agents and tool use
Learn:
- tool calling
- function schemas
- ReAct / plan-act loops
- when the model is improvising instead of reasoning
- safe agent behavior
- how to constrain agent actions

### Phase 3: Context engineering and memory
Learn:
- context window management
- context trimming
- summarization and memory design
- RAG vs raw prompt stuffing
- knowledge grounding
- why long but noisy prompts often underperform

### Phase 4: Production reliability
Learn:
- evals
- hallucination detection
- LLM-as-judge
- human approval loops
- observability
- rollback and safe execution
- test-first validation

### Phase 5: Business and domain judgment
Learn:
- how to separate business decisions from execution
- when to use deterministic logic
- when to use RAG
- when to use tool calling
- when to use humans in the loop
- how to apply AI to real workflows such as:
  - MSME operations
  - GovTech workflows
  - document handling
  - manufacturing SOP support
  - plant maintenance workflows
  - local service automation

## Must-learn topics

### 1. How LLMs work
Understand:
- tokenization
- embeddings
- attention
- context windows
- generation
- confidence vs truth

### 2. Why agents fail
Study:
- false confidence
- stale context
- wrong tool call
- wrong file edits
- unsupported assumptions
- silent failure after an apparently correct output

### 3. How to direct agents
Use this workflow:
- define the business problem
- write a PRD
- define specs and constraints
- define success criteria
- ask for a plan before code changes
- require validation
- review every diff manually

### 4. When to use which pattern
- Deterministic rules for validation, business logic, forms, and compliance
- RAG for documents, SOPs, manuals, and internal knowledge
- Tool calling for APIs, DBs, file systems, and scripts
- LLM-as-judge for scoring and QA
- Adversarial prompting for brainstorming and stress-testing
- Human review for high-risk actions

## Recommended roadmap sequence

1. Fundamentals
2. Prompting basics
3. LLM core behavior
4. Tool calling and agent loops
5. Context engineering and memory
6. Evaluation and hallucination detection
7. Real-world business workflows

## Suggested repo structure

```text
agentic-ai-builder-roadmap/
├── README.md
├── docs/
│   ├── llm-under-the-hood.md
│   ├── tool-calling-and-agents.md
│   ├── spec-driven-agent-workflows.md
│   ├── hallucination-detection.md
│   ├── context-window-and-token-optimization.md
│   └── business-ai-for-india.md
├── projects/
│   ├── project-01-prd-to-agent.md
│   ├── project-02-rag-knowledge-assistant.md
│   ├── project-03-agent-review-bot.md
│   └── project-04-msme-workflow-assistant.md
├── exercises/
│   ├── exercise-01-hello-llm.md
│   ├── exercise-02-tool-use.md
│   ├── exercise-03-rag-mini-demo.md
│   └── exercise-04-agent-eval.md
├── resources/
│   ├── official-docs.md
│   ├── reference-links.md
│   └── curated-reading-list.md
├── .gitignore
└── LICENSE
```

## Success checklist

- [ ] I understand tokens, context, and why they matter
- [ ] I understand why models hallucinate
- [ ] I know how to catch bad agent behavior
- [ ] I can write a PRD/spec for a small workflow
- [ ] I can tell when to use RAG vs rules vs tool calling
- [ ] I can validate agents with tests and checks
- [ ] I can reason about real business value instead of only model hype

## Final note

The real skill in AI is not sounding smart. The real skill is:
- deciding what should be automated
- constraining behavior
- validating output
- knowing when to stop and ask for human judgment

That is what turns AI from a demo into a useful system.
