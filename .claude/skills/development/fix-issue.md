# Fix Issue Skill

## Purpose
Debug and fix bugs, issues, or failing tests. This skill reproduces issues, identifies root causes, implements fixes, and validates that the fix works without introducing regressions.

## When to Use This Skill
- Fixing bugs reported by users or QA
- Debugging failing tests
- Addressing issues found in code review
- Fixing regressions introduced by recent changes
- Resolving production incidents
- Debugging integration or E2E test failures

## Invocation
```bash
# Fix a described issue
@james *fix "Login fails when email contains + symbol"

# Fix an issue in a specific task
@james *fix task-auth-002 --issue "Rate limiting not working"

# Debug failing test
@james *debug "Test failing: should return 401 for invalid password"

# Fix from quality review feedback
@james *fix task-auth-002 --feedback quinn

# With reproduction steps
@james *fix "Checkout fails" --reproduce "1. Add item to cart, 2. Click checkout, 3. Error 500"
```

## Prerequisites
- Clear description of the issue
- Ability to reproduce the issue (or failing test)
- Access to relevant code and logs
- Test framework configured

## Skill Configuration
```yaml
skill_name: fix-issue
version: 1.0.0
subagent: james-developer
execution_mode: sequential
halt_on_error: false
output_directory: (project root)
```

---

## STEP 0: Load Context and Understand Issue

### Actions
1. Parse issue description
2. Identify affected component/feature
3. Load related task or story (if applicable)
4. Check recent commits (if regression)
5. Review error logs or stack traces

### Issue Description Analysis

**Extract:**
- **What:** What is broken?
- **When:** When does it happen? (always, sometimes, specific condition)
- **Where:** Which component/file/endpoint?
- **Expected:** What should happen?
- **Actual:** What actually happens?
- **Impact:** How severe? (critical, high, medium, low)

**Example:**

```
Issue: "Login fails when email contains + symbol"

Analysis:
- What: Login endpoint rejects valid emails with + symbol
- When: Always happens for emails like "user+tag@example.com"
- Where: POST /api/auth/login endpoint
- Expected: Email accepted, user logged in
- Actual: Returns 400 "Invalid email format"
- Impact: Medium (blocks some users, workaround exists)
```

### Load Related Context

**If task ID provided:**
```markdown
Task: task-auth-002-login
Status: Review (implemented, in QA)
Implemented: 2025-01-15
Issue: Found during quality review by Quinn

Related Files:
- src/controllers/auth.controller.ts
- src/services/auth.service.ts
- src/utils/validation.ts
```

**If no task ID:**
```markdown
Search for related code:
- Grep for "login" in controllers
- Check recent commits to auth files
- Review error logs for stack trace
```

---

## STEP 1: Reproduce the Issue

### Actions
1. Create a failing test that demonstrates the bug
2. Run the test (verify it fails)
3. Confirm the failure matches the issue description
4. Document reproduction steps

### Write Failing Test

**Purpose:** Create evidence that the bug exists

**Example for Email Issue:**

```typescript
// src/__tests__/integration/auth.integration.test.ts

describe('[Bug Fix] Login with + symbol in email', () => {
  it('should accept email addresses with + symbol', async () => {
    // Setup: Create user with + in email
    await User.create({
      email: 'user+tag@example.com',
      password: await bcrypt.hash('SecurePass123!', 12)
    });

    // Attempt login
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'user+tag@example.com',
        password: 'SecurePass123!'
      });

    // Expected: Login succeeds
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('token');
  });
});
```

### Run Test

```bash
npm test -- --testNamePattern="Login with \\+ symbol in email"
```

**Expected Output:**
```
FAIL src/__tests__/integration/auth.integration.test.ts
  ✕ should accept email addresses with + symbol (125 ms)

  ● [Bug Fix] Login with + symbol in email › should accept email addresses with + symbol

    expect(received).toBe(expected) // Object.is equality

    Expected: 200
    Received: 400

      52 |     // Expected: Login succeeds
      53 |     expect(response.status).toBe(200);
    > 54 |     expect(response.body).toHaveProperty('token');
         |                          ^
      55 |   });

    at Object.<anonymous> (src/__tests__/integration/auth.integration.test.ts:54:26)
```

