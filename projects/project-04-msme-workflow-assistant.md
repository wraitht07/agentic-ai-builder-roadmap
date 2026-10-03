# Project 04: MSME Workflow Assistant

## Goal

Design a small workflow assistant for a realistic micro-business or local service setting.

## Example scenarios

- small manufacturing vendor review support
- invoice or purchase-process assistant
- support ticket triage for a local service business
- service workflow assistant for a local government process

## Key design principle

Do not make it a general “AI manager.” Make it a narrow workflow tool with clear boundaries.

## Required structure

- business problem
- specific user roles
- small set of SOPs or document sources
- approval step for sensitive outputs
- validation logic for actions

## Example workflow

1. Intake a request
2. Retrieve relevant SOP or policy
3. Summarize the steps
4. Ask clarifying questions when information is missing
5. Produce a final recommendation or answer
6. Require a human approve if the final action is risky or irreversible

## Success criteria

- useful in a real process
- grounded in real documents
- understandable to non-technical users
- can be validated manually without full AI trust

## Stretch ideas

- add a response log
- add support for multilingual inputs
- integrate a simple human approval form
