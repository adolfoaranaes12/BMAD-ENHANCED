---
name: quality-gate
description: Synthesize all quality assessments (risk, test-design, traceability, NFR) into evidence-based gate decision (PASS/CONCERNS/FAIL/WAIVED) with comprehensive rationale
version: 2.0
category: Quality
acceptance:
  all_assessments_synthesized: "All available quality assessments (risk profile, test design, traceability, NFR) loaded and synthesized into dimension scores"
  decision_made: "Evidence-based gate decision made (PASS/CONCERNS/FAIL/WAIVED) with clear rationale and criteria evaluation"
  reports_generated: "Both YAML (CI/CD automation) and Markdown (human review) reports generated with complete audit trail"
  action_items_identified: "Action items identified for CONCERNS/FAIL decisions with priorities and recommendations"
inputs:
  task_id:
    required: true
    description: "Task identifier for gate assessment (e.g., 'task-007')"
  task_file:
    required: true
    description: "Path to task specification file"
  config_file:
    required: false
    description: "Path to project configuration (defaults to .claude/config.yaml)"
  require_all_assessments:
    required: false
    description: "If true, all 4 assessments required; if false, minimum 1 required (defaults to false)"
outputs:
  gate_decision:
    description: "Final gate decision (PASS/CONCERNS/FAIL/WAIVED)"
  overall_quality_score:
    description: "Overall quality score (0-100)"
  dimension_scores:
    description: "Scores for all 6 quality dimensions"
  critical_issues_count:
    description: "Number of critical issues blocking gate"
  action_items_count:
    description: "Number of action items for remediation"
  yaml_report_path:
    description: "Path to YAML report (for CI/CD automation)"
  markdown_report_path:
    description: "Path to Markdown report (for human review)"
telemetry:
  emit: "skill.quality-gate.completed"
  track:
    - task_id
    - gate_decision
    - overall_quality_score
    - risk_management_score
    - test_coverage_score
    - traceability_score
    - nfr_score
    - implementation_quality_score
    - compliance_score
    - critical_issues_count
    - action_items_count
    - assessments_available
    - waivers_granted
    - gate_duration_ms
---

# Quality Gate Decision

The **quality-gate** skill performs the final quality gate assessment by synthesizing all previous quality evaluations and making an evidence-based decision on whether the implementation is ready to proceed (merge, deploy, release). This skill integrates risk management, test coverage, requirements traceability, and non-functional requirements into a comprehensive quality score across 6 dimensions, then applies configurable criteria to make a gate decision with clear rationale.

Unlike individual quality assessments that evaluate specific aspects (risks, tests, NFRs), the quality gate provides a holistic view of overall quality by weighting and combining all assessments. The gate produces two outputs: a YAML report for CI/CD automation and a markdown report for human review, enabling both automated and manual quality processes. Decisions include PASS (all criteria met), CONCERNS (some issues but can proceed), FAIL (critical issues block proceeding), or WAIVED (issues acknowledged and waived with justification).

The assessment evaluates 6 quality dimensions with configurable weights: Risk Management (25%), Test Coverage (20%), Traceability (20%), NFR (25%), Implementation Quality (5%), and Compliance (5%). Each dimension is scored independently, then combined into an overall quality score. Critical gap rules (e.g., no critical security gaps) and dimension minimums (e.g., traceability ≥65%) are applied to determine if the gate passes.

## When to Use This Skill

**Use quality-gate when you need to:**
- Make final quality decision before merge/deploy/release
- Synthesize all quality assessments into overall quality score
- Generate audit trail for compliance documentation
- Integrate quality checks into CI/CD pipeline
- Track quality waivers with justification
- Determine if implementation meets quality standards

**This skill is particularly valuable:**
- After all quality assessments complete (risk, test-design, trace, nfr)
- As final checkpoint before code merge or deployment
- For regulatory compliance requiring audit trail
- When automated quality gates are part of CI/CD
- For tracking quality trends over time (score history)

**Do NOT use quality-gate when:**
- Quality assessments haven't been performed yet (run assessments first)
- Task is in early planning stage (no implementation to assess)
- You only need specific assessment (use individual assessment skills instead)

## Prerequisites

Before running quality-gate, ensure you have:

1. **Task specification file** with implementation details
2. **Project configuration** (.claude/config.yaml) with gate criteria
3. **At least one quality assessment** completed:
   - Minimum: Traceability OR NFR (functional or quality attributes)
   - Recommended: All 4 assessments (risk, test-design, traceability, nfr)
