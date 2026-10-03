"""Minimal ReAct agent loop – reusable skeleton.

Place this under /code so later stages and projects can import or copy it.
Matches the practice in stages/03-tool-use-and-hello-agent.md
and the classic paradigms taught in Hello-Agents Chapter 4.
"""

from typing import Callable, Any
import json


def react_loop(
    llm: Callable[[str], str],
    tools: dict[str, Callable[..., Any]],
    user_goal: str,
    max_steps: int = 8,
) -> str:
    """Minimal ReAct agent loop.

    Args:
        llm: function that takes a prompt string and returns the model text
        tools: name → python callable
        user_goal: the high-level task
        max_steps: hard limit to prevent infinite loops

    Returns:
        Final answer string or a max-steps message
    """
    history = [f"User goal: {user_goal}"]
    tool_desc = "\n".join(
        f"- {name}: {fn.__doc__ or 'no description'}" for name, fn in tools.items()
    )

    for step in range(max_steps):
        prompt = (
            f"You are a careful agent. You have these tools:\n{tool_desc}\n\n"
            "Conversation so far:\n"
            + "\n".join(history)
            + "\n\n"
            "Think step by step. If you need a tool, output exactly:\n"
            'TOOL_CALL: {"name": "tool_name", "args": {...}}\n'
            "Otherwise give the final answer as:\nFINAL: <answer>\n"
        )

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


# Example tools for local testing
def get_current_time() -> str:
    """Return the current local time as ISO string."""
    from datetime import datetime
    return datetime.now().isoformat(timespec="seconds")


def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


if __name__ == "__main__":
    # Dummy LLM for offline testing – replace with a real call
    def dummy_llm(prompt: str) -> str:
        if "time" in prompt.lower() and "TOOL_CALL" not in prompt:
            return 'TOOL_CALL: {"name": "get_current_time", "args": {}}'
        return "FINAL: Done (dummy)."

    tools = {
        "get_current_time": get_current_time,
        "add_numbers": add_numbers,
    }
    result = react_loop(dummy_llm, tools, "What time is it?")
    print(result)
