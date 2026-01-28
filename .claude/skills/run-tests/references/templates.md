# Run Tests Templates and Output Formats

## Complete Workflow Output Templates

This document contains all output formats, examples, and templates for the run-tests skill.

---

## Step 0: Scope Determination Templates

### Task-Based Scope Pattern

**Input:** `task-auth-002-login`

**Process:**
```bash
# Extract keywords from task ID
task_id="task-auth-002-login"
keywords=("auth" "login")

# Create regex pattern
pattern="(auth|login)"

# Find matching test files
find . -type f -name "*.test.*" | grep -E "$pattern"
```

**Output:**
```
Found 2 test files matching pattern (auth|login):
  - src/__tests__/controllers/auth.controller.test.ts
  - src/__tests__/services/login.service.test.ts
```

### File-Based Scope Pattern

**Input:** `src/controllers/auth.controller.ts`

**Process:**
```bash
# Source file: src/controllers/auth.controller.ts
# Test patterns to search:
#   1. src/__tests__/**/auth.controller.test.ts
#   2. src/controllers/__tests__/auth.controller.test.ts
#   3. src/controllers/auth.controller.test.ts
#   4. __tests__/controllers/auth.controller.test.ts
```

**Output:**
```
Found test file for src/controllers/auth.controller.ts:
  - src/__tests__/controllers/auth.controller.test.ts
```

### All Tests Scope

**Input:** `--all`

**Process:**
```bash
# Find all test files
find . -type f \( -name "*.test.*" -o -name "*.spec.*" \)
```

**Output:**
```
Found 47 test files:
  - src/__tests__/controllers/auth.controller.test.ts
  - src/__tests__/controllers/user.controller.test.ts
  - src/__tests__/services/auth.service.test.ts
  [... 44 more files ...]
```

---

## Step 1: Test Execution Templates

### bmad-commands run_tests.py Invocation

**Command:**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --pattern "(auth|login)" \
  --coverage true \
  --output json
```

**Parameters:**
- `--path`: Project root directory (`.` for current)
- `--framework`: Test framework (`jest`, `pytest`, `mocha`, `vitest`, etc.)
- `--pattern`: Optional regex pattern to filter test files
- `--coverage`: Generate coverage report (`true`/`false`)
- `--output`: Output format (`json`, `text`, `junit`)

### Successful Test Execution Response

**Complete JSON Response:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "skipped_tests": 0,
    "duration_ms": 13685,
    "test_suites": {
      "total": 2,
      "passed": 2,
      "failed": 0
    },
    "coverage_percent": 91.25,
    "coverage": {
      "statements": {
        "covered": 210,
        "total": 240,
        "percent": 87.5
      },
      "branches": {
        "covered": 45,
        "total": 52,
        "percent": 86.5
      },
      "functions": {
        "covered": 28,
        "total": 28,
        "percent": 100
      },
      "lines": {
        "covered": 208,
        "total": 238,
        "percent": 87.4
      }
    },
    "failures": []
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest",
    "scope": "task-auth-002",
    "timestamp": "2025-10-30T14:23:45.123Z",
    "duration_ms": 13685
  },
  "errors": []
}
```

### Failed Test Execution Response

**Complete JSON Response with Failures:**
```json
{
  "success": true,
  "outputs": {
    "passed": false,
    "total_tests": 12,
    "passed_tests": 9,
    "failed_tests": 3,
    "skipped_tests": 0,
    "duration_ms": 11234,
    "test_suites": {
      "total": 2,
      "passed": 1,
      "failed": 1
    },
    "coverage_percent": 85.2,
    "failures": [
      {
        "test_name": "should return 401 for invalid credentials",
        "test_file": "src/__tests__/controllers/auth.controller.test.ts",
        "test_suite": "AuthController",
        "error_message": "Expected status 401, received 500",
        "stack_trace": "    at Object.<anonymous> (src/__tests__/controllers/auth.controller.test.ts:42:27)",
        "duration_ms": 156
      },
      {
        "test_name": "should hash password before storing",
        "test_file": "src/__tests__/services/auth.service.test.ts",
        "test_suite": "AuthService",
        "error_message": "AssertionError: expected 'plaintext' to match /^\\$2[ayb]\\$.{56}$/",
        "stack_trace": "    at Context.<anonymous> (src/__tests__/services/auth.service.test.ts:78:34)",
        "duration_ms": 89
      },
      {
        "test_name": "should rate limit login attempts",
        "test_file": "src/__tests__/controllers/auth.controller.test.ts",
        "test_suite": "AuthController",
        "error_message": "Timeout of 5000ms exceeded",
        "stack_trace": "    at listOnTimeout (node:internal/timers:569:17)",
        "duration_ms": 5012
      }
    ]
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest",
    "scope": "task-auth-002",
    "timestamp": "2025-10-30T14:23:45.123Z",
    "duration_ms": 11234
  },
  "errors": []
}
```

### Test Execution Error Response