4. **Waiver requests** documented (if any gaps require waiving)

**Optional but recommended:**
- All 4 quality assessments for comprehensive gate
- Gate criteria configured in project config
- CI/CD pipeline configured to consume YAML output

## Sequential Quality Gate Process

This skill executes through 9 sequential steps (Step 0 + Steps 1-8). Each step must complete successfully before proceeding. The process systematically synthesizes all quality dimensions, calculates scores, applies criteria, and makes the final gate decision.

### Step 0: Load Configuration and Assessments

**Purpose:** Load project configuration, task specification, and all available quality assessment reports. Determine which assessments are available and verify minimum requirements are met.

**Actions:**
1. Load project configuration from `.claude/config.yaml` (gate criteria, dimension weights, thresholds)
2. Read task specification file (extract task ID, title, implementation status)
3. Find and load latest quality assessments for this task:
   - Risk profile: `.claude/quality/assessments/{task-id}-risk-{latest-date}.md`
   - Test design: `.claude/quality/assessments/{task-id}-test-design-{latest-date}.md`
   - Traceability: `.claude/quality/assessments/{task-id}-trace-{latest-date}.md`
   - NFR assessment: `.claude/quality/assessments/{task-id}-nfr-{latest-date}.md`
4. Extract key metrics from each available assessment (scores, gaps, recommendations)
5. Check minimum assessment requirements (at least traceability OR nfr required)
6. Load any waiver requests from task file
7. Prepare output paths for YAML and Markdown reports

**Halt If:**
- Config file missing or invalid
- Task file not found
- Minimum assessments not available (require at least 1 of: traceability or NFR)
- Cannot create output directory

**Output:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: {task-id} - {title}
✓ Quality assessments loaded:
  ├─ Risk Profile: {available} (Score: {score}, {risks_count} risks)
  ├─ Test Design: {available} ({tests_count} tests)
  ├─ Traceability: {available} (Score: {score}%)
  └─ NFR Assessment: {available} (Score: {score}%)
✓ Minimum requirements: {met/not met}
✓ Waiver requests: {count}
✓ Output: {yaml_path}, {markdown_path}
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md) for detailed dimension definitions and scoring methodology.

---

### Step 1: Synthesize Risk Management Dimension

**Purpose:** Evaluate risk management effectiveness from risk profile assessment. Calculate risk management score based on mitigation coverage, test coverage for high risks, and risk score distribution.

**Actions:**
1. Load risk profile data (if available): total risks, critical/high/medium/low counts, mitigation status, test coverage
2. Calculate risk management score using formula:
   ```
   Risk Management Score = (
     (Mitigation Coverage × 0.5) +
     (Test Coverage for High Risks × 0.3) +
     (Risk Score Distribution × 0.2)
   )
   ```
3. Determine risk management status (PASS ≥75%, CONCERNS 50-74%, FAIL <50%)
4. Identify risk management gaps (critical risks without mitigation, high risks without tests)
5. Calculate weighted contribution to overall gate (score × 25% weight)

**If Risk Profile Not Available:**
- Mark dimension as N/A
- Redistribute weight to other dimensions
- Note assumption of acceptable risk management

**Output:**
```
✓ Risk Management dimension synthesized
✓ Score: {score}% ({status})
✓ Critical Risks: {count} ({mitigated_count} mitigated)
✓ High Risks: {count} ({tested_count} tested)
✓ Contribution to Gate: {weighted_score} points (25% weight)
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md#risk-management-dimension) for detailed risk scoring formula.

---

### Step 2: Synthesize Test Coverage Dimension

**Purpose:** Evaluate test strategy and coverage from test-design assessment. Calculate test coverage score based on P0 tests passing, P1 tests implemented, and overall coverage percentage.

**Actions:**
1. Load test design data (if available): total tests by priority (P0/P1/P2), tests by level (unit/integration/e2e), implementation status, pass status, coverage percentage
2. Calculate test coverage score using formula:
   ```
   Test Coverage Score = (
     (P0 Tests Passing × 0.5) +
     (P1 Tests Implemented × 0.3) +
     (Coverage Percentage × 0.2)
   )
   ```
3. Determine test coverage status (PASS ≥80%, CONCERNS 65-79%, FAIL <65%)
4. Identify test coverage gaps (P0 tests not passing, P1 tests not implemented, coverage below threshold)
5. Calculate weighted contribution to overall gate (score × 20% weight)

**If Test Design Not Available:**
- Mark dimension as N/A
- Fallback: Use test coverage from traceability if available
- Note assumption that tests exist

**Output:**
```
✓ Test Coverage dimension synthesized
✓ Score: {score}% ({status})
✓ P0 Tests: {passing}/{total} passing
✓ P1 Tests: {implemented}/{total} implemented
✓ Coverage: {coverage}%
✓ Contribution to Gate: {weighted_score} points (20% weight)
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md#test-coverage-dimension) for test coverage scoring methodology.

