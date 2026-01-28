# Best Practices & Integration Guide

## Purpose

Best practices for task execution, common pitfalls to avoid, and integration with other skills.

---

## Best Practices

### 1. Trust the Task Spec

**✅ Good:**
```markdown
Reading from task spec context:
- Data model structure already defined
- API endpoint spec already documented
- Testing requirements already specified
- File paths already provided

Implementing exactly as specified without additional research.
```

**❌ Bad:**
```markdown
- Task spec says "User model with email"
- Let me search architecture docs for user model patterns
- Let me read PRD for user requirements
- Let me check other files for user examples

Result: Wasted time, context drift, unnecessary complexity
```

**Why:**
- Planning skill already embedded ALL necessary context
- Architecture lookups during implementation cause drift
- Task spec is single source of truth
- Always-load files provide coding standards

**Principle:** Everything needed is in task spec + always-load files

---

### 2. Sequential Execution

**✅ Good:**
```markdown
Task 1:
  → Subtask 1.1 → Validate → Mark complete
  → Subtask 1.2 → Validate → Mark complete
  → Task validation → Mark complete

Task 2:
  → Subtask 2.1 → Validate → Mark complete
  ...
```

**❌ Bad:**
```markdown
- Look ahead to Task 3 (seems easier)
- Start Task 3 Subtask 3.2 (can do this now)
- Go back to Task 1
- Jump to Task 2 Subtask 2.3

Result: Confusion, missing dependencies, incomplete tasks
```

**Why:**
- Tasks ordered for dependencies
- Sequential execution prevents missing steps
- Validation gates ensure quality
- Clear progress tracking

**Principle:** One task at a time, one subtask at a time

---

### 3. Test Before Checking

**✅ Good:**
```markdown
Subtask: Write unit tests for user schema

1. Write tests (12 tests)
2. Run tests: 12 passed, 0 failed ✅
3. Verify coverage: 94% ✅
4. Mark subtask complete: [x]
```

**❌ Bad:**
```markdown
1. Write tests (12 tests)
2. Mark subtask complete: [x]
3. Move to next subtask
4. (Tests never run, might be failing)
```

**Why:**
- Tests must pass before marking complete
- Prevents shipping broken tests
- Catches issues immediately
- Ensures validation gates work

**Principle:** Write → Run → Verify → Check

---

### 4. Document As You Go

**✅ Good:**
```markdown
After each task:
- Update Completion Notes with details
- Document decisions and learnings
- Note deviations from plan
- Record patterns for reuse
- Update Files Modified list

Result: Rich documentation, clear audit trail
```

**❌ Bad:**
```markdown
Complete all 5 tasks silently, then try to remember:
- What did I do in Task 1?
- Why did I make that choice in Task 2?
- What was that edge case in Task 3?

Result: Incomplete documentation, lost learnings
```

**Why:**
- Fresh memory = better documentation
- Learnings help future tasks
- Audit trail for quality review
- Patterns can be reused

**Principle:** Document immediately, not at the end

---

### 5. Respect Permissions

**✅ Good:**
```markdown
Editing only:
- Implementation Record section
- Checkboxes ([ ] to [x])
- Status line (Approved → InProgress → Review)

Never touching:
- Objective, AC, Context, Task descriptions
```

**❌ Bad:**
```markdown
- "I'll just clarify this AC while I'm here..."
- "Let me fix this typo in the objective..."
- "I'll add this context that's missing..."

Result: Corrupted task spec, audit trail broken
```

**Why:**
- Clear permission boundaries prevent accidents
- Task spec is planning artifact (read-only for dev)
- Implementation Record is dev artifact (write-only for dev)
- Separation of concerns

**Principle:** Stay within permission boundaries

---

### 6. Halt When Appropriate

**✅ Good:**
```markdown
Subtask fails 3 times:
→ HALT
→ Present error to user
→ Ask for guidance
→ Resume when resolved

Ambiguous requirement:
→ HALT
→ Explain ambiguity
→ Ask for clarification
→ Resume with clear direction
```

