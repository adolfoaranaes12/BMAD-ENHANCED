# Task: Implement User Authentication System

<!-- BMAD Enhanced Task Specification -->
<!-- Version: 1.0 -->
<!-- This file follows the BMAD context embedding pattern -->

## Metadata

- **Task ID:** task-002
- **Created:** 2025-10-31
- **Last Updated:** 2025-10-31
- **Related Epic/Feature:** Authentication & Authorization Module
- **Priority:** P1 (High)

## Status

Draft

---

## Objective

**As a** system user,
**I want** to securely register, log in, and manage my account,
**so that** I can access protected application features with confidence in security.

---

## Acceptance Criteria

1. **User Registration**: Users can register with email and password, with proper validation (email format, password strength) ✅ *Completed in task-001*
2. **Secure Authentication**: Passwords are hashed (bcrypt), JWT tokens issued on successful login
3. **Login Flow**: Users can log in with valid credentials and receive a JWT token
4. **Password Reset**: Users can request password reset via email and complete the reset flow
5. **Protected Routes**: API endpoints and routes verify JWT tokens before granting access
6. **Security Standards**: Rate limiting on auth endpoints, proper error handling without information leakage

---

## Context (Embedded from Architecture)

<!-- CRITICAL: This section contains ALL context needed for implementation -->
<!-- Implementation skill should NOT need to read architecture docs -->
<!-- Every technical detail MUST include source reference -->

### Previous Task Insights

**From task-001 (User Signup):**
- User model and repository established with email, password (bcrypt hashed), emailVerified
- Zod validation patterns for email and password established
- Express route structure: routes/auth/{feature}.ts pattern
- Service layer pattern: services/auth/{feature}.service.ts
- Repository layer: repositories/user.repository.ts with createUser, findByEmail
- Test structure: Unit tests in __tests__ directories, integration tests with Supertest
- bcrypt cost factor 12 used for password hashing (~150ms, acceptable)
- Password excluded from response types using TypeScript Omit utility

**Key patterns to follow:**
- Continue using Zod for all validation schemas
- Service layer handles business logic, repository handles data access
- Route handlers focus on request/response, delegate to services
- All errors properly typed with statusCode property
- Source references maintained in code comments

[Source: .claude/tasks/task-001-user-signup-validation.md]

### Data Models

**User Model (existing from task-001):**
```typescript
interface User {
  id: string;          // UUID, primary key
  email: string;       // Unique, validated email
  password: string;    // bcrypt hashed, never exposed in responses
  emailVerified: boolean;  // Email verification status (default: false)
  createdAt: Date;     // Auto-generated timestamp
  updatedAt: Date;     // Auto-updated timestamp
}
```

**PasswordReset Model (new):**
```typescript
interface PasswordReset {
  id: string;          // UUID, primary key
  userId: string;      // Foreign key to User.id
  token: string;       // Unique reset token (UUID or random string)
  expiresAt: Date;     // Token expiration (1 hour from creation)
  used: boolean;       // Whether token has been used (default: false)
  createdAt: Date;     // Auto-generated timestamp
}
```

**Prisma Schema Addition:**
```prisma
model PasswordReset {
  id        String   @id @default(uuid())
  userId    String
  user      User     @relation(fields: [userId], references: [id])
  token     String   @unique
  expiresAt DateTime
  used      Boolean  @default(false)
  createdAt DateTime @default(now())

  @@index([token])
  @@index([userId])
}

// Add to User model:
model User {
  id            String          @id @default(uuid())
  email         String          @unique
  password      String
  emailVerified Boolean         @default(false)
  createdAt     DateTime        @default(now())
  updatedAt     DateTime        @updatedAt
  passwordResets PasswordReset[] // New relation
}
```

**JWT Token Structure:**
```typescript
interface TokenPayload {
  userId: string;      // User ID
  email: string;       // User email
  iat: number;         // Issued at (timestamp)
  exp: number;         // Expiration (timestamp)
}

interface TokenResponse {
  token: string;       // JWT token string
  expiresIn: number;   // Seconds until expiration
}
```

