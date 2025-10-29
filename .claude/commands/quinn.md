Parse command and arguments from user input.

Command format: /quinn <command> <args>

Example: /quinn review task-auth-002

Extract:
- command: ${1} (first argument, e.g., "review")
- args: ${@:2} (remaining arguments)

Route to router skill:
Use .claude/skills/router.md with command "@quinn *${1} ${@:2}"
