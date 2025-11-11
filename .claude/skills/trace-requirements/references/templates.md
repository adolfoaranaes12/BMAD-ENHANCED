# Requirements Traceability Templates and Output Formats

All output formats, examples, and templates for the trace-requirements skill.

---

## Step 0: Configuration Loading Output

**Complete Output Format:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: task-006-user-signup - User signup with email verification
✓ Acceptance Criteria: 8 criteria identified
  - AC-1: User can sign up with email and password
  - AC-2: Password must be at least 8 characters
  - AC-3: System must validate email format
  - AC-4: System must rate-limit login attempts to 5 per minute
  - AC-5: System must hash passwords with bcrypt (10 rounds)
  - AC-6: System must send email verification link
  - AC-7: User cannot login until email verified
  - AC-8: System must prevent duplicate email registrations
✓ Related assessments:
  - Risk profile: FOUND (.claude/quality/assessments/task-006-risk-20251028.md)
  - Test design: FOUND (.claude/quality/assessments/task-006-test-design-20251029.md)
✓ Implementation files: 6 files identified
  - src/routes/auth/signup.ts (created, lines 1-87)
  - src/validators/auth.ts (created, lines 1-45)
  - src/middleware/rate-limit.ts (modified, lines 23-56)
  - src/services/email.service.ts (modified, lines 78-123)
  - src/models/user.model.ts (modified, lines 12-25)
  - src/__tests__/auth/signup.test.ts (created, lines 1-234)
✓ Output: .claude/quality/assessments/task-006-trace-20251030.md

Ready to begin traceability analysis...
```

---

## Step 1: Forward Traceability Examples

### Implemented AC Example

**AC with Complete Implementation:**
```markdown
AC-1: User can sign up with email and password

Status: ✅ Implemented

Evidence:
  1. File: src/routes/auth/signup.ts:15-42
     Function: handleSignup()
     Description: Implements POST /api/auth/signup endpoint. Accepts email/password
                  in request body, validates inputs, hashes password with bcrypt,
                  creates user record in database, sends verification email, and
                  returns JWT token for authenticated session.

     Code Snippet:
     ```typescript
     export async function handleSignup(req: Request, res: Response) {
       const { email, password } = req.body;

       // Validate inputs
       const validation = validateSignupInput({ email, password });
       if (!validation.success) {
         return res.status(400).json({ errors: validation.errors });
       }

       // Hash password
       const hashedPassword = await bcrypt.hash(password, 10);

       // Create user
       const user = await prisma.user.create({
         data: { email, password: hashedPassword, emailVerified: false }
       });

       // Send verification email
       await sendVerificationEmail(user.email);

       // Return success
       return res.status(201).json({
         user: { id: user.id, email: user.email },
         token: generateJWT(user)
       });
     }
     ```

  2. File: src/validators/auth.ts:12-28
     Function: validateSignupInput()
     Description: Validates email format (RFC 5322) and password requirements
                  (minimum length, character types). Returns success boolean
                  and detailed error messages for validation failures.

Implementation Notes:
  - Complete implementation of signup flow
  - Follows security best practices (password hashing, email verification)
  - Proper error handling with user-friendly messages
  - Integrated with existing auth infrastructure

Dependencies:
  - bcrypt library for password hashing (v5.1.1)
  - Prisma ORM for database operations
  - JWT library for token generation
  - Email service for verification emails
```

### Partial Implementation Example

**AC with Incomplete Implementation:**
```markdown
AC-4: System must rate-limit login attempts to 5 per minute

Status: ⚠️  Partial

Evidence:
  1. File: src/middleware/rate-limit.ts:23-45
     Function: loginRateLimiter()
     Description: Rate limiting middleware configured for /api/auth/login endpoint.
                  Uses redis-rate-limit library with 5 requests per 60 seconds
                  per IP address.

     Code Snippet:
     ```typescript
     export const loginRateLimiter = rateLimit({
       store: new RedisStore({ client: redisClient }),
       windowMs: 60 * 1000, // 1 minute
       max: 5, // 5 requests per minute
       message: 'Too many login attempts, please try again later',
       standardHeaders: true,
       legacyHeaders: false,
     });
     ```

Gaps:
  ⚠️  Rate limiter tracks by IP address only (not by email/username)
      - Issue: Attacker can rotate IPs to bypass rate limit
      - Recommendation: Track by both IP AND email/username
      - Effort: Small (30 min)
      - Priority: P1

  ⚠️  No exponential backoff (fixed 1-minute window)
      - Issue: Attacker can retry every 60 seconds indefinitely
      - Recommendation: Implement exponential backoff (1min, 2min, 4min...)
      - Effort: Medium (2 hours)
      - Priority: P1

