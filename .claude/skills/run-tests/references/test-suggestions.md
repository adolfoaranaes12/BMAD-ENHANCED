# Test Suggestions Guide

## Purpose

Generate concrete, actionable test suggestions for identified coverage gaps.

---

## Suggestion Format

### Complete Suggestion Template

```markdown
### Gap N: [Descriptive Name]

**File:** `path/to/file.ts:lines`
**Category:** [Error Handling|Edge Case|Rare Branch|Dead Code]
**Criticality:** [CRITICAL|HIGH|MEDIUM|LOW]

**Uncovered Code:**
```language
[actual code that's uncovered]
```

**Why Test:**
[1-2 sentences explaining why this should be tested]

**Impact if Untested:**
[1-2 sentences on consequences]

**Suggested Test:**
```language
[complete, runnable test example]
```
```

---

## Example Suggestions by Category

### 1. Error Handling Suggestion

```markdown
### Gap 1: Database Connection Failure

**File:** `src/controllers/auth.controller.ts:48-50`
**Category:** Error Handling
**Criticality:** HIGH

**Uncovered Code:**
```typescript
if (!isDatabaseConnected()) {
  return res.status(503).json({ error: 'Service unavailable' });
}
```

**Why Test:**
Database failures are expected in production environments. This error path ensures proper HTTP status codes and graceful degradation.

**Impact if Untested:**
- Users may receive wrong status codes
- Monitoring alerts may not trigger
- Client retry logic may not work correctly

**Suggested Test:**
```typescript
describe('auth.controller', () => {
  it('should return 503 when database is unavailable', async () => {
    // Arrange
    jest.spyOn(db, 'isConnected').mockReturnValue(false);

    // Act
    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'password123' });

    // Assert
    expect(response.status).toBe(503);
    expect(response.body).toEqual({ error: 'Service unavailable' });
  });
});
```
```

---

### 2. Edge Case Suggestion

```markdown
### Gap 2: Session Expiration

**File:** `src/middleware/auth.middleware.ts:67-69`
**Category:** Edge Case
**Criticality:** HIGH

**Uncovered Code:**
```typescript
if (user.lastLogin && Date.now() - user.lastLogin > MAX_SESSION_AGE) {
  return res.status(401).json({ error: 'Session expired' });
}
```

**Why Test:**
Session expiration is a critical security boundary. Users must be logged out after inactivity periods.

**Impact if Untested:**
- Security vulnerability (stale sessions)
- Poor user experience (unexpected logouts or no logouts)
- Compliance issues (session timeout requirements)

**Suggested Test:**
```typescript
describe('auth middleware', () => {
  it('should reject requests with expired sessions', async () => {
    // Arrange
    const expiredDate = Date.now() - (MAX_SESSION_AGE + 1000);
    const token = generateToken({ userId: '123', lastLogin: expiredDate });

    // Act
    const response = await request(app)
      .get('/api/protected')
      .set('Authorization', `Bearer ${token}`);

    // Assert
    expect(response.status).toBe(401);
    expect(response.body.error).toBe('Session expired');
  });

  it('should accept requests with valid sessions', async () => {
    // Arrange
    const recentDate = Date.now() - 1000; // 1 second ago
    const token = generateToken({ userId: '123', lastLogin: recentDate });

    // Act
    const response = await request(app)
      .get('/api/protected')
      .set('Authorization', `Bearer ${token}`);

    // Assert
    expect(response.status).toBe(200);
  });
});
```
```

---

### 3. Unexpected Error Suggestion

```markdown
### Gap 3: Unexpected Error Handling

**File:** `src/services/auth.service.ts:112-115`
**Category:** Error Handling
**Criticality:** MEDIUM

**Uncovered Code:**
```typescript
catch (error) {
  console.error('Unexpected error during login:', error);
  throw new InternalServerError('Authentication failed');
}
```

**Why Test:**
Catch-all error handlers ensure unexpected errors are logged and handled gracefully.

**Impact if Untested:**
- Unknown if error logging works
- Error response format may be incorrect
- Debugging production issues may be difficult

**Suggested Test:**
```typescript
describe('auth.service', () => {
  it('should handle unexpected errors gracefully', async () => {
    // Arrange
    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation();
    jest.spyOn(db, 'findByEmail').mockRejectedValue(new Error('Unexpected DB error'));

    // Act & Assert
    await expect(
      authService.login('test@example.com', 'password123')
    ).rejects.toThrow(InternalServerError);

    expect(consoleErrorSpy).toHaveBeenCalledWith(
      'Unexpected error during login:',
      expect.any(Error)
    );

    consoleErrorSpy.mockRestore();
  });
});
```
```

---

### 4. Branch Coverage Suggestion