**Bug reproduced! ✅**

---

## STEP 2: Identify Root Cause

### Actions
1. Trace execution path
2. Add debug logging if needed
3. Check relevant code
4. Identify the exact line/logic causing the issue
5. Understand why it's wrong

### Trace Execution Path

**For HTTP request issues:**
```
Request → Middleware → Controller → Service → Database
           ↑ Check each step
```

**For email validation issue:**
```
POST /api/auth/login
  ↓
auth.controller.ts:login()
  ↓
loginSchema.safeParse(req.body)  ← Check validation
  ↓
z.string().email()
  ↓
(uses internal email regex)
```

### Add Debug Logging

```typescript
// Temporarily add logging
export const login = async (req: Request, res: Response): Promise<Response> => {
  console.log('Login attempt:', req.body);

  const validationResult = loginSchema.safeParse(req.body);
  console.log('Validation result:', validationResult);

  if (!validationResult.success) {
    console.log('Validation errors:', validationResult.error);
    return res.status(400).json({
      error: validationResult.error.errors[0].message,
      code: 'VALIDATION_ERROR'
    });
  }

  // ... rest of code
};
```

### Run with Debug Logging

```bash
npm test -- --testNamePattern="Login with \\+ symbol"
```

**Output:**
```
console.log
  Login attempt: { email: 'user+tag@example.com', password: 'SecurePass123!' }

console.log
  Validation result: {
    success: false,
    error: ZodError: [
      {
        validation: "email",
        code: "invalid_string",
        message: "Invalid email",
        path: [ "email" ]
      }
    ]
  }
```

### Identify Root Cause

```
Root Cause Found:
- Location: src/schemas/auth.schema.ts:5
- Issue: z.string().email() uses internal regex that doesn't allow + symbol
- Code: z.string().email('Invalid email format')

Current regex (Zod internal):
/^[^\s@]+@[^\s@]+\.[^\s@]+$/

Problem: This simple regex is RFC 5322 compliant for basic cases,
but Zod's email() validator may be too strict.

Solution: Use custom regex or adjust validation
```

### Documented Root Cause

```markdown
**Root Cause Analysis:**

**Location:** `src/schemas/auth.schema.ts:5`

**Issue:** Zod's built-in `email()` validator rejects valid email addresses containing + symbol

**Why it's wrong:** RFC 5322 allows + in the local part of email addresses (before @).
Emails like "user+tag@example.com" are valid and commonly used for email filtering.

**Impact:** Users with + in their email cannot log in

**Evidence:**
- Test fails with 400 "Invalid email" for "user+tag@example.com"
- Validation error shows email rejected by Zod validator
- RFC 5322 allows + in local part

**Fix Strategy:** Use custom regex that allows + symbol
```

---

## STEP 3: Implement Fix

### Actions
1. Make minimal code change to fix the issue
2. Don't over-engineer or refactor unrelated code
3. Keep the fix focused and simple
4. Add comments explaining the fix

### Implement Fix

**File:** `src/schemas/auth.schema.ts`

**Before:**
```typescript
import { z } from 'zod';

export const loginSchema = z.object({
  email: z.string().email('Invalid email format'),
  password: z.string().min(1, 'Password is required'),
});
```

**After:**
```typescript
import { z } from 'zod';

// Custom email regex that allows + symbol (RFC 5322 compliant)
// Allows: user@example.com, user+tag@example.com, first.last@example.com
const EMAIL_REGEX = /^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

export const loginSchema = z.object({
  email: z.string().regex(EMAIL_REGEX, 'Invalid email format'),
  password: z.string().min(1, 'Password is required'),
});
```

**Change Summary:**
- Replaced `z.string().email()` with custom regex
- Regex explicitly includes + in allowed characters
- Added comment explaining why custom regex is needed

---

## STEP 4: Validate Fix

### Actions
1. Run the failing test (should now pass)
2. Run all related tests (no regressions)
3. Run full test suite (no unexpected failures)
4. Manual testing (if applicable)

### Run Failing Test

```bash
npm test -- --testNamePattern="Login with \\+ symbol"
```

