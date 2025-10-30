# Orchestration Guide

## Purpose

Guide for coordinating execution of 5 specialized quality skills with proper dependencies and sequencing.

---

## The 5 Quality Skills

### 1. risk-profile

**Purpose:** Assess implementation risks using P×I methodology

**Location:** `.claude/skills/quality/risk-profile.md`

**Inputs:**
- Task file
- Configuration

**Outputs:**
- Risk assessment report
- Risk scores (P×I 1-9 scale)
- Mitigation strategies
- Test scenario priorities

**Duration:** ~2-3 minutes

**Dependencies:** None (can run first)

---

### 2. test-design

**Purpose:** Design comprehensive test strategy with P0/P1/P2 priorities

**Location:** `.claude/skills/quality/test-design.md`

**Inputs:**
- Task file
- Configuration
- Risk profile (optional, enhances prioritization)

**Outputs:**
- Test design document
- Test scenarios (Given-When-Then)
- Mock strategies
- CI/CD integration plan

**Duration:** ~2-3 minutes

**Dependencies:**
- Optional: risk-profile (for risk-informed test prioritization)

---

### 3. trace-requirements

**Purpose:** Map AC → Implementation → Tests with gap analysis

**Location:** `.claude/skills/quality/trace-requirements.md`

**Inputs:**
- Task file
- Configuration
- Risk profile (optional, for gap severity)
- Test design (optional, for test mapping)

**Outputs:**
- Traceability matrix
- Coverage analysis
- Gap identification
- Recommendations

**Duration:** ~2-3 minutes

**Dependencies:**
- Optional: risk-profile, test-design (enhance gap assessment)

---

### 4. nfr-assess

**Purpose:** Assess non-functional requirements (6 categories)

**Location:** `.claude/skills/quality/nfr-assess.md`

**Inputs:**
- Task file
- Configuration
- Risk profile (optional, cross-reference)
- Traceability (optional, for evidence)
- Test design (optional, for validation)

**Outputs:**
- NFR scores (security, performance, reliability, maintainability, scalability, usability)
- Category assessments
- Gap identification

**Duration:** ~3-4 minutes

**Dependencies:**
- Optional: All previous assessments enhance NFR analysis

---

### 5. quality-gate

**Purpose:** Synthesize all assessments and make final gate decision

**Location:** `.claude/skills/quality/quality-gate.md`

**Inputs:**
- Task file
- Configuration
- Risk profile
- Test design
- Traceability
- NFR assessment

**Outputs:**
- Gate decision (PASS/CONCERNS/FAIL/WAIVED)
- Overall quality score
- Gate YAML (for CI/CD)
- Gate Markdown (human-readable)

**Duration:** ~1-2 minutes

**Dependencies:**
- **REQUIRED:** At minimum, traceability (critical for gate)
- **Recommended:** All 4 previous assessments for comprehensive gate

---

## Orchestration Sequence

### Recommended Order

```
1. risk-profile
   ↓
2. test-design (uses risk profile)
   ↓
3. trace-requirements (uses risk + test)
   ↓
4. nfr-assess (uses risk + trace + test)
   ↓
5. quality-gate (uses all assessments)
```

**Rationale:**
- Risk profile first: Identifies high-risk areas for all other assessments
- Test design second: Uses risks to prioritize tests
- Traceability third: Uses risk + test data to assess gap severity
- NFR fourth: Has full context from previous assessments
- Gate last: Synthesizes everything into final decision

---

### Dependency Graph

```
                    risk-profile
                         |
                  +------+------+
                  |             |
                  v             v
            test-design    (enhances all)
                  |             |
                  +------+------+
                         |
                         v
               trace-requirements
                         |
                  +------+------+
                  |             |
                  v             v
              nfr-assess   (uses all)
                         |
                         v
                   quality-gate
```

**Key Dependencies:**
- Solid arrows: Data flow / enhancement
- quality-gate: **Requires** traceability at minimum
- All others: **Enhanced by** but not blocked by dependencies

---

## Skill Invocation

### Pattern for Each Skill

```typescript
// 1. Announce execution
console.log(`Executing: {skill-name}.md`);
console.log(`Task: {task-id}`);

// 2. Prepare context
const context = {
  taskFile: taskFilePath,
  config: configData,
  riskProfile: riskProfileData,  // if available
  testDesign: testDesignData,    // if available
  // ...
};

// 3. Invoke skill
const result = await executeSkill(skillPath, context);

// 4. Check result status
if (result.status === 'error') {
  handleSkillError(skillName, result.error);
} else if (result.status === 'complete') {
  // Capture results for next skills
  captureResults(skillName, result);

  // Present summary to user
  presentSummary(skillName, result.summary);
}

// 5. Store output for downstream skills
storeAssessment(skillName, result);
```

---

### Example: Invoking risk-profile

```bash
# Step 1: Announce
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Executing: Risk Profile Assessment"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Task: task-007-user-auth"
echo "Duration: ~2-3 minutes"
echo ""

# Step 2: Prepare inputs
# (Read task file, config, etc.)

# Step 3: Execute skill
# Use .claude/skills/quality/risk-profile.md
# with task context

# Step 4: Capture output
RISK_FILE=".claude/quality/assessments/task-007-risk-20251029.md"
TOTAL_RISKS=12
CRITICAL_RISKS=1
HIGH_RISKS=3

# Step 5: Present summary
echo "✓ Risk Profile complete"
echo "✓ Total Risks: $TOTAL_RISKS ($CRITICAL_RISKS critical, $HIGH_RISKS high)"
echo "✓ Report: $RISK_FILE"
echo ""
```

