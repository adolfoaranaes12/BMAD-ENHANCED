# Execution Modes Guide

## Purpose

Guide for the 3 execution modes: Full Review, Individual Skills, and Resume Partial Review.

---

## Mode 1: Full Review (Recommended)

**When to use:**
- Complete quality assessment needed
- Preparing for merge/deploy/release
- First-time quality review
- Comprehensive gate decision required

**What happens:**
- Executes all 5 skills in sequence
- Builds complete context progressively
- Generates all assessment reports
- Produces comprehensive gate decision

**Duration:** ~10-15 minutes

**Output:**
- 5 assessment reports (risk, test, trace, nfr, gate)
- Gate YAML (for CI/CD)
- Gate Markdown (human-readable)
- Task file updated with Quality Review summary

---

### Full Review Workflow

```
1. Load Config & Verify Task
   ↓
2. Execute risk-profile
   ↓
3. Execute test-design (with risk context)
   ↓
4. Execute trace-requirements (with risk + test context)
   ↓
5. Execute nfr-assess (with all context)
   ↓
6. Execute quality-gate (synthesize all)
   ↓
7. Update Task File
   ↓
8. Present Unified Summary
   ↓
9. Collect User Decision
```

---

### Example Full Review Session

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Starting Full Quality Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-007-user-auth
Mode: Full Review
Duration: ~10-15 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1/5] Executing: Risk Profile Assessment
✓ Complete (2m 30s)
✓ 12 risks identified (1 critical, 3 high)
✓ Report: .claude/quality/assessments/task-007-risk-20251029.md

[2/5] Executing: Test Design
✓ Complete (2m 15s)
✓ 24 tests designed (8 P0, 12 P1, 4 P2)
✓ Report: .claude/quality/assessments/task-007-test-design-20251029.md

[3/5] Executing: Requirements Traceability
✓ Complete (2m 45s)
✓ Traceability Score: 87.5%
✓ Report: .claude/quality/assessments/task-007-trace-20251029.md

[4/5] Executing: NFR Assessment
✓ Complete (3m 10s)
✓ Overall NFR Score: 72%
✓ Report: .claude/quality/assessments/task-007-nfr-20251029.md

[5/5] Executing: Quality Gate
✓ Complete (1m 45s)
✓ Gate Decision: CONCERNS
✓ Overall Score: 75.5%
✓ Reports: .claude/quality/gates/task-007-gate-20251029.*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quality Review Complete (12m 25s)

Next: Presenting unified summary...
```

---

## Mode 2: Individual Skills

**When to use:**
- Need only one quality dimension
- Quick feedback during development
- Re-assessing after fixes to specific area
- Building custom quality workflow

**What happens:**
- User selects specific skill(s) to run
- Only selected skills execute
- Context limited to selected skills
- Partial assessment (not comprehensive)

**Duration:** ~2-4 minutes per skill

**Output:**
- Only requested assessment report(s)
- No unified gate decision (unless gate selected)
- Task file not updated

---

### Individual Skill Selection

**Prompt user:**
```
Individual Skill Selection

Which skill(s) would you like to run?

1. Risk Profile only
   - Assess implementation risks (P×I methodology)
   - Duration: ~2-3 minutes

2. Test Design only
   - Design test strategy with priorities
   - Duration: ~2-3 minutes

3. Requirements Traceability only
   - Map AC → Implementation → Tests
   - Duration: ~2-3 minutes

4. NFR Assessment only
   - Assess non-functional requirements
   - Duration: ~3-4 minutes

5. Quality Gate only
   - Synthesize existing assessments into gate decision
   - Requires: At least traceability assessment exists
   - Duration: ~1-2 minutes

Select skill number(s) (comma-separated): [1-5]
```

---

### Example Individual Skill Session

**User selects:** Risk Profile only

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Executing: Risk Profile Assessment (Individual)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-007-user-auth
Mode: Individual Skill

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing: risk-profile.md
✓ Complete (2m 30s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Risk Profile Results:

Total Risks: 12
- Critical: 1 (Authentication bypass)
- High: 3 (SQL injection, XSS, Password storage)
- Medium: 5
- Low: 3

Mitigation Coverage: 3/4 high risks mitigated
Test Coverage: All P0 risks have test scenarios

Report: .claude/quality/assessments/task-007-risk-20251029.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Note: This is an individual assessment. For comprehensive
quality review, run Full Review mode.
```

---

### Running Quality Gate (Individual)

**Special case:** Quality Gate requires other assessments

**Check existing assessments:**
```bash
ls .claude/quality/assessments/task-007-*

# Found:
task-007-risk-20251029.md
task-007-test-design-20251029.md
task-007-trace-20251029.md
task-007-nfr-20251029.md
```

**If assessments exist:**
```
✓ Existing assessments found:
  - Risk Profile
  - Test Design
  - Traceability
  - NFR Assessment

Proceeding with Quality Gate synthesis...
```

**If no assessments:**
```
✗ Cannot run Quality Gate without assessments

Quality Gate requires at minimum:
- Requirements Traceability (critical)

Recommended:
- Risk Profile
- Test Design
- NFR Assessment

Options:
A) Run Full Review to generate all assessments
B) Run Traceability first, then Quality Gate
C) Cancel
```

---

## Mode 3: Resume Partial Review

**When to use:**
- Previous review was interrupted
- Want to skip completed assessments
- Re-running after fixing specific issues
- Updating specific dimensions

