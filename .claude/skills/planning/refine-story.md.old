# Refine Story Skill

## Purpose
Transform vague, incomplete, or ambiguous user stories into clear, sprint-ready stories with well-defined acceptance criteria, test scenarios, and technical guidance. This skill applies structured refinement techniques to improve story quality and reduce implementation ambiguity.

## When to Use This Skill
- Story has vague or unclear requirements
- Acceptance criteria are missing or incomplete
- Story is too large and needs decomposition
- Technical approach is unclear
- Story needs edge case identification
- Before sprint commitment (definition of ready check)
- After stakeholder feedback requiring clarification

## Invocation
```bash
# Basic story refinement
@alex *refine story-auth-001

# Refinement with specific focus
@alex *refine story-auth-001 --focus acceptance-criteria

# Batch refinement
@alex *refine story-auth-001 story-auth-002 story-auth-003

# Interactive refinement (asks user questions)
@alex *refine story-auth-001 --interactive
```

## Prerequisites
- Story file must exist in `.claude/stories/`
- Basic user story narrative (As a... I want... So that...)
- General understanding of feature context

## Skill Configuration
```yaml
skill_name: refine-story
version: 1.0.0
subagent: alex-planner
execution_mode: sequential
halt_on_error: false
output_directory: .claude/refinements
```

---

## STEP 0: Load Story and Assess Quality

### Actions
1. Read story file
2. Parse story components (title, narrative, AC, etc.)
3. Assess story quality against "Definition of Ready"
4. Identify specific gaps and ambiguities
5. Determine refinement strategy

### Story Components to Check

```yaml
Required Components:
  - Title (clear, concise)
  - User Story narrative (As a... I want... So that...)
  - Acceptance Criteria (specific, testable)
  - Priority (P0/P1/P2/P3)

Recommended Components:
  - Technical Notes
  - Dependencies
  - Test Scenarios
  - Edge Cases
  - Definition of Done

Optional Components:
  - Estimation
  - Sprint assignment
  - Wireframes/mockups
```

### Definition of Ready Checklist

A story is "ready" when:
- ✅ **Independent:** Can be worked on without other stories (or dependencies clear)
- ✅ **Negotiable:** Flexible on implementation details
- ✅ **Valuable:** Delivers clear value to user/business
- ✅ **Estimable:** Team can estimate with confidence
- ✅ **Small:** Fits in one sprint (typically ≤13 points)
- ✅ **Testable:** Clear how to verify it works

### Quality Assessment Matrix

| Dimension | Poor (1) | Fair (2) | Good (3) | Excellent (4) |
|-----------|----------|----------|----------|---------------|
| **Title** | Vague | Generic | Descriptive | Specific & action-oriented |
| **Narrative** | Missing/incomplete | Basic format | Clear value | Compelling value prop |
| **AC** | None or 1-2 vague | 2-3 generic | 3-5 specific | 5-8 comprehensive & testable |
| **Technical Notes** | None | Minimal | Moderate | Detailed with links |
| **Edge Cases** | None | 1-2 mentioned | Several identified | Comprehensive list |
| **Dependencies** | Unclear | Mentioned | Listed | Detailed with impact |

### Example: Poor Quality Story

```markdown
**Title:** Login Feature

**User Story:**
Users should be able to login.

**Acceptance Criteria:**
- Login works
- Users can access their account

**Priority:** P0
```

**Assessment:**
```yaml
Quality Score: 1.5/4 (Poor)

Issues Identified:
  - Title too generic (missing "how")
  - Narrative incomplete (no "As a..." format, no "So that...")
  - AC vague and untestable ("login works" - how?)
  - Missing technical notes
  - No edge cases
  - No test scenarios
  - Missing dependencies (depends on signup?)

Ready for Sprint? ❌ No
Estimated Refinement: 15 minutes
```

### Example: Good Quality Story

```markdown
**Title:** User Login with Email and Password

**User Story:**
As a registered user,
I want to log in with my email and password
So that I can access my personalized account and data.

**Acceptance Criteria:**
- AC-1: User can enter email and password on login form
- AC-2: Email is validated for format (valid email structure)
- AC-3: Password is verified against hashed value in database
- AC-4: Success returns JWT token with 24-hour expiration
- AC-5: Invalid credentials return 401 with clear error message
- AC-6: Account lockout after 5 failed attempts
- AC-7: Login attempt is logged for security audit

**Technical Notes:**
- Use bcrypt for password verification
- JWT token includes user ID and roles
- Redis for rate limiting
- PostgreSQL for user lookup

**Dependencies:**
- story-auth-001 (Signup must exist first)

**Priority:** P0
```

