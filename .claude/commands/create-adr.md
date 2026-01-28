---
description: Create Architecture Decision Record for technical decisions
argument-hint: <context> [--decision <decision>]
allowed-tools: Skill
---

Invoke the create-adr skill:

Use Skill tool: `Skill(command="create-adr")`

This will execute the ADR creation workflow:
1. Parse context (problem statement or file reference)
2. Analyze decision context and constraints
3. Generate alternatives (typically 3 options)
4. Evaluate trade-offs for each alternative
5. Select recommended decision (or use --decision arg)
6. Create ADR document following template
7. Assign ADR number and save to docs/adrs/

The skill will parse $ARGUMENTS for:
- `context` - Decision context, problem, or file reference (required)
- `--decision` - Pre-selected decision (optional, skill will recommend if not provided)

Output: ADR file at docs/adrs/adr-XXX-title.md with context, alternatives, trade-offs, decision
