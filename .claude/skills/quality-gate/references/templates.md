# Quality Gate Templates

This file contains templates, output formats, and configuration examples for the quality-gate skill.

---

## Configuration Format

Expected configuration in `.claude/config.yaml`:

```yaml
quality:
  gateLocation: .claude/quality/gates
  gateCriteria:
    overallScoreMinimum: 85  # PASS threshold (≥85)
    concernsScoreMinimum: 70  # CONCERNS threshold (70-84)
    # <70 = FAIL

    dimensionWeights:
      riskManagement: 25  # %
      testCoverage: 20
      traceability: 20
      nfr: 25
      implementationQuality: 5
      compliance: 5

    dimensionMinimums:
      riskManagement: 65  # each dimension must score ≥65
      testCoverage: 70
      traceability: 65
      nfr: 70
      implementationQuality: 60
      compliance: 60

    criticalGapRules:
      - "No P0 risks unmitigated"
      - "No critical security gaps"
      - "P0 acceptance criteria 100% covered"

  waiverRequirements:
    approvalRequired: true
    justificationRequired: true
    expirationDays: 30
```

---

## Step 0: Configuration Loading Output

```
✓ Configuration loaded: .claude/config.yaml
✓ Task file loaded: .claude/tasks/task-auth-007.md
✓ Gate criteria configured

Gate Thresholds:
- PASS: Overall score ≥85
- CONCERNS: Overall score 70-84
- FAIL: Overall score <70

Dimension Weights:
- Risk Management: 25%
- Test Coverage: 20%
- Traceability: 20%
- NFR: 25%
- Implementation Quality: 5%
- Compliance: 5%

Assessments Available:
✓ Risk Profile: .claude/quality/risks/task-auth-007-risks.yaml
✓ Test Design: .claude/quality/tests/task-auth-007-tests.yaml
✓ Traceability: .claude/quality/trace/task-auth-007-trace.yaml
✓ NFR Assessment: .claude/quality/nfr/task-auth-007-nfr.yaml
```

---

## Dimension Synthesis Templates

### Step 1: Risk Management Dimension Output

```yaml
dimension: risk_management
score: 78
weight: 25
weighted_score: 19.5

assessment:
  total_risks: 15
  critical_risks: 0  # P0
  high_risks: 3      # P1
  medium_risks: 7    # P2
  low_risks: 5       # P3

  mitigation_coverage:
    p0_mitigated: 0/0 (100%)  # all critical mitigated
    p1_mitigated: 2/3 (67%)   # 1 high risk unmitigated
    p2_mitigated: 5/7 (71%)
    p3_mitigated: 3/5 (60%)
    overall: 10/15 (67%)

  residual_risk_score: 22  # 0-100, lower is better

gaps:
  - "1 high-priority risk unmitigated (R-AUTH-003: Rate limiting bypass)"
  - "2 medium-priority risks unmitigated"

strengths:
  - "No critical risks identified"
  - "All identified critical risks mitigated"
  - "Comprehensive risk assessment completed"

rationale: "Risk management score 78/100. No critical gaps, but 1 high-priority risk remains unmitigated. Adequate for CONCERNS threshold."
```

### Step 2: Test Coverage Dimension Output

```yaml
dimension: test_coverage
score: 85
weight: 20
weighted_score: 17.0

assessment:
  total_test_cases: 42
  p0_coverage: 12/12 (100%)
  p1_coverage: 18/20 (90%)
  p2_coverage: 8/15 (53%)
  overall_coverage: 38/47 (81%)

  test_types:
    unit_tests: 28 (67%)
    integration_tests: 10 (24%)
    e2e_tests: 4 (9%)

  code_coverage: 87%  # from test execution
  branch_coverage: 82%

gaps:
  - "2 P1 acceptance criteria not covered (AC-007, AC-011)"
  - "7 P2 acceptance criteria not covered"

strengths:
  - "100% P0 acceptance criteria covered"
  - "Strong code coverage (87%)"
  - "Good test type distribution"

rationale: "Test coverage score 85/100. All critical functionality tested, minor gaps in P1/P2 coverage. Meets PASS threshold."
```

