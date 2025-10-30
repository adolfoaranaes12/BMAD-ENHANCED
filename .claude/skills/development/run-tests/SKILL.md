---
name: run-tests
description: Execute tests with coverage analysis using bmad-commands, identify coverage gaps, and suggest missing tests. Use for test execution and quality validation.
acceptance:
  - tests_executed: "All matching tests successfully executed"
  - coverage_generated: "Coverage report generated successfully"
  - gaps_identified: "Coverage gaps analyzed and categorized"
  - suggestions_provided: "Missing test suggestions provided (if gaps exist)"
inputs:
  scope:
    type: string
    required: true
    description: "Test scope: task_id, file_path, or '--all'"
    validation: "Must be valid task ID, file path, or '--all'"
  coverage:
    type: boolean
    required: false
    description: "Generate coverage report"
    default: true
  framework:
    type: string
    required: false
    description: "Test framework (jest, pytest, mocha)"
    default: "jest"
outputs:
  tests_passed:
    type: boolean
    description: "Whether all tests passed"
  total_tests:
    type: number
    description: "Total number of tests executed"
  passed_tests:
    type: number
    description: "Number of tests that passed"
  failed_tests:
    type: number
    description: "Number of tests that failed"
  coverage_percent:
    type: number
    description: "Overall test coverage percentage"
  coverage_gaps:
    type: array
    description: "List of identified coverage gaps with criticality"
telemetry:
  emit: "skill.run-tests.completed"
  track:
    - scope
    - framework
    - total_tests
    - passed_tests
    - failed_tests
    - coverage_percent
    - duration_ms
    - gaps_count
---

# Run Tests Skill

## Purpose

Execute tests, generate coverage reports, analyze coverage gaps, and suggest missing tests to improve code quality and test completeness.

**Core Capabilities:**
- Test execution via bmad-commands
- Coverage report generation and analysis
- Gap identification with criticality assessment
- Missing test suggestions with concrete examples

## Prerequisites

- Test framework configured (Jest, Pytest, Mocha, etc.)
- Tests written for the code being tested
- bmad-commands skill available at `.claude/skills/bmad-commands/`
- Project dependencies installed

---

## Workflow

### Step 0: Determine Test Scope

**Action:** Parse input and identify which tests to run.

**Scope Types:**

**Task-based:**
```bash
# Input: task-auth-002-login
→ Extract keywords: "auth", "login"
→ Pattern: (auth|login)
→ Find matching test files
```

**File-based:**
```bash
# Input: src/controllers/auth.controller.ts
→ Find test: src/__tests__/**/auth.controller.test.ts
```

**All tests:**
```bash
# Input: --all
→ Run all test files matching **/*.test.ts
```

**See:** `references/test-execution-guide.md` for detailed scope determination

---

### Step 1: Execute Tests

**Action:** Use bmad-commands to run tests.

Execute:
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json
```

**Parse Response:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "coverage_percent": 87,
    "duration_ms": 2456,
    "failures": []
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest"
  },
  "errors": []
}
```

**Verify:**
- Check `success == true`
- Extract test results from `outputs`
- Check for failures in `outputs.failures`

**If tests fail:**
- Report failed tests from `outputs.failures`
- Provide failure details
- Suggest fixes or reruns

**See:** `references/test-execution-guide.md` for execution details

---

### Step 2: Generate Coverage Report

**Action:** Parse coverage data and generate reports.

**Coverage Metrics:**
- Statements coverage
- Branch coverage
- Function coverage
- Line coverage

**Parse Coverage:**
```json
{
  "coverage_percent": 87,
  "statements": { "covered": 210, "total": 240, "percent": 87.5 },
  "branches": { "covered": 45, "total": 52, "percent": 86.5 },
  "functions": { "covered": 28, "total": 28, "percent": 100 },
  "lines": { "covered": 208, "total": 238, "percent": 87.4 }
}
```

