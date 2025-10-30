# Implement Feature Skill

## Purpose
Implement features from task specifications or user stories using test-driven development (TDD). This skill writes tests first, implements code to make tests pass, and validates the implementation meets all acceptance criteria.

## When to Use This Skill
- Implementing features from task specifications
- Implementing user stories from sprints
- Building new functionality based on requirements
- Converting designs/mockups into working code
- Test-driven development of any feature

## Invocation
```bash
# From task specification
@james *implement task-auth-002-login

# From user story
@james *implement story-auth-001

# From description (creates implicit task)
@james *implement "Add logout button to navbar"

# With options
@james *implement task-auth-002 --skip-tests
@james *implement task-auth-002 --tdd=false
```

## Prerequisites
- Task specification exists (for task-based) OR
- User story exists (for story-based) OR
- Clear feature description (for ad-hoc)
- Development environment set up
- Test framework configured
- Dependencies installed

## Skill Configuration
```yaml
skill_name: implement-feature
version: 1.0.0
subagent: james-developer
execution_mode: sequential
halt_on_error: true
output_directory: (project root)
```

---

## STEP 0: Load Configuration and Task Context

### Actions
1. Validate input (task ID, story ID, or description)
2. Load configuration from `.claude/config.yaml`
3. Load task specification or story file
4. Verify task status is "Approved" or story is "Ready"
5. Initialize implementation framework

### Input Validation

**Task ID Format:**
```
task-{component}-{number}-{slug}

Examples:
- task-auth-002-login
- task-ui-015-logout-button
- task-api-042-user-endpoint
```

**Story ID Format:**
```
story-{component}-{number}-{slug}

Examples:
- story-auth-001-signup
- story-payment-005-stripe
```

### Load Task Specification

**From:** `.claude/tasks/{task-id}.md` or `.claude/stories/{story-id}.md`

**Required Sections:**
- Objective (what to build)
- Acceptance Criteria (testable requirements)
- Context (technical details, data models, APIs)
- Tasks / Subtasks (sequential steps)

**Example Task:**
```markdown
# Task: User Login Endpoint

**ID:** task-auth-002-login
**Status:** Approved
**Priority:** P0

## Objective
As a registered user, I want to log in with my email and password
so that I can access my personalized account.

## Acceptance Criteria
- AC-1: User can submit email and password to POST /api/auth/login
- AC-2: Valid credentials return 200 with JWT token
- AC-3: Invalid credentials return 401 with "Invalid credentials"
- AC-4: Missing fields return 400 with validation errors
- AC-5: Rate limiting: 5 attempts per 10 minutes
- AC-6: JWT token expires after 24 hours
- AC-7: Successful login is logged for security audit

## Context

**Technology Stack:**
- Node.js 20 + TypeScript
- Express.js
- bcrypt (password hashing)
- jsonwebtoken (JWT)
- Zod (validation)
- Jest (testing)

**Data Models:**
users table:
  - id: UUID
  - email: VARCHAR(254)
  - password_hash: VARCHAR(60)
  - created_at: TIMESTAMP

**API Specification:**
POST /api/auth/login
Request: { email: string, password: string }
Response: { token: string, expiresIn: number }
```

### Load Configuration

From `.claude/config.yaml`:
```yaml
developer:
  test_framework: jest
  tdd_enabled: true
  coverage_threshold: 80
  linter: eslint
  formatter: prettier

project:
  source_directory: src
  test_directory: src/__tests__
```

---

## STEP 1: Analyze Requirements

### Actions
1. Parse all acceptance criteria
2. Identify testable requirements
3. Analyze technical context
4. Identify files to create/modify
5. Determine test strategy
6. Estimate implementation steps

### Parse Acceptance Criteria

**For each AC, identify:**
- What to test (behavior/outcome)
- How to test (unit, integration, E2E)
- Test data needed
- Expected result

**Example Analysis:**

