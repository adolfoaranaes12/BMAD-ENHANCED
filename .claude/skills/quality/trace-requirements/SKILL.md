---
name: trace-requirements
description: Create comprehensive bidirectional requirements traceability matrix mapping acceptance criteria → implementation → tests with gap analysis, severity ratings, and coverage assessment for audit-ready documentation
version: 2.0
category: Quality
acceptance:
  forward_traceability: "All acceptance criteria mapped to implementation evidence with file paths, line ranges, function names, and code snippets demonstrating implementation"
  backward_traceability: "All tests mapped to acceptance criteria they validate with test files, scenarios, types (unit/integration/E2E), and priorities (P0/P1/P2)"
  gaps_identified: "Coverage gaps identified and classified by type (implementation/test), severity (CRITICAL/HIGH/MEDIUM/LOW), and priority (P0/P1/P2) with required actions"
  traceability_report_generated: "Complete traceability report generated with matrix, detailed entries, gap analysis, recommendations, and quality gate impact assessment"
telemetry:
  emit: "skill.trace-requirements.completed"
  track:
    - task_id
    - total_acceptance_criteria
    - implemented_count
    - partial_implementation_count
    - not_implemented_count
    - implementation_coverage_percentage
    - tested_count
    - partial_test_count
    - not_tested_count
    - test_coverage_percentage
    - total_gaps
    - critical_gaps_count
    - high_gaps_count
    - medium_gaps_count
    - low_gaps_count
    - traceability_score
    - risk_profile_available
    - test_design_available
---

# Requirements Traceability Analysis

Perform **bidirectional requirements traceability analysis** ensuring every acceptance criterion is implemented and tested. Creates audit-ready traceability matrix showing complete chain: Requirements → Implementation → Tests.

## Purpose

Create comprehensive traceability documentation that demonstrates:
- **Forward traceability:** AC → Implementation (with file/line evidence)
- **Backward traceability:** Tests → AC (with test scenario mapping)
- **Gap identification:** Missing implementation or test coverage
- **Severity assessment:** CRITICAL/HIGH/MEDIUM/LOW based on risk and impact
- **Coverage metrics:** Implementation coverage, test coverage, traceability score
- **Quality gate impact:** Prediction of gate status (PASS/CONCERNS/FAIL)

**Key Capabilities:**
- Evidence-based verification with file paths, line ranges, code snippets
- Integration with risk-profile (risk-informed gap severity)
- Integration with test-design (test-to-requirement mapping)
- Audit-ready documentation for compliance
- Actionable recommendations with effort estimates

## When to Use This Skill

**Best Used:**
- During implementation review to verify all requirements addressed
- Before quality gate to ensure completeness
- During audit preparation to demonstrate traceability
- After test-design to map tests to requirements
- When coverage gaps need identification and prioritization

**Integration Points:**
- Reads task specification for acceptance criteria
- Reads risk profile for risk-informed gap severity (optional)
- Reads test design for test-to-requirement mapping (optional)
- Reads actual implementation files for evidence
- Reads test files for test coverage verification

**Triggers:**
- User asks to "trace requirements", "check coverage", "verify AC implementation"
- Before quality gate (proactively suggest)
- During code review (verify completeness)

## Traceability Concepts

### Forward Traceability (AC → Implementation)
Maps each acceptance criterion to its implementation:

```
AC-1: User can signup with email and password
  ↓
Implementation Evidence:
  - File: src/routes/auth/signup.ts:15-42
  - Function: handleSignup()
  - Status: ✅ Implemented
  - Code Snippet: [5-10 lines showing implementation]
```

**Classification:**
- ✅ **Implemented:** Clear evidence found in code
- ⚠️ **Partial:** Some evidence but incomplete
- ❌ **Not Implemented:** No evidence found
- ❓ **Unclear:** Code exists but unclear if it satisfies AC

### Backward Traceability (Tests → AC)
Maps each test to the acceptance criteria it validates:

```
Test: "should create user with valid email and password"
  ↑
Validates: AC-1 (User can signup)
  - File: src/routes/auth/__tests__/signup.test.ts:12-24
  - Type: Integration, Priority: P0
  - Status: ✅ Tested
```