[Source: task-001-user-signup-validation.md#data-models]

### API Specifications

**Endpoint 1: POST /api/auth/login**

Request Body:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

Success Response (200 OK):
```json
{
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "emailVerified": false
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600
}
```

Error Responses:
- 400 Bad Request: Invalid email/password format
- 401 Unauthorized: Invalid credentials
- 500 Internal Server Error: Server error

Authentication: None (public endpoint)
Rate Limiting: 5 requests per minute per IP

---

**Endpoint 2: POST /api/auth/password-reset/request**

Request Body:
```json
{
  "email": "user@example.com"
}
```

Success Response (200 OK):
```json
{
  "message": "Password reset email sent if account exists"
}
```

Note: Always return success even if email not found (security best practice - don't leak account existence)

Authentication: None (public endpoint)
Rate Limiting: 3 requests per minute per IP

---

**Endpoint 3: POST /api/auth/password-reset/confirm**

Request Body:
```json
{
  "token": "reset-token-uuid",
  "newPassword": "NewSecurePass456!"
}
```

Success Response (200 OK):
```json
{
  "message": "Password reset successful"
}
```

Error Responses:
- 400 Bad Request: Invalid token or password format
- 401 Unauthorized: Invalid or expired token
- 500 Internal Server Error: Server error

Authentication: None (public endpoint)
Rate Limiting: 5 requests per minute per IP

---

**Middleware: verifyToken**

Applied to protected routes via middleware chain.

Expects Authorization header: `Bearer <jwt-token>`

On success: Attaches user object to request, continues to next middleware

On failure: Returns 401 Unauthorized with error message

[Source: docs/standards.md#api-security]

### Component Specifications

Not applicable - this is a backend API task with no UI components.

### File Locations

**Type Definitions:**
- `src/types/auth.ts` - Extend with LoginRequest, LoginResponse, PasswordResetRequest, TokenPayload, TokenResponse

**Validation Schemas:**
- `src/schemas/auth.schema.ts` - Extend with loginSchema, passwordResetRequestSchema, passwordResetConfirmSchema

**Repository Layer:**
- `src/repositories/user.repository.ts` - Extend with findById, updatePassword methods
- `src/repositories/password-reset.repository.ts` - NEW: createReset, findByToken, markUsed, deleteExpired

**Service Logic:**
- `src/services/auth/token.service.ts` - NEW: generateToken, verifyToken, decodeToken
- `src/services/auth/login.service.ts` - NEW: authenticateUser (validate credentials, generate token)
- `src/services/auth/password-reset.service.ts` - NEW: requestReset, confirmReset

**Route Handlers:**
- `src/routes/auth/login.ts` - NEW: POST /api/auth/login endpoint
- `src/routes/auth/password-reset.ts` - NEW: POST /api/auth/password-reset/request and /confirm
- `src/routes/auth/index.ts` - MODIFY: Register new routes

**Middleware:**
- `src/middleware/auth.middleware.ts` - NEW: verifyToken middleware for protected routes
- `src/middleware/rate-limit.middleware.ts` - NEW: Rate limiting configuration

**Configuration:**
- `.env` - Add JWT_SECRET, JWT_EXPIRATION (e.g., "1h"), PASSWORD_RESET_EXPIRATION (e.g., "1h")

**Test Files:**
- `src/services/auth/__tests__/token.service.test.ts` - NEW
- `src/services/auth/__tests__/login.service.test.ts` - NEW
- `src/services/auth/__tests__/password-reset.service.test.ts` - NEW
- `src/routes/auth/__tests__/login.integration.test.ts` - NEW
- `src/routes/auth/__tests__/password-reset.integration.test.ts` - NEW
- `src/middleware/__tests__/auth.middleware.test.ts` - NEW
- `tests/e2e/auth/login.e2e.test.ts` - NEW
- `tests/e2e/auth/password-reset.e2e.test.ts` - NEW

[Source: task-001-user-signup-validation.md#file-locations]

### Testing Requirements

**Testing Strategy:**
- **Framework:** Jest + Supertest for HTTP testing
- **Coverage Target:** >80% for all new code
- **Test Levels:** Unit, Integration, E2E

**Required Test Cases:**

**Login Endpoint:**
1. Happy path: Valid credentials return user + token (AC: 2, 3)
2. Invalid email format rejected with 400 (AC: 3)
3. Invalid password (wrong password) returns 401 (AC: 3)
4. Non-existent email returns 401 (AC: 3)
5. Token structure validated (contains userId, email, exp) (AC: 2)
6. Token expiration set correctly (AC: 2)
7. Password not included in response (AC: 2)

**Token Service:**
8. Token generation creates valid JWT (AC: 2)
9. Token verification succeeds for valid token (AC: 5)
10. Token verification fails for expired token (AC: 5)
11. Token verification fails for invalid signature (AC: 5)
12. Token decoding extracts correct payload (AC: 2, 5)

**Auth Middleware:**
13. Valid token allows request through (AC: 5)
14. Missing Authorization header returns 401 (AC: 5)
15. Invalid token format returns 401 (AC: 5)
16. Expired token returns 401 (AC: 5)
17. User object attached to request (AC: 5)

**Password Reset:**
18. Reset request creates token and returns success (AC: 4)
19. Reset request for non-existent email still returns success (security) (AC: 4, 6)
20. Reset confirm with valid token updates password (AC: 4)
21. Reset confirm with expired token returns 401 (AC: 4)
22. Reset confirm with used token returns 401 (AC: 4)
23. Reset token cannot be reused after successful reset (AC: 4)
24. Old password no longer works after reset (AC: 4)
25. New password works after reset (AC: 4)

**Security:**
26. Rate limiting triggers after 5 login attempts (AC: 6)
27. Rate limiting triggers after 3 password reset requests (AC: 6)
28. Passwords never logged or exposed in errors (AC: 2, 6)

**Mock Strategy:**
- **Unit tests:** Mock repositories, mock bcrypt, mock JWT sign/verify
- **Integration tests:** Use test database, real JWT, real bcrypt
- **E2E tests:** Use test database with full setup/teardown, real services

[Source: docs/standards.md#testing-standards]

### Technical Constraints

**Performance:**
- API response time: <200ms for p95 (excluding bcrypt ~150ms for login)
- Database queries: Maximum 3 per request
- Token generation: <10ms (JWT is fast)
- Password reset token cleanup: Run daily cron job to delete expired tokens

**Security:**
- JWT secret: Store in environment variable, minimum 32 characters, randomly generated
- JWT expiration: 1 hour (configurable via env var)
- Password reset token expiration: 1 hour
- Password reset tokens: UUID v4 format, cryptographically random
- Never expose token secrets in logs or errors
- Rate limiting: 5 req/min for login, 3 req/min for password reset
- Error messages: Generic "Invalid credentials" (don't leak account existence)
- HTTPS required in production (not enforced in code, but documented requirement)

**Dependencies:**
- jsonwebtoken: ^9.x (JWT generation and verification)
- express-rate-limit: ^7.x (rate limiting middleware)
- uuid: ^9.x (password reset token generation)
- Existing: bcrypt ^5.x, Zod ^3.x, Prisma ^5.x, Jest ^29.x

[Source: docs/standards.md#security-standards, docs/standards.md#performance-standards]

---

## Tasks / Subtasks

<!-- Sequential tasks with clear validation points -->
<!-- Each task should reference applicable acceptance criteria -->
<!-- Check off boxes as implementation progresses -->

- [ ] **Task 1:** Create JWT token service and types (AC: 2, 3, 5)
  - [ ] Install dependencies: `jsonwebtoken`, `@types/jsonwebtoken`
  - [ ] Add JWT_SECRET and JWT_EXPIRATION to `.env` file
  - [ ] Create `src/types/auth.ts` with TokenPayload and TokenResponse interfaces
  - [ ] Create `src/services/auth/token.service.ts` with methods:
    - [ ] `generateToken(userId: string, email: string): TokenResponse`
    - [ ] `verifyToken(token: string): TokenPayload | null`
    - [ ] `decodeToken(token: string): TokenPayload | null`
  - [ ] Write comprehensive unit tests in `src/services/auth/__tests__/token.service.test.ts`
  - [ ] Test cases: generation, verification, expiration, invalid signature
  - [ ] **Validate:** All token operations working, tests passing

- [ ] **Task 2:** Implement login service (AC: 2, 3)
  - [ ] Extend `src/types/auth.ts` with LoginRequest and LoginResponse types
  - [ ] Extend `src/schemas/auth.schema.ts` with loginSchema (email + password validation)
  - [ ] Create `src/services/auth/login.service.ts` with method:
    - [ ] `authenticateUser(email: string, password: string): Promise<LoginResponse>`
    - [ ] Look up user by email using user.repository.findByEmail
    - [ ] Verify password with bcrypt.compare
    - [ ] Generate JWT token using token.service.generateToken
    - [ ] Return user (without password) + token + expiresIn
    - [ ] Handle errors: user not found (401), invalid password (401), database error (500)
  - [ ] Write comprehensive unit tests with mocked dependencies
  - [ ] Test cases: successful login, invalid credentials, non-existent user, database error
  - [ ] **Validate:** Service logic correct, all error cases handled, tests passing

- [ ] **Task 3:** Create login API endpoint (AC: 3)
  - [ ] Create `src/routes/auth/login.ts` route handler
  - [ ] Add request validation middleware using loginSchema
  - [ ] Connect route to login.service.authenticateUser
  - [ ] Format success response: 200 with user + token + expiresIn
  - [ ] Format error responses: 400 (validation), 401 (invalid credentials), 500 (server error)
  - [ ] Register route in `src/routes/auth/index.ts`: `router.post('/login', ...)`
  - [ ] Write integration tests in `src/routes/auth/__tests__/login.integration.test.ts`
  - [ ] Use Supertest to test endpoint with test database
  - [ ] Test cases: valid login, invalid format, wrong password, non-existent email
  - [ ] **Validate:** Endpoint working, responses match specification, tests passing

- [ ] **Task 4:** Implement authentication middleware (AC: 5)
  - [ ] Create `src/middleware/auth.middleware.ts`
  - [ ] Implement `verifyToken` middleware function:
    - [ ] Extract token from Authorization header (`Bearer <token>`)
    - [ ] Verify token using token.service.verifyToken
    - [ ] Attach user payload to request object (req.user = payload)
    - [ ] Call next() on success
    - [ ] Return 401 on missing/invalid/expired token
  - [ ] Add TypeScript types for extended Request interface (req.user)
  - [ ] Write unit tests in `src/middleware/__tests__/auth.middleware.test.ts`
  - [ ] Test cases: valid token, missing header, invalid token, expired token, malformed header
  - [ ] **Validate:** Middleware correctly protects routes, tests passing

- [ ] **Task 5:** Implement password reset request flow (AC: 4)
  - [ ] Run Prisma migration: Add PasswordReset model to schema, run `prisma migrate dev`
  - [ ] Create `src/repositories/password-reset.repository.ts` with methods:
    - [ ] `createReset(userId: string, token: string, expiresAt: Date): Promise<PasswordReset>`
    - [ ] `findByToken(token: string): Promise<PasswordReset | null>`
    - [ ] `markUsed(id: string): Promise<void>`
  - [ ] Install dependency: `uuid` for token generation
  - [ ] Create `src/services/auth/password-reset.service.ts` with method:
    - [ ] `requestReset(email: string): Promise<{ message: string }>`
    - [ ] Look up user by email (if not found, still return success - security)
    - [ ] Generate UUID token
    - [ ] Calculate expiration (1 hour from now)
    - [ ] Store token in password_resets table
    - [ ] Log "Password reset email would be sent" (mock email service)
    - [ ] Return generic success message
  - [ ] Write unit tests for service and repository
  - [ ] **Validate:** Reset request flow working, token stored correctly, tests passing

- [ ] **Task 6:** Implement password reset confirmation flow (AC: 4)
  - [ ] Extend `src/repositories/user.repository.ts` with method:
    - [ ] `updatePassword(userId: string, hashedPassword: string): Promise<void>`
  - [ ] Extend `src/schemas/auth.schema.ts` with passwordResetConfirmSchema (token + newPassword)
  - [ ] Extend `src/services/auth/password-reset.service.ts` with method:
    - [ ] `confirmReset(token: string, newPassword: string): Promise<{ message: string }>`
    - [ ] Find password reset by token
    - [ ] Validate: token exists, not expired, not used
    - [ ] Hash new password with bcrypt (cost 12)
    - [ ] Update user password using user.repository.updatePassword
    - [ ] Mark token as used using password-reset.repository.markUsed
    - [ ] Return success message
  - [ ] Create `src/routes/auth/password-reset.ts` with both endpoints:
    - [ ] POST /request (calls requestReset)
    - [ ] POST /confirm (calls confirmReset)
  - [ ] Register routes in `src/routes/auth/index.ts`
  - [ ] Write integration tests for both endpoints
  - [ ] Test full flow: request → confirm → old password fails → new password works
  - [ ] **Validate:** Complete password reset flow working, tests passing

- [ ] **Task 7:** Add rate limiting and security hardening (AC: 6)
  - [ ] Install dependency: `express-rate-limit`
  - [ ] Create `src/middleware/rate-limit.middleware.ts` with configurations:
    - [ ] authRateLimiter: 5 requests per minute (for login, signup)
    - [ ] passwordResetRateLimiter: 3 requests per minute
  - [ ] Apply authRateLimiter to:
    - [ ] POST /api/auth/signup (task-001)
    - [ ] POST /api/auth/login
  - [ ] Apply passwordResetRateLimiter to:
    - [ ] POST /api/auth/password-reset/request
    - [ ] POST /api/auth/password-reset/confirm
  - [ ] Test rate limiting behavior (manual or integration test)
  - [ ] Verify error messages don't leak sensitive information
  - [ ] **Validate:** Rate limiting active, security hardened, no information leakage

- [ ] **Task 8:** E2E testing and validation (AC: all)
  - [ ] Create `tests/e2e/auth/login.e2e.test.ts`:
    - [ ] Test complete login flow: signup → login → receive token → use token on protected route
    - [ ] Test invalid credentials flow
  - [ ] Create `tests/e2e/auth/password-reset.e2e.test.ts`:
    - [ ] Test complete password reset flow: request → confirm → login with new password
    - [ ] Test expired token scenario
    - [ ] Test token reuse prevention
  - [ ] Run full test suite: `npm test`
  - [ ] Check coverage: `npm run test:coverage`
  - [ ] Verify coverage ≥80% for new code
  - [ ] Manually verify all 6 acceptance criteria
  - [ ] **Validate:** All tests passing, coverage targets met, all AC verified

- [ ] **Final Validation:**
  - [ ] All 6 acceptance criteria verified and documented
  - [ ] All tests passing (unit + integration + E2E)
  - [ ] Code coverage ≥80% for new code
  - [ ] Rate limiting active on all auth endpoints
  - [ ] No passwords or secrets logged
  - [ ] Error messages generic (no information leakage)
  - [ ] JWT tokens working for protected routes
  - [ ] Code follows TypeScript strict mode and project standards

---

## Implementation Record

<!-- IMPORTANT: This section is ONLY modified by implementation skill -->
<!-- Planning skill does NOT populate this section -->

### Agent Model Used

*To be filled during implementation*

### Debug Log References

*To be filled during implementation*

### Completion Notes

*To be filled during implementation*

### Files Modified

*To be filled during implementation*

### Testing Results

*To be filled during implementation*

---

## Quality Review

<!-- IMPORTANT: This section is ONLY modified by quality skill -->
<!-- Populated after implementation is marked "Ready for Review" -->

### Review Date

*To be filled during quality review*

### Reviewer

*To be filled during quality review*

### Quality Gate Decision

*To be filled during quality review*

### Quality Gate File

*To be filled during quality review*

### Summary

*To be filled during quality review*

---

## Change Log

<!-- Track changes to this task specification -->

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2025-10-31 | 1.0 | Initial task specification created for Session 6 validation | create-task-spec-skill-v1.0 |

---

<!-- End of Task Specification -->