**What happens:**
- Detects existing assessment files
- Asks user which to keep vs re-run
- Skips kept assessments
- Runs only missing/re-run assessments
- Synthesizes into gate decision

**Duration:** Varies (only missing assessments)

**Output:**
- New assessment reports (only for re-run skills)
- Complete gate decision (uses existing + new assessments)
- Task file updated

---

### Resume Detection

**Check for existing assessments:**
```bash
# List all assessment files for task
ls .claude/quality/assessments/task-007-* 2>/dev/null

# Found:
task-007-risk-20251028.md
task-007-test-design-20251028.md
```

**Analyze existing:**
```yaml
existingAssessments:
  riskProfile:
    exists: true
    file: task-007-risk-20251028.md
    date: 2025-10-28
    age: 1 day

  testDesign:
    exists: true
    file: task-007-test-design-20251028.md
    date: 2025-10-28
    age: 1 day

  traceRequirements:
    exists: false

  nfrAssess:
    exists: false

  qualityGate:
    exists: false
```

---

### Resume Prompt

**Present to user:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Resume Partial Quality Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-007-user-auth

Existing Assessments Found:

1. ✓ Risk Profile (1 day old)
   File: task-007-risk-20251028.md
   Status: Keep or Re-run?

2. ✓ Test Design (1 day old)
   File: task-007-test-design-20251028.md
   Status: Keep or Re-run?

Missing Assessments:

3. ✗ Requirements Traceability
4. ✗ NFR Assessment
5. ✗ Quality Gate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Options:

A) Keep existing, run missing only (3, 4, 5)
   Duration: ~6-7 minutes

B) Re-run all (1, 2, 3, 4, 5)
   Duration: ~10-11 minutes (full review)

C) Custom selection (choose which to keep/re-run)

Which option? [Default: A]
```

---

### Custom Selection

**If user selects custom:**
```
Custom Assessment Selection

For each existing assessment, choose action:

1. Risk Profile (1 day old)
   K) Keep (use existing)
   R) Re-run (generate new)
   [Default: K]

2. Test Design (1 day old)
   K) Keep (use existing)
   R) Re-run (generate new)
   [Default: K]

Enter selections (e.g., "K,R" or "keep,rerun"): _
```

**User enters:** `K,R`

**Execution plan:**
```
Execution Plan:

✓ Keep: Risk Profile (existing)
⟳ Re-run: Test Design (generate new)
⟳ Run: Requirements Traceability (new)
⟳ Run: NFR Assessment (new)
⟳ Run: Quality Gate (synthesize all)

Estimated duration: ~8-9 minutes

Proceed? (Y/n)
```

---

### Example Resume Session

**Resume with keep existing:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Resuming Quality Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-007-user-auth
Mode: Resume (Keep existing, run missing)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1/5] Risk Profile
✓ Using existing (1 day old)
✓ File: .claude/quality/assessments/task-007-risk-20251028.md

[2/5] Test Design
✓ Using existing (1 day old)
✓ File: .claude/quality/assessments/task-007-test-design-20251028.md

[3/5] Executing: Requirements Traceability
✓ Complete (2m 45s)
✓ Traceability Score: 87.5%
✓ Report: .claude/quality/assessments/task-007-trace-20251029.md

[4/5] Executing: NFR Assessment
✓ Complete (3m 10s)
✓ Overall NFR Score: 72%
✓ Report: .claude/quality/assessments/task-007-nfr-20251029.md

[5/5] Executing: Quality Gate
✓ Complete (1m 45s)
✓ Gate Decision: CONCERNS
✓ Overall Score: 75.5%
✓ Reports: .claude/quality/gates/task-007-gate-20251029.*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quality Review Complete (7m 40s)

Used:
- 2 existing assessments (kept)
- 3 new assessments (generated)

Next: Presenting unified summary...
```

---

## Mode Selection Decision Tree

```
Start: Need Quality Review
  |
  ├─ Need comprehensive assessment?
  │  └─ YES → Full Review Mode
  │
  ├─ Need only specific dimension?
  │  └─ YES → Individual Skills Mode
  │
  ├─ Have partial assessments already?
  │  └─ YES → Resume Mode
  │
  └─ Unsure?
     └─ Default → Full Review Mode (most comprehensive)
```

---

## Mode Comparison

| Feature | Full Review | Individual | Resume |
|---------|-------------|------------|--------|
| Duration | 10-15 min | 2-4 min/skill | Varies |
| Comprehensiveness | Complete | Partial | Complete |
| Gate Decision | Yes | Optional | Yes |
| Context Building | Full | Limited | Full |
| Task File Update | Yes | No | Yes |
| Use Case | Production | Development | Re-assessment |

---

## Best Practices by Mode

### Full Review
- Use before merge/deploy
- First quality review
- Production readiness
- Compliance requirements

### Individual Skills
- During development (quick feedback)
- After fixing specific issue
- Building custom workflow
- Learning/experimentation

### Resume
- After interruption
- Re-assessment after fixes
- Updating stale assessments
- Iterative improvement

---

## Quick Reference

**Full Review:**
- All 5 skills in sequence
- ~10-15 minutes
- Comprehensive gate decision
- Updates task file

**Individual Skills:**
- Select specific skill(s)
- ~2-4 minutes per skill
- Partial assessment
- No task file update

**Resume:**
- Keep existing, run missing
- Variable duration
- Complete gate decision
- Updates task file

---

*Part of review-task skill - Quality Suite*