**Assessment:**
```yaml
Quality Score: 3.5/4 (Excellent)

Strengths:
  - Clear, specific title
  - Complete user story format with value
  - 7 specific, testable AC
  - Technical guidance provided
  - Dependencies documented

Minor Improvements:
  - Could add edge cases (rate limiting scenarios)
  - Could add test scenarios
  - Could specify error messages

Ready for Sprint? ✅ Yes (with minor enhancements)
Estimated Refinement: 5 minutes (polish only)
```

---

## STEP 1: Enhance User Story Narrative

### User Story Format

**Standard Format:**
```
As a [persona],
I want to [action],
So that [benefit/value].
```

### Persona Identification

**Who is the user?**
- End user (customer, member, visitor)
- Admin user (administrator, moderator)
- System user (API client, integration)
- Developer (for technical stories)

**Examples:**
- "As a new customer"
- "As a returning user"
- "As a site administrator"
- "As an API consumer"
- "As a system (automated process)"

### Action Clarification

**What does the user want to do?**
- Be specific and action-oriented
- Use active verbs
- Avoid technical jargon (unless developer story)

**Poor Examples:**
- ❌ "have login functionality"
- ❌ "use the system"
- ❌ "be authenticated"

**Good Examples:**
- ✅ "log in with my email and password"
- ✅ "reset my password via email"
- ✅ "enable two-factor authentication"

### Benefit/Value Articulation

**Why does the user want this?**
- What problem does it solve?
- What value does it provide?
- What outcome does it enable?

**Poor Examples:**
- ❌ "So that I can login" (circular, no value)
- ❌ "So that the system works" (vague)

**Good Examples:**
- ✅ "So that I can access my personalized account and data"
- ✅ "So that I can recover access if I forget my credentials"
- ✅ "So that I can protect my account from unauthorized access"

### Refinement Example

**Before:**
```
Users should be able to login.
```

**After:**
```
As a registered user,
I want to log in with my email and password
So that I can access my personalized account and data securely.
```

**Refinement Rationale:**
- Added persona: "registered user" (not new user)
- Specified action: "log in with email and password" (clear mechanism)
- Articulated value: "access personalized account and data securely" (clear benefit)

---

## STEP 2: Develop Comprehensive Acceptance Criteria

### AC Best Practices

**Good AC are:**
- **Specific:** No ambiguity about what needs to be true
- **Testable:** Can verify with a test case
- **Implementation-independent:** What, not how
- **User-focused:** From user perspective when possible
- **Numbered:** For easy reference (AC-1, AC-2, etc.)

### AC Formula

```
Given [context/precondition]
When [action/event]
Then [expected outcome]
```

Or simpler format:
```
- AC-X: [Subject] [verb] [expected behavior]
```

### AC Categories

#### 1. Happy Path (Core Functionality)
```
- AC-1: User can enter email and password on login form
- AC-2: Valid credentials return JWT token
- AC-3: User is redirected to dashboard after successful login
```

#### 2. Validation & Errors
```
- AC-4: Invalid email format returns 400 error with "Invalid email format"
- AC-5: Wrong password returns 401 error with "Invalid credentials"
- AC-6: Non-existent email returns 401 error with "Invalid credentials" (security)
```

#### 3. Edge Cases
```
- AC-7: Empty email field shows validation error
- AC-8: Empty password field shows validation error
- AC-9: Account locked after 5 failed attempts (rate limiting)
```

#### 4. Security & Compliance
```
- AC-10: Password is never logged or exposed in responses
- AC-11: Login attempts are logged for security audit
- AC-12: JWT token expires after 24 hours
```

#### 5. Performance & Scalability
```
- AC-13: Login response time < 500ms for 95th percentile
- AC-14: System handles 100 concurrent login requests
```

#### 6. Accessibility & Usability
```
- AC-15: Login form is keyboard accessible (tab navigation)
- AC-16: Error messages are screen-reader friendly
```

### Example Refinement

**Before (Poor AC):**
```
Acceptance Criteria:
- Login works
- Error handling
- Security
```

