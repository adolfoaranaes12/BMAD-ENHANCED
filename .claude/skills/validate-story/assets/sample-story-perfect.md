---
epic_id: "epic-001"
story_id: "story-003"
title: "User Authentication System"
status: "Draft"
created: "2025-01-15"
---

# Story 1.3: User Authentication System

## Objective

Implement secure user authentication system with JWT tokens, password hashing, and session management to enable users to register, log in, and maintain secure sessions.

## Context

The application currently has no authentication mechanism. Users cannot create accounts or securely access the system. This story implements the foundational authentication layer that all future user-specific features will depend on. This is the first story in the User Management epic and must be completed before stories 1.4 (User Profiles) and 1.5 (Password Reset).

## Acceptance Criteria

**AC1:** User can register with valid email and password
- Email must be unique and follow standard email format
- Password must be at least 8 characters with uppercase, lowercase, and number
- Registration creates user record in database
- Password is hashed with bcrypt before storage

**AC2:** User can log in with correct credentials
- Login accepts email and password
- Returns JWT access token (1-hour expiry) and refresh token (7-day expiry)
- Failed login returns 401 Unauthorized with appropriate error message
- Successful login updates lastLoginAt timestamp

**AC3:** User can log out
- Logout invalidates refresh token in Redis
- Client discards access token
- Returns 200 OK on successful logout

**AC4:** Secure password storage
- All passwords hashed with bcrypt, salt rounds 10
- No plaintext passwords in database or logs
- Password hash never returned in API responses

**AC5:** Session management with token refresh
- Access tokens expire after 1 hour
- Refresh tokens expire after 7 days
- Client can refresh access token using valid refresh token
- Refresh token rotation on each use

## Tasks/Subtasks

**Task 1: Database Schema and Models**
1.1. Create users table migration (email, passwordHash, createdAt, lastLoginAt)
1.2. Create User model with Sequelize
1.3. Add unique constraint on email field
1.4. Create database indexes on email for query performance

**Task 2: Password Hashing Service**
2.1. Install bcrypt dependency (npm install bcrypt)
2.2. Create PasswordService class with hash() and compare() methods
2.3. Configure bcrypt salt rounds (10) in environment config
2.4. Add unit tests for PasswordService

**Task 3: JWT Token Service**
3.1. Install jsonwebtoken and dotenv dependencies
3.2. Create TokenService class with generateAccessToken() and generateRefreshToken()
3.3. Configure JWT secret in .env file
3.4. Implement token verification middleware
3.5. Add unit tests for TokenService

**Task 4: User Registration Endpoint**
4.1. Create POST /api/auth/register endpoint
4.2. Add Joi validation schema (email format, password strength)
4.3. Check for duplicate email before creating user
4.4. Hash password using PasswordService
4.5. Create user record in database
4.6. Return 201 Created with user data (exclude passwordHash)

**Task 5: User Login Endpoint**
5.1. Create POST /api/auth/login endpoint
5.2. Add Joi validation for email and password
5.3. Find user by email
5.4. Verify password using PasswordService.compare()
5.5. Generate access token and refresh token
5.6. Store refresh token in Redis with 7-day TTL
5.7. Update lastLoginAt timestamp
5.8. Return 200 OK with tokens

**Task 6: Logout Endpoint**
6.1. Create POST /api/auth/logout endpoint
6.2. Extract refresh token from request body
6.3. Delete refresh token from Redis
6.4. Return 200 OK

**Task 7: Token Refresh Endpoint**
7.1. Create POST /api/auth/refresh endpoint
7.2. Verify refresh token from Redis
7.3. Generate new access token and refresh token
7.4. Rotate refresh token (delete old, store new)
7.5. Return 200 OK with new tokens

**Task 8: Authentication Middleware**
8.1. Create requireAuth middleware
8.2. Extract access token from Authorization header
8.3. Verify token using TokenService
8.4. Attach user data to req.user
8.5. Return 401 if token invalid or expired

