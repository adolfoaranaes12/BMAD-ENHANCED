# Refactor Code Templates

This file contains all templates, output formats, and configuration examples for the refactor-code skill.

---

## Configuration Format

Expected configuration in `.claude/config.yaml`:

```yaml
quality:
  allowRefactoring: true|false
  refactoringAggressiveness: conservative|moderate|aggressive
  requireTestsPass: true
  refactoringLog: .claude/quality/refactoring-log.md

testing:
  testCommand: "npm test"
  coverageCommand: "npm run test:coverage"
  integrationCommand: "npm run test:integration"
  e2eCommand: "npm run test:e2e"
```

---

## User Decision: Refactoring Scope

When asking user to choose refactoring scope:

```
Automated refactoring is available. Choose scope:
A) Skip refactoring (proceed to final quality gate)
B) Conservative (low-risk improvements only, P0 refactorings)
C) Moderate (recommended improvements, P0 + P1 refactorings)
D) Aggressive (all identified opportunities, P0 + P1 + P2)

Which option would you like? [Default: B]
```

---

## Step 0 Output Template

Prerequisites validation output:

```
✓ Refactoring enabled in configuration
✓ Tests exist and passing (45 tests, 100% pass rate)
✓ Quality assessment complete
✓ Refactoring scope: Moderate (P0 + P1)
✓ Ready to proceed
```

Failure output:

```
✗ Refactoring prerequisites not met:
✗ Configuration disables refactoring (quality.allowRefactoring: false)
✗ Override with allow_refactoring=true input parameter if desired

Halting refactoring process.
```

---

## Step 1 Output Template

Refactoring opportunities analysis:

```
Refactoring Opportunities Identified:

P0 (Critical):
1. Extract validation logic from signup route (Medium Risk)
   - File: src/routes/auth/signup.ts:15-30
   - Reason: High severity issue "Validation in route handler"
   - Impact: Improves testability and separation of concerns
   - Estimated effort: 15 minutes

P1 (High):
2. Extract method: hashPassword from signup service (Low Risk)
   - File: src/services/auth/signup.service.ts:34-45
   - Reason: Reduces technical debt "Password hashing inline"
   - Impact: Improves reusability
   - Estimated effort: 5 minutes

3. Rename: existingUser → existingUserWithEmail (Low Risk)
   - File: src/services/auth/signup.service.ts:25
   - Reason: Improves code clarity
   - Impact: Better self-documenting code
   - Estimated effort: 2 minutes

P2 (Medium):
4. Simplify conditional in password validation (Low Risk)
   - File: src/utils/password-validator.ts:12-25
   - Reason: Nested if/else reduces readability
   - Impact: Improved maintainability
   - Estimated effort: 10 minutes

Selected for Moderate Refactoring: 1, 2, 3 (P0 + P1, 3 refactorings)
Skipped: 4 (P2, outside chosen scope)

Total estimated effort: 22 minutes
```

No opportunities output:

```
No refactoring opportunities identified within chosen scope.

Code quality is already meeting standards. Proceeding to quality gate.
```

---

## Step 2 Output Templates

### Announce Refactoring

Before applying each refactoring:

```
Applying refactoring 1/3: Extract validation logic
- File: src/routes/auth/signup.ts
- Type: Extract Method
- Risk: Medium
- Expected: Validation logic moved to separate module
```

### Success Output

After tests pass:

```
✓ Refactoring successful
✓ All tests passing (45/45)
✓ Changes committed to refactoring
✓ Proceeding to next refactoring
```

### Failure Output

After tests fail:

```
✗ Tests failed after refactoring
✗ Failed tests: 2/45
  - signup.service.test.ts: "should validate email format"
  - signup.service.test.ts: "should reject invalid passwords"
✗ Rolling back changes...
✓ Original code restored
✗ Skipping this refactoring

Error details logged to refactoring log.
```

### Progress Update

After each refactoring:

```
Refactoring Progress: 1/3 complete
- Applied: 1
- Skipped: 0
- Failed: 0
- Remaining: 2
```

### Final Progress

After all refactorings:

```
Refactoring Complete: 3/3 applied successfully

Applied Refactorings:
✓ 1. Extract validation logic → Success
✓ 2. Extract hashPassword method → Success
✓ 3. Rename existingUser variable → Success

Test Results:
- All tests passing: 45/45 (100%)
- Execution time: 4.2s
- No regressions detected
```

