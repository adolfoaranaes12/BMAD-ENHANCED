---
description: Review completed task against specification with quality checklist
argument-hint: <task-id> [--include-code-review]
allowed-tools: Skill
---

Invoke the review-task skill:

Use Skill tool: `Skill(command="review-task")`

This will execute the task review workflow:
1. Load task specification and implementation
2. Verify acceptance criteria met
3. Review code quality (if --include-code-review)
4. Check test coverage and quality
5. Validate documentation
6. Assess error handling
7. Generate review report with findings

The skill will parse $ARGUMENTS for:
- `task-id` - Task identifier (e.g., task-006) (required)
- `--include-code-review` - Include detailed code review (optional)

Output: Task review report with findings, recommendations, and approval status
