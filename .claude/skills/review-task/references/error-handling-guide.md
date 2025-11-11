# Error Handling & Graceful Degradation Guide

## Purpose

Guide for handling skill execution failures with graceful degradation and fallback strategies.

---

## Skill Failure Impact Analysis

### risk-profile Failure

**Impact:** Moderate
- Gate decision lacks risk context
- Test priorities less informed
- Gap severity assessments limited
- NFR cross-reference missing

**Can proceed?** YES (with degraded accuracy)

**Fallback strategies:**
1. Use implementation file analysis for basic risk identification
2. Rely on test design for basic test priorities
3. Note in gate report: "Risk assessment unavailable"

**Example fallback:**
```yaml
riskManagement:
  status: N/A
  fallback: basic-implementation-analysis
  confidence: LOW
  note: "Risk profile assessment failed. Using basic file analysis instead."
  riskScore: 50%  # Conservative default
  recommendation: "Re-run risk profile before production deployment"
```

---

### test-design Failure

**Impact:** Moderate
- Gate decision lacks test strategy context
- Test coverage metrics incomplete
- Mock strategies missing

**Can proceed?** YES (use traceability test data as fallback)

**Fallback strategies:**
1. Use traceability's test data (tests → AC mapping)
2. Extract test counts from test files directly
3. Note in gate report: "Test design unavailable, using traceability data"

**Example fallback:**
```yaml
testCoverage:
  status: DEGRADED
  fallback: traceability-test-data
  confidence: MEDIUM
  note: "Test design assessment failed. Using test data from traceability."
  metrics:
    totalTests: {from traceability}
    p0Tests: {inferred from test names}
    testsPassing: {from test file}
  recommendation: "Re-run test design for comprehensive test strategy"
```

---

### trace-requirements Failure

**Impact:** **CRITICAL**
- Gate decision requires traceability for AC coverage
- Cannot assess requirements completeness
- Cannot map tests to requirements
- Implementation coverage unknown

**Can proceed?** **NO** - Must fix and re-run

**Why critical:**
- Traceability is foundation for quality gate
- Without it, cannot verify AC implementation
- Cannot determine test coverage
- Gate decision would be unreliable

**Action:**
```
✗ Requirements Traceability assessment failed

CRITICAL: Cannot proceed with quality gate

Traceability is required for:
- Acceptance criteria coverage verification
- Test-to-requirement mapping
- Implementation completeness assessment
- Gap identification

Error: {error_details}

Actions:
1. Review error details above
2. Fix underlying issue (missing files, invalid format, etc.)
3. Re-run: trace-requirements skill
4. Then continue with quality review

Cannot generate gate decision without traceability.
Quality review HALTED.
```

---

### nfr-assess Failure

**Impact:** High
- Gate decision lacks NFR scores
- Security assessment missing
- Performance assessment missing
- No NFR-specific gaps identified

**Can proceed?** YES (use implementation quality as proxy)

**Fallback strategies:**
1. Use basic code quality checks
2. Infer security from risk profile
3. Note in gate report: "NFR assessment unavailable"
4. Lower overall gate confidence

**Example fallback:**
```yaml
nfr:
  status: N/A
  fallback: implementation-quality-proxy
  confidence: LOW
  note: "NFR assessment failed. Using implementation quality as proxy."
  overallScore: 60%  # Conservative default from impl quality
  categories:
    security: N/A (check risk profile)
    performance: N/A
    reliability: {from impl quality}
    maintainability: {from impl quality}
  recommendation: "Re-run NFR assessment before production deployment"
```

---

### quality-gate Failure

**Impact:** **CRITICAL**
- Cannot make gate decision
- No synthesis of assessments
- No final recommendation
- Review cannot complete

**Can proceed?** **NO** - Must fix and re-run

**Why critical:**
- Gate is the final output of review
- Without it, no actionable decision
- Cannot update task file
- Cannot provide recommendation

**Action:**
```
✗ Quality Gate synthesis failed

CRITICAL: Cannot complete quality review

Quality Gate is the final synthesis step.
Without it, review has no actionable output.

Error: {error_details}

Actions:
1. Review error details above
2. Verify all input assessments are valid
3. Check gate skill configuration
4. Fix underlying issue
5. Re-run: quality-gate skill

Quality review HALTED.
```

---

## Error Detection

### During Skill Execution

**Monitor for:**
1. Non-zero exit codes
2. Missing output files
3. Incomplete data in output
4. Error messages in skill output
5. Timeouts (skill taking >10 minutes)

