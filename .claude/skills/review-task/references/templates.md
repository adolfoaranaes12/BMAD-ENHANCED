# Quality Review Templates

This file contains output templates, YAML examples, and formatting standards for the review-task orchestration skill.

---

## Step Output Templates

### Step 0: Configuration Output

```
✓ Configuration loaded
✓ Task: {task-id} - {title}
✓ Task status: Review (ready for quality assessment)
✓ Implementation complete: {tasks_complete}/{total_tasks}
✓ Execution mode: {Full Review | Individual Skills | Resume}
```

---

### Step 1: Risk Profile Output

**Console Output:**
```
✓ Risk Profile complete
✓ Total Risks: {total} ({critical} critical, {high} high)
✓ Mitigation Coverage: {mitigated}/{high_risk_items}
✓ Report: {file_path}
```

**Captured Data:**
```yaml
riskProfile:
  status: complete
  file: .claude/quality/assessments/{task-id}-risk-{date}.md
  summary:
    totalRisks: 12
    criticalRisks: 1
    highRisks: 3
    highRisksMitigated: 2/4
```

---

### Step 2: Test Design Output

**Console Output:**
```
✓ Test Design complete
✓ Total Tests: {total} ({p0} P0, {p1} P1, {p2} P2)
✓ Test Levels: {unit} unit, {integration} integration, {e2e} E2E
✓ Report: {file_path}
```

**Captured Data:**
```yaml
testDesign:
  status: complete
  file: .claude/quality/assessments/{task-id}-test-design-{date}.md
  summary:
    totalTests: 24
    p0Tests: 8
    p1Tests: 12
    p2Tests: 4
```

---

### Step 3: Traceability Output

**Console Output:**
```
✓ Requirements Traceability complete
✓ Traceability Score: {score}%
✓ Implementation Coverage: {impl_coverage}%
✓ Test Coverage: {test_coverage}%
✓ Gaps: {total_gaps} ({critical} critical, {high} high)
✓ Report: {file_path}
```

**Captured Data:**
```yaml
traceability:
  status: complete
  file: .claude/quality/assessments/{task-id}-trace-{date}.md
  summary:
    totalAC: 6
    implemented: 5
    tested: 6
    implementationCoverage: 83%
    testCoverage: 100%
    traceabilityScore: 87.5%
```

---

### Step 4: NFR Assessment Output

**Console Output:**
```
✓ NFR Assessment complete
✓ Overall NFR Score: {score}%
✓ Security: {security}%, Reliability: {reliability}%
✓ Critical NFR Gaps: {critical_gaps}
✓ Report: {file_path}
```

**Captured Data:**
```yaml
nfr:
  status: complete
  file: .claude/quality/assessments/{task-id}-nfr-{date}.md
  summary:
    overallScore: 72%
    categories:
      security: 70%
      performance: 80%
      reliability: 65%
      maintainability: 75%
      scalability: 70%
      usability: 70%
```

---

### Step 5: Quality Gate Output

**Console Output:**
```
✓ Quality Gate complete
✓ Gate Decision: {PASS/CONCERNS/FAIL/WAIVED}
✓ Overall Quality Score: {score}%
✓ Can Proceed: {YES/NO}
✓ Blockers: {count}
✓ Action Items: {count} ({p0} P0, {p1} P1)
✓ Reports: {yaml-file}, {md-file}
```

**Captured Data:**
```yaml
qualityGate:
  status: complete
  yamlFile: .claude/quality/gates/{task-id}-gate-{date}.yaml
  mdFile: .claude/quality/gates/{task-id}-gate-{date}.md
  decision:
    status: CONCERNS
    overallScore: 75.5%
    canProceed: true
    blockers: []
    actionItems: 3
```

---

### Step 6: Task File Update Output

```
✓ Task file Quality Review section updated
✓ Task file: {task-file-path}
```

---

## Task File Update Template

When updating task file with quality review results:

