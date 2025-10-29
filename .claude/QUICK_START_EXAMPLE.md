# Quick Start Example: User Authentication

This example walks you through creating your first task using BMAD Enhanced skills.

---

## Scenario

**Feature:** User authentication with email and password

**Requirements:**
- Users can sign up with email and password
- Passwords must meet security requirements (8+ chars, complexity)
- Duplicate emails prevented
- Users can log in and receive JWT token

---

## Step 1: Configure Project (One-Time Setup)

Edit `.claude/config.yaml` if needed:

```yaml
project:
  name: My Application
  type: greenfield

documentation:
  architecture: docs/architecture.md
  standards: docs/standards.md

development:
  alwaysLoadFiles:
    - docs/standards.md
```

If you don't have architecture docs yet, create minimal ones:

```bash
mkdir -p docs
```

**docs/architecture.md:**
```markdown
# Architecture

## Tech Stack
- Node.js 20+
- Express.js for API
- PostgreSQL database
- Prisma ORM
- JWT for authentication
- bcrypt for password hashing

## Project Structure
```
src/
├── routes/       # API endpoints
├── services/     # Business logic
├── models/       # Data models
├── middleware/   # Auth, validation
└── utils/        # Helpers
```

## Data Models

### User
- id: UUID (primary key)
- email: string (unique, lowercase)
- password: string (bcrypt hashed, cost 12)
- createdAt: timestamp
- updatedAt: timestamp

## API Patterns

### Authentication Endpoints
- POST /api/auth/signup - Create new user
- POST /api/auth/login - Authenticate user

Request format:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

Response format (201):
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  },
  "token": "jwt_token"
}
```

## Security Standards
- All passwords hashed with bcrypt, cost 12
- Input validation with Zod schemas
- Rate limiting on auth endpoints: 5 req/min
- SQL injection prevented via Prisma ORM
- JWT expiry: 24 hours
```

**docs/standards.md:**
```markdown
# Coding Standards

## Testing
- Framework: Jest + Supertest
- Coverage target: >80%
- Test levels:
  - Unit: Business logic, validation
  - Integration: API endpoints with test DB
  - E2E: Complete user journeys

## File Organization
- One model per file
- One route per file
- Co-locate tests with code (\_\_tests\_\_ folder)

## Error Handling
- Use try-catch for async operations
- Return consistent error format
- Log errors with context

## Code Style
- Use TypeScript strict mode
- ESLint + Prettier for formatting
- Async/await (no callbacks)
```

---

## Step 2: Create Task Specification

Ask Claude Code:

```
Use the planning skill at .claude/skills/planning/create-task-spec.md
to create a task specification for user authentication (signup and login).

Requirements:
- Users can sign up with email and password
- Password must be 8+ chars with uppercase, lowercase, number, special char
- Duplicate emails prevented with 409 error
- Users can log in and receive JWT token
- Failed login returns 401 error