**Expected Output:**
```
PASS src/__tests__/integration/auth.integration.test.ts
  ✓ should accept email addresses with + symbol (95 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

**Fix validated! ✅**

### Run All Auth Tests

```bash
npm test auth
```

**Check for regressions:**
```
PASS src/__tests__/services/auth.service.test.ts
PASS src/__tests__/integration/auth.integration.test.ts
  ✓ should return 200 and JWT token for valid credentials
  ✓ should return 401 for wrong password
  ✓ should return 401 for non-existent email
  ✓ should return 400 for missing email
  ✓ should return 400 for missing password
  ✓ should return 400 for invalid email format
  ✓ should return 429 after 5 failed attempts
  ✓ should accept email addresses with + symbol (NEW)

Test Suites: 2 passed, 2 total
Tests:       13 passed, 13 total (was 12, now 13)
```

**No regressions! All existing tests still pass! ✅**

### Run Full Test Suite

```bash
npm test
```

**Expected:**
```
Test Suites: 15 passed, 15 total
Tests:       142 passed, 142 total
```

**No unexpected failures! ✅**

---

## STEP 5: Add Edge Case Tests

### Actions
1. Consider related edge cases
2. Write tests for edge cases
3. Verify current fix handles them
4. If not, extend fix

### Identify Edge Cases

**For email validation fix:**
```markdown
Related edge cases to test:
1. Email with multiple + symbols (user+tag+more@example.com)
2. Email with . before @ (first.last@example.com)
3. Email with - in domain (user@my-domain.com)
4. Email with numbers (user123@domain.com)
5. Email with % symbol (user%test@domain.com)
6. Email with underscore (user_test@domain.com)
```

### Write Edge Case Tests

```typescript
describe('[Bug Fix] Email validation edge cases', () => {
  it('should accept email with multiple + symbols', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'user+tag+more@example.com',
        password: 'SecurePass123!'
      });

    expect(response.status).not.toBe(400);
  });

  it('should accept email with dots in local part', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'first.last@example.com',
        password: 'SecurePass123!'
      });

    expect(response.status).not.toBe(400);
  });

  it('should accept email with hyphen in domain', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'user@my-domain.com',
        password: 'SecurePass123!'
      });

    expect(response.status).not.toBe(400);
  });

  it('should reject email without @ symbol', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'notanemail.com',
        password: 'SecurePass123!'
      });

    expect(response.status).toBe(400);
  });

  it('should reject email without domain extension', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'user@domain',
        password: 'SecurePass123!'
      });

    expect(response.status).toBe(400);
  });
});
```

### Run Edge Case Tests

```bash
npm test -- --testNamePattern="Email validation edge cases"
```

**Expected:**
```
PASS src/__tests__/integration/auth.integration.test.ts
  ✓ should accept email with multiple + symbols
  ✓ should accept email with dots in local part
  ✓ should accept email with hyphen in domain
  ✓ should reject email without @ symbol
  ✓ should reject email without domain extension

Tests: 5 passed, 5 total
```

**All edge cases handled! ✅**

---

## STEP 6: Clean Up Debug Code

### Actions
1. Remove debug logging
2. Remove commented code
3. Keep the fix and new tests
4. Ensure code is clean

### Remove Debug Logging

**File:** `src/controllers/auth.controller.ts`

**Remove:**
```typescript
console.log('Login attempt:', req.body);
console.log('Validation result:', validationResult);
console.log('Validation errors:', validationResult.error);
```

**Keep:**
```typescript
export const login = async (req: Request, res: Response): Promise<Response> => {
  try {
    const validationResult = loginSchema.safeParse(req.body);
    if (!validationResult.success) {
      return res.status(400).json({
        error: validationResult.error.errors[0].message,
        code: 'VALIDATION_ERROR'
      });
    }
    // ... rest of code
  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });
  }
};
```

---

## STEP 7: Document Fix

### Actions
1. Update task file (if applicable)
2. Add fix documentation
3. Commit with clear message
4. Update changelog (if exists)

### Update Task File

**File:** `.claude/tasks/task-auth-002-login.md`

**Add to Bug Fixes section:**

```markdown
## Bug Fixes

### Fix 1: Email validation rejects + symbol

**Date:** 2025-01-15
**Fixed By:** James (Developer)
**Issue:** Login fails when email contains + symbol
**Root Cause:** Zod's built-in email() validator too strict
**Severity:** Medium

