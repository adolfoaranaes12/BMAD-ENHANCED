# Implementation Skill: Execute Task Specification

<!-- BMAD Enhanced Implementation Skill -->
<!-- Inspired by BMAD-METHOD Dev agent pattern -->
<!-- Version: 1.0 -->

## Purpose

Execute task specifications sequentially with comprehensive testing and validation at each step. This skill follows the BMAD Dev agent pattern: read task spec for ALL context (never load architecture docs), execute tasks in order, update only Implementation Record section.

**Key Innovation (BMAD Pattern):**
- ALL context already embedded in task spec by planning skill
- Dev reads ONLY task spec + always-load files (coding standards)
- No architecture lookup during implementation
- Result: Focused execution, no context searching, no drift

## When to Use This Skill

Use this skill when you need to:
- Implement an approved task specification
- Execute sequential tasks with validation
- Write comprehensive tests
- Maintain implementation audit trail

**Do NOT use this skill for:**
- Draft task specs (must be "Approved" status)
- Exploratory coding (use freeform approach)
- Emergency hotfixes (too structured for urgency)

## Core Principles (BMAD-Inspired)

1. **Context Sufficiency:** Task spec contains ALL info needed aside from always-load files
2. **No Architecture Lookup:** NEVER load PRD/architecture docs unless explicitly in task notes
3. **Sequential Execution:** Complete current task before starting next
4. **Validation Gates:** Run tests + validations before checking off tasks
5. **Limited File Permissions:** ONLY update Implementation Record section of task file
6. **Halt on Ambiguity:** Stop and ask user if requirements unclear

## File Modification Permissions

**CRITICAL PERMISSION BOUNDARIES:**

**YOU ARE AUTHORIZED TO:**
- ✅ Update "Implementation Record" section of task file
- ✅ Update task/subtask checkboxes ([ ] to [x])
- ✅ Create, modify, delete implementation files (src/, tests/, etc.)
- ✅ Run commands (tests, linters, builds)

**YOU ARE NOT AUTHORIZED TO:**
- ❌ Modify "Objective" section of task file
- ❌ Modify "Acceptance Criteria" section of task file
- ❌ Modify "Context" section of task file
- ❌ Modify "Tasks / Subtasks" descriptions (only checkboxes)
- ❌ Modify "Quality Review" section of task file
- ❌ Change task status to "Done" (only "InProgress" → "Review")

## SEQUENTIAL Task Execution

**CRITICAL:** Do not proceed to next step until current step is complete

### Step 0: Load Configuration and Task Specification

**Actions:**

1. Load `.claude/config.yaml`:
   - Extract `development.alwaysLoadFiles`
   - Extract `development.debugLog`
   - Extract `workflow.haltOn` settings
   - Extract `skills.implementation.*` settings

2. Get task file path from user:
   - Example: `.claude/tasks/task-006-user-signup.md`
   - Verify file exists

3. Read task specification:
   - Load entire task file
   - Parse status, objective, acceptance criteria, context, tasks

4. Verify task is approved:
   - Check status is "Approved"
   - If "Draft": HALT with "Task must be approved before implementation"
   - If "InProgress": Confirm user wants to continue/resume
   - If "Review" or "Done": HALT with "Task already completed"

5. Load always-load files:
   - Read each file in `development.alwaysLoadFiles`
   - These contain coding standards, project rules

6. Update task status to "InProgress":
   - Edit task file status line from "Approved" to "InProgress"
   - Record start time in Implementation Record

**Output:**
- Configuration loaded
- Task specification loaded and parsed
- Always-load files (standards) loaded
- Status updated to "InProgress"

**Halt Conditions:**
- Configuration file missing
- Task file missing or unreadable
- Task status not "Approved"
- Always-load files missing

### Step 1: Review Task Context and Plan Execution

**Actions:**

1. Review embedded context:
   - Previous task insights
   - Data models and schemas
   - API specifications
   - Component specifications
   - File locations
   - Testing requirements
   - Technical constraints

2. Review task breakdown:
   - Count total tasks and subtasks
   - Identify current task (first unchecked)
   - Understand task dependencies and sequence