**Complete JSON Error Response:**
```json
{
  "success": false,
  "outputs": {},
  "telemetry": {
    "command": "run_tests",
    "framework": "jest",
    "scope": "task-auth-002",
    "timestamp": "2025-10-30T14:23:45.123Z",
    "duration_ms": 234
  },
  "errors": [
    {
      "code": "TEST_FRAMEWORK_NOT_FOUND",
      "message": "Jest configuration not found. Expected jest.config.js or jest section in package.json",
      "severity": "error",
      "suggestion": "Run 'npm install --save-dev jest' and create jest.config.js"
    }
  ]
}
```

---

## Step 2: Coverage Report Templates

### Complete Coverage Data Structure

**Full Coverage Object:**
```json
{
  "coverage_percent": 91.25,
  "statements": {
    "covered": 210,
    "total": 240,
    "percent": 87.5,
    "uncovered_ranges": [
      { "file": "src/controllers/auth.controller.ts", "lines": "45-48" },
      { "file": "src/controllers/auth.controller.ts", "lines": "67" },
      { "file": "src/services/auth.service.ts", "lines": "78" },
      { "file": "src/services/auth.service.ts", "lines": "112-115" }
    ]
  },
  "branches": {
    "covered": 45,
    "total": 52,
    "percent": 86.5,
    "uncovered_branches": [
      { "file": "src/controllers/auth.controller.ts", "line": 34, "branch": "else" },
      { "file": "src/middleware/rate-limit.ts", "line": 23, "branch": "catch" }
    ]
  },
  "functions": {
    "covered": 28,
    "total": 28,
    "percent": 100,
    "uncovered_functions": []
  },
  "lines": {
    "covered": 208,
    "total": 238,
    "percent": 87.4,
    "uncovered_lines": [
      { "file": "src/controllers/auth.controller.ts", "lines": [45, 46, 47, 48, 67] },
      { "file": "src/services/auth.service.ts", "lines": [78, 112, 113, 114, 115] },
      { "file": "src/middleware/rate-limit.ts", "lines": [23, 24, 25] }
    ]
  },
  "per_file": [
    {
      "file": "src/controllers/auth.controller.ts",
      "statements": { "covered": 72, "total": 78, "percent": 92.31 },
      "branches": { "covered": 14, "total": 16, "percent": 87.50 },
      "functions": { "covered": 8, "total": 8, "percent": 100 },
      "lines": { "covered": 72, "total": 78, "percent": 92.31 },
      "uncovered_lines": [45, 46, 47, 48, 67]
    },
    {
      "file": "src/services/auth.service.ts",
      "statements": { "covered": 76, "total": 84, "percent": 90.48 },
      "branches": { "covered": 10, "total": 12, "percent": 83.33 },
      "functions": { "covered": 11, "total": 11, "percent": 100 },
      "lines": { "covered": 76, "total": 84, "percent": 90.48 },
      "uncovered_lines": [78, 112, 113, 114, 115]
    },
    {
      "file": "src/middleware/rate-limit.ts",
      "statements": { "covered": 24, "total": 27, "percent": 88.89 },
      "branches": { "covered": 8, "total": 8, "percent": 100 },
      "functions": { "covered": 4, "total": 4, "percent": 100 },
      "lines": { "covered": 24, "total": 27, "percent": 88.89 },
      "uncovered_lines": [23, 24, 25]
    },
    {
      "file": "src/utils/jwt.ts",
      "statements": { "covered": 38, "total": 38, "percent": 100 },
      "branches": { "covered": 13, "total": 13, "percent": 100 },
      "functions": { "covered": 5, "total": 5, "percent": 100 },
      "lines": { "covered": 38, "total": 38, "percent": 100 },
      "uncovered_lines": []
    }
  ]
}
```

### Text Coverage Report Format

**Complete Coverage Table:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 COVERAGE REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File                              | % Stmts | % Branch | % Funcs | % Lines | Uncovered
----------------------------------|---------|----------|---------|---------|----------
src/controllers/auth.controller.ts|   92.31 |    87.50 |     100 |   92.31 | 45-48,67
src/services/auth.service.ts      |   90.48 |    83.33 |     100 |   90.48 | 78,112-115
src/middleware/rate-limit.ts      |   88.89 |      100 |     100 |   88.89 | 23-25
src/utils/jwt.ts                  |     100 |      100 |     100 |     100 |
----------------------------------|---------|----------|---------|---------|----------
Overall                           |   91.25 |    88.42 |     100 |   91.25 |
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thresholds (configured in jest.config.js):
  Statements: ≥80% ✅ (91.25%)
  Branches:   ≥80% ✅ (88.42%)
  Functions:  ≥80% ✅ (100%)
  Lines:      ≥80% ✅ (91.25%)

Status: ✅ ALL THRESHOLDS MET
```

### Low Coverage Warning Format

**Below Threshold Report:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ COVERAGE BELOW THRESHOLD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File                              | % Stmts | % Branch | % Funcs | % Lines | Status
----------------------------------|---------|----------|---------|---------|--------
src/controllers/auth.controller.ts|   92.31 |    87.50 |     100 |   92.31 | ✅
src/services/auth.service.ts      |   67.86 |    58.33 |   90.91 |   67.86 | ❌ BELOW
src/middleware/rate-limit.ts      |   74.07 |    62.50 |     100 |   74.07 | ❌ BELOW
src/utils/jwt.ts                  |     100 |      100 |     100 |     100 | ✅
----------------------------------|---------|----------|---------|---------|--------
Overall                           |   76.54 |    75.26 |   95.65 |   76.54 | ❌ BELOW

Thresholds (configured in jest.config.js):
  Statements: ≥80% ❌ (76.54% - need 3.46% more)
  Branches:   ≥80% ❌ (75.26% - need 4.74% more)
  Functions:  ≥80% ✅ (95.65%)
  Lines:      ≥80% ❌ (76.54% - need 3.46% more)

Status: ❌ THRESHOLDS NOT MET - Need to add ~8-12 tests
```