**After (Comprehensive AC):**
```
Acceptance Criteria:

**Happy Path:**
- AC-1: User can enter email and password on login form
- AC-2: Valid email and password return 200 response with JWT token
- AC-3: JWT token includes user ID, roles, and 24-hour expiration
- AC-4: User is redirected to dashboard after successful login

**Validation:**
- AC-5: Empty email returns 400 with "Email is required"
- AC-6: Invalid email format returns 400 with "Invalid email format"
- AC-7: Empty password returns 400 with "Password is required"

**Error Handling:**
- AC-8: Wrong password returns 401 with "Invalid credentials"
- AC-9: Non-existent email returns 401 with "Invalid credentials" (no email enumeration)
- AC-10: Server errors return 500 with generic "Login failed, please try again"

**Security:**
- AC-11: Password is never exposed in logs or responses
- AC-12: Login attempts are logged with timestamp, IP, and outcome
- AC-13: Account locked for 15 minutes after 5 failed attempts within 10 minutes
- AC-14: Locked account returns 429 with "Account temporarily locked"

**Performance:**
- AC-15: Login response time < 500ms for 95% of requests
```

---

## STEP 3: Identify and Document Edge Cases

### Edge Case Categories

#### 1. Boundary Conditions
```
- Password: min length (12 chars), max length (128 chars)
- Email: min length (3 chars), max length (254 chars, RFC 5321)
- Rate limit: exactly 5 attempts (4 is ok, 5th triggers lock)
```

#### 2. Unusual Input
```
- Email with special characters (user+tag@domain.com)
- Email with international characters (müller@domain.de)
- Password with emojis, unicode, special characters
- Copy-pasted credentials with extra whitespace
```

#### 3. Timing & Concurrency
```
- Multiple login attempts from same user simultaneously
- Password changed while login attempt in progress
- Token refresh while previous token still valid
- Account locked while user has active session
```

#### 4. State Transitions
```
- User already logged in attempts to login again
- User logs in from multiple devices/browsers
- User deleted account but session still active
- User role changed while logged in
```

#### 5. External Dependencies
```
- Database connection lost during login
- Redis (rate limiting) unavailable
- Email service down (for password reset link)
- JWT secret rotated (invalidates old tokens)
```

#### 6. Security Scenarios
```
- Brute force attack (rapid login attempts)
- Credential stuffing (using leaked passwords)
- SQL injection attempts in email field
- XSS attempts in form inputs
```

### Example Edge Case Documentation

```markdown
## Edge Cases

**Boundary Conditions:**
1. Password exactly 12 characters (minimum)
2. Password exactly 128 characters (maximum)
3. Email exactly 254 characters (RFC 5321 max)
4. Exactly 5 failed login attempts (triggers lock)

**Unusual Input:**
5. Email with + symbol (user+tag@domain.com) - should work
6. Email with dots (first.last@domain.com) - should work
7. Password with unicode (emoji, Chinese characters) - should work
8. Whitespace at start/end of email/password - should trim

**Concurrency:**
9. Same user logs in from 2 browsers simultaneously - both should succeed
10. User changes password while another login attempt in-flight - may succeed or fail (race condition)
11. Account locked while user has 2 failed attempts in parallel - prevent timing attack

**State:**
12. User already logged in (has valid token) attempts login again - should succeed (new token)
13. User role changed from User to Admin while logged in - new login reflects new role
14. User account soft-deleted but has active session - session invalidated

**External Failures:**
15. Database connection lost mid-login - return 500, don't lock account
16. Redis unavailable (rate limiting) - fail open (allow login) or fail closed (deny)?
17. JWT secret rotated - existing tokens invalid, user must re-login

**Security:**
18. 1000 rapid login attempts (brute force) - rate limit kicks in, IP blocked
19. SQL injection attempt (email: "' OR 1=1--") - parameterized query prevents
20. XSS attempt (email: "<script>alert('xss')</script>") - input validation prevents
```

---

## STEP 4: Add Technical Guidance

### Technical Notes Structure

#### 1. Technology Stack
```markdown
**Tech Stack:**
- Backend: Node.js with Express.js
- Database: PostgreSQL
- Authentication: bcrypt for hashing, jsonwebtoken for JWT
- Rate Limiting: Redis
- Validation: Zod
```

#### 2. Architecture Patterns
```markdown
**Patterns:**
- Repository pattern for data access
- Service layer for business logic
- Controller for HTTP handling
- Middleware for auth checks
```