---

### Step 3: Synthesize Traceability Dimension

**Purpose:** Evaluate requirements traceability from traceability assessment. Calculate traceability score based on implementation coverage, test coverage, and gap coverage.

**Actions:**
1. Load traceability data (if available): total AC, implementation status (implemented/partial/not implemented), test status (tested/partial/not tested), gaps by severity
2. Calculate traceability score using formula:
   ```
   Traceability Score = (
     (Implementation Coverage × 0.5) +
     (Test Coverage × 0.4) +
     (Gap Coverage × 0.1)
   )
   ```
   Where Gap Coverage = 100% - (Critical×30% + High×20% + Medium×10%)
3. Determine traceability status (PASS ≥80%, CONCERNS 65-79%, FAIL <65%)
4. Identify traceability gaps (AC not implemented, AC not tested, missing evidence)
5. Calculate weighted contribution to overall gate (score × 20% weight)

**If Traceability Not Available:**
- If NFR available: Proceed (NFR covers quality attributes)
- If NFR also missing: Halt (minimum requirement not met)

**Output:**
```
✓ Traceability dimension synthesized
✓ Score: {score}% ({status})
✓ Implementation Coverage: {impl_coverage}%
✓ Test Coverage: {test_coverage}%
✓ Gaps: {critical}/{high}/{medium} (critical/high/medium)
✓ Contribution to Gate: {weighted_score} points (20% weight)
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md#traceability-dimension) for traceability scoring formula.

---

### Step 4: Synthesize NFR Dimension

**Purpose:** Evaluate non-functional requirements from NFR assessment. Use overall NFR score directly, check for critical gaps in security/reliability, and apply special rules for production blockers.

**Actions:**
1. Load NFR data (if available): overall score, category scores (security, performance, reliability, maintainability, scalability, usability), gaps by severity and category
2. NFR score is direct: Overall NFR Score from assessment (no additional calculation)
3. Determine NFR status (PASS ≥75%, CONCERNS 60-74%, FAIL <60%)
4. Apply special rules:
   - Security <50%: FAIL (production blocker)
   - Reliability <50%: FAIL (production blocker)
   - Critical security gap: CONCERNS or FAIL
   - Critical reliability gap: CONCERNS
5. Identify NFR gaps (critical gaps by category, categories below 50%, high-severity gaps)
6. Calculate weighted contribution to overall gate (score × 25% weight)

**If NFR Not Available:**
- If Traceability available: Proceed (traceability covers functional correctness)
- If Traceability also missing: Halt (minimum requirement not met)
- Fallback: Use implementation quality as proxy

**Output:**
```
✓ NFR dimension synthesized
✓ Overall NFR Score: {score}% ({status})
✓ Security: {security_score}% ({security_status})
✓ Reliability: {reliability_score}% ({reliability_status})
✓ Critical NFR Gaps: {count} (Security: {sec}, Reliability: {rel})
✓ Contribution to Gate: {weighted_score} points (25% weight)
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md#nfr-dimension) for NFR dimension scoring and special rules.

---

### Step 5: Synthesize Implementation Quality Dimension

**Purpose:** Evaluate implementation quality from task specification and implementation record. Calculate implementation quality score based on task completion, testing, documentation, and code review status.

**Actions:**
1. Extract implementation data from task specification: status (Draft/In Progress/Review/Complete), files changed, implementation record (completion, testing, documentation)
2. Calculate implementation quality score using formula:
   ```
   Implementation Quality Score = (
     (Task Completion × 0.4) +
     (Testing × 0.3) +
     (Documentation × 0.2) +
     (Code Review × 0.1)
   )
   ```