3. Check for existing work:
   - Scan file list to see what already exists
   - Review completion notes for progress so far

4. Confirm understanding with user:
   ```markdown
   ## Execution Plan

   **Task:** User Signup Implementation
   **File:** .claude/tasks/task-006-user-signup.md

   **Context Loaded:**
   - ✓ Task specification (all context embedded)
   - ✓ Coding standards from docs/standards.md
   - ✓ Previous auth patterns from task-003

   **Execution Sequence:**
   1. Task 1: Create user model (3 subtasks)
   2. Task 2: Implement signup service (4 subtasks)
   3. Task 3: Create API endpoint (5 subtasks)
   4. Task 4: Add email verification (3 subtasks)
   5. Task 5: Write comprehensive tests (3 subtasks)

   **Total:** 5 tasks, 18 subtasks

   **Ready to begin implementation? (yes/no)**
   ```

5. Wait for user confirmation

**Output:**
- Context reviewed and understood
- Execution plan presented
- User confirmation received

**Halt Conditions:**
- Context appears insufficient (missing critical info)
- Task breakdown unclear or ambiguous
- User does not confirm to proceed

### Step 2: Execute Current Task

**Actions:**

**For each task in sequence:**

1. Announce current task:
   ```markdown
   ## Executing Task 1: Create user model (AC: 1, 2)

   **Subtasks:**
   - [ ] Define User interface in src/types/user.ts
   - [ ] Create user schema with Zod validation
   - [ ] Add database migration for users table
   - [ ] Write unit tests for validation logic
   - [ ] Validate: Model matches architecture spec
   ```

2. **For each subtask in sequence:**

   a. **Implement subtask:**
      - Read context from task spec for specific details
      - Create/modify files as specified
      - Follow coding standards from always-load files
      - Use patterns from previous task insights

   b. **If subtask is "Write tests":**
      - Write unit/integration/E2E tests as specified
      - Follow testing requirements from context
      - Ensure tests cover edge cases
      - Tests must pass before marking subtask complete

   c. **If subtask is "Validate":**
      - Run relevant tests
      - Run linter/formatter
      - Verify output matches acceptance criteria
      - Check against technical constraints

   d. **Update subtask checkbox:**
      - Edit task file to mark subtask complete: `- [x]`
      - ONLY if subtask fully complete and validated

   e. **Record implementation notes:**
      - Update "Completion Notes" in Implementation Record
      - Document any deviations from plan
      - Note any challenges or decisions
      - Log useful patterns for future tasks

3. **After all subtasks complete:**

   a. **Run task validation:**
      - Execute all tests related to this task
      - Run full lint check
      - Verify acceptance criteria coverage

   b. **Update task checkbox:**
      - Edit task file to mark task complete: `- [x]`
      - ONLY if all subtasks complete and validation passed

   c. **Update Implementation Record:**
      - Add files created/modified to "Files Modified" section
      - Add completion notes specific to this task
      - Update debug log if complex issues encountered

4. **Move to next task:**
   - Repeat Step 2 for next unchecked task

**Example Implementation Flow:**

```markdown
Starting Task 1: Create user model
├─ Subtask 1.1: Define User interface
│  ├─ Create src/types/user.ts
│  ├─ Define interface with id, email, password, createdAt
│  └─ ✓ Mark subtask complete
├─ Subtask 1.2: Create Zod schema
│  ├─ Add validation schema in src/schemas/user.schema.ts
│  ├─ Email validation with RFC 5322 format
│  ├─ Password min 8 chars, complexity requirements
│  └─ ✓ Mark subtask complete
├─ Subtask 1.3: Database migration
│  ├─ Create migration file migrations/001_create_users.sql
│  ├─ Users table with proper types and constraints
│  └─ ✓ Mark subtask complete
├─ Subtask 1.4: Write unit tests
│  ├─ Create src/schemas/__tests__/user.schema.test.ts
│  ├─ Test valid/invalid email formats
│  ├─ Test valid/invalid passwords
│  ├─ Run tests: 12 tests, 12 passed
│  └─ ✓ Mark subtask complete
├─ Subtask 1.5: Validate model
│  ├─ Run all tests: PASS
│  ├─ Run linter: PASS
│  ├─ Compare with architecture spec: MATCH
│  └─ ✓ Mark subtask complete
└─ ✓ Task 1 complete

[Update Implementation Record with completion notes]

Moving to Task 2: Implement signup service...
```

