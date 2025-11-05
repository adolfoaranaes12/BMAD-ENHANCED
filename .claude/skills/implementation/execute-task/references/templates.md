# Execute Task Templates and Output Formats

All output formats, examples, and templates for the execute-task skill.

---

## Step 0: Load Configuration and Task Specification

### Command Examples

**Load Configuration:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/config.yaml \
  --output json
```

**Load Task Specification:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/tasks/task-006-user-signup.md \
  --output json
```

### Configuration Response Format

```json
{
  "success": true,
  "outputs": {
    "content": "...",
    "development": {
      "alwaysLoadFiles": [
        ".claude/docs/coding-standards.md",
        ".claude/docs/architecture.md"
      ],
      "execute": {
        "validation": {
          "enabled": true,
          "strict_mode": false
        }
      }
    }
  },
  "errors": []
}
```

### Task Specification Response Format

```json
{
  "success": true,
  "outputs": {
    "content": "...",
    "task_id": "task-006",
    "status": "Approved",
    "objective": "Implement user signup flow",
    "acceptance_criteria": [
      "Users can sign up with email and password",
      "Validation errors are shown clearly"
    ],
    "tasks": [
      {
        "name": "Create signup form component",
        "subtasks": [
          "Create signup form UI",
          "Add form validation",
          "Write tests"
        ]
      }
    ]
  },
  "errors": []
}
```

### Status Update

**Before:**
```markdown
Status: Approved
```

**After:**
```markdown
Status: InProgress
```

---

## Step 1: Review Task Context and Plan Execution

### Execution Plan Template

```markdown
## Execution Plan

**Task:** Implement User Signup Flow
**File:** .claude/tasks/task-006-user-signup.md

**Context Loaded:**
- ✓ Task specification (all context embedded)
- ✓ Coding standards from .claude/docs/coding-standards.md
- ✓ Architecture guide from .claude/docs/architecture.md

**Execution Sequence:**
1. Task 1: Create signup form component (3 subtasks)
2. Task 2: Implement signup service (4 subtasks)
3. Task 3: Add validation logic (2 subtasks)
4. Task 4: Write integration tests (2 subtasks)
5. Task 5: Add error handling (2 subtasks)

**Total:** 5 tasks, 13 subtasks

**Ready to begin implementation? (yes/no)**
```

### Context Review Checklist

**Context Elements to Review:**
- Previous task insights (learnings from related tasks)
- Data models and schemas (user model, validation schemas)
- API specifications (endpoints, request/response formats)
- Component specifications (UI components, props, state)
- File locations (where to create/modify files)
- Testing requirements (unit, integration, E2E)
- Technical constraints (libraries to use, patterns to follow)

---

## Step 2: Execute Current Task

### Task Announcement Template

```markdown
## Executing Task 1: Create Signup Form Component (AC: Users can sign up with email and password)

**Subtasks:**
- [ ] Create signup form UI with email/password fields
- [ ] Add client-side validation (email format, password strength)
- [ ] Write unit tests for form component
```

### Subtask Progress Updates

**Starting Subtask:**
```markdown
### Subtask 1.1: Create signup form UI with email/password fields

Creating React component: src/components/auth/SignupForm.tsx
```

**Completing Subtask:**
```markdown
✓ Subtask 1.1 complete: SignupForm component created
  - Created: src/components/auth/SignupForm.tsx
  - Features: Email input, password input, confirm password, submit button
  - Styling: Tailwind CSS classes applied
```

**Updating Checkbox:**
```markdown
## Executing Task 1: Create Signup Form Component

**Subtasks:**
- [x] Create signup form UI with email/password fields
- [ ] Add client-side validation (email format, password strength)
- [ ] Write unit tests for form component
```

### Implementation Record Update (During Execution)

```markdown
### Completion Notes

**Task 1: Create signup form component**
- Created SignupForm.tsx with email/password inputs
- Used React Hook Form for form state management
- Applied Tailwind CSS for responsive design
- Decision: Used zod for validation schema (better TypeScript support than yup)
- Deviation: Added "Confirm Password" field (not in original spec but improves UX)

**Task 2: Implement signup service**
- Created AuthService.signup method
- Integrated with backend /api/auth/signup endpoint
- Implements retry logic (max 3 attempts with exponential backoff)
- Learning: Backend expects camelCase but returns snake_case, added adapter
```

