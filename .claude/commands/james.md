---
description: Route implementation commands to James (Developer) subagent for feature implementation, bug fixes, refactoring, QA fixes, debugging, and code explanation
argument-hint: <command> <args>
allowed-tools: Task
---

# James (Developer) Command Router

Route user commands to the james-developer-v2 subagent for implementation operations.

## Usage

```bash
/james <command> <args>
```

## Available Commands

- `*implement` - Implement features using TDD
- `*fix` - Fix bugs with test coverage
- `*test` - Run tests and report results
- `*refactor` - Refactor code safely
- `*apply-qa-fixes` - Apply QA review fixes
- `*debug` - Debug issues with diagnostics
- `*explain` - Explain code functionality

## Examples

```bash
/james *implement task-auth-002
/james *fix bug-login-timeout
/james *test src/auth/
/james *refactor src/auth/login.ts
/james *apply-qa-fixes task-auth-002
/james *debug "Login failing with 500 error"
/james *explain src/auth/jwt.ts
```

## Implementation

Parse command and arguments from user input.

Command format: /james <command> <args>

Extract:
- command: ${1} (first argument, e.g., "implement")
- args: ${@:2} (remaining arguments)

Route to james-developer-v2 subagent:
Invoke @james-developer-v2 with command "*${1} ${@:2}"