---

### Example: Invoking test-design (with risk context)

```bash
# Step 1: Announce
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Executing: Test Design"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Task: task-007-user-auth"
echo "Risk Profile: $RISK_FILE (for risk-informed prioritization)"
echo ""

# Step 2: Prepare inputs (including risk profile)
# (Read task file, config, risk assessment)

# Step 3: Execute skill
# Use .claude/skills/quality/test-design.md
# with task + risk context

# Step 4: Capture output
TEST_FILE=".claude/quality/assessments/task-007-test-design-20251029.md"
TOTAL_TESTS=24
P0_TESTS=8

# Step 5: Present summary
echo "✓ Test Design complete"
echo "✓ Total Tests: $TOTAL_TESTS ($P0_TESTS P0)"
echo "✓ Report: $TEST_FILE"
echo ""
```

---

## Context Passing

### Progressive Context Building

Each skill adds to the context for downstream skills:

**After risk-profile:**
```yaml
context:
  riskProfile:
    file: .claude/quality/assessments/task-007-risk-20251029.md
    summary:
      totalRisks: 12
      criticalRisks: 1
      highRisks: 3
      topRisks:
        - Authentication bypass
        - SQL injection
        - Password storage
```

**After test-design:**
```yaml
context:
  riskProfile: { ... }
  testDesign:
    file: .claude/quality/assessments/task-007-test-design-20251029.md
    summary:
      totalTests: 24
      p0Tests: 8
      testLevels:
        unit: 12
        integration: 10
        e2e: 2
```

**After trace-requirements:**
```yaml
context:
  riskProfile: { ... }
  testDesign: { ... }
  traceability:
    file: .claude/quality/assessments/task-007-trace-20251029.md
    summary:
      traceabilityScore: 87.5%
      implementationCoverage: 83%
      testCoverage: 100%
      gaps:
        critical: 0
        high: 2
```

**After nfr-assess:**
```yaml
context:
  riskProfile: { ... }
  testDesign: { ... }
  traceability: { ... }
  nfr:
    file: .claude/quality/assessments/task-007-nfr-20251029.md
    summary:
      overallScore: 72%
      security: 70%
      performance: 80%
      reliability: 65%
```

**For quality-gate:**
```yaml
context:
  riskProfile: { ... }
  testDesign: { ... }
  traceability: { ... }
  nfr: { ... }
  # Gate synthesizes all of the above
```

---

## Parallel vs Sequential

### Can Run in Parallel

**Skills 1-4 can technically run in parallel** if you don't need enhanced analysis:

```
risk-profile ──┐
test-design ───┼──> (all complete) ──> quality-gate
trace-req ─────┤
nfr-assess ────┘
```

**Pros:**
- Faster (~3 minutes total vs ~10 minutes sequential)

**Cons:**
- Less accurate (no risk-informed test priorities)
- Less context for gap severity
- Missed cross-references

---

### Recommended Sequential (with batching)

**Batch 1:** risk-profile (foundational)
**Batch 2:** test-design + trace-requirements (parallel, both use risk)
**Batch 3:** nfr-assess (uses all previous)
**Batch 4:** quality-gate (synthesizes all)

```
risk-profile
     |
     v
[test-design, trace-requirements] (parallel)
     |
     v
nfr-assess
     |
     v
quality-gate
```

**Duration:** ~7-8 minutes (vs 10-11 sequential, vs 3-4 fully parallel)

**Accuracy:** High (most cross-references preserved)

---

## Progress Tracking

### Track Execution Status

```yaml
orchestrationState:
  taskId: task-007-user-auth
  startTime: 2025-10-29T10:00:00Z
  executionMode: full

  skills:
    riskProfile:
      status: complete
      startTime: 2025-10-29T10:00:00Z
      endTime: 2025-10-29T10:02:30Z
      duration: 150s
      file: .claude/quality/assessments/task-007-risk-20251029.md

    testDesign:
      status: in_progress
      startTime: 2025-10-29T10:02:35Z

    traceRequirements:
      status: pending

    nfrAssess:
      status: pending

    qualityGate:
      status: pending
```

---

### Present Progress Updates

After each skill completes:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Review Progress: 2/5 Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ 1. Risk Profile - Complete (2m 30s)
✓ 2. Test Design - Complete (2m 15s)
⏳ 3. Traceability - In Progress...
○ 4. NFR Assessment - Pending
○ 5. Quality Gate - Pending

Estimated time remaining: ~6 minutes
```

---

## Quick Reference

**Skill Order:**
1. risk-profile (foundation)
2. test-design (uses risk)
3. trace-requirements (uses risk + test)
4. nfr-assess (uses all)
5. quality-gate (synthesizes all)

**Duration:**
- Full sequential: ~10-11 minutes
- Batched: ~7-8 minutes
- Fully parallel: ~3-4 minutes (less accurate)

**Dependencies:**
- quality-gate **requires** traceability at minimum
- All others **enhanced by** but not blocked by dependencies

**Context Flow:**
- Each skill adds to context
- Downstream skills use accumulated context
- quality-gate synthesizes all

---

*Part of review-task skill - Quality Suite*