**❌ Bad:**
```markdown
Subtask fails 3 times:
→ Try different approach (guess #4)
→ Try another approach (guess #5)
→ Try random solution (guess #10)
→ Eventually something works (maybe)

Result: Wasted time, wrong solution, brittle code
```

**Why:**
- Guessing wastes time
- User input faster than trial-and-error
- Prevents wrong solutions
- Maintains quality

**Principle:** Ask, don't guess

---

## Common Pitfalls to Avoid

### Pitfall 1: Loading Architecture Docs

**❌ Don't:**
```markdown
During implementation:
- Read docs/architecture/user-model.md
- Read docs/PRD.md
- Read docs/api-spec.md
- Search codebase for patterns
```

**✅ Do:**
```markdown
Read only:
- Task spec (has all context embedded)
- Always-load files (coding standards)
- Existing code referenced in task spec
```

**Why:**
- Context already embedded by planning skill
- Architecture lookups cause drift
- Wastes time searching
- Introduces inconsistencies

---

### Pitfall 2: Skipping Validations

**❌ Don't:**
```markdown
- Write code
- Mark subtask complete [x]
- Move to next subtask
- (Never run tests, never validate)
```

**✅ Do:**
```markdown
- Write code
- Run tests (must pass)
- Run linter (must pass)
- Verify output matches requirements
- THEN mark subtask complete [x]
```

**Why:**
- Validation gates ensure quality
- Catch issues early
- Prevent regressions
- Maintain test coverage

---

### Pitfall 3: Editing Wrong Sections

**❌ Don't:**
```markdown
"I'll just update this AC to match what I implemented..."
"Let me clarify this task description..."
"I'll fix this typo in the context..."
```

**✅ Do:**
```markdown
"Task spec is read-only. If something needs changing:
1. Note the issue in Completion Notes
2. Halt if it's critical
3. Ask user to update task spec if needed"
```

**Why:**
- Prevents corruption of planning artifact
- Maintains clear audit trail
- Separation of concerns (plan vs. implementation)

---

### Pitfall 4: Non-Sequential Execution

**❌ Don't:**
```markdown
- Task 1 subtask 1.1 done
- Task 3 looks easy, do that
- Task 2 subtask 2.3 seems interesting
- Back to Task 1 subtask 1.2
```

**✅ Do:**
```markdown
- Task 1: Complete all subtasks in order
- Task 1 validation
- Task 2: Complete all subtasks in order
- Task 2 validation
...
```

**Why:**
- Dependencies between tasks
- Clear progress tracking
- Prevents missing steps
- Easier to resume if halted

---

### Pitfall 5: Insufficient Documentation

**❌ Don't:**
```markdown
Implementation Record:
### Completion Notes
Implemented all tasks.

### Files Modified
Created files, modified files.

### Testing Results
Tests passing.
```

**✅ Do:**
```markdown
Implementation Record:
### Completion Notes
**Task 1:** Created User model with Zod validation...
- Discovered unicode email edge case
- Added punycode encoding
- 12 tests, 94% coverage
- Pattern reusable for other models

[Detailed notes for each task]

### Files Modified
**Created:**
- src/types/user.ts (User interface)
- src/schemas/user.schema.ts (Zod validation)
[Complete list with descriptions]

### Testing Results
**Unit Tests:**
- src/schemas/__tests__/user.schema.test.ts: 12 passed
- Coverage: 94% statements, 89% branches
[Complete test results]
```

**Why:**
- Detailed documentation helps future work
- Learnings are valuable
- Audit trail for quality review
- Patterns can be reused

---

### Pitfall 6: Ignoring Halt Conditions

**❌ Don't:**
```markdown
Attempt 1: Failed
Attempt 2: Failed
Attempt 3: Failed
Attempt 4: Failed (trying different approach)
Attempt 5: Failed (trying another approach)
...
Attempt 15: Finally works (maybe)
```

