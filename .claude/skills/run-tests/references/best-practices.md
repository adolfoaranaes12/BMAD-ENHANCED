# Testing & Coverage Best Practices

## Purpose

Guidelines for writing effective tests, achieving meaningful coverage, and maintaining test quality.

---

## Core Testing Principles

### 1. Test Behavior, Not Implementation

**✅ Good - Tests behavior:**
```typescript
it('should authenticate user with valid credentials', async () => {
  const result = await authService.login('user@example.com', 'password123');
  expect(result.success).toBe(true);
  expect(result.token).toBeDefined();
});
```

**❌ Bad - Tests implementation:**
```typescript
it('should call bcrypt.compare with correct arguments', async () => {
  await authService.login('user@example.com', 'password123');
  expect(bcrypt.compare).toHaveBeenCalledWith('password123', hashedPassword);
});
```

**Why:** Implementation can change; behavior should remain stable.

---

### 2. Follow the AAA Pattern

**Arrange-Act-Assert:**
```typescript
it('should increment counter on click', () => {
  // Arrange
  const counter = new Counter();

  // Act
  counter.increment();

  // Assert
  expect(counter.value).toBe(1);
});
```

**Benefits:**
- Clear structure
- Easy to read
- Easy to debug
- Consistent pattern

---

### 3. Test Edge Cases & Boundaries

**Examples:**
```typescript
describe('age validation', () => {
  it('should accept minimum valid age (18)', () => {
    expect(validateAge(18)).toBe(true);
  });

  it('should reject below minimum (17)', () => {
    expect(validateAge(17)).toBe(false);
  });

  it('should accept maximum valid age (120)', () => {
    expect(validateAge(120)).toBe(true);
  });

  it('should reject above maximum (121)', () => {
    expect(validateAge(121)).toBe(false);
  });

  it('should reject negative ages', () => {
    expect(validateAge(-5)).toBe(false);
  });

  it('should reject zero', () => {
    expect(validateAge(0)).toBe(false);
  });
});
```

**Boundary Categories:**
- Numeric boundaries (min, max, zero, negative)
- String boundaries (empty, very long, special characters)
- Collection boundaries (empty, single item, many items)
- Time boundaries (past, present, future)

---

### 4. Use Descriptive Test Names

**Format:** `should [expected behavior] when [condition]`

**✅ Good:**
```typescript
it('should return 401 when password is incorrect', ...)
it('should create user when all fields are valid', ...)
it('should throw error when email already exists', ...)
```

**❌ Bad:**
```typescript
it('test login', ...)
it('user creation', ...)
it('handles errors', ...)
```

---

### 5. Keep Tests Independent

**✅ Good - Independent:**
```typescript
describe('user service', () => {
  beforeEach(() => {
    // Fresh state for each test
    db.clear();
  });

  it('should create user', async () => {
    const user = await userService.create({ email: 'test@example.com' });
    expect(user.id).toBeDefined();
  });

  it('should find user by id', async () => {
    const created = await userService.create({ email: 'test@example.com' });
    const found = await userService.findById(created.id);
    expect(found).toEqual(created);
  });
});
```

**❌ Bad - Dependent:**
```typescript
let userId; // Shared state between tests

it('should create user', async () => {
  const user = await userService.create({ email: 'test@example.com' });
  userId = user.id; // Next test depends on this
});

it('should find user by id', async () => {
  const found = await userService.findById(userId); // Depends on previous test
  expect(found).toBeDefined();
});
```

---

## Coverage Best Practices

### 1. Aim for Meaningful Coverage, Not 100%

**Good Target:**
- 80-85%: Minimum acceptable
- 85-95%: Good coverage
- 95%+: Excellent for critical code

**Don't Chase 100%:**
```typescript
// Don't test trivial code just for coverage
class User {
  get email() { return this._email; } // Skip testing simple getters
  set email(value) { this._email = value; } // Skip testing simple setters
}
```

---

### 2. Focus on Critical Code

**High Priority:**
- Authentication & authorization
- Payment processing
- Data validation
- Security checks
- Business logic
- Error handling

**Lower Priority:**
- Simple getters/setters
- Framework integration code
- Debug logging
- Development-only code

---

### 3. Use Coverage to Find Gaps, Not as a Goal

**✅ Good - Coverage reveals gaps:**
```bash
Coverage: 78%
Uncovered: auth.controller.ts:48-50 (database error handling)
Action: Add test for database failure scenario
```

**❌ Bad - Coverage as goal:**
```bash
Coverage: 78%
Action: Add tests for trivial code to reach 80%
```

---

### 4. Ignore Unreachable Code

**Examples to exclude:**
```javascript
// jest.config.js
module.exports = {
  coveragePathIgnorePatterns: [
    '/node_modules/',
    '/dist/',
    '/.test.ts$/',
    '/test-helpers/',
    '/mocks/',
  ],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/*.test.ts',
    '!src/**/index.ts', // Usually just re-exports
  ],
};
```

---

## Test Organization

### 1. Group Related Tests

**✅ Good:**
```typescript
describe('AuthController', () => {
  describe('login', () => {
    it('should return token for valid credentials', ...);
    it('should return 401 for invalid password', ...);
    it('should return 401 for non-existent user', ...);
    it('should return 429 for too many attempts', ...);
  });

  describe('logout', () => {
    it('should invalidate token on logout', ...);
    it('should return 401 for already logged out user', ...);
  });
});
```

---

### 2. Use Setup & Teardown Appropriately

