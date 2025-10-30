# Skill: Quality Gate Decision

## Metadata

**Skill Name:** quality-gate
**Version:** 1.0
**Category:** Quality
**Purpose:** Synthesize all quality assessments (risk, test-design, traceability, NFR) and make evidence-based quality gate decision (PASS/CONCERNS/FAIL/WAIVED) with comprehensive rationale and action items
**Output:** `.claude/quality/gates/{task-id}-gate-{YYYYMMDD}.yaml` (structured) and `.claude/quality/gates/{task-id}-gate-{YYYYMMDD}.md` (human-readable)

---

## Overview

This skill performs the **final quality gate assessment** by synthesizing all previous quality evaluations and making an evidence-based decision on whether the implementation is ready to proceed (merge, deploy, release).

**Key Capabilities:**
- Synthesizes 4 quality assessments: risk, test-design, traceability, NFR
- Applies configurable quality gate criteria
- Multi-dimensional scoring across 6 quality dimensions
- Evidence-based decision with clear rationale
- Action items for CONCERNS/FAIL outcomes
- Waiver support with justification tracking
- Audit trail for compliance
- Integration with CI/CD (YAML output for automation)

**Quality Gate Decisions:**
- ✅ **PASS**: All quality criteria met, ready to proceed
- ⚠️ **CONCERNS**: Some quality issues identified, but can proceed with caveats
- ❌ **FAIL**: Critical quality issues, must fix before proceeding
- 🟡 **WAIVED**: Quality issues acknowledged and waived with justification

**Quality Dimensions:**
1. **Risk Management**: Risks identified, scored, mitigated (from risk-profile)
2. **Test Coverage**: Comprehensive test strategy with P0/P1/P2 tests (from test-design)
3. **Requirements Traceability**: AC → Implementation → Tests chain (from trace-requirements)
4. **Non-Functional Requirements**: Security, performance, reliability, etc. (from nfr-assess)
5. **Implementation Quality**: Code quality, completeness, documentation
6. **Compliance**: Standards, policies, regulatory requirements

**When to Use:**
- After all quality assessments complete (risk, test-design, trace, nfr)
- Before merge/deploy/release decision
- As final checkpoint in quality process
- For audit and compliance documentation

**Integration Points:**
- Reads all quality assessment reports
- Reads task specification for requirements
- Reads project configuration for gate criteria
- Generates YAML output for CI/CD automation
- Generates markdown report for human review

---

## Execution Process

This skill executes **sequentially** through 8 steps. Each step must complete successfully before proceeding to the next.

### Halt Conditions
- Task specification file not found
- Required assessments missing (minimum: traceability or NFR)
- Output directory not writable

---

## Step 0: Load Configuration and Assessments

**Purpose:** Load project configuration, task specification, and all quality assessment reports.

**Actions:**

1. **Load Project Configuration**
   ```yaml
   # Read .claude/config.yaml
   quality:
     qualityLocation: .claude/quality
     gateThreshold: CONCERNS        # Minimum level to pass gate
     riskScoreThreshold: 6           # Risk scores ≥6 are high-risk
     requireAllAssessments: false    # If true, all 4 assessments required

   gate:
     # Quality dimension weights (must sum to 100%)
     weights:
       riskManagement: 25%
       testCoverage: 20%
       traceability: 20%
       nfr: 25%
       implementationQuality: 5%
       compliance: 5%

     # Dimension thresholds (PASS if ≥ threshold)
     thresholds:
       riskManagement: 75%
       testCoverage: 80%
       traceability: 80%
       nfr: 75%
       implementationQuality: 70%
       compliance: 90%

     # Critical gap rules
     criticalGapRules:
       securityGaps: FAIL            # Any critical security gap → FAIL
       reliabilityGaps: CONCERNS      # Any critical reliability gap → CONCERNS
       otherGaps: PASS                # Other critical gaps → PASS (with action items)

     # Waiver rules
     waiverAllowed: true
     waiverRequiresJustification: true
     waiverRequiresApprover: false
   ```

