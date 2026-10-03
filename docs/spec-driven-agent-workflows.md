# Spec-Driven Agent Workflows

Spec-driven development means turning vague intent into a structured contract before implementation begins. This is especially important when using coding agents, because agents are fast but can become unreliable when the goal is not precise enough.

## 1. Why specs matter

Without a spec, the agent is left to guess:
- what counts as success
- what constraints apply
- which edge cases matter
- what files should change
- what must not be changed

This is how agent work becomes sloppy or dangerous.

## 2. A practical spec structure

A small but useful spec should include:
- objective
- scope
- inputs
- outputs
- constraints
- success criteria
- validation steps
- edge cases and failure modes

Example:

```text
Objective:
Build a small document triage agent that classifies files into categories.

Scope:
Only process .pdf and .txt documents in a given folder.

Inputs:
Folder path, allowed categories, optional confidence threshold.

Outputs:
A JSON file with filename, category, confidence, and notes.

Constraints:
Do not modify unrelated files. Respect the read-only folder.

Success criteria:
- returns valid JSON
- processes all files in scope
- each file assigned to one category
- no hallucinated categories

Validation:
Run the script against test files and verify output JSON matches schema.
```

## 3. PRD mindset for agent tasks

A Product Requirements Document (PRD) gives the agent the business goal.

Typical PRD elements:
- problem statement
- target users
- user journey
- constraints
- non-goals
- acceptance criteria

This keeps the agent grounded in the human intent rather than improvising.

## 4. Deepen the work with explicit acceptance checks

A useful agent task must end with evidence.

For example:
- tests pass
- output matches expected schema
- no unrelated files changed
- result corresponds to known business rules

If the agent cannot prove this, the work is not trustworthy.

## 5. Typical agent failure patterns without specs

- agent adds features not requested
- agent changes wrong file
- agent assumes missing requirements
- agent returns answer without validating execution
- agent performs broad edits instead of surgical modifications

## 6. Best practices for spec-driven agent work

- write the task in plain language first
- then convert it to a structured spec
- keep scope narrow
- define what success looks like clearly
- require a plan before implementation
- require validation after implementation

## 7. Human role in the workflow

The human owns:
- domain logic
- business priorities
- risk tolerance
- final review
- deployment decisions

The agent owns execution inside the defined space.

## 8. Exercise

Draft a one-page spec for one of these:
- a small invoice parser
- a document classifier for office files
- a vendor-list summarizer
- a form extraction helper for a government workflow

## 9. Next steps

Read:
- docs/hallucination-detection.md
- docs/business-ai-for-india.md
- projects/project-01-prd-to-agent.md
