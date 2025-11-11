# Requirement Analysis Guide

## Purpose

Systematic approach to analyzing acceptance criteria and planning test strategy for feature implementation.

---

## Step 1: Parse Acceptance Criteria

For each acceptance criterion, identify:

**What to Test:**
- Expected behavior or outcome
- Input conditions
- Output/result format
- State changes

**How to Test:**
- Unit test (isolated function/method)
- Integration test (multiple components)
- E2E test (full user flow)

**Test Data Needed:**
- Valid inputs
- Invalid inputs
- Edge cases
- Boundary conditions

**Expected Result:**
- Success response/behavior
- Error responses
- Side effects (logs, database changes)

---

## Example: Login Feature Analysis

### Acceptance Criterion
```
AC-2: Valid credentials return 200 with JWT token
```

### Analysis

**What to Test:**
- Behavior: POST request with valid email/password
- Input: { email: string, password: string }
- Output: { token: string, expiresIn: number }
- State: Session created, login logged

**How to Test:**
- Test Type: Integration (multiple components involved)
- Scope: Controller → Service → Database → JWT generation
- Dependencies: User model, bcrypt, JWT library

**Test Data:**
```javascript
Valid User:
  - email: "test@example.com"
  - password: "SecurePass123!"
  - Expected: 200 status, JWT token in response

Multiple Test Cases:
  1. First-time login (no existing session)
  2. Re-login (existing session should be replaced)
  3. Login from different device/IP
```

**Expected Result:**
```json
{
  "status": 200,
  "body": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "expiresIn": 86400
  }
}
```

---

## Example: Validation Analysis

### Acceptance Criterion
```
AC-4: Missing fields return 400 with validation errors
```

### Analysis

**What to Test:**
- Behavior: POST request with missing required fields
- Input: Missing email OR missing password
- Output: { error: string, code: string }
- State: No session created, failed attempt logged

**How to Test:**
- Test Type: Integration
- Scope: Validation middleware → Error handler
- Dependencies: Zod validation library

**Test Data:**
```javascript
Missing Email:
  - body: { password: "SecurePass123!" }
  - Expected: 400, error message about email

Missing Password:
  - body: { email: "test@example.com" }
  - Expected: 400, error message about password

Missing Both:
  - body: {}
  - Expected: 400, error message about both fields
```

**Expected Result:**
```json
{
  "status": 400,
  "body": {
    "error": "Email is required",
    "code": "VALIDATION_ERROR"
  }
}
```

---

## File Identification Pattern

### Step 1: Identify Core Entities

From acceptance criteria, identify main entities:
- User
- Login Request/Response
- JWT Token
- Rate Limit Counter
- Audit Log

### Step 2: Map to File Structure

**Controllers** (Handle HTTP requests):
- `src/controllers/auth.controller.ts` - Login endpoint handler

**Services** (Business logic):
- `src/services/auth.service.ts` - Authentication logic
- `src/services/user.service.ts` - User operations

**Middleware** (Request processing):
- `src/middleware/rate-limit.ts` - Rate limiting
- `src/middleware/validation.ts` - Input validation

**Utilities** (Helpers):
- `src/utils/jwt.ts` - JWT generation/verification
- `src/utils/audit.ts` - Audit logging

**Schemas** (Validation):
- `src/schemas/auth.schema.ts` - Zod validation schemas

**Tests**:
- `src/__tests__/services/auth.service.test.ts` - Unit tests
- `src/__tests__/integration/auth.integration.test.ts` - Integration tests

**Routes**:
- `src/routes/auth.routes.ts` - Route definitions

### Step 3: Identify Dependencies

**Files to Create:**
- All files that don't exist yet
- Primary implementation + tests

**Files to Modify:**
- Existing routes file (add new route)
- Existing app.ts (register routes)
- Existing config (if needed)

**Files to Reference:**
- Existing models (User)
- Existing database config
- Existing error handlers

---

## Test Strategy Pattern

### Count Acceptance Criteria

Example: Login feature has 7 acceptance criteria

### Map to Test Types