2. **Load Task Specification**
   ```bash
   TASK_FILE=".claude/tasks/{task-id}-{slug}.md"
   ```
   Extract:
   - Task ID, title, type
   - Objective, acceptance criteria
   - Implementation status
   - Quality requirements

3. **Load Quality Assessments**
   ```bash
   # Find latest assessments for this task
   RISK_FILE=".claude/quality/assessments/{task-id}-risk-{latest-date}.md"
   TEST_FILE=".claude/quality/assessments/{task-id}-test-design-{latest-date}.md"
   TRACE_FILE=".claude/quality/assessments/{task-id}-trace-{latest-date}.md"
   NFR_FILE=".claude/quality/assessments/{task-id}-nfr-{latest-date}.md"
   ```

   **For each assessment:**
   - Extract overall score/status
   - Extract critical/high gaps
   - Extract recommendations
   - Extract evidence and metrics

   **Minimum Requirements:**
   - At least one of: traceability OR nfr (functional correctness OR quality attributes)
   - Recommended: All 4 assessments for comprehensive gate

4. **Check Assessment Availability:**
   ```
   Available Assessments:
   ├─ Risk Profile: [✓ Available | ✗ Missing]
   ├─ Test Design: [✓ Available | ✗ Missing]
   ├─ Traceability: [✓ Available | ✗ Missing]
   └─ NFR Assessment: [✓ Available | ✗ Missing]

   Minimum met: [Yes | No]
   ```

5. **Load Waiver Requests** (if any)
   ```yaml
   # Check if task file has waiver section
   waiverRequests:
     - gap: GAP-SEC-1
       justification: "Rate limiting to be added in phase 2"
       requestedBy: "Tech Lead"
       approvedBy: null
       status: pending
   ```

6. **Prepare Output**
   ```bash
   OUTPUT_DIR="{qualityLocation}/gates"
   OUTPUT_YAML="{task-id}-gate-{YYYYMMDD}.yaml"
   OUTPUT_MD="{task-id}-gate-{YYYYMMDD}.md"
   ```

**Halt If:**
- Config file missing or invalid
- Task file not found
- Minimum assessments not available (if requireAllAssessments: true and not all present)
- Cannot create output directory

**Output:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: {task-id} - {title}
✓ Quality assessments loaded:
  ├─ Risk Profile: {available} (Score: {score}, Date: {date})
  ├─ Test Design: {available} ({test_count} tests, Date: {date})
  ├─ Traceability: {available} (Score: {score}%, Date: {date})
  └─ NFR Assessment: {available} (Score: {score}%, Date: {date})
✓ Waiver requests: {count}
✓ Output: {output-yaml}, {output-md}
```

---

## Step 1: Synthesize Risk Management Dimension

**Purpose:** Evaluate risk management effectiveness from risk profile assessment.

**Actions:**

1. **Load Risk Profile Data** (if available)
   ```yaml
   riskProfile:
     totalRisks: 12
     criticalRisks: 1  # Score ≥7
     highRisks: 3      # Score ≥6
     mediumRisks: 5
     lowRisks: 3
     highRisksMitigated: 2/4  # (critical + high) with mitigation
     highRisksTested: 3/4     # (critical + high) with tests
   ```

2. **Calculate Risk Management Score:**
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

   Example:
   - Critical: 1, High: 3 → Total high-risk: 4
   - Mitigated: 2/4 = 50%
   - Tested: 3/4 = 75%
   - Distribution: 100% - (1×20% + 3×10%) = 50%

   Score = (50 × 0.5) + (75 × 0.3) + (50 × 0.2)
        = 25 + 22.5 + 10
        = 57.5%
   ```

3. **Determine Risk Management Status:**
   ```
   Status = [PASS | CONCERNS | FAIL] based on threshold
   - ≥75%: PASS
   - 50-74%: CONCERNS
   - <50%: FAIL
   ```

