# Quality Skill: Automated Code Refactoring

<!-- BMAD Enhanced Quality Skill -->
<!-- Safe, test-driven refactoring during quality review -->
<!-- Version: 1.0 -->

## Purpose

Safely improve code quality through automated refactoring while maintaining behavioral correctness. This skill identifies refactoring opportunities and applies them incrementally with continuous test validation.

**Key Innovation:**
- Test-driven refactoring: Run tests after each change
- Automatic rollback: Revert if tests fail
- Safety first: Only safe, behavior-preserving refactorings
- Evidence-based: Log rationale for all changes

## When to Use This Skill

Use this skill when you need to:
- Improve code quality without changing behavior
- Reduce technical debt systematically
- Apply refactorings identified during quality review
- Enhance maintainability before production deployment

**Do NOT use this skill for:**
- Feature additions (use implementation skill)
- Bug fixes (use debug skill)
- Breaking changes (requires manual review)
- Experimental refactorings (too risky)

## File Modification Permissions

**CRITICAL PERMISSION BOUNDARIES:**

**YOU ARE AUTHORIZED TO:**
- ✅ Read all implementation and test files
- ✅ Modify implementation files for refactoring
- ✅ Run tests to validate refactorings
- ✅ Create refactoring log file
- ✅ Update quality assessment with refactoring notes

**YOU ARE NOT AUTHORIZED TO:**
- ❌ Modify test behavior (tests must remain unchanged)
- ❌ Change functionality (behavior must be preserved)
- ❌ Modify task specification
- ❌ Skip test validation
- ❌ Force refactorings when tests fail

---

## SEQUENTIAL Task Execution

**CRITICAL:** Execute steps in order. Never skip test validation.

### Step 0: Load Configuration and Validate Prerequisites

**Purpose:** Verify refactoring is allowed and safe to proceed

**Actions:**

1. **Load Configuration:**
   ```yaml
   # Read .claude/config.yaml
   quality:
     allowRefactoring: true|false
     refactoringAggressiveness: conservative|moderate|aggressive
     requireTestsPass: true
     refactoringLog: .claude/quality/refactoring-log.md
   ```

2. **Check Prerequisites:**
   - Verify `allowRefactoring: true` in config
   - Verify task status is "Review"
   - Verify quality assessment has been run (quality gate exists)
   - Verify tests exist and are passing

3. **Get Refactoring Scope:**
   - Prompt user: "Automated refactoring is available. Options:
     - A) Skip refactoring (proceed to final quality gate)
     - B) Conservative refactoring (low-risk improvements only)
     - C) Moderate refactoring (recommended improvements)
     - D) Aggressive refactoring (all identified opportunities)

     Which option would you like?"
   - Store user's choice