### Task Validation Output

**After all subtasks complete:**
```markdown
## Task 1 Validation

**Running tests:**
✓ SignupForm.test.tsx: All 8 tests passing
  - Renders form correctly
  - Validates email format
  - Validates password strength
  - Shows validation errors
  - Handles form submission
  - Disables submit during submission
  - Shows success message
  - Clears form after success

**Linting:**
✓ No linting errors
✓ No formatting issues

**Acceptance criteria coverage:**
✓ AC1: Users can sign up with email and password - COVERED
  - Implementation: SignupForm component + AuthService.signup
  - Tests: SignupForm.test.tsx (submit test)

**Task 1 COMPLETE** - Marking checkbox [x]
```

---

## Step 3: Final Validation and Documentation

### Complete Test Suite Execution

**Command:**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \
  --output json
```

**Response Format:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 19,
    "passed_tests": 19,
    "failed_tests": 0,
    "coverage_percent": 87,
    "duration_ms": 3456,
    "test_suites": [
      {
        "name": "SignupForm.test.tsx",
        "tests": 8,
        "passed": 8,
        "failed": 0
      },
      {
        "name": "AuthService.test.tsx",
        "tests": 11,
        "passed": 11,
        "failed": 0
      }
    ],
    "failures": []
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest"
  },
  "errors": []
}
```

### Acceptance Criteria Verification

**Format:**
```markdown
**Acceptance Criteria Verification:**

✓ **AC1: Users can sign up with email and password**
  - Implementation:
    - SignupForm.tsx (UI component)
    - AuthService.signup() (API integration)
    - ValidationSchema.ts (email/password validation)
  - Tests:
    - SignupForm.test.tsx (form submission)
    - AuthService.test.tsx (API integration)
  - Coverage: 100%

✓ **AC2: Validation errors are shown clearly**
  - Implementation:
    - SignupForm.tsx (error display logic)
    - ErrorMessage.tsx (error UI component)
  - Tests:
    - SignupForm.test.tsx (error display tests)
  - Coverage: 100%

**All acceptance criteria met and verified**
```

### Implementation Record Complete Template

```markdown
### Agent Model Used
claude-sonnet-4-5-20250929

### Completion Notes

**Task 1: Create signup form component**
- Created SignupForm.tsx with email/password inputs
- Used React Hook Form for form state management
- Applied Tailwind CSS for responsive design
- Decision: Used zod for validation schema (better TypeScript support)
- Deviation: Added "Confirm Password" field for better UX

**Task 2: Implement signup service**
- Created AuthService.signup method
- Integrated with /api/auth/signup endpoint
- Implements retry logic (3 attempts, exponential backoff)
- Learning: Backend uses snake_case responses, added adapter layer

**Task 3: Add validation logic**
- Email format validation (RFC 5322 compliant)
- Password strength: min 8 chars, 1 uppercase, 1 number, 1 special
- Real-time validation with debounce (300ms)

**Task 4: Write integration tests**
- E2E test: Full signup flow (form → API → success)
- E2E test: Error handling (network error, validation error)

**Task 5: Add error handling**
- Network error handling with retry
- Validation error display
- Rate limiting handling (429 responses)

### Files Modified

**Created:**
- src/components/auth/SignupForm.tsx
- src/components/auth/ErrorMessage.tsx
- src/services/AuthService.ts
- src/schemas/ValidationSchema.ts
- src/utils/apiAdapter.ts
- tests/components/SignupForm.test.tsx
- tests/services/AuthService.test.tsx
- tests/e2e/signup.test.tsx

**Modified:**
- src/types/user.ts (added SignupRequest type)
- src/App.tsx (added signup route)
- src/api/client.ts (added retry interceptor)

### Testing Results

**Unit Tests:** 15 passed, 0 failed
- SignupForm.test.tsx: 8 tests
- AuthService.test.tsx: 7 tests

**Integration Tests:** 4 passed, 0 failed
- signup.test.tsx: 4 E2E tests

**Coverage:** 87% statements, 82% branches
**Regression Tests:** 19 tests, all passing
**Total Execution Time:** 3.4s
```

