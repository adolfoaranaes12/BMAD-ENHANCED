# Task Execution Guide

## Purpose

Execute tasks and subtasks sequentially with validation gates, following TDD and BMAD patterns.

---

## Step 2: Execute Current Task

### Core Execution Loop

**For each task in sequential order:**

1. Announce current task
2. Execute each subtask
3. Validate task completion
4. Update checkboxes and documentation
5. Move to next task

---

## Task Execution Pattern

### 1. Announce Current Task

**Format:**
```markdown
## Executing Task N: [Task Name] (AC: X, Y)

**Maps to Acceptance Criteria:** AC1, AC2
**Subtasks:** M subtasks
**Dependencies:** [Previous tasks if any]

**Subtask List:**
- [ ] Subtask N.1: [Description]
- [ ] Subtask N.2: [Description]
- [ ] Subtask N.3: [Description]
...
```

**Purpose:**
- Clear communication of current work
- Maps task to acceptance criteria
- Shows overall task structure

---

### 2. Execute Each Subtask

**For each subtask in order:**

#### a. Implement Subtask

**Read context from task spec:**
```markdown
### Data Models (from task spec context)
User interface:
- id: string (UUID)
- email: string (validated)
- password: string (hashed)
- createdAt: Date
- updatedAt: Date
```

**Create/modify files:**
```typescript
// src/types/user.ts
export interface User {
  id: string;
  email: string;
  password: string;
  createdAt: Date;
  updatedAt: Date;
}
```

**Follow coding standards:**
- Use patterns from always-load files
- Follow naming conventions
- Use established patterns from previous tasks

#### b. If Subtask is "Write tests"

**Write comprehensive tests:**

**Unit Tests:**
```typescript
// src/schemas/__tests__/user.schema.test.ts
describe('User Schema Validation', () => {
  it('should accept valid email', () => {
    const result = userSchema.safeParse({
      email: 'test@example.com',
      password: 'SecurePass123!'
    });
    expect(result.success).toBe(true);
  });

  it('should reject invalid email', () => {
    const result = userSchema.safeParse({
      email: 'not-an-email',
      password: 'SecurePass123!'
    });
    expect(result.success).toBe(false);
  });

  // Test edge cases, boundaries, error conditions
});
```

**Integration Tests:**
```typescript
// src/services/auth/__tests__/signup.service.integration.test.ts
describe('Signup Service Integration', () => {
  it('should create user with valid data', async () => {
    const user = await signupService.createUser({
      email: 'test@example.com',
      password: 'SecurePass123!'
    });

    expect(user.id).toBeDefined();
    expect(user.email).toBe('test@example.com');
  });

  it('should prevent duplicate emails', async () => {
    await signupService.createUser({
      email: 'test@example.com',
      password: 'pass1'
    });

    await expect(
      signupService.createUser({
        email: 'test@example.com',
        password: 'pass2'
      })
    ).rejects.toThrow('Email already exists');
  });
});
```

**Run Tests:**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path src/schemas/__tests__/ \
  --framework auto \
  --output json
```

**Verify all tests pass** before marking subtask complete.

#### c. If Subtask is "Validate"

**Run relevant tests:**
```bash
# Unit tests for this component
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path src/types/ \
  --framework auto

# Integration tests if applicable
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path src/services/auth/__tests__/ \
  --framework auto
```

**Run linter/formatter:**
```bash
npm run lint
npm run format:check
```

**Verify output matches acceptance criteria:**
- Check AC1: User can signup ✅
- Check AC2: Password security ✅
- Check AC3: Duplicate prevention ✅

**Check against technical constraints:**
- Performance: Response time <200ms ✅
- Security: Passwords hashed with bcrypt ✅
- Validation: Email RFC 5322 compliant ✅

#### d. Update Subtask Checkbox

**ONLY mark complete if:**
- Implementation fully complete
- Tests written and passing
- Validation successful
- No errors or warnings

**Edit Task File:**
- Change `- [ ] Subtask N.M: Description`
- To `- [x] Subtask N.M: Description`

**Example:**
```markdown
- [x] Task 1: Create user model
  - [x] Define User interface in src/types/user.ts
  - [x] Create user schema with Zod validation
  - [ ] Add database migration for users table  ← Currently working