#### 3. Security Considerations
```markdown
**Security:**
- Use bcrypt with cost factor 12
- JWT token payload: { userId, roles, iat, exp }
- Never log passwords (even hashed)
- Use parameterized queries to prevent SQL injection
- Rate limit: 5 attempts per 10 minutes per IP
```

#### 4. Data Models
```markdown
**Database Schema:**

users table:
  - id: UUID (primary key)
  - email: VARCHAR(254) UNIQUE NOT NULL
  - password_hash: VARCHAR(60) NOT NULL (bcrypt output)
  - created_at: TIMESTAMP
  - updated_at: TIMESTAMP
  - is_locked: BOOLEAN DEFAULT FALSE
  - locked_until: TIMESTAMP NULL

login_attempts table:
  - id: UUID
  - user_id: UUID (foreign key)
  - ip_address: INET
  - success: BOOLEAN
  - attempted_at: TIMESTAMP
```

#### 5. External Dependencies
```markdown
**Dependencies:**
- Existing: Express app, PostgreSQL connection, Redis client
- New: jsonwebtoken (^9.0.0), Zod (^3.22.0)
- External Services: None
```

#### 6. Performance Requirements
```markdown
**Performance:**
- Response time: < 500ms (p95)
- Throughput: 100 concurrent requests
- Database indexes: email (unique), user_id + attempted_at (for rate limiting)
```

### Example Technical Notes

```markdown
## Technical Notes

**Technology Stack:**
- Node.js 20.x with TypeScript
- Express.js for routing
- PostgreSQL 16 for user storage
- Redis 7 for rate limiting
- bcrypt (cost 12) for password hashing
- jsonwebtoken for JWT generation
- Zod for input validation

**Implementation Approach:**

1. **Controller Layer** (`src/controllers/auth.controller.ts`)
   - HTTP request/response handling
   - Input validation with Zod
   - Error mapping (service errors → HTTP status codes)

2. **Service Layer** (`src/services/auth.service.ts`)
   - Business logic (verify credentials, generate token)
   - Rate limiting check (Redis)
   - Login attempt logging

3. **Repository Layer** (`src/repositories/user.repository.ts`)
   - Database queries (find user by email)
   - Parameterized queries (prevent SQL injection)

4. **Middleware** (`src/middleware/rate-limit.ts`)
   - Check Redis for failed attempt count
   - Increment on failure, reset on success

**Security Considerations:**
- Password never leaves database unhashed
- JWT secret stored in environment variable (not committed)
- Rate limiting prevents brute force (5 attempts / 10 min / IP)
- Error messages avoid email enumeration (always "Invalid credentials")
- Login attempts logged for security audit

**Data Models:**

users table:
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
  email VARCHAR(254) UNIQUE NOT NULL
  password_hash VARCHAR(60) NOT NULL
  is_locked BOOLEAN DEFAULT FALSE
  locked_until TIMESTAMP NULL
  created_at TIMESTAMP DEFAULT NOW()
  updated_at TIMESTAMP DEFAULT NOW()

Indexes:
  - PRIMARY KEY (id)
  - UNIQUE INDEX idx_users_email ON users(email)

**API Contract:**

Request:
POST /api/auth/login
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "SecurePassword123!"
}

Success Response (200):
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 86400,
  "user": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "email": "user@example.com",
    "roles": ["user"]
  }
}

Error Response (401):
{
  "error": "Invalid credentials",
  "code": "AUTH_INVALID_CREDENTIALS"
}

**Performance:**
- Database query: < 50ms (indexed email lookup)
- Bcrypt comparison: ~200ms (cost 12)
- JWT generation: < 10ms
- Total response: < 500ms (p95)

**Testing Notes:**
- Mock bcrypt in unit tests (bcrypt is slow)
- Use test database for integration tests
- Test rate limiting with multiple rapid requests
- Test concurrent logins from same user
```

---

## STEP 5: Create Test Scenarios

### Test Scenario Structure

```markdown
**Test Scenario:** [Descriptive name]
**Type:** [Unit / Integration / E2E]
**Priority:** [P0 / P1 / P2]

**Given:** [Preconditions]
**When:** [Action]
**Then:** [Expected outcome]

**Test Data:**
[Specific test data to use]
```

### Test Types