```markdown
AC-1: User can submit email and password to POST /api/auth/login

Test Type: Integration
Test: HTTP request to POST /api/auth/login
Test Data: { email: "test@example.com", password: "SecurePass123!" }
Expected: Request accepted (200 or 401, but not 404)

---

AC-2: Valid credentials return 200 with JWT token

Test Type: Integration
Test: POST with valid credentials
Test Data: Email/password for existing user
Expected: 200 status, body contains { token: string, expiresIn: number }

---

AC-3: Invalid credentials return 401 with "Invalid credentials"

Test Type: Integration
Test: POST with wrong password OR non-existent email
Test Data: Wrong password: { email: "exists@example.com", password: "WrongPass" }
Expected: 401 status, body contains { error: "Invalid credentials" }

---

AC-4: Missing fields return 400 with validation errors

Test Type: Integration
Test: POST with missing email or password
Test Data: { email: "test@example.com" } (missing password)
Expected: 400 status, body contains validation error message

---

AC-5: Rate limiting: 5 attempts per 10 minutes

Test Type: Integration
Test: Make 6 rapid requests
Expected: First 5 attempts processed (200/401), 6th returns 429

---

AC-6: JWT token expires after 24 hours

Test Type: Unit
Test: Decode generated token, check exp claim
Expected: exp = iat + 86400 seconds (24 hours)

---

AC-7: Successful login is logged for security audit

Test Type: Integration
Test: Successful login, check logs
Expected: Log entry with { userId, ip, timestamp, success: true }
```

### Identify Files to Create/Modify

**Based on analysis:**

```yaml
Files to Create:
  - src/controllers/auth.controller.ts (login handler)
  - src/services/auth.service.ts (business logic)
  - src/middleware/rate-limit.ts (rate limiting)
  - src/utils/jwt.ts (JWT utilities)
  - src/__tests__/controllers/auth.controller.test.ts (tests)
  - src/__tests__/integration/auth.integration.test.ts (integration tests)

Files to Modify:
  - src/routes/auth.routes.ts (add login route)
  - src/app.ts (if needed for middleware)

Files to Reference:
  - src/models/user.model.ts (existing user model)
  - src/config/database.ts (existing DB connection)
```

### Determine Test Strategy

```markdown
**Unit Tests (5 tests):**
1. auth.service.findUserByEmail - returns user when exists
2. auth.service.findUserByEmail - returns null when not exists
3. auth.service.verifyPassword - returns true for correct password
4. auth.service.verifyPassword - returns false for incorrect password
5. jwt.generateToken - generates valid token with correct expiration

**Integration Tests (7 tests):**
1. POST /api/auth/login - 200 with token for valid credentials
2. POST /api/auth/login - 401 for wrong password
3. POST /api/auth/login - 401 for non-existent email
4. POST /api/auth/login - 400 for missing email
5. POST /api/auth/login - 400 for missing password
6. POST /api/auth/login - 400 for invalid email format
7. POST /api/auth/login - 429 after 5 failed attempts

**Total: 12 tests**
```

---

## STEP 2: Set Up Test Framework

### Actions
1. Create test files
2. Set up mocks for dependencies
3. Write test scaffolding
4. Configure test environment

### Create Test Files

**Unit Test File:** `src/__tests__/services/auth.service.test.ts`

```typescript
import { describe, it, expect, jest, beforeEach } from '@jest/globals';
import { AuthService } from '../../services/auth.service';
import { User } from '../../models/user.model';
import bcrypt from 'bcrypt';

describe('[Unit] AuthService', () => {
  let authService: AuthService;

  beforeEach(() => {
    authService = new AuthService();
    jest.clearAllMocks();
  });

  describe('findUserByEmail', () => {
    it('should return user when email exists', async () => {
      // Test will go here
    });

    it('should return null when email does not exist', async () => {
      // Test will go here
    });
  });

  describe('verifyPassword', () => {
    it('should return true for correct password', async () => {
      // Test will go here
    });

    it('should return false for incorrect password', async () => {
      // Test will go here
    });
  });
});
```

**Integration Test File:** `src/__tests__/integration/auth.integration.test.ts`

```typescript
import { describe, it, expect, beforeAll, afterAll } from '@jest/globals';
import request from 'supertest';
import app from '../../app';
import { User } from '../../models/user.model';
import { setupTestDatabase, teardownTestDatabase } from '../helpers/db';

describe('[Integration] POST /api/auth/login', () => {
  beforeAll(async () => {
    await setupTestDatabase();
    // Create test user
    await User.create({
      email: 'test@example.com',
      password: await bcrypt.hash('SecurePass123!', 12)
    });
  });

  afterAll(async () => {
    await teardownTestDatabase();
  });

  it('should return 200 and JWT token for valid credentials', async () => {
    // Test will go here
  });

  it('should return 401 for wrong password', async () => {
    // Test will go here
  });

  // ... more tests
});
```

### Set Up Mocks

```typescript
// Mock database
jest.mock('../../models/user.model', () => ({
  User: {
    findByEmail: jest.fn(),
    create: jest.fn(),
  }
}));

// Mock bcrypt
jest.mock('bcrypt', () => ({
  compare: jest.fn(),
  hash: jest.fn(),
}));

// Mock JWT
jest.mock('jsonwebtoken', () => ({
  sign: jest.fn(() => 'mock.jwt.token'),
  verify: jest.fn(),
}));
```

