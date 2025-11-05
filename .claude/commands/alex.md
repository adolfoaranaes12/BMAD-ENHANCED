---
description: Route planning commands to Alex (Planner) subagent for requirements analysis, task specifications, epic breakdowns, estimation, and sprint planning
argument-hint: <command> <args>
allowed-tools: Task
---

# Alex (Planner) Command Router

Route user commands to the alex-planner-v2 subagent for planning operations.

## Usage

```bash
/alex <command> <args>
```

## Available Commands

- `*create-task-spec` - Create detailed task specifications
- `*breakdown-epic` - Break down epics into user stories
- `*estimate` - Estimate story points for backlog items
- `*refine-story` - Refine vague requirements into clear stories
- `*plan-sprint` - Plan sprint backlog with velocity

## Examples

```bash
/alex *create-task-spec "User login with email validation"
/alex *breakdown-epic "User Authentication System"
/alex *estimate story-auth-005
/alex *refine-story "Users should be able to log in"
/alex *plan-sprint "Sprint 15" --velocity 40
```

## Implementation

Parse command and arguments from user input.

Command format: /alex <command> <args>

Extract:
- command: ${1} (first argument, e.g., "breakdown")
- args: ${@:2} (remaining arguments)

Route to alex-planner-v2 subagent:
Invoke @alex-planner-v2 with command "*${1} ${@:2}"
