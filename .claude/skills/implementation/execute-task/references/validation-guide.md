# Validation Guide

## Purpose

Run comprehensive validation, finalize documentation, and prepare task for quality review.

---

## Step 3: Final Validation and Documentation

### 1. Run Complete Test Suite

**Action:** Execute all tests to ensure nothing broke.

**Execute:**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --coverage true \
  --output json
```

**Parse Response:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 19,
    "passed_tests": 19,
    "failed_tests": 0,
    "coverage_percent": 94.2,
    "coverage_details": {
      "statements": { "percent": 94.2 },
      "branches": { "percent": 89.1 },
      "functions": { "percent": 100 },
      "lines": { "percent": 94.2 }
    },
    "duration_ms": 4200
  }
}
```

**Verify:**
- All new tests passing ✅
- All regression tests passing ✅
- Coverage meets threshold (≥80%) ✅
- No test failures or errors ✅

**If tests fail:**
```markdown
❌ Test Failures Detected

**Failed Tests:** X/Y
**Details:**
- Test: "should handle duplicate emails"
  Error: Expected 409, got 500
  File: src/services/auth/__tests__/signup.service.test.ts:45

**Action Required:**
1. Review failing tests
2. Fix implementation or test issues
3. Re-run test suite
4. Do not proceed until all tests pass
```

**Run linter:**
```bash
npm run lint
```

**Run type checker (if TypeScript):**
```bash
npm run type-check
```

---

### 2. Verify Acceptance Criteria

**Action:** Map each AC to implementation and tests.

**Review Each AC:**

**AC1: User can signup with valid email/password**
- Implementation: ✅ src/services/auth/signup.service.ts
- Tests: ✅ 5 integration tests cover signup flow
- Edge cases: ✅ Valid/invalid emails, passwords tested

**AC2: Password security requirements enforced**
- Implementation: ✅ src/schemas/user.schema.ts (Zod validation)
- Tests: ✅ 8 unit tests verify password rules
- Security: ✅ bcrypt hashing with cost 12

**AC3: Duplicate emails prevented**
- Implementation: ✅ Unique constraint in database + service check
- Tests: ✅ 2 integration tests verify duplicate prevention
- Error handling: ✅ Returns 409 Conflict

**AC4: Confirmation email sent**
- Implementation: ✅ Email service integration
- Tests: ✅ 2 integration tests verify email sending
- Mock: ✅ Email service mocked in tests

**Result:**
```markdown
✅ All Acceptance Criteria Verified

- ✓ AC1: User signup implemented and tested
- ✓ AC2: Password security enforced and tested
- ✓ AC3: Duplicate prevention implemented and tested
- ✓ AC4: Email confirmation implemented and tested

**Coverage:** 4/4 ACs (100%)
```

---

### 3. Verify All Checkboxes Marked

**Action:** Scan task spec for any unchecked boxes.

**Scan Task File:**
```bash
grep "- \[ \]" .claude/tasks/task-006-user-signup.md
```

**If any unchecked boxes found:**
```markdown
⚠️ Incomplete Tasks Detected

**Unchecked Items:**
- Task 3, Subtask 3.4: Write E2E tests

**Action Required:**
- Complete remaining subtasks
- Mark checkboxes only when validated
- Re-run final validation when complete
```

**If all boxes checked:**
```markdown
✅ All Tasks Complete

- ✓ Task 1: Create user model (5 subtasks)
- ✓ Task 2: Implement signup service (4 subtasks)
- ✓ Task 3: Create API endpoint (5 subtasks)
- ✓ Task 4: Add email verification (3 subtasks)
- ✓ Task 5: Write comprehensive tests (3 subtasks)

**Total:** 5 tasks, 20 subtasks, all complete
```

---

### 4. Update Implementation Record

**Action:** Finalize documentation in task file.

#### a. Agent Model Used

```markdown
### Agent Model Used

claude-sonnet-4-5-20250929
```

#### b. Debug Log References (if applicable)

```markdown
### Debug Log References

**Issues Encountered:**
1. Unicode email validation edge case (line 234)
   - Resolution: Added punycode encoding check
   - Time spent: 15 minutes

2. bcrypt async timeout in tests (line 567)
   - Resolution: Increased test timeout to 10s
   - Time spent: 5 minutes
```

#### c. Completion Notes

```markdown
### Completion Notes

**Task 1: Create User Model**
- Implemented User interface with all required fields
- Created Zod schema with comprehensive validation
- Database migration with proper constraints
- 12 unit tests, all passing (94% coverage)
- Discovered unicode email edge case, added handling

**Task 2: Implement Signup Service**
- Service with bcrypt password hashing (cost 12)
- Duplicate email check before insertion
- Transaction support for data consistency
- 8 unit tests, all passing
- Reused auth patterns from task-003

**Task 3: Create API Endpoint**
- POST /api/auth/signup endpoint
- Request validation middleware
- Error handling for all cases (400, 409, 500)
- 5 integration tests, all passing
- Response time <150ms

**Task 4: Add Email Verification**
- Email service integration
- Confirmation email template
- Token generation for email verification link
- 2 integration tests with mocked email service

**Task 5: Comprehensive Tests**
- 2 E2E tests for complete signup flow
- Total: 27 tests, all passing
- Coverage: 94% statements, 89% branches
- All regression tests passing (47 existing tests)

**Key Learnings:**
- bcrypt cost 12 adds ~150ms latency, acceptable for auth endpoints
- Unicode emails require punycode encoding check
- Email service mock pattern works well for testing
- Transaction support critical for signup (user + email in one transaction)

**Deviations from Spec:**
- Added punycode encoding for unicode emails (not in original spec)
  Reason: Discovered during testing, prevents validation bypass
  Impact: +5ms validation time, no breaking changes
```

