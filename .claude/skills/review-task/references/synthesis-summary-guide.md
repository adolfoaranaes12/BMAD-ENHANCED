# Synthesis & Summary Guide

## Purpose

Guide for combining results from all 5 skills and presenting unified quality review summary.

---

## Data Collection

### Collect Results from Each Skill

After each skill completes, capture key data:

**From risk-profile:**
```yaml
riskProfile:
  file: .claude/quality/assessments/task-007-risk-20251029.md
  summary:
    totalRisks: 12
    criticalRisks: 1
    highRisks: 3
    mediumRisks: 5
    lowRisks: 3
    mitigated: 3
    highRisksMitigated: 3/4
    topRisks:
      - "Authentication bypass (P=3, I=3, Score=9)"
      - "SQL injection (P=2, I=3, Score=6)"
      - "XSS vulnerability (P=2, I=3, Score=6)"
```

**From test-design:**
```yaml
testDesign:
  file: .claude/quality/assessments/task-007-test-design-20251029.md
  summary:
    totalTests: 24
    p0Tests: 8
    p1Tests: 12
    p2Tests: 4
    testLevels:
      unit: 12
      integration: 10
      e2e: 2
    estimatedDuration: "5m 30s"
    mockStrategies: ["Database", "Email Service", "Payment Gateway"]
```

**From trace-requirements:**
```yaml
traceability:
  file: .claude/quality/assessments/task-007-trace-20251029.md
  summary:
    totalAC: 6
    implemented: 5
    tested: 6
    implementationCoverage: 83%
    testCoverage: 100%
    traceabilityScore: 87.5%
    gaps:
      critical: 0
      high: 2
      medium: 1
      low: 0
```

**From nfr-assess:**
```yaml
nfr:
  file: .claude/quality/assessments/task-007-nfr-20251029.md
  summary:
    overallScore: 72%
    categories:
      security: 70%
      performance: 80%
      reliability: 65%
      maintainability: 75%
      scalability: 70%
      usability: 70%
    gaps:
      critical: 2
      high: 4
      medium: 3
      low: 1
```

**From quality-gate:**
```yaml
qualityGate:
  yamlFile: .claude/quality/gates/task-007-gate-20251029.yaml
  mdFile: .claude/quality/gates/task-007-gate-20251029.md
  decision:
    status: CONCERNS
    overallScore: 75.5%
    canProceed: true
    confidence: HIGH
    blockers: []
    actionItems:
      p0: 2
      p1: 5
      p2: 3
      total: 10
    waivers: 1
    reasoning: |
      Implementation meets baseline quality standards with some concerns.
      2 P0 action items must be addressed before merge.
      Security gaps identified but mitigated with monitoring.
```

---

## Synthesis Strategy

### Combine Dimensions into Overall Picture

**6 Quality Dimensions:**

1. **Risk Management** (from risk-profile)
2. **Test Coverage** (from test-design + traceability)
3. **Requirements Traceability** (from trace-requirements)
4. **Non-Functional Requirements** (from nfr-assess)
5. **Implementation Quality** (from task file Implementation Record)
6. **Compliance** (from gate decision)

**Each dimension scored 0-100%**

---

### Dimension Synthesis

**1. Risk Management Dimension:**
```yaml
riskManagement:
  score: 75%
  status: GOOD
  metrics:
    totalRisks: 12
    criticalMitigated: 1/1 (100%)
    highMitigated: 3/4 (75%)
    risksMitigated: 4/12 (33%)
    testCoverage: 4/4 P0 risks (100%)
  details:
    - "✓ All critical risks mitigated"
    - "⚠ 1 high risk not yet mitigated (password complexity)"
    - "✓ All high risks have test coverage"
  source: {risk-file}
```

**2. Test Coverage Dimension:**
```yaml
testCoverage:
  score: 85%
  status: EXCELLENT
  metrics:
    totalTests: 24
    p0Designed: 8/8 (100%)
    p1Designed: 12/12 (100%)
    testsPassing: 20/24 (83%)
    codeCoverage: 87%
  details:
    - "✓ All P0 tests designed and passing"
    - "⚠ 4 P1 tests failing (need fixes)"
    - "✓ Code coverage above 85% threshold"
  sources:
    - {test-design-file}
    - {trace-file}
```

