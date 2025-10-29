# Run Tests Skill

## Purpose
Run tests, generate coverage reports, analyze test gaps, and suggest improvements. This skill provides comprehensive test execution and analysis for validating implementations.

## When to Use This Skill
- Running tests after implementation
- Generating coverage reports
- Analyzing test coverage gaps
- Identifying missing test cases
- Running tests in CI/CD pipeline
- Debugging failing tests
- Validating test quality

## Invocation
```bash
# Run all tests
@james *test --all

# Run tests for specific task
@james *test task-auth-002

# Run tests for specific file
@james *test src/controllers/auth.controller.ts

# Run with coverage
@james *test task-auth-002 --coverage

# Run in watch mode
@james *test src/services/auth.service.ts --watch

# Analyze coverage gaps
@james *coverage task-auth-002

# Run specific test suite
@james *test --suite integration
```

## Prerequisites
- Test framework configured (Jest, Mocha, etc.)
- Tests written for the code
- Project dependencies installed

## Skill Configuration
```yaml
skill_name: run-tests
version: 1.0.0
subagent: james-developer
execution_mode: sequential
halt_on_error: false
output_directory: coverage/
```

---

## STEP 0: Load Configuration and Determine Test Scope

### Actions
1. Parse test command and parameters
2. Determine which tests to run
3. Load test configuration
4. Identify test framework
5. Set execution options

### Parse Input

**Examples:**

```bash
# Input: task-auth-002
→ Scope: Tests related to task-auth-002
→ Pattern: auth, login
→ Files: src/__tests__/**/*auth*.test.ts

# Input: src/controllers/auth.controller.ts
→ Scope: Tests for specific file
→ Pattern: auth.controller
→ Files: src/__tests__/**/auth.controller.test.ts

# Input: --all
→ Scope: All tests
→ Pattern: **/*.test.ts
→ Files: All test files

# Input: --suite integration
→ Scope: Integration test suite
→ Pattern: integration
→ Files: src/__tests__/integration/**/*.test.ts
```

### Load Test Configuration

**From:** `package.json` or `jest.config.js`

```json
{
  "jest": {
    "preset": "ts-jest",
    "testEnvironment": "node",
    "coverageDirectory": "coverage",
    "coverageReporters": ["text", "lcov", "html"],
    "collectCoverageFrom": [
      "src/**/*.ts",
      "!src/**/*.d.ts",
      "!src/**/*.test.ts"
    ],
    "testMatch": [
      "**/__tests__/**/*.test.ts",
      "**/?(*.)+(spec|test).ts"
    ],
    "coverageThresholds": {
      "global": {
        "branches": 80,
        "functions": 80,
        "lines": 80,
        "statements": 80
      }
    }
  }
}
```

### Determine Test Pattern

**For task-based testing:**
```typescript
// task-auth-002-login
→ Extract keywords: "auth", "login"
→ Build pattern: (auth|login)
→ Find related test files
```

**For file-based testing:**
```typescript
// src/controllers/auth.controller.ts
→ Extract: auth.controller
→ Find test: src/__tests__/**/auth.controller.test.ts
```

---

## STEP 1: Run Tests

### Actions
1. Build test command
2. Execute tests
3. Capture output (stdout, stderr)
4. Parse test results
5. Report status

### Build Test Command

**Pattern:**
```bash
npm test -- [options] [pattern]
```

**Examples:**

```bash
# All tests
npm test

# Specific pattern
npm test -- --testPathPattern="auth"

# With coverage
npm test -- --coverage

# Verbose output
npm test -- --verbose

# Watch mode
npm test -- --watch

# Update snapshots
npm test -- -u
```

### Execute Tests

```bash
npm test -- --testPathPattern="auth" --coverage
```

### Capture Output

