---
description: Execute task specification with full implementation workflow
argument-hint: "<task-spec-file> [--mode standard|tdd|fast]"
allowed-tools: Skill
---

Invoke the execute-task skill:

Use Skill tool with skill="execute-task"

This will execute the complete task implementation workflow:
1. Load and parse task specification
2. Extract context and requirements
3. Implement according to specification
4. Run tests and validate acceptance criteria
5. Generate implementation report

The skill will parse $ARGUMENTS for:
- `task-spec-file` - Path to task specification file (required)
- `--mode` - Execution mode: standard (default), tdd (test-driven), or fast (skip extensive validation)

Output: Implemented feature with tests and validation report