### Status Update

**Before:**
```markdown
Status: InProgress
```

**After:**
```markdown
Status: Review
```

### Completion Summary Template

```markdown
## Implementation Complete - Ready for Review

**Task:** Implement User Signup Flow
**Status:** Review

**What Was Implemented:**
✓ Signup form component with email/password inputs
✓ Client-side validation (email format, password strength)
✓ Backend integration with retry logic
✓ Error handling and user feedback
✓ Comprehensive test coverage

**All Acceptance Criteria Met:**
✓ AC1: Users can sign up with email and password
  - SignupForm component with form validation
  - AuthService.signup integration
  - Full E2E test coverage

✓ AC2: Validation errors are shown clearly
  - Real-time validation feedback
  - Error message component
  - Network error handling

**Test Results:**
✓ 19 tests, 19 passed, 0 failed
✓ 87% code coverage
✓ All regression tests passing

**Files Created:** 8 new files
**Files Modified:** 3 existing files

**Quality review needed? (yes/no)**
```

---

## Step 4: Handle Quality Review (Optional)

### If User Requests Quality Review

```markdown
Task marked "Review" and ready for quality assessment.

Next: Use quality review skill with this task file.

**Command:**
Use .claude/skills/quality/review-task/SKILL.md with input {task_file: ".claude/tasks/task-006-user-signup.md"}
```

### If User Approves Without Review

```markdown
User approved implementation without formal quality review.

Next steps:
1. Commit changes: git add . && git commit -m "Implement user signup flow"
2. Mark task status as "Done"
3. Move to next task (if any)

**Note:** Implementation Record is complete and task is marked Review status.
```

---

## Complete JSON Output Format

### Successful Execution

```json
{
  "implementation_complete": true,
  "tasks_completed": 5,
  "subtasks_completed": 13,
  "tests_passed": true,
  "total_tests": 19,
  "files_modified": [
    "src/components/auth/SignupForm.tsx",
    "src/components/auth/ErrorMessage.tsx",
    "src/services/AuthService.ts",
    "src/schemas/ValidationSchema.ts",
    "src/utils/apiAdapter.ts",
    "tests/components/SignupForm.test.tsx",
    "tests/services/AuthService.test.tsx",
    "tests/e2e/signup.test.tsx",
    "src/types/user.ts",
    "src/App.tsx",
    "src/api/client.ts"
  ],
  "status": "Review",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006-user-signup.md",
    "tasks_completed": 5,
    "subtasks_completed": 13,
    "tests_passed": true,
    "total_tests": 19,
    "files_modified_count": 11,
    "duration_ms": 245680,
    "halt_count": 0
  }
}
```

### Execution with Halts

```json
{
  "implementation_complete": true,
  "tasks_completed": 5,
  "subtasks_completed": 13,
  "tests_passed": true,
  "total_tests": 19,
  "files_modified": [
    "..."
  ],
  "status": "Review",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006-user-signup.md",
    "tasks_completed": 5,
    "subtasks_completed": 13,
    "tests_passed": true,
    "total_tests": 19,
    "files_modified_count": 11,
    "duration_ms": 356890,
    "halt_count": 2,
    "halt_reasons": [
      "Ambiguous Requirements (Task 2.3 - unclear API endpoint)",
      "User Interruption (User asked for clarification)"
    ]
  }
}
```

### Failed Execution (Test Failures)

```json
{
  "implementation_complete": false,
  "tasks_completed": 3,
  "subtasks_completed": 9,
  "tests_passed": false,
  "total_tests": 12,
  "failed_tests": 3,
  "files_modified": [
    "src/components/auth/SignupForm.tsx",
    "src/services/AuthService.ts",
    "tests/components/SignupForm.test.tsx"
  ],
  "status": "InProgress",
  "error": "Test failures: 3 tests failing",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006-user-signup.md",
    "tasks_completed": 3,
    "subtasks_completed": 9,
    "tests_passed": false,
    "total_tests": 12,
    "failed_tests": 3,
    "files_modified_count": 3,
    "duration_ms": 145230,
    "halt_count": 1,
    "halt_reasons": [
      "Test Failures (3 consecutive failures on subtask 3.2)"
    ]
  }
}
```

