---
name: refactor-code
description: Safely improve code quality through test-driven refactoring with automatic validation and rollback. Use during quality review to reduce technical debt while preserving behavior.
acceptance:
  - config_validated: "Configuration allows refactoring and prerequisites verified"
  - opportunities_identified: "Refactoring opportunities identified and prioritized by risk"
  - refactorings_applied: "Selected refactorings applied incrementally with test validation"
  - log_created: "Refactoring log documenting all changes with rationale"
  - tests_passing: "All tests passing after refactoring with no behavioral changes"
inputs:
  task_file:
    type: string
    required: true
    description: "Path to task specification with quality findings"
  aggressiveness:
    type: enum
    required: false
    description: "Refactoring scope: conservative, moderate, aggressive"
    default: "moderate"
  allow_refactoring:
    type: boolean
    required: false
    description: "Override config to allow/disallow refactoring"
outputs:
  refactorings_applied:
    type: number
    description: "Number of refactorings successfully applied"
  refactorings_failed:
    type: number
    description: "Number of refactorings that failed and were rolled back"
  files_modified:
    type: array
    description: "List of files modified during refactoring"
  quality_impact:
    type: object
    description: "Before/after quality metrics showing improvements"
telemetry:
  emit: "skill.refactor-code.completed"
  track:
    - refactorings_applied
    - refactorings_failed
    - refactorings_skipped
    - success_rate
    - files_modified_count
    - quality_improvement_percent
    - duration_ms
---

# Refactor Code Skill

## Purpose

Safely improve code quality through automated refactoring while maintaining behavioral correctness. This skill identifies refactoring opportunities from quality findings and applies them incrementally with continuous test validation.

**Core Capabilities:**
- Test-driven refactoring (run tests after each change)
- Automatic rollback on test failures
- Risk-based prioritization (P0-P3, Low/Medium/High risk)
- Incremental application (one refactoring at a time)
- Full traceability (log all changes with rationale)
- Quality metrics tracking (before/after comparison)

**Key Innovation:**
Safety-first approach ensures refactorings never break functionality. Each change is validated with tests before proceeding.

## Prerequisites

- Task status is "Review"
- Quality assessment has been run (quality gate exists)
- Tests exist and are currently passing
- Configuration allows refactoring (`quality.allowRefactoring: true`)

---

## Workflow

### Step 0: Load Configuration and Validate Prerequisites

**Action:** Verify refactoring is allowed and safe to proceed.

**Load configuration:**
```yaml
# Read .claude/config.yaml
quality:
  allowRefactoring: true|false
  refactoringAggressiveness: conservative|moderate|aggressive
  requireTestsPass: true
  refactoringLog: .claude/quality/refactoring-log.md
```

**Check prerequisites:**
1. Verify `allowRefactoring: true` in config (or input override)
2. Verify task status is "Review"
3. Verify quality assessment exists (`.claude/quality/gates/{task-id}-gate.yaml`)
4. Verify tests exist and are passing

**Get refactoring scope:**
```
Automated refactoring is available. Choose scope:
A) Skip refactoring (proceed to final quality gate)
B) Conservative (low-risk improvements only, P0 refactorings)
C) Moderate (recommended improvements, P0 + P1 refactorings)
D) Aggressive (all identified opportunities, P0 + P1 + P2)

Which option would you like? [Default: B]
```