---

## Step 3: Gap Analysis Templates

### Gap Category Examples

#### Critical Priority Gaps

**Security-Related Code:**
```typescript
// src/controllers/auth.controller.ts:45-48
async login(req: Request, res: Response) {
  try {
    const { email, password } = req.body;
    const user = await this.authService.validateCredentials(email, password);

    // ❌ UNCOVERED: Security validation
    if (!user.emailVerified) {
      return res.status(403).json({ error: 'Email not verified' });
    }

    const token = await this.jwtService.sign({ userId: user.id });
    return res.json({ token });
  } catch (error) {
    // ❌ UNCOVERED: Error handling for security endpoint
    console.error('Login error:', error);
    return res.status(500).json({ error: 'Internal error' });
  }
}
```

**Data Modification:**
```typescript
// src/services/user.service.ts:112-115
async deleteUser(userId: string): Promise<void> {
  // ❌ UNCOVERED: Critical data deletion
  if (!userId || userId.trim() === '') {
    throw new Error('Invalid user ID');
  }

  await this.db.users.delete({ where: { id: userId } });
  await this.auditLog.log('user_deleted', { userId });
}
```

#### High Priority Gaps

**Error Handling:**
```typescript
// src/services/auth.service.ts:78
async validateCredentials(email: string, password: string): Promise<User> {
  const user = await this.db.users.findUnique({ where: { email } });

  if (!user) {
    throw new Error('User not found');
  }

  const isValid = await bcrypt.compare(password, user.passwordHash);

  if (!isValid) {
    // ❌ UNCOVERED: Failed login attempt handling
    await this.rateLimiter.increment(email);
    throw new Error('Invalid credentials');
  }

  return user;
}
```

**Business Logic Edge Cases:**
```typescript
// src/services/subscription.service.ts:45-52
async upgradeSubscription(userId: string, newPlan: Plan): Promise<void> {
  const user = await this.db.users.findUnique({ where: { id: userId } });

  // ❌ UNCOVERED: Edge case validation
  if (user.currentPlan === newPlan) {
    throw new Error('Already on this plan');
  }

  // ❌ UNCOVERED: Downgrade prevention
  if (newPlan.tier < user.currentPlan.tier) {
    throw new Error('Cannot downgrade, use downgrade endpoint');
  }

  await this.db.users.update({
    where: { id: userId },
    data: { planId: newPlan.id }
  });
}
```

#### Medium Priority Gaps

**Logging and Monitoring:**
```typescript
// src/middleware/audit-log.ts:34-38
async log(action: string, metadata: Record<string, any>): Promise<void> {
  try {
    await this.db.auditLogs.create({
      data: { action, metadata, timestamp: new Date() }
    });
  } catch (error) {
    // ❌ UNCOVERED: Non-critical error logging
    console.error('Failed to write audit log:', error);
  }
}
```

**Validation Edge Cases:**
```typescript
// src/utils/validation.ts:23-27
function validateEmail(email: string): boolean {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // ❌ UNCOVERED: Edge case validation
  if (email.length > 254) {
    return false; // RFC 5321 maximum length
  }

  return regex.test(email);
}
```

#### Low Priority Gaps

**Development/Debug Code:**
```typescript
// src/utils/logger.ts:12-15
function log(level: string, message: string): void {
  // ❌ UNCOVERED: Debug-only code
  if (process.env.NODE_ENV === 'development') {
    console.log(`[${level}] ${message}`);
  }

  this.transport.send(level, message);
}
```

**Trivial Getters:**
```typescript
// src/models/user.model.ts:45-48
class User {
  // ❌ UNCOVERED: Trivial getter
  get fullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}
```

### Gap Analysis Output Format

**Complete Gap Analysis JSON:**
```json
{
  "total_gaps": 12,
  "critical_gaps": 2,
  "high_gaps": 4,
  "medium_gaps": 4,
  "low_gaps": 2,
  "gaps": [
    {
      "id": 1,
      "file": "src/controllers/auth.controller.ts",
      "lines": "45-48",
      "code_snippet": "if (!user.emailVerified) {\n  return res.status(403).json({ error: 'Email not verified' });\n}",
      "criticality": "CRITICAL",
      "category": "security",
      "reason": "Email verification bypass could allow unauthorized access",
      "impact": "Security vulnerability - unauthorized users could access protected resources",
      "test_complexity": "low",
      "estimated_time_minutes": 10
    },
    {
      "id": 2,
      "file": "src/services/user.service.ts",
      "lines": "112-115",
      "code_snippet": "await this.db.users.delete({ where: { id: userId } });",
      "criticality": "CRITICAL",
      "category": "data_modification",
      "reason": "User deletion without proper validation or soft-delete",
      "impact": "Data loss - irreversible user data deletion",
      "test_complexity": "medium",
      "estimated_time_minutes": 15
    },
    {
      "id": 3,
      "file": "src/services/auth.service.ts",
      "lines": "78",
      "code_snippet": "await this.rateLimiter.increment(email);",
      "criticality": "HIGH",
      "category": "error_handling",
      "reason": "Rate limiting on failed login attempts",
      "impact": "Security - brute force attack prevention",
      "test_complexity": "medium",
      "estimated_time_minutes": 12
    },
    {
      "id": 4,
      "file": "src/controllers/auth.controller.ts",
      "lines": "67",
      "code_snippet": "catch (error) {\n  console.error('Login error:', error);\n  return res.status(500).json({ error: 'Internal error' });\n}",
      "criticality": "HIGH",
      "category": "error_handling",
      "reason": "Error handling for authentication endpoint",
      "impact": "User experience - proper error responses for auth failures",
      "test_complexity": "low",
      "estimated_time_minutes": 8
    }
  ]
}
```