**Generate Text Report:**
```
File                  | % Stmts | % Branch | % Funcs | % Lines | Uncovered
----------------------|---------|----------|---------|---------|----------
auth.controller.ts    |   92.31 |    87.50 |     100 |   92.31 | 45-48,67
auth.service.ts       |   90.48 |    83.33 |     100 |   90.48 | 78,112-115
rate-limit.ts         |   88.89 |      100 |     100 |   88.89 | 23-25
jwt.ts                |     100 |      100 |     100 |     100 |
----------------------|---------|----------|---------|---------|----------
Overall               |   91.25 |    88.42 |     100 |   91.25 |
```

**Check Thresholds:**
- Statements: ≥80% required
- Branches: ≥80% required
- Functions: ≥80% required
- Lines: ≥80% required

**See:** `references/coverage-analysis-guide.md` for detailed coverage parsing

---

### Step 3: Analyze Coverage Gaps

**Action:** Identify uncovered code and categorize by criticality.

**Gap Categories:**

**1. Error Handling (High Priority)**
```typescript
// Uncovered error handling
catch (error) {
  console.error('Database error:', error);  // ❌ Uncovered
  return res.status(500).json({ error: 'Internal error' });
}
```

**2. Edge Cases (Medium Priority)**
```typescript
// Uncovered edge case
if (user.lastLogin && Date.now() - user.lastLogin > MAX_SESSION_AGE) {
  return res.status(401).json({ error: 'Session expired' }); // ❌ Uncovered
}
```

**3. Rare Branches (Low Priority)**
```typescript
// Uncovered rare branch
if (process.env.NODE_ENV === 'development') {  // ❌ Uncovered
  console.log('Debug mode');
}
```

**Criticality Assessment:**

**Critical (Must Test):**
- Security-related code
- Payment processing
- Data deletion/modification
- Authentication/authorization

**High (Should Test):**
- Error handling for expected errors
- Business logic edge cases
- State transitions

**Medium (Nice to Test):**
- Logging statements
- Non-critical error handling
- Minor edge cases

**Low (Optional):**
- Debug code
- Development-only code
- Trivial getters/setters

**See:** `references/gap-analysis-guide.md` for detailed gap analysis

---

### Step 4: Suggest Missing Tests

**Action:** Generate concrete test suggestions for coverage gaps.

**For each gap, provide:**
1. File and line numbers
2. Criticality level
3. Why it should be tested
4. Concrete test example

**Suggestion Format:**
```markdown
### Gap 1: Database Connection Failure
**File:** `src/controllers/auth.controller.ts:48-50`
**Criticality:** HIGH
**Why:** Production database failures are expected
**Test:**
```typescript
it('should return 503 when database is unavailable', async () => {
  jest.spyOn(db, 'isConnected').mockReturnValue(false);

  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'pass' });

  expect(response.status).toBe(503);
});
```
```

**Prioritization:**
1. HIGH priority gaps (3-5 suggestions)
2. MEDIUM priority gaps (2-3 suggestions)
3. LOW priority gaps (optional)

**See:** `references/test-suggestions.md` for suggestion templates

---

### Step 5: Present Summary

**Action:** Provide comprehensive test execution summary.

**Summary Format:**
```markdown
✅ Tests Executed Successfully

**Scope:** task-auth-002-login
**Framework:** jest
**Duration:** 13.7s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🧪 Test Results**

Test Suites: 2 passed, 2 total
Tests:       12 passed, 12 total
Status:      ✅ ALL TESTS PASSING

**📊 Coverage Report**

Overall Coverage: 91.25%

| Metric     | Coverage | Threshold | Status |
|------------|----------|-----------|--------|
| Statements | 91.25%   | ≥80%      | ✅ Pass |
| Branches   | 88.42%   | ≥80%      | ✅ Pass |
| Functions  | 100%     | ≥80%      | ✅ Pass |
| Lines      | 91.25%   | ≥80%      | ✅ Pass |

**Status:** ✅ ALL THRESHOLDS MET

**🔍 Coverage Gaps (5 identified)**

High Priority (3):
1. Database connection error handling
2. Session expiration check
3. Unexpected error catch block

Medium Priority (2):
4. Rate limiter error handling
5. Audit logging failure handling

**💡 Suggested Tests**

I can write 5 additional tests to improve coverage to ~96%:
1. Database failure handling (HIGH)
2. Session expiration (HIGH)
3. Unexpected error handling (HIGH)
4. Rate limiter resilience (MEDIUM)
5. Audit log resilience (MEDIUM)

Would you like me to add these tests?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Next Steps:**
- ✅ Tests passing
- ⚠️ Consider adding 3 HIGH priority tests (optional)
- ✅ Ready for review
```

