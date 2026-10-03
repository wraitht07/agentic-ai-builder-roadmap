# Tool Calling and Agents

A coding agent is a system that uses an LLM to decide what action to take next, then executes a tool or code action, and repeats until the task is done or a stopping condition is met.

## 1. The basic pattern

The agent loop usually looks like this:
1. Read the task and context
2. Decide what to do next
3. Call a tool or function
4. Get tool output
5. Update working memory or reasoning
6. Repeat until the task is complete

This is not magic. It is a structured decision loop.

## 2. Tool calling

A tool is a capability the model can invoke. Examples include:
- reading a file
- searching code
- writing a patch
- running tests
- querying a database
- calling an API

Good tool design matters.

A tool should have:
- a clear purpose
- a narrow, well-defined input schema
- understandable output
- safe permission boundaries

## 3. Why tool calling matters

Without a tool, the model is just generating text.

With a tool, it can do grounded work like:
- inspect repository state
- run build/test commands
- fetch documentation
- write or edit files
- validate results with a real run

This is where AI becomes more operational and more useful.

## 4. Risks in tool-use agents

Agent failures often happen here:
- wrong tool chosen
- wrong schema or argument format
- tool call succeeds but result is misread
- model makes up the existence of a file or API
- model keeps trying random actions instead of narrowing down

## 5. Good agent workflow

Use an explicit pattern:
- understand the goal
- inspect only required files
- make a focused plan
- execute a small patch
- validate with a test or check
- summarize the result and assumptions

Bad patterns:
- broad repo-wide edits without understanding scope
- one giant prompt with no constraints
- letting the model “just fix it” without validation

## 6. Tool design principles

Good tool design should be:
- specific
- auditable
- small in scope
- safe by default
- easy to test

Use the right tool for the right action. Do not give a model a giant, vague “do everything” tool if a smaller targeted tool would work better.

## 7. Human control is still essential

The agent should work inside human-defined guardrails.

You should still keep ownership of:
- the requirement
- the acceptance criteria
- the architecture
- the level of trust
- final review and deployment decisions

## 8. Common beginner mistakes

- giving the agent too much autonomy too early
- skipping validation
- allowing broad repo edits without narrowing scope
- treating the first output as correct
- not checking whether the model used the right tool or the right file

## 9. Practical exercises

Try these:
- ask an agent to read one file and summarize a function
- ask it to update one config value and then validate the project
- ask it to identify a failing test without editing code first

## 10. Next steps

Read:
- docs/spec-driven-agent-workflows.md
- docs/hallucination-detection.md
- projects/project-01-prd-to-agent.md