```
PASS src/__tests__/services/auth.service.test.ts (5.234 s)
  [Unit] AuthService
    findUserByEmail
      ✓ should return user when email exists (12 ms)
      ✓ should return null when email does not exist (8 ms)
    verifyPassword
      ✓ should return true for correct password (102 ms)
      ✓ should return false for incorrect password (98 ms)

PASS src/__tests__/integration/auth.integration.test.ts (8.451 s)
  [Integration] POST /api/auth/login
    ✓ should return 200 and JWT token for valid credentials (125 ms)
    ✓ should return 401 for wrong password (110 ms)
    ✓ should return 401 for non-existent email (108 ms)
    ✓ should return 400 for missing email (95 ms)
    ✓ should return 400 for missing password (92 ms)
    ✓ should return 400 for invalid email format (88 ms)
    ✓ should return 429 after 5 failed attempts (250 ms)

Test Suites: 2 passed, 2 total
Tests:       11 passed, 11 total
Snapshots:   0 total
Time:        13.685 s
```

### Parse Test Results

```yaml
test_suites:
  passed: 2
  failed: 0
  total: 2

tests:
  passed: 11
  failed: 0
  skipped: 0
  total: 11

duration: 13.685s

status: SUCCESS
```

---

## STEP 2: Generate Coverage Report

### Actions
1. Parse coverage data
2. Generate reports (text, HTML, lcov)
3. Identify uncovered lines
4. Calculate coverage percentages
5. Compare against thresholds

### Parse Coverage Data

**From:** `coverage/coverage-final.json`

```json
{
  "/path/to/src/controllers/auth.controller.ts": {
    "path": "/path/to/src/controllers/auth.controller.ts",
    "statementMap": { ... },
    "fnMap": { ... },
    "branchMap": { ... },
    "s": { "0": 1, "1": 1, "2": 0, ... },
    "f": { "0": 1, "1": 0, ... },
    "b": { "0": [1, 0], ... }
  }
}
```

### Generate Text Report

```
---------------------------|---------|----------|---------|---------|-------------------
File                       | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
---------------------------|---------|----------|---------|---------|-------------------
All files                  |   91.25 |    88.42 |     100 |   91.25 |
 controllers               |   92.31 |    87.50 |     100 |   92.31 |
  auth.controller.ts       |   92.31 |    87.50 |     100 |   92.31 | 45-48,67
 middleware                |   88.89 |      100 |     100 |   88.89 |
  rate-limit.ts            |   88.89 |      100 |     100 |   88.89 | 23-25
 services                  |   90.48 |    83.33 |     100 |   90.48 |
  auth.service.ts          |   90.48 |    83.33 |     100 |   90.48 | 78,112-115
 utils                     |   95.00 |    90.00 |     100 |   95.00 |
  jwt.ts                   |     100 |      100 |     100 |     100 |
  audit.ts                 |   90.00 |    80.00 |     100 |   90.00 | 34-36,55
---------------------------|---------|----------|---------|---------|-------------------
```

### Identify Uncovered Lines

**Example:**

**File:** `src/controllers/auth.controller.ts`

**Uncovered Lines:** 45-48, 67

```typescript
40: export const login = async (req, res) => {
41:   try {
42:     const validationResult = loginSchema.safeParse(req.body);
43:     if (!validationResult.success) {
44:       return res.status(400).json({ error: 'Validation error' });
45:     }                                                              // ✅ Covered
46:
47:     // Uncovered: Database connection error handling
48:     if (!isDatabaseConnected()) {                                  // ❌ Line 48 uncovered
49:       return res.status(503).json({ error: 'Service unavailable' }); // ❌ Line 49 uncovered
50:     }                                                              // ❌ Line 50 uncovered
51:
52:     const user = await authService.authenticateUser(email, password);
...
65:     return res.status(200).json({ token, expiresIn: 86400 });
66:   } catch (error) {
67:     console.error('Unexpected error:', error);                     // ❌ Line 67 uncovered
68:     return res.status(500).json({ error: 'Internal error' });
69:   }
70: };
```

### Check Thresholds

