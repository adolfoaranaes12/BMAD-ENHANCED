---
description: Execute test suite with coverage analysis and gap identification
argument-hint: [test-path] [--coverage] [--suggest-tests]
allowed-tools: Skill
---

Invoke the run-tests skill:

Use Skill tool: `Skill(command="run-tests")`

This will execute the test execution workflow:
1. Discover test files and framework
2. Execute test suite (unit, integration, E2E)
3. Analyze test results and failures
4. Calculate coverage metrics
5. Identify coverage gaps
6. Suggest additional tests (if --suggest-tests)
7. Generate test execution report

The skill will parse $ARGUMENTS for:
- `test-path` - Path to tests or specific test file (default: auto-discover)
- `--coverage` - Include coverage analysis (default: true)
- `--suggest-tests` - Generate test suggestions for gaps (default: false)
- `--level` - Test level: unit, integration, e2e, all (default: all)

Output: Test execution report with results, coverage metrics, gap analysis, test suggestions
