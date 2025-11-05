---
description: Route Product Owner commands to Sarah for backlog management, story validation, quality assurance, and INVEST criteria enforcement
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the sarah-po subagent for Product Owner operations.

Use the Task tool with:
- subagent_type: sarah-po
- description: Sarah Product Owner command
- prompt: Execute Product Owner command: $ARGUMENTS