**3. Requirements Traceability Dimension:**
```yaml
traceability:
  score: 87.5%
  status: EXCELLENT
  metrics:
    totalAC: 6
    implementationCoverage: 83% (5/6 AC)
    testCoverage: 100% (6/6 AC)
    traceabilityScore: 87.5%
  gaps:
    critical: 0
    high: 2
    medium: 1
  details:
    - "✓ All AC have test coverage"
    - "⚠ 1 AC partially implemented (email verification)"
    - "✓ High traceability score (>80%)"
  source: {trace-file}
```

**4. Non-Functional Requirements Dimension:**
```yaml
nfr:
  score: 72%
  status: CONCERNS
  categories:
    security: 70% (CONCERNS)
    performance: 80% (GOOD)
    reliability: 65% (CONCERNS)
    maintainability: 75% (GOOD)
    scalability: 70% (CONCERNS)
    usability: 70% (CONCERNS)
  details:
    - "⚠ Security: Input validation gaps, password complexity"
    - "✓ Performance: Response times meet targets"
    - "⚠ Reliability: Error handling incomplete"
    - "✓ Maintainability: Good code quality, docs present"
  source: {nfr-file}
```

**5. Implementation Quality Dimension:**
```yaml
implementationQuality:
  score: 90%
  status: EXCELLENT
  metrics:
    tasksComplete: 8/8 (100%)
    subtasksComplete: 24/24 (100%)
    implementationRecordComplete: true
    filesModified: 12
    testFiles: 6
  details:
    - "✓ All tasks and subtasks complete"
    - "✓ Implementation Record fully documented"
    - "✓ Code follows project standards"
  source: task-file
```

**6. Compliance Dimension:**
```yaml
compliance:
  score: 85%
  status: GOOD
  checks:
    acceptanceCriteriaMet: 83% (5/6)
    testingStandards: 100%
    documentationStandards: 90%
    codeStandards: 85%
    securityStandards: 70%
  details:
    - "✓ Testing standards met"
    - "⚠ Security standards gaps (input validation)"
    - "✓ Documentation complete"
  source: gate-file
```

---

## Task File Update

### Locate Quality Review Section

**Find in task file:**
```markdown
## Quality Review
<!-- This section updated by quality-review skill -->
```

**Or if missing, add after Implementation Record:**
```markdown
## Implementation Record

[...]

---

## Quality Review
<!-- This section updated by quality-review skill -->
```

---

### Generate Quality Review Summary

**Template:**
```markdown
## Quality Review

### Review Date
{YYYYMMDD HH:MM:SS}

### Reviewer
review-task-v2.0 (claude-sonnet-4-5)

### Quality Gate Decision
**{PASS | CONCERNS | FAIL | WAIVED}**

### Overall Quality Score
**{score}%**

### Assessment Reports

All detailed reports available at:

1. **⭐ Quality Gate (START HERE):** `.claude/quality/gates/{task-id}-gate-{date}.md`
2. **Risk Profile:** `.claude/quality/assessments/{task-id}-risk-{date}.md`
3. **Test Design:** `.claude/quality/assessments/{task-id}-test-design-{date}.md`
4. **Requirements Traceability:** `.claude/quality/assessments/{task-id}-trace-{date}.md`
5. **NFR Assessment:** `.claude/quality/assessments/{task-id}-nfr-{date}.md`
6. **Gate YAML (CI/CD):** `.claude/quality/gates/{task-id}-gate-{date}.yaml`

### Executive Summary

{2-3 sentence summary from gate decision}

**Example:**
```
Implementation demonstrates good overall quality (75.5%) with some concerns requiring attention. All acceptance criteria are tested with excellent traceability (87.5%). Two P0 action items related to security gaps must be addressed before merge: input validation strengthening and password complexity enforcement.
```

### Quality Dimensions

| Dimension | Score | Status | Key Findings |
|-----------|-------|--------|--------------|
| Risk Management | {risk_score}% | {status} | {top_finding} |
| Test Coverage | {test_score}% | {status} | {top_finding} |
| Requirements Traceability | {trace_score}% | {status} | {top_finding} |
| Non-Functional Requirements | {nfr_score}% | {status} | {top_finding} |
| Implementation Quality | {impl_score}% | {status} | {top_finding} |
| Compliance | {compliance_score}% | {status} | {top_finding} |

**Example:**
```markdown
| Dimension | Score | Status | Key Findings |
|-----------|-------|--------|--------------|
| Risk Management | 75% | GOOD | All critical risks mitigated, 1 high risk open |
| Test Coverage | 85% | EXCELLENT | All P0 tests passing, 4 P1 tests need fixes |
| Requirements Traceability | 87.5% | EXCELLENT | All AC tested, 1 AC partially implemented |
| Non-Functional Requirements | 72% | CONCERNS | Security gaps identified, performance good |
| Implementation Quality | 90% | EXCELLENT | All tasks complete, well-documented |
| Compliance | 85% | GOOD | Testing standards met, security gaps |
```

### Key Findings

**Critical:**
{List critical findings from all assessments}

**High Priority:**
{List high priority findings}

**Example:**
```markdown
### Key Findings