---

## Halt Message Templates

### Consecutive Failures Halt

```markdown
⚠️ EXECUTION HALTED

**Reason:** Consecutive Failures (3 attempts)
**Context:** Implementing subtask 2.3 "Add password strength validation"
**Issue:** Password validation regex not matching expected pattern
  - Attempt 1: Regex too permissive, allowed weak passwords
  - Attempt 2: Regex too strict, rejected valid passwords
  - Attempt 3: Regex syntax error, tests failing
**Need from User:**
  - Clarify password strength requirements (exact criteria)
  - Or provide example valid/invalid passwords
  - Or approve current implementation (min 8 chars, 1 uppercase, 1 number)
**Current Progress:**
  - Tasks complete: 2 of 5
  - Subtasks complete: 7 of 13
  - Current task: Task 2 (2 of 4 subtasks complete)
**Ready to Resume:** Once password validation requirements are clarified
```

### Ambiguous Requirements Halt

```markdown
⚠️ EXECUTION HALTED

**Reason:** Ambiguous Requirements
**Context:** Implementing subtask 3.1 "Integrate with backend API"
**Issue:** API endpoint specification unclear
  - Task spec mentions "/api/auth/signup"
  - But architecture doc shows "/api/v1/users/register"
  - Unclear which endpoint to use
  - Context doesn't specify API version strategy
**Need from User:**
  - Clarify correct API endpoint
  - Or provide API specification document
  - Or confirm which architecture document is current
**Current Progress:**
  - Tasks complete: 2 of 5
  - Subtasks complete: 8 of 13
  - Current task: Task 3 (0 of 4 subtasks complete)
**Ready to Resume:** Once API endpoint is confirmed
```

### Missing Dependencies Halt

```markdown
⚠️ EXECUTION HALTED

**Reason:** Missing Dependencies
**Context:** Implementing subtask 4.1 "Write E2E tests"
**Issue:** Test framework not configured
  - Task spec mentions "write E2E tests"
  - But Playwright/Cypress not found in package.json
  - No E2E test configuration files
  - Context doesn't specify which E2E framework to use
**Need from User:**
  - Install and configure E2E test framework (Playwright or Cypress?)
  - Or confirm E2E tests should be skipped
  - Or provide E2E test setup guide
**Current Progress:**
  - Tasks complete: 3 of 5
  - Subtasks complete: 11 of 13
  - Current task: Task 4 (0 of 2 subtasks complete)
**Ready to Resume:** Once E2E framework is set up or requirements clarified
```

### Regression Failures Halt

```markdown
⚠️ EXECUTION HALTED

**Reason:** Regression Failures
**Context:** Implementing subtask 2.2 "Add email validation"
**Issue:** Existing login tests started failing
  - LoginForm.test.tsx: 3 tests now failing
  - Error: "Email validation too strict"
  - Changes to validation schema broke existing login flow
  - Indicates breaking change introduced
**Need from User:**
  - Review breaking change acceptability
  - Or adjust acceptance criteria for backward compatibility
  - Or approve updating login tests to match new validation
**Current Progress:**
  - Tasks complete: 1 of 5
  - Subtasks complete: 5 of 13
  - Current task: Task 2 (1 of 4 subtasks complete)
**Ready to Resume:** Once breaking change is approved or validation is adjusted
```

### User Interruption Halt

```markdown
⚠️ EXECUTION HALTED

**Reason:** User Interruption
**Context:** Implementing subtask 3.3 "Add rate limiting handling"
**Issue:** User asked question mid-execution
**User Question:** "Should we use exponential backoff or fixed delay for rate limiting retries?"
**Current Progress:**
  - Tasks complete: 2 of 5
  - Subtasks complete: 10 of 13
  - Current task: Task 3 (2 of 4 subtasks complete)
**Ready to Resume:** Once user question is answered
```