---

## Step 4: Test Suggestion Templates

### Complete Test Suggestion Format

**Suggestion with Full Test Implementation:**
```markdown
### Gap 1: Email Verification Check (CRITICAL)

**File:** `src/controllers/auth.controller.ts:45-48`
**Lines:** 45-48
**Criticality:** CRITICAL
**Category:** Security
**Estimated Time:** 10 minutes

**Why This Should Be Tested:**
Email verification is a security control that prevents unauthorized access. Without testing this path, we cannot verify that unverified users are properly blocked from accessing the system.

**Current Gap:**
```typescript
if (!user.emailVerified) {
  return res.status(403).json({ error: 'Email not verified' });
}
```

**Suggested Test:**
```typescript
describe('AuthController - Email Verification', () => {
  it('should return 403 when user email is not verified', async () => {
    // Arrange
    const unverifiedUser = {
      id: 'user-123',
      email: 'test@example.com',
      emailVerified: false,
      passwordHash: await bcrypt.hash('password123', 10)
    };

    jest.spyOn(authService, 'validateCredentials')
      .mockResolvedValue(unverifiedUser);

    // Act
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'password123'
      });

    // Assert
    expect(response.status).toBe(403);
    expect(response.body).toEqual({
      error: 'Email not verified'
    });
    expect(jwtService.sign).not.toHaveBeenCalled();
  });

  it('should return token when user email is verified', async () => {
    // Arrange
    const verifiedUser = {
      id: 'user-123',
      email: 'test@example.com',
      emailVerified: true,
      passwordHash: await bcrypt.hash('password123', 10)
    };

    jest.spyOn(authService, 'validateCredentials')
      .mockResolvedValue(verifiedUser);
    jest.spyOn(jwtService, 'sign')
      .mockResolvedValue('jwt-token-123');

    // Act
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'password123'
      });

    // Assert
    expect(response.status).toBe(200);
    expect(response.body).toEqual({
      token: 'jwt-token-123'
    });
    expect(jwtService.sign).toHaveBeenCalledWith({
      userId: 'user-123'
    });
  });
});
```

**Coverage Impact:**
- Adds coverage for lines 45-48
- Tests both branches of email verification check
- Improves security test coverage by 5%
- Estimated coverage increase: +2.1% overall
```

### Test Suggestion for Error Handling

```markdown
### Gap 2: Database Connection Failure (HIGH)

**File:** `src/controllers/auth.controller.ts:67`
**Lines:** 67-70
**Criticality:** HIGH
**Category:** Error Handling
**Estimated Time:** 8 minutes

**Why This Should Be Tested:**
Database connection failures are expected in production. We need to verify that the application handles these failures gracefully with appropriate error messages and status codes.

**Current Gap:**
```typescript
catch (error) {
  console.error('Login error:', error);
  return res.status(500).json({ error: 'Internal error' });
}
```

**Suggested Test:**
```typescript
describe('AuthController - Error Handling', () => {
  it('should return 500 when database connection fails', async () => {
    // Arrange
    jest.spyOn(authService, 'validateCredentials')
      .mockRejectedValue(new Error('ECONNREFUSED: Database connection failed'));

    // Act
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'password123'
      });

    // Assert
    expect(response.status).toBe(500);
    expect(response.body).toEqual({
      error: 'Internal error'
    });
  });

  it('should log error details when database fails', async () => {
    // Arrange
    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation();
    const dbError = new Error('ECONNREFUSED: Database connection failed');

    jest.spyOn(authService, 'validateCredentials')
      .mockRejectedValue(dbError);

    // Act
    await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'password123'
      });

    // Assert
    expect(consoleErrorSpy).toHaveBeenCalledWith('Login error:', dbError);
    consoleErrorSpy.mockRestore();
  });
});
```

**Coverage Impact:**
- Adds coverage for error catch block (lines 67-70)
- Tests error logging
- Improves error handling test coverage by 12%
- Estimated coverage increase: +1.8% overall
```

### Test Suggestion for Edge Cases