Implementation Status: Partial (basic rate limiting exists, but lacks robust protections)
```

### Not Implemented Example

**AC with Missing Implementation:**
```markdown
AC-7: User cannot login until email verified

Status: ❌ Not Implemented

Evidence:
  No evidence found in implementation files.

Expected Implementation:
  - Check user.emailVerified flag in login handler
  - Return 403 Forbidden if email not verified
  - Return error message: "Please verify your email before logging in"
  - Optionally: Resend verification email option

Searched Locations:
  - src/routes/auth/login.ts (no email verification check found)
  - src/middleware/auth.middleware.ts (no verification check)
  - src/services/auth.service.ts (no verification logic)

Gap Severity: CRITICAL
  - Security requirement to prevent unauthorized access
  - Core authentication flow requirement
  - High risk if missing (unverified users can access system)

Required Action: Implement email verification check in login handler

Effort Estimate: Small (1-2 hours)
  - Add check in login handler (30 min)
  - Add tests for verification flow (1 hour)
  - Update API documentation (30 min)

Priority: P0 (must fix before merge)

Related Tests: None found (will need new tests)
```

---

## Step 1: Forward Traceability Output

**Complete Step Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Forward Traceability Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Acceptance Criteria: 8

Implementation Status:
  ✅ Implemented:     5 criteria (62.5%)
  ⚠️  Partial:         2 criteria (25.0%)
  ❌ Not Implemented: 1 criterion  (12.5%)
  ❓ Unclear:         0 criteria (0.0%)

Implementation Coverage: 75.0%
  Formula: (5 + 0.5 × 2) / 8 = 6 / 8 = 75%

Breakdown by Status:
  ✅ AC-1: User can sign up with email and password - Implemented
  ✅ AC-2: Password must be at least 8 characters - Implemented
  ✅ AC-3: System must validate email format - Implemented
  ⚠️  AC-4: System must rate-limit login attempts to 5 per minute - Partial
  ✅ AC-5: System must hash passwords with bcrypt (10 rounds) - Implemented
  ✅ AC-6: System must send email verification link - Implemented
  ❌ AC-7: User cannot login until email verified - Not Implemented
  ⚠️  AC-8: System must prevent duplicate email registrations - Partial

Implementation Gaps: 3 (1 not implemented, 2 partial)
  - Critical: 1 (AC-7)
  - High: 2 (AC-4, AC-8)

Next: Build backward traceability (tests → AC)
```

---

## Step 2: Backward Traceability Examples

### Test Mapping Example

**Test-to-AC Mapping:**
```markdown
Test Suite: src/__tests__/auth/signup.test.ts

describe('POST /api/auth/signup', () => {
  it('should create user with valid email and password', async () => {
    // Validates: AC-1 (User can sign up with email and password)
    // Type: Integration, Priority: P0
    // Coverage: Happy path
  });

  it('should reject password shorter than 8 characters', async () => {
    // Validates: AC-2 (Password must be at least 8 characters)
    // Type: Unit, Priority: P0
    // Coverage: Validation edge case
  });

  it('should reject invalid email format', async () => {
    // Validates: AC-3 (System must validate email format)
    // Type: Unit, Priority: P0
    // Coverage: Validation edge case
  });

  it('should hash password before storing in database', async () => {
    // Validates: AC-5 (System must hash passwords with bcrypt)
    // Type: Integration, Priority: P0
    // Coverage: Security requirement
  });

  it('should send verification email after signup', async () => {
    // Validates: AC-6 (System must send email verification link)
    // Type: Integration, Priority: P0
    // Coverage: Happy path
  });

  it('should return 409 for duplicate email', async () => {
    // Validates: AC-8 (System must prevent duplicate email registrations)
    // Type: Integration, Priority: P0
    // Coverage: Error case
  });
});

Total Tests in Suite: 12
Tests Mapped to ACs: 6
ACs Validated by Suite: 5 (AC-1, AC-2, AC-3, AC-5, AC-6, AC-8)
ACs Not Tested: 2 (AC-4: Rate limiting, AC-7: Email verification gate)
```

### Detailed Test-to-AC Entry

