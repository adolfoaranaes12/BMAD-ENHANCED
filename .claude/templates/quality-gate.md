# Quality Gate Report: {{TASK_TITLE}}

**Task:** {{TASK_ID}}
**Date:** {{DATE}}
**Assessor:** {{ASSESSOR}}

---

## Gate Decision

### Status: {{GATE_STATUS}}

**Overall Quality Score:** {{OVERALL_SCORE}}% (Threshold: {{THRESHOLD}}%)

**Decision:** {{GATE_DECISION_ICON}} **{{GATE_STATUS}}**

**Confidence:** {{CONFIDENCE}}  <!-- HIGH | MEDIUM | LOW -->

**Can Proceed:** {{CAN_PROCEED}}  <!-- YES | NO | CONDITIONAL -->

---

## Executive Summary

{{EXECUTIVE_SUMMARY}}

**Key Findings:**
{{#each KEY_FINDINGS}}
- {{icon}} {{finding}}
{{/each}}

**Blockers:** {{#if BLOCKERS}}{{BLOCKER_COUNT}}{{else}}None{{/if}}

**Action Items:** {{ACTION_ITEM_COUNT}} ({{P0_ACTIONS}} P0, {{P1_ACTIONS}} P1, {{P2_ACTIONS}} P2)

**Waivers:** {{WAIVER_COUNT}} {{#if WAIVER_COUNT}}granted{{/if}}

---

## Quality Dimension Scores

| Dimension | Score | Weight | Weighted | Threshold | Status |
|-----------|-------|--------|----------|-----------|--------|
| Risk Management | {{RISK_SCORE}}% | {{RISK_WEIGHT}}% | {{RISK_WEIGHTED}} | {{RISK_THRESHOLD}}% | {{RISK_STATUS}} |
| Test Coverage | {{TEST_SCORE}}% | {{TEST_WEIGHT}}% | {{TEST_WEIGHTED}} | {{TEST_THRESHOLD}}% | {{TEST_STATUS}} |
| Traceability | {{TRACE_SCORE}}% | {{TRACE_WEIGHT}}% | {{TRACE_WEIGHTED}} | {{TRACE_THRESHOLD}}% | {{TRACE_STATUS}} |
| NFR | {{NFR_SCORE}}% | {{NFR_WEIGHT}}% | {{NFR_WEIGHTED}} | {{NFR_THRESHOLD}}% | {{NFR_STATUS}} |
| Implementation Quality | {{IMPL_SCORE}}% | {{IMPL_WEIGHT}}% | {{IMPL_WEIGHTED}} | {{IMPL_THRESHOLD}}% | {{IMPL_STATUS}} |
| Compliance | {{COMPLIANCE_SCORE}}% | {{COMPLIANCE_WEIGHT}}% | {{COMPLIANCE_WEIGHTED}} | {{COMPLIANCE_THRESHOLD}}% | {{COMPLIANCE_STATUS}} |
| **Overall** | **{{OVERALL_SCORE}}%** | **100%** | **{{OVERALL_SCORE}}** | **{{THRESHOLD}}%** | **{{GATE_STATUS}}** |

**Legend:**
- ✅ PASS: Meets or exceeds threshold
- ⚠️ CONCERNS: Below threshold but acceptable with action items
- ❌ FAIL: Critical issues, must fix before proceeding
- N/A: Assessment not performed (dimension weight redistributed)

---

## 1. Risk Management Dimension

**Score:** {{RISK_SCORE}}% ({{RISK_STATUS}})
**Weight:** {{RISK_WEIGHT}}%
**Contribution:** {{RISK_WEIGHTED}} points

{{#if RISK_AVAILABLE}}

**Assessment:** `.claude/quality/assessments/{{TASK_ID}}-risk-{{RISK_DATE}}.md`

**Risk Distribution:**
- Total Risks: {{TOTAL_RISKS}}
- Critical (≥7): {{CRITICAL_RISKS}}
- High (≥6): {{HIGH_RISKS}}
- Medium (3-5): {{MEDIUM_RISKS}}
- Low (1-2): {{LOW_RISKS}}

**Mitigation Status:**
- High-risk items: {{HIGH_RISK_ITEMS}} (Critical + High)
- Mitigated: {{HIGH_RISK_MITIGATED}}/{{HIGH_RISK_ITEMS}} ({{MITIGATION_PERCENTAGE}}%)
- Tested: {{HIGH_RISK_TESTED}}/{{HIGH_RISK_ITEMS}} ({{TEST_PERCENTAGE}}%)

**Score Calculation:**
```
Risk Management Score = (
  (Mitigation Coverage × 0.5) +
  (Test Coverage × 0.3) +
  (Risk Distribution × 0.2)
)

= ({{MITIGATION_PERCENTAGE}}% × 0.5) +
  ({{TEST_PERCENTAGE}}% × 0.3) +
  ({{DISTRIBUTION_SCORE}}% × 0.2)

= {{RISK_SCORE}}%
```

**Critical/High Risks:**
{{#each CRITICAL_HIGH_RISKS}}
{{number}}. **Risk #{{risk_id}}**: {{risk_title}} (Score: {{risk_score}})
   - Mitigation: {{mitigation_status}}
   - Tests: {{test_status}}
   - Status: {{overall_status}}
{{/each}}

**Gaps:**
{{#each RISK_GAPS}}
- {{gap_id}}: {{description}} ({{severity}})
{{/each}}

{{#if RISK_STATUS == 'FAIL' || RISK_STATUS == 'CONCERNS'}}
**Recommendations:**
{{#each RISK_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}
{{/if}}

{{else}}

**Assessment:** Not performed

**Note:** Risk profile assessment not available. Assuming acceptable risk management based on other quality signals.

**Impact on Gate:** Dimension weight redistributed to other dimensions.

{{/if}}

---

## 2. Test Coverage Dimension

**Score:** {{TEST_SCORE}}% ({{TEST_STATUS}})
**Weight:** {{TEST_WEIGHT}}%
**Contribution:** {{TEST_WEIGHTED}} points

{{#if TEST_DESIGN_AVAILABLE}}

**Assessment:** `.claude/quality/assessments/{{TASK_ID}}-test-design-{{TEST_DATE}}.md`

**Test Distribution:**
- Total Tests: {{TOTAL_TESTS}}
- P0 (Critical): {{P0_TESTS}} ({{P0_PASSING}}/{{P0_TESTS}} passing)
- P1 (High): {{P1_TESTS}} ({{P1_IMPLEMENTED}}/{{P1_TESTS}} implemented)
- P2 (Medium): {{P2_TESTS}}

**Test Levels:**
- Unit: {{UNIT_TESTS}}
- Integration: {{INTEGRATION_TESTS}}
- E2E: {{E2E_TESTS}}

**Coverage:**
- Line Coverage: {{LINE_COVERAGE}}%
- Branch Coverage: {{BRANCH_COVERAGE}}%
- Function Coverage: {{FUNCTION_COVERAGE}}%

**Score Calculation:**
```
Test Coverage Score = (
  (P0 Tests Passing × 0.5) +
  (P1 Tests Implemented × 0.3) +
  (Coverage Percentage × 0.2)
)

= ({{P0_PASSING_PERCENTAGE}}% × 0.5) +
  ({{P1_IMPLEMENTED_PERCENTAGE}}% × 0.3) +
  ({{LINE_COVERAGE}}% × 0.2)

= {{TEST_SCORE}}%
```

**P0 Test Status:**
{{#each P0_TEST_STATUS}}
- {{test_name}}: {{status}}
{{/each}}

**Gaps:**
{{#each TEST_GAPS}}
- {{gap_id}}: {{description}} ({{severity}})
{{/each}}

{{#if TEST_STATUS == 'FAIL' || TEST_STATUS == 'CONCERNS'}}
**Recommendations:**
{{#each TEST_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}
{{/if}}

{{else}}

**Assessment:** Not performed (using traceability test data if available)

**Fallback:** Test coverage extracted from traceability assessment.

{{/if}}

---

## 3. Traceability Dimension

**Score:** {{TRACE_SCORE}}% ({{TRACE_STATUS}})
**Weight:** {{TRACE_WEIGHT}}%
**Contribution:** {{TRACE_WEIGHTED}} points

{{#if TRACE_AVAILABLE}}

**Assessment:** `.claude/quality/assessments/{{TASK_ID}}-trace-{{TRACE_DATE}}.md`

**Acceptance Criteria:**
- Total AC: {{TOTAL_AC}}
- Implemented: {{AC_IMPLEMENTED}} ({{IMPL_PERCENTAGE}}%)
- Partial: {{AC_PARTIAL}}
- Not Implemented: {{AC_NOT_IMPLEMENTED}}

**Test Coverage:**
- Tested: {{AC_TESTED}} ({{TEST_PERCENTAGE}}%)
- Partial Tests: {{AC_PARTIAL_TESTS}}
- Not Tested: {{AC_NOT_TESTED}}

**Traceability Matrix:**
- Complete (✅): {{AC_COMPLETE}} AC
- Partial (⚠️): {{AC_PARTIAL_STATUS}} AC
- Incomplete (❌): {{AC_INCOMPLETE}} AC

**Score Calculation:**
```
Traceability Score = (
  (Implementation Coverage × 0.5) +
  (Test Coverage × 0.4) +
  (Gap Coverage × 0.1)
)

= ({{IMPL_COVERAGE}}% × 0.5) +
  ({{TEST_COVERAGE}}% × 0.4) +
  ({{GAP_COVERAGE}}% × 0.1)

= {{TRACE_SCORE}}%
```

**Coverage Gaps:**
{{#each TRACE_GAPS}}
- {{gap_id}}: {{description}} ({{severity}})
{{/each}}

{{#if TRACE_STATUS == 'FAIL' || TRACE_STATUS == 'CONCERNS'}}
**Recommendations:**
{{#each TRACE_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}
{{/if}}

{{else}}

**Assessment:** Not performed

**Note:** Traceability assessment is REQUIRED for quality gate. This is a critical gap.

**Impact on Gate:** {{#if GATE_STATUS == 'FAIL'}}Gate status: FAIL (missing required assessment){{else}}Using implementation record as fallback{{/if}}

{{/if}}

---

## 4. Non-Functional Requirements (NFR) Dimension

**Score:** {{NFR_SCORE}}% ({{NFR_STATUS}})
**Weight:** {{NFR_WEIGHT}}%
**Contribution:** {{NFR_WEIGHTED}} points

{{#if NFR_AVAILABLE}}

**Assessment:** `.claude/quality/assessments/{{TASK_ID}}-nfr-{{NFR_DATE}}.md`

**NFR Category Scores:**

| Category | Score | Status | Critical Gaps | High Gaps |
|----------|-------|--------|---------------|-----------|
| Security | {{SECURITY_SCORE}}% | {{SECURITY_STATUS}} | {{SECURITY_CRITICAL}} | {{SECURITY_HIGH}} |
| Performance | {{PERFORMANCE_SCORE}}% | {{PERFORMANCE_STATUS}} | {{PERFORMANCE_CRITICAL}} | {{PERFORMANCE_HIGH}} |
| Reliability | {{RELIABILITY_SCORE}}% | {{RELIABILITY_STATUS}} | {{RELIABILITY_CRITICAL}} | {{RELIABILITY_HIGH}} |
| Maintainability | {{MAINTAINABILITY_SCORE}}% | {{MAINTAINABILITY_STATUS}} | {{MAINTAINABILITY_CRITICAL}} | {{MAINTAINABILITY_HIGH}} |
| Scalability | {{SCALABILITY_SCORE}}% | {{SCALABILITY_STATUS}} | {{SCALABILITY_CRITICAL}} | {{SCALABILITY_HIGH}} |
| Usability | {{USABILITY_SCORE}}% | {{USABILITY_STATUS}} | {{USABILITY_CRITICAL}} | {{USABILITY_HIGH}} |

**Overall NFR Score:** {{NFR_SCORE}}%

**Critical NFR Gaps:** {{NFR_CRITICAL_GAPS}}

{{#if NFR_CRITICAL_GAPS > 0}}
**Critical Gaps Detail:**
{{#each NFR_CRITICAL_GAP_DETAILS}}
- **{{gap_id}}**: {{description}} ({{category}}, {{severity}})
{{/each}}
{{/if}}

**Security Assessment:**
{{#if SECURITY_SCORE < 50}}
⚠️ **PRODUCTION BLOCKER**: Security score below 50% ({{SECURITY_SCORE}}%)
{{else if SECURITY_STATUS == 'CONCERNS'}}
⚠️ Security concerns identified, see NFR assessment for details
{{else}}
✅ Security assessment passed
{{/if}}

**Reliability Assessment:**
{{#if RELIABILITY_SCORE < 50}}
⚠️ **PRODUCTION BLOCKER**: Reliability score below 50% ({{RELIABILITY_SCORE}}%)
{{else if RELIABILITY_STATUS == 'CONCERNS'}}
⚠️ Reliability concerns identified, see NFR assessment for details
{{else}}
✅ Reliability assessment passed
{{/if}}

**NFR Gaps:**
{{#each NFR_GAPS}}
- {{gap_id}}: {{description}} ({{category}}, {{severity}})
{{/each}}

{{#if NFR_STATUS == 'FAIL' || NFR_STATUS == 'CONCERNS'}}
**Recommendations:**
{{#each NFR_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}
{{/if}}

{{else}}

**Assessment:** Not performed

**Note:** NFR assessment not available. Assuming acceptable quality attributes based on other signals.

**Impact on Gate:** Dimension weight redistributed to other dimensions.

{{/if}}

---

## 5. Implementation Quality Dimension

**Score:** {{IMPL_SCORE}}% ({{IMPL_STATUS}})
**Weight:** {{IMPL_WEIGHT}}%
**Contribution:** {{IMPL_WEIGHTED}} points

**Task Status:** {{TASK_STATUS}}

**Implementation Metrics:**
- Task Completion: {{TASK_COMPLETION}}%
- Testing: {{TESTING_COMPLETION}}%
- Documentation: {{DOCUMENTATION_COMPLETION}}%
- Code Review: {{CODE_REVIEW_COMPLETION}}%

**Implementation Record:**
- Files Changed: {{FILES_CHANGED}}
- Lines Added: {{LINES_ADDED}}
- Lines Deleted: {{LINES_DELETED}}
- Components Modified: {{COMPONENTS_MODIFIED}}

**Score Calculation:**
```
Implementation Quality = (
  (Task Completion × 0.4) +
  (Testing × 0.3) +
  (Documentation × 0.2) +
  (Code Review × 0.1)
)

= ({{TASK_COMPLETION}}% × 0.4) +
  ({{TESTING_COMPLETION}}% × 0.3) +
  ({{DOCUMENTATION_COMPLETION}}% × 0.2) +
  ({{CODE_REVIEW_COMPLETION}}% × 0.1)

= {{IMPL_SCORE}}%
```

**Quality Indicators:**
{{#each IMPL_INDICATORS}}
- {{indicator}}: {{status}}
{{/each}}

{{#if IMPL_STATUS == 'FAIL' || IMPL_STATUS == 'CONCERNS'}}
**Gaps:**
{{#each IMPL_GAPS}}
- {{gap}}
{{/each}}

**Recommendations:**
{{#each IMPL_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}
{{/if}}

---

## 6. Compliance Dimension

**Score:** {{COMPLIANCE_SCORE}}% ({{COMPLIANCE_STATUS}})
**Weight:** {{COMPLIANCE_WEIGHT}}%
**Contribution:** {{COMPLIANCE_WEIGHTED}} points

**Compliance Requirements:**

| Requirement | Type | Status | Evidence |
|-------------|------|--------|----------|
{{COMPLIANCE_MATRIX_ROWS}}

**Score Calculation:**
```
Compliance Score = (Requirements Met / Total Requirements) × 100%

= {{COMPLIANCE_MET}}/{{COMPLIANCE_TOTAL}} × 100%
= {{COMPLIANCE_SCORE}}%
```

**Standards Compliance:**
{{#each STANDARDS}}
- {{standard}}: {{status}}
{{/each}}

**Policy Compliance:**
{{#each POLICIES}}
- {{policy}}: {{status}}
{{/each}}

{{#if COMPLIANCE_STATUS == 'FAIL' || COMPLIANCE_STATUS == 'CONCERNS'}}
**Gaps:**
{{#each COMPLIANCE_GAPS}}
- {{gap}}
{{/each}}

**Recommendations:**
{{#each COMPLIANCE_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}
{{/if}}

---

## Gate Decision Rationale

{{GATE_DECISION_RATIONALE}}

**Decision Criteria:**

{{#each DECISION_CRITERIA}}
- {{criterion}}: {{status}} {{#if met}}✓{{else}}✗{{/if}}
{{/each}}

**Evaluation Summary:**

{{#if GATE_STATUS == 'PASS'}}
### ✅ PASS - Ready to Proceed

All quality criteria met. No critical issues identified. Implementation demonstrates:
- {{pass_reason_1}}
- {{pass_reason_2}}
- {{pass_reason_3}}

**Next Steps:**
1. Proceed with merge
2. Monitor post-deployment metrics
3. Track any minor action items

{{/if}}

{{#if GATE_STATUS == 'CONCERNS'}}
### ⚠️ CONCERNS - Can Proceed with Action Items

Overall quality acceptable, but some concerns identified:
{{#each CONCERN_REASONS}}
- {{reason}}
{{/each}}

**Can proceed because:**
{{#each PROCEED_REASONS}}
- {{reason}}
{{/each}}

**Must address:**
{{#each MUST_ADDRESS}}
- {{item}}
{{/each}}

**Next Steps:**
1. Review and acknowledge action items
2. Create tickets for P1 actions
3. Proceed with merge
4. Complete action items before release
5. Track waived items (if any)

{{/if}}

{{#if GATE_STATUS == 'FAIL'}}
### ❌ FAIL - Cannot Proceed

Critical quality issues identified that block proceeding:
{{#each FAIL_REASONS}}
- {{reason}}
{{/each}}

**Blockers:**
{{#each BLOCKERS}}
{{number}}. **{{blocker_id}}**: {{description}} ({{severity}})
   - Impact: {{impact}}
   - Required Action: {{action}}
   - Estimated Effort: {{effort}}
{{/each}}

**Next Steps:**
1. Address all blockers
2. Re-run quality assessments
3. Re-run quality gate
4. Do NOT proceed with merge until blockers resolved

{{/if}}

{{#if GATE_STATUS == 'WAIVED'}}
### 🟡 WAIVED - Proceeding with Acknowledged Gaps

Quality issues waived with justification:
{{#each WAIVED_REASONS}}
- {{reason}}
{{/each}}

**Waivers granted (see Waivers section below)**

**Next Steps:**
1. Track waived items in issue tracker
2. Proceed with merge (waiver approved)
3. Address waived items in follow-up work
4. Re-assess in next gate review

{{/if}}

---

## Action Items

{{#if ACTION_ITEMS}}

**Total Action Items:** {{ACTION_ITEM_COUNT}} ({{P0_ACTION_COUNT}} P0, {{P1_ACTION_COUNT}} P1, {{P2_ACTION_COUNT}} P2)

### P0 Actions (Must Complete Before Merge)

{{#each P0_ACTIONS}}
**{{action_number}}. {{action_id}}: {{title}}**
- **Priority:** P0 (Critical)
- **Related Gap:** {{related_gap}}
- **Description:** {{description}}
- **Action:** {{action}}
- **Owner:** {{owner}}
- **Due Date:** {{due_date}}
- **Estimated Effort:** {{effort}}
- **Validation:** {{validation}}

{{/each}}

{{#if no_p0_actions}}
✅ No P0 actions required.
{{/if}}

### P1 Actions (Should Complete Before Release)

{{#each P1_ACTIONS}}
**{{action_number}}. {{action_id}}: {{title}}**
- **Priority:** P1 (High)
- **Related Gap:** {{related_gap}}
- **Description:** {{description}}
- **Action:** {{action}}
- **Owner:** {{owner}}
- **Estimated Effort:** {{effort}}

{{/each}}

### P2 Actions (Future Enhancement)

{{#each P2_ACTIONS}}
- **{{action_id}}**: {{title}} ({{related_gap}}) - {{action}} [{{effort}}]
{{/each}}

{{else}}

✅ No action items. All quality criteria met.

{{/if}}

---

## Waivers

{{#if WAIVERS}}

**Total Waivers Granted:** {{WAIVER_COUNT}}

{{#each WAIVERS}}
### Waiver {{waiver_number}}: {{gap_id}}

**Gap:** {{gap_description}}
**Severity:** {{severity}}
**Category:** {{category}}

**Justification:**
{{justification}}

**Approval:**
- **Requested By:** {{requested_by}}
- **Approved By:** {{approved_by}}
- **Approval Date:** {{approval_date}}

**Tracking:**
- **Follow-up Ticket:** {{ticket_id}}
- **Target Resolution:** {{target_date}}
- **Owner:** {{owner}}

**Impact:**
{{impact}}

**Mitigation:**
{{mitigation}}

---

{{/each}}

{{else}}

No waivers granted. All gaps must be addressed or do not exist.

{{/if}}

---

## Assessment Cross-Reference

**Available Assessments:**

{{#if RISK_AVAILABLE}}
- ✓ **Risk Profile:** `.claude/quality/assessments/{{TASK_ID}}-risk-{{RISK_DATE}}.md`
  - Total Risks: {{TOTAL_RISKS}}
  - High-Risk Items: {{HIGH_RISK_ITEMS}}
  - Mitigation Coverage: {{MITIGATION_PERCENTAGE}}%
{{else}}
- ✗ **Risk Profile:** Not performed
{{/if}}

{{#if TEST_DESIGN_AVAILABLE}}
- ✓ **Test Design:** `.claude/quality/assessments/{{TASK_ID}}-test-design-{{TEST_DATE}}.md`
  - Total Tests: {{TOTAL_TESTS}}
  - P0 Tests: {{P0_TESTS}} ({{P0_PASSING}} passing)
  - Coverage: {{LINE_COVERAGE}}%
{{else}}
- ✗ **Test Design:** Not performed
{{/if}}

{{#if TRACE_AVAILABLE}}
- ✓ **Traceability:** `.claude/quality/assessments/{{TASK_ID}}-trace-{{TRACE_DATE}}.md`
  - Total AC: {{TOTAL_AC}}
  - Implementation Coverage: {{IMPL_COVERAGE}}%
  - Test Coverage: {{TEST_COVERAGE}}%
{{else}}
- ✗ **Traceability:** Not performed
{{/if}}

{{#if NFR_AVAILABLE}}
- ✓ **NFR Assessment:** `.claude/quality/assessments/{{TASK_ID}}-nfr-{{NFR_DATE}}.md`
  - Overall NFR Score: {{NFR_SCORE}}%
  - Security: {{SECURITY_SCORE}}%
  - Reliability: {{RELIABILITY_SCORE}}%
{{else}}
- ✗ **NFR Assessment:** Not performed
{{/if}}

**Quality Gate:**
- **YAML:** `.claude/quality/gates/{{TASK_ID}}-gate-{{DATE}}.yaml` (for CI/CD)
- **Markdown:** `.claude/quality/gates/{{TASK_ID}}-gate-{{DATE}}.md` (this file)

---

## Recommendations

**Immediate Recommendations:**
{{#each IMMEDIATE_RECOMMENDATIONS}}
{{number}}. {{recommendation}}
{{/each}}

**Long-Term Recommendations:**
{{#each LONGTERM_RECOMMENDATIONS}}
{{number}}. {{recommendation}}
{{/each}}

**For Future Tasks:**
{{#each FUTURE_RECOMMENDATIONS}}
- {{recommendation}}
{{/each}}

---

## Audit Trail

**Gate Assessment History:**

{{#each AUDIT_TRAIL}}
**{{entry_number}}. {{timestamp}} - {{action}}**
- Assessor: {{assessor}}
- Result: {{result}}
- Score: {{score}}%
- Status: {{status}}
{{#if notes}}
- Notes: {{notes}}
{{/if}}

{{/each}}

**Current Gate Assessment:**
- Timestamp: {{CURRENT_TIMESTAMP}}
- Version: {{GATE_VERSION}}
- Assessor: {{ASSESSOR}}
- Result: {{GATE_STATUS}}

**Next Gate Assessment:**
- Trigger: {{NEXT_GATE_TRIGGER}}  <!-- Before release, after fixes, etc. -->
- Estimated Date: {{NEXT_GATE_DATE}}

---

## Sign-Off

{{#if REQUIRES_SIGNOFF}}

**Approval Required:**

- [ ] **Technical Lead:** {{TECH_LEAD_NAME}}
      Date: __________ Signature: __________

- [ ] **Quality Assurance:** {{QA_NAME}}
      Date: __________ Signature: __________

{{#if REQUIRES_ADDITIONAL_SIGNOFF}}
- [ ] **Security Review:** {{SECURITY_REVIEWER}}
      Date: __________ Signature: __________

- [ ] **Architecture Review:** {{ARCHITECT_NAME}}
      Date: __________ Signature: __________
{{/if}}

{{else}}

**No formal sign-off required.** Gate decision is advisory.

{{/if}}

---

## Notes

{{ADDITIONAL_NOTES}}

---

## Appendices

### Appendix A: Configuration

**Quality Gate Configuration:**
```yaml
{{GATE_CONFIGURATION}}
```

### Appendix B: Dimension Calculation Details

{{#each DIMENSION_CALCULATIONS}}
**{{dimension}}:**
```
{{calculation}}
```
{{/each}}

### Appendix C: Gap Summary

| Gap ID | Category | Severity | Status | Waived |
|--------|----------|----------|--------|--------|
{{GAP_SUMMARY_ROWS}}

---

## Version

**Gate Report Version:** {{REPORT_VERSION}}
**Template Version:** 1.0
**Assessment Date:** {{DATE}}
**Report Status:** {{REPORT_STATUS}}

---

<!-- End of Quality Gate Report -->