---

## STEP 3: Write Tests (TDD - Red Phase)

### Actions
1. Write unit tests (simplest first)
2. Write integration tests
3. Run tests (should all fail)
4. Verify test failures are correct

### Write Unit Tests

**Test 1: findUserByEmail - user exists**

```typescript
it('should return user when email exists', async () => {
  const mockUser = {
    id: '123',
    email: 'test@example.com',
    password_hash: 'hashed_password'
  };

  (User.findByEmail as jest.Mock).mockResolvedValue(mockUser);

  const result = await authService.findUserByEmail('test@example.com');

  expect(result).toEqual(mockUser);
  expect(User.findByEmail).toHaveBeenCalledWith('test@example.com');
});
```

**Test 2: findUserByEmail - user does not exist**

```typescript
it('should return null when email does not exist', async () => {
  (User.findByEmail as jest.Mock).mockResolvedValue(null);

  const result = await authService.findUserByEmail('nonexistent@example.com');

  expect(result).toBeNull();
});
```

**Test 3: verifyPassword - correct password**

```typescript
it('should return true for correct password', async () => {
  (bcrypt.compare as jest.Mock).mockResolvedValue(true);

  const result = await authService.verifyPassword('password123', 'hashed_password');

  expect(result).toBe(true);
  expect(bcrypt.compare).toHaveBeenCalledWith('password123', 'hashed_password');
});
```

**Test 4: verifyPassword - incorrect password**

```typescript
it('should return false for incorrect password', async () => {
  (bcrypt.compare as jest.Mock).mockResolvedValue(false);

  const result = await authService.verifyPassword('wrongpassword', 'hashed_password');

  expect(result).toBe(false);
});
```

**Test 5: generateToken - valid token with expiration**

```typescript
it('should generate JWT token with 24-hour expiration', () => {
  const userId = '123';
  const token = jwtUtils.generateToken(userId);

  expect(jwt.sign).toHaveBeenCalledWith(
    { userId },
    expect.any(String),
    { expiresIn: '24h' }
  );
  expect(token).toBe('mock.jwt.token');
});
```

### Write Integration Tests

**Test 1: Valid credentials**

```typescript
it('should return 200 and JWT token for valid credentials', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'test@example.com',
      password: 'SecurePass123!'
    });

  expect(response.status).toBe(200);
  expect(response.body).toHaveProperty('token');
  expect(response.body).toHaveProperty('expiresIn', 86400);
  expect(typeof response.body.token).toBe('string');
});
```

**Test 2: Wrong password**

```typescript
it('should return 401 for wrong password', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'test@example.com',
      password: 'WrongPassword!'
    });

  expect(response.status).toBe(401);
  expect(response.body).toHaveProperty('error', 'Invalid credentials');
  expect(response.body).toHaveProperty('code', 'AUTH_INVALID_CREDENTIALS');
});
```

**Test 3: Non-existent email**

```typescript
it('should return 401 for non-existent email', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'nonexistent@example.com',
      password: 'SomePassword123!'
    });

  expect(response.status).toBe(401);
  expect(response.body).toHaveProperty('error', 'Invalid credentials');
});
```

**Test 4: Missing email**

```typescript
it('should return 400 for missing email', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      password: 'SecurePass123!'
    });

  expect(response.status).toBe(400);
  expect(response.body).toHaveProperty('error');
  expect(response.body.error).toContain('email');
});
```

**Test 5: Missing password**

```typescript
it('should return 400 for missing password', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'test@example.com'
    });

  expect(response.status).toBe(400);
  expect(response.body).toHaveProperty('error');
  expect(response.body.error).toContain('password');
});
```

**Test 6: Invalid email format**

```typescript
it('should return 400 for invalid email format', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'not-an-email',
      password: 'SecurePass123!'
    });

  expect(response.status).toBe(400);
  expect(response.body).toHaveProperty('error');
  expect(response.body.error).toContain('email');
});
```

**Test 7: Rate limiting after 5 attempts**

```typescript
it('should return 429 after 5 failed attempts', async () => {
  // Make 5 failed attempts
  for (let i = 0; i < 5; i++) {
    await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'WrongPassword!'
      });
  }

  // 6th attempt should be rate limited
  const response = await request(app)
    .post('/api/auth/login')
    .send({
      email: 'test@example.com',
      password: 'WrongPassword!'
    });

  expect(response.status).toBe(429);
  expect(response.body).toHaveProperty('error');
  expect(response.body.error).toContain('rate limit');
});
```

### Run Tests (Verify All Fail)

```bash
npm test auth
```