**Task 9: Rate Limiting**
9.1. Install express-rate-limit dependency
9.2. Configure rate limiter (100 requests per 15 minutes)
9.3. Apply to /api/auth/* endpoints
9.4. Return 429 Too Many Requests when limit exceeded

**Task 10: Integration Tests**
10.1. Test user registration flow (valid and invalid inputs)
10.2. Test login flow (correct/incorrect credentials)
10.3. Test logout flow
10.4. Test token refresh flow
10.5. Test authentication middleware (valid/invalid/expired tokens)

**Task 11: Error Handling**
11.1. Standardize error response format {error: {code, message}}
11.2. Handle duplicate email error (409 Conflict)
11.3. Handle invalid credentials error (401 Unauthorized)
11.4. Handle expired token error (401 Unauthorized)

**Task 12: Documentation**
12.1. Add JSDoc comments to all service classes
12.2. Update API documentation with auth endpoints
12.3. Document authentication flow in README

## Dev Notes

### Technical Implementation Approach

**Architecture:**
- RESTful API endpoints under /api/auth/
- Service layer pattern: PasswordService, TokenService
- Repository pattern: UserRepository for database access
- Middleware: Authentication and rate limiting

**Key Technical Decisions:**
1. **JWT Strategy:** Short-lived access tokens (1 hour) with longer refresh tokens (7 days)
   - Access tokens: Stateless, verified via signature
   - Refresh tokens: Stored in Redis for revocation capability

2. **Password Security:** bcrypt with salt rounds 10
   - Industry standard, slow hashing protects against brute force
   - Salt rounds configurable via env var for future adjustment

3. **Token Storage:**
   - Access tokens: Client-side only (localStorage or memory)
   - Refresh tokens: Redis with automatic expiry (7-day TTL)

4. **Database:** PostgreSQL with Sequelize ORM
   - Users table with email unique constraint
   - Indexes on email for login query performance

### Integration Points

1. **Redis Connection:**
   - Used for refresh token storage
   - Configured in src/config/redis.ts
   - Existing Redis instance, no new setup needed

2. **Sequelize Connection:**
   - Add User model to existing Sequelize setup
   - Migration will run with other migrations (npm run migrate)

3. **Express App:**
   - Mount auth routes at /api/auth
   - Apply global error handler middleware

### File Structure

```
src/
├── models/
│   └── User.ts                 (New: Sequelize User model)
├── services/
│   ├── PasswordService.ts      (New: bcrypt wrapper)
│   └── TokenService.ts         (New: JWT generation/verification)
├── routes/
│   └── auth.routes.ts          (New: /register, /login, /logout, /refresh)
├── middleware/
│   ├── authenticate.ts         (New: JWT verification middleware)
│   └── rateLimiter.ts          (New: Rate limiting config)
├── controllers/
│   └── AuthController.ts       (New: Request handlers)
└── config/
    └── jwt.ts                  (New: JWT configuration)

tests/
├── unit/
│   ├── PasswordService.test.ts
│   └── TokenService.test.ts
└── integration/
    └── auth.routes.test.ts

migrations/
└── 20250115-create-users-table.js

.env
└── Add: JWT_SECRET, JWT_ACCESS_EXPIRY, JWT_REFRESH_EXPIRY, BCRYPT_SALT_ROUNDS
```

### Potential Gotchas

1. **JWT Secret:** Must be strong random string (min 32 characters)
   - Generate with: `openssl rand -base64 32`
   - Store in .env, never commit to git

2. **Bcrypt Performance:** Bcrypt is intentionally slow
   - May need to increase test timeouts
   - Salt rounds 10 is good balance (speed vs security)

3. **Token Expiry Timing:** Client must handle token refresh
   - Implement token refresh before expiry (e.g., at 50 minutes)
   - Handle 401 gracefully and redirect to login

4. **Redis Connection:** Ensure Redis running locally
   - Start with: `redis-server`
   - Docker: `docker run -p 6379:6379 redis`

5. **Race Conditions:** Token refresh can have races
   - Implement token rotation to handle refresh token reuse
   - Short grace period for old refresh tokens

## Testing & Validation

### Test Strategy

**Unit Tests (Jest):**
- PasswordService.hash() and compare() methods
- TokenService.generate() and verify() methods
- Input validation schemas

**Integration Tests (Jest + Supertest):**
- Full auth flow: register → login → use protected endpoint → logout
- Error scenarios: invalid inputs, duplicate emails, wrong passwords
- Token lifecycle: generation, verification, expiry, refresh

**Security Tests:**
- Verify passwords never returned in responses
- Verify JWTs signed correctly
- Verify rate limiting works

### Test Scenarios

**Registration:**
- ✅ Valid email and password → 201 Created
- ❌ Invalid email format → 400 Bad Request
- ❌ Weak password (< 8 chars) → 400 Bad Request
- ❌ Duplicate email → 409 Conflict

**Login:**
- ✅ Correct credentials → 200 OK with tokens
- ❌ Wrong password → 401 Unauthorized
- ❌ Non-existent email → 401 Unauthorized
- ❌ Missing fields → 400 Bad Request

**Protected Endpoints:**
- ✅ Valid access token → 200 OK
- ❌ No token → 401 Unauthorized
- ❌ Invalid token → 401 Unauthorized
- ❌ Expired token → 401 Unauthorized

**Token Refresh:**
- ✅ Valid refresh token → 200 OK with new tokens
- ❌ Invalid refresh token → 401 Unauthorized
- ❌ Expired refresh token → 401 Unauthorized

**Logout:**
- ✅ Valid refresh token → 200 OK
- ✅ Token invalidated after logout → 401 on reuse

### Validation Steps

1. Run unit tests: `npm run test:unit`
   - All PasswordService tests pass
   - All TokenService tests pass
   - Coverage ≥ 80%

2. Run integration tests: `npm run test:integration`
   - All auth flow tests pass
   - All error scenario tests pass

3. Manual testing with Postman:
   - Register new user
   - Log in with credentials
   - Access protected endpoint with token
   - Refresh token before expiry
   - Log out and verify token invalidated

4. Security verification:
   - Check database: passwordHash present, no plaintext passwords
   - Check responses: no passwordHash in JSON
   - Check logs: no passwords logged

### Testing Tools

- **Jest:** Test framework
- **Supertest:** HTTP assertion library
- **faker:** Generate test data (emails, passwords)
- **Postman:** Manual API testing

## File List

**New Files:**
- src/models/User.ts
- src/services/PasswordService.ts
- src/services/TokenService.ts
- src/routes/auth.routes.ts
- src/middleware/authenticate.ts
- src/middleware/rateLimiter.ts
- src/controllers/AuthController.ts
- src/config/jwt.ts
- tests/unit/PasswordService.test.ts
- tests/unit/TokenService.test.ts
- tests/integration/auth.routes.test.ts
- migrations/20250115-create-users-table.js

**Modified Files:**
- src/app.ts (mount auth routes)
- .env (add JWT_SECRET, etc.)
- package.json (add dependencies: bcrypt, jsonwebtoken, express-rate-limit)

## Dependencies

**External:**
- bcrypt ^5.1.0 (password hashing)
- jsonwebtoken ^9.0.0 (JWT generation/verification)
- express-rate-limit ^6.7.0 (rate limiting)
- joi ^17.7.0 (input validation) - already installed
- ioredis ^5.3.0 (Redis client) - already installed

**Internal:**
- None (first story in epic, no dependencies)

**System:**
- Node.js ≥ 16.0.0
- PostgreSQL ≥ 13.0
- Redis ≥ 6.0

## Security Considerations

**Authentication:**
- JWT-based authentication with short-lived access tokens
- Refresh token rotation to prevent token reuse attacks
- Tokens stored in Redis for revocation capability

**Password Security:**
- Bcrypt hashing with salt rounds 10
- Password strength validation (min 8 chars, complexity requirements)
- No plaintext passwords in database, logs, or responses

**Input Validation:**
- Joi schemas for all inputs
- Email format validation
- Password strength validation
- Sanitization of user inputs

**Rate Limiting:**
- 100 requests per 15 minutes per IP
- Prevents brute force attacks on login/register

**Data Protection:**
- HTTPS enforced in production (configured in reverse proxy)
- JWT secret stored in environment variable
- Sensitive data never logged

**Vulnerability Prevention:**
- SQL injection: Sequelize ORM with parameterized queries
- XSS: Input sanitization, output encoding
- CSRF: Not applicable (stateless JWT auth)

---

*Story Template Version: 1.0*
*Created: 2025-01-15*
*Last Updated: 2025-01-15*