4. **Identify Risk Management Gaps:**
   - Critical risks without mitigation
   - High risks without tests
   - High risk scores (≥6) in critical areas

5. **Risk Management Contribution to Gate:**
   ```
   Weight: 25% (from config)
   Score: 57.5%
   Weighted Score: 57.5 × 0.25 = 14.4 points
   ```

**If Risk Profile Not Available:**
```
Risk Management Dimension: N/A
Note: Risk profile assessment not performed. Assuming acceptable risk management.
Weighted Score: 0 (dimension weight redistributed to other dimensions)
```

**Output:**
```
✓ Risk Management dimension synthesized
✓ Score: {score}% ({status})
✓ Critical Risks: {count} ({mitigated_count} mitigated)
✓ High Risks: {count} ({tested_count} tested)
✓ Contribution to Gate: {weighted_score} points
```

---

## Step 2: Synthesize Test Coverage Dimension

**Purpose:** Evaluate test strategy and coverage from test-design assessment.

**Actions:**

1. **Load Test Design Data** (if available)
   ```yaml
   testDesign:
     totalTests: 24
     p0Tests: 8   # Critical, must pass
     p1Tests: 12  # High, should pass
     p2Tests: 4   # Medium, nice to have
     testLevels:
       unit: 12
       integration: 10
       e2e: 2
     p0TestsImplemented: 8/8     # All P0 tests exist
     p0TestsPassing: 8/8         # All P0 tests pass
     p1TestsImplemented: 10/12   # Most P1 tests exist
     coveragePercentage: 85%     # Line coverage
   ```

2. **Calculate Test Coverage Score:**
   ```
   Test Coverage Score = (
     (P0 Tests Passing × 0.5) +
     (P1 Tests Implemented × 0.3) +
     (Coverage Percentage × 0.2)
   )

   Example:
   - P0 Passing: 8/8 = 100%
   - P1 Implemented: 10/12 = 83%
   - Coverage: 85%

   Score = (100 × 0.5) + (83 × 0.3) + (85 × 0.2)
        = 50 + 24.9 + 17
        = 91.9%
   ```

3. **Determine Test Coverage Status:**
   ```
   - ≥80%: PASS (excellent coverage)
   - 65-79%: CONCERNS (acceptable but gaps)
   - <65%: FAIL (insufficient coverage)
   ```

4. **Identify Test Coverage Gaps:**
   - P0 tests not passing
   - P1 tests not implemented
   - Coverage below threshold on critical paths

5. **Test Coverage Contribution to Gate:**
   ```
   Weight: 20%
   Score: 91.9%
   Weighted Score: 91.9 × 0.20 = 18.4 points
   ```

**If Test Design Not Available:**
```
Test Coverage Dimension: N/A
Note: Test design assessment not performed. Assuming tests exist from traceability.
Fallback: Use test coverage from traceability assessment if available.
```

**Output:**
```
✓ Test Coverage dimension synthesized
✓ Score: {score}% ({status})
✓ P0 Tests: {passing}/{total} passing
✓ Coverage: {coverage}%
✓ Contribution to Gate: {weighted_score} points
```

---

## Step 3: Synthesize Traceability Dimension

**Purpose:** Evaluate requirements traceability from traceability assessment.

**Actions:**

1. **Load Traceability Data** (if available)
   ```yaml
   traceability:
     totalAC: 8
     implemented: 7
     partial: 1
     notImplemented: 0
     tested: 7
     partialTests: 1
     notTested: 0
     implementationCoverage: 87.5%  # (impl + partial) / total
     testCoverage: 87.5%            # (tested + partial) / total
     traceabilityScore: 87.5%       # Composite score
     gaps:
       critical: 0
       high: 1
       medium: 2
       low: 0
   ```