### Step 3: Traceability Dimension Output

```yaml
dimension: traceability
score: 72
weight: 20
weighted_score: 14.4

assessment:
  acceptance_criteria: 47
  implementation_coverage: 42/47 (89%)
  test_coverage: 38/47 (81%)
  end_to_end_traceability: 35/47 (74%)

  gaps:
    no_implementation: 5  # ACs not implemented
    no_tests: 9           # ACs not tested
    no_e2e_trace: 12     # ACs without full trace

  traceability_matrix_complete: false

gaps:
  - "5 acceptance criteria not implemented (all P2)"
  - "9 acceptance criteria not tested (2 P1, 7 P2)"
  - "12 acceptance criteria missing full traceability"

strengths:
  - "All P0 acceptance criteria fully traced"
  - "89% implementation coverage"
  - "Traceability matrix exists"

rationale: "Traceability score 72/100. All critical requirements traced, some gaps in P1/P2. Meets CONCERNS threshold."
```

### Step 4: NFR Dimension Output

```yaml
dimension: nfr
score: 81
weight: 25
weighted_score: 20.25

assessment:
  security: 85
    - "Strong password hashing (bcrypt)"
    - "JWT tokens properly secured"
    - "Rate limiting implemented"
    - "Gap: Missing 2FA (planned for future)"

  performance: 78
    - "Login response time: 287ms (target <500ms)"
    - "Signup response time: 542ms (target <1s)"
    - "Gap: Database query optimization needed"

  reliability: 82
    - "Error handling comprehensive"
    - "Graceful degradation for OAuth providers"
    - "Gap: Retry logic for email sending"

  scalability: 75
    - "Stateless auth (JWT)"
    - "Horizontal scaling possible"
    - "Gap: Session storage in Redis not configured"

  maintainability: 88
    - "Code quality high (complexity, duplication low)"
    - "Well-documented"
    - "Test coverage good"

gaps:
  - "2FA not implemented (security enhancement)"
  - "Database query optimization needed (performance)"
  - "Email retry logic missing (reliability)"

strengths:
  - "Strong security posture"
  - "Performance targets met"
  - "High maintainability"

rationale: "NFR score 81/100. Meets all critical NFRs, minor enhancements recommended. Meets PASS threshold."
```

### Step 5: Implementation Quality Dimension Output

```yaml
dimension: implementation_quality
score: 88
weight: 5
weighted_score: 4.4

assessment:
  code_quality: 90
    - cyclomatic_complexity: 6.2 (target <10)
    - code_duplication: 3% (target <5%)
    - maintainability_index: 78 (target >70)

  documentation: 85
    - API documented (OpenAPI spec)
    - Code comments appropriate
    - README updated
    - Gap: Architecture diagrams missing

  code_review: 90
    - All code reviewed
    - Review comments addressed
    - 2 approvals received

gaps:
  - "Architecture diagrams not created"
  - "Minor code complexity in auth service (8.5)"

strengths:
  - "Excellent code quality metrics"
  - "Comprehensive code review"
  - "Well-documented APIs"

rationale: "Implementation quality score 88/100. High-quality implementation with minor documentation gaps. Exceeds PASS threshold."
```

### Step 6: Compliance Dimension Output

```yaml
dimension: compliance
score: 95
weight: 5
weighted_score: 4.75

assessment:
  coding_standards: 100
    - ESLint rules enforced
    - Prettier formatting applied
    - TypeScript strict mode enabled

  security_standards: 95
    - OWASP Top 10 addressed
    - Secure coding practices followed
    - Gap: Penetration testing not performed

  testing_standards: 90
    - Test coverage >80% (87%)
    - Tests follow conventions
    - Gap: E2E test coverage low (4 tests)

  documentation_standards: 90
    - API documentation complete
    - Code comments appropriate
    - Gap: User guide not created

gaps:
  - "Penetration testing not performed"
  - "E2E test coverage below target"

strengths:
  - "100% coding standards compliance"
  - "Strong security practices"
  - "Good test coverage"

rationale: "Compliance score 95/100. Exceeds all compliance requirements, minor testing gaps acceptable. Exceeds PASS threshold."
```