**Complete Test Entry:**
```markdown
Test: "should create user with valid email and password"

Validates: AC-1 (User can sign up with email and password)

Test Details:
  - File: src/__tests__/auth/signup.test.ts:12-35
  - Type: Integration Test
  - Priority: P0 (critical path)
  - Framework: Jest + Supertest
  - Duration: ~250ms

Test Scenario:
  Given: Valid email "test@example.com" and password "SecurePass123"
  When: POST /api/auth/signup with valid credentials
  Then:
    - Response status is 201 (Created)
    - Response includes user object with id and email
    - Response includes JWT token
    - User is created in database with hashed password
    - emailVerified is false
    - Verification email is sent

Assertions:
  1. expect(response.status).toBe(201)
  2. expect(response.body.user).toHaveProperty('id')
  3. expect(response.body.user.email).toBe('test@example.com')
  4. expect(response.body.token).toBeDefined()
  5. expect(mockEmailService.send).toHaveBeenCalledWith(...)

Coverage: ✅ Complete (happy path covered, all core assertions present)

Related ACs: Also validates AC-5 (password hashing) and AC-6 (email sending)
```

---

## Step 2: Backward Traceability Output

**Complete Step Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Backward Traceability Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Tests Found: 12
Test Suites: 1
Test Files: src/__tests__/auth/signup.test.ts

Test Coverage by AC:
  ✅ AC-1: User can sign up - TESTED (2 tests: happy path, edge cases)
  ✅ AC-2: Password length - TESTED (3 tests: boundary, validation, errors)
  ✅ AC-3: Email validation - TESTED (2 tests: valid/invalid formats)
  ❌ AC-4: Rate limiting - NOT TESTED (no tests found)
  ✅ AC-5: Password hashing - TESTED (1 test: bcrypt verification)
  ✅ AC-6: Email verification - TESTED (2 tests: sending, link format)
  ❌ AC-7: Email gate - NOT TESTED (no tests found)
  ⚠️  AC-8: Duplicate prevention - PARTIAL (only 409 error, no constraint tests)

Test Coverage Summary:
  ✅ Tested:        5 ACs (62.5%)
  ⚠️  Partial:       1 AC  (12.5%)
  ❌ Not Tested:    2 ACs (25.0%)

Test Coverage Percentage: 68.75%
  Formula: (5 + 0.5 × 1) / 8 = 5.5 / 8 = 68.75%

Test Types:
  - Unit Tests: 4 (validation, edge cases)
  - Integration Tests: 8 (API endpoints, database)
  - E2E Tests: 0

Test Priorities:
  - P0 (Critical): 10 tests
  - P1 (High): 2 tests
  - P2 (Medium): 0 tests

Test Gaps: 3 (2 not tested, 1 partial)
  - Critical: 1 (AC-7: Email gate not tested)
  - High: 2 (AC-4: Rate limiting, AC-8: Duplicate constraint)

Next: Identify and classify coverage gaps
```

---

## Step 3: Gap Analysis Examples

### Implementation Gap Example

**Critical Implementation Gap:**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPLEMENTATION GAP #1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AC-7: User cannot login until email verified

Gap Type: Implementation Missing
Status: ❌ Not Implemented

Severity: CRITICAL (Score: 9)
  - Security requirement to prevent unauthorized access
  - Core authentication flow requirement
  - HIGH risk if missing (from risk profile Risk #3)
  - Allows unverified users to access system

Impact:
  - Security: Unverified users can login and access system
  - User Experience: Violates expected authentication flow
  - Compliance: May violate email verification requirements

Risk Profile Reference:
  - Risk #3: Unauthorized access via unverified accounts
  - Risk Score: 8 (HIGH)
  - Likelihood: MEDIUM, Impact: HIGH
  → Gap severity amplified: HIGH → CRITICAL

Required Action:
  1. Add email verification check in login handler
  2. Return 403 Forbidden if user.emailVerified is false
  3. Return clear error message with resend link option
  4. Add tests for verification gate

Implementation Guidance:
  File: src/routes/auth/login.ts
  Location: After password validation, before JWT generation

  Code to add:
  ```typescript
  if (!user.emailVerified) {
    return res.status(403).json({
      error: 'Email not verified',
      message: 'Please verify your email before logging in',
      resendLink: `/api/auth/resend-verification?email=${user.email}`
    });
  }
  ```

Effort Estimate: Small (1-2 hours)
  - Implementation: 30 minutes
  - Testing: 1 hour
  - Documentation: 30 minutes

Priority: P0 (MUST FIX before merge)

Blocker: YES (security requirement, blocks merge/release)
```

