---
description: Route Business Analysis commands to Mary for brainstorming, market research, competitive analysis, and early-stage discovery
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the mary-analyst subagent for Business Analysis operations.

Use the Task tool with:
- subagent_type: mary-analyst
- description: Mary Business Analyst command
- prompt: Execute Business Analysis command: $ARGUMENTS