---

## Error Templates

### Error 1: Task File Not Found

**Output:**
```markdown
❌ Error: Task file not found

**File:** .claude/tasks/task-999-missing.md
**Issue:** File does not exist at specified path

**Action Required:**
- Verify file path is correct
- Ensure task file has been created
- Check task file naming convention (task-XXX-name.md)

**Example:**
.claude/tasks/task-006-user-signup.md
```

**JSON Output:**
```json
{
  "implementation_complete": false,
  "error": "Task file not found: .claude/tasks/task-999-missing.md",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-999-missing.md",
    "duration_ms": 150,
    "halt_count": 0
  }
}
```

---

### Error 2: Task Status Not Approved

**Output:**
```markdown
❌ Error: Task must be Approved before execution

**File:** .claude/tasks/task-006-user-signup.md
**Current Status:** Draft
**Required Status:** Approved

**Action Required:**
- Review task specification
- Update status to "Approved" if ready
- Or use planning skill to finalize task spec

**Status Progression:**
Draft → Approved → InProgress → Review → Done
```

**JSON Output:**
```json
{
  "implementation_complete": false,
  "error": "Task status is 'Draft', must be 'Approved' to execute",
  "current_status": "Draft",
  "required_status": "Approved",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006-user-signup.md",
    "duration_ms": 320,
    "halt_count": 0
  }
}
```

---

### Error 3: Test Failures

**Output:**
```markdown
❌ Error: Tests failing

**Failed Tests:** 3
**Total Tests:** 19

**Failures:**
1. SignupForm.test.tsx > validates email format
   - Expected: Validation error shown
   - Received: No error displayed
   - Line: 45

2. SignupForm.test.tsx > validates password strength
   - Expected: "Password must be at least 8 characters"
   - Received: "Password is too weak"
   - Line: 62

3. AuthService.test.tsx > handles network errors
   - Expected: Retry 3 times
   - Received: Retry 1 time
   - Line: 128

**Action Required:**
- Review test failures
- Fix implementation issues
- Re-run tests
- Or update tests if requirements changed
```

**JSON Output:**
```json
{
  "implementation_complete": false,
  "tests_passed": false,
  "total_tests": 19,
  "passed_tests": 16,
  "failed_tests": 3,
  "error": "3 tests failing",
  "test_failures": [
    {
      "file": "SignupForm.test.tsx",
      "test": "validates email format",
      "line": 45,
      "expected": "Validation error shown",
      "received": "No error displayed"
    },
    {
      "file": "SignupForm.test.tsx",
      "test": "validates password strength",
      "line": 62,
      "expected": "Password must be at least 8 characters",
      "received": "Password is too weak"
    },
    {
      "file": "AuthService.test.tsx",
      "test": "handles network errors",
      "line": 128,
      "expected": "Retry 3 times",
      "received": "Retry 1 time"
    }
  ],
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006-user-signup.md",
    "tasks_completed": 4,
    "subtasks_completed": 12,
    "duration_ms": 234560,
    "halt_count": 1
  }
}
```

---

### Error 4: Missing Dependencies

**Output:**
```markdown
❌ Error: Missing dependencies

**Missing:** react-hook-form
**Context:** Required for Task 1 "Create signup form component"

**Issue:** Package not found in node_modules or package.json

**Action Required:**
- Install missing dependency: npm install react-hook-form
- Or update task spec to use different approach
- Or confirm dependency should be added to project

**Common Causes:**
- Dependency not documented in task spec
- Package.json out of sync
- npm install not run recently
```

**JSON Output:**
```json
{
  "implementation_complete": false,
  "error": "Missing dependency: react-hook-form",
  "missing_dependencies": ["react-hook-form"],
  "context": "Required for Task 1: Create signup form component",
  "suggested_action": "npm install react-hook-form",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006-user-signup.md",
    "tasks_completed": 0,
    "subtasks_completed": 1,
    "duration_ms": 12340,
    "halt_count": 1,
    "halt_reasons": ["Missing Dependencies"]
  }
}
```