---

## Step 3: Refactoring Log Template

Complete refactoring log structure (append to `.claude/quality/refactoring-log.md`):

```markdown
## Refactoring Session: task-auth-001 - 2025-10-29

**Task:** Implement user signup with email verification
**Scope:** Moderate (P0 + P1)
**Duration:** 18 minutes
**Success Rate:** 3/3 refactorings (100%)

### Refactorings Applied

#### 1. Extract Validation Logic
- **File:** src/routes/auth/signup.ts:15-30
- **Type:** Extract Method
- **Priority:** P0 (Critical)
- **Risk:** Medium
- **Rationale:** Validation in route handler (high severity issue from quality gate)
- **Before:** 30 lines of validation logic embedded in route handler
- **After:** 3 lines calling `validateSignupRequest()` from utils/validation.ts
- **Impact:**
  - Improved testability (validation now independently testable)
  - Separation of concerns (route handles HTTP, validation isolated)
  - Reusability (validation can be used in other routes)
- **Tests:** ✓ All passing (45/45)
- **Files Modified:**
  - src/routes/auth/signup.ts (reduced 27 lines)
  - src/utils/validation.ts (created, 35 lines)

#### 2. Extract Method: hashPassword
- **File:** src/services/auth/signup.service.ts:34-45
- **Type:** Extract Method
- **Priority:** P1 (High)
- **Risk:** Low
- **Rationale:** Password hashing logic inline (technical debt item)
- **Before:** 12 lines of bcrypt hashing inline in service method
- **After:** 1 line calling `hashPassword()` from utils/password.ts
- **Impact:**
  - Reusability (hashing logic available for password resets)
  - Testability (hashing can be mocked in tests)
  - Maintainability (single source of truth for hashing)
- **Tests:** ✓ All passing (45/45)
- **Files Modified:**
  - src/services/auth/signup.service.ts (reduced 11 lines)
  - src/utils/password.ts (created, 18 lines)

#### 3. Rename: existingUser → existingUserWithEmail
- **File:** src/services/auth/signup.service.ts:25
- **Type:** Rename
- **Priority:** P1 (High)
- **Risk:** Low
- **Rationale:** Variable name ambiguous (code clarity issue)
- **Before:** Variable `existingUser` unclear what property it matches on
- **After:** Variable `existingUserWithEmail` explicitly indicates email lookup
- **Impact:**
  - Readability (self-documenting code)
  - Maintainability (clear intent for future developers)
- **Tests:** ✓ All passing (45/45)
- **Files Modified:**
  - src/services/auth/signup.service.ts (3 occurrences renamed)

### Refactorings Skipped

None

### Refactorings Failed

None

### Files Modified

- **src/routes/auth/signup.ts:** 62 lines → 35 lines (-27 lines, -43%)
- **src/services/auth/signup.service.ts:** 89 lines → 78 lines (-11 lines, -12%)
- **src/utils/validation.ts:** 0 lines → 35 lines (new file)
- **src/utils/password.ts:** 0 lines → 18 lines (new file)

**Total change:** 151 lines → 166 lines (+15 lines, but improved organization)

### Test Results

**Before refactoring:**
- Total tests: 45
- Passing: 45 (100%)
- Failing: 0
- Execution time: 4.2s
- Coverage: 85%

**After refactoring:**
- Total tests: 45
- Passing: 45 (100%)
- Failing: 0
- Execution time: 4.1s (-0.1s)
- Coverage: 87% (+2%)

**Regression check:** ✓ No behavioral changes detected

### Quality Impact

**Code Complexity:**
- Cyclomatic complexity: Average 8.5 → 6.2 (-27%)
- Cognitive complexity: Average 12.3 → 9.1 (-26%)

**Code Duplication:**
- Duplicated blocks: 3 → 0 (-100%)
- Duplication percentage: 15% → 3% (-80%)

**Maintainability:**
- Maintainability index: 67 → 78 (+16%)
- Lines per function: Average 28 → 22 (-21%)

**Test Coverage:**
- Statement coverage: 85% → 87% (+2%)
- Branch coverage: 78% → 82% (+4%)

### Quality Gate Impact

Refactoring improved code quality dimension score:
- Before: 72/100
- After: 84/100
- Improvement: +12 points

This improvement may positively impact final quality gate decision.

### Backups Created

Original files backed up to `.claude/quality/backups/task-auth-001/`:
- src/routes/auth/signup.ts.backup
- src/services/auth/signup.service.ts.backup

### Next Steps

1. Review refactored code: `git diff HEAD`
2. Verify alignment with project coding style
3. Commit changes: `git commit -m "refactor: improve auth code quality (automated)"`
4. Proceed with quality gate decision (quality-gate skill)

---
```