**Output:**
- All tasks executed sequentially
- All subtasks completed with checkboxes marked
- Tests written and passing
- Implementation Record updated
- Files created/modified list maintained

**Halt Conditions:**
- 3 consecutive implementation failures on same subtask
- Ambiguous requirements discovered (context insufficient)
- Missing dependencies not documented in task spec
- Regression test failures (existing tests break)
- User requests halt

### Step 3: Final Validation and Documentation

**Actions:**

1. **Run complete test suite:**
   ```bash
   npm test              # Run all tests
   npm run lint          # Run linter
   npm run type-check    # Run type checker (if TypeScript)
   ```

2. **Verify acceptance criteria:**
   - Review each AC from task spec
   - Map AC to implementation and tests
   - Confirm all ACs covered

3. **Verify all checkboxes marked:**
   - Scan task spec for any unchecked [ ] boxes
   - Ensure all tasks and subtasks complete

4. **Update Implementation Record:**

   a. **Agent Model Used:**
      ```markdown
      ### Agent Model Used
      claude-sonnet-4-5-20250929
      ```

   b. **Completion Notes:**
      ```markdown
      ### Completion Notes
      - Implemented user signup with email/password validation
      - Reused auth middleware pattern from task-003
      - Added extra validation for unicode emails (edge case discovered)
      - bcrypt cost 12 adds ~150ms latency (acceptable for auth endpoint)
      - All 4 acceptance criteria validated and tested
      ```

   c. **Files Modified:**
      ```markdown
      ### Files Modified

      **Created:**
      - src/types/user.ts
      - src/schemas/user.schema.ts
      - src/services/auth/signup.service.ts
      - src/routes/auth/signup.ts
      - migrations/001_create_users.sql
      - src/schemas/__tests__/user.schema.test.ts
      - src/services/auth/__tests__/signup.service.test.ts
      - src/routes/auth/__tests__/signup.integration.test.ts
      - tests/e2e/auth/signup.e2e.test.ts

      **Modified:**
      - src/routes/auth/index.ts (added signup route)
      - README.md (updated API documentation)
      ```

   d. **Testing Results:**
      ```markdown
      ### Testing Results

      **Unit Tests:**
      - 12 tests, 12 passed, 0 failed
      - Coverage: 94% statements, 89% branches, 100% functions

      **Integration Tests:**
      - 5 tests, 5 passed, 0 failed
      - API endpoints verified

      **E2E Tests:**
      - 2 tests, 2 passed, 0 failed
      - Complete signup flow validated

      **Total Execution Time:** 4.2s
      **Regression Tests:** All passing (47 tests)
      ```

5. **Update task status to "Review":**
   - Edit task file status line from "InProgress" to "Review"
   - DO NOT mark as "Done" (quality skill does that)

6. **Present completion summary to user:**
   ```markdown
   ## Implementation Complete - Ready for Review

   **Task:** User Signup Implementation
   **File:** .claude/tasks/task-006-user-signup.md
   **Status:** Review (ready for quality assessment)

   **What Was Implemented:**
   ✓ User data model with validation
   ✓ Signup service with password hashing
   ✓ API endpoint POST /api/auth/signup
   ✓ Email verification integration
   ✓ Comprehensive test suite (19 tests total)

   **All Acceptance Criteria Met:**
   ✓ AC1: User can signup with valid email/password
   ✓ AC2: Password security requirements enforced
   ✓ AC3: Duplicate emails prevented
   ✓ AC4: Confirmation email sent

   **Test Results:**
   ✓ 19 tests, 19 passed, 0 failed
   ✓ 94% code coverage
   ✓ All regression tests passing (47 tests)
   ✓ Linter and type checker passing

   **Files Created:** 9 new files
   **Files Modified:** 2 existing files

   **Next Steps:**
   1. Review implementation if desired
   2. Run quality review skill for systematic assessment
   3. If quality gate passes, mark task as "Done"

   **Quality review needed? (yes/no)**
   ```

