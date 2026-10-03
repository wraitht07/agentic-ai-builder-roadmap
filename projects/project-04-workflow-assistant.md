# Project 04: Multi-step Workflow Agent (with human gates)

## Goal

Build a constrained multi-step agent for a realistic operational workflow. The pattern must transfer across sectors.

## Example domains (pick one)

- Purchase / invoice exception handling (MSME or retail)
- Maintenance or permit-style checklist support (manufacturing / chemical)
- Guest or order exception handling (hospitality / retail)
- Internal request triage + draft response (any business automation context)

## Design rules

- Narrow scope. One clear workflow only.
- Explicit “must never do” list.
- Tool calls only for allowed actions.
- Human approval gate before any external message, financial action, or irreversible write.
- Every run produces a short log of steps and sources.

## Required deliverables

1. One-page PRD + acceptance criteria
2. Tool schemas + permission model
3. Working agent loop (reuse or extend `code/react_skeleton.py`)
4. Small eval set (8–12 cases) covering happy path + failure modes
5. Short write-up of residual risks

## Success criteria

- Agent stays inside defined bounds on the eval set
- High-risk actions are blocked or require explicit human confirmation
- You can explain every tool call and every residual risk in plain language

This project demonstrates the exact skills early-stage automation and vertical startups hire for: constrained multi-step agency with clear ownership.