```markdown
## Quality Review

### Review Date
{YYYYMMDD}

### Reviewer
review-task-v2.0 (claude-sonnet-4-5)

### Quality Gate Decision
{PASS | CONCERNS | FAIL | WAIVED}

### Overall Quality Score
{score}%

### Assessment Reports
- Risk Profile: `.claude/quality/assessments/{task-id}-risk-{date}.md`
- Test Design: `.claude/quality/assessments/{task-id}-test-design-{date}.md`
- Traceability: `.claude/quality/assessments/{task-id}-trace-{date}.md`
- NFR Assessment: `.claude/quality/assessments/{task-id}-nfr-{date}.md`
- Quality Gate: `.claude/quality/gates/{task-id}-gate-{date}.md` (⭐ Start here)

### Summary
{Brief 2-3 sentence summary from gate decision}

### Key Findings
{Top 3-5 findings from gate report}

### Action Items
{P0 action items, if any}

### Recommendation
{Recommendation from gate decision: approve/fix/waive}
```

---

## Unified Summary Template (Step 7)

Present this comprehensive summary after all assessments complete:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Comprehensive Quality Review Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id} - {title}
Date: {YYYYMMDD}
Duration: {duration}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Quality Gate Decision: {STATUS}

**Overall Quality Score:** {score}%
**Can Proceed:** {YES/NO/CONDITIONAL}
**Blockers:** {count}
**Action Items:** {count} ({p0} P0, {p1} P1, {p2} P2)

{Brief rationale from gate decision}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📊 Quality Dimension Scores

1. Risk Management: {risk_score}%
2. Test Coverage: {test_score}%
3. Requirements Traceability: {trace_score}%
4. Non-Functional Requirements: {nfr_score}%
5. Implementation Quality: {impl_score}%
6. Compliance: {compliance_score}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🚨 Critical Findings

{List of critical/high findings from all assessments}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✅ Action Items

### P0 (Must Complete Before Merge):
{P0 action items from gate}

### P1 (Should Complete Before Release):
{P1 action items from gate}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📄 Generated Reports

1. ⭐ Quality Gate (START HERE): {gate-md-file}
2. Risk Profile: {risk-file}
3. Test Design: {test-file}
4. Traceability: {trace-file}
5. NFR Assessment: {nfr-file}
6. Gate YAML (CI/CD): {gate-yaml-file}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Next Steps

What would you like to do?

A) Accept decision and proceed with merge
B) Review detailed reports first
C) Address action items now
D) Request waiver for specific gaps
E) Re-run specific assessment
```

---

## User Decision Response Templates

### A) Accept and Proceed

```
✓ Gate decision accepted

**Next Steps:**
1. Merge implementation when ready
2. Create tickets for P1 action items
3. Mark task as "Done" after merge
4. File reports archived at:
   - Gate: {gate-file}
   - Assessments: .claude/quality/assessments/{task-id}-*

**Action Items Tracking:**
- P0 items: {count} (must complete before merge)
- P1 items: {count} (track in issue system)

Ready to proceed with merge.
```

---

### B) Review Reports First

```
**Report Navigation Guide:**

**Start here:**
⭐ Quality Gate Report: {gate-md-file}
   - Executive summary
   - Overall decision and score
   - Links to all detailed assessments
   - Action items prioritized

**Dive deeper (as needed):**
1. Risk Profile: {risk-file}
   - P×I scores for all risks
   - Mitigation strategies
   - High-risk test scenarios

2. Test Design: {test-file}
   - Complete test strategy
   - P0/P1/P2 prioritization
   - Mock strategies

3. Traceability: {trace-file}
   - AC → Implementation → Tests mapping
   - Coverage gaps
   - Traceability matrix

4. NFR Assessment: {nfr-file}
   - Security, performance, reliability scores
   - Category-specific findings
   - Improvement recommendations

**Pro tip:** Gate report has direct links to relevant sections of each assessment.
```

---

### C) Address Action Items Now

```
**Action Items Breakdown:**

**P0 (Blocking - must fix before merge):**
{List P0 items with file references}

**P1 (Important - should fix before release):**
{List P1 items with file references}

**Recommended approach:**
1. Create subtasks for each P0 item
2. Implement fixes using implement-feature skill
3. Re-run affected quality assessments
4. Re-run quality-gate for updated decision

