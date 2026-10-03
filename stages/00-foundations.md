# Stage 0 — Foundations

This stage checks four tools you will use later. If you already know them, skip ahead. If not, do the small practice once.

## When to skip this stage

Check these four things. You do not need to memorize commands. You do need to find information and finish each task yourself:

- [ ] Use Python to get public data from an API, then find one value in the JSON.
- [ ] Use Git to clone, create a branch, commit, and push. Know what a merge conflict is.
- [ ] Use the command line to change folders, create files, and run a Python script.
- [ ] Read YAML and JSON.

If all four are easy, go straight to [Stage 1 — LLM Basics](01-llm-basics.md).

## Learning Goals

After this stage you can:

- Get data from an API with Python and read the needed part of the JSON.
- Run a program from a terminal and find the file it created.
- Save a version with Git and return to that version when needed.
- Recognize YAML, JSON, and an API token, and know what must not be shared.

## Hands-on Practice: Build a Small GitHub Data Tool

**Outcome:** Have Python get public data from GitHub, show it on screen, write it to a file, and save the result with Git. No account or token required.

### 1. Create the program

Create a new folder. Save the following as `github_profile.py`:

```python
import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent": "stage-0-practice"})

with urlopen(request, timeout=10) as response:
    profile = json.load(response)

result = f"{profile['login']} has {profile['followers']} followers"
print(result)
Path("result.txt").write_text(result + "\n", encoding="utf-8")
```

### 2. Run the program

```bash
python github_profile.py
```

### 3. Save the result with Git

```bash
git init
git add github_profile.py result.txt
git commit -m "Add GitHub profile checker"
```

## Completion Check

- [ ] The terminal shows a GitHub account and follower count.
- [ ] `result.txt` contains the same result.
- [ ] `git log --oneline` shows the commit you just made.
- [ ] The program and commit contain no password or API token.

When all four are done, continue to Stage 1.

## Extra practice (only what you need)

1. **Python:** Replace `torvalds` with your own GitHub account.
2. **Git:** Create a branch, change the output, commit again, push to a remote.
3. **Command line:** Create `src`, `tests`, `docs` folders and run from different paths.
4. **JSON / YAML:** Save the full API response; create a small config file with indentation practice.

## Why this stage exists for an India/MSME builder

Almost every real agent workflow (invoice checker, SOP assistant, local-service bot) starts with:
- calling an API or reading a file
- writing intermediate results
- version-controlling the code so you can roll back a bad agent edit

Master these four tools once; they appear in every later stage.

## Next

→ [Stage 1 — LLM Basics](01-llm-basics.md)
