---
description: Apply fixes from quality gate report in priority order
argument-hint: <gate-report-file> [--priority high|all]
allowed-tools: Skill
---

Invoke the apply-qa-fixes skill:

Use Skill tool: `Skill(command="apply-qa-fixes")`

This will execute the QA fix application workflow:
1. Load quality gate report
2. Parse issues and recommendations
3. Prioritize fixes (critical → high → medium)
4. Apply fixes incrementally
5. Run tests after each fix
6. Validate issue resolution
7. Generate fix application report

The skill will parse $ARGUMENTS for:
- `gate-report-file` - Path to quality gate report (required)
- `--priority` - Fix priority level: high (critical+high only), all (default: high)
- `--batch` - Apply fixes in batch vs incrementally (default: incremental)

Output: Applied fixes, test results, updated quality gate report
