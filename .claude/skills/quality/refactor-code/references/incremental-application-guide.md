# Incremental Application Guide

## Purpose

Step-by-step process for applying refactorings safely with test validation and automatic rollback.

---

## Core Principle

**One refactoring at a time, always validate with tests.**

Never apply multiple refactorings simultaneously. Never skip test validation. Never continue if tests fail without rollback.

---

## Application Workflow

### Phase 1: Preparation

**Before applying any refactorings:**

1. **Verify clean state:**
   ```bash
   git status  # Should be clean or only expected changes
   npm test    # Should show 100% passing
   ```

2. **Record baseline:**
   ```
   Test baseline:
   - Total tests: 45
   - Passing: 45
   - Failing: 0
   - Execution time: 4.2s
   - Coverage: 85%
   ```

3. **Create session backup:**
   ```bash
   git stash push -u -m "Pre-refactoring backup"
   # Or create a branch
   git checkout -b refactor-session-$(date +%Y%m%d-%H%M%S)
   ```

4. **Initialize progress tracking:**
   ```
   Refactoring Session Initialized:
   - Total selected: 5 refactorings
   - Aggressiveness: Moderate
   - Start time: 2025-10-29 10:00:00
   ```

---

### Phase 2: Iterative Application

For each refactoring in priority order:

---

#### Step 1: Announce Refactoring

**Output clear context:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Refactoring 1 of 5: Extract Validation Logic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Type: Extract Method
Priority: P0 (Critical)
Risk: Low
Files affected: 2
  - src/routes/auth/signup.ts (modify)
  - src/utils/validation.ts (create)

Rationale: Addresses high severity issue "Validation in route handler"

Expected outcome:
- Validation logic moved to dedicated utility
- Route handler simplified (30 lines → 10 lines)
- Improved testability and separation of concerns

Proceeding...
```

---

#### Step 2: Create Backup

**Save current state for rollback:**

**Option A: In-memory backup**
```typescript
// Read current file content
const originalContent = await readFile('src/routes/auth/signup.ts', 'utf-8');

