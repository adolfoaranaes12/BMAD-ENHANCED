# Implementation Templates

This file contains standard templates and formats for the implement-feature skill.

---

## Task Specification Format

When loading task specifications in Step 0, expect this format:

### Required Task Spec Structure

```markdown
# Task: [Task ID] - [Task Title]

## Objective

[Clear, concise description of what to build]

## Acceptance Criteria

1. **AC-1**: [Testable requirement with specific, measurable outcome]
2. **AC-2**: [Testable requirement with specific, measurable outcome]
3. **AC-3**: [Testable requirement with specific, measurable outcome]

## Context

**Technology Stack:**
- Language: [TypeScript/Python/etc.]
- Framework: [Express/FastAPI/etc.]
- Database: [PostgreSQL/MongoDB/etc.]
- Testing: [Jest/Pytest/etc.]

**Data Models:**
```typescript
// User model
interface User {
  id: string;
  email: string;
  passwordHash: string;
  createdAt: Date;
}
```

**API Specification:**

### POST /api/auth/signup

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (201):**
```json
{
  "token": "jwt.token.here",
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

**Response (400):**
```json
{
  "error": "Invalid email format"
}
```

**Response (409):**
```json
{
  "error": "Email already exists"
}
```

## Tasks

1. Create user signup form validation schema
2. Implement password hashing with bcrypt
3. Create user signup controller
4. Add POST /api/auth/signup route
5. Write unit tests for validation
6. Write integration tests for signup flow
7. Update API documentation

## Dependencies

- Requires: `task-auth-001-user-model` (User database model)
- Blocks: `task-auth-003-login` (Login functionality)

## Assumptions

- User model already exists with email and passwordHash fields
- JWT token generation utility already implemented
- PostgreSQL database configured

## Notes

- Use bcrypt cost factor of 12 for password hashing
- Email validation should follow RFC 5322 standard
- JWT tokens should expire in 24 hours
```

---

## Output Format

When completing implementation, return this structured output:

### Success Output

```json
{
  "implementation_complete": true,
  "test_coverage_percent": 87,
  "files_modified": [
    "src/auth/signup.controller.ts",
    "src/schemas/auth.schema.ts",
    "src/routes/auth.routes.ts",
    "tests/unit/auth/signup.test.ts",
    "tests/integration/auth/signup.integration.test.ts"
  ],
  "tests_passed": true,
  "telemetry": {
    "skill": "implement-feature",
    "task_id": "task-auth-002-signup",
    "duration_ms": 45000,
    "files_modified_count": 5,
    "tests_total": 12,
    "tests_passed": 12,
    "tests_failed": 0,
    "coverage_percent": 87,
    "timestamp": "2025-01-15T14:30:00Z"
  }
}
```

### Error Output

```json
{
  "implementation_complete": false,
  "error": "Task specification not found",
  "error_code": "file_not_found",
  "details": {
    "path": "workspace/tasks/task-auth-002-signup.md",
    "suggestion": "Create task spec first using create-task-spec skill"
  },
  "telemetry": {
    "skill": "implement-feature",
    "task_id": "task-auth-002-signup",
    "duration_ms": 1200,
    "step_failed": "load_task_spec",
    "timestamp": "2025-01-15T14:30:00Z"
  }
}
```

---

## Task File Update Template

After completing implementation, update the task file with this structure:

### Implementation Record Template

```markdown
## Implementation

**Status:** ✅ Complete
**Implemented By:** James (Developer)
**Date:** 2025-01-15
**Duration:** 45 minutes

### Changes

**Files Created:**
- `src/auth/signup.controller.ts` - User signup controller with validation
- `src/schemas/auth.schema.ts` - Zod validation schemas for auth
- `tests/unit/auth/signup.test.ts` - Unit tests (8 tests)
- `tests/integration/auth/signup.integration.test.ts` - Integration tests (4 tests)

**Files Modified:**
- `src/routes/auth.routes.ts` - Added POST /api/auth/signup route

### Test Results

**Coverage:** 87% (target: 80%)
**Tests Total:** 12
**Tests Passed:** 12
**Tests Failed:** 0

**Test Breakdown:**
- Unit tests: 8/8 passing
- Integration tests: 4/4 passing

### Acceptance Criteria Status

- ✅ **AC-1**: User can enter email and password on signup form
  - Tests: `signup.test.ts:15-32`
  - Status: Passing

- ✅ **AC-2**: Email validated with Zod
  - Tests: `signup.test.ts:34-56`
  - Status: Passing

- ✅ **AC-3**: Password hashed with bcrypt
  - Tests: `signup.test.ts:58-72`
  - Status: Passing

- ✅ **AC-4**: Duplicate emails rejected with 409
  - Tests: `signup.integration.test.ts:15-34`
  - Status: Passing

- ✅ **AC-5**: Success returns JWT token
  - Tests: `signup.integration.test.ts:36-52`
  - Status: Passing

- ✅ **AC-6**: User record saved to PostgreSQL
  - Tests: `signup.integration.test.ts:54-68`
  - Status: Passing

### Technical Notes

**Password Hashing:**
- Using bcrypt with cost factor 12 (as specified)
- Average hash time: ~200ms

**Email Validation:**
- Custom RFC 5322-compliant regex
- Allows + symbol in email local part

**JWT Tokens:**
- 24-hour expiration (as specified)
- HS256 algorithm
- Contains user ID and email

### Performance

- Signup endpoint: ~250ms average response time
- Database insert: ~50ms
- Password hashing: ~200ms (bcrypt cost 12)

### Commit

```bash
git commit -m "feat: implement user signup with email/password

- Add signup controller with validation
- Implement password hashing with bcrypt (cost 12)
- Add POST /api/auth/signup route
- Create Zod validation schemas for auth
- Add 12 tests (8 unit, 4 integration)
- Test coverage: 87%

Implements: task-auth-002-signup
All acceptance criteria met
```
```

---

## Commit Message Templates

### Feature Implementation

```bash
git commit -m "feat: [brief description]

- [Change 1]
- [Change 2]
- [Change 3]
- [Test summary]

Implements: [task-id]
[Additional notes]"
```

**Example:**
```bash
git commit -m "feat: implement user signup with email/password

- Add signup controller with validation
- Implement password hashing with bcrypt (cost 12)
- Add POST /api/auth/signup route
- Create Zod validation schemas
- Add 12 tests (8 unit, 4 integration)

Implements: task-auth-002-signup
Coverage: 87%"
```

### Bug Fix During Implementation

```bash
git commit -m "fix: [brief description]

- [Root cause]
- [Fix applied]
- [Tests added]

Related: [task-id]"
```

**Example:**
```bash
git commit -m "fix: email validation rejects valid + symbols

- Root cause: Overly strict email regex
- Applied RFC 5322-compliant validation
- Added 3 edge case tests

Related: task-auth-002-signup"
```

### Refactoring

```bash
git commit -m "refactor: [brief description]

- [Refactoring 1]
- [Refactoring 2]
- No functional changes
- All tests passing

Related: [task-id]"
```

**Example:**
```bash
git commit -m "refactor: extract password hashing to utility

- Move bcrypt logic to auth.utils.ts
- Add error handling for hash failures
- No functional changes
- All tests passing (12/12)

Related: task-auth-002-signup"
```

---

## Summary Report Template

Present this summary when implementation is complete:

### Implementation Complete Template

```markdown
✅ Implementation Complete: [Task Title]

**Task:** [task-id]
**Duration:** [X] minutes
**Status:** All acceptance criteria met

## Changes Summary

**Files Created:** [X]
- [file-1] - [purpose]
- [file-2] - [purpose]

**Files Modified:** [X]
- [file-1] - [changes]

## Test Results

**Coverage:** [X]% (target: 80%)
**Tests:** [X]/[X] passing

**Breakdown:**
- Unit tests: [X]/[X] passing
- Integration tests: [X]/[X] passing
- E2E tests: [X]/[X] passing (if applicable)

## Acceptance Criteria

- ✅ AC-1: [criterion] - Tests passing
- ✅ AC-2: [criterion] - Tests passing
- ✅ AC-3: [criterion] - Tests passing

## Performance

- [Endpoint]: ~[X]ms average response
- [Operation]: ~[X]ms

## Next Steps

- Ready for code review
- Ready for QA testing
- Consider: [any follow-up tasks]

## Commit

Committed with message: "[commit message]"
```

**Example:**
```markdown
✅ Implementation Complete: User Signup with Email/Password

**Task:** task-auth-002-signup
**Duration:** 45 minutes
**Status:** All acceptance criteria met

## Changes Summary

**Files Created:** 4
- src/auth/signup.controller.ts - Signup controller with validation
- src/schemas/auth.schema.ts - Zod validation schemas
- tests/unit/auth/signup.test.ts - Unit tests (8 tests)
- tests/integration/auth/signup.integration.test.ts - Integration tests (4 tests)

**Files Modified:** 1
- src/routes/auth.routes.ts - Added POST /api/auth/signup route

## Test Results

**Coverage:** 87% (target: 80%)
**Tests:** 12/12 passing

**Breakdown:**
- Unit tests: 8/8 passing
- Integration tests: 4/4 passing

## Acceptance Criteria

- ✅ AC-1: User can enter email and password - Tests passing
- ✅ AC-2: Email validated with Zod - Tests passing
- ✅ AC-3: Password hashed with bcrypt - Tests passing
- ✅ AC-4: Duplicate emails rejected with 409 - Tests passing
- ✅ AC-5: Success returns JWT token - Tests passing
- ✅ AC-6: User record saved to PostgreSQL - Tests passing

## Performance

- POST /api/auth/signup: ~250ms average response
- Password hashing: ~200ms (bcrypt cost 12)
- Database insert: ~50ms

## Next Steps

- Ready for code review
- Ready for QA testing
- Consider: Add rate limiting to prevent spam signups

## Commit

Committed with message: "feat: implement user signup with email/password"
```

---

## Error Message Templates

### Task Spec Not Found

```markdown
❌ Error: Task specification not found

**Path:** workspace/tasks/{task_id}.md
**Action:** Create task spec first using create-task-spec skill

**Next Steps:**
1. Run: Use create-task-spec skill with requirements
2. Verify task spec created at workspace/tasks/{task_id}.md
3. Retry implementation
```

### Tests Failing

```markdown
❌ Error: Tests failing after implementation

**Failed Tests:** {count}
**Coverage:** {percent}%

**Failures:**
- {test-1}: {error-message}
- {test-2}: {error-message}

**Action:**
1. Review failure messages above
2. Fix implementation issues
3. Re-run tests
4. Verify all tests pass
```

### Coverage Below Threshold

```markdown
⚠️ Warning: Coverage below threshold

**Current Coverage:** {actual}%
**Required Coverage:** 80%
**Gap:** {gap}%

**Action:**
1. Identify uncovered code paths
2. Add tests for uncovered logic
3. Focus on:
   - Error handling paths
   - Edge cases
   - Conditional branches
4. Re-run tests to verify coverage
```

---

## Test Output Templates

### bmad-commands run_tests.py Output

**Success:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "coverage_percent": 87,
    "duration_ms": 8500,
    "framework": "jest"
  },
  "telemetry": {
    "command": "run_tests",
    "timestamp": "2025-01-15T14:30:00Z"
  },
  "errors": []
}
```

**Failure:**
```json
{
  "success": true,
  "outputs": {
    "passed": false,
    "total_tests": 12,
    "passed_tests": 10,
    "failed_tests": 2,
    "coverage_percent": 72,
    "duration_ms": 8500,
    "framework": "jest",
    "failures": [
      {
        "test": "should reject duplicate emails",
        "error": "Expected 409, received 500",
        "file": "signup.integration.test.ts:25"
      },
      {
        "test": "should hash password with bcrypt",
        "error": "Expected hash to start with $2b$, received plain text",
        "file": "signup.test.ts:62"
      }
    ]
  },
  "telemetry": {
    "command": "run_tests",
    "timestamp": "2025-01-15T14:30:00Z"
  },
  "errors": []
}
```

---

*Part of BMAD Enhanced Development Suite - implement-feature skill*
