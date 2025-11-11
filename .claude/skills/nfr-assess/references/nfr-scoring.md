# NFR Assessment Scoring Methodology

This reference provides detailed scoring methodology, weighting formulas, status determination thresholds, and integration of automated checks for NFR assessment.

---

## Table of Contents

1. [Criterion-Level Scoring](#criterion-level-scoring)
2. [Category-Level Scoring](#category-level-scoring)
3. [Overall NFR Score Calculation](#overall-nfr-score-calculation)
4. [Status Determination](#status-determination)
5. [Scoring Examples](#scoring-examples)
6. [Automated Check Integration](#automated-check-integration)
7. [Custom Threshold Configuration](#custom-threshold-configuration)

---

## Criterion-Level Scoring

Each individual criterion within a category is scored using a 4-point scale:

### Scoring Scale

| Status | Score | Points | Description |
|--------|-------|--------|-------------|
| ✅ PASS | 100 | Full | Criterion fully met with strong evidence |
| ⚠️ CONCERNS | 50 | Half | Criterion partially met, some gaps exist |
| ❌ FAIL | 0 | None | Criterion not met, critical issue present |
| ❓ UNCLEAR | null | Excluded | Insufficient evidence to assess (excluded from calculation) |

### Scoring Guidelines

**PASS (100 points):**
- Criterion is fully satisfied
- Strong evidence provided (code, configuration, test results)
- No significant gaps or concerns
- Meets or exceeds best practices

**CONCERNS (50 points):**
- Criterion is partially satisfied
- Some evidence provided but incomplete
- Minor gaps exist that should be addressed
- Meets minimum requirements but not best practices

**FAIL (0 points):**
- Criterion is not satisfied
- No evidence or evidence shows critical issues
- Significant gaps that pose risks
- Does not meet minimum requirements

**UNCLEAR (excluded):**
- Cannot determine if criterion is met
- Insufficient evidence to make assessment
- Not applicable to this task/project
- Excluded from score calculation to avoid penalizing unknowns

---

## Category-Level Scoring

Each NFR category (Security, Performance, Reliability, Maintainability, Scalability, Usability) has 10 criteria. The category score is calculated as the average of all assessed criteria.

### Category Score Formula

```
Category Score = (Σ Criterion Points) / (Total Assessed Criteria)

Where:
- Σ Criterion Points = Sum of all PASS (100), CONCERNS (50), FAIL (0)
- Total Assessed Criteria = Count of PASS + CONCERNS + FAIL (excludes UNCLEAR)
```

### Example: Security Category

```
Criteria Assessment:
1. Authentication: PASS (100)
2. Authorization: PASS (100)
3. Input Validation: CONCERNS (50)
4. Output Encoding: PASS (100)
5. Dependency Vulnerabilities: FAIL (0)
6. Secrets Management: PASS (100)
7. HTTPS/TLS: UNCLEAR (excluded)
8. Rate Limiting: CONCERNS (50)
9. CORS: PASS (100)
10. Security Headers: CONCERNS (50)

Calculation:
Total Points = 100 + 100 + 50 + 100 + 0 + 100 + 50 + 100 + 50 = 650
Assessed Criteria = 9 (excluding UNCLEAR)
Security Score = 650 / 9 = 72.2%
```

### Category Status Determination

Based on the category score:

| Score Range | Status | Description |
|-------------|--------|-------------|
| ≥75% | ✅ PASS | Category meets requirements |
| 50-74% | ⚠️ CONCERNS | Category has gaps needing attention |
| <50% | ❌ FAIL | Category has critical issues |

---

## Overall NFR Score Calculation

The overall NFR score is a weighted average of all 6 category scores. Different categories have different weights based on their typical impact on system quality.

### Default Category Weights

```yaml
Security: 25%          # Highest weight - production blocker if failed
Performance: 20%       # High weight - direct user impact
Reliability: 20%       # High weight - system stability critical
Maintainability: 15%   # Medium weight - long-term health
Scalability: 10%       # Lower weight - may not be immediate concern
Usability: 10%         # Lower weight - developer experience
```

### Overall Score Formula

```
Overall NFR Score = (
  Security Score × 0.25 +
  Performance Score × 0.20 +
  Reliability Score × 0.20 +
  Maintainability Score × 0.15 +
  Scalability Score × 0.10 +
  Usability Score × 0.10
)
```

### Example: Overall NFR Calculation

```
Category Scores:
- Security: 72% (CONCERNS)
- Performance: 85% (PASS)
- Reliability: 65% (CONCERNS)
- Maintainability: 80% (PASS)
- Scalability: 70% (CONCERNS)
- Usability: 68% (CONCERNS)

Calculation:
Overall NFR Score = (72 × 0.25) + (85 × 0.20) + (65 × 0.20) + (80 × 0.15) + (70 × 0.10) + (68 × 0.10)
                  = 18.0 + 17.0 + 13.0 + 12.0 + 7.0 + 6.8
                  = 73.8%

Overall Status: CONCERNS (60-74% range)
```

---

## Status Determination

### Overall NFR Status Thresholds

| Score Range | Status | Grade | Description |
|-------------|--------|-------|-------------|
| ≥90% | ✅ PASS | Excellent | Outstanding quality across all categories |
| 75-89% | ✅ PASS | Good | Solid quality, minor improvements possible |
| 60-74% | ⚠️ CONCERNS | Needs Improvement | Significant gaps requiring attention |
| <60% | ❌ FAIL | Critical Issues | Multiple critical gaps, not production-ready |

### Status Reasoning

**PASS (Excellent: ≥90%):**
- All categories performing well
- No critical gaps
- Best practices followed throughout
- Production-ready with high confidence

**PASS (Good: 75-89%):**
- Most categories performing well
- Some minor gaps but manageable
- Meets production requirements
- Can merge with confidence

**CONCERNS (60-74%):**
- Multiple categories with gaps
- Some critical gaps may exist
- Requires remediation before production
- Should address P0 gaps before merge

**FAIL (<60%):**
- Critical failures in multiple categories
- Security or reliability blockers present
- Not production-ready
- Must fix critical issues before merge

### Category-Specific Thresholds for Quality Gate Blocking

Some categories are more critical than others for production readiness:

| Category | Threshold | Impact if Below |
|----------|-----------|-----------------|
| Security | <50% | ❌ FAIL - Production blocker |
| Reliability | <50% | ❌ FAIL - Production blocker |
| Performance | <50% | ⚠️ CONCERNS - May need optimization |
| Maintainability | <50% | ⚠️ CONCERNS - Technical debt concern |
| Scalability | <40% | ⚠️ CONCERNS - May not scale (if needed) |
| Usability | <40% | ⚠️ CONCERNS - Poor developer experience |

**Reasoning:**
- **Security <50%**: Critical security vulnerabilities pose immediate risk to production
- **Reliability <50%**: System instability will cause production incidents
- **Performance <50%**: Poor performance impacts user experience but may be acceptable initially
- Other categories below 50%: Concerns but may not block initial release

---

## Scoring Examples

### Example 1: High-Quality API Implementation

**Category Scores:**
- Security: 95% (9/10 PASS, 1/10 CONCERNS)
- Performance: 90% (8/10 PASS, 2/10 CONCERNS)
- Reliability: 88% (8/10 PASS, 1/10 CONCERNS, 1/10 UNCLEAR)
- Maintainability: 85% (7/10 PASS, 3/10 CONCERNS)
- Scalability: 80% (7/10 PASS, 2/10 CONCERNS, 1/10 UNCLEAR)
- Usability: 75% (6/10 PASS, 3/10 CONCERNS, 1/10 FAIL)

**Overall Score:**
```
(95 × 0.25) + (90 × 0.20) + (88 × 0.20) + (85 × 0.15) + (80 × 0.10) + (75 × 0.10)
= 23.75 + 18.0 + 17.6 + 12.75 + 8.0 + 7.5
= 87.6%
```

**Status:** ✅ PASS (Good) - Ready for production with minor improvements recommended

---

### Example 2: Implementation with Security Concerns

**Category Scores:**
- Security: 45% (4/10 PASS, 3/10 CONCERNS, 3/10 FAIL)
- Performance: 80% (7/10 PASS, 3/10 CONCERNS)
- Reliability: 70% (6/10 PASS, 3/10 CONCERNS, 1/10 FAIL)
- Maintainability: 75% (6/10 PASS, 4/10 CONCERNS)
- Scalability: 65% (5/10 PASS, 4/10 CONCERNS, 1/10 FAIL)
- Usability: 60% (5/10 PASS, 4/10 CONCERNS, 1/10 FAIL)

**Overall Score:**
```
(45 × 0.25) + (80 × 0.20) + (70 × 0.20) + (75 × 0.15) + (65 × 0.10) + (60 × 0.10)
= 11.25 + 16.0 + 14.0 + 11.25 + 6.5 + 6.0
= 65.0%
```

**Status:** ❌ FAIL - Security <50% is production blocker, despite overall score of 65%

**Key Issue:** Security score below 50% threshold triggers automatic FAIL regardless of overall score

---

### Example 3: Solid Implementation with Documentation Gaps

**Category Scores:**
- Security: 85% (8/10 PASS, 1/10 CONCERNS, 1/10 FAIL)
- Performance: 78% (7/10 PASS, 2/10 CONCERNS, 1/10 FAIL)
- Reliability: 82% (7/10 PASS, 3/10 CONCERNS)
- Maintainability: 60% (4/10 PASS, 5/10 CONCERNS, 1/10 FAIL) - Low due to missing documentation
- Scalability: 70% (5/10 PASS, 5/10 CONCERNS)
- Usability: 55% (4/10 PASS, 4/10 CONCERNS, 2/10 FAIL) - Low due to missing API docs

**Overall Score:**
```
(85 × 0.25) + (78 × 0.20) + (82 × 0.20) + (60 × 0.15) + (70 × 0.10) + (55 × 0.10)
= 21.25 + 15.6 + 16.4 + 9.0 + 7.0 + 5.5
= 74.75%
```

**Status:** ⚠️ CONCERNS - Just below 75% PASS threshold, documentation gaps holding back score

**Recommendation:** Add documentation (README, API docs) to push Maintainability and Usability above 75%, which would increase overall score to ~78% (PASS)

---

## Automated Check Integration

Many NFR criteria can be assessed automatically. Automated checks provide objective, reproducible metrics.

### Security Automated Checks

#### Dependency Vulnerability Scan

**Tool:** `npm audit`, `snyk`, `OWASP Dependency Check`

**Scoring Rules:**
```yaml
Critical Vulnerabilities:
  0: Contributes to PASS
  1+: Automatically FAIL criterion

High Vulnerabilities:
  0-2: Contributes to PASS
  3-5: Contributes to CONCERNS
  6+: Contributes to FAIL
```

**Example:**
```json
{
  "vulnerabilities": {
    "critical": 0,
    "high": 3,
    "moderate": 12,
    "low": 25
  }
}
```
→ 0 critical, 3 high = **CONCERNS** (50 points) for "Dependency Vulnerabilities" criterion

---

### Performance Automated Checks

#### Load Test Results

**Tool:** `artillery`, `k6`, `ab`, `wrk`

**Scoring Rules:**
```yaml
Response Time (p95):
  < threshold: Contributes to PASS
  threshold to 2×threshold: Contributes to CONCERNS
  > 2×threshold: Contributes to FAIL

Default threshold: 500ms

Success Rate:
  ≥99%: Contributes to PASS
  95-98%: Contributes to CONCERNS
  <95%: Contributes to FAIL
```

**Example:**
```json
{
  "latency": {
    "avg": 120,
    "p50": 100,
    "p95": 350,
    "p99": 650
  },
  "successRate": 99.8
}
```
→ p95 (350ms) < threshold (500ms), success rate 99.8% = **PASS** (100 points) for "Response Time" criterion

---

### Maintainability Automated Checks

#### Test Coverage

**Tool:** `jest --coverage`, `nyc`, `pytest-cov`

**Scoring Rules:**
```yaml
Line Coverage:
  ≥80%: Contributes to PASS
  60-79%: Contributes to CONCERNS
  <60%: Contributes to FAIL

Critical Path Coverage (if measurable):
  ≥90%: Contributes to PASS
  75-89%: Contributes to CONCERNS
  <75%: Contributes to FAIL
```

**Example:**
```json
{
  "total": {
    "lines": { "pct": 85 },
    "statements": { "pct": 87 },
    "functions": { "pct": 90 },
    "branches": { "pct": 82 }
  }
}
```
→ 85% line coverage ≥80% = **PASS** (100 points) for "Test Coverage" criterion

---

#### Linting

**Tool:** `eslint`, `pylint`, `rubocop`

**Scoring Rules:**
```yaml
Errors:
  0: Contributes to PASS
  1-5: Contributes to CONCERNS
  6+: Contributes to FAIL

Warnings (less impactful):
  0-10: Does not impact score
  11-30: May contribute to CONCERNS
  31+: Contributes to CONCERNS
```

**Example:**
```json
{
  "errorCount": 2,
  "warningCount": 15
}
```
→ 2 errors (1-5 range) = **CONCERNS** (50 points) for "Code Quality" criterion

---

#### Complexity Analysis

**Tool:** `complexity-report`, `radon`, `lizard`

**Scoring Rules:**
```yaml
Average Cyclomatic Complexity:
  ≤5: Contributes to PASS
  6-10: Contributes to CONCERNS
  >10: Contributes to FAIL

Max Complexity (worst function):
  ≤10: Does not impact score
  11-15: Contributes to CONCERNS
  >15: Contributes to FAIL
```

**Example:**
```json
{
  "avgComplexity": 4.2,
  "maxComplexity": 15,
  "functionsAbove10": 2
}
```
→ Avg complexity 4.2 (good) but max complexity 15 (11-15 range) = **CONCERNS** (50 points) for "Complexity" criterion

---

## Custom Threshold Configuration

Projects can customize NFR thresholds in `.claude/config.yaml`:

### Example Configuration

```yaml
quality:
  qualityLocation: .claude/quality
  riskScoreThreshold: 6

nfr:
  # Custom category weights (must sum to 1.0)
  weights:
    security: 0.30        # Increase security weight for security-critical system
    performance: 0.25     # Increase performance weight for high-traffic system
    reliability: 0.20
    maintainability: 0.10
    scalability: 0.10
    usability: 0.05

  # Security thresholds
  security:
    vulnerabilityScanRequired: true
    maxCriticalVulns: 0
    maxHighVulns: 2
    maxModerateVulns: 10

  # Performance thresholds
  performance:
    maxResponseTime: 300ms       # Stricter than default 500ms
    minThroughput: 200 req/s     # Higher than default 100 req/s
    maxMemoryUsage: 256MB        # Lower than default 512MB

  # Maintainability thresholds
  maintainability:
    minTestCoverage: 85%         # Stricter than default 80%
    maxCyclomaticComplexity: 8   # Stricter than default 10
    maxFunctionLength: 40        # Stricter than default 50

  # Reliability thresholds
  reliability:
    healthCheckRequired: true
    monitoringRequired: true
    structuredLoggingRequired: true

  # Scalability thresholds (optional)
  scalability:
    statelessRequired: true
    asyncProcessingRequired: true

  # Usability thresholds (optional)
  usability:
    apiDocumentationRequired: true
    wcagComplianceRequired: true  # If UI
```

### Using Custom Thresholds

When custom thresholds are defined:
1. Load thresholds from config during Step 0
2. Use custom thresholds in automated checks
3. Document custom thresholds in assessment report
4. Compare results against custom thresholds (not defaults)

**Example:**
```
Default: Performance response time threshold 500ms
Custom: Performance response time threshold 300ms

Load test result: p95 = 350ms

Default scoring: 350 < 500 → PASS
Custom scoring: 350 > 300 → CONCERNS

Result: CONCERNS (50 points) due to custom threshold
```

---

## Weighting Customization by Project Type

Different project types may benefit from different category weights:

### Security-Critical System (Banking, Healthcare)
```yaml
security: 0.35      # Highest priority
reliability: 0.25   # Critical for data integrity
performance: 0.15
maintainability: 0.10
scalability: 0.10
usability: 0.05
```

### High-Traffic Consumer App
```yaml
performance: 0.30   # User experience critical
scalability: 0.25   # Must handle growth
security: 0.20
reliability: 0.15
usability: 0.05
maintainability: 0.05
```

### Internal Tool / Admin Dashboard
```yaml
maintainability: 0.25  # Long-term maintenance important
usability: 0.25        # Developer productivity
reliability: 0.20
security: 0.15         # Still important but less critical
performance: 0.10
scalability: 0.05
```

### Public API
```yaml
reliability: 0.30   # Uptime critical for customers
usability: 0.25     # Developer experience drives adoption
performance: 0.20
security: 0.15
maintainability: 0.05
scalability: 0.05
```

---

*This reference provides comprehensive scoring methodology for NFR assessment.*
