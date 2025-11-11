---
description: Execute interactive checklist-driven workflows with decision branching
argument-hint: "<checklist-path> [--context <file>]"
allowed-tools: Skill
---

Invoke the interactive-checklist skill:

Use Skill tool with skill="interactive-checklist"

This will execute the interactive checklist workflow:
1. Load checklist template with decision points
2. Execute checklist items sequentially
3. Handle user input for decisions and branches
4. Track completion status and workflow state
5. Generate completion report with decisions made

The skill will parse $ARGUMENTS for:
- `checklist-path` - Path to checklist template file (required)
- `--context` - Optional context file for checklist execution

Output: Completed checklist with decisions, actions taken, and completion report
