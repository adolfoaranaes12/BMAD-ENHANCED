---
name: execute-task
description: Execute approved task specifications sequentially with TDD, comprehensive testing, and validation. Use for implementing tasks from approved specs with full audit trail.
acceptance:
  - task_loaded: "Task specification successfully loaded and validated"
  - status_updated: "Task status progressed from Approved → InProgress → Review"
  - all_complete: "All tasks and subtasks marked complete"
  - tests_passing: "All tests written and passing"
  - criteria_verified: "All acceptance criteria verified and documented"
  - record_complete: "Implementation Record fully populated"
inputs:
  task_file:
    type: string
    required: true
    description: "Path to task specification file (e.g., .claude/tasks/task-006.md)"
    validation: "Must be existing file with status 'Approved'"
  auto_confirm:
    type: boolean
    required: false
    description: "Skip execution plan confirmation"
    default: false
outputs:
  implementation_complete:
    type: boolean
    description: "Whether all tasks completed successfully"
  tasks_completed:
    type: number
    description: "Number of tasks completed"
  subtasks_completed:
    type: number
    description: "Number of subtasks completed"
  tests_passed:
    type: boolean
    description: "Whether all tests passed"
  total_tests:
    type: number
    description: "Total number of tests executed"
  files_modified:
    type: array
    description: "List of files created or modified"
  status:
    type: string
    description: "Final task status (should be 'Review')"
telemetry:
  emit: "skill.execute-task.completed"
  track:
    - task_file
    - tasks_completed
    - subtasks_completed
    - tests_passed
    - total_tests
    - files_modified_count
    - duration_ms
    - halt_count
---

# Execute Task Skill

## Purpose

Execute approved task specifications sequentially using Test-Driven Development (TDD), with comprehensive validation at each step and full implementation audit trail.

**Core Capabilities:**
- Sequential task/subtask execution with validation gates
- Permission-controlled file modifications
- Comprehensive testing and documentation
- Implementation Record maintenance
- Halt-on-error safeguards

**BMAD Pattern (Key Innovation):**
- ALL context embedded in task spec by planning skill
- Dev reads ONLY task spec + always-load files (coding standards)
- No architecture lookup during implementation
- Result: Focused execution, no context searching, no drift

## Prerequisites

- Task specification file with status "Approved"
- Configuration file (`.claude/config.yaml`) with development settings
- Always-load files (coding standards) available
- Test framework configured (Jest, Pytest, etc.)

---

## Workflow

### Step 0: Load Configuration and Task Specification

**Action:** Load all required context and verify task readiness.

Execute:
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/config.yaml \
  --output json

python .claude/skills/bmad-commands/scripts/read_file.py \
  --path {task_file} \
  --output json
```

**Parse Response:**
- Extract `development.alwaysLoadFiles` from config
- Extract task status, objective, acceptance criteria, tasks
- Verify status is "Approved"

**Validation:**
- Configuration file exists and loadable
- Task file exists and loadable
- Task status is "Approved" (halt if Draft/Review/Done)
- Always-load files exist

**Update Status:**
- Change task status from "Approved" to "InProgress"
- Record start time in Implementation Record

**See:** `references/configuration-guide.md` for detailed configuration loading

---

### Step 1: Review Task Context and Plan Execution

**Action:** Review embedded context and present execution plan to user.

**Context Review:**
- Previous task insights
- Data models and schemas
- API specifications
- Component specifications
- File locations
- Testing requirements
- Technical constraints

**Task Breakdown:**
- Count total tasks and subtasks
- Identify current task (first unchecked)
- Understand task dependencies

**Present Plan:**
```markdown
## Execution Plan

**Task:** [Task Name]
**File:** [task_file]

**Context Loaded:**
- ✓ Task specification (all context embedded)
- ✓ Coding standards from [always-load files]

**Execution Sequence:**
1. Task 1: [Name] (X subtasks)
2. Task 2: [Name] (Y subtasks)
...

**Total:** N tasks, M subtasks