3. Determine implementation quality status (PASS ≥70%, CONCERNS 50-69%, FAIL <50%)
4. Calculate weighted contribution to overall gate (score × 5% weight)

**Output:**
```
✓ Implementation Quality dimension synthesized
✓ Score: {score}% ({status})
✓ Task Completion: {completion}%
✓ Testing: {testing}%
✓ Documentation: {documentation}%
✓ Contribution to Gate: {weighted_score} points (5% weight)
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md#implementation-quality-dimension) for implementation quality scoring.

---

### Step 6: Synthesize Compliance Dimension

**Purpose:** Evaluate compliance with standards, policies, and regulatory requirements. Check if required compliance activities (security review, privacy review, etc.) have been completed.

**Actions:**
1. Check compliance requirements from config: standards (OWASP, WCAG, REST API best practices), policies (security review, privacy review, legal review)
2. Evaluate compliance: For each requirement, check if assessment addressed it and extract compliance status
3. Calculate compliance score: (Requirements Met / Total Requirements) × 100%
4. Determine compliance status (PASS 100%, CONCERNS 90-99%, FAIL <90%)
5. Calculate weighted contribution to overall gate (score × 5% weight)

**Output:**
```
✓ Compliance dimension synthesized
✓ Score: {score}% ({status})
✓ Standards Met: {count}/{total}
✓ Policies Met: {count}/{total}
✓ Contribution to Gate: {weighted_score} points (5% weight)
```

**Reference:** See [gate-dimensions.md](references/gate-dimensions.md#compliance-dimension) for compliance evaluation methodology.

---

### Step 7: Calculate Overall Quality Score and Make Decision

**Purpose:** Synthesize all dimensions into overall quality score, apply gate criteria, evaluate waivers, and make final gate decision.

**Actions:**
1. Calculate overall quality score: Sum of all weighted dimension scores (target: 100%)
2. Apply quality gate criteria from config:
   - Overall score threshold (default: ≥75%)
   - Dimension minimums (risk ≥50%, test ≥65%, trace ≥65%, nfr ≥60%, impl ≥50%, compliance ≥90%)
   - Critical gap rules (no critical security gaps, max 1 critical reliability gap)
3. Evaluate each criterion: Check if overall score meets threshold, all dimensions meet minimums, critical gap rules satisfied
4. Determine preliminary gate decision:
   - FAIL: Security/reliability <50%, critical security gap, overall <60%
   - CONCERNS: Overall <75%, dimension below minimum, or critical gaps
   - PASS: All criteria met
5. Check waiver requests: If any gaps waived with justification, remove from critical count and re-evaluate decision
6. Finalize decision with reasoning: Document status, overall score, criteria met/not met, blockers, action items

**Output:**
```
✓ Overall Quality Score calculated: {score}%
✓ Gate Decision: {PASS/CONCERNS/FAIL/WAIVED}
✓ Criteria Met: {count}/{total}
✓ Critical Issues: {count}
✓ Waivers Granted: {count}
✓ Action Items: {count}
```

**Reference:** See [gate-decision-logic.md](references/gate-decision-logic.md) for complete decision matrix and criteria.

---

### Step 8: Generate Quality Gate Reports and Present Summary

**Purpose:** Generate structured YAML (for CI/CD automation) and human-readable Markdown (for review) reports, then present concise summary to user.

**Actions:**
1. Generate YAML report:
   - Task metadata (ID, title, type)
   - Assessment metadata (date, assessor, available assessments)
   - Scores (overall score, dimension scores with weights and status)
   - Decision (status, confidence, reasoning, blockers, action items)
   - Waivers (gap ID, justification, approver, date)
   - Audit trail (timestamp, action, result, assessor)
2. Generate Markdown report using template:
   - Populate template from `.claude/templates/quality-gate.md`
   - Include all dimension details, scores, gaps, action items
   - Format for human readability with clear sections
3. Present summary to user:
   - Overall quality score and gate decision
   - Dimension scores with status indicators
   - Reasoning for decision
   - Critical issues and blockers (if any)
   - Action items with priorities
   - Waivers granted (if any)
   - Next steps (complete action items, proceed with merge, etc.)
4. Emit telemetry event with all metrics

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Gate Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id} - {title}
Date: {date}

📊 Overall Quality Score: {score}% ({status})

Dimension Scores:
├─ Risk Management: {score}% ({status}, {weighted} pts)
├─ Test Coverage: {score}% ({status}, {weighted} pts)
├─ Traceability: {score}% ({status}, {weighted} pts)
├─ NFR: {score}% ({status}, {weighted} pts)
├─ Implementation Quality: {score}% ({status}, {weighted} pts)
└─ Compliance: {score}% ({status}, {weighted} pts)

🎯 Gate Decision: {PASS/CONCERNS/FAIL/WAIVED}

Reasoning: {decision rationale}

Can Proceed: {YES/NO}

{Blockers section if FAIL}
{Action Items section if CONCERNS}
{Waivers section if granted}

📄 Reports Generated:
├─ YAML: {yaml_path}
└─ Markdown: {markdown_path}

💡 Next Steps:
{recommended next steps based on decision}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Execution Complete.**

**Reference:** See [gate-examples.md](references/gate-examples.md) for example reports and summaries.

---

## Integration with Other Skills

### Integration with Individual Assessments

**Inputs from assessments:**
- **risk-profile** provides risk scores, mitigation status, high-risk test coverage → feeds Risk Management dimension
- **test-design** provides test counts by priority, implementation/pass status, coverage → feeds Test Coverage dimension
- **trace-requirements** provides AC implementation/test coverage, gaps → feeds Traceability dimension
- **nfr-assess** provides overall NFR score, category scores, critical gaps → feeds NFR dimension

**Sequential workflow:**
```
1. Run risk-profile (optional)
2. Run test-design (optional)
3. Run trace-requirements (required*)
4. Run nfr-assess (required*)
5. Run quality-gate (synthesizes all)