```markdown
### Gap 3: Rate Limiter Failure Resilience (MEDIUM)

**File:** `src/services/auth.service.ts:78`
**Lines:** 78
**Criticality:** MEDIUM
**Category:** Error Handling / Resilience
**Estimated Time:** 12 minutes

**Why This Should Be Tested:**
The rate limiter is a Redis-based service that can fail independently of the main application. We need to verify that authentication continues to work even when the rate limiter is unavailable (fail-open strategy for availability).

**Current Gap:**
```typescript
if (!isValid) {
  await this.rateLimiter.increment(email);
  throw new Error('Invalid credentials');
}
```

**Suggested Test:**
```typescript
describe('AuthService - Rate Limiter Resilience', () => {
  it('should still reject invalid credentials when rate limiter fails', async () => {
    // Arrange
    const user = {
      id: 'user-123',
      email: 'test@example.com',
      passwordHash: await bcrypt.hash('correct-password', 10)
    };

    jest.spyOn(db.users, 'findUnique').mockResolvedValue(user);
    jest.spyOn(rateLimiter, 'increment')
      .mockRejectedValue(new Error('Redis connection failed'));

    // Act & Assert
    await expect(
      authService.validateCredentials('test@example.com', 'wrong-password')
    ).rejects.toThrow('Invalid credentials');
  });

  it('should log rate limiter failures without blocking auth', async () => {
    // Arrange
    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation();
    const user = {
      id: 'user-123',
      email: 'test@example.com',
      passwordHash: await bcrypt.hash('correct-password', 10)
    };

    jest.spyOn(db.users, 'findUnique').mockResolvedValue(user);
    const redisError = new Error('Redis connection failed');
    jest.spyOn(rateLimiter, 'increment').mockRejectedValue(redisError);

    // Act & Assert
    await expect(
      authService.validateCredentials('test@example.com', 'wrong-password')
    ).rejects.toThrow('Invalid credentials');

    // Verify error was logged but didn't block the authentication flow
    expect(consoleErrorSpy).toHaveBeenCalledWith(
      'Rate limiter error:',
      redisError
    );
    consoleErrorSpy.mockRestore();
  });

  it('should increment rate limiter on successful failure', async () => {
    // Arrange
    const user = {
      id: 'user-123',
      email: 'test@example.com',
      passwordHash: await bcrypt.hash('correct-password', 10)
    };

    jest.spyOn(db.users, 'findUnique').mockResolvedValue(user);
    const incrementSpy = jest.spyOn(rateLimiter, 'increment')
      .mockResolvedValue(undefined);

    // Act & Assert
    await expect(
      authService.validateCredentials('test@example.com', 'wrong-password')
    ).rejects.toThrow('Invalid credentials');

    expect(incrementSpy).toHaveBeenCalledWith('test@example.com');
  });
});
```

**Coverage Impact:**
- Adds coverage for rate limiter call (line 78)
- Tests resilience and fail-open behavior
- Improves service reliability test coverage by 8%
- Estimated coverage increase: +1.2% overall
```

---

## Step 5: Complete Summary Templates

### Success Summary (All Tests Passing, Good Coverage)

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ TESTS EXECUTED SUCCESSFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Scope:** task-auth-002-login
**Framework:** Jest
**Duration:** 13.7s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🧪 Test Results

**Test Suites:** 2 passed, 2 total
**Tests:**       12 passed, 12 total
**Duration:**    13.7s

**Status:** ✅ ALL TESTS PASSING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📊 Coverage Report

**Overall Coverage:** 91.25%

| Metric     | Coverage | Threshold | Status |
|------------|----------|-----------|--------|
| Statements | 91.25%   | ≥80%      | ✅ Pass |
| Branches   | 88.42%   | ≥80%      | ✅ Pass |
| Functions  | 100%     | ≥80%      | ✅ Pass |
| Lines      | 91.25%   | ≥80%      | ✅ Pass |

**Status:** ✅ ALL THRESHOLDS MET

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔍 Coverage Gaps (5 identified)

### High Priority (3)

1. **Database connection error handling**
   - File: `src/controllers/auth.controller.ts:67-70`
   - Impact: Production resilience

2. **Session expiration check**
   - File: `src/middleware/session.ts:34-37`
   - Impact: Security

3. **Unexpected error catch block**
   - File: `src/services/auth.service.ts:112-115`
   - Impact: Error handling

### Medium Priority (2)

4. **Rate limiter error handling**
   - File: `src/middleware/rate-limit.ts:45-48`
   - Impact: Service resilience

5. **Audit logging failure handling**
   - File: `src/utils/audit-log.ts:23-26`
   - Impact: Observability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Suggested Tests

I can write 5 additional tests to improve coverage to ~96%:

### High Priority Tests (3)

1. **Database failure handling** (10 min)
   - Test authentication when database connection fails
   - Verify 500 error response and error logging

2. **Session expiration** (8 min)
   - Test session timeout enforcement
   - Verify 401 error for expired sessions

3. **Unexpected error handling** (8 min)
   - Test catch block for unexpected service errors
   - Verify error logging and user-facing error messages

### Medium Priority Tests (2)

4. **Rate limiter resilience** (12 min)
   - Test auth flow when Redis rate limiter is down
   - Verify fail-open behavior for availability

5. **Audit log resilience** (10 min)
   - Test audit logging failures don't block main flow
   - Verify error logging for audit failures