2. **Calculate Traceability Score:**
   ```
   Traceability Score = (
     (Implementation Coverage × 0.5) +
     (Test Coverage × 0.4) +
     (Gap Coverage × 0.1)
   )

   Where Gap Coverage = 100% - (Critical×30% + High×20% + Medium×10%)

   Example:
   - Implementation Coverage: 87.5%
   - Test Coverage: 87.5%
   - Gaps: 0 critical, 1 high, 2 medium
   - Gap Coverage: 100% - (0×30% + 1×20% + 2×10%) = 60%

   Score = (87.5 × 0.5) + (87.5 × 0.4) + (60 × 0.1)
        = 43.75 + 35 + 6
        = 84.75%
   ```

3. **Determine Traceability Status:**
   ```
   - ≥80%: PASS
   - 65-79%: CONCERNS
   - <65%: FAIL
   ```

4. **Identify Traceability Gaps:**
   - AC not implemented
   - AC not tested
   - Missing evidence

5. **Traceability Contribution to Gate:**
   ```
   Weight: 20%
   Score: 84.75%
   Weighted Score: 84.75 × 0.20 = 16.95 points
   ```

**If Traceability Not Available:**
```
Traceability Dimension: Required but missing
Halt: Cannot proceed with quality gate without traceability assessment
```

**Output:**
```
✓ Traceability dimension synthesized
✓ Score: {score}% ({status})
✓ Implementation Coverage: {impl_coverage}%
✓ Test Coverage: {test_coverage}%
✓ Contribution to Gate: {weighted_score} points
```

---

## Step 4: Synthesize NFR Dimension

**Purpose:** Evaluate non-functional requirements from NFR assessment.

**Actions:**

1. **Load NFR Data** (if available)
   ```yaml
   nfr:
     overallScore: 72%
     categories:
       security: 70%
       performance: 80%
       reliability: 65%
       maintainability: 75%
       scalability: 70%
       usability: 70%
     gaps:
       critical: 2  # Security, reliability
       high: 4
       medium: 3
       low: 1
     criticalGapsByCategory:
       security: 1
       reliability: 1
       other: 0
   ```

2. **NFR Score is Direct:**
   ```
   NFR Score = Overall NFR Score from assessment = 72%
   ```

3. **Determine NFR Status:**
   ```
   - ≥75%: PASS
   - 60-74%: CONCERNS
   - <60%: FAIL

   Special Rules:
   - Security <50%: FAIL (production blocker)
   - Reliability <50%: FAIL (production blocker)
   - Critical security gap: CONCERNS or FAIL
   - Critical reliability gap: CONCERNS
   ```

4. **Identify NFR Gaps:**
   - Critical gaps by category
   - Categories below 50% (production blockers)
   - High-severity gaps in security/reliability

5. **NFR Contribution to Gate:**
   ```
   Weight: 25%
   Score: 72%
   Weighted Score: 72 × 0.25 = 18 points
   ```

**If NFR Not Available:**
```
NFR Dimension: N/A
Note: NFR assessment not performed. Assuming acceptable quality attributes.
Fallback: Use implementation quality dimension (code quality, documentation) as proxy.
```

**Output:**
```
✓ NFR dimension synthesized
✓ Overall NFR Score: {score}% ({status})
✓ Security: {security_score}% ({security_status})
✓ Reliability: {reliability_score}% ({reliability_status})
✓ Critical NFR Gaps: {count}
✓ Contribution to Gate: {weighted_score} points
```

---

## Step 5: Synthesize Implementation Quality Dimension

**Purpose:** Evaluate implementation quality from task specification and code artifacts.

**Actions:**

1. **Extract Implementation Data from Task:**
   ```yaml
   implementation:
     status: Review           # Draft, In Progress, Review, Complete
     filesChanged: 12
     linesAdded: 450
     linesDeleted: 80
     implementationRecord:
       complete: true         # All tasks completed
       tested: true           # Tests written
       documented: partial    # Some documentation
   ```