**Critical:**
- Authentication bypass risk mitigated with additional validation (Risk Profile)

**High Priority:**
- 2 security gaps: Input validation incomplete, password complexity not enforced (NFR Assessment)
- 1 AC partially implemented: Email verification sends but doesn't block unverified users (Traceability)
- 4 P1 tests failing: Password strength tests need updated fixtures (Test Design)
```

### Action Items

**Must Complete Before Merge (P0):**
{List P0 action items from gate}

**Should Complete Before Release (P1):**
{List P1 action items from gate}

**Example:**
```markdown
### Action Items

**Must Complete Before Merge (P0):**
1. **Strengthen input validation** - Add validation for all user inputs (email, password, name) with proper sanitization (Est: 2 hours)
2. **Enforce password complexity** - Implement password strength requirements (min 12 chars, upper/lower/number/special) (Est: 1 hour)

**Should Complete Before Release (P1):**
1. Fix 4 failing P1 tests (password strength test fixtures) (Est: 1 hour)
2. Complete email verification blocking (prevent unverified users from accessing protected resources) (Est: 3 hours)
3. Add error handling for edge cases in password reset flow (Est: 2 hours)
4. Improve logging for authentication failures (security monitoring) (Est: 1 hour)
5. Add rate limiting to password reset endpoint (prevent abuse) (Est: 2 hours)

**Total estimated effort:** P0: 3 hours, P1: 9 hours
```

### Recommendation

{Recommendation from gate decision: approve/fix/waive}

**Example:**
```markdown
### Recommendation

**Gate Status:** CONCERNS - Can proceed with conditions

**Recommended Action:**
1. Address 2 P0 action items (estimated 3 hours)
2. Re-run security assessment to verify fixes
3. Then proceed with merge

**Rationale:**
Implementation is production-ready with two security gaps that must be closed. The gaps are well-understood and have straightforward fixes. Once addressed, the implementation will meet all quality standards for merge.

**Waiver Option:**
If urgent merge needed, P0 items can be addressed post-merge with:
- Waiver approved by: [Security Team Lead]
- Timeline: Must be fixed within 2 business days
- Mitigation: Enhanced monitoring enabled for authentication endpoints
- Tracking: Created follow-up tickets AUTH-101, AUTH-102
```

### Approval

- [ ] Quality review complete
- [ ] Action items documented
- [ ] Decision: {APPROVE | FIX_THEN_APPROVE | REJECT | WAIVED}
- [ ] Approved by: _______________
- [ ] Date: _______________

---

For complete assessment details and technical findings, start with the Quality Gate report linked above.
```

---

### Update Task File

