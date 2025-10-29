Parse command and arguments from user input.

Command format: /orchestrator <command> <args>

Example: /orchestrator deliver "User login feature"

Extract:
- command: ${1} (first argument, e.g., "deliver")
- args: ${@:2} (remaining arguments)

Route to router skill:
Use .claude/skills/router.md with command "@orchestrator *${1} ${@:2}"