This is a P1 (High Priority) task for the "Auth" epic.
```

### What the Planning Skill Will Do

1. **Gather Requirements:**
   - Asks you to confirm the user story
   - Validates acceptance criteria
   - Confirms priority

2. **Load Context:**
   - Reads docs/architecture.md
   - Reads docs/standards.md
   - Extracts User model, API patterns, security standards

3. **Create Task Breakdown:**
   ```markdown
   - [ ] Task 1: Create user model and validation (AC: 1, 2)
     - [ ] Define User type in src/types/user.ts
     - [ ] Create Zod validation schema
     - [ ] Create Prisma schema
     - [ ] Write unit tests for validation
     - [ ] Validate: Model matches architecture spec

   - [ ] Task 2: Implement signup service (AC: 1, 2, 3)
     - [ ] Create signup.service.ts
     - [ ] Implement password hashing
     - [ ] Add duplicate email check
     - [ ] Write unit tests
     - [ ] Validate: All edge cases covered

   - [ ] Task 3: Create signup endpoint (AC: 1, 3)
     - [ ] Add POST /api/auth/signup route
     - [ ] Add request validation middleware
     - [ ] Implement error handling
     - [ ] Write integration tests
     - [ ] Validate: API matches spec

   - [ ] Task 4: Implement login service (AC: 4, 5)
     - [ ] Create login.service.ts
     - [ ] Implement password verification
     - [ ] Generate JWT token
     - [ ] Write unit tests
     - [ ] Validate: Security requirements met

   - [ ] Task 5: Create login endpoint (AC: 4, 5)
     - [ ] Add POST /api/auth/login route
     - [ ] Add request validation
     - [ ] Implement rate limiting
     - [ ] Write integration tests
     - [ ] Validate: API matches spec

   - [ ] Task 6: Write comprehensive tests
     - [ ] Write E2E test for signup flow
     - [ ] Write E2E test for login flow
     - [ ] Run full test suite
     - [ ] Verify >80% coverage
   ```

4. **Generate Task File:**
   - Creates `.claude/tasks/task-001-user-authentication.md`
   - Status: "Draft"
   - All context embedded with source references

5. **Present for Approval:**
   ```markdown
   ## Task Specification Created

   **File:** .claude/tasks/task-001-user-authentication.md
   **Status:** Draft
   **Priority:** P1 (High)

   **Context Embedded:**
   - User model with Zod validation [Source: docs/architecture.md#data-models]
   - API spec: POST /api/auth/signup and /api/auth/login [Source: docs/architecture.md#api-patterns]
   - Security: bcrypt cost 12, rate limiting [Source: docs/standards.md#security]
   - Testing: Jest + Supertest, >80% coverage [Source: docs/standards.md#testing]

   **Task Breakdown:**
   - 6 main tasks with 23 subtasks total
   - Maps to all 5 acceptance criteria
   - Includes comprehensive test coverage

   Ready to review? (yes/no)
   ```

### Your Action

Review the generated file:

```bash
cat .claude/tasks/task-001-user-authentication.md
```

If it looks good, update the status:

```markdown
## Status

Approved  # Changed from Draft
```

---

## Step 3: Execute Implementation

Ask Claude Code:

```
Use the implementation skill at .claude/skills/implementation/execute-task.md
to execute .claude/tasks/task-001-user-authentication.md
```

### What the Implementation Skill Will Do

1. **Load Task Spec:**
   - Reads entire task file
   - Verifies status is "Approved"
   - Loads docs/standards.md (always-load file)
   - Updates status to "InProgress"

2. **Execute Task 1: Create user model**
   ```
   Creating src/types/user.ts...
   Creating src/schemas/user.schema.ts...
   Creating prisma/schema.prisma (User model)...
   Writing tests src/schemas/__tests__/user.schema.test.ts...
   Running tests... ✓ 8 tests passed
   ✓ Task 1 complete
   ```

3. **Execute Task 2: Signup service**
   ```
   Creating src/services/auth/signup.service.ts...
   Implementing password hashing with bcrypt cost 12...
   Adding duplicate email check...
   Writing tests... ✓ 10 tests passed
   ✓ Task 2 complete
   ```

4. **Execute Task 3: Signup endpoint**
   ```
   Creating src/routes/auth/signup.ts...
   Adding validation middleware...
   Writing integration tests... ✓ 5 tests passed
   ✓ Task 3 complete
   ```

5. **Execute Task 4: Login service**
   ```
   Creating src/services/auth/login.service.ts...
   Implementing JWT generation...
   Writing tests... ✓ 8 tests passed
   ✓ Task 4 complete
   ```

6. **Execute Task 5: Login endpoint**
   ```
   Creating src/routes/auth/login.ts...
   Adding rate limiting middleware...
   Writing integration tests... ✓ 5 tests passed
   ✓ Task 5 complete
   ```

7. **Execute Task 6: Comprehensive tests**
   ```
   Writing E2E tests... ✓ 4 tests passed
   Running full test suite... ✓ 40 tests passed
   Coverage: 89% statements, 85% branches
   ✓ Task 6 complete
   ```

8. **Final Validation:**
   ```
   All tests passing: 40/40 ✓
   Coverage: 89% (exceeds 80% target) ✓
   Linter passing ✓
   All acceptance criteria met ✓
   ```

9. **Update Implementation Record:**
   ```markdown
   ### Agent Model Used
   claude-sonnet-4-5-20250929

   ### Completion Notes
   - Implemented user authentication with signup and login
   - All security requirements met (bcrypt, rate limiting, JWT)
   - Added extra validation for email format edge cases
   - 40 tests written across unit/integration/E2E
   - All acceptance criteria validated

   ### Files Modified
   **Created:**
   - src/types/user.ts
   - src/schemas/user.schema.ts
   - src/services/auth/signup.service.ts
   - src/services/auth/login.service.ts
   - src/routes/auth/signup.ts
   - src/routes/auth/login.ts
   - src/middleware/auth.middleware.ts
   - src/middleware/rateLimit.middleware.ts
   - prisma/schema.prisma (User model)
   - [12 test files]

   **Modified:**
   - src/routes/index.ts (added auth routes)

   ### Testing Results
   - Unit Tests: 23 tests, 23 passed
   - Integration Tests: 13 tests, 13 passed
   - E2E Tests: 4 tests, 4 passed
   - Total: 40 tests, 40 passed
   - Coverage: 89% statements, 85% branches, 92% functions
   ```

10. **Present Completion:**
    ```markdown
    ## Implementation Complete - Ready for Review

    ✓ All 6 tasks complete (23 subtasks)
    ✓ 40 tests passing (23 unit, 13 integration, 4 E2E)
    ✓ 89% code coverage
    ✓ All acceptance criteria met

    Status updated to "Review"

    Quality review needed? (yes/no)
    ```

---

## Step 4: Quality Review

Ask Claude Code:

```
Use the quality skill at .claude/skills/quality/review-task.md
to review .claude/tasks/task-001-user-authentication.md
```

### What the Quality Skill Will Do

1. **Requirements Traceability:**
   ```markdown
   ✓ AC1: Users can sign up - FULL COVERAGE
     - Implementation: src/services/auth/signup.service.ts:15-67
     - Tests: 8 unit + 5 integration + 2 E2E = 15 tests

   ✓ AC2: Password security - FULL COVERAGE
     - Implementation: src/schemas/user.schema.ts:12-28
     - Tests: 10 tests covering all requirements

   ✓ AC3: Duplicate prevention - FULL COVERAGE
     - Implementation: src/services/auth/signup.service.ts:45-52
     - Tests: 3 tests (unit + integration)

   ✓ AC4: Login with JWT - FULL COVERAGE
     - Implementation: src/services/auth/login.service.ts:18-56
     - Tests: 8 unit + 5 integration + 2 E2E = 15 tests

   ✓ AC5: Failed login handling - FULL COVERAGE
     - Implementation: src/services/auth/login.service.ts:33-41
     - Tests: 5 tests covering error cases

   **Summary:** 5/5 acceptance criteria fully tested
   ```

2. **Test Coverage Analysis:**
   ```markdown
   - Total Tests: 40 (23 unit, 13 integration, 4 E2E)
   - Coverage: 89% statements, 85% branches, 92% functions
   - Quality: Excellent (reliable, maintainable, fast)
   - Gaps: None critical
   ```

3. **NFR Assessment:**
   ```markdown
   **Security:** ✓ PASS
   - Password hashing: bcrypt cost 12 ✓
   - Input validation: Zod schemas ✓
   - SQL injection: Prisma ORM ✓
   - Rate limiting: 5 req/min ✓
   - JWT security: 24hr expiry, HS256 ✓

   **Performance:** ✓ PASS
   - API response: 132ms avg (under 200ms target) ✓
   - Database queries: Optimized (no N+1) ✓
   - Bcrypt cost balanced: 12 adds ~150ms ✓

   **Reliability:** ✓ PASS
   - Error handling: Comprehensive try-catch ✓
   - Logging: Structured with context ✓
   - Validation: All inputs validated ✓

   **Maintainability:** ✓ PASS
   - Standards compliance: ESLint passing ✓
   - Test coverage: 89% (exceeds 80% target) ✓
   - Documentation: API documented ✓
   ```

4. **Quality Gate Decision:**
   ```markdown
   **Status:** PASS

   **Rationale:**
   Implementation successfully delivers all functional requirements
   with comprehensive test coverage (89%) and strong adherence to
   security and performance standards. No critical issues identified.

   All acceptance criteria validated through 40 tests across
   unit/integration/E2E levels. Security requirements fully met
   (password hashing, rate limiting, input validation). Performance
   targets achieved. Code quality excellent.

   Recommended for immediate merge.
   ```

5. **Generate Quality Gate:**
   - Creates `.claude/quality/gates/task-001-gate.yaml`
   - Updates task file Quality Review section

6. **Present Summary:**
   ```markdown
   ## Quality Review Complete

   **Quality Gate Decision: PASS**

   ### Requirements Traceability
   ✓ 5/5 acceptance criteria fully tested

   ### Test Coverage
   ✓ 40 tests (23 unit, 13 integration, 4 E2E)
   ✓ 89% coverage (exceeds 80% target)

   ### Non-Functional Requirements
   ✓ Security: PASS (all requirements met)
   ✓ Performance: PASS (132ms avg, under target)
   ✓ Reliability: PASS (comprehensive error handling)
   ✓ Maintainability: PASS (standards compliant, documented)

   ### Recommendation
   ✓ Approve for immediate merge
   ✓ No action items required

   **What would you like to do?**
   - (a) Mark task "Done" and commit
   - (b) Review gate file first
   ```

---

## Step 5: Complete and Commit

Mark the task complete:

**Edit `.claude/tasks/task-001-user-authentication.md`:**
```markdown
## Status

Done  # Changed from Review
```

Commit your changes:

```bash
git add .
git commit -m "feat: add user authentication (signup and login)

- Implement user signup with email/password validation
- Implement user login with JWT token generation
- Add password security requirements (8+ chars, complexity)
- Prevent duplicate emails with unique constraint
- Add rate limiting on auth endpoints (5 req/min)
- Comprehensive test coverage: 40 tests, 89% coverage
- All security requirements met (bcrypt, validation, JWT)

Quality Gate: PASS
Task: .claude/tasks/task-001-user-authentication.md
Gate: .claude/quality/gates/task-001-gate.yaml

🤖 Generated with BMAD Enhanced
"
```

---

## Summary

**What You Accomplished:**

✅ **Planned** a feature with hyper-detailed context embedding
✅ **Implemented** sequentially with validation at each step
✅ **Tested** comprehensively (40 tests, 89% coverage)
✅ **Reviewed** systematically with quality gate
✅ **Documented** completely with audit trail

**Time Saved:**
- No mid-implementation context searching
- No ambiguous requirements
- No missed test cases
- No quality review debates

**Quality Gained:**
- All requirements traceable to tests
- Security requirements validated
- Performance measured
- Clear audit trail

---

## Next Steps

1. **Try Another Feature:**
   - Use what you learned
   - Build on established patterns
   - Note learnings in completion records

2. **Customize Configuration:**
   - Adjust quality thresholds
   - Add more always-load files
   - Configure halt conditions

3. **Provide Feedback:**
   - What worked well?
   - What was confusing?
   - What should be improved?

---

**Congratulations! You've completed your first BMAD Enhanced workflow!** 🎉