#### 1. Unit Tests (Fast, Isolated)
Test individual functions/methods:
```markdown
**Test:** Validate email format
**Type:** Unit
**Priority:** P0

**Given:** Email validation function
**When:** Called with "invalid-email"
**Then:** Returns false

**Test Data:**
- Valid: "user@example.com"
- Invalid: "invalid", "@example.com", "user@", "user @example.com"
```

#### 2. Integration Tests (Medium, With Dependencies)
Test multiple components together:
```markdown
**Test:** Successful login flow
**Type:** Integration
**Priority:** P0

**Given:** User exists in database with email "test@example.com"
**When:** POST /api/auth/login with valid credentials
**Then:**
  - Returns 200 status
  - Returns JWT token
  - Token is valid and contains user ID
  - Login attempt logged as success

**Test Data:**
Database seed:
  - email: "test@example.com"
  - password: "SecurePassword123!" (hashed)
```

#### 3. E2E Tests (Slow, Full System)
Test complete user workflows:
```markdown
**Test:** User signs up and logs in
**Type:** E2E
**Priority:** P1

**Given:** Clean database
**When:**
  1. POST /api/auth/signup (create account)
  2. POST /api/auth/login (log in)
**Then:**
  - Both requests succeed
  - Login returns valid token
  - Token can be used to access protected route

**Test Data:**
- email: "newuser@example.com"
- password: "SecurePassword123!"
```

### Example Test Scenarios

```markdown
## Test Scenarios

### Unit Tests

**U-1: Validate email format**
- **Priority:** P0
- **Given:** Email validation function
- **When:** Called with various email formats
- **Then:** Returns true for valid, false for invalid
- **Test Data:**
  - Valid: "user@example.com", "user+tag@example.com", "first.last@example.com"
  - Invalid: "invalid", "@example.com", "user@", "user @example.com"

**U-2: Hash password with bcrypt**
- **Priority:** P0
- **Given:** Password hashing function
- **When:** Called with "SecurePassword123!"
- **Then:** Returns bcrypt hash starting with "$2b$12$"
- **Test Data:** password: "SecurePassword123!", cost: 12

**U-3: Verify password against hash**
- **Priority:** P0
- **Given:** Bcrypt hash of "SecurePassword123!"
- **When:** Compare with "SecurePassword123!" (correct) and "WrongPassword" (incorrect)
- **Then:** Returns true for correct, false for incorrect

**U-4: Generate JWT token**
- **Priority:** P0
- **Given:** JWT generation function
- **When:** Called with userId "123" and roles ["user"]
- **Then:** Returns valid JWT token containing userId and roles
- **Test Data:** userId: "123", roles: ["user"], expiresIn: "24h"

### Integration Tests

**I-1: Successful login with valid credentials**
- **Priority:** P0
- **Given:** User in database (email: "test@example.com", password hashed)
- **When:** POST /api/auth/login with valid credentials
- **Then:**
  - Returns 200 status
  - Returns JWT token
  - Token payload contains userId and roles
  - Login attempt logged as success
- **Test Data:**
  ```json
  {
    "email": "test@example.com",
    "password": "SecurePassword123!"
  }
  ```

**I-2: Failed login with wrong password**
- **Priority:** P0
- **Given:** User in database
- **When:** POST /api/auth/login with wrong password
- **Then:**
  - Returns 401 status
  - Returns error: "Invalid credentials"
  - Login attempt logged as failure
  - Failed attempt count incremented in Redis

**I-3: Failed login with non-existent email**
- **Priority:** P0
- **Given:** Email does not exist in database
- **When:** POST /api/auth/login
- **Then:**
  - Returns 401 status (same as wrong password, no enumeration)
  - Returns error: "Invalid credentials"

**I-4: Account lockout after 5 failed attempts**
- **Priority:** P0
- **Given:** User in database, 4 failed login attempts already
- **When:** POST /api/auth/login with wrong password (5th attempt)
- **Then:**
  - Returns 429 status
  - Returns error: "Account temporarily locked"
  - Account locked for 15 minutes
  - Subsequent login attempts return 429 (even with correct password)

**I-5: Successful login resets failed attempt counter**
- **Priority:** P1
- **Given:** User in database, 3 failed login attempts
- **When:** POST /api/auth/login with valid credentials
- **Then:**
  - Returns 200 status with JWT token
  - Failed attempt counter reset to 0 in Redis

### End-to-End Tests

**E-1: Complete signup and login flow**
- **Priority:** P1
- **Given:** Clean database
- **When:**
  1. POST /api/auth/signup (create account)
  2. POST /api/auth/login (log in with new account)
  3. GET /api/user/profile (access protected route with token)
- **Then:**
  - All requests succeed
  - Profile data matches signup data

**E-2: Concurrent logins from same user**
- **Priority:** P2
- **Given:** User in database
- **When:** Two simultaneous POST /api/auth/login requests
- **Then:**
  - Both return 200 with different JWT tokens
  - Both tokens are valid
  - No race condition errors

### Performance Tests

**P-1: Login response time under load**
- **Priority:** P1
- **Given:** 100 concurrent users
- **When:** All attempt login simultaneously
- **Then:**
  - 95% of requests complete in < 500ms
  - No request fails due to timeout
  - Database and Redis connections remain stable
```