**Estimated Time:** ~48 minutes for all 5 tests
**Estimated Coverage Gain:** +4.75% (91.25% → 96%)

Would you like me to add these tests?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✅ Next Steps

- ✅ Tests passing
- ⚠️ Consider adding 3 HIGH priority tests (optional but recommended)
- ✅ Ready for code review
- ✅ Ready for pull request

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Failed Tests Summary

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ TESTS FAILED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Scope:** task-auth-002-login
**Framework:** Jest
**Duration:** 11.2s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🧪 Test Results

**Test Suites:** 1 passed, 1 failed, 2 total
**Tests:**       9 passed, 3 failed, 12 total
**Duration:**    11.2s

**Status:** ❌ 3 TESTS FAILING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ❌ Failed Tests

### 1. should return 401 for invalid credentials

**File:** `src/__tests__/controllers/auth.controller.test.ts`
**Suite:** AuthController
**Duration:** 156ms

**Error:**
```
Expected status 401, received 500

Stack trace:
  at Object.<anonymous> (src/__tests__/controllers/auth.controller.test.ts:42:27)
```

**Likely Cause:**
The controller is returning 500 (Internal Server Error) instead of 401 (Unauthorized). This suggests:
- Exception being thrown instead of proper validation
- Missing error handling in validateCredentials
- Database error occurring during validation

**Suggested Fix:**
1. Check auth.service.ts validateCredentials method
2. Ensure invalid credentials throw proper AuthenticationError
3. Add error handling for database errors

---

### 2. should hash password before storing

**File:** `src/__tests__/services/auth.service.test.ts`
**Suite:** AuthService
**Duration:** 89ms

**Error:**
```
AssertionError: expected 'plaintext' to match /^\$2[ayb]\$.{56}$/

Stack trace:
  at Context.<anonymous> (src/__tests__/services/auth.service.test.ts:78:34)
```

**Likely Cause:**
Password is being stored as plaintext instead of being hashed. This is a **CRITICAL SECURITY ISSUE**.

**Suggested Fix:**
1. In user creation/update methods, hash password with bcrypt before saving
2. Add password hashing middleware
3. Review all user creation paths to ensure passwords are always hashed

**Example Fix:**
```typescript
async createUser(email: string, password: string): Promise<User> {
  const passwordHash = await bcrypt.hash(password, 10);  // Add this line
  return this.db.users.create({
    data: { email, passwordHash }  // Use passwordHash, not password
  });
}
```

---

### 3. should rate limit login attempts

**File:** `src/__tests__/controllers/auth.controller.test.ts`
**Suite:** AuthController
**Duration:** 5012ms

**Error:**
```
Timeout of 5000ms exceeded

Stack trace:
  at listOnTimeout (node:internal/timers:569:17)
```

**Likely Cause:**
Test is hanging, likely due to:
- Async operation not completing
- Missing mock for rate limiter
- Real Redis connection blocking test

**Suggested Fix:**
1. Add mock for rateLimiter.check()
2. Ensure all async operations have proper error handling
3. Increase test timeout or fix hanging operation