**Expected Output:**
```
FAIL src/__tests__/services/auth.service.test.ts
  ✕ should return user when email exists (5 ms)
  ✕ should return null when email does not exist (3 ms)
  ✕ should return true for correct password (2 ms)
  ✕ should return false for incorrect password (2 ms)
  ✕ should generate JWT token with 24-hour expiration (1 ms)

FAIL src/__tests__/integration/auth.integration.test.ts
  ✕ should return 200 and JWT token for valid credentials (15 ms)
  ✕ should return 401 for wrong password (12 ms)
  ✕ should return 401 for non-existent email (11 ms)
  ✕ should return 400 for missing email (10 ms)
  ✕ should return 400 for missing password (10 ms)
  ✕ should return 400 for invalid email format (10 ms)
  ✕ should return 429 after 5 failed attempts (18 ms)

Test Suites: 2 failed, 2 total
Tests:       12 failed, 12 total
```

**This is expected! TDD Red Phase complete.**

---

## STEP 4: Implement Code (TDD - Green Phase)

### Actions
1. Implement simplest code to make tests pass
2. Start with unit tests (easier)
3. Then integration tests
4. Refactor as needed
5. Keep tests passing

### Implement Service Layer

**File:** `src/services/auth.service.ts`

```typescript
import { User } from '../models/user.model';
import bcrypt from 'bcrypt';

export class AuthService {
  /**
   * Find user by email address
   */
  async findUserByEmail(email: string): Promise<User | null> {
    return await User.findByEmail(email);
  }

  /**
   * Verify password against hash
   */
  async verifyPassword(password: string, passwordHash: string): Promise<boolean> {
    return await bcrypt.compare(password, passwordHash);
  }

  /**
   * Authenticate user with email and password
   * Returns user if credentials are valid, null otherwise
   */
  async authenticateUser(email: string, password: string): Promise<User | null> {
    const user = await this.findUserByEmail(email);
    if (!user) {
      return null;
    }

    const isPasswordValid = await this.verifyPassword(password, user.password_hash);
    if (!isPasswordValid) {
      return null;
    }

    return user;
  }
}
```

**Run unit tests:**
```bash
npm test auth.service.test.ts
```

**Expected:**
```
PASS src/__tests__/services/auth.service.test.ts
  ✓ should return user when email exists (5 ms)
  ✓ should return null when email does not exist (3 ms)
  ✓ should return true for correct password (2 ms)
  ✓ should return false for incorrect password (2 ms)

Tests: 4 passed, 4 total
```

### Implement JWT Utilities

**File:** `src/utils/jwt.ts`

```typescript
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'dev_secret_change_in_production';
const JWT_EXPIRES_IN = '24h';

export interface TokenPayload {
  userId: string;
}

/**
 * Generate JWT token for user
 */
export const generateToken = (userId: string): string => {
  return jwt.sign(
    { userId } as TokenPayload,
    JWT_SECRET,
    { expiresIn: JWT_EXPIRES_IN }
  );
};

/**
 * Verify and decode JWT token
 */
export const verifyToken = (token: string): TokenPayload => {
  return jwt.verify(token, JWT_SECRET) as TokenPayload;
};
```

**Run JWT test:**
```bash
npm test jwt.test.ts
```

**Expected:**
```
PASS src/__tests__/utils/jwt.test.ts
  ✓ should generate JWT token with 24-hour expiration (1 ms)

Tests: 1 passed, 1 total
```

### Implement Validation Schema

**File:** `src/schemas/auth.schema.ts`

```typescript
import { z } from 'zod';

export const loginSchema = z.object({
  email: z.string().email('Invalid email format'),
  password: z.string().min(1, 'Password is required'),
});

export type LoginInput = z.infer<typeof loginSchema>;
```

### Implement Controller

**File:** `src/controllers/auth.controller.ts`

```typescript
import { Request, Response } from 'express';
import { AuthService } from '../services/auth.service';
import { generateToken } from '../utils/jwt';
import { loginSchema } from '../schemas/auth.schema';
import { logLoginAttempt } from '../utils/audit';

const authService = new AuthService();

/**
 * POST /api/auth/login
 * Authenticate user and return JWT token
 */
export const login = async (req: Request, res: Response): Promise<Response> => {
  try {
    // Validate input
    const validationResult = loginSchema.safeParse(req.body);
    if (!validationResult.success) {
      return res.status(400).json({
        error: validationResult.error.errors[0].message,
        code: 'VALIDATION_ERROR'
      });
    }

    const { email, password } = validationResult.data;

    // Authenticate user
    const user = await authService.authenticateUser(email, password);
    if (!user) {
      // Log failed attempt
      await logLoginAttempt({
        email,
        ip: req.ip,
        success: false,
        timestamp: new Date()
      });

      return res.status(401).json({
        error: 'Invalid credentials',
        code: 'AUTH_INVALID_CREDENTIALS'
      });
    }

    // Generate token
    const token = generateToken(user.id);

    // Log successful attempt
    await logLoginAttempt({
      email,
      userId: user.id,
      ip: req.ip,
      success: true,
      timestamp: new Date()
    });

    // Return token
    return res.status(200).json({
      token,
      expiresIn: 86400 // 24 hours in seconds
    });

  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });
  }
};
```