---

## STEP 6: Define Story Size and Splitting Criteria

### Story Size Assessment

**Size Categories:**
```yaml
XS (1-2 points): < 4 hours, single developer, minimal complexity
S (3-5 points): 4-8 hours, single developer, moderate complexity
M (8 points): 1-2 days, may need collaboration, higher complexity
L (13 points): 2-3 days, definitely needs collaboration, very complex
XL (21+ points): > 3 days, MUST SPLIT
```

### Splitting Triggers

**Split a story if:**
1. Estimated at > 13 points
2. Spans multiple sprints
3. Has more than 10 acceptance criteria
4. Involves 3+ distinct components/layers
5. Team has low confidence in estimate (<70%)
6. Has multiple distinct user personas
7. Can deliver value incrementally

### Splitting Strategies

#### 1. By Workflow Steps
**Original (too large):**
"User can complete entire onboarding process"

**Split:**
- Story A: User can create account (signup)
- Story B: User can verify email
- Story C: User can complete profile
- Story D: User can set preferences

#### 2. By CRUD Operations
**Original (too large):**
"User can manage their profile"

**Split:**
- Story A: User can view profile
- Story B: User can edit profile
- Story C: User can delete account

#### 3. By Persona
**Original (too large):**
"Users can log in"

**Split:**
- Story A: Standard user login
- Story B: Admin user login with 2FA
- Story C: API client login (OAuth)

#### 4. By Priority (MVP Slicing)
**Original (too large):**
"Complete authentication system"

**Split:**
- Story A (MVP): Basic email/password login
- Story B (Nice-to-have): Social login (Google, Facebook)
- Story C (Future): Biometric login

#### 5. By Technical Layers
**Original (too large):**
"Complete login feature"

**Split:**
- Story A: Backend login API
- Story B: Frontend login form
- Story C: Integration and error handling

#### 6. By Happy Path vs Edge Cases
**Original (too large):**
"User login with all error handling"

**Split:**
- Story A: Happy path login (valid credentials)
- Story B: Error handling (invalid credentials, rate limiting)

### Example Splitting

**Original Story (21 points - Too Large):**
```markdown
**Title:** Complete User Authentication System

**User Story:**
As a user, I want a complete authentication system so that I can access the platform securely.

**Acceptance Criteria:**
- AC-1: User can sign up with email/password
- AC-2: Email verification required
- AC-3: User can log in
- AC-4: User can log out
- AC-5: User can reset password
- AC-6: Two-factor authentication
- AC-7: Social login (Google, Facebook)
- AC-8: Rate limiting
- AC-9: Session management
- AC-10: Admin role management

**Estimated:** 21 points (MUST SPLIT)
```

**Split into Smaller Stories:**

```markdown
**Story 1: User Signup (5 points)**
As a new user, I want to create an account with email/password
So that I can access the platform.
- AC: Signup form, validation, password hashing, email uniqueness

**Story 2: Email Verification (3 points)**
As a signed-up user, I want to verify my email address
So that the platform knows I'm a real person.
- AC: Verification email sent, verification link, email status update

**Story 3: User Login (3 points)**
As a registered user, I want to log in
So that I can access my account.
- AC: Login form, credential validation, JWT token

**Story 4: User Logout (1 point)**
As a logged-in user, I want to log out
So that I can secure my session.
- AC: Logout endpoint, token invalidation

**Story 5: Password Reset (5 points)**
As a user, I want to reset my forgotten password
So that I can regain access to my account.
- AC: Reset request, email with link, new password form

**Story 6: Rate Limiting (3 points)**
As the system, I want to rate limit login attempts
So that brute force attacks are prevented.
- AC: 5 attempts per 10 min, account lockout, clear error messages

**Story 7: Social Login - Google (8 points)**
As a user, I want to log in with my Google account
So that I don't need to create another password.
- AC: Google OAuth integration, account linking, profile sync

**Total after split: 28 points across 7 stories** (averages 4 points each)
```