**Example Fix:**
```typescript
it('should rate limit login attempts', async () => {
  jest.spyOn(rateLimiter, 'check')
    .mockResolvedValue({ allowed: false, remaining: 0 });

  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'password' });

  expect(response.status).toBe(429);
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ⚠️ Action Required

**Critical Issues:**
1. **Password hashing not working** - SECURITY ISSUE (Fix immediately!)
2. Invalid credential handling returning 500 instead of 401
3. Rate limiter test hanging - likely missing mock

**Next Steps:**
1. Fix password hashing in user service (PRIORITY 1)
2. Fix error handling in auth controller
3. Add rate limiter mocks to tests
4. Re-run tests after fixes

**Do not proceed with coverage analysis until all tests pass.**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Low Coverage Summary

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ TESTS PASSING BUT COVERAGE LOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Scope:** task-auth-002-login
**Framework:** Jest
**Duration:** 9.8s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🧪 Test Results

**Test Suites:** 2 passed, 2 total
**Tests:**       8 passed, 8 total
**Duration:**    9.8s

**Status:** ✅ ALL TESTS PASSING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ⚠️ Coverage Report

**Overall Coverage:** 62.35% (Below 80% threshold)

| Metric     | Coverage | Threshold | Gap      | Status  |
|------------|----------|-----------|----------|---------|
| Statements | 62.35%   | ≥80%      | -17.65%  | ❌ Fail  |
| Branches   | 54.17%   | ≥80%      | -25.83%  | ❌ Fail  |
| Functions  | 73.33%   | ≥80%      | -6.67%   | ❌ Fail  |
| Lines      | 61.92%   | ≥80%      | -18.08%  | ❌ Fail  |

**Status:** ❌ NEED ~12-15 MORE TESTS TO REACH THRESHOLD

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔍 Critical Coverage Gaps (15 identified)

### Critical Priority (4)

1. **Email verification check** - `auth.controller.ts:45-48`
2. **Password hashing validation** - `auth.service.ts:67-71`
3. **User deletion validation** - `user.service.ts:112-115`
4. **Token expiration check** - `jwt.service.ts:89-92`

### High Priority (6)

5. **Database connection error handling** - `auth.controller.ts:78-82`
6. **Rate limiter increment on failure** - `auth.service.ts:98`
7. **Session timeout enforcement** - `session.middleware.ts:34-41`
8. **Permission validation** - `auth.middleware.ts:56-62`
9. **Refresh token rotation** - `token.service.ts:123-129`
10. **Audit log on sensitive operations** - `audit.middleware.ts:23-28`

### Medium Priority (5)

11. **Rate limiter resilience** - `rate-limit.ts:45-48`
12. **Cache fallback on Redis failure** - `cache.service.ts:78-84`
13. **Email validation edge cases** - `validation.ts:23-27`
14. **Pagination boundary handling** - `user.controller.ts:145-150`
15. **Query parameter sanitization** - `sanitize.middleware.ts:34-39`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Prioritized Test Plan

To reach 80% coverage, I recommend adding **12 tests in this order**:

### Phase 1: Critical Tests (4 tests, ~35 min)

**Estimated coverage gain: +10-12%**

1. ✅ Email verification enforcement (8 min)
2. ✅ Password hashing on user creation (10 min)
3. ✅ User deletion validation (8 min)
4. ✅ Token expiration validation (9 min)

### Phase 2: High Priority Tests (4 tests, ~40 min)

**Estimated coverage gain: +8-10%**

5. ✅ Database connection error handling (10 min)
6. ✅ Rate limiter on failed login (8 min)
7. ✅ Session timeout enforcement (12 min)
8. ✅ Permission validation (10 min)

### Phase 3: Additional High Priority (4 tests, ~45 min)

**Estimated coverage gain: +6-8%**

9. ✅ Refresh token rotation (12 min)
10. ✅ Audit logging (10 min)
11. ✅ Rate limiter resilience (12 min)
12. ✅ Cache Redis failover (11 min)

**Total Time:** ~2 hours
**Total Coverage Gain:** ~24-30%
**Final Coverage:** ~80-92%

Would you like me to:
A) Write all 12 tests now
B) Start with Phase 1 (4 critical tests)
C) Show me the test code for review first

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ⚠️ Recommendation

Coverage is significantly below threshold. I **strongly recommend** adding at least the **4 critical tests** before proceeding with code review or deployment.

These tests cover:
- Security controls (email verification, password hashing)
- Data integrity (user deletion validation)
- Authentication (token expiration)

Without these tests, the code has significant security and quality risks.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Complete JSON Output Format

### Full Skill Output Structure

```json
{
  "tests_passed": true,
  "total_tests": 12,
  "passed_tests": 12,
  "failed_tests": 0,
  "skipped_tests": 0,
  "duration_ms": 13685,
  "coverage_percent": 91.25,
  "coverage": {
    "statements": {
      "covered": 210,
      "total": 240,
      "percent": 87.5
    },
    "branches": {
      "covered": 45,
      "total": 52,
      "percent": 86.5
    },
    "functions": {
      "covered": 28,
      "total": 28,
      "percent": 100
    },
    "lines": {
      "covered": 208,
      "total": 238,
      "percent": 87.4
    }
  },
  "coverage_gaps": [
    {
      "id": 1,
      "file": "src/controllers/auth.controller.ts",
      "lines": "45-48",
      "criticality": "HIGH",
      "category": "error_handling",
      "reason": "Database connection error handling uncovered",
      "estimated_time_minutes": 10
    },
    {
      "id": 2,
      "file": "src/middleware/session.ts",
      "lines": "34-37",
      "criticality": "HIGH",
      "category": "security",
      "reason": "Session expiration check uncovered",
      "estimated_time_minutes": 8
    },
    {
      "id": 3,
      "file": "src/services/auth.service.ts",
      "lines": "112-115",
      "criticality": "HIGH",
      "category": "error_handling",
      "reason": "Unexpected error catch block uncovered",
      "estimated_time_minutes": 8
    },
    {
      "id": 4,
      "file": "src/middleware/rate-limit.ts",
      "lines": "45-48",
      "criticality": "MEDIUM",
      "category": "resilience",
      "reason": "Rate limiter error handling uncovered",
      "estimated_time_minutes": 12
    },
    {
      "id": 5,
      "file": "src/utils/audit-log.ts",
      "lines": "23-26",
      "criticality": "MEDIUM",
      "category": "observability",
      "reason": "Audit logging failure handling uncovered",
      "estimated_time_minutes": 10
    }
  ],
  "test_suggestions": [
    {
      "priority": "HIGH",
      "title": "Database connection error handling",
      "file": "src/controllers/auth.controller.ts",
      "lines": "45-48",
      "estimated_time_minutes": 10,
      "estimated_coverage_gain_percent": 1.8
    },
    {
      "priority": "HIGH",
      "title": "Session expiration enforcement",
      "file": "src/middleware/session.ts",
      "lines": "34-37",
      "estimated_time_minutes": 8,
      "estimated_coverage_gain_percent": 1.5
    },
    {
      "priority": "HIGH",
      "title": "Unexpected error handling",
      "file": "src/services/auth.service.ts",
      "lines": "112-115",
      "estimated_time_minutes": 8,
      "estimated_coverage_gain_percent": 1.4
    },
    {
      "priority": "MEDIUM",
      "title": "Rate limiter resilience",
      "file": "src/middleware/rate-limit.ts",
      "lines": "45-48",
      "estimated_time_minutes": 12,
      "estimated_coverage_gain_percent": 1.2
    },
    {
      "priority": "MEDIUM",
      "title": "Audit log resilience",
      "file": "src/utils/audit-log.ts",
      "lines": "23-26",
      "estimated_time_minutes": 10,
      "estimated_coverage_gain_percent": 0.9
    }
  ],
  "telemetry": {
    "skill": "run-tests",
    "scope": "task-auth-002",
    "framework": "jest",
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "coverage_percent": 91.25,
    "duration_ms": 13685,
    "gaps_count": 5,
    "suggestions_count": 5,
    "timestamp": "2025-10-30T14:23:58.808Z"
  }
}
```

---

## Error Templates

### No Tests Found Error

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ ERROR: NO TESTS FOUND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Scope:** task-auth-002-login
**Pattern:** (auth|login)

**Error:** No test files found matching pattern "(auth|login)"

**Searched Locations:**
- src/__tests__/**/*.test.*
- src/**/__tests__/**/*.test.*
- __tests__/**/*.test.*
- **/*.spec.*

**Suggestions:**
1. Verify test files exist for this scope
2. Check test file naming conventions (*.test.ts, *.spec.ts)
3. Ensure tests are in standard locations (__tests__/, src/__tests__/)
4. Try running with --all flag to see all tests

**Example Test File Locations:**
- src/__tests__/controllers/auth.controller.test.ts
- src/__tests__/services/login.service.test.ts
- __tests__/integration/auth.test.ts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Test Framework Not Configured Error

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ ERROR: TEST FRAMEWORK NOT CONFIGURED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Framework:** Jest
**Error:** Jest configuration not found

**Missing:**
- jest.config.js
- jest.config.ts
- jest section in package.json

**To Fix:**
1. Install Jest: `npm install --save-dev jest @types/jest ts-jest`
2. Create jest.config.js:

```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testMatch: ['**/__tests__/**/*.test.ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts'
  ],
  coverageThresholds: {
    global: {
      statements: 80,
      branches: 80,
      functions: 80,
      lines: 80
    }
  }
};
```

3. Add test script to package.json:

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

4. Re-run tests

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Integration Examples

### CI/CD Integration (GitHub Actions)

```yaml
name: Run Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests with coverage
        run: |
          python .claude/skills/bmad-commands/scripts/run_tests.py \
            --path . \
            --framework auto \
            --coverage true \
            --output json > test-results.json

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
          flags: unittests
          name: codecov-umbrella

      - name: Check coverage thresholds
        run: |
          COVERAGE=$(jq '.outputs.coverage_percent' test-results.json)
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "Coverage $COVERAGE% is below 80% threshold"
            exit 1
          fi