**✅ Do:**
```markdown
Attempt 1: Failed
Attempt 2: Failed
Attempt 3: Failed
→ HALT
→ Present error to user
→ Get guidance
→ Resume with correct approach
```

**Why:**
- User input faster than trial-and-error
- Prevents wrong solutions
- Saves time
- Maintains code quality

---

## Integration with Other Skills

### Before Execute-Task

**Planning Skills:**
1. **create-task-spec** - Creates initial task specification
2. **refine-story** - Refines requirements into detailed tasks
3. **breakdown-epic** - Breaks large features into tasks

**Result:** Task file with status "Approved" containing:
- Complete objective
- Measurable acceptance criteria
- Embedded context (data models, APIs, patterns, file paths)
- Sequential task breakdown with subtasks
- All info needed for implementation

**Handoff:**
```markdown
Planning Complete → Task Approved → Ready for Execute-Task

Task file: .claude/tasks/task-006-user-signup.md
Status: Approved
Context: All embedded in task file
Standards: Referenced in always-load files
```

---

### During Execute-Task

**Implementation Skills:**
1. **execute-task** (this skill) - Main implementation orchestrator
2. **bmad-commands** - Primitive operations (read, write, test)

**Workflow:**
- Execute-task orchestrates sequence
- bmad-commands provides deterministic operations
- Tests executed via bmad-commands
- Files read/written via bmad-commands

**Benefits:**
- Observable (telemetry from commands)
- Testable (commands have contracts)
- Composable (skills use commands)
- Reliable (deterministic operations)

---

### After Execute-Task

**Quality Skills:**
1. **review-task** - Systematic quality assessment
2. **quality-gate** - Quality threshold checks
3. **test-design** - Test coverage analysis

**Handoff:**
```markdown
Implementation Complete → Status: Review → Ready for Quality Skills

Task file: .claude/tasks/task-006-user-signup.md
Status: Review
Implementation Record: Complete
Tests: All passing (27 tests)
Coverage: 94% statements

Next: Use quality review skill for systematic assessment
```

**Example:**
```bash
# After execute-task completes:
Use review-task skill with task-006-user-signup.md

# Review evaluates:
- Implementation matches ACs
- Code quality standards
- Test coverage adequacy
- Documentation completeness

# If quality gate passes:
- Mark task status as "Done"
- Proceed to next task or integration
```

---

### Workflow Integration

**Complete Flow:**

```
Planning Phase:
1. create-task-spec → Task file (Draft)
2. refine-story → Task file (Refined)
3. User approval → Task file (Approved)

↓

Implementation Phase:
4. execute-task (this skill) → Implementation complete
   - Status: Approved → InProgress → Review
   - Uses bmad-commands for operations
   - Writes Implementation Record
   - All tests passing

↓

Quality Phase:
5. review-task → Quality assessment
6. quality-gate → Pass/fail decision
   - If pass: Status → Done
   - If fail: Status → InProgress, fix issues

↓

Integration Phase:
7. Commit changes
8. Create pull request
9. Deploy (if applicable)
```

---

## Quick Reference

**Best Practices:**
1. Trust task spec (don't search for more context)
2. Sequential execution (one task at a time)
3. Test before checking (validate before marking complete)
4. Document as you go (not at the end)
5. Respect permissions (Implementation Record only)
6. Halt when appropriate (ask, don't guess)

**Pitfalls to Avoid:**
1. Loading architecture docs (context already embedded)
2. Skipping validations (test before checking)
3. Editing wrong sections (permissions matter)
4. Non-sequential execution (follow task order)
5. Insufficient documentation (detail is valuable)
6. Ignoring halt conditions (halt at 3 failures)

**Integration:**
- Before: Planning skills create approved task
- During: Uses bmad-commands for operations
- After: Quality skills assess and approve

---

*Part of execute-task skill - Implementation Suite*