---

## STEP 7: Update Story File with Refinements

### Updated Story Structure

```markdown
# Story: [Title]

**ID:** [story-id]
**Epic:** [Epic name]
**Priority:** [P0/P1/P2/P3]
**Status:** [Backlog / Ready / In Progress / Done]
**Estimated:** [Story points] ([Confidence %])

---

## User Story

As a [persona],
I want to [action],
So that [benefit].

---

## Acceptance Criteria

**Happy Path:**
- AC-1: [Primary success criterion]
- AC-2: [Secondary success criterion]

**Validation:**
- AC-3: [Input validation rule]
- AC-4: [Error handling]

**Security:**
- AC-5: [Security requirement]

**Performance:**
- AC-6: [Performance requirement]

---

## Technical Notes

**Technology Stack:**
- [List of technologies]

**Implementation Approach:**
- [Key technical decisions]

**Security Considerations:**
- [Security requirements]

**Data Models:**
- [Database schema or API contracts]

---

## Edge Cases

1. [Boundary condition]
2. [Unusual input]
3. [Concurrency scenario]
4. [State transition]
5. [External failure]

---

## Test Scenarios

### Unit Tests
- U-1: [Test description]

### Integration Tests
- I-1: [Test description]

### E2E Tests (Optional)
- E-1: [Test description]

---

## Dependencies

**Blocks:**
- [story-id]: [Reason]

**Blocked By:**
- [story-id]: [Reason]

**Parallel:**
- [story-id]: [Can work simultaneously]

---

## Definition of Done

- [ ] All acceptance criteria met
- [ ] Code reviewed and approved
- [ ] Unit tests written and passing (>80% coverage)
- [ ] Integration tests written and passing
- [ ] Documentation updated
- [ ] No critical/high severity bugs
- [ ] Deployed to staging environment
- [ ] PO sign-off received

---

## Estimation

**Story Points:** [X]
**Confidence:** [High/Medium/Low] ([%])
**Estimated Date:** [YYYY-MM-DD]
**Estimator:** [Name]

### Breakdown
- Complexity: [1-5]
- Effort: [1-5]
- Risk: [0-3]

---

## Notes

[Any additional context, links to designs, research, etc.]

---

**Refinement History:**
- [Date]: Original creation
- [Date]: Refined by [Name] - [Changes made]
```

---

## STEP 8: Generate Refinement Report

### Report Structure

**File:** `.claude/refinements/[story-id]-refinement-[date].md`

```markdown
# Story Refinement Report

**Story ID:** [story-id]
**Story Title:** [Title]
**Refinement Date:** [YYYY-MM-DD]
**Refined By:** Alex (Planner)

---

## Summary

**Quality Before:** [X]/4
**Quality After:** [Y]/4
**Improvement:** +[Y-X] points

**Ready for Sprint?**
- Before: ❌ No
- After: ✅ Yes

**Key Improvements:**
- [List of major improvements]

---

## Before & After Comparison

### Title
- **Before:** [Original title]
- **After:** [Refined title]
- **Change:** [Description of change]

### User Story
- **Before:** [Original narrative]
- **After:** [Refined narrative]
- **Change:** [Description of change]

### Acceptance Criteria
- **Before:** [X] AC ([List])
- **After:** [Y] AC ([List])
- **Change:** Added [Y-X] new AC, clarified [Z] existing AC

### Technical Notes
- **Before:** [Status]
- **After:** [Enhanced status]
- **Change:** [Description]

---

## Specific Changes Made

### 1. Enhanced User Story Narrative
[Description of changes]

### 2. Expanded Acceptance Criteria
[New AC added]

### 3. Added Technical Guidance
[Technical notes added]

### 4. Identified Edge Cases
[Edge cases documented]

### 5. Created Test Scenarios
[Test scenarios added]

---

## Definition of Ready Assessment

| Criterion | Before | After |
|-----------|--------|-------|
| Independent | ❌ | ✅ |
| Negotiable | ✅ | ✅ |
| Valuable | ⚠️ | ✅ |
| Estimable | ❌ | ✅ |
| Small | ❌ | ✅ |
| Testable | ❌ | ✅ |

**Overall:** Ready for Sprint ✅

---

## Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

---

## Next Steps

- [ ] Review refined story with team
- [ ] Estimate story points (@alex *estimate [story-id])
- [ ] Add to sprint backlog (@alex *sprint)
- [ ] Assign to developer
- [ ] Begin implementation (@james *implement [story-id])

---

*Generated by: `.claude/skills/planning/refine-story.md` v1.0.0*
*Subagent: Alex (Planner)*
```