### Implement Rate Limiting Middleware

**File:** `src/middleware/rate-limit.ts`

```typescript
import { Request, Response, NextFunction } from 'express';
import { RateLimiterMemory } from 'rate-limiter-flexible';

const rateLimiter = new RateLimiterMemory({
  points: 5, // 5 attempts
  duration: 600, // per 10 minutes
  blockDuration: 600, // block for 10 minutes
});

/**
 * Rate limit middleware for login attempts
 * Limits to 5 attempts per 10 minutes per IP
 */
export const loginRateLimiter = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    await rateLimiter.consume(req.ip);
    next();
  } catch (error) {
    res.status(429).json({
      error: 'Too many login attempts. Please try again later.',
      code: 'RATE_LIMIT_EXCEEDED'
    });
  }
};
```

### Wire Up Routes

**File:** `src/routes/auth.routes.ts`

```typescript
import { Router } from 'express';
import { login } from '../controllers/auth.controller';
import { loginRateLimiter } from '../middleware/rate-limit';

const router = Router();

router.post('/login', loginRateLimiter, login);

export default router;
```

**File:** `src/app.ts` (add route)

```typescript
import authRoutes from './routes/auth.routes';

// ... existing code

app.use('/api/auth', authRoutes);
```

### Run All Tests

```bash
npm test auth
```

**Expected:**
```
PASS src/__tests__/services/auth.service.test.ts
  ✓ should return user when email exists
  ✓ should return null when email does not exist
  ✓ should return true for correct password
  ✓ should return false for incorrect password

PASS src/__tests__/utils/jwt.test.ts
  ✓ should generate JWT token with 24-hour expiration

PASS src/__tests__/integration/auth.integration.test.ts
  ✓ should return 200 and JWT token for valid credentials
  ✓ should return 401 for wrong password
  ✓ should return 401 for non-existent email
  ✓ should return 400 for missing email
  ✓ should return 400 for missing password
  ✓ should return 400 for invalid email format
  ✓ should return 429 after 5 failed attempts

Test Suites: 3 passed, 3 total
Tests:       12 passed, 12 total
Snapshots:   0 total
Time:        2.456 s
```

**TDD Green Phase complete! All tests passing!**

---

## STEP 5: Refactor (TDD - Refactor Phase)

### Actions
1. Review code for improvements
2. Extract duplicated logic
3. Improve naming
4. Add comments where needed
5. Run tests after each refactor (must stay green)

### Refactoring Opportunities

**Before: Controller has logging logic**
```typescript
export const login = async (req: Request, res: Response): Promise<Response> => {
  // ... validation

  const user = await authService.authenticateUser(email, password);
  if (!user) {
    // Logging logic inline
    await logLoginAttempt({
      email,
      ip: req.ip,
      success: false,
      timestamp: new Date()
    });
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const token = generateToken(user.id);

  // Logging logic inline
  await logLoginAttempt({
    email,
    userId: user.id,
    ip: req.ip,
    success: true,
    timestamp: new Date()
  });

  return res.status(200).json({ token, expiresIn: 86400 });
};
```

**After: Extract logging to service**
```typescript
// auth.service.ts
export class AuthService {
  /**
   * Authenticate user and log attempt
   */
  async loginWithAudit(
    email: string,
    password: string,
    ip: string
  ): Promise<{ user: User | null; success: boolean }> {
    const user = await this.authenticateUser(email, password);

    await logLoginAttempt({
      email,
      userId: user?.id,
      ip,
      success: !!user,
      timestamp: new Date()
    });

    return { user, success: !!user };
  }
}

// auth.controller.ts
export const login = async (req: Request, res: Response): Promise<Response> => {
  try {
    const validationResult = loginSchema.safeParse(req.body);
    if (!validationResult.success) {
      return res.status(400).json({
        error: validationResult.error.errors[0].message,
        code: 'VALIDATION_ERROR'
      });
    }

    const { email, password } = validationResult.data;
    const { user, success } = await authService.loginWithAudit(email, password, req.ip);

    if (!success) {
      return res.status(401).json({
        error: 'Invalid credentials',
        code: 'AUTH_INVALID_CREDENTIALS'
      });
    }

    const token = generateToken(user!.id);

    return res.status(200).json({
      token,
      expiresIn: 86400
    });

  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });
  }
};
```