```

### GitLab CI Integration

```yaml
test:
  stage: test
  image: node:18
  script:
    - npm ci
    - python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto --coverage true --output json > test-results.json
    - COVERAGE=$(jq '.outputs.coverage_percent' test-results.json)
    - |
      if (( $(echo "$COVERAGE < 80" | bc -l) )); then
        echo "Coverage $COVERAGE% is below 80% threshold"
        exit 1
      fi
  coverage: '/Overall Coverage: (\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/
      - test-results.json
    expire_in: 30 days
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running tests before commit..."

python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --coverage true \
  --output json > test-results.json

SUCCESS=$(jq '.success' test-results.json)
PASSED=$(jq '.outputs.passed' test-results.json)
COVERAGE=$(jq '.outputs.coverage_percent' test-results.json)

if [ "$SUCCESS" != "true" ] || [ "$PASSED" != "true" ]; then
  echo "❌ Tests failed. Commit aborted."
  cat test-results.json | jq '.outputs.failures'
  exit 1
fi

if (( $(echo "$COVERAGE < 80" | bc -l) )); then
  echo "⚠️ Coverage $COVERAGE% is below 80% threshold"
  echo "Continue with commit? (y/n)"
  read -r response
  if [[ ! "$response" =~ ^[Yy]$ ]]; then
    exit 1
  fi
fi

echo "✅ All tests passed with $COVERAGE% coverage"
exit 0
```

---

## Framework-Specific Examples

### Jest Configuration

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: [
    '**/__tests__/**/*.test.ts',
    '**/?(*.)+(spec|test).ts'
  ],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/*.interface.ts',
    '!src/index.ts'
  ],
  coverageThresholds: {
    global: {
      statements: 80,
      branches: 80,
      functions: 80,
      lines: 80
    }
  },
  coverageReporters: ['text', 'lcov', 'json', 'html'],
  setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  }
};
```

### Pytest Configuration

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
addopts =
    --verbose
    --cov=src
    --cov-report=term-missing
    --cov-report=html
    --cov-report=json
    --cov-fail-under=80
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### Mocha Configuration

```javascript
// .mocharc.js
module.exports = {
  require: ['ts-node/register', 'source-map-support/register'],
  extensions: ['ts'],
  spec: ['src/**/*.test.ts', 'test/**/*.test.ts'],
  watchExtensions: ['ts'],
  timeout: 5000,
  reporter: 'spec',
  ui: 'bdd'
};
```

---

*Complete templates and output formats for run-tests skill*