#### d. Files Modified

```markdown
### Files Modified

**Created:**
- src/types/user.ts (interface definition)
- src/schemas/user.schema.ts (Zod validation)
- src/services/auth/signup.service.ts (signup logic)
- src/routes/auth/signup.ts (API endpoint)
- src/templates/email/confirmation.html (email template)
- migrations/001_create_users.sql (database migration)
- src/schemas/__tests__/user.schema.test.ts (12 tests)
- src/services/auth/__tests__/signup.service.test.ts (8 tests)
- src/routes/auth/__tests__/signup.integration.test.ts (5 tests)
- tests/e2e/auth/signup.e2e.test.ts (2 tests)

**Modified:**
- src/routes/auth/index.ts (added signup route import/export)
- src/services/email/index.ts (added confirmation template)
- README.md (updated API documentation for POST /api/auth/signup)
- package.json (added bcrypt dependency)
```

#### e. Testing Results

```markdown
### Testing Results

**Unit Tests:**
- File: src/schemas/__tests__/user.schema.test.ts
  Tests: 12 passed, 0 failed
  Coverage: 94% statements, 89% branches, 100% functions

- File: src/services/auth/__tests__/signup.service.test.ts
  Tests: 8 passed, 0 failed
  Coverage: 92% statements, 85% branches, 100% functions

**Integration Tests:**
- File: src/routes/auth/__tests__/signup.integration.test.ts
  Tests: 5 passed, 0 failed
  Coverage: API endpoints verified

**E2E Tests:**
- File: tests/e2e/auth/signup.e2e.test.ts
  Tests: 2 passed, 0 failed
  Coverage: Complete signup flow validated

**Regression Tests:**
- Existing tests: 47 total, 47 passed, 0 failed
- No breaking changes introduced

**Total Execution Time:** 4.2s
**Overall Coverage:** 94.2% statements, 89.1% branches, 100% functions, 94.2% lines

**Status:** ✅ ALL TESTS PASSING
```

---

### 5. Update Task Status to "Review"

**Action:** Mark task ready for quality review.

**Edit Task File:**
- Locate "## Status" section
- Change status from "InProgress" to "Review"
- DO NOT mark as "Done" (quality skill does that)

**Example:**
```markdown
## Status

Review

## Implementation Record

**Started:** 2025-10-29 11:30 AM
**Completed:** 2025-10-29 2:45 PM
**Duration:** 3 hours 15 minutes
**Agent:** Claude Code (execute-task skill)
```

---

### 6. Present Completion Summary

**Format:**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Implementation Complete - Ready for Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Task:** User Signup Implementation
**File:** .claude/tasks/task-006-user-signup.md
**Status:** Review (ready for quality assessment)
**Duration:** 3 hours 15 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### What Was Implemented

✓ User data model with comprehensive validation
✓ Signup service with secure password hashing (bcrypt cost 12)
✓ API endpoint POST /api/auth/signup with full error handling
✓ Email verification with confirmation template
✓ Comprehensive test suite (27 tests total)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### All Acceptance Criteria Met

✓ AC1: User can signup with valid email/password
✓ AC2: Password security requirements enforced
✓ AC3: Duplicate emails prevented with unique constraint
✓ AC4: Confirmation email sent via email service

**Coverage:** 4/4 ACs (100%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Test Results

✓ Unit Tests: 20 tests, 20 passed, 0 failed
✓ Integration Tests: 5 tests, 5 passed, 0 failed
✓ E2E Tests: 2 tests, 2 passed, 0 failed
✓ Regression Tests: 47 tests, 47 passed, 0 failed

**Total:** 27 new tests, all passing
**Coverage:** 94.2% statements, 89.1% branches, 100% functions
**Linter:** No issues
**Type Check:** All types valid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Files

**Created:** 10 new files
- 4 implementation files
- 1 database migration
- 4 test files
- 1 email template

**Modified:** 4 existing files
- Routes index
- Email service
- README
- package.json

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Key Learnings

- Unicode email handling added (edge case discovered)
- bcrypt cost 12 performance acceptable (~150ms)
- Email service mock pattern effective for testing
- Transaction support critical for data consistency

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Next Steps

1. **Option A:** Run quality review skill for systematic assessment
   Command: Use quality review skill with task file

2. **Option B:** Manual review and approve
   - Review implementation if desired
   - Mark task as "Done" when satisfied

3. **Option C:** Request changes
   - Update task spec with change requests
   - Re-run execute-task skill

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Quality review needed? (yes/no)**
```

---

## Halt Conditions

**Must halt if:**

1. **Test Failures**
   - Any tests failing
   - Action: Fix issues, re-run

2. **Acceptance Criteria Not Met**
   - One or more ACs unverified
   - Action: Complete missing work

3. **Unchecked Tasks**
   - Tasks/subtasks not marked complete
   - Action: Complete remaining work

4. **Coverage Below Threshold**
   - Coverage <80%
   - Action: Add tests for uncovered code

---

## Quick Reference

**Validation Checklist:**
- [ ] All tests passing
- [ ] All ACs verified
- [ ] All checkboxes marked
- [ ] Implementation Record complete
- [ ] Status updated to "Review"
- [ ] Completion summary presented

**Output Status:**
- Tests: All passing
- ACs: All verified
- Tasks: All complete
- Status: Review

---

*Part of execute-task skill - Implementation Suite*