**Run tests after refactor:**
```bash
npm test auth
```

**Expected:**
```
PASS src/__tests__/services/auth.service.test.ts
PASS src/__tests__/utils/jwt.test.ts
PASS src/__tests__/integration/auth.integration.test.ts

Tests: 12 passed, 12 total
```

**Refactoring successful! Tests still pass.**

---

## STEP 6: Run Full Validation Suite

### Actions
1. Run all tests
2. Check test coverage
3. Run linter
4. Run type checker
5. Check for security issues
6. Verify performance (if applicable)

### Run All Tests

```bash
npm test
```

**Check:**
- All tests pass
- No flaky tests
- Reasonable execution time

### Check Coverage

```bash
npm test -- --coverage
```

**Expected Output:**
```
File                           | % Stmts | % Branch | % Funcs | % Lines |
-------------------------------|---------|----------|---------|---------|
All files                      |   89.23 |    85.71 |   91.67 |   89.47 |
 controllers                   |   92.31 |    87.50 |     100 |   92.31 |
  auth.controller.ts           |   92.31 |    87.50 |     100 |   92.31 |
 middleware                    |   88.89 |      100 |     100 |   88.89 |
  rate-limit.ts                |   88.89 |      100 |     100 |   88.89 |
 services                      |   90.48 |    83.33 |     100 |   90.48 |
  auth.service.ts              |   90.48 |    83.33 |     100 |   90.48 |
 utils                         |   85.71 |       80 |   83.33 |   85.71 |
  jwt.ts                       |     100 |      100 |     100 |     100 |
  audit.ts                     |      75 |       60 |      75 |      75 |
```

**Thresholds:**
- Statements: >80% ✅
- Branches: >80% ✅
- Functions: >80% ✅
- Lines: >80% ✅

### Run Linter

```bash
npm run lint
```

**Expected:**
```
✔ No linting errors found
```

**If errors found:**
```bash
npm run lint -- --fix
```

### Run Type Checker

```bash
npm run type-check
```

**Expected:**
```
✔ No type errors found
```

### Security Check (Optional)

```bash
npm audit
```

**Check for:**
- High/critical vulnerabilities in dependencies
- Outdated packages with security issues

---

## STEP 7: Update Task File

### Actions
1. Update Implementation Record
2. Add files changed
3. Add tests written
4. Add coverage metrics
5. Mark task status as "Review"
6. Add any notes or learnings

### Update Implementation Record

**File:** `.claude/tasks/task-auth-002-login.md`

**Add to Implementation Record section:**