2. **Calculate Implementation Quality Score:**
   ```
   Implementation Quality = (
     (Task Completion × 0.4) +
     (Testing × 0.3) +
     (Documentation × 0.2) +
     (Code Review × 0.1)
   )

   Example:
   - Task Completion: 100% (all subtasks done)
   - Testing: 100% (tests written and passing)
   - Documentation: 50% (some docs, not complete)
   - Code Review: 0% (not yet reviewed)

   Score = (100 × 0.4) + (100 × 0.3) + (50 × 0.2) + (0 × 0.1)
        = 40 + 30 + 10 + 0
        = 80%
   ```

3. **Determine Implementation Quality Status:**
   ```
   - ≥70%: PASS
   - 50-69%: CONCERNS
   - <50%: FAIL
   ```

4. **Implementation Quality Contribution to Gate:**
   ```
   Weight: 5%
   Score: 80%
   Weighted Score: 80 × 0.05 = 4 points
   ```

**Output:**
```
✓ Implementation Quality dimension synthesized
✓ Score: {score}% ({status})
✓ Task Completion: {completion}%
✓ Testing: {testing}%
✓ Documentation: {documentation}%
✓ Contribution to Gate: {weighted_score} points
```

---

## Step 6: Synthesize Compliance Dimension

**Purpose:** Evaluate compliance with standards, policies, and regulatory requirements.

**Actions:**