**Classification:**
- ✅ **Tested:** AC has at least one test validating it
- ⚠️ **Partial:** AC has tests but not all scenarios covered
- ❌ **Not Tested:** AC has no tests
- 🔄 **Indirect:** AC tested indirectly through E2E or other tests

### Gap Severity Ratings

**CRITICAL (Score 9):**
- Security requirement not implemented or tested
- Data integrity requirement missing
- Core functionality not implemented
- High-risk area (from risk profile) not tested

**HIGH (Score 6-8):**
- Important requirement not implemented
- Security test missing (but implementation exists)
- Performance requirement not validated
- P0 test missing

**MEDIUM (Score 3-5):**
- Minor requirement not implemented
- Edge case test missing
- P1 test missing
- Partial implementation without full test coverage

**LOW (Score 1-2):**
- Nice-to-have requirement missing
- P2 test missing
- Documentation-only gap

## SEQUENTIAL Skill Execution

**CRITICAL:** Do not proceed to next step until current step is complete

### Step 0: Load Configuration and Context

**Purpose:** Load project configuration, task specification, and related assessments

**Actions:**

1. **Load configuration from `.claude/config.yaml`:**
   - Extract quality settings (assessmentLocation)
   - Extract risk score threshold (for gap severity assessment)

2. **Get task file path from user:**
   - Example: `.claude/tasks/task-006-user-signup.md`
   - Verify file exists and is readable

3. **Read task specification:**
   - Extract task ID, title, type
   - Load objective and context
   - **Load Acceptance Criteria** (primary traceability source)
   - Load Implementation Record section (files created/modified)
   - Load Quality Review section (if exists)

4. **Load related assessments (optional but enhances analysis):**
   - Risk profile: `.claude/quality/assessments/{task-id}-risk-*.md` (for gap severity)
   - Test design: `.claude/quality/assessments/{task-id}-test-design-*.md` (for test mapping)

5. **Identify implementation files:**
   - From task spec "Implementation Record" section
   - Files created/modified during implementation
   - Line ranges for each change

6. **Prepare output:**
   - Output directory: `.claude/quality/assessments/`
   - Output file: `{task-id}-trace-{YYYYMMDD}.md`
   - Template: `.claude/templates/trace-requirements.md` (if exists)

