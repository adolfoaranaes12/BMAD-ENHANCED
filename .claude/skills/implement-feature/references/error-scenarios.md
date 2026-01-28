# Error Scenarios

## Purpose

Common error scenarios during TDD implementation and how to handle them.

---

## Scenario 1: Task Spec Not Found

### Error

```
Task specification not found at workspace/tasks/task-auth-002.md
```

### Why This Happens

- Task ID is incorrect
- Task spec hasn't been created yet
- File was moved or deleted
- Wrong workspace directory

### How to Handle

**Step 1: Verify Task ID**
```bash
# Check if file exists
ls workspace/tasks/task-auth-*.md

# Check exact filename
```

**Step 2: If File Missing**
- Task spec must be created first
- Use `create-task-spec` skill to create it
- Halt implementation until spec exists

**Step 3: Resolution**
```bash
# Create task spec
@alex *create-task-spec --from-user-story story-auth-001

# Then retry implementation
@james *implement task-auth-002
```

---

## Scenario 2: Tests Failing After Implementation

### Error

```
✗ 4 failing
✓ 8 passing

Failures:
1. "should return 401 for wrong password" - Expected 401, got 500
2. "should return 400 for missing email" - Expected 400, got 500
```

### Why This Happens

- Missing error handling in controller
- Unhandled exceptions bubbling up
- Middleware not applied correctly
- Test expectations incorrect

### How to Handle

**Step 1: Review Error Messages**
```typescript
// Check what's actually happening
console.error('Error details:', error);
```

**Step 2: Add Error Handling**
```typescript
// Before
export const login = async (req: Request, res: Response) => {
  const user = await authService.authenticate(email, password);
  // Error: authenticate() throws, not caught
};

// After
export const login = async (req: Request, res: Response) => {
  try {
    const user = await authService.authenticate(email, password);
    // ...
  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({ error: 'Internal error' });
  }
};
```

**Step 3: Re-run Tests**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --output json
```

---

## Scenario 3: Coverage Below Threshold

### Error

```
Test coverage 72% below threshold 80%
```

### Why This Happens

- Not all code paths tested
- Missing edge case tests
- Error handling not tested
- Setup/teardown code not covered

### How to Handle

**Step 1: Identify Uncovered Code**
```bash
# Run coverage report
npm test -- --coverage

# Look for red/yellow lines in report
```

**Step 2: Add Missing Tests**
```typescript
// Example: Missing error path test
it('should handle database connection error', async () => {
  (User.findByEmail as jest.Mock).mockRejectedValue(
    new Error('Database unavailable')
  );

  await expect(
    authService.findUserByEmail('test@example.com')
  ).rejects.toThrow('Database unavailable');
});
```

**Step 3: Verify Coverage**
```bash
# Re-run tests with coverage
npm test -- --coverage

# Check if now >= 80%
```

---

## Scenario 4: Ambiguous Requirements

### Error

```
Implementation blocked: Requirements unclear

AC-5: "Rate limiting should be implemented"

Questions:
- Rate limit per what? (IP? User? Email?)
- What limit? (5, 10, 100 requests?)
- What time window? (minute, hour, day?)
- What happens after limit? (Block? Delay? Captcha?)
```

### Why This Happens

- Acceptance criteria too vague
- Missing technical details
- Conflicting requirements
- Unstated assumptions

### How to Handle

**Step 1: Document Questions**
```markdown
## Clarification Needed

**AC-5: Rate Limiting**

Questions:
1. Rate limit scope: Per IP address or per user account?
2. Rate limit count: How many attempts allowed?
3. Time window: Per minute, hour, or day?
4. Blocking behavior: Temporary block or permanent?
5. Reset mechanism: Automatic or manual?
```

**Step 2: Request Refinement**
```bash
@alex *refine task-auth-002 --focus rate-limiting
```

**Step 3: Halt Implementation**
- Cannot proceed without clarification
- Mark task as "Blocked"
- Wait for updated spec

---

## Scenario 5: Missing Dependencies

### Error

```
Cannot find module '../models/user.model'
```

### Why This Happens

- Dependency task not implemented yet
- File referenced doesn't exist
- Import path incorrect
- Circular dependency

### How to Handle

**Step 1: Identify Missing Dependency**
```typescript
// Error: User model doesn't exist
import { User } from '../models/user.model';

// Check if file exists
ls src/models/user.model.ts  // File not found
```

**Step 2: Check Task Dependencies**
```markdown
## Dependencies

This task (task-auth-002-login) depends on:
- task-auth-001-signup (creates User model)

Status: task-auth-001 is NOT complete
```

**Step 3: Resolution Options**

**Option A: Implement Dependency First**
```bash
@james *implement task-auth-001
# Then retry this task
@james *implement task-auth-002
```

**Option B: Expand Scope (with user approval)**
```bash
# Ask user
"Task auth-002 depends on User model from auth-001.
Should I:
1. Implement auth-001 first (recommended)
2. Create minimal User model as part of this task (expands scope)"

# If user approves option 2, proceed
```

---

## Scenario 6: Tests Pass But Feature Doesn't Work

### Error

```
All tests passing (12/12)
But manual testing shows login not working
```

### Why This Happens

- Tests mock too much (not testing real behavior)
- Integration tests missing
- Test data doesn't match production data
- Environment-specific issues

### How to Handle

**Step 1: Review Test Mocks**
```typescript
// Problem: Over-mocking
jest.mock('../services/auth.service');  // Mocking entire service
// Tests pass but real service broken

// Solution: Mock only external dependencies
jest.mock('../models/user.model');      // Mock only database
// Test real service logic
```

**Step 2: Add Integration Tests**
```typescript
// Add end-to-end test without mocks
it('should login with real database', async () => {
  // Use real database (test database)
  await User.create({ email: 'test@example.com', password: 'hashed' });

  const response = await request(app)
    .post('/api/auth/login')
    .send({ email: 'test@example.com', password: 'password' });

  expect(response.status).toBe(200);
});
```

**Step 3: Manual Testing**
```bash
# Start dev server
npm run dev

# Test endpoint manually
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password"}'
```

---

## Quick Reference

| Error | Likely Cause | Resolution |
|-------|--------------|------------|
| File not found | Missing dependency or wrong path | Check imports, implement dependency |
| Tests failing | Missing error handling | Add try-catch blocks |
| Low coverage | Missing test cases | Add tests for uncovered paths |
| Unclear requirements | Vague acceptance criteria | Request refinement |
| Tests pass but broken | Over-mocking | Add integration tests |
| Timeout | Long-running operation | Optimize or increase timeout |
| Memory leak | Event listeners not cleaned | Add cleanup in afterEach |
| Flaky tests | Race conditions | Add await, fix timing issues |

---

*Part of implement-feature skill - Development Suite*