**beforeEach/afterEach - For each test:**
```typescript
describe('user service', () => {
  beforeEach(async () => {
    await db.clear();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });
});
```

**beforeAll/afterAll - Once per suite:**
```typescript
describe('database tests', () => {
  beforeAll(async () => {
    await db.connect();
  });

  afterAll(async () => {
    await db.disconnect();
  });
});
```

---

### 3. Organize Test Files

**Project Structure:**
```
src/
├── controllers/
│   ├── auth.controller.ts
│   └── user.controller.ts
└── __tests__/
    ├── unit/
    │   ├── controllers/
    │   │   ├── auth.controller.test.ts
    │   │   └── user.controller.test.ts
    │   └── services/
    ├── integration/
    │   ├── auth.integration.test.ts
    │   └── user.integration.test.ts
    └── e2e/
        └── user-flow.e2e.test.ts
```

---

## Mocking Best Practices

### 1. Mock External Dependencies

**✅ Good - Mock database:**
```typescript
import { db } from '../database';

jest.mock('../database');

it('should create user', async () => {
  (db.insert as jest.Mock).mockResolvedValue({ id: '123' });

  const user = await userService.create({ email: 'test@example.com' });

  expect(user.id).toBe('123');
});
```

---

### 2. Use Realistic Mock Data

**✅ Good:**
```typescript
const mockUser = {
  id: 'user-123',
  email: 'john.doe@example.com',
  firstName: 'John',
  lastName: 'Doe',
  createdAt: new Date('2025-01-15'),
};
```

**❌ Bad:**
```typescript
const mockUser = { id: '1', email: 'a', name: 'b' };
```

---

### 3. Don't Over-Mock

**✅ Good - Mock external services:**
```typescript
jest.mock('../services/email');
jest.mock('../database');
```

**❌ Bad - Mocking everything:**
```typescript
jest.mock('../services/email');
jest.mock('../database');
jest.mock('../utils/validation'); // Don't mock internal utilities
jest.mock('../models/user'); // Don't mock internal models
```

---

## Test Performance

### 1. Keep Tests Fast

**Techniques:**
- Use in-memory databases (SQLite)
- Mock slow external services
- Run tests in parallel
- Avoid unnecessary sleeps/waits

**✅ Good:**
```typescript
it('should rate limit requests', async () => {
  // Mock time instead of waiting
  jest.useFakeTimers();

  await rateLimiter.checkLimit('user-123');
  jest.advanceTimersByTime(RATE_LIMIT_WINDOW);
  await rateLimiter.checkLimit('user-123');

  jest.useRealTimers();
});
```

**❌ Bad:**
```typescript
it('should rate limit requests', async () => {
  await rateLimiter.checkLimit('user-123');
  await new Promise(resolve => setTimeout(resolve, 60000)); // 1 minute wait!
  await rateLimiter.checkLimit('user-123');
});
```

---

### 2. Run Tests in Parallel

**Jest Configuration:**
```javascript
module.exports = {
  maxWorkers: '50%', // Use half CPU cores
  testTimeout: 5000, // 5 second timeout
};
```

---

### 3. Fail Fast on CI

**Strategy:**
- Run fast unit tests first
- Run integration tests after unit tests pass
- Run E2E tests last

**CI Configuration:**
```yaml
- run: npm run test:unit
- run: npm run test:integration
  if: success()
- run: npm run test:e2e
  if: success()
```

---

## Common Anti-Patterns

### 1. Testing Implementation Details

**❌ Avoid:**
```typescript
it('should call validateEmail method', () => {
  const spy = jest.spyOn(userService, 'validateEmail');
  userService.create({ email: 'test@example.com' });
  expect(spy).toHaveBeenCalled(); // Testing internal call
});
```

**✅ Better:**
```typescript
it('should reject invalid email addresses', () => {
  expect(() => userService.create({ email: 'invalid' }))
    .toThrow('Invalid email'); // Test behavior
});
```

---

### 2. Brittle Tests

**❌ Brittle:**
```typescript
expect(response.body).toEqual({
  id: '123',
  email: 'test@example.com',
  createdAt: '2025-10-29T12:00:00.000Z', // Exact timestamp fails
  updatedAt: '2025-10-29T12:00:00.000Z',
});
```

**✅ Robust:**
```typescript
expect(response.body).toEqual({
  id: expect.any(String),
  email: 'test@example.com',
  createdAt: expect.any(String),
  updatedAt: expect.any(String),
});
```

---

### 3. Shared Test State

**❌ Avoid shared state:**
```typescript
let user; // Global state

it('creates user', async () => {
  user = await userService.create(...);
});

it('updates user', async () => {
  await userService.update(user.id, ...); // Depends on previous test
});
```

**✅ Use fixtures:**
```typescript
async function createTestUser() {
  return await userService.create({ email: 'test@example.com' });
}

it('updates user', async () => {
  const user = await createTestUser(); // Independent
  await userService.update(user.id, ...);
});
```

---

## Quick Reference

**Coverage Targets:**
- Minimum: 80%
- Good: 85-95%
- Excellent: 95%+

**Test Structure:**
- Use AAA pattern (Arrange-Act-Assert)
- Descriptive names: "should [behavior] when [condition]"
- Keep tests independent
- Group related tests with describe()

**Priority:**
1. Security & data integrity
2. Business logic & error handling
3. Edge cases
4. Logging & debug code (optional)

**Performance:**
- Keep tests under 5 seconds
- Use mocks for external services
- Run tests in parallel
- Fail fast on CI

---

*Part of run-tests skill - Development Suite*
