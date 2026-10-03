# Stage 3 — Tool Use and First Agent Loop

This is the heart of Track B (Agent Builder). You will implement a minimal ReAct-style loop that can call tools.

## Learning Goals

- Write a correct tool schema (JSON Schema or function description)
- Force the model to choose and call the right tool
- Implement the classic Observe → Think → Act → Observe loop
- Detect when the model is improvising instead of following the schema

## Core concepts (from Hello-Agents Chapter 4)

1. **ReAct** – Reason + Act interleaved with observations
2. **Plan-and-Solve** – first produce a plan, then execute step by step
3. **Reflection** – after an action, critique and revise

You only need to implement a solid ReAct skeleton here. The others become later improvements.

## Minimal ReAct skeleton (code block)

```python
# code/react_skeleton.py  (also place under /code later)
from typing import Callable, Any
import json

def react_loop(
    llm: Callable[[str], str],
    tools: dict[str, Callable[..., Any]],
    user_goal: str,
    max_steps: int = 8,
):
    """Minimal ReAct agent loop.

    llm: function that takes a prompt and returns the model text
    tools: name → python function
    """
    history = [f"User goal: {user_goal}"]
    tool_desc = "\n".join(
        f"- {name}: {fn.__doc__ or 'no description'}" for name, fn in tools.items()
    )

    for step in range(max_steps):
        prompt = f"""You are a careful agent. You have these tools:\n{tool_desc}\n\n"""
        prompt += "Conversation so far:\n" + "\n".join(history) + "\n\n"
        prompt += "Think step by step. If you need a tool, output exactly:\n"
        prompt += 'TOOL_CALL: {"name": "tool_name", "args": {...}}\n'
        prompt += "Otherwise give the final answer as:\nFINAL: <answer>\n"

        response = llm(prompt).strip()
        history.append(f"Assistant: {response}")

        if response.startswith("FINAL:"):
            return response[len("FINAL:"):].strip()

        if response.startswith("TOOL_CALL:"):
            try:
                call = json.loads(response[len("TOOL_CALL:"):].strip())
                name = call["name"]
                args = call.get("args", {})
                if name not in tools:
                    obs = f"Error: unknown tool {name}"
                else:
                    obs = str(tools[name](**args))
                history.append(f"Observation: {obs}")
            except Exception as e:
                history.append(f"Observation: tool call failed – {e}")
        else:
            history.append("Observation: model did not follow the required format")

    return "Max steps reached without FINAL answer."
```

## Practice

1. Implement two tools: `get_current_time` and `add_numbers(a, b)`.
2. Run the loop with a simple goal that requires both tools.
3. Force a deliberate schema violation and observe how the loop recovers (or fails).
4. Add a third tool that reads a local text file (simulate an SOP or invoice).

## Completion Check

- [ ] The agent correctly calls tools in the right order
- [ ] Bad tool names or missing arguments produce a clear observation, not a silent crash
- [ ] You can point to the exact place where the model “thought” vs “acted”
- [ ] You understand why an unbounded loop is dangerous in production

## Next

→ Stage 4 (frameworks) or jump to Stage 6 (Memory & RAG) if you already know LangGraph / AutoGen basics.

Deep dive: Hello-Agents Chapter 4 + the self-built HelloAgents framework.