**Changes:**
- `src/schemas/auth.schema.ts`: Replaced Zod email() with custom RFC 5322-compliant regex
- Added test: "should accept email addresses with + symbol"
- Added 5 edge case tests for email validation

**Impact:**
- Users with + in email can now log in
- No regressions to existing functionality
- Better RFC 5322 compliance

**Tests:**
- ✅ Bug test passes
- ✅ All existing tests pass (no regressions)
- ✅ Edge case tests pass

**Files Changed:**
- `src/schemas/auth.schema.ts` (3 lines modified)
- `src/__tests__/integration/auth.integration.test.ts` (60 lines added)
```

### Commit Changes

```bash
git add .
git commit -m "fix: allow + symbol in email addresses

- Replaced Zod email() with RFC 5322-compliant regex
- Added test for + symbol in email
- Added edge case tests for email validation

Fixes: Email validation incorrectly rejected valid emails with + symbol
Impact: Users with + in email can now log in
Tests: 6 new tests, all passing, no regressions"
```

---

## STEP 8: Present Summary to User

### Summary Format

```markdown
✅ Bug Fixed: Email validation rejects + symbol

**Issue:** Login fails when email contains + symbol
**Severity:** Medium
**Time to Fix:** 12 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🐛 Root Cause**

Location: `src/schemas/auth.schema.ts:5`
Issue: Zod's built-in email() validator rejected valid emails with + symbol
Why: Regex too strict, doesn't follow RFC 5322 completely

**🔧 Fix Applied**

Changed:
```diff
- email: z.string().email('Invalid email format'),
+ email: z.string().regex(EMAIL_REGEX, 'Invalid email format'),
```

Added RFC 5322-compliant regex:
```typescript
const EMAIL_REGEX = /^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
```

**✅ Validation**

Reproduction Test: ✅ Now passes
Existing Tests: ✅ All pass (no regressions)
Edge Cases: ✅ 5 additional tests added, all pass

Test Results:
```
PASS src/__tests__/integration/auth.integration.test.ts
  ✓ should accept email addresses with + symbol (NEW)
  ✓ should accept email with multiple + symbols (NEW)
  ✓ should accept email with dots in local part (NEW)
  ✓ should accept email with hyphen in domain (NEW)
  ✓ should reject email without @ symbol (NEW)
  ✓ should reject email without domain extension (NEW)
  ✓ should return 200 and JWT token for valid credentials
  ✓ should return 401 for wrong password
  ... (all other tests still pass)

Tests: 18 passed, 18 total (was 12, added 6)
```

**📁 Files Changed**

Modified:
- `src/schemas/auth.schema.ts` (+3 lines)

Added Tests:
- `src/__tests__/integration/auth.integration.test.ts` (+60 lines, 6 tests)

**📝 Impact**

✅ Users with + in email can now log in
✅ Better RFC 5322 compliance
✅ No regressions to existing functionality
✅ Edge cases covered

**🎯 Status**

Committed: `fix: allow + symbol in email addresses`
Task Updated: `.claude/tasks/task-auth-002-login.md`
Ready for: Re-review by Quinn (if was in review)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Common Issue Patterns

### Pattern 1: Validation Too Strict

**Symptoms:**
- Valid input rejected
- Error message: "Invalid [field]"

**Debug Steps:**
1. Check validation schema/regex
2. Test with various valid inputs
3. Check against spec (RFC, standard)

**Fix:**
- Relax validation to match spec
- Add tests for edge cases

---

### Pattern 2: Missing Error Handling

**Symptoms:**
- Uncaught exception
- 500 Internal Server Error
- No error message

**Debug Steps:**
1. Check stack trace
2. Identify missing try-catch
3. Check for unhandled promise rejections

**Fix:**
- Add try-catch blocks
- Handle expected errors explicitly
- Add appropriate HTTP status codes

**Example:**
```typescript
// Before (no error handling)
export const getUser = async (req, res) => {
  const user = await User.findById(req.params.id);
  return res.json(user);
};

// After (with error handling)
export const getUser = async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) {
      return res.status(404).json({
        error: 'User not found',
        code: 'USER_NOT_FOUND'
      });
    }
    return res.json(user);
  } catch (error) {
    console.error('Error fetching user:', error);
    return res.status(500).json({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });
  }
};
```

