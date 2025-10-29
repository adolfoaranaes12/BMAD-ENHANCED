Parse command and arguments from user input.

Command format: /alex <command> <args>

Example: /alex breakdown "User Authentication System"

Extract:
- command: ${1} (first argument, e.g., "breakdown")
- args: ${@:2} (remaining arguments)

Route to router skill:
Use .claude/skills/router.md with command "@alex *${1} ${@:2}"
