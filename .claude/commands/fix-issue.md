---
description: Fix identified issue with root cause analysis and validation
argument-hint: <task-id> [--skip-tests]
allowed-tools: Skill
---

Invoke the fix-issue skill:

Use Skill tool: `Skill(command="fix-issue")`

This will execute the issue fixing workflow:
1. Load task/issue specification
2. Reproduce the issue
3. Perform root cause analysis
4. Implement fix
5. Write/update tests
6. Validate fix resolves issue
7. Generate fix summary

The skill will parse $ARGUMENTS for:
- `task-id` - Task or issue identifier (required)
- `--skip-tests` - Skip test creation (not recommended)
- `--validation` - Validation approach: manual, automated (default: automated)

Output: Fixed code, tests, validation report, root cause analysis
