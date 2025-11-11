# Quality Gate Dimensions

This reference provides detailed scoring methodology for all 6 quality dimensions used by the quality-gate skill. Each dimension includes scoring formulas, status determination thresholds, gap identification, and calculation examples.

---

## Table of Contents

1. [Risk Management Dimension](#risk-management-dimension)
2. [Test Coverage Dimension](#test-coverage-dimension)
3. [Traceability Dimension](#traceability-dimension)
4. [NFR Dimension](#nfr-dimension)
5. [Implementation Quality Dimension](#implementation-quality-dimension)
6. [Compliance Dimension](#compliance-dimension)
7. [Dimension Weight Configuration](#dimension-weight-configuration)

---

## Risk Management Dimension

**Weight:** 25% (default, highest weight)

**Purpose:** Evaluate risk management effectiveness from risk profile assessment.

### Data Required

From risk-profile assessment:
```yaml
riskProfile:
  totalRisks: 12
  criticalRisks: 1     # Score ≥7
  highRisks: 3         # Score ≥6
  mediumRisks: 5       # Score 4-5
  lowRisks: 3          # Score ≤3

  # Mitigation coverage
  highRisksMitigated: 2/4    # (critical + high) with mitigation strategy

  # Test coverage for risks
  highRisksTested: 3/4       # (critical + high) with test cases
```

### Scoring Formula

```
Risk Management Score = (
  (Mitigation Coverage × 0.5) +
  (Test Coverage for High Risks × 0.3) +
  (Risk Score Distribution × 0.2)
)

Where:
- Mitigation Coverage = (High-risk items with mitigation) / (Critical + High risks)
- Test Coverage = (High-risk items with tests) / (Critical + High risks)
- Risk Score Distribution = 100% - (Critical × 20% + High × 10%)
```

### Status Thresholds

| Score Range | Status | Description |
|-------------|--------|-------------|
| ≥75% | PASS | Excellent risk management, high-risk items mitigated and tested |
| 50-74% | CONCERNS | Acceptable risk management but gaps exist |
| <50% | FAIL | Insufficient risk management, critical/high risks unaddressed |

### Calculation Example

**Scenario:**
- Critical risks: 1
- High risks: 3
- Total high-risk: 4
- Mitigated: 2/4 = 50%
- Tested: 3/4 = 75%
- Risk distribution: 100% - (1×20% + 3×10%) = 100% - 50% = 50%

**Calculation:**
```
Risk Management Score = (50 × 0.5) + (75 × 0.3) + (50 × 0.2)
                      = 25 + 22.5 + 10
                      = 57.5%

Status: CONCERNS (50-74% range)
Weighted Contribution: 57.5 × 0.25 = 14.4 points
```

### Gap Identification

Gaps in risk management:
- **Critical:** Critical risks (score ≥7) without mitigation strategy
- **High:** High risks (score ≥6) without test coverage
- **Medium:** High-risk areas with partial mitigation

---

## Test Coverage Dimension

**Weight:** 20% (default)

**Purpose:** Evaluate test strategy and coverage from test-design assessment.

### Data Required

From test-design assessment:
```yaml
testDesign:
  totalTests: 24
  p0Tests: 8           # Critical priority, must pass
  p1Tests: 12          # High priority, should pass
  p2Tests: 4           # Medium priority, nice to have

  testLevels:
    unit: 12
    integration: 10
    e2e: 2

  p0TestsImplemented: 8/8      # All P0 tests exist
  p0TestsPassing: 8/8          # All P0 tests pass
  p1TestsImplemented: 10/12    # Most P1 tests exist

  coveragePercentage: 85%      # Line coverage from test runs
```

### Scoring Formula

```
Test Coverage Score = (
  (P0 Tests Passing × 0.5) +
  (P1 Tests Implemented × 0.3) +
  (Coverage Percentage × 0.2)
)

Where:
- P0 Tests Passing = (P0 tests passing) / (Total P0 tests) × 100%
- P1 Tests Implemented = (P1 tests implemented) / (Total P1 tests) × 100%
- Coverage Percentage = Line coverage from test suite
```

### Status Thresholds

| Score Range | Status | Description |
|-------------|--------|-------------|
| ≥80% | PASS | Excellent test coverage, all P0 tests passing |
| 65-79% | CONCERNS | Acceptable coverage but gaps in P0/P1 tests |
| <65% | FAIL | Insufficient test coverage, P0 tests failing or missing |

### Calculation Example

**Scenario:**
- P0 tests: 8 total, 8 passing → 100%
- P1 tests: 12 total, 10 implemented → 83%
- Line coverage: 85%

**Calculation:**
```
Test Coverage Score = (100 × 0.5) + (83 × 0.3) + (85 × 0.2)
                    = 50 + 24.9 + 17
                    = 91.9%

Status: PASS (≥80%)
Weighted Contribution: 91.9 × 0.20 = 18.4 points
```

### Gap Identification

Gaps in test coverage:
- **Critical:** P0 tests not passing (blocks gate)
- **High:** P1 tests not implemented, coverage <70% on critical paths
- **Medium:** P2 tests missing, coverage 70-80% overall

---

## Traceability Dimension

**Weight:** 20% (default)

**Purpose:** Evaluate requirements traceability from traceability assessment.

### Data Required

From trace-requirements assessment:
```yaml
traceability:
  totalAC: 8                    # Total acceptance criteria

  # Implementation status
  implemented: 7                 # Fully implemented
  partial: 1                     # Partially implemented
  notImplemented: 0              # Not implemented

  # Test status
  tested: 7                      # Fully tested
  partialTests: 1                # Partially tested
  notTested: 0                   # Not tested

  # Coverage percentages
  implementationCoverage: 87.5%  # (impl + 0.5×partial) / total
  testCoverage: 87.5%            # (tested + 0.5×partial) / total
  traceabilityScore: 87.5%       # Composite score

  # Gaps
  gaps:
    critical: 0
    high: 1
    medium: 2
    low: 0
```

### Scoring Formula

```
Traceability Score = (
  (Implementation Coverage × 0.5) +
  (Test Coverage × 0.4) +
  (Gap Coverage × 0.1)
)

Where:
- Implementation Coverage = (Fully impl + 0.5×Partial) / Total AC × 100%
- Test Coverage = (Fully tested + 0.5×Partial) / Total AC × 100%
- Gap Coverage = 100% - (Critical×30% + High×20% + Medium×10%)
```

### Status Thresholds

| Score Range | Status | Description |
|-------------|--------|-------------|
| ≥80% | PASS | Excellent traceability, all AC implemented and tested |
| 65-79% | CONCERNS | Acceptable traceability but some AC gaps |
| <65% | FAIL | Insufficient traceability, AC not implemented or tested |

### Calculation Example

**Scenario:**
- Implementation coverage: 87.5%
- Test coverage: 87.5%
- Gaps: 0 critical, 1 high, 2 medium
- Gap coverage: 100% - (0×30% + 1×20% + 2×10%) = 60%

**Calculation:**
```
Traceability Score = (87.5 × 0.5) + (87.5 × 0.4) + (60 × 0.1)
                   = 43.75 + 35 + 6
                   = 84.75%

Status: PASS (≥80%)
Weighted Contribution: 84.75 × 0.20 = 16.95 points
```

### Gap Identification

Gaps in traceability:
- **Critical:** AC not implemented at all (0% implementation)
- **High:** AC not tested, partial implementation without tests
- **Medium:** Partial implementation or partial tests, missing evidence

---

## NFR Dimension

**Weight:** 25% (default, tied for highest)

**Purpose:** Evaluate non-functional requirements from NFR assessment.

### Data Required

From nfr-assess assessment:
```yaml
nfr:
  overallScore: 72%              # Overall NFR score (weighted average)

  # Category scores
  categories:
    security: 70%
    performance: 80%
    reliability: 65%
    maintainability: 75%
    scalability: 70%
    usability: 70%

  # Gaps by severity
  gaps:
    critical: 2                   # Critical gaps (P0)
    high: 4                       # High gaps (P1)
    medium: 3                     # Medium gaps (P2)
    low: 1                        # Low gaps (P3)

  # Critical gaps by category
  criticalGapsByCategory:
    security: 1                   # Critical security gap
    reliability: 1                # Critical reliability gap
    other: 0                      # No critical gaps in other categories
```

### Scoring Formula

```
NFR Score = Overall NFR Score from assessment (no additional calculation)

The NFR assessment already performs weighted calculation across 6 categories:
  Security × 0.25 +
  Performance × 0.20 +
  Reliability × 0.20 +
  Maintainability × 0.15 +
  Scalability × 0.10 +
  Usability × 0.10
```

### Status Thresholds

| Score Range | Status | Description |
|-------------|--------|-------------|
| ≥75% | PASS | Excellent NFR quality across all categories |
| 60-74% | CONCERNS | Acceptable NFR quality but some gaps |
| <60% | FAIL | Insufficient NFR quality, critical gaps present |

**Special Rules (Production Blockers):**
- Security <50% → FAIL (regardless of overall score)
- Reliability <50% → FAIL (regardless of overall score)
- Critical security gap → CONCERNS or FAIL
- Critical reliability gap → CONCERNS

### Calculation Example

**Scenario:**
- Overall NFR score: 72%
- Security: 70% (CONCERNS)
- Reliability: 65% (CONCERNS)
- Critical security gaps: 1
- Critical reliability gaps: 1

**Evaluation:**
```
NFR Score = 72% (from NFR assessment)

Status Determination:
- Overall score: 72% → CONCERNS range (60-74%)
- Security: 70% → Above 50% threshold ✓
- Reliability: 65% → Above 50% threshold ✓
- Critical security gaps: 1 → Triggers CONCERNS (or FAIL)
- Critical reliability gaps: 1 → Triggers CONCERNS

Final Status: CONCERNS (due to critical gaps + score in CONCERNS range)
Weighted Contribution: 72 × 0.25 = 18 points
```

### Gap Identification

Gaps in NFR:
- **Critical:** Security <50%, Reliability <50%, critical security/reliability gaps
- **High:** Category scores <75%, high-severity gaps in critical categories
- **Medium:** Category scores 75-85%, high-severity gaps in non-critical categories

---

## Implementation Quality Dimension

**Weight:** 5% (default, lowest weight)

**Purpose:** Evaluate implementation quality from task specification and implementation record.

### Data Required

From task specification:
```yaml
implementation:
  status: Review                 # Draft, In Progress, Review, Complete
  filesChanged: 12
  linesAdded: 450
  linesDeleted: 80

  implementationRecord:
    complete: true               # All implementation tasks completed
    tested: true                 # Tests written and passing
    documented: partial          # Some documentation exists
    reviewed: false              # Code review not yet done
```

### Scoring Formula

```
Implementation Quality Score = (
  (Task Completion × 0.4) +
  (Testing × 0.3) +
  (Documentation × 0.2) +
  (Code Review × 0.1)
)

Where:
- Task Completion = Implementation record completion percentage
- Testing = Tests written and passing (binary: 100% if true, 0% if false)
- Documentation = Documentation completeness (0-100%)
- Code Review = Code review status (100% if approved, 50% if in review, 0% if not reviewed)
```

### Status Thresholds

| Score Range | Status | Description |
|-------------|--------|-------------|
| ≥70% | PASS | Implementation complete with tests and documentation |
| 50-69% | CONCERNS | Implementation mostly complete but gaps in testing/docs |
| <50% | FAIL | Implementation incomplete or untested |

### Calculation Example

**Scenario:**
- Task completion: 100% (all tasks done)
- Testing: 100% (tests written and passing)
- Documentation: 50% (some docs, not complete)
- Code review: 0% (not yet reviewed)

**Calculation:**
```
Implementation Quality Score = (100 × 0.4) + (100 × 0.3) + (50 × 0.2) + (0 × 0.1)
                             = 40 + 30 + 10 + 0
                             = 80%

Status: PASS (≥70%)
Weighted Contribution: 80 × 0.05 = 4 points
```

### Gap Identification

Gaps in implementation quality:
- **Critical:** Implementation incomplete, tests not written or failing
- **High:** Documentation missing, code review not done
- **Medium:** Partial documentation, code review in progress

---

## Compliance Dimension

**Weight:** 5% (default, lowest weight)

**Purpose:** Evaluate compliance with standards, policies, and regulatory requirements.

### Data Required

From project configuration and assessments:
```yaml
compliance:
  standards:
    - OWASP Top 10 (security)
    - WCAG 2.1 AA (accessibility, if UI)
    - REST API Best Practices
    - Company Coding Standards

  policies:
    - Security Review Required: true
    - Privacy Review Required: false
    - Legal Review Required: false

  # Extracted from assessments
  standardsMet:
    - OWASP Top 10: Addressed in NFR (Security: 70%) → PASS
    - REST API Best Practices: Addressed in NFR (Usability: 70%) → PASS
    - Company Coding Standards: Linting passed → PASS

  policiesMet:
    - Security Review: Not done → FAIL
```

### Scoring Formula

```
Compliance Score = (Requirements Met / Total Requirements) × 100%

Where:
- Requirements = Standards + Policies
- Met = Requirements with evidence of compliance
```

### Status Thresholds

| Score Range | Status | Description |
|-------------|--------|-------------|
| 100% | PASS | Fully compliant with all standards and policies |
| 90-99% | CONCERNS | Minor compliance gaps (1-2 items not met) |
| <90% | FAIL | Significant compliance issues (3+ items not met) |

### Calculation Example

**Scenario:**
- Total requirements: 4 (3 standards + 1 policy)
- Standards met: 3/3
- Policies met: 0/1 (security review not done)
- Total met: 3/4

**Calculation:**
```
Compliance Score = 3/4 × 100% = 75%

Status: FAIL (<90%)
Weighted Contribution: 75 × 0.05 = 3.75 points
```

### Gap Identification

Gaps in compliance:
- **Critical:** Required policy not met (security review, legal review)
- **High:** Standards not addressed (OWASP, WCAG)
- **Medium:** Best practices not followed (coding standards)

---

## Dimension Weight Configuration

Dimension weights are configurable in `.claude/config.yaml`:

### Default Weights

```yaml
gate:
  weights:
    riskManagement: 25%        # Highest: Risk management critical
    nfr: 25%                   # Highest: Quality attributes critical
    testCoverage: 20%          # High: Test strategy important
    traceability: 20%          # High: Requirements coverage important
    implementationQuality: 5%  # Low: Already covered by other dimensions
    compliance: 5%             # Low: Usually pass/fail, not granular
```

**Total must sum to 100%**

### Weight Customization by Project Type

**Security-Critical Project (Banking, Healthcare):**
```yaml
weights:
  nfr: 35%                     # Emphasize NFR (especially security)
  riskManagement: 30%          # Emphasize risk management
  testCoverage: 15%
  traceability: 15%
  compliance: 5%
  implementationQuality: 0%    # Remove (covered by NFR)
```

**High-Traffic Consumer App:**
```yaml
weights:
  nfr: 30%                     # Emphasize NFR (especially performance)
  testCoverage: 25%            # Emphasize testing
  traceability: 20%
  riskManagement: 20%
  implementationQuality: 5%
  compliance: 0%               # Remove if not applicable
```

**Internal Tool:**
```yaml
weights:
  traceability: 30%            # Emphasize functional correctness
  testCoverage: 25%            # Emphasize testing
  implementationQuality: 20%   # Emphasize code quality
  nfr: 20%                     # Reduce NFR weight
  riskManagement: 5%
  compliance: 0%
```

### Dimension Minimum Thresholds

Each dimension has a minimum threshold (must meet to pass gate):

```yaml
gate:
  thresholds:
    riskManagement: 50%        # Must have basic risk management
    testCoverage: 65%          # Must have decent test coverage
    traceability: 65%          # Must have decent AC coverage
    nfr: 60%                   # Must have acceptable quality
    implementationQuality: 50% # Must be mostly complete
    compliance: 90%            # Must be nearly fully compliant
```

**Special Thresholds (Production Blockers):**
- Security (NFR category) <50% → FAIL
- Reliability (NFR category) <50% → FAIL

---

*This reference provides comprehensive dimension scoring methodology for quality gates.*