### Test Gap Example

**High-Priority Test Gap:**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEST GAP #1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AC-4: System must rate-limit login attempts to 5 per minute

Gap Type: Test Coverage Missing
Implementation: ⚠️  Partial (basic rate limiting exists, but gaps in implementation)
Test Coverage: ❌ Not Tested

Severity: HIGH (Score: 7)
  - Security requirement (brute force protection)
  - Implementation exists but incomplete
  - No tests to validate rate limiting behavior

Missing Test Scenarios:
  1. ❌ Should return 429 after 5 failed login attempts within 1 minute
  2. ❌ Should reset rate limit counter after 1 minute
  3. ❌ Should track rate limit per email (not just IP)
  4. ❌ Should implement exponential backoff for repeated violations
  5. ❌ Should include Retry-After header in 429 response

Implementation Gaps (found during analysis):
  - Rate limiter only tracks by IP (should also track by email)
  - No exponential backoff (fixed 1-minute window)
  - No monitoring/alerting for rate limit violations

Required Action:
  1. Fix implementation gaps (add email tracking, exponential backoff)
  2. Write comprehensive test suite for rate limiting:
     - Happy path: Normal login attempts
     - Rate limit: Exceed 5 attempts in 1 minute
     - Reset: Rate limit resets after window
     - Email tracking: Different users same IP
     - IP tracking: Same user different IPs
     - Exponential backoff: Repeated violations

Test Implementation Guidance:
  File: src/__tests__/auth/rate-limit.test.ts (new file)
  Framework: Jest + Supertest

  Example test:
  ```typescript
  describe('Rate Limiting', () => {
    it('should return 429 after 5 failed login attempts', async () => {
      const email = 'test@example.com';

      // Make 5 failed attempts
      for (let i = 0; i < 5; i++) {
        await request(app)
          .post('/api/auth/login')
          .send({ email, password: 'wrong' })
          .expect(401);
      }

      // 6th attempt should be rate limited
      const response = await request(app)
        .post('/api/auth/login')
        .send({ email, password: 'wrong' });

      expect(response.status).toBe(429);
      expect(response.headers['retry-after']).toBeDefined();
      expect(response.body.message).toContain('Too many login attempts');
    });
  });
  ```

Effort Estimate: Medium (3-4 hours)
  - Fix implementation gaps: 2 hours
  - Write comprehensive tests: 2 hours

Priority: P1 (SHOULD FIX before release)

Blocker: NO (can merge, but should fix before production)
```

---

## Step 3: Gap Analysis Output

**Complete Step Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Coverage Gap Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Gaps Identified: 6

Gap Breakdown:
  - Implementation Gaps: 3
    * Not Implemented: 1 (AC-7)
    * Partial: 2 (AC-4, AC-8)

  - Test Gaps: 3
    * Not Tested: 2 (AC-4, AC-7)
    * Partial Test Coverage: 1 (AC-8)

Gap Severity Distribution:
  - CRITICAL (Score 9): 1 gap
    * AC-7: Email verification gate (implementation + test)

  - HIGH (Score 6-8): 4 gaps
    * AC-4: Rate limiting (implementation partial, test missing)
    * AC-4: Rate limiting tests (5 test scenarios missing)
    * AC-8: Duplicate prevention (database constraint missing)
    * AC-8: Duplicate prevention tests (constraint tests missing)

  - MEDIUM (Score 3-5): 1 gap
    * AC-8: Duplicate prevention (error handling partial)

Priority Distribution:
  - P0 (Must Fix): 1 gap (AC-7)
  - P1 (Should Fix): 4 gaps (AC-4, AC-8 issues)
  - P2 (Nice to Have): 1 gap

Blockers: 1 (AC-7 blocks merge due to security requirement)

Total Effort to Close All Gaps: 9-13 hours
  - P0 Gaps: 1-2 hours
  - P1 Gaps: 8-11 hours

Risk Profile Integration:
  - 2 gaps match HIGH risks in risk profile
  - Gap severities amplified based on risk scores
  - AC-7 severity: HIGH → CRITICAL (matches Risk #3)

Next: Generate traceability report
```

---

## Complete Traceability Matrix Example

**Matrix Format:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUIREMENTS TRACEABILITY MATRIX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-006-user-signup - User signup with email verification
Date: 2025-10-30

