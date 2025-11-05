---
description: Route Scrum Master commands to Bob for developer-ready story creation and clear handoffs
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the bob-sm subagent for Scrum Master operations.

Use the Task tool with:
- subagent_type: bob-sm
- description: Bob Scrum Master command
- prompt: Execute Scrum Master command: $ARGUMENTS