---

## Step 3 Output Template

Log creation confirmation:

```
✓ Refactoring log created: .claude/quality/refactoring-log.md
✓ Quality gate updated with refactoring results
✓ 3 refactorings applied, 0 failed, 0 skipped
✓ Backups created in .claude/quality/backups/task-auth-001/
```

---

## Step 4: Metrics Comparison Template

Before/after quality metrics:

```
Code Quality Metrics Comparison:

Lines of Code:
- Before: 151 lines
- After: 166 lines
- Change: +15 lines (+10%)
- Analysis: Increased due to new util files, but improved organization

Cyclomatic Complexity:
- Before: Average 8.5
- After: Average 6.2
- Change: -27% (improved)
- Analysis: Reduced nested logic through extraction

Cognitive Complexity:
- Before: Average 12.3
- After: Average 9.1
- Change: -26% (improved)
- Analysis: Simpler functions easier to understand

Code Duplication:
- Before: 15% duplicated
- After: 3% duplicated
- Change: -80% (improved)
- Analysis: Extracted common logic to utilities

Maintainability Index:
- Before: 67/100
- After: 78/100
- Change: +16% (improved)
- Analysis: Better separation of concerns

Test Coverage:
- Before: 85% statements, 78% branches
- After: 87% statements, 82% branches
- Change: +2% statements, +4% branches (improved)
- Analysis: Extracted code easier to test

Functions Per File:
- Before: Average 4.2 functions/file
- After: Average 3.8 functions/file
- Change: -10% (improved)
- Analysis: Better distribution across modules

Lines Per Function:
- Before: Average 28 lines/function
- After: Average 22 lines/function
- Change: -21% (improved)
- Analysis: Smaller, more focused functions
```

---

## Step 4: Final Summary Template

Comprehensive refactoring summary:

```markdown
## Automated Refactoring Complete

**Status:** ✓ Successful
**Refactorings Applied:** 3/3 (100% success rate)
**Duration:** 18 minutes
**Scope:** Moderate (P0 + P1)
**Tests:** All passing (45/45, 100%)

### Quality Improvements

- ✅ Code complexity reduced 27%
- ✅ Duplication reduced 80%
- ✅ Test coverage increased 2%
- ✅ Maintainability improved 16%
- ✅ All quality dimensions improved

### Files Modified

**Modified:**
- src/routes/auth/signup.ts (62 → 35 lines, -43%)
- src/services/auth/signup.service.ts (89 → 78 lines, -12%)

**Created:**
- src/utils/validation.ts (35 lines)
- src/utils/password.ts (18 lines)

### Refactorings Applied

1. ✓ Extract validation logic (P0, Medium Risk)
2. ✓ Extract hashPassword method (P1, Low Risk)
3. ✓ Rename existingUser variable (P1, Low Risk)

### Test Validation

- Unit tests: 45/45 passing ✓
- Integration tests: Not configured
- E2E tests: Not configured
- Coverage: 87% (+2%)
- Execution time: 4.1s

### Quality Gate Impact

Refactoring improved code quality score from **72/100 → 84/100**.

This improvement may positively influence the final quality gate decision.

### Next Steps

1. **Review refactored code:**
   ```bash
   git diff HEAD
   ```

2. **Verify alignment with coding style:**
   - Check naming conventions
   - Verify file organization
   - Confirm documentation updated

3. **Commit refactored code:**
   ```bash
   git add .
   git commit -m "refactor: improve auth code quality (automated)

   - Extract validation logic to utils/validation.ts
   - Extract password hashing to utils/password.ts
   - Rename existingUser for clarity

   Quality improvements:
   - Code complexity: -27%
   - Duplication: -80%
   - Test coverage: +2%
   - Maintainability: +16%

   All tests passing (45/45).
   "
   ```

4. **Proceed with quality gate:**
   ```bash
   Use quality-gate skill with task_file
   ```

### Detailed Documentation

- **Refactoring log:** `.claude/quality/refactoring-log.md`
- **Backups:** `.claude/quality/backups/task-auth-001/`
- **Quality gate:** `.claude/quality/gates/task-auth-001-gate.yaml`

### Safety Verification

✓ All tests passing
✓ No behavioral changes
✓ Backups created
✓ Changes logged
✓ Rollback available

---
```

