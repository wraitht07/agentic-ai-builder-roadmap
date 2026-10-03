# Exercise 02: Tool Use

**Linked stage**: Stage 3

## Goal

Force a model to use a well-defined tool schema and observe what happens when the schema is violated.

## Instructions

1. Define two simple tools with clear JSON schemas (or function signatures):
   - `get_current_time()`
   - `add_numbers(a: float, b: float)`
2. Use the ReAct skeleton in `code/react_skeleton.py` or a provider’s native tool-calling API.
3. Give a goal that requires both tools.
4. Deliberately send a malformed tool call (wrong name or missing argument) and observe recovery.
5. Add a third tool that reads a local text file (simulate an SOP).

## Questions to reflect on

- Did the model follow the schema without extra free text?
- How did the loop handle an unknown tool name?
- Was the final answer grounded in the tool observations?

## Deliverable

- Working agent loop that uses at least two tools
- Screenshot or log of a successful multi-tool run
- Note of one failure mode you observed

## Success criteria

- [ ] Tools are called in the correct order
- [ ] Schema violations produce clear observations, not silent crashes
- [ ] Final answer references tool results