---

## STEP 9: Present Refinement Summary to User

### Summary Format

```markdown
✅ Story Refinement Complete

**Story:** [story-id] - [Title]

**Quality Improvement:**
- Before: 1.5/4 (Poor)
- After: 3.5/4 (Excellent)
- Change: +2.0 points

**Key Enhancements:**
- ✅ Added complete "As a... I want... So that..." narrative
- ✅ Expanded from 2 vague AC to 15 specific, testable AC
- ✅ Added comprehensive technical notes (tech stack, security, data models)
- ✅ Identified 12 edge cases
- ✅ Created 10 test scenarios (unit, integration, E2E)
- ✅ Defined clear dependencies

**Ready for Sprint:** ✅ Yes (high confidence)

**Files Updated:**
- `.claude/stories/[story-id].md` (refined story)
- `.claude/refinements/[story-id]-refinement-[date].md` (detailed report)

**Next Steps:**
1. Estimate story points: `@alex *estimate [story-id]`
2. Add to sprint: `@alex *sprint "Sprint 1"`
3. Begin implementation: `@james *implement [story-id]`
```

---

## Integration with Other Skills

### Before Refinement
1. **@alex *breakdown** - Create initial stories from epic
   - Stories start rough, need refinement

### After Refinement
1. **@alex *estimate** - Estimate refined stories
   - Refinement increases estimation confidence
2. **@alex *sprint** - Add to sprint plan
3. **@james *implement** - Implement with clear guidance

---

## Best Practices

### 1. Refine Collaboratively
- Involve developers (technical feasibility)
- Involve QA (testability)
- Involve PO (business value)
- Use this skill as starting point for team discussion

### 2. Keep Stories Independent
- Minimize dependencies
- Each story should deliver standalone value
- Avoid "part 1, part 2" stories

### 3. Make AC Testable
- Use specific numbers, not "fast" or "many"
- Define error messages exactly
- Specify response codes

### 4. Document Assumptions
- What are we assuming exists?
- What are we NOT building?
- What is out of scope?

### 5. Balance Detail vs Flexibility
- Enough detail to estimate and implement
- Not so much that it constrains creativity
- Specify "what" not "how" when possible

---

## Common Patterns

### Pattern 1: The "Login Story"
**Initial (Poor):**
"Users can log in"

**Refined:**
- Clear persona (registered user)
- Specific mechanism (email + password)
- Detailed AC (validation, errors, security)
- Technical notes (JWT, bcrypt, rate limiting)
- Edge cases (account lockout, concurrent login)
- Test scenarios (unit, integration)

### Pattern 2: The "CRUD Story"
**Initial (Poor):**
"Users can manage their profile"

**Refined:**
- Split into: View, Edit, Delete (3 stories)
- Each story has specific AC
- Technical notes on data models
- Validation rules defined
- API contracts specified

### Pattern 3: The "Integration Story"
**Initial (Poor):**
"Integrate with payment processor"

**Refined:**
- Clear value (what user can do)
- Detailed AC (success, failures, refunds)
- Technical notes (API keys, webhooks, PCI compliance)
- Edge cases (network failures, duplicate charges)
- Test scenarios (mock service in tests)

---

## Skill Metadata

```yaml
skill_name: refine-story
version: 1.0.0
subagent: alex-planner
category: planning
execution_mode: sequential

inputs:
  required:
    - story_id
  optional:
    - focus (acceptance-criteria, technical-notes, edge-cases)
    - interactive (ask user questions)

outputs:
  - Updated story file
  - Refinement report

dependencies:
  - breakdown-epic.md (creates stories to refine)

execution_time: 5-15 minutes per story
```

---

*This skill is part of the BMAD Enhanced Planning Suite.*
*For issues or improvements, see `.claude/skills/planning/README.md`*