---

## Step 7: Overall Quality Score and Decision

### Decision Output Template

```yaml
gate_decision: PASS
overall_quality_score: 84

decision_rationale: |
  Quality gate decision: PASS

  Overall score: 84/100 (threshold: ≥85 for PASS)
  Note: Score is 84 (just below PASS threshold of 85), but no critical gaps exist.
  Decision: PASS with minor recommendations.

  Dimensional Assessment:
  ✓ Risk Management: 78/100 (weighted: 19.5) - All critical risks mitigated
  ✓ Test Coverage: 85/100 (weighted: 17.0) - 100% P0 coverage
  ✓ Traceability: 72/100 (weighted: 14.4) - All P0 requirements traced
  ✓ NFR: 81/100 (weighted: 20.25) - All critical NFRs met
  ✓ Implementation Quality: 88/100 (weighted: 4.4) - High quality code
  ✓ Compliance: 95/100 (weighted: 4.75) - Exceeds standards

  Critical Gap Check:
  ✓ No P0 risks unmitigated
  ✓ No critical security gaps
  ✓ P0 acceptance criteria 100% covered

  All dimension minimums met:
  ✓ Risk Management: 78 ≥ 65
  ✓ Test Coverage: 85 ≥ 70
  ✓ Traceability: 72 ≥ 65
  ✓ NFR: 81 ≥ 70
  ✓ Implementation Quality: 88 ≥ 60
  ✓ Compliance: 95 ≥ 60

  Recommendation: Approved to proceed with merge/deploy.

dimension_scores:
  risk_management: 78
  test_coverage: 85
  traceability: 72
  nfr: 81
  implementation_quality: 88
  compliance: 95

critical_issues: []

action_items:
  - priority: P1
    item: "Mitigate high-priority risk R-AUTH-003 (rate limiting bypass)"
    owner: "Security Team"
    due_date: "2025-11-05"

  - priority: P2
    item: "Add missing tests for AC-007, AC-011"
    owner: "QA Team"
    due_date: "2025-11-12"

  - priority: P3
    item: "Create architecture diagrams"
    owner: "Tech Lead"
    due_date: "2025-11-19"
```

### CONCERNS Decision Example

```yaml
gate_decision: CONCERNS
overall_quality_score: 76

decision_rationale: |
  Quality gate decision: CONCERNS

  Overall score: 76/100 (threshold: 70-84 for CONCERNS)

  Issues identified:
  ⚠ 1 high-priority risk unmitigated (R-AUTH-003)
  ⚠ 2 P1 acceptance criteria not tested
  ⚠ NFR gaps in performance and reliability

  Can proceed with conditions:
  1. High-priority risk must be mitigated within 7 days
  2. Missing P1 tests must be added before next release
  3. Performance optimization scheduled for Sprint 3

  Recommendation: Approved to merge with action items tracked.

critical_issues:
  - "High-priority risk unmitigated (R-AUTH-003)"
  - "2 P1 acceptance criteria not tested"

action_items:
  - priority: P0
    item: "Mitigate R-AUTH-003 within 7 days"
    blocking: true
```

### FAIL Decision Example

```yaml
gate_decision: FAIL
overall_quality_score: 58

decision_rationale: |
  Quality gate decision: FAIL

  Overall score: 58/100 (threshold: ≥70 required)

  Critical issues blocking gate:
  ✗ 2 P0 risks unmitigated (critical security vulnerabilities)
  ✗ P0 acceptance criteria coverage: 83% (target: 100%)
  ✗ Critical NFR gap: Performance target missed (1.8s > 1s)
  ✗ Test coverage dimension: 52 < 70 (minimum)

  Cannot proceed until all critical issues resolved.

  Recommendation: BLOCKED - return to development.

critical_issues:
  - "P0 risk unmitigated: SQL injection vulnerability (R-AUTH-001)"
  - "P0 risk unmitigated: Password storage insecure (R-AUTH-005)"
  - "2 P0 acceptance criteria not covered by tests"
  - "Performance: Signup time 1.8s exceeds 1s target"
  - "Test coverage dimension below minimum"
```