```markdown
## Implementation Record

**Status:** Review
**Implemented By:** James (Developer)
**Implementation Date:** 2025-01-15
**Duration:** 18 minutes

### Files Changed

**Created:**
- `src/controllers/auth.controller.ts` (65 lines) - Login endpoint handler
- `src/services/auth.service.ts` (85 lines) - Auth business logic
- `src/middleware/rate-limit.ts` (25 lines) - Rate limiting middleware
- `src/utils/jwt.ts` (30 lines) - JWT utilities
- `src/schemas/auth.schema.ts` (10 lines) - Zod validation schemas
- `src/__tests__/services/auth.service.test.ts` (120 lines) - Unit tests
- `src/__tests__/integration/auth.integration.test.ts` (180 lines) - Integration tests

**Modified:**
- `src/routes/auth.routes.ts` (+5 lines) - Added login route
- `src/app.ts` (+2 lines) - Registered auth routes

**Total:**
- New Lines: 515
- Modified Lines: 7
- Files Created: 7
- Files Modified: 2

### Tests Written

**Unit Tests: 5**
- ✅ AuthService.findUserByEmail - returns user when exists
- ✅ AuthService.findUserByEmail - returns null when not exists
- ✅ AuthService.verifyPassword - returns true for correct password
- ✅ AuthService.verifyPassword - returns false for incorrect password
- ✅ JwtUtils.generateToken - generates valid token with 24h expiration

**Integration Tests: 7**
- ✅ POST /api/auth/login - 200 with token for valid credentials
- ✅ POST /api/auth/login - 401 for wrong password
- ✅ POST /api/auth/login - 401 for non-existent email
- ✅ POST /api/auth/login - 400 for missing email
- ✅ POST /api/auth/login - 400 for missing password
- ✅ POST /api/auth/login - 400 for invalid email format
- ✅ POST /api/auth/login - 429 after 5 failed attempts

**Total: 12 tests, all passing**

### Test Coverage

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

### Acceptance Criteria Coverage

- ✅ AC-1: User can submit email and password to POST /api/auth/login
- ✅ AC-2: Valid credentials return 200 with JWT token
- ✅ AC-3: Invalid credentials return 401 with "Invalid credentials"
- ✅ AC-4: Missing fields return 400 with validation errors
- ✅ AC-5: Rate limiting: 5 attempts per 10 minutes
- ✅ AC-6: JWT token expires after 24 hours
- ✅ AC-7: Successful login is logged for security audit

**All acceptance criteria met! 7/7**

### Technical Decisions

1. **Rate Limiting:** Used `rate-limiter-flexible` library for in-memory rate limiting
   - Alternative: Redis-based for multi-server deployment
   - Decision: In-memory is sufficient for now, easy to migrate later

2. **Password Verification:** Used bcrypt.compare() directly in service
   - Alternative: Custom timing-safe comparison
   - Decision: bcrypt is industry standard, timing-safe by default

3. **JWT Storage:** Token returned in response body (not cookie)
   - Alternative: HttpOnly cookie for XSS protection
   - Decision: Frontend needs flexibility, will implement cookie option later

4. **Audit Logging:** Synchronous logging to database
   - Alternative: Async queue for performance
   - Decision: Login is infrequent, acceptable performance impact

### Known Limitations

1. **Rate limiting is per-IP, not per-account:**
   - Multiple accounts from same IP share rate limit
   - Consider adding per-account rate limiting

2. **No email verification check:**
   - Users can log in even if email not verified
   - Depends on story-auth-004 (Email Verification)

3. **JWT cannot be invalidated before expiration:**
   - No logout mechanism yet
   - Depends on story-auth-003 (Logout) for token blacklist

### Next Steps

- [ ] Quality review: `@quinn *review task-auth-002-login`
- [ ] Address any quality concerns
- [ ] Create pull request
- [ ] Merge to main
```

---

## STEP 8: Present Summary to User

### Summary Format

```markdown
✅ Implementation Complete: User Login Endpoint

**Task:** task-auth-002-login
**Duration:** 18 minutes
**Status:** Ready for Quality Review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**📊 Summary**

Files Changed: 9 (7 created, 2 modified)
Lines Added: 515
Tests Written: 12 (5 unit, 7 integration)
Tests Passing: 12/12 (100%)
Coverage: 91.25%

**✅ Acceptance Criteria Met: 7/7**
- AC-1: POST /api/auth/login endpoint ✅
- AC-2: Valid credentials return JWT ✅
- AC-3: Invalid credentials return 401 ✅
- AC-4: Validation errors return 400 ✅
- AC-5: Rate limiting (5/10min) ✅
- AC-6: JWT expires in 24 hours ✅
- AC-7: Login attempts logged ✅

**📁 Files Created**
- src/controllers/auth.controller.ts
- src/services/auth.service.ts
- src/middleware/rate-limit.ts
- src/utils/jwt.ts
- src/schemas/auth.schema.ts
- src/__tests__/services/auth.service.test.ts
- src/__tests__/integration/auth.integration.test.ts

**📁 Files Modified**
- src/routes/auth.routes.ts
- src/app.ts

**🧪 Test Results**
```
PASS src/__tests__/services/auth.service.test.ts
PASS src/__tests__/integration/auth.integration.test.ts

Tests:       12 passed, 12 total
Test Suites: 2 passed, 2 total
Time:        2.456 s
```

**📈 Coverage Report**
```
File                 | % Stmts | % Branch | % Funcs | % Lines |
---------------------|---------|----------|---------|---------|
auth.controller.ts   |   92.31 |    87.50 |     100 |   92.31 |
auth.service.ts      |   90.48 |    83.33 |     100 |   90.48 |
rate-limit.ts        |   88.89 |      100 |     100 |   88.89 |
jwt.ts               |     100 |      100 |     100 |     100 |
---------------------|---------|----------|---------|---------|
Overall              |   91.25 |    88.42 |     100 |   91.25 |
```

**📝 Key Technical Decisions**
1. Rate limiting: In-memory (easy migration to Redis later)
2. JWT in response body (cookie option deferred)
3. Synchronous audit logging (acceptable for login frequency)

**⚠️ Known Limitations**
1. Rate limiting per-IP (not per-account)
2. No email verification check (depends on story-auth-004)
3. JWT cannot be invalidated early (depends on story-auth-003)

**🎯 Next Steps**
→ Quality Review: `@quinn *review task-auth-002-login`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task file updated: `.claude/tasks/task-auth-002-login.md`
Status: Review (ready for Quinn)
```