---

## Integration Examples

### Integration with create-task-spec

**Workflow:**
1. **create-task-spec** outputs task file with status "Draft"
2. User reviews and approves task spec
3. User changes status to "Approved"
4. **execute-task** loads task file and begins implementation

**Example:**
```markdown
# Using create-task-spec then execute-task

## Step 1: Create task spec
Input: {feature: "User signup flow"}
Output: .claude/tasks/task-006-user-signup.md (status: Draft)

## Step 2: Review and approve
User reviews task spec
User updates status: Draft → Approved

## Step 3: Execute task
Input: {task_file: ".claude/tasks/task-006-user-signup.md"}
Output: Implementation complete, status: Review
```

---

### Integration with review-task (Quality Review)

**Workflow:**
1. **execute-task** completes implementation
2. Task status is "Review"
3. **review-task** performs quality assessment
4. If quality passes, task status → "Done"

**Example:**
```markdown
# Execute then review workflow

## Step 1: Execute task
Input: {task_file: ".claude/tasks/task-006-user-signup.md"}
Output: Implementation complete, status: Review

## Step 2: Quality review
Input: {task_file: ".claude/tasks/task-006-user-signup.md"}
Output: Quality assessment (PASS/CONCERNS/FAIL)

## Step 3: If PASS
Task status: Review → Done
Ready for commit/PR
```

---

### Integration with run-tests

**Workflow:**
1. **execute-task** implements subtask
2. Internally calls **run-tests** via bmad-commands
3. Tests must pass before marking subtask complete
4. Final validation runs complete test suite

**Example:**
```markdown
# Test integration during execution

## During subtask execution:
Subtask 1.3: "Write unit tests for signup form"
  → Create tests/SignupForm.test.tsx
  → Run tests via bmad-commands run_tests.py
  → Verify: passed_tests === total_tests
  → Mark subtask complete: [x]

## During final validation:
Step 3: Final validation
  → Run complete test suite via bmad-commands
  → Verify: all tests passing, coverage >= threshold
  → Update Implementation Record with test results
  → Update status: InProgress → Review
```

---

### CI/CD Integration

**GitHub Actions Example:**
```yaml
name: Execute Task

on:
  workflow_dispatch:
    inputs:
      task_file:
        description: 'Task specification file'
        required: true
        type: string

jobs:
  execute:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Execute task
        run: |
          claude execute-task \
            --task-file "${{ inputs.task_file }}" \
            --auto-confirm true

      - name: Run tests
        run: npm test

      - name: Upload Implementation Record
        uses: actions/upload-artifact@v3
        with:
          name: implementation-record
          path: ${{ inputs.task_file }}
```

**GitLab CI Example:**
```yaml
execute-task:
  stage: implement
  script:
    - npm ci
    - |
      claude execute-task \
        --task-file "$TASK_FILE" \
        --auto-confirm true
    - npm test
  variables:
    TASK_FILE: ".claude/tasks/task-006-user-signup.md"
  artifacts:
    paths:
      - .claude/tasks/*.md
    reports:
      junit: test-results.xml
  only:
    - execute-task
```

---

## Command-Line Usage Examples

### Basic Execution

```bash
# Execute task with confirmation prompt
claude execute-task --task-file .claude/tasks/task-006-user-signup.md

# Execute task with auto-confirm (CI/CD mode)
claude execute-task --task-file .claude/tasks/task-006-user-signup.md --auto-confirm true

# Execute task with verbose logging
claude execute-task --task-file .claude/tasks/task-006-user-signup.md --verbose
```

### Using JSON Output

```bash
# Execute and capture JSON output
claude execute-task \
  --task-file .claude/tasks/task-006-user-signup.md \
  --output json > execution-result.json

# Parse output with jq
claude execute-task \
  --task-file .claude/tasks/task-006-user-signup.md \
  --output json | jq '.tasks_completed'
```

### Error Handling

```bash
# Execute with error handling
if claude execute-task --task-file .claude/tasks/task-006-user-signup.md; then
  echo "✅ Implementation complete"
  git add .
  git commit -m "Implement user signup flow"
else
  echo "❌ Implementation failed"
  exit 1
fi
```

