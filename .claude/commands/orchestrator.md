---
description: Route workflow orchestration commands to Orchestrator subagent for multi-step workflows, cross-subagent coordination, and complete feature delivery pipelines
argument-hint: <command> <args>
allowed-tools: Task
---

# Orchestrator Command Router

Route user commands to the orchestrator-v2 subagent for workflow operations.

## Usage

```bash
/orchestrator <command> <args>
```

## Available Commands

- `*workflow` - Execute complete workflows (feature-delivery, epic-to-sprint, sprint-execution)
- `*coordinate` - Cross-subagent coordination
- `*resume` - Resume failed workflow
- `*abort` - Abort running workflow
- `*status` - Check workflow status

## Examples

```bash
/orchestrator *workflow feature-delivery "Add logout button"
/orchestrator *workflow epic-to-sprint "User Authentication" --velocity 40
/orchestrator *coordinate "Validate architecture and create plan" --subagents winston,alex
/orchestrator *resume workflow-003
/orchestrator *status workflow-001
```

## Implementation

Parse command and arguments from user input.

Command format: /orchestrator <command> <args>

Extract:
- command: ${1} (first argument, e.g., "deliver")
- args: ${@:2} (remaining arguments)

Route to orchestrator-v2 subagent:
Invoke @orchestrator-v2 with command "*${1} ${@:2}"