**Halt If:**
- Configuration disables refactoring
- No tests exist (can't validate safety)
- Tests are currently failing
- Quality assessment not yet run
- User chooses to skip

**Output:**
```
✓ Refactoring enabled in configuration
✓ Tests exist and passing (45 tests, 100% pass rate)
✓ Quality assessment complete
✓ Refactoring scope: Moderate
✓ Ready to proceed
```

---

### Step 1: Analyze Code for Refactoring Opportunities

**Purpose:** Identify specific refactoring opportunities based on quality findings

**Actions:**

1. **Load Quality Findings:**
   - Read quality gate file (`.claude/quality/gates/{task-id}-gate.yaml`)
   - Extract issues by severity (critical, high, medium, low)
   - Extract technical debt items
   - Extract code quality findings

2. **Scan Implementation Files:**
   - Read all files from task Implementation Record
   - Identify common refactoring patterns:
     - **Extract Method**: Long methods (>50 lines)
     - **Extract Variable**: Complex expressions
     - **Rename**: Unclear variable/function names
     - **Remove Duplication**: Repeated code blocks
     - **Simplify Conditionals**: Nested if/else chains
     - **Extract Class**: Classes with too many responsibilities
     - **Inline**: Unnecessary indirection
     - **Move Method**: Misplaced functionality

3. **Prioritize Refactorings:**
   - **P0 (Critical):** Addresses critical/high severity issues
   - **P1 (High):** Reduces technical debt
   - **P2 (Medium):** Improves maintainability
   - **P3 (Low):** Nice-to-have improvements

4. **Filter by Aggressiveness Level:**
   - **Conservative:** Only P0 refactorings, very safe
   - **Moderate:** P0 + P1 refactorings, recommended
   - **Aggressive:** P0 + P1 + P2 refactorings, all opportunities

5. **Estimate Risk for Each Refactoring:**
   - **Low Risk:** Rename, extract variable, inline
   - **Medium Risk:** Extract method, simplify conditionals
   - **High Risk:** Extract class, move method, large-scale changes

**Output:**
```
Refactoring Opportunities Identified:

P0 (Critical):
1. Extract validation logic from signup route (Medium Risk)
   - File: src/routes/auth/signup.ts:15-30
   - Reason: Addresses high severity issue "Validation in route handler"
   - Impact: Improves testability and separation of concerns

P1 (High):
2. Extract method: hashPassword from signup service (Low Risk)
   - File: src/services/auth/signup.service.ts:34-35
   - Reason: Reduces technical debt "Password hashing inline"
   - Impact: Improves reusability

3. Rename variable: existingUser → existingUserWithEmail (Low Risk)
   - File: src/services/auth/signup.service.ts:25
   - Reason: Improves code clarity
   - Impact: Better self-documenting code

P2 (Medium):
4. Extract interface: SignupServiceDeps (Low Risk)
   - File: src/services/auth/signup.service.ts
   - Reason: Improves testability
   - Impact: Easier to mock dependencies

Selected for Moderate Refactoring: 1, 2, 3 (P0 + P1)
```

**Halt Conditions:**
- No refactoring opportunities identified (already clean code)
- All identified refactorings exceed user's chosen aggressiveness level
- Risk assessment shows all refactorings are high-risk

---

### Step 2: Apply Refactorings Incrementally

**Purpose:** Apply each refactoring one at a time with validation

**Actions:**

For each selected refactoring (in priority order):

1. **Announce Refactoring:**
   ```
   Applying refactoring 1/3: Extract validation logic
   - File: src/routes/auth/signup.ts
   - Type: Extract Method
   - Risk: Medium
   - Expected outcome: Validation logic moved to separate module
   ```

2. **Apply Single Refactoring:**
   - Read current file content
   - Apply refactoring transformation
   - Write refactored content
   - Create backup of original (in memory, for rollback)

3. **Run Tests Immediately:**
   ```bash
   npm test  # or appropriate test command
   ```
   - Capture test output
   - Check exit code (0 = pass, non-zero = fail)

4. **Evaluate Test Results:**
   - **If tests pass:**
     ```
     ✓ Refactoring successful
     ✓ All tests passing (45/45)
     ✓ Proceeding to next refactoring
     ```
     - Log refactoring in refactoring log
     - Keep changes
     - Proceed to next refactoring

   - **If tests fail:**
     ```
     ✗ Tests failed after refactoring
     ✗ Failed tests: 2/45
     ✗ Rolling back changes
     ```
     - Restore original file from backup
     - Log failed refactoring attempt
     - Skip this refactoring
     - Proceed to next refactoring (or halt if critical)

5. **Update Refactoring Progress:**
   ```
   Refactoring Progress: 1/3 complete
   - Applied: 1
   - Skipped: 0
   - Failed: 0
   ```

**Safety Rules:**
- Never apply multiple refactorings simultaneously
- Never skip test validation
- Never continue if critical refactoring fails
- Never modify tests to make them pass
- Always preserve backups until tests pass

**Output:**
```
Refactoring Complete: 3/3 applied successfully
- Extract validation logic: ✓ Success
- Extract hashPassword method: ✓ Success
- Rename existingUser variable: ✓ Success
- All tests passing: 45/45 (100%)
```

**Halt Conditions:**
- Multiple consecutive refactoring failures (>3)
- Tests fail and can't be restored
- User requests halt
- Time limit exceeded (optional safety measure)

---

### Step 3: Create Refactoring Log

**Purpose:** Document all refactoring changes with rationale

**Actions:**

1. **Create Log File:**
   - Path: `.claude/quality/refactoring-log.md`
   - Append new entry (preserve existing logs)

2. **Log Structure:**
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

   #### 2. Extract hashPassword Method
   - **File:** src/services/auth/signup.service.ts:34-35
   - **Type:** Extract Method
   - **Risk:** Low
   - **Rationale:** Reduce technical debt, improve reusability
   - **Before:** Inline bcrypt.hash(password, BCRYPT_COST)
   - **After:** Dedicated hashPassword(password) method
   - **Impact:** Reusable, easier to test, consistent hashing
   - **Tests:** ✓ All passing (45/45)

   ### Refactorings Skipped

   None

   ### Refactorings Failed

   None

   ### Files Modified

   - src/routes/auth/signup.ts (30 lines → 15 lines, -50%)
   - src/services/auth/signup.service.ts (47 lines → 52 lines, +10%)
   - src/utils/validation.ts (0 lines → 35 lines, new file)
   - src/utils/password.ts (0 lines → 20 lines, new file)

   ### Test Results

   - Before refactoring: 45 tests, 45 passing, 0 failing
   - After refactoring: 45 tests, 45 passing, 0 failing
   - Test execution time: 4.2s → 4.1s (-0.1s)

   ### Quality Impact

   - Code duplication: Reduced
   - Separation of concerns: Improved
   - Testability: Improved
   - Maintainability: Improved
   - Technical debt: Reduced
   ```

3. **Update Quality Gate File:**
   - Add refactoring summary to gate file
   - Update code quality metrics
   - Note improvements in maintainability

**Output:**
```
✓ Refactoring log created: .claude/quality/refactoring-log.md
✓ Quality gate updated with refactoring results
✓ 3 refactorings applied, 0 failed, 0 skipped
```

---

### Step 4: Update Task File with Refactoring Notes

**Purpose:** Record refactoring in task's Quality Review section

**Actions:**

1. **Read Task File:**
   - Load task specification
   - Find Quality Review section

2. **Append Refactoring Summary:**
   ```markdown
   ### Automated Refactoring Applied

   **Date:** 2025-10-28
   **Scope:** Moderate (P0 + P1 refactorings)
   **Success Rate:** 3/3 (100%)

   **Refactorings Applied:**
   1. ✓ Extract validation logic → src/utils/validation.ts
   2. ✓ Extract hashPassword method → src/utils/password.ts
   3. ✓ Rename existingUser → existingUserWithEmail

   **Quality Impact:**
   - Testability: Improved (validation and hashing now independently testable)
   - Maintainability: Improved (clearer separation of concerns)
   - Code duplication: Reduced
   - Technical debt: Reduced

   **Test Validation:**
   - All 45 tests passing after refactoring
   - No behavioral changes
   - Execution time unchanged (4.1s)

   **See detailed log:** .claude/quality/refactoring-log.md
   ```

3. **Update Files Modified Section:**
   - Add refactored files to list
   - Note which files were created vs modified

**Output:**
```
✓ Task file updated with refactoring summary
✓ Quality Review section reflects improvements
✓ Files Modified list updated
```

---

### Step 5: Final Test Validation and Summary

**Purpose:** Confirm all tests pass and provide final summary

**Actions:**

1. **Run Full Test Suite:**
   ```bash
   npm test
   npm run test:integration  # if exists
   npm run test:e2e         # if exists
   ```

2. **Generate Coverage Report:**
   ```bash
   npm run test:coverage
   ```

3. **Compare Before/After Metrics:**
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

4. **Provide Final Summary to User:**
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
   2. Verify refactorings align with your coding style
   3. Commit changes with message: "refactor: improve code quality (automated)"
   4. Proceed with quality gate decision

   **Detailed Log:** .claude/quality/refactoring-log.md
   ```

**Halt Conditions:**
- Final test suite fails (critical issue)
- Coverage drops significantly (regression)
- User reports unexpected behavior

---

## Completion Criteria

Automated refactoring is complete when:

- [ ] All selected refactorings attempted
- [ ] Tests passing after refactoring
- [ ] Refactoring log created
- [ ] Task file updated with summary
- [ ] Quality metrics improved or maintained
- [ ] User notified of results

## Safety Guarantees

This skill guarantees:

1. **Behavioral Preservation:** No functionality changes
2. **Test Validation:** Tests run after each refactoring
3. **Automatic Rollback:** Failed refactorings reverted
4. **Full Traceability:** All changes logged with rationale
5. **Incremental Changes:** One refactoring at a time
6. **User Control:** User chooses aggressiveness level

## Common Refactoring Patterns

### Extract Method

**When:** Method >50 lines or complex logic block

**Example:**
```typescript
// Before
async function signup(req, res) {
  if (!req.body.email) return res.status(400).json({...});
  if (!isValidEmail(req.body.email)) return res.status(400).json({...});
  if (!req.body.password) return res.status(400).json({...});
  if (req.body.password.length < 8) return res.status(400).json({...});
  // ... more validation

  // ... business logic
}

// After
async function signup(req, res) {
  const validation = validateSignupRequest(req.body);
  if (!validation.valid) return res.status(400).json(validation.errors);

  // ... business logic
}
```

### Extract Variable

**When:** Complex expression used multiple times

**Example:**
```typescript
// Before
if (user.role === 'admin' && user.permissions.includes('write') && !user.suspended) {
  // ...
}

// After
const canWrite = user.role === 'admin' &&
                 user.permissions.includes('write') &&
                 !user.suspended;
if (canWrite) {
  // ...
}
```

### Rename

**When:** Variable/function name unclear

**Example:**
```typescript
// Before
const u = await findUser(email);

// After
const existingUserWithEmail = await findUserByEmail(email);
```

### Remove Duplication

**When:** Same code appears 2+ times

**Example:**
```typescript
// Before
const hashedPassword = await bcrypt.hash(password, 12);  // In signup
const hashedPassword = await bcrypt.hash(newPassword, 12);  // In password reset

// After
async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, 12);
}
```

## Refactoring Risk Matrix

| Refactoring Type | Typical Risk | Safe When |
|------------------|-------------|-----------|
| Rename | Low | Good test coverage |
| Extract Variable | Low | Expression has no side effects |
| Inline | Low | Single usage, no side effects |
| Extract Method | Medium | Method has clear single responsibility |
| Move Method | Medium | Dependencies are clear |
| Simplify Conditional | Medium | Tests cover all branches |
| Extract Class | High | Class boundaries well-defined |
| Change Signature | High | All callers identified |

## Integration with Quality Review

This skill is designed to integrate with the `review-task.md` orchestrator:

**Quality Review Workflow (with refactoring):**
1. risk-profile → Identify risks
2. test-design → Validate test strategy
3. trace-requirements → Map AC to tests
4. nfr-assess → Assess security, performance, reliability, maintainability
5. **refactor-code → Improve code quality (optional)**
6. quality-gate → Final decision (reflects improvements)

**When to run refactoring:**
- After NFR assessment (when issues identified)
- Before quality gate (so improvements reflected in decision)
- Only if user opts in
- Only if tests exist and pass

## Best Practices

1. **Start Conservative:**
   - First refactoring session: Use conservative mode
   - Build confidence before moderate/aggressive

2. **Review Changes:**
   - Always review refactored code
   - Verify it matches your coding style
   - Check for unintended consequences

3. **Commit Separately:**
   - Commit refactorings separate from features
   - Use clear commit message: "refactor: {description} (automated)"

4. **Monitor Impact:**
   - Track code quality metrics over time
   - Verify maintainability improves
   - Watch for patterns to refactor proactively

5. **Teach the System:**
   - If refactoring inappropriate, note why
   - System learns from feedback
   - Improves over time

## Limitations

**This skill cannot:**
- ❌ Fix bugs (behavior changes)
- ❌ Add features (scope changes)
- ❌ Refactor without tests (can't validate safety)
- ❌ Change architectural patterns (too risky)
- ❌ Refactor external libraries (not under control)

**This skill requires:**
- ✅ Existing tests that pass
- ✅ Clear separation between test and implementation
- ✅ Permission in configuration
- ✅ Quality assessment already run

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial refactoring skill with test-driven safety |

---

**End of Refactoring Skill**
