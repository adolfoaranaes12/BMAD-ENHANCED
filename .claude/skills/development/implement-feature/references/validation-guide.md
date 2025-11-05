# Validation Guide

## Purpose

Complete validation procedures for TDD implementation before marking feature complete.

---

## Step 1: Run All Tests

### Using bmad-commands

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --output json
```

### Parse Response

```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "coverage_percent": 87,
    "duration_ms": 2456
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest",
    "duration_ms": 2500
  },
  "errors": []
}
```

### Verification Checklist

- [ ] `outputs.passed == true`
- [ ] `outputs.failed_tests == 0`
- [ ] `outputs.coverage_percent >= 80`
- [ ] `outputs.total_tests >= expected_count`
- [ ] No flaky tests (run multiple times to verify)

---

## Step 2: Check Test Coverage

### Coverage Thresholds

| Metric | Minimum | Target | Excellent |
|--------|---------|--------|-----------|
| Statements | 80% | 85% | 90%+ |
| Branches | 75% | 80% | 85%+ |
| Functions | 85% | 90% | 95%+ |
| Lines | 80% | 85% | 90%+ |

### Parse Coverage from Output

```typescript
const { coverage_percent } = outputs;

if (coverage_percent < 80) {
  console.error(`Coverage ${coverage_percent}% below threshold 80%`);
  // Add more tests
}
```

### Coverage Report Example

```
File                     | % Stmts | % Branch | % Funcs | % Lines |
-------------------------|---------|----------|---------|---------|
auth.controller.ts       |   92.31 |    87.50 |     100 |   92.31 |
auth.service.ts          |   90.48 |    83.33 |     100 |   90.48 |
rate-limit.ts            |   88.89 |      100 |     100 |   88.89 |
jwt.ts                   |     100 |      100 |     100 |     100 |
-------------------------|---------|----------|---------|---------|
Overall                  |   91.25 |    88.42 |     100 |   91.25 |
```

---

## Step 3: Check for Syntax Errors

### TypeScript Type Check

```bash
npm run type-check
# or
tsc --noEmit
```

### Expected Output

```
✓ No type errors found
```

### If Errors Found

```
src/auth/login.ts:45:12 - error TS2339: Property 'emaill' does not exist on type 'User'.

45   return user.emaill;
              ~~~~~~

Found 1 error.
```

**Action:** Fix type errors and re-run validation.

---

## Step 4: Run Linter

### ESLint Check

```bash
npm run lint
```

### Expected Output

```
✓ No linting errors found
```

### Auto-Fix Minor Issues

```bash
npm run lint -- --fix
```

---

## Step 5: Verify Acceptance Criteria

### Checklist Verification

For each acceptance criterion from task spec:

```markdown
## Acceptance Criteria Coverage

- ✅ AC-1: User can submit email/password to POST /api/auth/login
  - Test: `should accept POST request with email and password`
  - Status: Passing

- ✅ AC-2: Valid credentials return 200 with JWT token
  - Test: `should return 200 and JWT token for valid credentials`
  - Status: Passing

- ✅ AC-3: Invalid credentials return 401
  - Test: `should return 401 for wrong password`
  - Test: `should return 401 for non-existent email`
  - Status: Passing

- ✅ AC-4: Missing fields return 400
  - Test: `should return 400 for missing email`
  - Test: `should return 400 for missing password`
  - Status: Passing

- ✅ AC-5: Rate limiting (5 attempts per 10 min)
  - Test: `should return 429 after 5 failed attempts`
  - Status: Passing

- ✅ AC-6: JWT expires after 24 hours
  - Test: `should generate token with 24-hour expiration`
  - Status: Passing

- ✅ AC-7: Login attempts logged
  - Test: `should log successful login attempt`
  - Test: `should log failed login attempt`
  - Status: Passing

**All acceptance criteria met: 7/7**
```

---

## Step 6: Manual Code Review

### Self-Review Checklist

**Code Quality:**
- [ ] No console.log() statements left in code
- [ ] No TODO comments without issues created
- [ ] No commented-out code blocks
- [ ] No debug statements
- [ ] Proper error handling
- [ ] Consistent naming conventions
- [ ] Appropriate access modifiers (public/private)

**Security:**
- [ ] No hardcoded secrets or API keys
- [ ] Passwords never logged
- [ ] User input properly validated
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF tokens used (if applicable)

**Performance:**
- [ ] No N+1 query problems
- [ ] Proper indexing on database queries
- [ ] No unnecessary loops
- [ ] Caching used appropriately
- [ ] No memory leaks (event listeners cleaned up)

**Maintainability:**
- [ ] Clear function/variable names
- [ ] Functions < 50 lines (ideally < 20)
- [ ] Single Responsibility Principle followed
- [ ] DRY principle followed (no duplication)
- [ ] Proper error messages
- [ ] Inline comments for complex logic only

---

## Step 7: Verify Files Created/Modified

### Expected Files Checklist

```markdown
**Files Created:**
- [ ] src/controllers/auth.controller.ts
- [ ] src/services/auth.service.ts
- [ ] src/middleware/rate-limit.ts
- [ ] src/utils/jwt.ts
- [ ] src/schemas/auth.schema.ts
- [ ] src/__tests__/services/auth.service.test.ts
- [ ] src/__tests__/integration/auth.integration.test.ts

**Files Modified:**
- [ ] src/routes/auth.routes.ts (added login route)
- [ ] src/app.ts (registered auth routes)
```

### Verify with Git

```bash
git status
git diff --stat
```

---

## Validation Summary Template

```markdown
## Implementation Validation Summary

**Task:** {task-id}
**Date:** {date}

### Test Results
✅ Tests Passing: {passed}/{total}
✅ Coverage: {coverage}% (threshold: 80%)
✅ No Syntax Errors
✅ No Linting Errors

### Acceptance Criteria
✅ All {n} acceptance criteria met
✅ All test cases passing

### Code Quality
✅ Self-review complete
✅ Security checks passed
✅ No known performance issues

### Files
✅ {n} files created
✅ {n} files modified
✅ All changes tracked in git

**Status:** Ready for Quality Review
**Next Step:** @quinn *review {task-id}
```

---

*Part of implement-feature skill - Development Suite*
