---
description: Route implementation commands to James (Developer) subagent for feature implementation, bug fixes, refactoring, QA fixes, debugging, and code explanation
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the james-developer-v2 subagent for implementation operations.

Use the Task tool with:
- subagent_type: james-developer-v2
- description: James development command
- prompt: Execute development command: $ARGUMENTS