**Output:**
- All tests passing
- All acceptance criteria verified
- Implementation Record complete
- Status updated to "Review"
- User presented with summary

**Halt Conditions:**
- Test failures that can't be resolved
- Acceptance criteria not fully met
- Critical bugs discovered

### Step 4: Handle Quality Review (Optional)

**Actions:**

1. If user requests quality review:
   ```markdown
   Task marked "Review" and ready for quality assessment.

   Next: Use quality review skill with this task file.

   Command: @quality-skill review .claude/tasks/task-006-user-signup.md
   ```

2. If user approves without quality review:
   ```markdown
   User approved implementation without formal quality review.

   Next steps:
   1. Commit changes
   2. Mark task status as "Done"
   3. Move to next task

   **Important:** Make sure to commit your changes before proceeding!
   ```

**Output:**
- User decision on quality review
- Clear next steps provided

## Completion Criteria

Task execution is complete when:

- [ ] All tasks and subtasks marked complete (checked)
- [ ] All tests written and passing
- [ ] All acceptance criteria verified
- [ ] Implementation Record fully populated
- [ ] Status updated to "Review"
- [ ] User presented with completion summary

## Permission Enforcement

**CRITICAL:** This skill ONLY updates specific sections of task file

**Edit Task File - Implementation Record Section Only:**
```markdown
## Implementation Record

### Agent Model Used
[CAN EDIT: Record model used]

### Debug Log References
[CAN EDIT: Add debug log entries]

### Completion Notes
[CAN EDIT: Add implementation notes]

### Files Modified
[CAN EDIT: List created/modified files]

### Testing Results
[CAN EDIT: Record test execution results]
```

**Edit Task File - Task Checkboxes Only:**
```markdown
- [x] Task 1: Description... (CAN EDIT: Change [ ] to [x])
  - [x] Subtask 1.1... (CAN EDIT: Change [ ] to [x])
```

**Edit Task File - Status Line Only:**
```markdown
## Status

InProgress → Review (CAN EDIT: Update status)
```

**DO NOT EDIT:**
- Objective section
- Acceptance Criteria section
- Context section (Previous Insights, Data Models, API Specs, etc.)
- Task descriptions (only checkboxes)
- Quality Review section

## Halt Conditions

**Must halt execution and ask user when:**

1. **Consecutive Failures (default: 3)**
   - Same subtask fails 3 times in a row
   - Present error to user and ask for guidance

2. **Ambiguous Requirements**
   - Context insufficient to implement subtask
   - Multiple valid interpretations
   - Critical technical decision needed

3. **Missing Dependencies**
   - Required library/service not documented
   - External API credentials needed
   - Database not accessible

4. **Regression Failures**
   - Existing tests start failing
   - Breaking change introduced
   - Must fix before proceeding

5. **User Interruption**
   - User requests halt
   - User asks question mid-execution

**Halt Message Format:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** [Ambiguous Requirements | Consecutive Failures | Missing Dependencies | Regression Failures]

**Context:** [Describe what was being attempted]

**Issue:** [Specific problem encountered]

**Need from User:**
- [What information/decision is needed]

**Current Progress:**
- ✓ Tasks 1-2 complete (6 subtasks)
- ⏸ Task 3 subtask 3.2 halted