---

## Error Handling

### Ambiguous Requirements

```
❌ Implementation Blocked: Ambiguous Requirements

Task: task-auth-002-login
Issue: AC-5 "Rate limiting" is not specific enough

Questions:
1. Rate limit per what? (IP? Account? Email?)
2. What should happen after limit? (Block? Slow down? Captcha?)
3. Should limit reset on successful login or only after time?

Cannot proceed without clarification.

Action Required:
→ Refine story: `@alex *refine task-auth-002-login --focus rate-limiting`
```

### Tests Failing After Implementation

```
❌ Implementation Failed: Tests Not Passing

Task: task-auth-002-login
Status: Tests failing after implementation

Test Results:
✓ 8 passing
✗ 4 failing

Failures:
1. "should return 401 for non-existent email" - Expected 401, got 500
2. "should return 400 for missing email" - Expected 400, got 500
3. "should return 400 for invalid email format" - Expected 400, got 500
4. "should return 429 after 5 failed attempts" - Rate limiter not working

Root Cause Analysis:
- Issues 1-3: Missing error handling in controller
- Issue 4: Rate limiter middleware not applied to route

Fix Strategy:
1. Add try-catch in controller
2. Add validation error handling
3. Apply rate limit middleware to route
4. Re-run tests

Status: Fixing issues, will retry
```

### Dependency Missing

```
❌ Implementation Blocked: Missing Dependency

Task: task-auth-002-login
Issue: Cannot implement without User model

Required:
- `src/models/user.model.ts` with `findByEmail()` method
- Database schema with users table

Current Status:
- File does not exist
- No database migration for users table

Action Required:
1. Implement story-auth-001 (User Signup) first, OR
2. Create User model as part of this task (expands scope)

Recommendation: Implement story-auth-001 first (proper dependency order)

Blocked: Yes
```

---

## Best Practices

### 1. Always Write Tests First (TDD)

**Workflow:**
```
🔴 Write test (fails)
  ↓
🟢 Write code (test passes)
  ↓
🔵 Refactor (test still passes)
  ↓
Repeat for next test
```

### 2. Keep Tests Focused

**Good:**
```typescript
it('should return 401 for wrong password', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'WrongPassword' });

  expect(response.status).toBe(401);
  expect(response.body.error).toBe('Invalid credentials');
});
```

**Bad:**
```typescript
it('should handle login', async () => {
  // Test correct password
  let response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'Correct' });
  expect(response.status).toBe(200);

  // Test wrong password
  response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'Wrong' });
  expect(response.status).toBe(401);

  // Test missing email
  response = await request(app)
    .post('/api/auth/login')
    .send({ password: 'Correct' });
  expect(response.status).toBe(400);

  // ... (too many concerns in one test)
});
```

### 3. Mock External Dependencies

**Always mock:**
- Database calls
- External APIs
- File system operations
- Time/dates (for consistent tests)

**Example:**
```typescript
// Mock current time for JWT expiration tests
jest.spyOn(Date, 'now').mockReturnValue(1640000000000);

const token = generateToken('123');
const decoded = jwt.decode(token);

expect(decoded.iat).toBe(1640000000);
expect(decoded.exp).toBe(1640086400); // 24 hours later
```

### 4. Commit Frequently

**Commit points:**
- After writing tests (red)
- After implementation (green)
- After refactoring (still green)

**Example:**
```bash
git commit -m "test: add login endpoint tests (red)"
git commit -m "feat: implement login endpoint (green)"
git commit -m "refactor: extract audit logging to service"
```

### 5. Update Documentation

**Always update:**
- Task file (Implementation Record)
- API documentation (if changed)
- README (if new setup required)
- Inline comments (for complex logic)

---

## Skill Metadata

```yaml
skill_name: implement-feature
version: 1.0.0
subagent: james-developer
category: implementation
execution_mode: sequential
halt_on_error: true

inputs:
  required:
    - task_id or story_id or feature_description
  optional:
    - skip_tests (boolean, default: false)
    - tdd (boolean, default: true)

outputs:
  - Implementation code (new/modified files)
  - Test files (unit + integration)
  - Updated task file with Implementation Record
  - Test results and coverage report

dependencies:
  - Task spec or story file must exist
  - Development environment configured
  - Test framework set up

execution_time: 10-30 minutes per feature
```

---

*This skill is part of the BMAD Enhanced Development Suite.*
*For issues or improvements, see `.claude/skills/development/README.md`*
