---
description: Route Product Manager commands to John for PRD creation, product strategy, and feature prioritization
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the john-pm subagent for Product Manager operations.

Use the Task tool with:
- subagent_type: john-pm
- description: John Product Manager command
- prompt: Execute Product Manager command: $ARGUMENTS
