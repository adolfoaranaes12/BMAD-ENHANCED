# TDD Best Practices

## Purpose

Best practices for Test-Driven Development to ensure high-quality, maintainable code.

---

## Core TDD Principles

### 1. Always Follow Red-Green-Refactor

```
🔴 RED: Write failing test
  ↓
🟢 GREEN: Make test pass (minimum code)
  ↓
🔵 REFACTOR: Improve code (keep tests green)
  ↓
Repeat for next requirement
```

**Never skip steps:**
- ❌ Don't write code before tests
- ❌ Don't refactor before tests pass
- ❌ Don't add features during refactoring

### 2. One Test at a Time

**Good:**
```typescript
// Write one test
it('should return user when email exists', () => {});

// Make it pass
// Write next test
it('should return null when email not found', () => {});
```

**Bad:**
```typescript
// Writing multiple tests before implementation
it('should return user when email exists', () => {});
it('should return null when email not found', () => {});
it('should handle database errors', () => {});
// Then implementing all at once
```

### 3. Keep Tests Simple and Focused

**Good:**
```typescript
it('should return 401 for wrong password', async () => {
  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'wrong' });

  expect(response.status).toBe(401);
});
```

**Bad:**
```typescript
it('should handle login', async () => {
  // Testing multiple things in one test
  let response = await request(app).post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'correct' });
  expect(response.status).toBe(200);

  response = await request(app).post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'wrong' });
  expect(response.status).toBe(401);

  response = await request(app).post('/api/auth/login')
    .send({ email: 'nonexistent@example.com', password: 'any' });
  expect(response.status).toBe(401);
});
```

---

## Test Organization

### Arrange-Act-Assert Pattern

```typescript
it('should authenticate user with valid credentials', async () => {
  // ARRANGE - Set up test data
  const mockUser = {
    id: '123',
    email: 'test@example.com',
    password_hash: 'hashed'
  };
  (User.findByEmail as jest.Mock).mockResolvedValue(mockUser);
  (bcrypt.compare as jest.Mock).mockResolvedValue(true);

  // ACT - Execute the operation
  const result = await authService.authenticateUser(
    'test@example.com',
    'password123'
  );

  // ASSERT - Verify the outcome
  expect(result).toEqual(mockUser);
  expect(User.findByEmail).toHaveBeenCalledWith('test@example.com');
  expect(bcrypt.compare).toHaveBeenCalledWith('password123', 'hashed');
});
```

### Test Naming Convention

**Pattern:**
```
it('should [expected behavior] when [condition]', () => {});
```

**Examples:**
```typescript
✅ it('should return user when email exists', () => {});
✅ it('should return 401 when password is incorrect', () => {});
✅ it('should throw error when database is unavailable', () => {});

❌ it('test login', () => {});                    // Too vague
❌ it('email exists', () => {});                  // Not a behavior
❌ it('authenticates the user correctly', () => {}); // Not specific enough
```

---

## Mocking Best Practices

### Mock External Dependencies Only

**Good:**
```typescript
// Mock external dependencies (database, API, file system)
jest.mock('../models/user.model');
jest.mock('bcrypt');

// Test real business logic
const result = await authService.authenticateUser(email, password);
```

**Bad:**
```typescript
// Mocking internal business logic
jest.mock('../services/auth.service');

// Now you're not testing your code!
const result = await authController.login(req, res);
```

### Keep Mocks Simple

**Good:**
```typescript
(User.findByEmail as jest.Mock).mockResolvedValue(mockUser);
```

**Bad:**
```typescript
(User.findByEmail as jest.Mock).mockImplementation(async (email) => {
  if (email === 'test@example.com') return mockUser;
  if (email === 'other@example.com') return otherUser;
  if (email.includes('admin')) return adminUser;
  if (Math.random() > 0.5) throw new Error('Random error');
  return null;
});
// Too complex - testing mock logic instead of real logic
```

---

## Common Pitfalls

### Pitfall 1: Testing Implementation Instead of Behavior

**Bad:**
```typescript
it('should call findByEmail and verifyPassword', async () => {
  await authService.authenticateUser('email', 'password');

  expect(authService.findByEmail).toHaveBeenCalled();
  expect(authService.verifyPassword).toHaveBeenCalled();
  // Testing HOW it works (implementation)
});
```

**Good:**
```typescript
it('should return user for valid credentials', async () => {
  const user = await authService.authenticateUser('email', 'password');

  expect(user).toEqual(mockUser);
  // Testing WHAT it does (behavior)
});
```

### Pitfall 2: Flaky Tests (Timing Issues)

**Bad:**
```typescript
it('should process async operation', async () => {
  processAsync();
  // No await - test may pass or fail randomly
  expect(result).toBe(expected);
});
```

**Good:**
```typescript
it('should process async operation', async () => {
  await processAsync();
  // Proper await - test is deterministic
  expect(result).toBe(expected);
});
```

### Pitfall 3: Tests That Always Pass

**Bad:**
```typescript
it('should throw error for invalid input', () => {
  try {
    validateInput(invalidData);
    // If no error thrown, test still passes!
  } catch (error) {
    expect(error.message).toBe('Invalid input');
  }
});
```

**Good:**
```typescript
it('should throw error for invalid input', () => {
  expect(() => validateInput(invalidData)).toThrow('Invalid input');
  // Test fails if no error thrown
});
```

---

## Test Coverage Guidelines

### What to Cover

**✅ Always Test:**
- Happy path (normal operation)
- Error paths (invalid input, failures)
- Edge cases (boundary conditions)
- Business logic (core functionality)

**⚠️ Consider Testing:**
- Complex conditionals
- Loops with non-trivial logic
- Error handling
- Data transformations

**❌ Don't Waste Time Testing:**
- Trivial getters/setters
- Framework code (Express, React, etc.)
- Third-party libraries
- Configuration files

### Coverage Targets

| Code Type | Target Coverage | Reason |
|-----------|----------------|---------|
| Business Logic | 90-100% | Core functionality |
| Controllers | 85-95% | API contracts |
| Services | 90-100% | Critical operations |
| Utilities | 80-90% | Helper functions |
| Models | 50-70% | Often simple |
| Config | 0-30% | Usually static |

---

## Commit Strategy

### Commit After Each Phase

```bash
# RED phase - Test written
git add src/__tests__/auth.service.test.ts
git commit -m "test: add authentication tests (red)"

# GREEN phase - Implementation working
git add src/services/auth.service.ts
git commit -m "feat: implement authentication service (green)"

# REFACTOR phase - Code improved
git add src/services/auth.service.ts
git commit -m "refactor: extract password verification logic"
```

### Commit Message Format

```
<type>: <description>

Types:
- test: Add or update tests
- feat: Add new feature
- fix: Bug fix
- refactor: Code refactoring
- docs: Documentation changes
- chore: Build/tooling changes

Examples:
test: add login endpoint tests (red)
feat: implement login endpoint (green)
refactor: extract validation logic
fix: handle database connection errors
```

---

## Quick Reference

**TDD Cycle:**
1. Write failing test (RED)
2. Write minimum code to pass (GREEN)
3. Refactor while keeping tests green (REFACTOR)
4. Repeat

**Test Structure:**
- Arrange (setup)
- Act (execute)
- Assert (verify)

**Naming:**
- `it('should [behavior] when [condition]')`

**Mocking:**
- Mock external dependencies only
- Keep mocks simple
- Test behavior, not implementation

**Coverage:**
- Business logic: 90-100%
- Controllers/Services: 85-95%
- Utilities: 80-90%

---

*Part of implement-feature skill - Development Suite*