---

## Output

Return structured output with telemetry:

```json
{
  "tests_passed": true,
  "total_tests": 12,
  "passed_tests": 12,
  "failed_tests": 0,
  "coverage_percent": 91.25,
  "coverage_gaps": [
    {
      "file": "src/controllers/auth.controller.ts",
      "lines": "48-50",
      "criticality": "HIGH",
      "category": "error_handling"
    }
  ],
  "telemetry": {
    "skill": "run-tests",
    "scope": "task-auth-002",
    "framework": "jest",
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "coverage_percent": 91.25,
    "duration_ms": 13685,
    "gaps_count": 5
  }
}
```

---

## Error Handling

If any step fails:

**1. No Tests Found:**
- Error: "No tests found matching scope"
- Action: Verify test files exist, check scope pattern

**2. Tests Failing:**
- Error: "X tests failing"
- Action: Report failures with details, suggest fixes

**3. Coverage Below Threshold:**
- Error: "Coverage X% below threshold Y%"
- Action: Identify gaps, suggest missing tests

**4. Test Framework Not Configured:**
- Error: "Test framework not detected"
- Action: Verify framework installation and configuration

---

## Common Scenarios

### Scenario 1: All Tests Passing, Good Coverage

If tests pass and coverage ≥80%:
- Report success
- Highlight any remaining gaps (optional improvements)
- Proceed with confidence

### Scenario 2: Tests Passing, Low Coverage

If tests pass but coverage <80%:
- Identify critical uncovered code
- Suggest HIGH priority tests first
- Offer to write missing tests

### Scenario 3: Tests Failing

If tests fail:
- Report which tests failed
- Show failure messages
- Suggest reviewing implementation
- Do not proceed with coverage analysis until tests pass

---

## Best Practices

1. **Run Tests Frequently** - After every significant change
2. **Prioritize Quality Over Coverage %** - Meaningful tests > 100% coverage
3. **Test What Matters** - Focus on business logic, error handling, edge cases
4. **Keep Tests Fast** - Mock external dependencies, use in-memory DBs
5. **Use Meaningful Test Names** - Describe expected behavior

**See:** `references/best-practices.md` for detailed testing best practices

---

## Routing Guidance

**Use this skill when:**
- Need to execute tests for implemented code
- Need coverage analysis
- Want to identify test gaps
- Need to validate implementation quality

**Always use after:**
- Feature implementation (`implement-feature`)
- Bug fixes (`fix-bug`)
- Code refactoring (`refactor-code`)

**Before:**
- Creating pull requests
- Deploying to production
- Code reviews

---

## Reference Files

Detailed documentation in `references/`:

- **test-execution-guide.md**: Test configuration and execution details
- **coverage-analysis-guide.md**: Coverage parsing and threshold checking
- **gap-analysis-guide.md**: Analyzing uncovered code and categorization
- **test-suggestions.md**: Missing test suggestion templates
- **best-practices.md**: Testing and coverage best practices

---

## Using This Skill

**From James subagent:**
```bash
@james *test task-auth-002
```

**Directly:**
```bash
Use .claude/skills/development/run-tests/SKILL.md with input {scope: "task-auth-002", coverage: true}
```

---

## Philosophy

This skill embodies BMAD's 3-layer architecture:

- **Uses Commands** (Layer 1): bmad-commands for run_tests
- **Provides Composition** (Layer 2): Test execution + analysis workflow
- **Enables Orchestration** (Layer 3): Called by James after implementation

By using commands, this skill is:
- **Observable**: Telemetry tracks test metrics
- **Testable**: Commands have known contracts
- **Composable**: Fits into implementation workflow
- **Reliable**: Deterministic test execution

---

*Part of BMAD Enhanced Development Suite*