---

### Pattern 3: Race Condition

**Symptoms:**
- Works sometimes, fails sometimes
- Flaky tests
- Inconsistent behavior

**Debug Steps:**
1. Add logging with timestamps
2. Check for concurrent operations
3. Identify shared state
4. Check for proper locking/transactions

**Fix:**
- Add database transactions
- Use proper locking mechanisms
- Make operations atomic
- Add rate limiting if needed

---

### Pattern 4: Memory Leak

**Symptoms:**
- Performance degrades over time
- Memory usage increases
- Application crashes after running for a while

**Debug Steps:**
1. Profile memory usage
2. Check for event listener leaks
3. Check for unclosed connections
4. Check for large data structures not being garbage collected

**Fix:**
- Remove event listeners when done
- Close database connections
- Clear caches periodically
- Use weak references where appropriate

---

### Pattern 5: Wrong Assumptions

**Symptoms:**
- Works in development, fails in production
- Works for some users, not others
- Works on some data, not others

**Debug Steps:**
1. Check environment differences
2. Check data differences
3. Check assumptions in code
4. Add assertions

**Fix:**
- Validate assumptions with tests
- Handle null/undefined explicitly
- Check data format before processing
- Add input validation

---

## Error Handling

### Cannot Reproduce Issue

```
⚠️ Cannot Reproduce: Email validation issue

Issue: "Login fails when email contains + symbol"
Status: Unable to reproduce

Attempts Made:
1. ✅ Created test with "user+tag@example.com"
2. ✅ Ran test - test PASSES (issue doesn't occur)
3. ✅ Manual test - login succeeds
4. ✅ Checked validation code - allows + symbol

Possible Reasons:
1. Issue already fixed in current codebase
2. Issue description inaccurate
3. Issue occurs only in specific environment (production?)
4. Issue requires specific data or state

Questions for Reporter:
1. What exact email address failed?
2. What was the exact error message?
3. Which environment? (dev, staging, production)
4. Can you provide request/response logs?
5. Is this still happening?

Action: Waiting for more information
```

### Fix Introduces Regression

```
❌ Fix Failed: Regression Detected

Issue: Email validation rejects + symbol
Fix Applied: Custom regex allowing + symbol
Status: Fix works, but broke existing tests

Test Failures:
✓ Bug test passes (+ symbol now works)
✗ "should reject invalid email" - NOW PASSES (should fail)
✗ "should reject email without domain" - NOW PASSES (should fail)

Root Cause of Regression:
New regex TOO permissive:
/^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/

Accepts invalid emails:
- "user@" (no domain)
- "@example.com" (no local part)

Fix for the Fix:
Make regex more strict while still allowing +:
/^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/
 ^must have 1+ chars  ^must have 1+ chars  ^must have 2+ chars

Updated regex:
/^[A-Za-z0-9._+%-]{1,}@[A-Za-z0-9.-]{1,}\.[A-Za-z]{2,}$/

Status: Fixing regression, will retest
```

---

## Best Practices

### 1. Always Write Failing Test First

Before fixing, create a test that demonstrates the bug. This:
- Proves the bug exists
- Prevents regressions
- Verifies the fix works

### 2. Make Minimal Changes

Don't refactor or "improve" unrelated code while fixing a bug. Keep the fix focused and simple.

### 3. Check for Regressions

Always run the full test suite after a fix. Ensure no existing tests break.

### 4. Document Root Cause

Explain why the bug happened, not just what you changed. This helps prevent similar bugs.

### 5. Add Edge Case Tests

Think about related edge cases and test them. One bug often indicates others nearby.

---

## Skill Metadata

```yaml
skill_name: fix-issue
version: 1.0.0
subagent: james-developer
category: debugging
execution_mode: sequential
halt_on_error: false

inputs:
  required:
    - issue_description
  optional:
    - task_id
    - reproduce_steps
    - feedback_source

outputs:
  - Fix code (modified files)
  - Test for the bug
  - Edge case tests
  - Updated task file with bug fix documentation

execution_time: 10-30 minutes per bug
```

---

*This skill is part of the BMAD Enhanced Development Suite.*
*For issues or improvements, see `.claude/skills/development/README.md`*