---

## Task File Update Template

Append this section to task file's Quality Review:

```markdown
### Automated Refactoring

**Date:** 2025-10-29
**Scope:** Moderate (P0 + P1)
**Status:** ✓ Complete

**Refactorings Applied:** 3/3 (100%)
1. Extract validation logic (P0)
2. Extract hashPassword method (P1)
3. Rename existingUser variable (P1)

**Quality Impact:**
- Code complexity: -27%
- Duplication: -80%
- Test coverage: +2%
- Maintainability: +16%

**Test Validation:** All passing (45/45)

**Files Modified:**
- src/routes/auth/signup.ts
- src/services/auth/signup.service.ts
- src/utils/validation.ts (new)
- src/utils/password.ts (new)

**Detailed log:** `.claude/quality/refactoring-log.md`
```

---

## Error Templates

### Tests Failing Before Refactoring

```
✗ Refactoring halted: Prerequisites not met

Current tests are failing (3/45 failed):
- signup.service.test.ts: "should validate email format"
- signup.service.test.ts: "should hash password"
- signup.route.test.ts: "should return 400 for invalid input"

Cannot proceed with refactoring while tests are failing.

Action required:
1. Fix failing tests
2. Verify all tests pass
3. Re-run refactor-code skill
```

### Configuration Disallows Refactoring

```
✗ Refactoring not permitted by configuration

Configuration setting: quality.allowRefactoring: false

To enable refactoring:
1. Update .claude/config.yaml: quality.allowRefactoring: true
2. Or override with input: allow_refactoring=true

Proceeding to quality gate without refactoring.
```

### No Tests Available

```
✗ Refactoring halted: No tests found

Cannot safely refactor without test validation.

Action required:
1. Add tests for implementation code
2. Verify tests pass
3. Re-run refactor-code skill

Proceeding to quality gate without refactoring.
```

### Multiple Refactorings Failed

```
✗ Refactoring session failed: Multiple critical failures

Failed refactorings: 3/3 (100% failure rate)
1. Extract validation logic → Tests failed (2 failing)
2. Extract hashPassword method → Tests failed (1 failing)
3. Rename existingUser → Tests failed (4 failing)

All changes have been rolled back.

Analysis:
The codebase may have hidden dependencies or tight coupling that prevents safe refactoring.

Recommendations:
1. Review test failures in refactoring log
2. Fix underlying issues preventing refactoring
3. Consider manual refactoring with careful test verification

Proceeding to quality gate with current code (no refactoring applied).
```

### Partial Success

```
⚠ Refactoring partially complete: Some failures encountered

Success rate: 2/4 refactorings applied (50%)

Applied:
✓ 1. Rename existingUser variable
✓ 3. Extract method: validateEmail

Failed:
✗ 2. Extract validation logic (tests failed, rolled back)
✗ 4. Simplify conditional (tests failed, rolled back)

Quality improvement: Partial (8% improvement)

Recommendations:
1. Review failed refactorings in log
2. Address test failures
3. Re-attempt failed refactorings manually

Proceeding to quality gate with partial improvements.
```

---

## Aggressiveness Level Definitions

### Conservative

```yaml
scope: P0 only
risk: Low risk only
patterns:
  - Rename (variable, function, class)
  - Extract Variable
  - Inline Variable
  - Add/remove comments
safety: Highest
estimated_impact: 5-10% improvement
recommended_for: First-time refactoring, critical production code
```

### Moderate (Recommended)

```yaml
scope: P0 + P1
risk: Low to Medium risk
patterns:
  - All Conservative patterns
  - Extract Method
  - Extract Class
  - Simplify Conditionals
  - Remove Duplication
safety: High
estimated_impact: 15-30% improvement
recommended_for: Most projects, routine quality improvement
```

### Aggressive

```yaml
scope: P0 + P1 + P2
risk: All risk levels
patterns:
  - All Moderate patterns
  - Move Method/Class
  - Change Architecture
  - Large-scale refactorings
safety: Moderate (requires careful validation)
estimated_impact: 30-50% improvement
recommended_for: Major technical debt reduction, greenfield preparation
```

---

*Part of BMAD Enhanced Quality Suite - refactor-code skill*