```

#### e. Record Implementation Notes

**Update Completion Notes:**
```markdown
### Completion Notes

**Task 1.1 - Define User Interface:**
- Created src/types/user.ts
- Interface includes all required fields from data model
- Added JSDoc comments for clarity

**Task 1.2 - Create Zod Schema:**
- Created src/schemas/user.schema.ts
- Email validation uses custom regex (RFC 5322 compliant)
- Password requirements: min 8 chars, uppercase, lowercase, number, special char
- Discovered edge case: Unicode emails need special handling (added)
```

**Document deviations:**
```markdown
**Deviations from Plan:**
- Added extra validation for unicode emails (not in original spec)
- Reason: Found issue during testing with international emails
- Impact: Slightly longer validation time (~5ms), acceptable trade-off
```

**Note patterns for future:**
```markdown
**Patterns for Future Tasks:**
- Zod schema pattern works well, reuse for other models
- bcrypt cost 12 adds ~150ms, document in API response times
- Email service integration is straightforward, can apply to other notifications
```

---

### 3. After All Subtasks Complete

#### a. Run Task Validation

**Execute all tests for this task:**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path src/types/ \
  --framework auto

python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path src/schemas/ \
  --framework auto
```

**Run full lint check:**
```bash
npm run lint:full
```

**Verify acceptance criteria coverage:**
- AC1: ✅ User can signup (tested in integration tests)
- AC2: ✅ Password security (validated in schema tests)
- AC3: ✅ Duplicate prevention (tested in service tests)
- AC4: ✅ Confirmation email (tested in E2E tests)

#### b. Update Task Checkbox

**Mark task complete:**
```markdown
- [x] Task 1: Create user model
  - [x] Define User interface
  - [x] Create Zod schema
  - [x] Database migration
  - [x] Write unit tests
  - [x] Validate model
```

**ONLY if:**
- All subtasks complete ✅
- All tests passing ✅
- Validation successful ✅
- ACs covered ✅

#### c. Update Implementation Record

**Add files to "Files Modified" section:**
```markdown
### Files Modified

**Created:**
- src/types/user.ts
- src/schemas/user.schema.ts
- migrations/001_create_users.sql
- src/schemas/__tests__/user.schema.test.ts
```

**Add task-specific completion notes:**
```markdown
### Completion Notes

**Task 1 Complete (Create User Model):**
- User interface with all required fields
- Zod schema with comprehensive validation
- Database migration with proper constraints
- 12 unit tests, all passing (94% coverage)
- Unicode email handling added (edge case discovered)
```

---

### 4. Move to Next Task

**After task validation:**
- Proceed to next unchecked task
- Repeat execution pattern
- Continue until all tasks complete

---

## Example Implementation Flow