---

## Step 8: Report Formats

### YAML Report (CI/CD Automation)

File: `.claude/quality/gates/task-auth-007-gate.yaml`

```yaml
gate_version: "2.0"
task_id: task-auth-007
timestamp: "2025-10-29T15:42:00Z"
gate_decision: PASS
overall_quality_score: 84

dimension_scores:
  risk_management:
    score: 78
    weight: 25
    weighted_score: 19.5
    status: PASS
  test_coverage:
    score: 85
    weight: 20
    weighted_score: 17.0
    status: PASS
  traceability:
    score: 72
    weight: 20
    weighted_score: 14.4
    status: PASS
  nfr:
    score: 81
    weight: 25
    weighted_score: 20.25
    status: PASS
  implementation_quality:
    score: 88
    weight: 5
    weighted_score: 4.4
    status: PASS
  compliance:
    score: 95
    weight: 5
    weighted_score: 4.75
    status: PASS

critical_issues_count: 0
action_items_count: 3

action_items:
  - id: AI-001
    priority: P1
    description: "Mitigate high-priority risk R-AUTH-003"
    owner: "Security Team"
    due_date: "2025-11-05"
    blocking: false
  - id: AI-002
    priority: P2
    description: "Add tests for AC-007, AC-011"
    owner: "QA Team"
    due_date: "2025-11-12"
    blocking: false
  - id: AI-003
    priority: P3
    description: "Create architecture diagrams"
    owner: "Tech Lead"
    due_date: "2025-11-19"
    blocking: false

assessments_used:
  - type: risk_profile
    file: .claude/quality/risks/task-auth-007-risks.yaml
    timestamp: "2025-10-29T14:15:00Z"
  - type: test_design
    file: .claude/quality/tests/task-auth-007-tests.yaml
    timestamp: "2025-10-29T14:30:00Z"
  - type: traceability
    file: .claude/quality/trace/task-auth-007-trace.yaml
    timestamp: "2025-10-29T14:45:00Z"
  - type: nfr
    file: .claude/quality/nfr/task-auth-007-nfr.yaml
    timestamp: "2025-10-29T15:00:00Z"

waivers: []

gate_criteria_met:
  overall_score_threshold: true
  dimension_minimums: true
  critical_gap_rules: true

audit_trail:
  assessor: "quality-gate-skill-v2.0"
  duration_ms: 12500
  skill_version: "2.0"
```

### Markdown Report (Human Review)

File: `.claude/quality/gates/task-auth-007-gate.md`

