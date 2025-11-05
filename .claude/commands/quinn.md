---
description: Route quality assessment commands to Quinn (Quality) subagent for code reviews, NFR assessments, quality gate decisions, requirements tracing, and risk assessment
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the quinn-quality-v2 subagent for quality operations.

Use the Task tool with:
- subagent_type: quinn-quality-v2
- description: Quinn quality command
- prompt: Execute quality command: $ARGUMENTS
