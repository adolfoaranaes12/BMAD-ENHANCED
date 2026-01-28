---
description: Generate risk profile with mitigation strategies and test priorities
argument-hint: <requirements-file> [--risk-threshold high|medium|low]
allowed-tools: Skill
---

Invoke the risk-profile skill:

Use Skill tool: `Skill(command="risk-profile")`

This will execute the risk profiling workflow:
1. Load requirements (PRD, epic, or architecture)
2. Identify risk categories (technical, security, performance, integration, data)
3. Assess risk likelihood and impact
4. Calculate risk scores (P0: critical, P1: high, P2: medium, P3: low)
5. Generate mitigation strategies
6. Prioritize test coverage based on risk
7. Create risk profile document

The skill will parse $ARGUMENTS for:
- `requirements-file` - Path to requirements or architecture document (required)
- `--risk-threshold` - Focus on risks at or above: high (P0-P1), medium (P0-P2), low (all)
- `--include-mitigation` - Include detailed mitigation plans (default: true)

Output: Risk profile with scored risks, mitigation strategies, test priorities