```markdown
### Gap 4: Rate Limit Exceeded

**File:** `src/middleware/rate-limiter.ts:45-47`
**Category:** Edge Case
**Criticality:** MEDIUM

**Uncovered Code:**
```typescript
if (attempts > MAX_ATTEMPTS) {
  return res.status(429).json({ error: 'Too many requests', retryAfter: WINDOW_MS });
}
```

**Why Test:**
Rate limiting is critical for API protection and fair usage enforcement.

**Impact if Untested:**
- DoS vulnerability (no rate limiting)
- Poor user experience (rate limit message format)
- Client retry logic may not work

**Suggested Test:**
```typescript
describe('rate limiter', () => {
  it('should block requests after exceeding rate limit', async () => {
    // Arrange
    const email = 'test@example.com';

    // Act - Make MAX_ATTEMPTS + 1 requests
    for (let i = 0; i < MAX_ATTEMPTS; i++) {
      await request(app)
        .post('/api/auth/login')
        .send({ email, password: 'wrong' });
    }

    const finalResponse = await request(app)
      .post('/api/auth/login')
      .send({ email, password: 'wrong' });

    // Assert
    expect(finalResponse.status).toBe(429);
    expect(finalResponse.body.error).toBe('Too many requests');
    expect(finalResponse.body.retryAfter).toBe(WINDOW_MS);
  });
});
```
```

---

## Suggestion Prioritization

### Priority 1: Critical Security & Data

**Examples:**
- Authentication bypass scenarios
- Authorization edge cases
- Data validation failures
- Payment processing errors

**Template:**
```markdown
🔴 CRITICAL: [Name]
Must test before production deployment.
Security/data integrity at risk.
```

---

### Priority 2: Expected Errors

**Examples:**
- Database connection failures
- Network timeouts
- Invalid input handling
- Third-party API failures

**Template:**
```markdown
🟠 HIGH: [Name]
Should test before next release.
Production failure scenario.
```

---

### Priority 3: Business Logic

**Examples:**
- Edge case calculations
- State transition edge cases
- Complex conditional branches
- Rare but valid user paths

**Template:**
```markdown
🟡 MEDIUM: [Name]
Nice to test, improves reliability.
Uncommon but valid scenario.
```

---

### Priority 4: Optional Coverage

**Examples:**
- Debug code
- Development-only paths
- Logging statements
- Trivial getters/setters

**Template:**
```markdown
🟢 LOW: [Name]
Optional, low value test.
Rarely executed code.
```

---

## Batch Suggestion Format

When suggesting multiple tests:

```markdown
## Suggested Tests to Improve Coverage

I've identified 5 coverage gaps. Here are the suggested tests by priority:

### High Priority (3 tests)

These handle expected production failures:

1. **Database Connection Failure** (auth.controller.ts:48-50)
2. **Session Expiration** (auth.middleware.ts:67-69)
3. **Rate Limit Exceeded** (rate-limiter.ts:45-47)

### Medium Priority (2 tests)

These improve error handling robustness:

4. **Unexpected Error Logging** (auth.service.ts:112-115)
5. **Audit Log Failure** (audit.service.ts:34-36)

---

### 📝 Implementation Estimate

- High priority: ~30 minutes (3 tests)
- Medium priority: ~20 minutes (2 tests)
- Total: ~50 minutes

**Coverage improvement:** 87% → 96% (+9%)

Would you like me to implement these tests?
```

---

## Test Writing Best Practices

**1. Follow AAA Pattern**
- Arrange: Set up test data and mocks
- Act: Execute the code under test
- Assert: Verify expected outcomes

**2. Use Descriptive Names**
```typescript
// ✅ Good
it('should return 503 when database is unavailable', ...)

// ❌ Bad
it('test database error', ...)
```

**3. Test One Thing**
```typescript
// ✅ Good - tests one scenario
it('should return 401 for wrong password', ...)

// ❌ Bad - tests multiple things
it('should handle various auth errors', ...)
```

**4. Use Realistic Data**
```typescript
// ✅ Good
const user = { email: 'test@example.com', password: 'SecurePass123!' };

// ❌ Bad
const user = { email: 'a', password: 'b' };
```

**5. Clean Up Resources**
```typescript
afterEach(() => {
  jest.clearAllMocks();
});
```

---

## Quick Reference

**Suggestion Template:**
1. File + lines
2. Category + criticality
3. Code snippet
4. Why test (1-2 sentences)
5. Impact (1-2 sentences)
6. Complete test example

**Prioritization:**
- 🔴 CRITICAL: Security, data integrity
- 🟠 HIGH: Expected errors, production scenarios
- 🟡 MEDIUM: Business logic, edge cases
- 🟢 LOW: Debug, dev-only, trivial code

---

*Part of run-tests skill - Development Suite*
