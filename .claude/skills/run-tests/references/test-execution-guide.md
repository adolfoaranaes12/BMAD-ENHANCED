# Test Execution Guide

## Purpose

Detailed guide for test execution configuration, scope determination, and running tests with bmad-commands.

---

## Test Scope Determination

### Task-Based Scope

**Input:** `task-auth-002-login`

**Process:**
1. Extract component: "auth"
2. Extract action: "login"
3. Build pattern: `(auth|login)`
4. Find files: `**/*auth*.test.ts`, `**/*login*.test.ts`

**Example:**
```bash
# Matches:
src/__tests__/services/auth.service.test.ts
src/__tests__/controllers/auth.controller.test.ts
src/__tests__/integration/auth-login.integration.test.ts
```

### File-Based Scope

**Input:** `src/controllers/auth.controller.ts`

**Process:**
1. Extract filename: "auth.controller"
2. Find test file: `**/*auth.controller.test.ts`

**Example:**
```bash
# Matches:
src/__tests__/controllers/auth.controller.test.ts
```

### Suite-Based Scope

**Input:** `--suite integration`

**Process:**
1. Find suite directory: `integration/`
2. Match all tests: `**/__tests__/integration/**/*.test.ts`

**Example:**
```bash
# Matches:
src/__tests__/integration/auth.integration.test.ts
src/__tests__/integration/user.integration.test.ts
src/__tests__/integration/payment.integration.test.ts
```

---

## Test Configuration

### Jest Configuration

**File:** `jest.config.js` or `package.json`

```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  coverageDirectory: 'coverage',
  coverageReporters: ['text', 'lcov', 'html'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/*.test.ts'
  ],
  testMatch: [
    '**/__tests__/**/*.test.ts',
    '**/?(*.)+(spec|test).ts'
  ],
  coverageThresholds: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

### Pytest Configuration

**File:** `pytest.ini` or `setup.cfg`

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --cov=src
    --cov-report=term
    --cov-report=html
    --cov-report=xml
    --cov-fail-under=80
```

---

## Using bmad-commands

### Execute Tests

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --output json
```

### Parameters

**--path** (required)
- Directory or file to test
- Examples: `.`, `src/controllers`, `src/auth/login.ts`

**--framework** (required)
- Test framework: `jest`, `pytest`, `mocha`

**--output** (optional)
- Output format: `json` (default), `text`

**--pattern** (optional)
- Test file pattern: `auth`, `login`, `integration`

**--coverage** (optional)
- Generate coverage: `true` (default), `false`

### Response Format

```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "skipped_tests": 0,
    "coverage_percent": 87.5,
    "duration_ms": 2456,
    "failures": []
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest",
    "duration_ms": 2500
  },
  "errors": []
}
```

---

## Test Execution Patterns

### Pattern 1: All Tests

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto
```

### Pattern 2: Specific Pattern

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --pattern auth
```

### Pattern 3: Specific File

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path src/__tests__/controllers/auth.controller.test.ts \
  --framework auto
```

### Pattern 4: With Coverage

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --coverage true
```

---

## Parsing Test Results

### Success Response

```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0
  }
}
```

**Interpretation:**
- All tests passed ✅
- 12/12 tests successful
- Ready to analyze coverage

### Failure Response

```json
{
  "success": true,
  "outputs": {
    "passed": false,
    "total_tests": 12,
    "passed_tests": 8,
    "failed_tests": 4,
    "failures": [
      {
        "test": "should return 401 for wrong password",
        "file": "auth.controller.test.ts",
        "message": "Expected 401, got 500",
        "stack": "..."
      }
    ]
  }
}
```

**Interpretation:**
- Tests failing ❌
- 8/12 tests passed, 4 failed
- Review failures before proceeding

---

## Handling Test Failures

### Step 1: Review Failure Messages

```typescript
for (const failure of outputs.failures) {
  console.log(`Failed: ${failure.test}`);
  console.log(`File: ${failure.file}`);
  console.log(`Reason: ${failure.message}`);
}
```

### Step 2: Categorize Failures

**Implementation bugs:**
- Code doesn't match expected behavior
- Fix implementation, re-run tests

**Test bugs:**
- Test expectations incorrect
- Fix test, re-run

**Environment issues:**
- Database not running
- Missing dependencies
- Fix environment, re-run

### Step 3: Report to User

```markdown
❌ Tests Failed

4 tests failing:

1. **should return 401 for wrong password**
   - File: auth.controller.test.ts
   - Error: Expected 401, got 500
   - Likely: Missing error handling in controller

2. **should handle database errors**
   - File: auth.service.test.ts
   - Error: TypeError: Cannot read property 'findByEmail' of undefined
   - Likely: Mock not properly configured

[Continue for all failures...]

**Action Required:**
1. Fix failing tests
2. Re-run: @james *test task-auth-002
```

---

## Quick Reference

**Common Commands:**
```bash
# All tests
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto

# Specific pattern
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto --pattern auth

# With coverage
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto --coverage true
```

**Response Fields:**
- `success`: Command executed successfully
- `outputs.passed`: All tests passed
- `outputs.total_tests`: Total test count
- `outputs.coverage_percent`: Overall coverage
- `outputs.failures`: Array of failed tests

---

*Part of run-tests skill - Development Suite*