### Complete Task Execution

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Executing Task 1: Create User Model (AC: 1, 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Subtasks:**
- [ ] 1.1: Define User interface
- [ ] 1.2: Create Zod schema
- [ ] 1.3: Database migration
- [ ] 1.4: Write unit tests
- [ ] 1.5: Validate model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Subtask 1.1: Define User Interface

**Action:** Create src/types/user.ts

**Implementation:**
- Created interface with id, email, password, timestamps
- Added JSDoc documentation
- Exported for use in services

**Validation:** Type checks passing ✅

**Status:** ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Subtask 1.2: Create Zod Schema

**Action:** Create src/schemas/user.schema.ts

**Implementation:**
- Email validation with RFC 5322 regex
- Password requirements: 8+ chars, complexity rules
- Custom error messages for each validation

**Validation:** Schema tests passing (4/4) ✅

**Status:** ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Subtask 1.3: Database Migration

**Action:** Create migrations/001_create_users.sql

**Implementation:**
- Users table with UUID primary key
- Email unique constraint
- Created/updated timestamps
- Proper indexes

**Validation:** Migration runs successfully ✅

**Status:** ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Subtask 1.4: Write Unit Tests

**Action:** Create src/schemas/__tests__/user.schema.test.ts

**Implementation:**
- 12 tests covering validation logic
- Valid/invalid email formats
- Valid/invalid passwords
- Edge cases (empty, special chars, unicode)

**Execution:** 12 tests, 12 passed, 0 failed ✅
**Coverage:** 94% statements, 89% branches ✅

**Status:** ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Subtask 1.5: Validate Model

**Action:** Run all validations

**Validations:**
- Tests: 12/12 passed ✅
- Linter: No issues ✅
- Type check: All types valid ✅
- Architecture match: Model matches spec ✅

**Status:** ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Task 1 Complete ✅

**Summary:**
- 5 subtasks completed
- 12 tests written and passing
- 94% code coverage
- All validations successful

**Files Created:**
- src/types/user.ts
- src/schemas/user.schema.ts
- migrations/001_create_users.sql
- src/schemas/__tests__/user.schema.test.ts

**Moving to Task 2...**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Halt Conditions

**Must halt when:**

1. **3 Consecutive Failures (Same Subtask)**
   ```markdown
   ⚠️ EXECUTION HALTED

   **Reason:** Consecutive Failures
   **Subtask:** 1.3 - Database Migration
   **Attempts:** 3 failures

   **Errors:**
   1. Syntax error in SQL (fixed, failed again)
   2. Foreign key constraint error (attempted fix, failed)
   3. Table already exists error (unclear how to proceed)

   **Need from User:**
   - Should migration be idempotent?
   - Should existing table be dropped?
   - Alternative migration strategy?
   ```

2. **Ambiguous Requirements**
   ```markdown
   ⚠️ EXECUTION HALTED

   **Reason:** Ambiguous Requirements
   **Subtask:** 2.1 - Implement password hashing

   **Issue:** Task spec says "hash passwords securely" but doesn't specify:
   - Which algorithm? (bcrypt, argon2, scrypt?)
   - What cost factor?
   - Should we salt? (Best practice says yes)

   **Need from User:**
   - Confirm hashing algorithm
   - Confirm cost factor
   ```

3. **Missing Dependencies**
   ```markdown
   ⚠️ EXECUTION HALTED

   **Reason:** Missing Dependencies
   **Subtask:** 4.2 - Send confirmation email

   **Issue:** Email service not configured:
   - No SMTP credentials found
   - Email service not documented in task spec
   - Unknown which email provider to use

   **Need from User:**
   - Email service setup instructions
   - Or: Should we mock email service for now?
   ```

4. **Regression Failures**
   ```markdown
   ⚠️ EXECUTION HALTED

   **Reason:** Regression Failures
   **Subtask:** 3.1 - Create signup endpoint

   **Issue:** Existing tests started failing:
   - auth.middleware.test.ts: 2 tests failing
   - User model change broke authentication flow

   **Need from User:**
   - Should we update auth middleware?
   - Should we revert user model changes?
   - Alternative approach?
   ```

---

## Quick Reference

**Task Execution Order:**
1. Announce task
2. Execute subtasks sequentially
3. Validate after each subtask
4. Update checkboxes only when complete
5. Document in Implementation Record
6. Validate entire task
7. Move to next task

**Testing:**
- Write tests before marking "Write tests" subtask complete
- Run tests before marking "Validate" subtask complete
- All tests must pass before task checkbox update

**Halt at 3 failures:**
- Same subtask, 3 consecutive attempts
- Present error and ask user for guidance

---

*Part of execute-task skill - Implementation Suite*