**Example monitoring:**
```typescript
async function executeSkill(skillPath: string, context: any) {
  const startTime = Date.now();
  const timeout = 10 * 60 * 1000; // 10 minutes

  try {
    // Execute skill
    const result = await runSkill(skillPath, context, timeout);

    // Check exit code
    if (result.exitCode !== 0) {
      return {
        status: 'error',
        error: `Skill failed with exit code ${result.exitCode}`,
        details: result.stderr
      };
    }

    // Check output file exists
    const outputFile = result.outputFile;
    if (!fs.existsSync(outputFile)) {
      return {
        status: 'error',
        error: `Output file not created: ${outputFile}`,
        details: 'Skill may have failed silently'
      };
    }

    // Check output completeness
    const output = await parseSkillOutput(outputFile);
    if (!isComplete(output)) {
      return {
        status: 'error',
        error: 'Output incomplete or malformed',
        details: `Missing required fields: ${getMissingFields(output)}`
      };
    }

    // Success
    return {
      status: 'complete',
      output: output,
      duration: Date.now() - startTime
    };

  } catch (error) {
    return {
      status: 'error',
      error: error.message,
      details: error.stack
    };
  }
}
```

---

## Error Handling Flow

### Decision Tree

```
Skill execution fails
  |
  ├─ Is skill critical? (trace-requirements or quality-gate)
  │  ├─ YES → HALT
  │  │    └─ Present error to user
  │  │    └─ Request fix and re-run
  │  │    └─ Cannot proceed
  │  │
  │  └─ NO → DEGRADE
  │       └─ Apply fallback strategy
  │       └─ Lower confidence
  │       └─ Note in gate report
  │       └─ Continue with next skill
  │
  └─ Fallback successful?
     ├─ YES → Continue
     │    └─ Mark dimension as degraded
     │    └─ Proceed to next skill
     │
     └─ NO → Prompt user
          └─ Option A: Skip skill and continue
          └─ Option B: Fix and re-run skill
          └─ Option C: Abort review
```

---

### Example Error Handling

**Non-critical skill fails (risk-profile):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  Skill Execution Error
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Skill: risk-profile
Error: Failed to analyze implementation files

Details:
- Could not read file: src/services/auth.service.ts
- Error: ENOENT: no such file or directory

Impact: MODERATE
- Gate decision will lack risk context
- Test priorities less informed
- Can proceed with fallback

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Options:

A) Continue with fallback (basic risk analysis)
   - Will use implementation file listing for basic risks
   - Gate confidence will be marked as MEDIUM
   - Recommended: Re-run risk profile after fixing file issue

B) Fix issue and re-run risk-profile
   - Review error above
   - Fix missing file or path issue
   - Re-run risk-profile skill
   - Then continue with review

C) Abort review
   - Stop quality review
   - Fix issues
   - Start fresh review later

Which option? [Default: A]
```

**Critical skill fails (trace-requirements):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ CRITICAL: Skill Execution Failed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Skill: trace-requirements
Error: Cannot parse acceptance criteria from task file

Details:
- Task file: .claude/tasks/task-007-user-auth.md
- Error: Acceptance Criteria section not found or malformed
- Expected format: ## Acceptance Criteria with numbered list

Impact: CRITICAL
- Traceability is REQUIRED for quality gate
- Cannot assess AC coverage without it
- Gate decision would be unreliable
- CANNOT PROCEED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Required Actions:

1. Review task file format
2. Ensure "## Acceptance Criteria" section exists
3. Ensure criteria are numbered list (1. criterion, 2. criterion...)
4. Fix task file format
5. Re-run: trace-requirements skill
6. Then continue with quality review

Quality review HALTED.

Would you like to:
A) View task file to inspect issue
B) Get guidance on correct AC format
C) Abort review (fix manually later)

Your choice: _
```

---

## Graceful Degradation

### Minimum Viable Gate

**When multiple non-critical skills fail, gate can still proceed with:**

**Minimum requirements:**
- ✅ trace-requirements (critical)
- ❌ risk-profile (degraded)
- ❌ test-design (degraded)
- ❌ nfr-assess (degraded)

**Resulting gate:**
```yaml
qualityGate:
  decision:
    status: CONCERNS
    confidence: LOW
    reasoning: |
      Limited assessment data available.
      Only traceability successfully assessed.
      Gate decision based primarily on requirements coverage.

  dimensions:
    riskManagement:
      status: N/A
      note: "Assessment failed, fallback used"

    testCoverage:
      status: DEGRADED
      note: "Test design failed, using traceability test data"
      score: {from traceability}

    traceability:
      status: COMPLETE
      score: {from trace-requirements}

    nfr:
      status: N/A
      note: "Assessment failed, implementation quality used as proxy"

    implementationQuality:
      status: COMPLETE
      score: {from task file}

    compliance:
      status: DEGRADED
      note: "Limited compliance checks due to missing assessments"

  overallScore: 60%  # Conservative, limited data
  canProceed: false  # Requires more assessments
  blockers:
    - "Risk assessment unavailable"
    - "NFR assessment unavailable"
    - "Confidence too low for merge decision"

  recommendation: |
    CANNOT APPROVE: Insufficient assessment data

    Required actions:
    1. Fix skill execution issues
    2. Re-run failed assessments (risk, test, nfr)
    3. Re-run quality gate with complete data
    4. Only then can make reliable merge decision

    Do not proceed with merge until complete assessment available.
```

