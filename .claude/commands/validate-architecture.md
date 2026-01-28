---
description: Validate architecture document for completeness, quality, and adherence to standards
argument-hint: <architecture-file> [--strict]
allowed-tools: Skill
---

Invoke the validate-architecture skill:

Use Skill tool: `Skill(command="validate-architecture")`

This will execute the architecture validation workflow:
1. Load architecture document
2. Check required sections present
3. Validate technology decisions have justifications
4. Verify ADRs exist and are complete
5. Assess NFR mapping
6. Check security considerations documented
7. Calculate validation score
8. Generate validation report with pass/fail

The skill will parse $ARGUMENTS for:
- `architecture-file` - Path to architecture document (default: docs/architecture.md)
- `--strict` - Use strict validation thresholds (default: false)

Output: Validation report with score, missing elements, pass/fail decision
