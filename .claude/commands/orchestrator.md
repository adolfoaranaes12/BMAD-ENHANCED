---
description: Route workflow orchestration commands to Orchestrator subagent for multi-step workflows, cross-subagent coordination, and complete feature delivery pipelines
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the orchestrator-v2 subagent for workflow operations.

Use the Task tool with:
- subagent_type: orchestrator-v2
- description: Orchestrator workflow command
- prompt: Execute workflow command: $ARGUMENTS