*At least one of trace-requirements or nfr-assess required
```

### Integration with CI/CD

**YAML output enables automation:**
- CI/CD pipeline reads `.claude/quality/gates/{task-id}-gate-{date}.yaml`
- Checks `gate.decision.status` field
- FAIL → Block PR merge, fail build
- CONCERNS → Post warning, require review
- PASS → Allow merge, proceed
- WAIVED → Log waiver, allow merge with tracking

**Example GitHub Actions integration:**
```yaml
- name: Check quality gate
  run: |
    GATE_STATUS=$(yq '.gate.decision.status' .claude/quality/gates/*.yaml)
    if [ "$GATE_STATUS" = "FAIL" ]; then
      echo "Quality gate FAILED"
      exit 1
    fi
```

**Reference:** See [gate-integration.md](references/gate-integration.md) for CI/CD integration examples and waiver handling.

---

## Best Practices

1. **Run all assessments before gate** - Comprehensive evaluation requires all 4 assessments for best results. Minimum is 1 (traceability or NFR), but all 4 recommended.

2. **Set clear thresholds upfront** - Define pass/fail criteria in `.claude/config.yaml` before running gate. Consistent criteria enable objective decisions.

3. **Use waivers judiciously** - Only waive gaps with clear justification and approval. Track all waivers for audit trail and future remediation.

4. **Automate in CI/CD** - Integrate gate checks into PR workflow using YAML output. Automated gates ensure consistent quality standards.

5. **Track action items** - For CONCERNS decisions, create tickets for action items to ensure follow-up. Don't let action items get lost.

6. **Document decisions clearly** - Provide detailed reasoning for gate decisions, especially FAIL or WAIVED. Clear rationale supports audit requirements.

7. **Re-run after fixes** - After addressing gaps, re-run quality-gate to validate improvements and update gate status. Track score improvements over time.

8. **Configure weights appropriately** - Adjust dimension weights based on project type (e.g., security-critical projects increase Security weight in NFR dimension).

---

## References

- **[gate-dimensions.md](references/gate-dimensions.md)** - Detailed scoring methodology for all 6 quality dimensions (Risk Management, Test Coverage, Traceability, NFR, Implementation Quality, Compliance) with formulas and examples

- **[gate-decision-logic.md](references/gate-decision-logic.md)** - Complete decision matrix, criteria evaluation rules, critical gap rules, waiver logic, and decision reasoning templates

- **[gate-integration.md](references/gate-integration.md)** - CI/CD integration examples (GitHub Actions, GitLab CI), waiver request process, audit trail generation, and YAML schema

- **[gate-examples.md](references/gate-examples.md)** - Complete example gate reports (PASS, CONCERNS, FAIL, WAIVED scenarios), YAML and Markdown outputs, and summary formats

---

*Quality Gate Decision skill - Version 2.0 - Minimal V2 Architecture*
