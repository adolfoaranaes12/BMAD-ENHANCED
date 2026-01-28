---
description: Run comprehensive quality gate assessment with pass/fail decision
argument-hint: <task-id> [--strict]
allowed-tools: Skill
---

Invoke the quality-gate skill:

Use Skill tool: `Skill(command="quality-gate")`

This will execute the quality gate assessment workflow:
1. Load task specification and implementation
2. Verify acceptance criteria coverage
3. Assess quality across 8 dimensions:
   - Requirements coverage
   - Code quality
   - Test coverage
   - Documentation
   - Security
   - Performance
   - Error handling
   - NFR compliance
4. Calculate quality score
5. Make pass/fail decision
6. Generate comprehensive report

The skill will parse $ARGUMENTS for:
- `task-id` - Task identifier (e.g., task-006) (required)
- `--strict` - Use strict thresholds (80%+ required vs 70%+)

Output: Quality gate report with pass/fail decision and remediation guidance