1. **Check Compliance Requirements:**
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
   ```

2. **Evaluate Compliance:**
   ```
   For each requirement:
   - Check if assessment addressed it
   - Extract compliance status from assessments
   - Determine pass/fail

   Example:
   - OWASP Top 10: Addressed in NFR (Security: 70%) → PASS
   - REST API Best Practices: Addressed in NFR (Usability: 70%) → PASS
   - Security Review: Required but not done → FAIL
   ```

3. **Calculate Compliance Score:**
   ```
   Compliance Score = (Requirements Met / Total Requirements) × 100%

   Example:
   - Total Requirements: 4
   - Met: 3
   - Not Met: 1 (Security Review)

   Score = 3/4 × 100% = 75%
   ```

4. **Determine Compliance Status:**
   ```
   - 100%: PASS (fully compliant)
   - 90-99%: CONCERNS (minor gaps)
   - <90%: FAIL (compliance issues)
   ```

5. **Compliance Contribution to Gate:**
   ```
   Weight: 5%
   Score: 75%
   Weighted Score: 75 × 0.05 = 3.75 points
   ```

**Output:**
```
✓ Compliance dimension synthesized
✓ Score: {score}% ({status})
✓ Standards Met: {count}/{total}
✓ Policies Met: {count}/{total}
✓ Contribution to Gate: {weighted_score} points
```

---

## Step 7: Calculate Overall Quality Score and Make Decision

**Purpose:** Synthesize all dimensions into overall quality score and make gate decision.

**Actions:**

1. **Calculate Overall Quality Score:**
   ```
   Overall Quality Score = Sum of all weighted dimension scores

   Example from Steps 1-6:
   - Risk Management: 14.4 points (57.5% × 25%)
   - Test Coverage: 18.4 points (91.9% × 20%)
   - Traceability: 16.95 points (84.75% × 20%)
   - NFR: 18 points (72% × 25%)
   - Implementation Quality: 4 points (80% × 5%)
   - Compliance: 3.75 points (75% × 5%)

   Total = 14.4 + 18.4 + 16.95 + 18 + 4 + 3.75 = 75.5%
   ```

2. **Apply Quality Gate Criteria:**
   ```yaml
   gateCriteria:
     overallScoreThreshold: 75%      # From config.gateThreshold
     dimensionMinimums:
       riskManagement: 50%            # Must be ≥50%
       testCoverage: 65%              # Must be ≥65%
       traceability: 65%              # Must be ≥65%
       nfr: 60%                       # Must be ≥60%
       implementationQuality: 50%     # Must be ≥50%
       compliance: 90%                # Must be ≥90%
     criticalGapRules:
       securityGaps: 0                # No critical security gaps
       reliabilityGaps: 1             # Max 1 critical reliability gap
   ```

3. **Evaluate Each Criterion:**
   ```yaml
   evaluation:
     overallScore: 75.5%
     overallThreshold: 75%
     overallMet: true ✓

     dimensionChecks:
       - dimension: Risk Management
         score: 57.5%
         minimum: 50%
         met: true ✓

       - dimension: Test Coverage
         score: 91.9%
         minimum: 65%
         met: true ✓

       - dimension: Traceability
         score: 84.75%
         minimum: 65%
         met: true ✓

       - dimension: NFR
         score: 72%
         minimum: 60%
         met: true ✓

       - dimension: Implementation Quality
         score: 80%
         minimum: 50%
         met: true ✓

       - dimension: Compliance
         score: 75%
         minimum: 90%
         met: false ✗ (COMPLIANCE ISSUE)

     criticalGapChecks:
       - rule: No critical security gaps
         actualGaps: 1
         met: false ✗ (SECURITY GAP)

       - rule: Max 1 critical reliability gap
         actualGaps: 1
         met: true ✓
   ```

4. **Determine Gate Decision:**
   ```
   Decision Logic:

   1. If any dimension FAIL (<50% security/reliability, or below minimum):
      → FAIL

   2. If critical security gaps > 0:
      → FAIL (or CONCERNS if waived)

   3. If overall score < threshold:
      → CONCERNS (or FAIL if significantly below)

   4. If all criteria met:
      → PASS

   5. If waiver approved:
      → WAIVED (specific gaps)

   Example Decision:
   - Overall Score: 75.5% ≥ 75% ✓
   - Dimensions: 5/6 meet minimums
   - Compliance: 75% < 90% ✗
   - Critical Security Gaps: 1 > 0 ✗

   Decision: CONCERNS
   Reason: Compliance below minimum, critical security gap present
   ```

5. **Check Waiver Requests:**
   ```yaml
   waiverRequests:
     - gap: GAP-SEC-1
       justification: "Dependency vulnerability fix scheduled for phase 2"
       approvedBy: "Tech Lead"
       status: approved
       decision: WAIVED
   ```

   If waiver approved:
   - Remove gap from critical gap count
   - Re-evaluate decision
   - Document waiver in gate report

6. **Finalize Decision:**
   ```yaml
   finalDecision:
     status: CONCERNS           # PASS | CONCERNS | FAIL | WAIVED
     overallScore: 75.5%
     reasoning: |
       Overall quality score 75.5% meets threshold (75%).
       However, compliance dimension at 75% below minimum 90%.
       Critical security gap (GAP-SEC-1) present but waived.
       Decision: CONCERNS - can proceed with action items.
     blockers: []               # Empty for CONCERNS
     actionItems:
       - Fix compliance gap: Complete security review process
       - Address compliance documentation
       - Track waived security gap for phase 2
   ```

**Output:**
```
✓ Overall Quality Score calculated: {score}%
✓ Gate Decision: {PASS/CONCERNS/FAIL/WAIVED}
✓ Criteria Met: {count}/{total}
✓ Critical Issues: {count}
✓ Action Items: {count}
```

---

## Step 8: Generate Quality Gate Reports and Present Summary

**Purpose:** Generate structured YAML and human-readable markdown reports, then present summary.

**Actions:**

1. **Generate YAML Report** (for CI/CD automation)
   ```yaml
   # .claude/quality/gates/{task-id}-gate-{YYYYMMDD}.yaml

   gate:
     task:
       id: task-007
       title: "User Authentication API"
       type: feature

     assessment:
       date: "2025-10-28"
       assessor: "Claude (Sonnet 4.5)"
       assessments:
         riskProfile: {available: true, date: "2025-10-28", score: 57.5}
         testDesign: {available: true, date: "2025-10-28", tests: 24}
         traceability: {available: true, date: "2025-10-28", score: 84.75}
         nfr: {available: true, date: "2025-10-28", score: 72}

     scores:
       overall: 75.5
       dimensions:
         riskManagement: {score: 57.5, weight: 25, weighted: 14.4, status: CONCERNS}
         testCoverage: {score: 91.9, weight: 20, weighted: 18.4, status: PASS}
         traceability: {score: 84.75, weight: 20, weighted: 16.95, status: PASS}
         nfr: {score: 72, weight: 25, weighted: 18, status: CONCERNS}
         implementationQuality: {score: 80, weight: 5, weighted: 4, status: PASS}
         compliance: {score: 75, weight: 5, weighted: 3.75, status: CONCERNS}

     decision:
       status: CONCERNS
       confidence: HIGH
       reasoning: |
         Overall quality score 75.5% meets threshold.
         Compliance dimension below minimum.
         Critical security gap waived with justification.
       blockers: []
       actionItems:
         - id: ACTION-1
           description: "Complete security review process"
           priority: P1
           owner: null
           dueDate: null
         - id: ACTION-2
           description: "Track waived security gap for phase 2"
           priority: P1
           owner: "Tech Lead"
           dueDate: "2025-11-15"

     waivers:
       - gap: GAP-SEC-1
         justification: "Dependency fix scheduled for phase 2"
         approvedBy: "Tech Lead"
         date: "2025-10-28"

     auditTrail:
       - timestamp: "2025-10-28T10:30:00Z"
         action: "Gate assessment performed"
         result: CONCERNS
         assessor: "Claude (Sonnet 4.5)"
   ```

2. **Generate Markdown Report** (for human review)
   Use `.claude/templates/quality-gate.md` template and populate all variables.

3. **Present Summary to User:**
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Quality Gate Assessment Complete
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Task: task-007 - User Authentication API
   Date: 2025-10-28

   📊 Overall Quality Score: 75.5% (⚠️ CONCERNS)

   Dimension Scores:
   ├─ Risk Management: 57.5% (⚠️ CONCERNS, 14.4 pts)
   ├─ Test Coverage: 91.9% (✅ PASS, 18.4 pts)
   ├─ Traceability: 84.75% (✅ PASS, 16.95 pts)
   ├─ NFR: 72% (⚠️ CONCERNS, 18 pts)
   ├─ Implementation Quality: 80% (✅ PASS, 4 pts)
   └─ Compliance: 75% (⚠️ CONCERNS, 3.75 pts)

   🎯 Gate Decision: ⚠️ CONCERNS

   Reasoning:
   - Overall score 75.5% meets threshold (75%) ✓
   - Test coverage and traceability excellent ✓
   - Risk management needs improvement (57.5% < 75%)
   - NFR acceptable but below ideal (72% < 75%)
   - Compliance below minimum (75% < 90%) ✗
   - Critical security gap waived (GAP-SEC-1)

   Can Proceed: YES (with action items)

   🔴 Blockers: None

   📋 Action Items (P1):
   1. Complete security review process (compliance)
   2. Track waived security gap (GAP-SEC-1) for phase 2
   3. Improve risk mitigation strategies (target 75%+)

   🟡 Waivers Granted:
   - GAP-SEC-1: Dependency vulnerability (approved by Tech Lead)

   📄 Reports Generated:
   ├─ YAML: .claude/quality/gates/task-007-gate-20251028.yaml
   └─ Markdown: .claude/quality/gates/task-007-gate-20251028.md

   💡 Next Steps:
   1. Review detailed gate report (markdown)
   2. Complete action items (P1 priority)
   3. Track waived gaps in issue tracker
   4. Proceed with merge (approved with CONCERNS)
   5. Schedule follow-up review for phase 2

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

4. **Ask User:**
   ```
   Would you like me to:
   A) Show detailed breakdown of specific dimension
   B) Generate action item tickets for tracking
   C) Update task file with gate decision
   D) Proceed with merge/deploy workflow
   ```

**Execution Complete.**

---

## Integration with CI/CD

The YAML output enables CI/CD automation:

```yaml
# .github/workflows/quality-gate.yml
name: Quality Gate