// Store in backup map
const backups = new Map<string, string>();
backups.set('src/routes/auth/signup.ts', originalContent);
```

**Option B: Git staging**
```bash
# Stage current state
git add src/routes/auth/signup.ts
# Now we can restore with: git checkout -- src/routes/auth/signup.ts
```

**Option C: Temporary file**
```bash
cp src/routes/auth/signup.ts src/routes/auth/signup.ts.backup
```

---

#### Step 3: Apply Refactoring

**Execute the transformation:**

**Example: Extract Method**

```typescript
// Before
async function signup(req: Request, res: Response) {
  // 30 lines of validation
  if (!req.body.email) {
    return res.status(400).json({ error: 'Email required' });
  }
  if (!isValidEmail(req.body.email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }
  // ... more validation

  // Business logic
  const user = await createUser(req.body);
  res.status(201).json({ user });
}

// After transformation
// File 1: src/routes/auth/signup.ts
async function signup(req: Request, res: Response) {
  const validation = validateSignupRequest(req.body);
  if (!validation.valid) {
    return res.status(400).json(validation.errors);
  }

  const user = await createUser(req.body);
  res.status(201).json({ user });
}

// File 2: src/utils/validation.ts (new file)
export function validateSignupRequest(body: any): ValidationResult {
  if (!body.email) {
    return { valid: false, errors: { error: 'Email required' } };
  }
  if (!isValidEmail(body.email)) {
    return { valid: false, errors: { error: 'Invalid email' } };
  }
  // ... rest of validation
  return { valid: true };
}
```

**Write transformed files:**
```bash
# Write modified file
cat > src/routes/auth/signup.ts <<'EOF'
[new content]
EOF

# Write new file
cat > src/utils/validation.ts <<'EOF'
[extracted validation]
EOF
```

---

#### Step 4: Run Tests Immediately

**Execute test suite:**

```bash
npm test 2>&1 | tee test-output.txt
```

**Capture critical information:**
- Exit code (0 = pass, non-zero = fail)
- Test counts (total, passing, failing)
- Execution time
- Any error messages

**Example output:**
```
Test Suites: 8 passed, 8 total
Tests:       45 passed, 45 total
Snapshots:   0 total
Time:        4.1s
Ran all test suites.

Exit code: 0
```

---

#### Step 5: Evaluate Results

**If tests pass (exit code 0):**

```
✓ Refactoring 1 successful: Extract Validation Logic
✓ All tests passing: 45/45 (100%)
✓ Execution time: 4.1s (baseline: 4.2s, -0.1s)
✓ No behavioral changes detected
✓ Keeping changes

Progress: 1/5 complete
- Applied: 1
- Failed: 0
- Skipped: 0
```

**Actions:**
1. Keep changes (don't restore backup)
2. Clear backup (or commit to git)
3. Log success in refactoring log
4. Update progress counter
5. Proceed to next refactoring

---

**If tests fail (exit code non-zero):**

```
✗ Refactoring 1 failed: Extract Validation Logic
✗ Tests failing: 2/45 (95.6% pass rate)
✗ Execution time: 4.8s (baseline: 4.2s, +0.6s)

Failed tests:
  - auth/signup.test.ts › validates email format
  - auth/signup.test.ts › rejects duplicate emails

Error summary:
  TypeError: validateSignupRequest is not a function
  at signup (src/routes/auth/signup.ts:12:23)

Root cause: Missing import statement for validateSignupRequest

✗ Rolling back changes...
```

**Rollback actions:**

**Option A: Restore from in-memory backup**
```typescript
const originalContent = backups.get('src/routes/auth/signup.ts');
await writeFile('src/routes/auth/signup.ts', originalContent, 'utf-8');
```

**Option B: Restore from git**
```bash
git checkout -- src/routes/auth/signup.ts
rm src/utils/validation.ts  # Remove new file
```

**Option C: Restore from temp file**
```bash
mv src/routes/auth/signup.ts.backup src/routes/auth/signup.ts
rm src/utils/validation.ts
```

**Verify rollback:**
```bash
npm test  # Should pass again
```

**Log failure:**
```
✓ Rollback successful
✓ Tests passing again: 45/45 (100%)
✓ Code restored to pre-refactoring state

Failure logged: Extract Validation Logic
Reason: Missing import statement
Resolution: Skip this refactoring, needs manual review

Progress: 1/5 attempted
- Applied: 0
- Failed: 1
- Skipped: 0
```

**Decision:**
- For non-critical refactoring (P1, P2): Skip and continue to next
- For critical refactoring (P0): Halt session, require manual fix

---

#### Step 6: Update Progress

**After each refactoring (success or failure):**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Refactoring Progress Update
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Completed: 1/5 refactorings
- Applied successfully: 1
- Failed and rolled back: 0
- Skipped: 0

Success rate: 100% (1/1 attempted)
Time elapsed: 2 minutes
Estimated remaining: 8 minutes

Next: Refactoring 2 - Extract hashPassword method
```

**Update internal tracking:**
```typescript
const progress = {
  total: 5,
  completed: 1,
  applied: 1,
  failed: 0,
  skipped: 0,
  startTime: new Date('2025-10-29T10:00:00'),
  currentTime: new Date('2025-10-29T10:02:00')
};
```

---

### Phase 3: Completion

**After all refactorings attempted:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Refactoring Session Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary:
- Total attempted: 5
- Successfully applied: 4
- Failed and rolled back: 1
- Skipped: 0

Success rate: 80% (4/5)
Duration: 12 minutes

Applied refactorings:
1. ✓ Extract validation logic (P0, Low Risk)
2. ✓ Extract hashPassword method (P1, Low Risk)
3. ✓ Rename existingUser variable (P1, Low Risk)
4. ✓ Simplify password strength check (P1, Medium Risk)

Failed refactorings:
5. ✗ Extract email service (P1, Medium Risk)
   Reason: Missing environment variable for email config
   Resolution: Needs manual configuration before retry

Final test status:
- Tests passing: 45/45 (100%)
- Execution time: 4.0s (baseline: 4.2s, -0.2s improvement)
- Coverage: 87% (baseline: 85%, +2% improvement)

Files modified:
- src/routes/auth/signup.ts (modified)
- src/services/auth/signup.service.ts (modified)
- src/utils/validation.ts (created)
- src/utils/password.ts (created)

Next steps:
1. Review changes with git diff
2. Manually address failed refactoring
3. Commit changes: "refactor: improve auth code quality"
4. Proceed to quality gate
```

---

## Error Handling

### Common Failure Scenarios

#### Scenario 1: Import Error

**Symptom:**
```
TypeError: validateSignupRequest is not a function
```

**Cause:**
- Missing import statement
- Incorrect import path
- Export not defined

**Resolution:**
1. Rollback immediately
2. Mark as manual review needed
3. Log missing import in failure notes

---

#### Scenario 2: Type Error

**Symptom:**
```
TypeError: Cannot read property 'email' of undefined
```

**Cause:**
- Changed function signature
- Missing parameter
- Incorrect destructuring

**Resolution:**
1. Rollback immediately
2. Increase risk level (Medium → High)
3. Skip in automated session

---

#### Scenario 3: Test Timeout

**Symptom:**
```
Test suite failed to run
Timeout - Async callback was not invoked within the 5000ms timeout
```

**Cause:**
- Introduced async issue
- Missing await
- Broken promise chain

**Resolution:**
1. Rollback immediately
2. Mark as high risk
3. Requires manual investigation

---

#### Scenario 4: Changed Behavior

**Symptom:**
```
Expected: 400 Bad Request
Received: 500 Internal Server Error
```

**Cause:**
- Logic error in refactoring
- Edge case not handled
- Incorrect transformation

**Resolution:**
1. Rollback immediately
2. Mark as unsafe refactoring
3. Do not retry automatically

---

### Halt Conditions

**Immediately halt refactoring session if:**

1. **Multiple consecutive failures (>3)**
   ```
   Halting: 3 consecutive refactorings failed
   Reason: Pattern suggests systematic issue
   Action: Manual review required before continuing
   ```

2. **Critical (P0) refactoring fails**
   ```
   Halting: Critical refactoring failed
   Reason: P0 refactoring essential for quality gate
   Action: Manual fix required before quality approval
   ```

3. **Tests cannot be restored**
   ```
   Halting: Rollback failed
   Reason: Tests still failing after rollback attempt
   Action: Immediate manual intervention required
   ```

4. **Coverage drops significantly (>10%)**
   ```
   Halting: Coverage regression detected
   Reason: Coverage dropped from 85% to 72%
   Action: Investigate coverage loss before continuing
   ```

5. **User requests halt**
   ```
   Halting: User-requested stop
   Reason: User reviewing progress
   Action: Resume when user approves
   ```

---

## Safety Checklist

Before each refactoring:
- [ ] Backup created (in-memory, git, or temp file)
- [ ] Files to modify identified
- [ ] Tests currently passing
- [ ] Transformation logic validated

During refactoring:
- [ ] Single refactoring applied (not multiple)
- [ ] All affected files updated
- [ ] Imports/exports updated
- [ ] Tests run immediately

After test validation:
- [ ] Exit code checked (0 = pass)
- [ ] Test counts verified (no new failures)
- [ ] Execution time reasonable (<2x baseline)
- [ ] Decision made (keep or rollback)

After rollback (if needed):
- [ ] Original files restored
- [ ] New files removed
- [ ] Tests passing again
- [ ] Failure logged

---

## Performance Optimization

### Parallel Testing

**Don't run full suite for small changes:**

```bash
# Instead of:
npm test  # Runs all 500 tests (60 seconds)

# Run only affected tests:
npm test -- --findRelatedTests src/routes/auth/signup.ts  # 10 tests (5 seconds)
```

**Only run full suite:**
- After all refactorings applied
- Before final summary
- If fast tests not available

---

### Incremental Commits

**For long sessions with many refactorings:**

```bash
# After every 3 successful refactorings:
git add .
git commit -m "refactor: apply batch 1 of 3 (extract methods)"

# Benefits:
# - Smaller rollback scope if issues found later
# - Can resume if session interrupted
# - Clearer history for review
```

---

## Quick Reference

**Application Flow:**
1. Preparation → Verify clean state, record baseline
2. For each refactoring:
   - Announce → Clear context
   - Backup → Save current state
   - Apply → Transform code
   - Test → Run suite immediately
   - Evaluate → Keep or rollback
   - Update → Progress tracking
3. Completion → Final summary, next steps

**On test failure:**
1. Rollback immediately (restore from backup)
2. Verify tests pass again
3. Log failure with reason
4. Decide: skip (P1/P2) or halt (P0)
5. Continue to next refactoring

**Halt conditions:**
- 3+ consecutive failures
- P0 refactoring fails
- Rollback fails
- Coverage drops >10%
- User requests

---

*Part of refactor-code skill - Quality Suite*