```yaml
Coverage Thresholds:
  Statements: 80% required, 91.25% actual ✅ PASS
  Branches:   80% required, 88.42% actual ✅ PASS
  Functions:  80% required, 100%   actual ✅ PASS
  Lines:      80% required, 91.25% actual ✅ PASS

Overall: ✅ PASS (all thresholds met)
```

---

## STEP 3: Analyze Coverage Gaps

### Actions
1. Identify uncovered code blocks
2. Categorize gaps (happy path, error path, edge case)
3. Assess criticality (critical, high, medium, low)
4. Suggest missing tests

### Categorize Uncovered Code

**Types of gaps:**

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
if (user.lastLogin && Date.now() - user.lastLogin > MAX_SESSION_AGE) {  // ❌ Uncovered
  return res.status(401).json({ error: 'Session expired' });
}
```

**3. Rare Branches (Low Priority)**
```typescript
// Uncovered rare branch
if (process.env.NODE_ENV === 'development') {  // ❌ Uncovered
  console.log('Debug mode active');
}
```

**4. Dead Code (Should Remove)**
```typescript
// Uncovered dead code
if (false) {  // ❌ Uncovered (impossible branch)
  doSomething();
}
```

### Assess Criticality

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

### Example Gap Analysis

```markdown
## Coverage Gap Analysis

### Gap 1: Database Connection Error Handling
**File:** `src/controllers/auth.controller.ts:48-50`
**Uncovered:**
```typescript
if (!isDatabaseConnected()) {
  return res.status(503).json({ error: 'Service unavailable' });
}
```

**Category:** Error Handling
**Criticality:** HIGH
**Reason:** Database failures are expected in production
**Suggested Test:**
```typescript
it('should return 503 when database is unavailable', async () => {
  // Mock database connection failure
  jest.spyOn(db, 'isConnected').mockReturnValue(false);

  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'pass' });

  expect(response.status).toBe(503);
  expect(response.body.error).toBe('Service unavailable');
});
```

---

### Gap 2: Unexpected Error Catch Block
**File:** `src/controllers/auth.controller.ts:67`
**Uncovered:**
```typescript
catch (error) {
  console.error('Unexpected error:', error);
  return res.status(500).json({ error: 'Internal error' });
}
```

**Category:** Error Handling
**Criticality:** MEDIUM
**Reason:** Unexpected errors are rare but should be tested
**Suggested Test:**
```typescript
it('should return 500 for unexpected errors', async () => {
  // Mock service to throw unexpected error
  jest.spyOn(authService, 'authenticateUser')
    .mockRejectedValue(new Error('Unexpected error'));

  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'pass' });

  expect(response.status).toBe(500);
  expect(response.body.error).toBe('Internal error');
});
```

---

### Gap 3: Session Expiration Edge Case
**File:** `src/services/auth.service.ts:112-115`
**Uncovered:**
```typescript
if (user.lastLogin && Date.now() - user.lastLogin > MAX_SESSION_AGE) {
  return null; // Session expired
}
```

**Category:** Edge Case
**Criticality:** HIGH
**Reason:** Security-related, prevents old sessions
**Suggested Test:**
```typescript
it('should reject login if session expired', async () => {
  const user = await User.create({
    email: 'test@example.com',
    password: hashedPassword,
    lastLogin: Date.now() - (MAX_SESSION_AGE + 1000) // Expired
  });

  const result = await authService.authenticateUser(
    'test@example.com',
    'password'
  );

  expect(result).toBeNull();
});
```
```

---

## STEP 4: Generate Coverage Report (HTML)

### Actions
1. Open HTML coverage report in browser (if possible)
2. Highlight uncovered lines visually
3. Provide link to report

### HTML Report Structure

```
coverage/
├── index.html                    (overview)
├── lcov-report/
│   ├── index.html               (detailed by file)
│   ├── controllers/
│   │   └── auth.controller.ts.html
│   ├── services/
│   │   └── auth.service.ts.html
│   └── utils/
│       ├── jwt.ts.html
│       └── audit.ts.html
└── lcov.info                     (for CI/CD)
```

### Visual Coverage Indicators

**In HTML report:**
- 🟢 Green: Covered lines
- 🔴 Red: Uncovered lines
- 🟡 Yellow: Partially covered (branches)

### Provide Link

```markdown
📊 Coverage Report Generated

