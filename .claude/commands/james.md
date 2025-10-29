Parse command and arguments from user input.

Command format: /james <command> <args>

Example: /james implement task-auth-002

Extract:
- command: ${1} (first argument, e.g., "implement")
- args: ${@:2} (remaining arguments)

Route to router skill:
Use .claude/skills/router.md with command "@james *${1} ${@:2}"
