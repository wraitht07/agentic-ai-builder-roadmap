# Project 03: Agent Review Bot

## Goal

Build a small judge-like system that checks whether another agent or model output is grounded and valid.

## Why this matters

This is a practical way to learn evaluation logic, hallucination spotting, and LLM-as-judge workflows.

## Basic design

- receive an answer or agent output
- break it into claims
- compare claims against the source or task description
- score each claim on groundedness and completeness
- report unsupported or weak claims

## Requirements

- define a rubric
- include a pass/fail result
- mark unsupported statements
- summarize evidence gaps

## Evaluation rubric example

- correctness: 0 to 5
- grounding: 0 to 5
- completeness: 0 to 5
- tool/fact validation: pass/fail

## Success criteria

- the review bot catches unsupported claims without relying only on vibes
- the output is easy to explain to a human reviewer
- it helps a human decide whether to accept or reject the result

## Stretch ideas

- compare two model outputs side by side
- generate a decision summary for human approval