**Halt if:**
- Configuration disables refactoring and no input override
- No tests exist (can't validate safety)
- Tests are currently failing
- Quality assessment not yet run
- User chooses to skip

**Output:**
```
✓ Refactoring enabled in configuration
✓ Tests exist and passing (45 tests, 100% pass rate)
✓ Quality assessment complete
✓ Refactoring scope: Moderate (P0 + P1)
✓ Ready to proceed
```

**See:** `references/risk-assessment-guide.md` for aggressiveness levels

---

### Step 1: Analyze Code for Refactoring Opportunities

**Action:** Identify specific refactoring opportunities based on quality findings.

**Load quality findings:**
1. Read quality gate file (`.claude/quality/gates/{task-id}-gate.yaml`)
2. Extract issues by severity (critical, high, medium, low)
3. Extract technical debt items
4. Extract code quality findings

**Scan implementation files:**
Read all files from task Implementation Record and identify patterns:
- **Extract Method**: Long methods (>50 lines)
- **Extract Variable**: Complex expressions
- **Rename**: Unclear variable/function names
- **Remove Duplication**: Repeated code blocks (2+ occurrences)
- **Simplify Conditionals**: Nested if/else chains
- **Extract Class**: Classes with too many responsibilities
- **Inline**: Unnecessary indirection
- **Move Method**: Misplaced functionality

**Prioritize refactorings:**
- **P0 (Critical):** Addresses critical/high severity quality issues
- **P1 (High):** Reduces technical debt
- **P2 (Medium):** Improves maintainability
- **P3 (Low):** Nice-to-have improvements

**Estimate risk for each:**
- **Low Risk:** Rename, extract variable, inline
- **Medium Risk:** Extract method, simplify conditionals
- **High Risk:** Extract class, move method, large-scale changes

**Filter by aggressiveness level:**
- **Conservative:** P0 only, low-risk refactorings
- **Moderate:** P0 + P1, low-to-medium risk refactorings
- **Aggressive:** P0 + P1 + P2, all risk levels

**Example output:**
```
Refactoring Opportunities Identified:

P0 (Critical):
1. Extract validation logic from signup route (Medium Risk)
   - File: src/routes/auth/signup.ts:15-30
   - Reason: High severity issue "Validation in route handler"
   - Impact: Improves testability and separation of concerns

P1 (High):
2. Extract method: hashPassword from signup service (Low Risk)
   - File: src/services/auth/signup.service.ts:34-35
   - Reason: Reduces technical debt "Password hashing inline"
   - Impact: Improves reusability

3. Rename: existingUser → existingUserWithEmail (Low Risk)
   - File: src/services/auth/signup.service.ts:25
   - Reason: Improves code clarity
   - Impact: Better self-documenting code

Selected for Moderate Refactoring: 1, 2, 3 (P0 + P1)
```

**Halt if:**
- No refactoring opportunities identified (already clean code)
- All refactorings exceed chosen aggressiveness level
- All refactorings are high-risk (safety concern)

**See:** `references/refactoring-patterns.md` for pattern identification

---

### Step 2: Apply Refactorings Incrementally

**Action:** Apply each refactoring one at a time with test validation.

**For each selected refactoring (in priority order):**

**1. Announce refactoring:**
```
Applying refactoring 1/3: Extract validation logic
- File: src/routes/auth/signup.ts
- Type: Extract Method
- Risk: Medium
- Expected: Validation logic moved to separate module
```

**2. Apply single refactoring:**
- Read current file content
- Apply refactoring transformation
- Write refactored content
- Create backup of original (for rollback)

**3. Run tests immediately:**
```bash
npm test  # or appropriate test command from config
```
- Capture test output
- Check exit code (0 = pass, non-zero = fail)

**4. Evaluate test results:**

**If tests pass:**
```
✓ Refactoring successful
✓ All tests passing (45/45)
✓ Proceeding to next refactoring
```
- Log refactoring in refactoring log
- Keep changes
- Proceed to next refactoring

**If tests fail:**
```
✗ Tests failed after refactoring
✗ Failed tests: 2/45
✗ Rolling back changes
```
- Restore original file from backup
- Log failed refactoring attempt with error details
- Skip this refactoring
- Proceed to next refactoring (or halt if critical P0 failure)

**5. Update progress:**
```
Refactoring Progress: 1/3 complete
- Applied: 1
- Skipped: 0
- Failed: 0
```

**Safety rules:**
- Never apply multiple refactorings simultaneously
- Never skip test validation
- Never continue if critical (P0) refactoring fails
- Never modify tests to make them pass
- Always preserve backups until tests pass

**Example output:**
```
Refactoring Complete: 3/3 applied successfully
- Extract validation logic: ✓ Success
- Extract hashPassword method: ✓ Success
- Rename existingUser variable: ✓ Success
- All tests passing: 45/45 (100%)
```

**Halt if:**
- Multiple consecutive failures (>3)
- Tests fail and can't be restored
- User requests halt
- Time limit exceeded (optional safety)

**See:** `references/incremental-application-guide.md` for detailed process

---

### Step 3: Create Refactoring Log

**Action:** Document all refactoring changes with rationale.

**Create/update log file:**
- Path: `.claude/quality/refactoring-log.md`
- Append new entry (preserve existing logs)

**Log structure:**
```markdown
## Refactoring Session: {task-id} - {date}

**Task:** {task-title}
**Scope:** {conservative|moderate|aggressive}
**Duration:** {minutes}
**Success Rate:** {applied}/{attempted} refactorings

### Refactorings Applied

#### 1. Extract Validation Logic
- **File:** src/routes/auth/signup.ts:15-30
- **Type:** Extract Method
- **Risk:** Medium
- **Rationale:** Validation in route handler (high severity issue)
- **Before:** 30 lines of validation in route handler
- **After:** 3 lines calling validateSignupRequest()
- **Impact:** Improved testability, separation of concerns
- **Tests:** ✓ All passing (45/45)

### Refactorings Failed

None

### Files Modified

- src/routes/auth/signup.ts (30 lines → 15 lines, -50%)
- src/utils/validation.ts (0 lines → 35 lines, new file)

### Test Results

- Before: 45 tests, 45 passing, 0 failing
- After: 45 tests, 45 passing, 0 failing
- Execution time: 4.2s → 4.1s (-0.1s)

### Quality Impact

- Code duplication: Reduced
- Separation of concerns: Improved
- Testability: Improved
- Maintainability: Improved
```

**Update quality gate file:**
- Add refactoring summary to gate file
- Update code quality metrics
- Note improvements in maintainability

**Output:**
```
✓ Refactoring log created: .claude/quality/refactoring-log.md
✓ Quality gate updated with refactoring results
✓ 3 refactorings applied, 0 failed, 0 skipped
```

**See:** `references/refactoring-log-template.md` for complete structure

---

### Step 4: Final Test Validation and Summary

**Action:** Confirm all tests pass and provide comprehensive summary.

**Run full test suite:**
```bash
npm test
npm run test:integration  # if exists
npm run test:e2e          # if exists
```

**Generate coverage report:**
```bash
npm run test:coverage  # if configured
```

**Compare before/after metrics:**
```
Code Quality Metrics:

Lines of Code:
- Before: 120 lines
- After: 110 lines
- Change: -8% (improved)

Cyclomatic Complexity:
- Before: Average 8.5
- After: Average 6.2
- Change: -27% (improved)

Code Duplication:
- Before: 15% duplicated
- After: 3% duplicated
- Change: -80% (improved)

Test Coverage:
- Before: 85%
- After: 87%
- Change: +2% (improved)
```

**Provide final summary:**
```markdown
## Automated Refactoring Complete

**Status:** ✓ Successful
**Refactorings Applied:** 3/3 (100% success rate)
**Duration:** 15 minutes
**Tests:** All passing (45/45)

**Quality Improvements:**
- ✅ Code complexity reduced 27%
- ✅ Duplication reduced 80%
- ✅ Test coverage increased 2%
- ✅ Maintainability improved

**Files Modified:**
- Modified: src/routes/auth/signup.ts
- Modified: src/services/auth/signup.service.ts
- Created: src/utils/validation.ts
- Created: src/utils/password.ts

**Next Steps:**
1. Review refactored code (git diff)
2. Verify refactorings align with coding style
3. Commit: "refactor: improve code quality (automated)"
4. Proceed with quality gate decision

**Detailed Log:** .claude/quality/refactoring-log.md
```

**Update task file:**
Append refactoring summary to task's Quality Review section with:
- Date and scope
- Success rate
- Refactorings applied
- Quality impact
- Test validation results

**Halt if:**
- Final test suite fails (critical issue)
- Coverage drops significantly (regression)
- User reports unexpected behavior

---

## Completion Criteria

Refactoring is complete when:

- [ ] Prerequisites validated (config, tests, quality gate)
- [ ] Refactoring opportunities identified and prioritized
- [ ] Selected refactorings applied incrementally
- [ ] All tests passing after refactoring
- [ ] Refactoring log created with full documentation
- [ ] Task file updated with summary
- [ ] Quality metrics improved or maintained
- [ ] User notified with actionable next steps

---

## Safety Guarantees

This skill guarantees:

1. **Behavioral Preservation:** No functionality changes, only structure
2. **Test Validation:** Tests run after each refactoring
3. **Automatic Rollback:** Failed refactorings immediately reverted
4. **Full Traceability:** All changes logged with rationale
5. **Incremental Changes:** One refactoring at a time
6. **User Control:** User chooses aggressiveness level

---

## Integration with Quality Review

This skill integrates with the quality review workflow:

**Quality Review Workflow:**
1. risk-profile → Identify risks
2. test-design → Validate test strategy
3. trace-requirements → Map ACs to tests
4. nfr-assess → Assess security, performance, maintainability
5. **refactor-code → Improve code quality (optional)**
6. quality-gate → Final decision (reflects improvements)

**When to run:**
- After NFR assessment (when issues identified)
- Before quality gate (so improvements reflected in decision)
- Only if user opts in
- Only if tests exist and pass

---

## Routing Guidance

**Use this skill when:**
- Quality review identifies refactoring opportunities
- Technical debt needs systematic reduction
- Code quality metrics below targets
- Maintainability concerns raised in review
- User opts in for automated improvements

**Do NOT use for:**
- Feature additions (use implementation skills)
- Bug fixes (use fix-issue skill)
- Breaking changes (requires manual review)
- Experimental refactorings (too risky)
- Projects without tests (can't validate safety)

**Feeds into:**
- quality-gate skill (improved metrics inform decision)

---

## Best Practices

1. **Start Conservative:**
   - First session: Use conservative mode
   - Build confidence before moderate/aggressive

2. **Review Changes:**
   - Always review refactored code via git diff
   - Verify alignment with coding style
   - Check for unintended consequences

3. **Commit Separately:**
   - Commit refactorings separate from features
   - Message: "refactor: {description} (automated)"

4. **Monitor Impact:**
   - Track quality metrics over time
   - Verify maintainability improves
   - Identify patterns to refactor proactively

---

## Limitations

**This skill cannot:**
- ❌ Fix bugs (changes behavior)
- ❌ Add features (changes scope)
- ❌ Refactor without tests (can't validate safety)
- ❌ Change architectural patterns (too risky)
- ❌ Refactor external libraries (not under control)

**This skill requires:**
- ✅ Existing tests that pass
- ✅ Clear separation between test and implementation
- ✅ Permission in configuration
- ✅ Quality assessment already run

---

## Reference Files

Detailed documentation in `references/`:

- **refactoring-patterns.md**: Common refactoring patterns with examples
- **risk-assessment-guide.md**: Risk levels, assessment, filtering by aggressiveness
- **incremental-application-guide.md**: Step-by-step application, test validation, rollback
- **refactoring-log-template.md**: Log structure and documentation format

---

## Using This Skill

**From command line:**
```bash
Use .claude/skills/quality/refactor-code/SKILL.md with input {task_file: ".claude/tasks/task-001.md", aggressiveness: "moderate"}
```

---

## Philosophy

This skill embodies BMAD's 3-layer architecture:

- **Uses Commands** (Layer 1): bmad-commands for read_file, write_file, run_tests
- **Provides Composition** (Layer 2): Test-driven refactoring workflow
- **Enables Orchestration** (Layer 3): Used by quality subagents

By refactoring safely and incrementally, this skill is:
- **Observable**: Telemetry tracks refactoring success rates
- **Testable**: Test validation after each change
- **Composable**: Integrates with quality review workflow
- **Reliable**: Automatic rollback on failures

---

*Part of BMAD Enhanced Quality Suite*