**Ready to Resume:** Once [issue] is resolved
```

## Usage Example

**User:** "Execute .claude/tasks/task-006-user-signup.md"

**Implementation Skill:**

1. Loads configuration and task spec
2. Verifies status is "Approved"
3. Loads coding standards from always-load files
4. Updates status to "InProgress"

5. Reviews embedded context:
   - User model schema with Zod validation
   - API spec: POST /api/auth/signup
   - Testing strategy: Unit + Integration + E2E
   - Security: bcrypt cost 12, rate limiting
   - Files: Exact paths for all components

6. Executes Task 1: Create user model
   - Creates src/types/user.ts with interface
   - Creates src/schemas/user.schema.ts with validation
   - Creates database migration
   - Writes unit tests (12 tests)
   - Runs validation (all pass)
   - Marks task complete ✓

7. Executes Task 2: Implement signup service
   - Creates src/services/auth/signup.service.ts
   - Implements password hashing with bcrypt
   - Adds duplicate email check
   - Writes unit tests (8 tests)
   - Runs validation (all pass)
   - Marks task complete ✓

8. Executes Task 3: Create API endpoint
   - Creates src/routes/auth/signup.ts
   - Adds request validation middleware
   - Implements error handling
   - Writes integration tests (5 tests)
   - Runs validation (all pass)
   - Marks task complete ✓

9. Executes Task 4: Add email verification
   - Integrates email service
   - Sends confirmation email
   - Writes integration tests (2 tests)
   - Marks task complete ✓

10. Executes Task 5: Comprehensive tests
    - Writes E2E tests (2 scenarios)
    - Runs full test suite (19 tests, all pass)
    - Verifies all ACs covered
    - Marks task complete ✓

11. Final validation:
    - All tests passing (19 + 47 regression)
    - 94% code coverage
    - All ACs verified
    - Linter passing

12. Updates Implementation Record:
    - Agent model: claude-sonnet-4-5
    - Completion notes: Implementation details and learnings
    - Files modified: 9 created, 2 modified
    - Testing results: 19 tests passed

13. Updates status to "Review"

14. Presents completion summary to user

**Result:** Task fully implemented, tested, documented, ready for quality review

## Best Practices

1. **Trust the Task Spec:**
   - Context is already embedded
   - Don't search for additional architecture docs
   - Follow specs exactly as written

2. **Sequential Execution:**
   - Complete current subtask before next
   - Don't skip ahead even if obvious
   - Validate before marking complete

3. **Test Before Checking:**
   - Write tests before marking subtask done
   - Run tests before checking task box
   - Ensure all tests pass

4. **Document As You Go:**
   - Update completion notes after each task
   - Record deviations and decisions
   - Note patterns for future tasks

5. **Respect Permissions:**
   - Only edit Implementation Record section
   - Only update checkboxes and status
   - Never modify context or AC sections

6. **Halt When Appropriate:**
   - Don't guess if requirements unclear
   - Don't proceed after repeated failures
   - Don't break regression tests

## Common Pitfalls to Avoid

1. **Loading Architecture Docs:**
   - ❌ Don't: Read docs/architecture/* during implementation
   - ✅ Do: Use context already embedded in task spec

2. **Skipping Validations:**
   - ❌ Don't: Mark task complete without running tests
   - ✅ Do: Validate after each task, run full suite at end

3. **Editing Wrong Sections:**
   - ❌ Don't: Modify acceptance criteria or context
   - ✅ Do: Only update Implementation Record and checkboxes

4. **Non-Sequential Execution:**
   - ❌ Don't: Jump to Task 3 because it seems easier
   - ✅ Do: Execute tasks in order, halt if blocked

5. **Insufficient Documentation:**
   - ❌ Don't: Just mark checkboxes without notes
   - ✅ Do: Document deviations, decisions, learnings

6. **Ignoring Halt Conditions:**
   - ❌ Don't: Proceed through 10 failures hoping it works
   - ✅ Do: Halt after 3 failures, ask user for guidance

## Integration with Other Skills

**Before This Skill:**
- Planning skill created task specification
- Task status set to "Approved"
- All context embedded in task file

**After This Skill:**
- Task status set to "Review"
- Implementation Record populated
- All tests passing
- Ready for quality skill

**Handoff to Quality Skill:**
```markdown
Implementation complete and ready for quality review:
- File: .claude/tasks/task-006-user-signup.md
- Status: Review
- All acceptance criteria implemented
- All tests passing
- Implementation Record complete

Next: Use quality review skill for systematic assessment
```

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial implementation skill based on BMAD Dev agent pattern |

---

**End of Implementation Skill**