Would you like me to:
- Create implementation subtasks now?
- Start fixing specific items?
- Re-prioritize action items?
```

---

### D) Request Waiver

**Waiver Request Template:**

```markdown
## Quality Gate Waiver Request

**Task:** {task-id}
**Date:** {YYYYMMDD}
**Requester:** {name}

### Gap Being Waived

**Finding ID:** {finding-id}
**Severity:** {P0/P1/P2}
**Category:** {Risk/Test/Trace/NFR/Implementation/Compliance}
**Description:** {what is being waived}

### Justification

{Why waiver is necessary}

### Risk Assessment

**Likelihood of Issue:** {Low/Medium/High}
**Impact if Issue Occurs:** {Low/Medium/High}
**Mitigation:** {how risk will be managed}

### Timeline

**Temporary Waiver:** {Yes/No}
**If yes, fix by:** {date}
**Owner:** {who will address this}

### Approval

**Approved by:** {approver name}
**Approval date:** {date}
**Conditions:** {any conditions for approval}
```

**After waiver granted:**
```
✓ Waiver recorded in gate file
✓ Gate decision updated to: WAIVED
✓ Waiver details: {gate-file}#waivers
✓ Follow-up ticket: {ticket-id} (if temporary waiver)
```

---

### E) Re-run Specific Assessment

```
**Re-run Assessment Options:**

Which assessment(s) need to be re-run?

1. Risk Profile - If risks changed
2. Test Design - If test strategy changed
3. Traceability - If implementation/tests changed
4. NFR Assessment - If NFR concerns changed
5. Quality Gate - Always re-run after any assessment changes

**Note:** Quality gate MUST be re-run if any assessment changes.

**Select assessments to re-run:**
{User selection}

**Re-running:**
{Execute selected skills}
{Re-run quality-gate}
{Present updated summary}
```

---

## Configuration Template

Expected configuration in `.claude/config.yaml`:

```yaml
quality:
  qualityLocation: .claude/quality
  gateThreshold: CONCERNS
  riskScoreThreshold: 6
  requireAllAssessments: false
```

---

## Execution Mode Templates

### Full Review Mode

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Review: Full Assessment
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id}
Mode: Full Review (all 5 skills)

Executing:
  ○ Risk Profile
  ○ Test Design
  ○ Requirements Traceability
  ○ NFR Assessment
  ○ Quality Gate

Estimated duration: 15-20 minutes
```

---

### Individual Skills Mode

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Review: Individual Skills
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id}
Mode: Individual Skills

Selected skills:
  ● {skill-1}
  ● {skill-2}

Note: Quality gate requires all assessments.
Individual mode will not generate gate decision.
```

---

### Resume Mode

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Review: Resume Partial Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id}
Mode: Resume

Previous assessments found:
  ✓ Risk Profile: {date}
  ✓ Test Design: {date}
  ✗ Traceability: Missing
  ✗ NFR Assessment: Missing
  ✗ Quality Gate: Missing

Resuming from: Requirements Traceability
Remaining: 3 skills
```

---

## Error Templates

### Task Not Ready Error

```
❌ Error: Task not ready for quality review

**Issue:** Task status is "{current-status}" (expected "Review")

**Prerequisites for quality review:**
- Task status: "Review"
- All tasks completed: [x] marked
- Implementation Record populated
- Tests passing
- Coverage >= threshold

**Next steps:**
1. Complete implementation
2. Update task status to "Review"
3. Re-run review-task
```

---

### Skill Execution Error

```
❌ Error: {skill-name} execution failed

**Error:** {error-message}

**Options:**
A) Fix issue and re-run this skill
B) Skip this skill and continue (reduces confidence)
C) Abort quality review

**Impact of skipping:**
- Quality gate confidence reduced
- Missing data for gate decision
- May prevent PASS decision
```

---

### Configuration Missing Error

```
❌ Error: Configuration file not found

**Expected:** .claude/config.yaml

**Required configuration:**
```yaml
quality:
  qualityLocation: .claude/quality
  gateThreshold: CONCERNS
  riskScoreThreshold: 6
```

**Next steps:**
1. Create .claude/config.yaml
2. Add quality configuration
3. Re-run review-task
```

---

*Part of BMAD Enhanced Quality Suite - review-task orchestration skill*