**Unit Tests** (isolated function/method tests):
- Count: ~3-5 per AC that involves business logic
- Example:
  - findUserByEmail (2 tests: found, not found)
  - verifyPassword (2 tests: valid, invalid)
  - generateToken (1 test: correct expiration)

**Integration Tests** (multi-component tests):
- Count: ~1-2 per AC that involves HTTP endpoints
- Example:
  - POST /api/auth/login - valid credentials (1 test)
  - POST /api/auth/login - invalid credentials (2 tests: wrong password, wrong email)
  - POST /api/auth/login - validation errors (3 tests: missing email, password, both)
  - POST /api/auth/login - rate limiting (1 test)

**Total Estimate:**
```
7 AC × ~2 tests average = ~14 tests
```

### Organize Tests

```
src/__tests__/
├── services/
│   ├── auth.service.test.ts (5 unit tests)
│   └── user.service.test.ts (3 unit tests)
├── utils/
│   └── jwt.test.ts (1 unit test)
└── integration/
    └── auth.integration.test.ts (7 integration tests)

Total: 16 tests
```

---

## Common Patterns

### Pattern 1: CRUD Operations

**Acceptance Criteria Format:**
- AC-1: Can create {entity}
- AC-2: Can read {entity}
- AC-3: Can update {entity}
- AC-4: Can delete {entity}
- AC-5: Cannot {action} without permission

**Test Strategy:**
- 4 happy path tests (CRUD)
- 4 error tests (validation, not found, etc.)
- 2-3 permission tests
- **Total:** ~10-11 tests

### Pattern 2: Authentication/Authorization

**Acceptance Criteria Format:**
- AC-1: Can authenticate with valid credentials
- AC-2: Cannot authenticate with invalid credentials
- AC-3: Session expires after {time}
- AC-4: Can access protected resources with valid session
- AC-5: Cannot access protected resources without session

**Test Strategy:**
- 2 authentication tests (valid, invalid)
- 2 session tests (valid, expired)
- 2 authorization tests (allowed, denied)
- **Total:** ~6 tests

### Pattern 3: Data Validation

**Acceptance Criteria Format:**
- AC-1: Required fields must be present
- AC-2: Email must be valid format
- AC-3: Password must meet complexity requirements
- AC-4: Data types must match schema

**Test Strategy:**
- 1 test per required field (missing field)
- 1 test per format validation (invalid format)
- 1 test per complexity rule (too short, no special chars, etc.)
- **Total:** ~8-12 tests depending on rules

---

## Decision Trees

### Should I Write Unit or Integration Test?

```
Does test involve HTTP request/response?
  ├─ YES → Integration Test
  │   └─ Test full request flow
  │
  └─ NO → Does test involve database/external service?
      ├─ YES → Integration Test (with mocks for externals)
      │   └─ Test service + database interaction
      │
      └─ NO → Unit Test
          └─ Test single function/method in isolation
```

### How Many Tests per Acceptance Criterion?

```
Is AC complex (multiple conditions)?
  ├─ YES → 2-4 tests
  │   ├─ Happy path (1 test)
  │   ├─ Error paths (1-2 tests)
  │   └─ Edge cases (1 test)
  │
  └─ NO → 1-2 tests
      ├─ Happy path (1 test)
      └─ One error case (1 test)
```

---

## Quick Reference

**Typical Test Counts:**
- Simple feature (1-3 AC): 5-8 tests
- Medium feature (4-7 AC): 10-15 tests
- Complex feature (8-12 AC): 15-25 tests

**File Count Estimates:**
- Simple: 2-4 files (1 implementation, 1-2 tests, 1 route)
- Medium: 5-8 files (2-3 implementation, 2-3 tests, 1 route, 1 middleware)
- Complex: 9-15 files (4-6 implementation, 4-6 tests, 2 routes, 1-2 middleware)

**Time Estimates:**
- Simple: 10-15 minutes
- Medium: 20-30 minutes
- Complex: 40-60 minutes

---

*Part of implement-feature skill - Development Suite*
