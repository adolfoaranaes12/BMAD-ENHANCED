# TDD Workflow Guide

## The Three Phases

### RED Phase: Write Failing Tests

**Goal:** Write tests that define desired behavior

**Steps:**
1. Write test for smallest unit of functionality
2. Test should fail for the right reason (not syntax error)
3. Run test suite to confirm failure
4. Commit the failing test (optional but recommended)

**Example:**
```typescript
describe('calculateTotal', () => {
  it('should sum array of numbers', () => {
    const result = calculateTotal([1, 2, 3]);
    expect(result).toBe(6);
  });
});

// Run: FAIL - calculateTotal is not defined
```

**Common Mistakes:**
- Writing implementation before test
- Test passes immediately (not really testing new behavior)
- Test fails for wrong reason (syntax error, missing imports)

---

### GREEN Phase: Make Tests Pass

**Goal:** Write simplest code to make tests pass

**Steps:**
1. Write minimum code needed
2. Don't worry about elegance yet
3. Run test suite to confirm pass
4. Commit the passing code

**Example:**
```typescript
function calculateTotal(numbers: number[]): number {
  return numbers.reduce((sum, n) => sum + n, 0);
}

// Run: PASS - All tests passing
```

**Common Mistakes:**
- Over-engineering the solution
- Adding features not covered by tests
- Skipping tests to "move faster"

---

### REFACTOR Phase: Improve Code

**Goal:** Improve code quality while keeping tests green

**Steps:**
1. Identify code smells
2. Apply refactoring pattern
3. Run tests after each change
4. Revert if tests break
5. Commit after successful refactor

**Refactoring Targets:**
- Remove duplication
- Improve naming
- Extract functions
- Simplify conditionals
- Add type safety

**Example:**
```typescript
// Before
function calculateTotal(numbers: number[]): number {
  let total = 0;
  for (let i = 0; i < numbers.length; i++) {
    total = total + numbers[i];
  }
  return total;
}

// After (refactored)
function calculateTotal(numbers: number[]): number {
  return numbers.reduce((sum, num) => sum + num, 0);
}

// Run: PASS - Tests still passing
```

---

## Test Structure

### AAA Pattern

**Arrange-Act-Assert:**

```typescript
it('should do something', () => {
  // Arrange: Set up test data and dependencies
  const input = [1, 2, 3];
  const expected = 6;

  // Act: Execute the function under test
  const result = calculateTotal(input);

  // Assert: Verify the result
  expect(result).toBe(expected);
});
```

---

## Testing Patterns

### Testing Async Functions

```typescript
it('should fetch user data', async () => {
  // Arrange
  const userId = '123';
  const mockUser = { id: '123', name: 'Test User' };

  // Act
  const user = await userService.getUser(userId);

  // Assert
  expect(user).toEqual(mockUser);
});
```

### Testing Error Cases

```typescript
it('should throw error when user not found', async () => {
  // Arrange
  const invalidId = 'invalid';

  // Act & Assert
  await expect(userService.getUser(invalidId))
    .rejects
    .toThrow('User not found');
});
```

### Testing Edge Cases

```typescript
describe('edge cases', () => {
  it('should handle empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('should handle negative numbers', () => {
    expect(calculateTotal([-1, -2, -3])).toBe(-6);
  });

  it('should handle single element', () => {
    expect(calculateTotal([42])).toBe(42);
  });
});
```

---

## Mocking Dependencies

### Using Jest Mocks

```typescript
// Mock external dependency
jest.mock('../database');

describe('UserService', () => {
  it('should call database with correct params', async () => {
    // Arrange
    const mockFind = jest.fn().mockResolvedValue({ id: '123' });
    database.users.find = mockFind;

    // Act
    await userService.getUser('123');

    // Assert
    expect(mockFind).toHaveBeenCalledWith({ id: '123' });
  });
});
```

---

## Coverage Guidelines

### Minimum Coverage

- **Statements**: 80%
- **Branches**: 75%
- **Functions**: 80%
- **Lines**: 80%

### What to Test

**Always test:**
- Happy paths (normal operation)
- Error cases (validation failures, exceptions)
- Edge cases (empty inputs, boundaries, nulls)
- Integration points (external dependencies)

**Don't test:**
- External libraries (already tested)
- Trivial getters/setters
- Framework code

---

## TDD Anti-Patterns

### 1. Testing Implementation Details

**Bad:**
```typescript
it('should call getUserById with correct id', () => {
  // Testing HOW it works, not WHAT it does
  expect(mockGetUserById).toHaveBeenCalledWith('123');
});
```

**Good:**
```typescript
it('should return user data for valid id', () => {
  // Testing behavior, not implementation
  const user = service.getUser('123');
  expect(user).toEqual({ id: '123', name: 'Test' });
});
```

### 2. Writing Tests After Code

Defeats the purpose of TDD. Write tests FIRST.

### 3. Skipping RED Phase

If test passes immediately, you're not testing new behavior.

### 4. Large Test Suites That Take Forever

Break into smaller, focused tests. Use mocks to avoid slow operations.

---

## Quick Reference

**TDD Cycle:**
1. Write failing test (RED)
2. Write code to pass test (GREEN)
3. Refactor code (while keeping tests green)
4. Repeat

**Test Structure:**
1. Arrange (setup)
2. Act (execute)
3. Assert (verify)

**Coverage Target:**
- 80% minimum
- Focus on critical paths first

**Remember:**
- Tests drive design
- Simple solutions first
- Refactor for clarity
- Tests document behavior