**Output:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: {task-id} - {title}
✓ Acceptance Criteria: {count} criteria identified
✓ Related assessments: Risk profile [{found/not found}], Test design [{found/not found}]
✓ Implementation files: {count} files identified
✓ Output: {output-file}
```

**Halt Conditions:**
- Configuration file missing (cannot proceed)
- Task file not found or unreadable (cannot proceed)
- Task has no acceptance criteria (cannot proceed)
- Cannot create output directory (cannot proceed)

**Reference:** See [evidence-collection.md](references/evidence-collection.md) for evidence collection techniques

---

### Step 1: Build Forward Traceability Matrix (AC → Implementation)

**Purpose:** Map each acceptance criterion to its implementation evidence

**Actions:**

1. **For each acceptance criterion:**
   - Extract AC from task specification
   - Example: "AC-1: User can sign up with email and password"

2. **Search implementation files for evidence:**
   - Read each file from Implementation Record
   - Search for relevant code implementing the AC
   - Record file paths, line ranges, function/class names
   - Extract code snippets as evidence (5-10 lines context)

3. **Classify implementation status:**
   - ✅ **Implemented:** Clear evidence found in code
   - ⚠️ **Partial:** Some evidence but incomplete (e.g., validation missing)
   - ❌ **Not Implemented:** No evidence found
   - ❓ **Unclear:** Code exists but unclear if it satisfies AC

4. **Record evidence for each AC:**
   ```markdown
   AC-1: User can sign up with email and password
   Status: ✅ Implemented
   Evidence:
     - File: src/routes/auth/signup.ts:15-42
       Function: handleSignup()
       Description: Implements signup endpoint accepting email/password,
                    hashing password, creating user in database, sending
                    verification email
       Snippet:
         ```typescript
         export async function handleSignup(req: Request, res: Response) {
           const { email, password } = req.body;
           const hashedPassword = await bcrypt.hash(password, 10);
           const user = await prisma.user.create({
             data: { email, password: hashedPassword, emailVerified: false }
           });
           await sendVerificationEmail(user.email);
           return res.status(201).json({ user, token: generateJWT(user) });
         }
         ```
   ```

5. **Calculate implementation coverage:**
   ```
   Implementation Coverage = (Implemented + 0.5 × Partial) / Total AC × 100%
   ```

**Output:**
```
✓ Forward traceability analysis complete
✓ Total Acceptance Criteria: {count}
✓ Implemented: {count} ({percentage}%)
✓ Partial: {count} ({percentage}%)
✓ Not Implemented: {count} ({percentage}%)
✓ Unclear: {count} ({percentage}%)
✓ Implementation Coverage: {percentage}%
```

**Halt Conditions:**
- Cannot read implementation files (cannot gather evidence)
- More than 50% of ACs have "Unclear" status (ambiguous task, needs clarification)

**Reference:** See [traceability-matrix.md](references/traceability-matrix.md) for matrix building techniques

---

### Step 2: Build Backward Traceability Matrix (Tests → AC)

**Purpose:** Map each test to the acceptance criteria it validates

**Actions:**

1. **Identify test files:**
   - From test-design assessment (if available)
   - From Implementation Record (test files created)
   - From convention: `**/*.test.ts`, `**/*.spec.ts`, `**/__tests__/*`

2. **For each test file, extract test cases:**
   - Read test file
   - Extract test names from `it()`, `test()`, `describe()` blocks
   - Extract test scenarios (Given-When-Then if present)

   ```typescript
   describe('POST /api/auth/signup', () => {
     it('should create user with valid email and password', async () => {
       // Test case 1: Validates AC-1
     });

     it('should reject password shorter than 8 characters', async () => {
       // Test case 2: Validates AC-2
     });
   });
   ```

3. **Map tests to acceptance criteria:**
   - Analyze test name and assertions
   - Determine which AC(s) the test validates
   - A single test can validate multiple ACs
   - An AC typically has multiple tests (happy path, edge cases, errors)

   ```markdown
   Test: "should create user with valid email and password"
   Validates: AC-1 (User can sign up with email and password)
   File: src/routes/auth/__tests__/signup.test.ts:12-24
   Type: Integration, Priority: P0
   Scenario: Given valid inputs, When signup called, Then user created and JWT returned
   ```

4. **Classify test coverage:**
   - ✅ **Tested:** AC has at least one test validating it
   - ⚠️ **Partial:** AC has tests but not all scenarios covered (e.g., only happy path)
   - ❌ **Not Tested:** AC has no tests
   - 🔄 **Indirect:** AC tested indirectly through E2E or other tests

5. **Calculate test coverage:**
   ```
   Test Coverage = (Tested + 0.5 × Partial) / Total AC × 100%
   ```

**Output:**
```
✓ Backward traceability analysis complete
✓ Total Tests: {count}
✓ Tested ACs: {count} ({percentage}%)
✓ Partial Test Coverage: {count} ({percentage}%)
✓ Not Tested: {count} ({percentage}%)
✓ Test Coverage: {percentage}%
```

**Halt Conditions:**
- None (can proceed even if no tests found, but will generate gaps)

**Reference:** See [traceability-matrix.md](references/traceability-matrix.md) for test mapping techniques

---

### Step 3: Identify Coverage Gaps

**Purpose:** Identify and classify gaps in implementation and test coverage with severity ratings

**Actions:**

1. **Identify implementation gaps:**
   - ACs with status: Not Implemented, Partial, or Unclear
   - Document missing functionality
   - Estimate impact and effort

   ```markdown
   Implementation Gap 1:
   - AC-4: "System must rate-limit login attempts to 5 per minute"
   - Status: Not Implemented
   - Severity: HIGH (security requirement, high risk if missing)
   - Impact: Brute force attacks possible
   - Required Action: Implement rate limiting middleware
   - Effort: Medium (2-4 hours)
   - Priority: P0 (must fix before merge)
   ```

2. **Identify test gaps:**
   - ACs with test coverage: Not Tested or Partial
   - Document missing test scenarios
   - Identify missing edge cases, error cases, security tests

   ```markdown
   Test Gap 1:
   - AC-2: "Password must be at least 8 characters"
   - Implementation: ✅ Implemented (validation in src/validators/auth.ts:23)
   - Test Coverage: ⚠️ Partial
   - Missing Scenarios:
     * Edge case: Password exactly 8 characters (boundary test)
     * Error case: Password with 7 characters (validation error)
     * Edge case: Password with special characters (acceptance)
   - Severity: MEDIUM (core validation, but implementation exists)
   - Required Action: Add missing test scenarios
   - Effort: Small (30 min - 1 hour)
   - Priority: P1
   ```

3. **Classify gap severity:**
   Use risk profile (if available) to inform severity:

   - **CRITICAL (Score 9):**
     - Security requirement not implemented or tested
     - Data integrity requirement missing
     - Core functionality not implemented
     - High-risk area (from risk profile) not tested

   - **HIGH (Score 6-8):**
     - Important requirement not implemented
     - Security test missing (but implementation exists)
     - Performance requirement not validated
     - P0 test missing

   - **MEDIUM (Score 3-5):**
     - Minor requirement not implemented
     - Edge case test missing
     - P1 test missing
     - Partial implementation without full test coverage

   - **LOW (Score 1-2):**
     - Nice-to-have requirement missing
     - P2 test missing
     - Documentation-only gap

4. **Cross-reference with risk profile (if available):**
   - Gaps in high-risk areas → Increase severity
   - Gaps with existing mitigation → Decrease severity
   - Gaps without test coverage for high-risk area → CRITICAL

5. **Calculate gap metrics:**
   ```
   Total Gaps = Implementation Gaps + Test Gaps
   Critical Gaps = Gaps with severity CRITICAL
   High Gaps = Gaps with severity HIGH
   Medium Gaps = Gaps with severity MEDIUM
   Low Gaps = Gaps with severity LOW

   Gap Coverage = (Total AC - Total Gaps) / Total AC × 100%
   ```

**Output:**
```
⚠ Coverage gaps identified
⚠ Total Gaps: {count}
⚠ Critical: {count} (Security/core functionality issues)
⚠ High: {count} (Important requirements missing)
⚠ Medium: {count} (Minor gaps, edge cases)
⚠ Low: {count} (Nice-to-have items)
⚠ Gap Coverage: {percentage}%
```

**Halt Conditions:**
- More than 50% implementation gaps (incomplete implementation, not ready for traceability)

**Reference:** See [gap-analysis.md](references/gap-analysis.md) for gap classification and severity assessment

---

### Step 4: Create Traceability Matrix

**Purpose:** Build comprehensive bidirectional traceability matrix combining all data

**Actions:**

1. **Build full traceability matrix (table format):**
   ```markdown
   | AC | Requirement | Implementation | Tests | Gaps | Status |
   |----|-------------|----------------|-------|------|--------|
   | AC-1 | User can sign up with email and password | ✅ signup.ts:15-42 | ✅ 3 tests (P0) | None | ✅ Complete |
   | AC-2 | Password must be at least 8 characters | ✅ validators/auth.ts:23 | ⚠️ 1 test (missing edge cases) | GAP-2 (MEDIUM) | ⚠️ Partial |
   | AC-3 | Email must be validated | ✅ signup.ts:40, email.ts:12 | ✅ 2 tests (P1) | None | ✅ Complete |
   | AC-4 | Rate-limit login attempts | ❌ Not implemented | ❌ No tests | GAP-1 (HIGH) | ❌ Incomplete |
   ```

2. **Generate detailed entries for each AC:**
   ```markdown
   ## AC-1: User can sign up with email and password

   **Implementation Status:** ✅ Implemented

   **Implementation Evidence:**
   - **File:** src/routes/auth/signup.ts:15-42
   - **Function:** handleSignup()
   - **Description:** Implements signup endpoint accepting email/password,
                      hashing password, creating user, sending verification email
   - **Code Snippet:** [5-10 lines showing implementation]

   **Test Coverage:** ✅ Tested

   **Test Evidence:**
   1. **Test:** "should create user with valid email and password"
      - **File:** src/routes/auth/__tests__/signup.test.ts:12-24
      - **Type:** Integration, Priority: P0
      - **Scenario:** Given valid inputs, When signup, Then user created

   2. **Test:** "should return 400 for invalid email format"
      - **File:** src/routes/auth/__tests__/signup.test.ts:26-35
      - **Type:** Integration, Priority: P0
      - **Scenario:** Given invalid email, When signup, Then 400 error

   **Coverage Status:** ✅ Complete
   - Implementation: ✅ Complete
   - Tests: ✅ Complete (3 tests covering happy path, validation, errors)
   - Gaps: None
   ```

3. **Generate gap details:**
   ```markdown
   ## GAP-1: Rate Limiting Not Implemented (HIGH)

   **Type:** Implementation Gap
   **Severity:** HIGH (Score: 7)
   **Criterion:** AC-4 - "System must rate-limit login attempts to 5 per minute"

   **Impact:**
   - Brute force attacks possible on login endpoint
   - Potential account takeover vulnerability
   - No protection against credential stuffing

   **Related Risk:** Risk #3 from risk profile: "Brute force attacks" (Score: 8)

   **Required Action:**
   1. Implement rate limiting middleware using express-rate-limit
   2. Configure limit: 5 requests per minute per IP
   3. Apply to /api/auth/login endpoint
   4. Add tests for rate limiting behavior

   **Effort:** Medium (2-4 hours)
   **Priority:** P0 (Must fix before merge - security issue)
   ```

4. **Calculate overall traceability score:**
   ```
   Traceability Score = (
     (Implementation Coverage × 0.5) +
     (Test Coverage × 0.4) +
     (Gap Coverage × 0.1)
   )

   Example:
   - Implementation Coverage: 85%
   - Test Coverage: 80%
   - Gap Coverage: 90% (10% gaps)

   Traceability Score = (85 × 0.5) + (80 × 0.4) + (90 × 0.1)
                      = 42.5 + 32 + 9
                      = 83.5%
   ```

**Output:**
```
✓ Traceability matrix complete
✓ Total Entries: {count} acceptance criteria
✓ Complete: {count} ({percentage}%)
✓ Partial: {count} ({percentage}%)
✓ Incomplete: {count} ({percentage}%)
✓ Overall Traceability Score: {percentage}%
```

**Halt Conditions:**
- None (matrix can always be generated from available data)

**Reference:** See [traceability-matrix.md](references/traceability-matrix.md) for complete matrix examples

---

### Step 5: Generate Recommendations

**Purpose:** Provide actionable recommendations for closing gaps and improving traceability

**Actions:**

1. **Prioritize gaps:**
   Sort by:
   1. Severity (CRITICAL → HIGH → MEDIUM → LOW)
   2. Priority (P0 → P1 → P2)
   3. Effort (Small → Medium → Large)

2. **Generate action plan:**
   ```markdown
   ## Immediate Actions (Before Merge - P0)

   1. **[GAP-1] Implement Rate Limiting (HIGH)**
      - Impact: Security vulnerability
      - Effort: Medium (2-4 hours)
      - Action: Add rate limiting middleware to /api/auth/login
      - Tests: Add 3 tests for rate limit behavior

   2. **[GAP-4] Add Input Sanitization Tests (CRITICAL)**
      - Impact: XSS vulnerability untested
      - Effort: Small (1-2 hours)
      - Action: Implementation exists, add tests for XSS/SQL injection
      - Tests: Add 5 tests for malicious inputs

   ## Short-Term Actions (Before Release - P1)

   3. **[GAP-2] Complete Password Validation Tests (MEDIUM)**
      - Impact: Edge cases not validated
      - Effort: Small (30 min - 1 hour)
      - Action: Add boundary and edge case tests
      - Tests: Add 2 tests (exactly 8 chars, special characters)
   ```

3. **Quality gate impact assessment:**
   ```markdown
   ## Impact on Quality Gate

   **Current Status:** CONCERNS

   **Reasoning:**
   - 2 HIGH-severity gaps present security risks
   - 1 CRITICAL gap has untested security implementation
   - Implementation coverage at 85% (above threshold)
   - Test coverage at 80% (above threshold)
   - But gaps in critical security areas

   **To Achieve PASS:**
   1. Close all CRITICAL gaps (GAP-4)
   2. Close all HIGH gaps (GAP-1, GAP-3) OR provide waiver with mitigation
   3. Achieve implementation coverage ≥90%
   4. Achieve test coverage ≥85%

   **Estimated Effort to PASS:** 4-6 hours
   ```

4. **Best practices for future tasks:**
   ```markdown
   ## Traceability Best Practices

   **For Future Tasks:**
   1. Write tests alongside implementation (TDD approach)
   2. Reference AC IDs in commit messages ("Implements AC-1, AC-3")
   3. Reference AC IDs in test names ("test should satisfy AC-2")
   4. Update traceability as you implement
   5. Run trace-requirements before marking task as "Review"

   **For This Task:**
   1. Close P0 gaps before requesting review
   2. Document any waived gaps with rationale
   3. Update Implementation Record with gap closure evidence
   4. Re-run trace-requirements after closing gaps
   ```

**Output:**
```
✓ Recommendations generated
✓ P0 Actions: {count} (must complete before merge)
✓ P1 Actions: {count} (should complete before release)
✓ P2 Actions: {count} (future enhancements)
✓ Estimated Effort to Close P0 Gaps: {hours} hours
✓ Quality Gate Prediction: {PASS/CONCERNS/FAIL}
```

**Halt Conditions:**
- None (recommendations can always be generated from gaps)

**Reference:** See [gap-analysis.md](references/gap-analysis.md) for prioritization and action planning

---

### Step 6: Generate Traceability Report and Present Summary

**Purpose:** Create comprehensive traceability report and present concise summary to user

**Actions:**

1. **Load template (if exists):**
   - Read `.claude/templates/trace-requirements.md`
   - Use default structure if template missing

2. **Populate template variables:**
   - Metadata: task ID, title, date, assessor
   - Metrics: implementation coverage, test coverage, traceability score
   - Counts: total AC, total gaps, critical/high/medium/low gaps
   - Data: traceability matrix, detailed entries, gap details, recommendations

3. **Generate file path:**
   - Format: `.claude/quality/assessments/{taskId}-trace-{YYYYMMDD}.md`
   - Example: `.claude/quality/assessments/task-006-trace-20251029.md`
   - Create directory if needed

4. **Write traceability report:**
   - Complete report with all sections
   - Validate all template variables replaced
   - No placeholder text remaining

5. **Present concise summary to user:**
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Requirements Traceability Analysis Complete
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Task: task-006 - User Signup Implementation
   Date: 2025-10-29

   📊 Coverage Metrics:
   ├─ Implementation Coverage: 85% (5/6 AC implemented)
   ├─ Test Coverage: 80% (5/6 AC tested)
   ├─ Gap Coverage: 93% (4 gaps identified)
   └─ Overall Traceability Score: 83.5%

   ⚠️  Coverage Gaps Identified:
   ├─ CRITICAL: 1 gap (untested security implementation)
   ├─ HIGH: 2 gaps (missing security features)
   ├─ MEDIUM: 1 gap (incomplete test scenarios)
   └─ LOW: 0 gaps

   🎯 Quality Gate Impact: CONCERNS

   Reasoning:
   - 2 HIGH-severity gaps present security risks
   - 1 CRITICAL gap has untested security implementation
   - Implementation and test coverage above thresholds
   - But critical gaps in security areas require attention

   ✅ To Achieve PASS:
   1. Close GAP-4 (CRITICAL): Add XSS/injection tests [1-2h]
   2. Close GAP-1 (HIGH): Implement rate limiting [2-4h]
   3. Close GAP-3 (HIGH): Add session management [3-5h]

   Estimated effort: 6-11 hours

   📄 Full Report:
   .claude/quality/assessments/task-006-trace-20251029.md

   💡 Next Steps:
   1. Review detailed traceability matrix in report
   2. Prioritize P0 gaps (before merge)
   3. Close critical and high-severity gaps
   4. Re-run trace analysis after closing gaps
   5. Update task Implementation Record with gap closure

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

**Output:**
```
✓ Traceability report generated
✓ Output: .claude/quality/assessments/{task-id}-trace-{date}.md
✓ Report size: {lines} lines
✓ Summary presented to user
```

**Halt Conditions:**
- File write fails (cannot save traceability report)

**Reference:** See [traceability-examples.md](references/traceability-examples.md) for complete report examples

---

## Integration with Other Skills

### Integration with risk-profile

**Input from risk-profile:**
- Risk scores for each risk area
- High-risk areas (score ≥6) requiring extra test coverage
- Mitigation strategies that may be implemented

**How trace-requirements uses it:**
- Gaps in high-risk areas → Increase gap severity
- Missing tests for high-risk areas → CRITICAL severity
- Risk mitigation → Cross-reference with implementation evidence

**Example:**
```markdown
Risk Profile says:
  Risk #3: Brute force attacks (Score: 8, HIGH)
  Mitigation: Implement rate limiting

Traceability finds:
  AC-4: "Rate-limit login attempts" → Not Implemented

Gap Severity:
  Base: HIGH (security requirement)
  Risk amplification: +1 (high-risk from risk profile)
  Final: CRITICAL (Score: 9)
```

### Integration with test-design

**Input from test-design:**
- Test scenarios with priorities (P0/P1/P2)
- Test files and locations
- Mock strategies
- Expected test counts

**How trace-requirements uses it:**
- Maps test scenarios to acceptance criteria
- Validates all P0 tests have corresponding AC
- Identifies test scenarios not linked to any AC (over-testing)
- Validates coverage matches test design plan

**Example:**
```markdown
Test Design says:
  Scenario 1: Valid signup (P0, Integration)
  - Validates: User can sign up with email and password
  - File: src/routes/auth/__tests__/signup.test.ts

Traceability confirms:
  AC-1: "User can sign up..." → ✅ Tested
  - Test: "should create user with valid email and password"
  - File: src/routes/auth/__tests__/signup.test.ts:12-24
  - Priority: P0 ✓ (matches test design)
```

### Integration with quality-gate

**Output to quality-gate:**
- Traceability score (contributes to gate decision)
- Coverage gaps (may block gate if critical)
- Action items for closing gaps
- Evidence for requirements traceability dimension

**How quality-gate uses it:**
```markdown
Quality Gate Decision:
1. Check traceability score:
   - Score ≥95% → PASS
   - Score 80-94% → CONCERNS
   - Score <80% → FAIL

2. Check critical gaps:
   - 0 critical gaps → continue evaluation
   - 1+ critical gaps → CONCERNS (or FAIL if security)

3. Check overall coverage:
   - Implementation ≥90% AND Test ≥85% → PASS
   - Implementation ≥80% OR Test ≥70% → CONCERNS
   - Implementation <80% OR Test <70% → FAIL
```

## Best Practices

1. **Reference AC IDs in Code:**
   ```typescript
   // Implements AC-1: User signup with email and password
   export async function handleSignup(req: Request, res: Response) {
     // ...
   }
   ```

2. **Reference AC IDs in Commits:**
   ```bash
   git commit -m "feat: implement user signup (AC-1, AC-2, AC-3)"
   ```

3. **Reference AC IDs in Test Names:**
   ```typescript
   it('should satisfy AC-1: user can sign up with email and password', async () => {
     // ...
   });
   ```

4. **Run Before Code Review:**
   - Check traceability before marking task as "Review"
   - Close gaps before requesting review
   - Re-run trace-requirements after closing gaps

5. **Use for Audit Trail:**
   - Demonstrate requirements → implementation → test chain
   - Show evidence for compliance
   - Cross-reference with risk profile for risk coverage

## Configuration

### In `.claude/config.yaml`

```yaml
quality:
  # Quality assessment location
  assessmentLocation: ".claude/quality/assessments"

  # Risk score threshold for gap severity amplification
  riskScoreThreshold: 6  # Gaps in areas with risk ≥6 get higher severity

  # Traceability thresholds
  traceability:
    implementationCoverage: 90    # Minimum implementation coverage
    testCoverage: 85               # Minimum test coverage
    traceabilityScore: 80          # Minimum overall traceability score
```

### Template File

`.claude/templates/trace-requirements.md` - Template for traceability report output (optional)

---

**Version:** 2.0 (Refactored for skill-creator compliance and Minimal V2 architecture)
**Category:** Quality
**Depends On:** risk-profile (optional, enhances gap severity), test-design (optional, enhances test mapping)
**Used By:** quality-gate (uses traceability score and gaps for gate decision)