┌─────┬──────────────────────────────────────────────┬──────────────┬────────────┬─────────────┐
│ AC  │ Requirement                                  │ Impl Status  │ Test Status│ Gap Severity│
├─────┼──────────────────────────────────────────────┼──────────────┼────────────┼─────────────┤
│ AC-1│ User can sign up with email and password    │ ✅ Implemented│ ✅ Tested   │ None        │
│ AC-2│ Password must be at least 8 characters      │ ✅ Implemented│ ✅ Tested   │ None        │
│ AC-3│ System must validate email format           │ ✅ Implemented│ ✅ Tested   │ None        │
│ AC-4│ System must rate-limit login attempts       │ ⚠️  Partial   │ ❌ Not Tested│ HIGH (P1)   │
│ AC-5│ System must hash passwords with bcrypt      │ ✅ Implemented│ ✅ Tested   │ None        │
│ AC-6│ System must send email verification link    │ ✅ Implemented│ ✅ Tested   │ None        │
│ AC-7│ User cannot login until email verified      │ ❌ Not Impl   │ ❌ Not Tested│ CRITICAL(P0)│
│ AC-8│ System must prevent duplicate email registr │ ⚠️  Partial   │ ⚠️  Partial  │ HIGH (P1)   │
└─────┴──────────────────────────────────────────────┴──────────────┴────────────┴─────────────┘

Coverage Summary:
  Implementation Coverage: 75.0% (5 complete, 2 partial, 1 missing)
  Test Coverage: 68.75% (5 tested, 1 partial, 2 missing)
  Overall Traceability Score: 71.9%

Quality Gate Impact: CONCERNS
  - 1 CRITICAL gap (blocks merge)
  - 4 HIGH gaps (should fix before release)
  - Overall score < 80% (target for PASS)