---

## Recovery Strategies

### Strategy 1: Retry with Exponential Backoff

**For transient errors:**
```typescript
async function executeWithRetry(
  skillPath: string,
  context: any,
  maxRetries: number = 3
) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const result = await executeSkill(skillPath, context);

      if (result.status === 'complete') {
        return result;
      }

      // If error is non-transient, don't retry
      if (isNonTransient(result.error)) {
        return result;
      }

      // Wait before retry (exponential backoff)
      const delay = Math.pow(2, attempt) * 1000; // 2s, 4s, 8s
      console.log(`Retry ${attempt}/${maxRetries} in ${delay}ms...`);
      await sleep(delay);

    } catch (error) {
      if (attempt === maxRetries) {
        return {
          status: 'error',
          error: `Failed after ${maxRetries} attempts: ${error.message}`
        };
      }
    }
  }
}
```

---

### Strategy 2: Partial Re-run

**Re-run only failed skills:**
```typescript
async function recoverFailedSkills(failedSkills: string[]) {
  console.log(`Re-running ${failedSkills.length} failed skills...`);

  const results = [];

  for (const skillName of failedSkills) {
    console.log(`\nRetrying: ${skillName}`);

    const result = await executeSkill(skillName, context);

    if (result.status === 'complete') {
      console.log(`✓ ${skillName} succeeded on retry`);
      results.push({ skill: skillName, status: 'recovered' });
    } else {
      console.log(`✗ ${skillName} still failing`);
      results.push({ skill: skillName, status: 'failed', error: result.error });
    }
  }

  return results;
}
```

---

### Strategy 3: User-Guided Recovery

**Prompt user for guidance:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recovery Options
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2 skills failed:
- risk-profile (Error: File not found)
- nfr-assess (Error: Parse error)

What would you like to do?

A) Auto-retry failed skills (with exponential backoff)
   - Will retry up to 3 times
   - 2s, 4s, 8s delays between retries

B) Skip failed skills and continue with fallbacks
   - Will use fallback strategies for missing data
   - Gate confidence will be marked as LOW/MEDIUM
   - You can re-run later

C) Fix issues manually and resume
   - Review errors above
   - Fix underlying issues
   - Resume review from where it left off

D) Abort review
   - Stop quality review
   - Start fresh review after fixing issues

Your choice: _
```

---

## Error Reporting

### Detailed Error Report

**Include in gate report:**
```yaml
errors:
  - skill: risk-profile
    timestamp: 2025-10-29T10:02:45Z
    error: "File not found: src/services/auth.service.ts"
    impact: MODERATE
    fallback: basic-implementation-analysis
    recoverable: true
    recommendation: "Fix file path and re-run risk profile"

  - skill: nfr-assess
    timestamp: 2025-10-29T10:08:15Z
    error: "Parse error in task file: Missing NFR section"
    impact: HIGH
    fallback: implementation-quality-proxy
    recoverable: true
    recommendation: "Add NFR section to task file and re-run NFR assessment"

assessmentQuality:
  overallConfidence: MEDIUM
  dataCompleteness: 60%
  fallbacksUsed: 2
  criticalDataMissing: false
  recommendation: "Re-run failed assessments before production deployment"
```

**Include in task file Quality Review:**
```markdown
### Assessment Quality

**Confidence:** MEDIUM (some assessments failed)
**Data Completeness:** 60% (2 of 5 assessments used fallbacks)

**Failed Assessments:**
- Risk Profile: File not found error (fallback: basic analysis)
- NFR Assessment: Parse error (fallback: implementation quality proxy)

**Recommendation:**
Re-run failed assessments before production deployment to ensure comprehensive quality review.

**Recovery Steps:**
1. Fix file path issue (src/services/auth.service.ts)
2. Add NFR section to task file
3. Re-run failed skills: risk-profile, nfr-assess
4. Re-run quality-gate to update decision
```

---

## Quick Reference

**Critical Skills (cannot proceed if fail):**
- trace-requirements (required for gate)
- quality-gate (final output)

**Non-Critical Skills (can degrade):**
- risk-profile (fallback: basic analysis)
- test-design (fallback: traceability test data)
- nfr-assess (fallback: implementation quality proxy)

**Error Handling Flow:**
1. Detect error during execution
2. Determine criticality
3. If critical: HALT, prompt user to fix
4. If non-critical: Apply fallback, continue
5. Report errors in gate report
6. Offer recovery options

**Graceful Degradation:**
- Use fallback strategies
- Lower confidence scores
- Note missing data
- Provide recovery recommendations
- Still generate gate decision (with caveats)

---

*Part of review-task skill - Quality Suite*