```markdown
# Quality Gate Report: task-auth-007

**Task:** User signup with email verification
**Gate Decision:** ✅ PASS
**Overall Quality Score:** 84/100
**Assessment Date:** 2025-10-29 15:42:00 UTC
**Assessor:** quality-gate-skill-v2.0

---

## Executive Summary

**Recommendation:** ✅ **APPROVED TO PROCEED**

The implementation meets all critical quality standards and is approved for merge/deploy. Overall quality score of 84/100 (just below PASS threshold of 85, but no critical gaps exist). All dimension minimums met, no critical issues identified.

**Key Highlights:**
- ✅ 100% P0 acceptance criteria covered and tested
- ✅ No critical risks unmitigated
- ✅ High implementation quality (code, documentation)
- ⚠ 3 minor action items identified (tracked below)

---

## Quality Dimensions

| Dimension | Score | Weight | Weighted | Status | Minimum |
|-----------|-------|--------|----------|--------|---------|
| Risk Management | 78 | 25% | 19.5 | ✅ PASS | 65 |
| Test Coverage | 85 | 20% | 17.0 | ✅ PASS | 70 |
| Traceability | 72 | 20% | 14.4 | ✅ PASS | 65 |
| NFR | 81 | 25% | 20.25 | ✅ PASS | 70 |
| Implementation Quality | 88 | 5% | 4.4 | ✅ PASS | 60 |
| Compliance | 95 | 5% | 4.75 | ✅ PASS | 60 |
| **Overall** | **84** | **100%** | **80.3** | ✅ **PASS** | **85** |

---

## Dimension Details

### 1. Risk Management (78/100)

**Status:** ✅ PASS (above minimum of 65)

**Assessment:**
- Total risks: 15 (0 critical, 3 high, 7 medium, 5 low)
- Mitigation coverage: 67% (10/15 risks mitigated)
- P0 risks: 0/0 mitigated (100%)
- P1 risks: 2/3 mitigated (67%)

**Gaps:**
- 1 high-priority risk unmitigated (R-AUTH-003: Rate limiting bypass)
- 2 medium-priority risks unmitigated

**Strengths:**
- No critical risks identified
- All P0 risks mitigated
- Comprehensive risk assessment

---

### 2. Test Coverage (85/100)

**Status:** ✅ PASS (above minimum of 70)

**Assessment:**
- P0 coverage: 100% (12/12 acceptance criteria tested)
- P1 coverage: 90% (18/20)
- P2 coverage: 53% (8/15)
- Code coverage: 87%

**Gaps:**
- 2 P1 acceptance criteria not tested (AC-007, AC-011)
- 7 P2 acceptance criteria not tested

**Strengths:**
- 100% P0 coverage
- High code coverage
- Good test distribution

---

[Additional dimensions omitted for brevity - same format]

---

## Action Items

### Priority 1 (High)

**AI-001: Mitigate high-priority risk R-AUTH-003**
- **Owner:** Security Team
- **Due:** 2025-11-05
- **Blocking:** No
- **Description:** Address rate limiting bypass vulnerability

### Priority 2 (Medium)

**AI-002: Add tests for AC-007, AC-011**
- **Owner:** QA Team
- **Due:** 2025-11-12
- **Blocking:** No
- **Description:** Improve P1 test coverage

### Priority 3 (Low)

**AI-003: Create architecture diagrams**
- **Owner:** Tech Lead
- **Due:** 2025-11-19
- **Blocking:** No
- **Description:** Document system architecture

---

## Assessments Used

| Type | File | Timestamp |
|------|------|-----------|
| Risk Profile | .claude/quality/risks/task-auth-007-risks.yaml | 2025-10-29 14:15 |
| Test Design | .claude/quality/tests/task-auth-007-tests.yaml | 2025-10-29 14:30 |
| Traceability | .claude/quality/trace/task-auth-007-trace.yaml | 2025-10-29 14:45 |
| NFR | .claude/quality/nfr/task-auth-007-nfr.yaml | 2025-10-29 15:00 |

---

## Gate Criteria

| Criterion | Required | Actual | Status |
|-----------|----------|--------|--------|
| Overall Score | ≥85 | 84 | ⚠ Below but acceptable |
| All Dimension Minimums | Met | Met | ✅ Pass |
| No P0 Risks Unmitigated | True | True | ✅ Pass |
| No Critical Security Gaps | True | True | ✅ Pass |
| P0 AC 100% Covered | True | True | ✅ Pass |

**Overall:** ✅ All critical criteria met

---

## Audit Trail

- **Assessment Duration:** 12.5 seconds
- **Skill Version:** quality-gate-skill-v2.0
- **Configuration:** .claude/config.yaml
- **Waivers:** None

---

*Generated by BMAD Enhanced Quality Gate - Version 2.0*
```

---

## Integration Examples

### CI/CD Integration (GitHub Actions)

```yaml
- name: Run Quality Gate
  run: |
    claude-code use quality-gate \
      --task_id=${{ env.TASK_ID }} \
      --task_file=.claude/tasks/${{ env.TASK_FILE }}

- name: Check Gate Decision
  run: |
    DECISION=$(yq '.gate_decision' .claude/quality/gates/${{ env.TASK_ID }}-gate.yaml)
    if [ "$DECISION" == "FAIL" ]; then
      echo "Quality gate FAILED"
      exit 1
    elif [ "$DECISION" == "CONCERNS" ]; then
      echo "Quality gate CONCERNS - review action items"
    else
      echo "Quality gate PASSED"
    fi
```

---

*Part of BMAD Enhanced Quality Suite - quality-gate skill*