**Use Edit tool:**
```typescript
// Read current task file
const taskContent = await readFile(taskFilePath, 'utf-8');

// Find Quality Review section
const reviewRegex = /## Quality Review[\s\S]*?(?=\n## |\n---\n|$)/;

// Generate new review content
const newReviewContent = generateReviewContent(
  gateDecision,
  allAssessments,
  actionItems
);

// Replace or append
if (reviewRegex.test(taskContent)) {
  // Replace existing
  const updated = taskContent.replace(reviewRegex, newReviewContent);
  await writeFile(taskFilePath, updated, 'utf-8');
} else {
  // Append new section
  const updated = taskContent + '\n\n' + newReviewContent;
  await writeFile(taskFilePath, updated, 'utf-8');
}
```

---

## Unified Summary Presentation

### Summary Structure

**Full summary format:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Comprehensive Quality Review Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id} - {title}
Date: {YYYYMMDD HH:MM:SS}
Duration: {duration}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Quality Gate Decision: {STATUS}

**Overall Quality Score:** {score}%
**Can Proceed:** {YES/NO/CONDITIONAL}
**Confidence:** {HIGH/MEDIUM/LOW}
**Blockers:** {count}
**Action Items:** {total} ({p0} P0, {p1} P1, {p2} P2)
**Waivers:** {count}

{Brief rationale from gate decision - 2-3 sentences}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📊 Quality Dimension Scores

1. Risk Management: {score}% ({status})
   - {key_metric_1}
   - {key_metric_2}
   - Report: {risk-file}

2. Test Coverage: {score}% ({status})
   - {key_metric_1}
   - {key_metric_2}
   - Report: {test-file}

3. Requirements Traceability: {score}% ({status})
   - {key_metric_1}
   - {key_metric_2}
   - Report: {trace-file}

4. Non-Functional Requirements: {score}% ({status})
   - {key_metric_1}
   - {key_metric_2}
   - Report: {nfr-file}

5. Implementation Quality: {score}% ({status})
   - {key_metric_1}
   - {key_metric_2}
   - Source: Task file

6. Compliance: {score}% ({status})
   - {key_metric_1}
   - {key_metric_2}
   - Source: Gate decision

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🚨 Critical Findings

{List of critical and high findings from all assessments, grouped by severity}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✅ Action Items

### P0 (Must Complete Before Merge):
{Numbered list with estimates}

### P1 (Should Complete Before Release):
{Numbered list with estimates}

### P2 (Nice to Have):
{Numbered list}

**Total Estimated Effort:** P0: {hours}, P1: {hours}, P2: {hours}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📄 Generated Reports

All reports available at `.claude/quality/`:

1. **⭐ Quality Gate (START HERE):** `gates/{task-id}-gate-{date}.md`
   → Comprehensive synthesis with all findings and recommendations

2. **Risk Profile:** `assessments/{task-id}-risk-{date}.md`
   → 12 risks identified (1 critical, 3 high), mitigation strategies

3. **Test Design:** `assessments/{task-id}-test-design-{date}.md`
   → 24 tests designed (8 P0, 12 P1, 4 P2), mock strategies

4. **Requirements Traceability:** `assessments/{task-id}-trace-{date}.md`
   → AC→Impl→Test mapping, 87.5% traceability score

5. **NFR Assessment:** `assessments/{task-id}-nfr-{date}.md`
   → 6 category scores, security/performance/reliability analysis

6. **Gate YAML (CI/CD):** `gates/{task-id}-gate-{date}.yaml`
   → Machine-readable gate decision for automation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Next Steps

{Recommendations based on gate status}

**For PASS:**
- ✅ Approved for merge
- Create tickets for P1/P2 action items
- Mark task as "Done" after merge
- Monitor in production

**For CONCERNS:**
- ⚠️ Address P0 action items (estimated {hours} hours)
- Re-run quality gate after fixes
- Then proceed with merge
- OR: Request waiver with justification

**For FAIL:**
- ❌ Blocked from merge
- Address all blocking issues
- Re-run full quality review
- Do not proceed until PASS or CONCERNS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ❓ What would you like to do?

