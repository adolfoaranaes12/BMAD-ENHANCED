---
description: Implement feature from task specification with TDD workflow
argument-hint: <task-spec-file> [--mode standard|tdd|fast] [--subtask <subtask-id>]
allowed-tools: Skill
---

Invoke the implement-feature skill:

Use Skill tool: `Skill(command="implement-feature")`

This will execute the feature implementation workflow:
1. Load and validate task specification
2. Analyze requirements and acceptance criteria
3. Set up development environment
4. Implement feature following task breakdown
5. Write comprehensive tests
6. Run validation checks
7. Generate implementation summary

The skill will parse $ARGUMENTS for:
- `task-spec-file` - Path to task specification file (required)
- `--mode` - Implementation mode: standard (default), tdd (test-first), fast (skip some checks)
- `--subtask` - Optional subtask identifier to implement only a specific subtask from the task spec

Output: Implemented feature with tests, validation report, completion summary