```

---

## Step 4: Complete Summary Format

**Full Summary Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Requirements Traceability Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-006-user-signup - User signup with email verification
Date: 2025-10-30
Assessor: trace-requirements skill v2.0
Duration: 4m 23s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Traceability Score: 71.9%

Formula: (Implementation Coverage × 0.6) + (Test Coverage × 0.4)
       = (75.0% × 0.6) + (68.75% × 0.4)
       = 45.0% + 27.5%
       = 71.9%

Status: CONCERNS (target: ≥80% for PASS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Coverage Breakdown:

Total Acceptance Criteria: 8

Forward Traceability (AC → Implementation):
  ✅ Implemented:     5 ACs (62.5%)
  ⚠️  Partial:         2 ACs (25.0%)
  ❌ Not Implemented: 1 AC  (12.5%)
  Implementation Coverage: 75.0%

Backward Traceability (Tests → AC):
  ✅ Tested:         5 ACs (62.5%)
  ⚠️  Partial:        1 AC  (12.5%)
  ❌ Not Tested:     2 ACs (25.0%)
  Test Coverage: 68.75%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  Coverage Gaps: 6 total

CRITICAL Gaps (P0 - Must Fix Before Merge):

1. [Implementation + Test] AC-7: Email Verification Gate
   Status: ❌ Not Implemented, ❌ Not Tested
   Impact: Security - Unverified users can login and access system
   Risk: Matches Risk #3 from risk profile (Score: 8, HIGH)
   Action: Implement email verification check in login handler
   Effort: 1-2 hours
   Priority: P0 - BLOCKS MERGE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH Gaps (P1 - Should Fix Before Release):

2. [Implementation] AC-4: Rate Limiting - Partial Implementation
   Status: ⚠️  Tracks IP only, no exponential backoff
   Action: Add email tracking + exponential backoff
   Effort: 2 hours
   Priority: P1

3. [Test] AC-4: Rate Limiting - Test Coverage Missing
   Status: ❌ 0 tests validating rate limiting behavior
   Action: Write 5 test scenarios (happy path, limit, reset, tracking)
   Effort: 2 hours
   Priority: P1

4. [Implementation] AC-8: Duplicate Prevention - Partial Implementation
   Status: ⚠️  Application-level check only, no DB constraint
   Action: Add unique constraint on email column in database
   Effort: 1 hour (migration + rollback plan)
   Priority: P1

5. [Test] AC-8: Duplicate Prevention - Partial Test Coverage
   Status: ⚠️  Only tests 409 error, doesn't test constraint
   Action: Add tests for database constraint enforcement
   Effort: 1 hour
   Priority: P1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Quality Gate Impact: CONCERNS

Reasoning:
  - Traceability score is 71.9% (below 80% threshold)
  - 1 CRITICAL gap (AC-7) blocks merge (security requirement)
  - 4 HIGH gaps should be fixed before production release
  - Implementation coverage 75% (below 85% target)
  - Test coverage 68.75% (below 80% target)

Decision:
  - Merge: BLOCKED until AC-7 (P0) is resolved
  - Release: BLOCKED until P1 gaps addressed
  - Recommendation: Fix all 6 gaps (~9-13 hours) before proceeding

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ To Achieve Quality Gate PASS:

Immediate (Before Merge):
  1. ⏱️  1-2 hours - Implement AC-7 (email verification gate)
     → Add check in login handler
     → Add 2-3 tests for verification gate
     → Update API documentation

After Merge (Before Release):
  2. ⏱️  2 hours - Fix AC-4 implementation (rate limiting)
  3. ⏱️  2 hours - Add AC-4 tests (rate limiting validation)
  4. ⏱️  1 hour  - Fix AC-8 implementation (database constraint)
  5. ⏱️  1 hour  - Add AC-8 tests (constraint validation)

Total Effort: 9-13 hours (~1.5 sprints)

Target Coverage After Fixes:
  - Implementation Coverage: 100% (8/8 ACs)
  - Test Coverage: 100% (8/8 ACs)
  - Traceability Score: 100%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Full Report: .claude/quality/assessments/task-006-trace-20251030.md

Report Contents:
  - Complete traceability matrix (8×3 grid)
  - Detailed AC-to-Implementation mappings (with evidence)
  - Detailed Test-to-AC mappings (with scenarios)
  - Complete gap analysis (6 gaps with remediation)
  - Recommendations (prioritized action plan)
  - Quality gate impact assessment

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Next Steps:

1. 🔥 Fix CRITICAL gap (AC-7) immediately
   → Blocks merge, must resolve before proceeding

2. 📖 Review detailed traceability report
   → .claude/quality/assessments/task-006-trace-20251030.md

3. 📋 Create epic for HIGH gaps (4 items, ~6 hours)
   → Track in project management, schedule for current sprint

4. 🔄 Re-run trace-requirements after fixes
   → Validate gap closure, update traceability score

5. ✅ Proceed to quality-gate when:
   → All P0 gaps closed (AC-7 implemented and tested)
   → Traceability score ≥80%
   → No blockers remaining

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## JSON Output Format

**Complete Skill Output:**
```json
{
  "task_id": "task-006-user-signup",
  "total_acceptance_criteria": 8,
  "implementation_coverage": {
    "implemented_count": 5,
    "partial_implementation_count": 2,
    "not_implemented_count": 1,
    "unclear_count": 0,
    "implementation_coverage_percentage": 75.0
  },
  "test_coverage": {
    "tested_count": 5,
    "partial_test_count": 1,
    "not_tested_count": 2,
    "indirect_test_count": 0,
    "test_coverage_percentage": 68.75
  },
  "traceability_score": 71.9,
  "overall_status": "CONCERNS",
  "gaps": [
    {
      "gap_id": 1,
      "ac_id": "AC-7",
      "ac_text": "User cannot login until email verified",
      "gap_type": "implementation",
      "implementation_status": "not_implemented",
      "test_status": "not_tested",
      "severity": "CRITICAL",
      "score": 9,
      "priority": "P0",
      "blocker": true,
      "required_action": "Implement email verification check in login handler",
      "effort_hours": 1.5,
      "risk_profile_reference": "Risk #3 (Score: 8, HIGH)"
    }
  ],
  "total_gaps": 6,
  "critical_gaps_count": 1,
  "high_gaps_count": 4,
  "medium_gaps_count": 1,
  "low_gaps_count": 0,
  "quality_gate_impact": "CONCERNS",
  "quality_gate_reasoning": "Traceability score 71.9% below 80% threshold. 1 CRITICAL gap blocks merge. 4 HIGH gaps should be fixed before release.",
  "report_path": ".claude/quality/assessments/task-006-trace-20251030.md",
  "risk_profile_available": true,
  "test_design_available": true,
  "telemetry": {
    "skill": "trace-requirements",
    "task_id": "task-006-user-signup",
    "total_acceptance_criteria": 8,
    "implementation_coverage_percentage": 75.0,
    "test_coverage_percentage": 68.75,
    "traceability_score": 71.9,
    "total_gaps": 6,
    "critical_gaps_count": 1,
    "duration_ms": 263000,
    "timestamp": "2025-10-30T15:12:45.789Z"
  }
}
```

---

*Complete templates and output formats for trace-requirements skill*