A) Accept decision and proceed with merge
B) Review detailed reports first (start with gate report)
C) Address action items now (hand to implementation skill)
D) Request waiver for specific gaps (document justification)
E) Re-run specific assessment (if implementation changed)

Your choice: _
```

---

## User Decision Handling

### Option A: Accept and Proceed

```
✓ Gate decision accepted: {STATUS}
✓ Decision recorded in gate file
✓ Quality Review section updated in task file

Next steps:
1. If PASS or CONCERNS: Proceed with merge
2. Create tickets for P1/P2 action items
3. Mark task as "Done" after successful merge
4. Monitor implementation in production

Action items tracking:
- P0 items: {list with ticket IDs}
- P1 items: {list with ticket IDs}

Would you like help creating action item tickets? (Y/n)
```

---

### Option B: Review Reports

```
📄 Report Navigation Guide

Start here:
1. **Quality Gate Report** (.claude/quality/gates/{task-id}-gate-{date}.md)
   - Executive summary of all findings
   - Synthesized gate decision with rationale
   - Links to all detailed assessments
   - Read first for complete picture

Then review specific dimensions as needed:
2. **Risk Profile** - If concerned about risks
3. **Test Design** - If concerned about test coverage
4. **Traceability** - If concerned about AC coverage
5. **NFR Assessment** - If concerned about security/performance

Each report cross-references others for deep dives.

Open gate report? (Y/n)
```

---

### Option C: Address Action Items

```
🔧 Addressing Action Items

Handing P0 action items to implementation skill:

Action Items (P0):
1. Strengthen input validation (2 hours)
2. Enforce password complexity (1 hour)

Creating subtasks in task file...
✓ Subtasks added to Implementation section

Invoking implementation skill with action items:
→ .claude/skills/development/implement-feature.md

After fixes complete:
1. Re-run quality assessments (security + traceability)
2. Re-run quality gate for updated decision
3. Return to review summary

Proceed with implementation? (Y/n)
```

---

### Option D: Request Waiver

```
📋 Waiver Request

Which gaps would you like to waive?

From P0 Action Items:
1. Strengthen input validation
2. Enforce password complexity

Select item(s) to waive (comma-separated): _

[User selects: 2]

Waiver Documentation for: Enforce password complexity

Required information:
1. Justification (why waiving?): _
2. Mitigation (what instead?): _
3. Timeline (when will it be addressed?): _
4. Approver (who approves?): _
5. Tracking (ticket ID?): _

[Collect answers]

Waiver Summary:
- Gap: Enforce password complexity
- Justification: {user_input}
- Mitigation: {user_input}
- Timeline: {user_input}
- Approver: {user_input}
- Tracking: {user_input}

✓ Waiver recorded in gate file
✓ Gate status updated to: WAIVED
✓ Task file updated with waiver details

Updated Gate Decision: WAIVED
- Can proceed: YES (with waiver)
- Follow-up required: YES (within {timeline})
```

---

### Option E: Re-run Assessment

```
🔄 Re-run Assessment

Which assessment(s) have outdated data?

Available assessments:
1. Risk Profile (current)
2. Test Design (current)
3. Traceability (current)
4. NFR Assessment (current)
5. Quality Gate (synthesizes all)

Select assessment(s) to re-run (comma-separated): _

[User selects: 3,4]

Re-running:
- Requirements Traceability
- NFR Assessment

After re-run:
- Will automatically re-run Quality Gate
- Will present updated summary
- Task file will be updated

Proceed? (Y/n)

[Execute selected assessments + gate]
[Present new unified summary]
```

---

## Quick Reference

**Task File Update:**
- Replace/append Quality Review section
- Include gate decision, scores, action items
- Link to all report files
- Add approval checkboxes

**Unified Summary:**
- Gate decision at top (most important)
- 6 dimension scores
- Critical findings
- Action items with estimates
- Report links (gate first)
- Next steps guidance
- User decision prompt

**User Decisions:**
- A) Accept → Proceed with merge
- B) Review → Guide to reports
- C) Address → Hand to implementation
- D) Waiver → Document and track
- E) Re-run → Update specific assessments

---

*Part of review-task skill - Quality Suite*