on:
  pull_request:
    types: [labeled]

jobs:
  quality-gate:
    if: github.event.label.name == 'ready-for-review'
    runs-on: ubuntu-latest
    steps:
      - name: Run quality assessments
        run: |
          # Run all quality skills
          claude-code skill risk-profile task-${{ github.event.number }}
          claude-code skill test-design task-${{ github.event.number }}
          claude-code skill trace-requirements task-${{ github.event.number }}
          claude-code skill nfr-assess task-${{ github.event.number }}
          claude-code skill quality-gate task-${{ github.event.number }}

      - name: Check gate decision
        run: |
          GATE_STATUS=$(yq '.gate.decision.status' .claude/quality/gates/task-*.yaml)
          if [ "$GATE_STATUS" = "FAIL" ]; then
            echo "Quality gate FAILED"
            exit 1
          elif [ "$GATE_STATUS" = "CONCERNS" ]; then
            echo "Quality gate CONCERNS - review required"
            # Post comment with action items
          else
            echo "Quality gate PASS"
          fi

      - name: Post gate report
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('.claude/quality/gates/task-${{ github.event.number }}-gate-*.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

---

## Decision Matrix

**Gate Status Decision Logic:**

| Overall Score | Dim Minimums | Critical Gaps | Compliance | Decision | Can Proceed? |
|---------------|--------------|---------------|------------|----------|--------------|
| ≥75% | All met | 0 | Met | ✅ PASS | Yes |
| ≥75% | All met | 0 | Not met | ⚠️ CONCERNS | Yes (with actions) |
| ≥75% | 1+ not met | 0 | Met | ⚠️ CONCERNS | Yes (with actions) |
| ≥75% | 1+ not met | 1+ | Met or not | ⚠️ CONCERNS | Yes (with actions) |
| <75% | All met | 0 | Met | ⚠️ CONCERNS | Yes (with actions) |
| <75% | 1+ not met | 0 | Not met | ⚠️ CONCERNS or ❌ FAIL | Conditional |
| <60% | Any | Any | Any | ❌ FAIL | No |
| Any | Security <50% | Any | Any | ❌ FAIL | No |
| Any | Reliability <50% | Any | Any | ❌ FAIL | No |
| Any | Any | Crit Sec Gap >0 | Any | ❌ FAIL | No (unless waived) |
| Any | Any | Any | Any (waived) | 🟡 WAIVED | Yes (tracked) |

---

## Best Practices

1. **Run all assessments before gate** - Comprehensive evaluation requires all 4 assessments
2. **Set clear thresholds** - Define pass/fail criteria upfront
3. **Use waivers judiciously** - Only for justified exceptions with tracking
4. **Automate in CI/CD** - Integrate gate checks into PR workflow
5. **Track action items** - Create tickets for CONCERNS action items
6. **Document decisions** - Clear rationale for audit trail
7. **Re-run after fixes** - Validate improvements after addressing gaps

---

## Skill Complete

This skill is now ready for use. To execute:

1. **Direct invocation** (when subagents built):
   ```
   @quinn *gate task-007
   ```

2. **Manual invocation** (current):
   ```
   I'd like to run quality gate assessment on task-007
   ```

---

## Version History

**Version 1.0** (2025-10-28)
- Initial skill implementation
- 8-step sequential execution
- 6-dimension quality assessment
- Evidence-based decision making
- Waiver support
- CI/CD integration (YAML output)
- Audit trail

---

<!-- End of Skill -->