HTML Report: file:///path/to/project/coverage/lcov-report/index.html

Quick Stats:
- Overall Coverage: 91.25%
- Files with < 80% coverage: 2
  - src/middleware/rate-limit.ts (88.89%)
  - src/services/auth.service.ts (90.48%)

Navigate to HTML report to see line-by-line coverage.
```

---

## STEP 5: Suggest Missing Tests

### Actions
1. Based on gap analysis, create test suggestions
2. Prioritize by criticality
3. Provide concrete test examples
4. Offer to write tests (if requested)

### Test Suggestions Report

```markdown
## Missing Test Recommendations

**Priority: HIGH (3 tests)**

### 1. Database Connection Failure
**File:** `src/controllers/auth.controller.ts`
**Line:** 48-50
**Why:** Production database failures are expected
**Test:**
```typescript
describe('[Error Handling] Database failures', () => {
  it('should return 503 when database is unavailable', async () => {
    jest.spyOn(db, 'isConnected').mockReturnValue(false);

    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'pass' });

    expect(response.status).toBe(503);
    expect(response.body).toHaveProperty('error', 'Service unavailable');
  });
});
```

### 2. Session Expiration
**File:** `src/services/auth.service.ts`
**Line:** 112-115
**Why:** Security-critical, prevents expired sessions
**Test:**
```typescript
describe('[Security] Session expiration', () => {
  it('should reject authentication if session expired', async () => {
    const expiredUser = {
      email: 'test@example.com',
      password_hash: await bcrypt.hash('pass', 12),
      lastLogin: Date.now() - (MAX_SESSION_AGE + 1000)
    };
    await User.create(expiredUser);

    const result = await authService.authenticateUser('test@example.com', 'pass');

    expect(result).toBeNull();
  });
});
```

### 3. Unexpected Error Handling
**File:** `src/controllers/auth.controller.ts`
**Line:** 67-68
**Why:** Ensures graceful failure for unexpected errors
**Test:**
```typescript
describe('[Error Handling] Unexpected errors', () => {
  it('should return 500 for unexpected service errors', async () => {
    jest.spyOn(authService, 'authenticateUser')
      .mockRejectedValue(new Error('Unexpected'));

    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'pass' });

    expect(response.status).toBe(500);
    expect(response.body).toHaveProperty('error', 'Internal error');
  });
});
```

---

**Priority: MEDIUM (2 tests)**

### 4. Rate Limiter Error Handling
**File:** `src/middleware/rate-limit.ts`
**Line:** 23-25
**Why:** Ensures rate limiter failures don't break login
**Test:**
```typescript
describe('[Resilience] Rate limiter failures', () => {
  it('should allow login if rate limiter fails', async () => {
    jest.spyOn(rateLimiter, 'consume')
      .mockRejectedValue(new Error('Redis down'));

    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'pass' });

    // Should fail open (allow request)
    expect(response.status).not.toBe(429);
  });
});
```

### 5. Audit Logging Failure
**File:** `src/utils/audit.ts`
**Line:** 34-36, 55
**Why:** Ensures audit log failures don't break login
**Test:**
```typescript
describe('[Resilience] Audit logging failures', () => {
  it('should complete login even if audit logging fails', async () => {
    jest.spyOn(auditLogger, 'log')
      .mockRejectedValue(new Error('Log service down'));

    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'pass' });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('token');
  });
});
```

---

