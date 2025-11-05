---
description: Route planning commands to Alex (Planner) subagent for requirements analysis, task specifications, epic breakdowns, estimation, and sprint planning
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the alex-planner-v2 subagent for planning operations.

Use the Task tool with:
- subagent_type: alex-planner-v2
- description: Alex planning command
- prompt: Execute planning command: $ARGUMENTS