---

## Best Practices with Examples

### Practice 1: Trust the Task Spec

**Good:**
```markdown
# Read context from task spec
Context section includes:
  - Data model: User type definition
  - API endpoint: POST /api/auth/signup
  - Validation rules: Email RFC 5322, Password min 8 chars

Implementation:
  → Use User type from context
  → Call POST /api/auth/signup
  → Validate email with RFC 5322
  → No additional architecture lookup needed
```

**Bad:**
```markdown
# Searching for additional context
Read task spec → Search for User type in codebase
→ Find 3 different User types, unsure which to use
→ Search for API docs, find outdated spec
→ Wasted time, context drift
```

---

### Practice 2: Sequential Execution

**Good:**
```markdown
Task 1: Create signup form component
  Subtask 1.1: Create UI → COMPLETE → Mark [x]
  Subtask 1.2: Add validation → COMPLETE → Mark [x]
  Subtask 1.3: Write tests → COMPLETE → Mark [x]
  → ALL subtasks done → Mark task [x]

Task 2: Implement signup service
  Subtask 2.1: Create service → STARTED
  ...
```

**Bad:**
```markdown
Task 1: Create signup form component
  Subtask 1.1: Create UI → COMPLETE
  Subtask 1.3: Write tests → STARTED (skipped 1.2!)
  → Out of order execution
  → Validation missing
  → Tests may not catch validation issues
```

---

### Practice 3: Test Before Checking

**Good:**
```markdown
Subtask 1.3: Write tests
  → Create SignupForm.test.tsx
  → Write 8 test cases
  → Run tests: npm test SignupForm.test.tsx
  → Result: 8 passed, 0 failed ✓
  → Mark subtask [x]
```

**Bad:**
```markdown
Subtask 1.3: Write tests
  → Create SignupForm.test.tsx
  → Write 8 test cases
  → Mark subtask [x] (didn't run tests!)
  → Later: Final validation finds 3 tests failing
```

---

### Practice 4: Document As You Go

**Good:**
```markdown
After Task 1:
  → Update Implementation Record:
    - Files created: SignupForm.tsx
    - Decision: Used zod (better TypeScript support)
    - Learning: Email validation regex complex, used library

After Task 2:
  → Update Implementation Record:
    - Files created: AuthService.ts
    - Deviation: Added retry logic (not in spec)
    - Learning: Backend returns snake_case, needed adapter
```

**Bad:**
```markdown
After all tasks complete:
  → Try to remember what was done
  → "I created some files... can't remember why I made certain decisions"
  → Incomplete Implementation Record
  → Loss of valuable learnings
```

---

### Practice 5: Respect Permissions

**Good:**
```markdown
# Allowed edits to task file:
- Update checkboxes: [ ] → [x]
- Update status: Approved → InProgress → Review
- Update Implementation Record section

# Example:
Status: Approved → InProgress
- [ ] Task 1: Create signup form → - [x] Task 1: Create signup form
Implementation Record:
  ### Completion Notes
  - Created SignupForm.tsx...
```

**Bad:**
```markdown
# Unauthorized edits:
- Modify Objective: "Implement signup" → "Implement signup AND login"
- Modify AC: Add new acceptance criteria
- Modify Context: Update data model
- Change status to "Done" (only quality skill can do this)
→ Violates permission boundaries
→ Causes workflow issues
```

---

### Practice 6: Halt When Appropriate

**Good:**
```markdown
Subtask 2.3: "Integrate with payment API"
  → Task spec mentions payment API
  → No API key or endpoint in context
  → Missing dependency: stripe library

ACTION: HALT
  Reason: Missing Dependencies
  Need: Payment API credentials and endpoint
  Or: Clarification if payment integration out of scope
```

**Bad:**
```markdown
Subtask 2.3: "Integrate with payment API"
  → No API key in context
  → Guess: Mock the payment API
  → Implement mock payment flow
  → Later: User expected real Stripe integration
  → Wasted effort implementing wrong thing
```

---

*Complete templates and output formats for execute-task skill*