**Would you like me to:**
- A) Write all HIGH priority tests (recommended)
- B) Write specific tests (specify which)
- C) Write all suggested tests
- D) Skip for now
```

---

## STEP 6: Write Missing Tests (If Requested)

### Actions
1. Create test file (if doesn't exist)
2. Add test cases to appropriate describe block
3. Run tests to verify they work
4. Update coverage report

### Add Tests

**File:** `src/__tests__/integration/auth-error-handling.test.ts`

```typescript
import { describe, it, expect, beforeAll, afterAll, jest } from '@jest/globals';
import request from 'supertest';
import app from '../../app';
import * as db from '../../config/database';
import { authService } from '../../services/auth.service';

describe('[Error Handling] Authentication Edge Cases', () => {
  beforeAll(async () => {
    await setupTestDatabase();
  });

  afterAll(async () => {
    await teardownTestDatabase();
    jest.restoreAllMocks();
  });

  describe('Database failures', () => {
    it('should return 503 when database is unavailable', async () => {
      jest.spyOn(db, 'isConnected').mockReturnValue(false);

      const response = await request(app)
        .post('/api/auth/login')
        .send({
          email: 'test@example.com',
          password: 'SecurePass123!'
        });

      expect(response.status).toBe(503);
      expect(response.body).toHaveProperty('error', 'Service unavailable');
      expect(response.body).toHaveProperty('code', 'SERVICE_UNAVAILABLE');

      jest.restoreAllMocks();
    });
  });

  describe('Unexpected errors', () => {
    it('should return 500 for unexpected service errors', async () => {
      jest.spyOn(authService, 'authenticateUser')
        .mockRejectedValue(new Error('Unexpected error'));

      const response = await request(app)
        .post('/api/auth/login')
        .send({
          email: 'test@example.com',
          password: 'SecurePass123!'
        });

      expect(response.status).toBe(500);
      expect(response.body).toHaveProperty('error', 'Internal error');
      expect(response.body).toHaveProperty('code', 'INTERNAL_ERROR');

      jest.restoreAllMocks();
    });
  });

  describe('Session expiration', () => {
    it('should reject authentication if session expired', async () => {
      // Create user with expired last login
      const user = await User.create({
        email: 'expired@example.com',
        password: await bcrypt.hash('SecurePass123!', 12),
        lastLogin: Date.now() - (MAX_SESSION_AGE + 1000) // Expired
      });

      const response = await request(app)
        .post('/api/auth/login')
        .send({
          email: 'expired@example.com',
          password: 'SecurePass123!'
        });

      expect(response.status).toBe(401);
      expect(response.body).toHaveProperty('error', 'Session expired');
      expect(response.body).toHaveProperty('code', 'SESSION_EXPIRED');
    });
  });
});
```

### Run New Tests

```bash
npm test -- auth-error-handling
```

**Expected:**
```
PASS src/__tests__/integration/auth-error-handling.test.ts
  [Error Handling] Authentication Edge Cases
    Database failures
      ✓ should return 503 when database is unavailable (85 ms)
    Unexpected errors
      ✓ should return 500 for unexpected service errors (45 ms)
    Session expiration
      ✓ should reject authentication if session expired (120 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
```

### Re-run Coverage

```bash
npm test -- --coverage
```

**New Coverage:**
```
File                 | % Stmts | % Branch | % Funcs | % Lines |
---------------------|---------|----------|---------|---------|
auth.controller.ts   |   96.15 |    93.75 |     100 |   96.15 | (was 92.31%)
auth.service.ts      |   95.24 |    91.67 |     100 |   95.24 | (was 90.48%)
rate-limit.ts        |   94.44 |      100 |     100 |   94.44 | (was 88.89%)
---------------------|---------|----------|---------|---------|
Overall              |   95.71 |    94.12 |     100 |   95.71 | (was 91.25%)
```

**Coverage improved! ✅**

---

## STEP 7: Present Summary to User

### Summary Format

```markdown
✅ Tests Executed Successfully

**Scope:** task-auth-002-login
**Duration:** 13.685 seconds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🧪 Test Results**

Test Suites: 2 passed, 2 total
Tests:       11 passed, 11 total
Duration:    13.685s

Status: ✅ ALL TESTS PASSING

**📊 Coverage Report**

Overall Coverage: 91.25%

| File                  | Stmts  | Branch | Funcs | Lines  |
|-----------------------|--------|--------|-------|--------|
| auth.controller.ts    | 92.31% | 87.50% | 100%  | 92.31% |
| auth.service.ts       | 90.48% | 83.33% | 100%  | 90.48% |
| rate-limit.ts         | 88.89% | 100%   | 100%  | 88.89% |
| jwt.ts                | 100%   | 100%   | 100%  | 100%   |
| audit.ts              | 90.00% | 80.00% | 100%  | 90.00% |

**Thresholds:**
- Statements: ✅ 91.25% (≥80% required)
- Branches:   ✅ 88.42% (≥80% required)
- Functions:  ✅ 100%   (≥80% required)
- Lines:      ✅ 91.25% (≥80% required)

**Status:** ✅ ALL THRESHOLDS MET

**🔍 Coverage Gaps Identified**

High Priority (3 gaps):
1. Database connection error handling (lines 48-50)
2. Session expiration check (lines 112-115)
3. Unexpected error catch block (line 67)

Medium Priority (2 gaps):
4. Rate limiter error handling (lines 23-25)
5. Audit logging failure handling (lines 34-36, 55)

**📝 Test Suggestions**

I can write 5 additional tests to improve coverage from 91.25% to ~96%:

1. ✅ Database failure handling (HIGH)
2. ✅ Session expiration (HIGH)
3. ✅ Unexpected error handling (HIGH)
4. Rate limiter resilience (MEDIUM)
5. Audit log resilience (MEDIUM)

Would you like me to add these tests? (Reply: yes/no/specific)

**📂 Coverage Report**

HTML Report: file:///path/to/coverage/lcov-report/index.html
LCOV File:   coverage/lcov.info (for CI/CD)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Next Steps:**
- ✅ Tests passing
- ⚠️ Consider adding 3 HIGH priority tests (optional)
- ✅ Ready for quality review: @quinn *review task-auth-002-login
```

---

## Best Practices

### 1. Run Tests Frequently

**During Development:**
```bash
# Watch mode for fast feedback
npm test -- --watch

# Run tests after each significant change
git add . && npm test && git commit
```

### 2. Prioritize Test Quality Over Coverage %

**Good:** 80% coverage with meaningful tests
**Bad:** 100% coverage with trivial tests

**Example:**
```typescript
// Bad: Trivial test for coverage
it('should export login function', () => {
  expect(typeof login).toBe('function');
});

// Good: Meaningful test
it('should return 200 with JWT for valid credentials', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'pass' });

  expect(response.status).toBe(200);
  expect(response.body).toHaveProperty('token');
});
```

### 3. Test What Matters

**Focus on:**
- Business logic
- Error handling
- Edge cases
- Security-critical code

**Don't obsess over:**
- Simple getters/setters
- Trivial utility functions
- Third-party library code

### 4. Use Meaningful Test Names

**Good:**
```typescript
it('should return 401 when password is incorrect', () => { ... });
```

**Bad:**
```typescript
it('test login', () => { ... });
```

### 5. Keep Tests Fast

**Slow tests = developers skip tests**

**Tips:**
- Mock external dependencies
- Use in-memory databases
- Parallelize test execution
- Avoid unnecessary setup/teardown

---

## Skill Metadata

```yaml
skill_name: run-tests
version: 1.0.0
subagent: james-developer
category: testing
execution_mode: sequential
halt_on_error: false

inputs:
  required:
    - scope (task_id, file_path, or --all)
  optional:
    - coverage (boolean, default: true)
    - watch (boolean, default: false)
    - suite (string: unit, integration, e2e)

outputs:
  - Test results (pass/fail counts)
  - Coverage report (text + HTML)
  - Coverage gap analysis
  - Test suggestions

execution_time: 5-60 seconds depending on test scope
```

---

*This skill is part of the BMAD Enhanced Development Suite.*
*For issues or improvements, see `.claude/skills/development/README.md`*
