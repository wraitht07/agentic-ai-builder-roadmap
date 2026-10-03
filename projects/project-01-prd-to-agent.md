# Project 01: PRD to Agent

## Goal

Turn a vague idea into a small, reliable agent task using a PRD and a spec.

## Suggested project problem

Build a small workflow that reads a folder of documents and classifies them into categories such as:
- invoice
- vendor doc
- policy
- support request
- unknown

## Required steps

1. Write a brief PRD
2. Define an input/output schema
3. Define success criteria
4. Ask the agent to generate a plan before code changes
5. Implement a minimal working version
6. Validate with sample fixtures
7. Review failures and improve the spec

## Example PRD outline

```text
Title: Document Triage Assistant
Problem: Users upload documents and need them classified quickly.
Audience: office staff and small business operators
Goals: reduce manual sorting time and reduce error
Constraints: only classify supported file types; no classification without evidence
Success metrics: 90% valid classifications on sample set; no unsupported labels
```

## Deliverables

- PRD markdown
- spec file
- minimal script
- validation checklist
- error log with known failure cases

## Evaluation criteria

- output schema is valid
- no unsupported classes
- input files are processed without changes outside the expected scope
- result can be explained by rules or retrieval

## Stretch ideas

- add a confidence score
- add human approval step
- support CSV output for downstream use
