---
description: Route quality assessment commands to Quinn (Quality) subagent for code reviews, NFR assessments, quality gate decisions, requirements tracing, and risk assessment
argument-hint: <command> <args>
allowed-tools: Task
---

# Quinn (Quality) Command Router

Route user commands to the quinn-quality-v2 subagent for quality operations.

## Usage

```bash
/quinn <command> <args>
```

## Available Commands

- `*review` - Comprehensive quality review
- `*assess-nfr` - Assess non-functional requirements
- `*validate-quality-gate` - Make quality gate decision
- `*trace-requirements` - Trace requirements to code/tests
- `*assess-risk` - Assess implementation risks

## Examples

```bash
/quinn *review task-auth-002
/quinn *assess-nfr task-auth-002
/quinn *validate-quality-gate task-auth-002
/quinn *trace-requirements task-auth-002
/quinn *assess-risk task-auth-002
```

## Implementation

Parse command and arguments from user input.

Command format: /quinn <command> <args>

Extract:
- command: ${1} (first argument, e.g., "review")
- args: ${@:2} (remaining arguments)

Route to quinn-quality-v2 subagent:
Invoke @quinn-quality-v2 with command "*${1} ${@:2}"
