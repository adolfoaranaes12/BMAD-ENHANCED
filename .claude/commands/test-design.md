---
description: Design comprehensive test strategy with test scenarios and coverage plan
argument-hint: <requirements-file> [--level unit|integration|e2e|all]
allowed-tools: Skill
---

Invoke the test-design skill:

Use Skill tool: `Skill(command="test-design")`

This will execute the test design workflow:
1. Load requirements (PRD, epic, or task spec)
2. Identify testable requirements
3. Generate test scenarios for each requirement
4. Design test cases (happy path, edge cases, error cases)
5. Plan test data and mocking strategy
6. Create test coverage matrix
7. Generate test design document

The skill will parse $ARGUMENTS for:
- `requirements-file` - Path to requirements document (required)
- `--level` - Test level: unit, integration, e2e, all (default: all)
- `--focus` - Focus area: happy-path, edge-cases, security, performance
- `--include-cicd` - Include CI/CD integration plan (default: true)

Output: Test design document with scenarios, cases, coverage plan, CI/CD strategy
