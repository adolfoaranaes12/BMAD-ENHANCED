# Test Examples

## Purpose

Comprehensive test patterns for TDD implementation covering unit tests, integration tests, and common testing scenarios.

---

## Unit Test Patterns

### Pattern 1: Service Method - Happy Path

```typescript
describe('AuthService.findUserByEmail', () => {
  it('should return user when email exists', async () => {
    // Arrange
    const mockUser = {
      id: '123',
      email: 'test@example.com',
      password_hash: 'hashed_password'
    };
    (User.findByEmail as jest.Mock).mockResolvedValue(mockUser);

    // Act
    const result = await authService.findUserByEmail('test@example.com');

    // Assert
    expect(result).toEqual(mockUser);
    expect(User.findByEmail).toHaveBeenCalledWith('test@example.com');
  });
});
```

### Pattern 2: Service Method - Error Path

```typescript
describe('AuthService.findUserByEmail', () => {
  it('should return null when email does not exist', async () => {
    // Arrange
    (User.findByEmail as jest.Mock).mockResolvedValue(null);

    // Act
    const result = await authService.findUserByEmail('nonexistent@example.com');

    // Assert
    expect(result).toBeNull();
  });
});
```

### Pattern 3: Boolean Verification

```typescript
describe('AuthService.verifyPassword', () => {
  it('should return true for correct password', async () => {
    // Arrange
    (bcrypt.compare as jest.Mock).mockResolvedValue(true);

    // Act
    const result = await authService.verifyPassword('password123', 'hashed_password');

    // Assert
    expect(result).toBe(true);
    expect(bcrypt.compare).toHaveBeenCalledWith('password123', 'hashed_password');
  });

  it('should return false for incorrect password', async () => {
    // Arrange
    (bcrypt.compare as jest.Mock).mockResolvedValue(false);

    // Act
    const result = await authService.verifyPassword('wrongpassword', 'hashed_password');

    // Assert
    expect(result).toBe(false);
  });
});
```

---

## Integration Test Patterns

### Pattern 1: API Endpoint - Success Response

```typescript
describe('POST /api/auth/login', () => {
  beforeAll(async () => {
    await setupTestDatabase();
    await User.create({
      email: 'test@example.com',
      password: await bcrypt.hash('SecurePass123!', 12)
    });
  });

  afterAll(async () => {
    await teardownTestDatabase();
  });

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
});
```

### Pattern 2: API Endpoint - Error Response

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

### Pattern 3: Validation Errors

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

### Pattern 4: Rate Limiting

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

---

## Test Setup Patterns

### Pattern 1: Database Setup/Teardown

```typescript
describe('[Integration] Auth Endpoints', () => {
  beforeAll(async () => {
    await setupTestDatabase();
  });

  afterAll(async () => {
    await teardownTestDatabase();
  });

  beforeEach(async () => {
    // Clean database before each test
    await User.deleteMany({});
  });

  // Tests...
});
```

### Pattern 2: Mock Setup

```typescript
describe('AuthService', () => {
  let authService: AuthService;

  beforeEach(() => {
    authService = new AuthService();
    jest.clearAllMocks();
  });

  // Mock external dependencies
  jest.mock('../../models/user.model', () => ({
    User: {
      findByEmail: jest.fn(),
      create: jest.fn(),
    }
  }));

  jest.mock('bcrypt', () => ({
    compare: jest.fn(),
    hash: jest.fn(),
  }));

  // Tests...
});
```

### Pattern 3: Test Data Factories

```typescript
// Test data factory
function createTestUser(overrides = {}) {
  return {
    id: '123',
    email: 'test@example.com',
    password_hash: 'hashed_password',
    created_at: new Date('2025-01-01'),
    ...overrides
  };
}

// Usage in tests
it('should authenticate user', async () => {
  const testUser = createTestUser({ email: 'custom@example.com' });
  (User.findByEmail as jest.Mock).mockResolvedValue(testUser);

  // Test logic...
});
```

---

## Common Test Scenarios

### Scenario 1: Testing Async Operations

```typescript
it('should handle async errors', async () => {
  // Mock async error
  (User.findByEmail as jest.Mock).mockRejectedValue(
    new Error('Database connection failed')
  );

  // Expect promise to reject
  await expect(
    authService.findUserByEmail('test@example.com')
  ).rejects.toThrow('Database connection failed');
});
```

### Scenario 2: Testing Date/Time

```typescript
it('should generate token with correct expiration', () => {
  // Mock current time
  const mockDate = new Date('2025-01-01T00:00:00Z');
  jest.spyOn(Date, 'now').mockReturnValue(mockDate.getTime());

  const token = jwtUtils.generateToken('123');
  const decoded = jwt.decode(token);

  expect(decoded.iat).toBe(Math.floor(mockDate.getTime() / 1000));
  expect(decoded.exp).toBe(Math.floor(mockDate.getTime() / 1000) + 86400);

  // Restore original implementation
  jest.restoreAllMocks();
});
```

### Scenario 3: Testing Error Messages

```typescript
it('should return descriptive error message', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'invalid-email', password: 'password' });

  expect(response.status).toBe(400);
  expect(response.body.error).toMatch(/email.*invalid|invalid.*email/i);
});
```

---

## Test Organization

### Organizing by Feature

```typescript
describe('Authentication Feature', () => {
  describe('Login', () => {
    describe('Happy Paths', () => {
      it('should allow login with valid credentials', async () => {});
    });

    describe('Error Paths', () => {
      it('should reject invalid credentials', async () => {});
      it('should reject missing fields', async () => {});
    });

    describe('Edge Cases', () => {
      it('should handle rate limiting', async () => {});
    });
  });
});
```

### Organizing by Test Type

```typescript
describe('[Unit] AuthService', () => {
  // Unit tests for AuthService
});

describe('[Integration] Auth API', () => {
  // Integration tests for auth endpoints
});

describe('[E2E] Authentication Flow', () => {
  // End-to-end tests for complete auth flow
});
```

---

## Quick Reference

**Test Naming Convention:**
```typescript
it('should [expected behavior] when [condition]', () => {});

Examples:
- it('should return user when email exists', () => {});
- it('should return 401 when password is incorrect', () => {});
- it('should throw error when database is unavailable', () => {});
```

**Assertion Patterns:**
```typescript
// Equality
expect(result).toBe(expected);          // Strict equality (===)
expect(result).toEqual(expected);       // Deep equality

// Truthy/Falsy
expect(result).toBeTruthy();
expect(result).toBeFalsy();
expect(result).toBeNull();
expect(result).toBeUndefined();

// Numbers
expect(result).toBeGreaterThan(5);
expect(result).toBeLessThanOrEqual(10);

// Strings
expect(result).toContain('substring');
expect(result).toMatch(/regex/);

// Arrays/Objects
expect(array).toContain(item);
expect(obj).toHaveProperty('key');
expect(obj).toHaveProperty('key', 'value');

// Promises
await expect(promise).resolves.toBe(value);
await expect(promise).rejects.toThrow(error);

// Function calls
expect(mockFn).toHaveBeenCalled();
expect(mockFn).toHaveBeenCalledWith(arg1, arg2);
expect(mockFn).toHaveBeenCalledTimes(3);
```

---

*Part of implement-feature skill - Development Suite*