**Ready to begin implementation? (yes/no)**
```

**Wait for confirmation** unless `auto_confirm=true`

**Halt Conditions:**
- Context appears insufficient
- Task breakdown unclear
- User does not confirm

**See:** `references/task-execution-guide.md` for execution details

---

### Step 2: Execute Current Task

**Action:** Execute each task and subtask sequentially with validation.

**For each task in sequence:**

1. **Announce current task:**
   ```markdown
   ## Executing Task N: [Name] (AC: X, Y)

   **Subtasks:**
   - [ ] Subtask N.1...
   - [ ] Subtask N.2...
   ...
   ```

2. **For each subtask:**

   a. **Implement subtask:**
      - Read context from task spec
      - Create/modify files as specified
      - Follow coding standards from always-load files

   b. **If subtask is "Write tests":**
      - Write unit/integration/E2E tests
      - Tests must pass before marking complete

   c. **If subtask is "Validate":**
      - Run relevant tests
      - Run linter/formatter
      - Verify output matches acceptance criteria

   d. **Update subtask checkbox:**
      - Mark subtask complete: `- [x]`
      - ONLY if fully complete and validated

   e. **Record implementation notes:**
      - Update "Completion Notes" in Implementation Record
      - Document deviations, decisions, learnings

3. **After all subtasks:**

   a. **Run task validation:**
      - Execute all tests related to task
      - Run lint check
      - Verify acceptance criteria coverage

   b. **Update task checkbox:**
      - Mark task complete: `- [x]`
      - ONLY if all subtasks complete and validated

   c. **Update Implementation Record:**
      - Add files created/modified
      - Add completion notes

4. **Move to next task**

**Halt Conditions:**
- 3 consecutive implementation failures on same subtask
- Ambiguous requirements discovered
- Missing dependencies not documented
- Regression test failures
- User requests halt

**See:** `references/task-execution-guide.md` for detailed execution examples

---

### Step 3: Final Validation and Documentation

**Action:** Run complete validation and finalize documentation.

**Validation:**

1. **Run complete test suite:**
   ```bash
   python .claude/skills/bmad-commands/scripts/run_tests.py \
     --path . \
     --framework jest \
     --output json
   ```

2. **Verify acceptance criteria:**
   - Review each AC from task spec
   - Map AC to implementation and tests
   - Confirm all ACs covered

3. **Verify all checkboxes marked:**
   - Scan task spec for unchecked [ ] boxes
   - Ensure all tasks and subtasks complete

**Documentation:**

Update Implementation Record:

```markdown
### Agent Model Used
[model_id]

### Completion Notes
[Implementation details, decisions, learnings]

### Files Modified

**Created:**
- [list of new files]

**Modified:**
- [list of modified files]

### Testing Results

**Unit Tests:** X passed, Y failed
**Integration Tests:** X passed, Y failed
**Coverage:** X% statements, Y% branches
**Regression Tests:** X tests, all passing
**Total Execution Time:** Xs
```

**Status Update:**
- Change status from "InProgress" to "Review"
- DO NOT mark as "Done" (quality skill does that)

**Present Summary:**
```markdown
## Implementation Complete - Ready for Review

**Task:** [Name]
**Status:** Review

**What Was Implemented:**
✓ [Summary of tasks]

**All Acceptance Criteria Met:**
✓ AC1: [description]
✓ AC2: [description]
...

**Test Results:**
✓ X tests, X passed, 0 failed
✓ Y% code coverage
✓ All regression tests passing

**Files Created:** X new files
**Files Modified:** Y existing files

**Quality review needed? (yes/no)**
```

**See:** `references/validation-guide.md` for validation details

---

### Step 4: Handle Quality Review (Optional)

**Action:** Provide next steps based on user decision.

**If user requests quality review:**
```markdown
Task marked "Review" and ready for quality assessment.

Next: Use quality review skill with this task file.
```

**If user approves without review:**
```markdown
User approved implementation without formal quality review.

Next steps:
1. Commit changes
2. Mark task status as "Done"
3. Move to next task
```

**Output:**
- User decision recorded
- Clear next steps provided

---

## File Modification Permissions

**CRITICAL PERMISSION BOUNDARIES:**

**YOU ARE AUTHORIZED TO:**
- ✅ Update "Implementation Record" section of task file
- ✅ Update task/subtask checkboxes ([ ] to [x])
- ✅ Update task status line (Approved → InProgress → Review)
- ✅ Create, modify, delete implementation files (src/, tests/, etc.)
- ✅ Run commands (tests, linters, builds)

**YOU ARE NOT AUTHORIZED TO:**
- ❌ Modify "Objective" section of task file
- ❌ Modify "Acceptance Criteria" section of task file
- ❌ Modify "Context" section of task file
- ❌ Modify task/subtask descriptions (only checkboxes)
- ❌ Modify "Quality Review" section of task file
- ❌ Change task status to "Done" (only to "Review")

**Enforcement:** Only edit Implementation Record section and checkboxes/status

**See:** `references/permissions-halts.md` for detailed permission boundaries

---

## Halt Conditions

**Must halt execution and ask user when:**

1. **Consecutive Failures (default: 3)**
   - Same subtask fails 3 times in a row
   - Present error and ask for guidance

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

5. **User Interruption**
   - User requests halt
   - User asks question mid-execution

**Halt Message Format:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** [category]
**Context:** [what was being attempted]
**Issue:** [specific problem]
**Need from User:** [what information/decision needed]
**Current Progress:** [tasks complete, tasks remaining]
**Ready to Resume:** Once [issue] is resolved
```

**See:** `references/permissions-halts.md` for halt handling details

---

## Output

Return structured output with telemetry:

```json
{
  "implementation_complete": true,
  "tasks_completed": 5,
  "subtasks_completed": 18,
  "tests_passed": true,
  "total_tests": 19,
  "files_modified": [
    "src/types/user.ts",
    "src/services/auth/signup.service.ts",
    ...
  ],
  "status": "Review",
  "telemetry": {
    "skill": "execute-task",
    "task_file": ".claude/tasks/task-006.md",
    "tasks_completed": 5,
    "subtasks_completed": 18,
    "tests_passed": true,
    "total_tests": 19,
    "files_modified_count": 11,
    "duration_ms": 245680,
    "halt_count": 0
  }
}
```

---

## Error Handling

If any step fails:

**1. Task File Not Found:**
- Error: "Task file not found"
- Action: Verify file path

**2. Task Status Not Approved:**
- Error: "Task must be Approved before execution"
- Action: Check task status, update if needed

**3. Test Failures:**
- Error: "X tests failing"
- Action: Review failures, fix issues, re-run

**4. Missing Dependencies:**
- Error: "Dependency X not found"
- Action: Verify task spec includes dependency info

---

## Best Practices

1. **Trust the Task Spec** - Context is already embedded, don't search for more
2. **Sequential Execution** - Complete current subtask before next
3. **Test Before Checking** - Write and run tests before marking complete
4. **Document As You Go** - Update completion notes after each task
5. **Respect Permissions** - Only edit Implementation Record and checkboxes
6. **Halt When Appropriate** - Don't guess if requirements unclear

**See:** `references/best-practices.md` for detailed best practices

---

## Routing Guidance

**Use this skill when:**
- Executing an approved task specification
- Need sequential, validated task execution
- Want comprehensive testing and documentation
- Need implementation audit trail

**Always use after:**
- Task spec created and approved
- Planning complete

**Before:**
- Quality review
- Pull request creation

---

## Reference Files

Detailed documentation in `references/`:

- **configuration-guide.md**: Loading config, always-load files, status management
- **task-execution-guide.md**: Executing tasks/subtasks, validation gates, examples
- **validation-guide.md**: Final validation, documentation, completion summary
- **implementation-record.md**: Templates for Implementation Record section
- **permissions-halts.md**: Permission boundaries, halt conditions, error handling
- **best-practices.md**: Best practices, pitfalls to avoid, integration patterns

---

## Using This Skill

**From command line:**
```bash
Use .claude/skills/implementation/execute-task/SKILL.md with input {task_file: ".claude/tasks/task-006.md"}
```

**Example:**
```bash
Execute task: .claude/tasks/task-006-user-signup.md
```

---

## Philosophy

This skill embodies BMAD's 3-layer architecture:

- **Uses Commands** (Layer 1): bmad-commands for read_file, run_tests
- **Provides Composition** (Layer 2): Task execution + validation workflow
- **Enables Orchestration** (Layer 3): Used by James/developer subagents

By using commands, this skill is:
- **Observable**: Telemetry tracks execution metrics
- **Testable**: Commands have known contracts
- **Composable**: Fits into development workflow
- **Reliable**: Deterministic task execution

---

*Part of BMAD Enhanced Implementation Suite*
