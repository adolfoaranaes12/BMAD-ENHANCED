# Requirements Traceability Matrix: {{TASK_TITLE}}

**Task:** {{TASK_ID}}
**Date:** {{DATE}}
**Assessor:** {{ASSESSOR}}
**Status:** {{STATUS}}  <!-- Draft | Final | Updated -->

---

## Executive Summary

**Overall Traceability Score:** {{TRACEABILITY_SCORE}}%

**Coverage Metrics:**
- Implementation Coverage: {{IMPLEMENTATION_COVERAGE}}% ({{IMPLEMENTED_COUNT}}/{{TOTAL_AC}} AC implemented)
- Test Coverage: {{TEST_COVERAGE}}% ({{TESTED_COUNT}}/{{TOTAL_AC}} AC tested)
- Gap Coverage: {{GAP_COVERAGE}}% ({{TOTAL_GAPS}} gaps identified)

**Gap Distribution:**
- Critical (Score 9): {{CRITICAL_GAPS}} gaps
- High (Score 6-8): {{HIGH_GAPS}} gaps
- Medium (Score 3-5): {{MEDIUM_GAPS}} gaps
- Low (Score 1-2): {{LOW_GAPS}} gaps

**Quality Gate Impact:** {{QUALITY_GATE_STATUS}}
**Estimated Effort to Close P0 Gaps:** {{P0_EFFORT_HOURS}} hours

---

## Traceability Matrix

| AC | Requirement | Impl Status | Test Status | Gaps | Overall |
|----|-------------|-------------|-------------|------|---------|
{{TRACEABILITY_MATRIX_ROWS}}
<!-- Example row:
| AC-1 | User can sign up with email/password | ✅ signup.ts:15-42 | ✅ 3 tests (P0) | None | ✅ Complete |
| AC-2 | Password ≥8 characters | ✅ validators/auth.ts:23 | ⚠️ 1 test | GAP-2 (MED) | ⚠️ Partial |
| AC-4 | Rate-limit login attempts | ❌ Not impl | ❌ No tests | GAP-1 (HIGH) | ❌ Incomplete |
-->

**Legend:**
- ✅ Complete: Fully implemented and tested
- ⚠️ Partial: Implemented but incomplete test coverage
- ❌ Incomplete: Not implemented or not tested
- ❓ Unclear: Implementation exists but unclear if satisfies AC

---

## Detailed Traceability Entries

{{#each TRACEABILITY_ENTRIES}}
### {{ac_id}}: {{ac_text}}

**Implementation Status:** {{impl_status_icon}} {{impl_status}}

{{#if impl_evidence}}
**Implementation Evidence:**
{{#each impl_evidence}}
- **File:** {{file}}:{{lines}}
  {{#if function}}**Function:** {{function}}{{/if}}
  **Description:** {{description}}
  **Code Snippet:**
  ```{{language}}
  {{snippet}}
  ```
{{/each}}
{{else}}
**Implementation Evidence:** None found

**Impact:** {{no_impl_impact}}
{{/if}}

**Test Coverage:** {{test_status_icon}} {{test_status}}

{{#if test_evidence}}
**Test Evidence:**
{{#each test_evidence}}
{{test_number}}. **Test:** "{{test_name}}"
   - **File:** {{file}}:{{lines}}
   - **Type:** {{test_type}}, **Priority:** {{priority}}
   - **Scenario:** {{scenario}}
   {{#if assertions}}
   - **Key Assertions:**
     {{#each assertions}}
     - {{this}}
     {{/each}}
   {{/if}}
{{/each}}
{{else}}
**Test Evidence:** None found

**Missing Test Scenarios:**
{{#each missing_scenarios}}
- {{this}}
{{/each}}
{{/if}}

**Overall Status:** {{overall_status_icon}} {{overall_status}}

{{#if gaps}}
**Associated Gaps:**
{{#each gaps}}
- {{gap_id}}: {{gap_description}} ({{severity}})
{{/each}}
{{/if}}

{{#if notes}}
**Notes:**
{{notes}}
{{/if}}

---

{{/each}}

---

## Coverage Gaps

**Total Gaps:** {{TOTAL_GAPS}} ({{CRITICAL_GAPS}} Critical, {{HIGH_GAPS}} High, {{MEDIUM_GAPS}} Medium, {{LOW_GAPS}} Low)

### Critical Gaps (Score 9)

{{#each CRITICAL_GAPS}}
#### GAP-{{number}}: {{title}} (CRITICAL - Score {{score}})

**Type:** {{type}}  <!-- Implementation Gap | Test Gap -->
**Criterion:** {{criterion_id}} - "{{criterion_text}}"

**Severity Reasoning:**
{{severity_reasoning}}

**Impact:**
{{impact}}

**Related Risk:** {{#if related_risk}}{{related_risk}}{{else}}None identified{{/if}}

**Required Action:**
{{required_action}}

{{#if type == 'Implementation Gap'}}
**Recommended Implementation:**
```{{language}}
{{recommended_code}}
```

**Implementation Effort:** {{effort}} ({{effort_hours}})
{{/if}}

{{#if type == 'Test Gap'}}
**Missing Test Scenarios:**
{{#each missing_scenarios}}
- {{this}}
{{/each}}

**Recommended Tests:**
{{#each recommended_tests}}
**Test {{test_number}}:** {{test_name}}
- **Scenario:** {{scenario}}
- **Priority:** {{priority}}
- **Expected Result:** {{expected_result}}
- **Estimated Time:** {{time}}

{{/each}}
{{/if}}

**Priority:** {{priority}} ({{priority_label}})
**Estimated Effort:** {{effort}} - {{effort_hours}}

**Validation:**
{{validation}}

---

{{/each}}

### High-Severity Gaps (Score 6-8)

{{#each HIGH_GAPS}}
#### GAP-{{number}}: {{title}} (HIGH - Score {{score}})

**Type:** {{type}}
**Criterion:** {{criterion_id}} - "{{criterion_text}}"

**Impact:** {{impact}}

**Required Action:** {{required_action}}

**Priority:** {{priority}}
**Effort:** {{effort}} ({{effort_hours}})

{{#if recommended_approach}}
**Recommended Approach:**
{{recommended_approach}}
{{/if}}

---

{{/each}}

### Medium-Severity Gaps (Score 3-5)

{{#each MEDIUM_GAPS}}
#### GAP-{{number}}: {{title}} (MEDIUM - Score {{score}})

**Type:** {{type}}
**Criterion:** {{criterion_id}}
**Impact:** {{impact}}
**Action:** {{required_action}}
**Effort:** {{effort}} ({{effort_hours}})

---

{{/each}}

### Low-Severity Gaps (Score 1-2)

{{#each LOW_GAPS}}
- **GAP-{{number}}**: {{title}} ({{type}}, Score {{score}}) - {{criterion_id}}: {{required_action}} [Effort: {{effort}}]
{{/each}}

---

## Recommendations

### Immediate Actions (Before Merge - P0)

{{#each P0_ACTIONS}}
**{{action_number}}. [{{gap_id}}] {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Effort:** {{effort}} ({{effort_hours}})
- **Action:** {{action}}
- **Tests:** {{tests_required}}
- **Acceptance:** {{acceptance_criteria}}

{{/each}}

{{#if no_p0_actions}}
✅ No P0 actions required. All critical and high-severity gaps addressed.
{{/if}}

### Short-Term Actions (Before Release - P1)

{{#each P1_ACTIONS}}
**{{action_number}}. [{{gap_id}}] {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Effort:** {{effort}} ({{effort_hours}})
- **Action:** {{action}}

{{/each}}

### Long-Term Actions (Future Enhancement - P2)

{{#each P2_ACTIONS}}
**{{action_number}}. [{{gap_id}}] {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Effort:** {{effort}} ({{effort_hours}})
- **Action:** {{action}}

{{/each}}

---

## Quality Gate Impact

**Current Traceability Metrics:**
- Implementation Coverage: {{IMPLEMENTATION_COVERAGE}}%
- Test Coverage: {{TEST_COVERAGE}}%
- Overall Traceability Score: {{TRACEABILITY_SCORE}}%

**Gap Distribution:**
- Critical: {{CRITICAL_GAPS}} (requires immediate attention)
- High: {{HIGH_GAPS}} (should be addressed before merge)
- Medium: {{MEDIUM_GAPS}} (can be deferred to follow-up)
- Low: {{LOW_GAPS}} (future enhancement)

**Quality Gate Prediction:** **{{QUALITY_GATE_STATUS}}**

**Reasoning:**
{{QUALITY_GATE_REASONING}}

{{#if QUALITY_GATE_STATUS == 'PASS'}}
**Excellent traceability!**
→ All acceptance criteria implemented and tested
→ No critical or high-severity gaps
→ Coverage metrics exceed thresholds
→ Ready for quality gate review
{{/if}}

{{#if QUALITY_GATE_STATUS == 'CONCERNS'}}
**Traceability concerns identified:**
→ {{CONCERNS_SUMMARY}}

**To Achieve PASS:**
{{#each PASS_REQUIREMENTS}}
{{step_number}}. {{requirement}} [{{effort}}]
{{/each}}

**Estimated Total Effort:** {{PASS_EFFORT_HOURS}} hours
{{/if}}

{{#if QUALITY_GATE_STATUS == 'FAIL'}}
**Traceability failures:**
→ {{FAIL_SUMMARY}}

**Critical Issues:**
{{#each CRITICAL_ISSUES}}
- {{issue}} (Blocks merge)
{{/each}}

**Required Actions Before Re-Review:**
{{#each REQUIRED_ACTIONS}}
{{step_number}}. {{action}} [{{effort}}]
{{/each}}
{{/if}}

---

## Integration with Other Assessments

### Risk Profile Integration

{{#if RISK_PROFILE_EXISTS}}
**Risk Profile:** `.claude/quality/assessments/{{TASK_ID}}-risk-{{RISK_DATE}}.md`

**Cross-Reference:**
{{#each RISK_CROSS_REFERENCES}}
- **Risk #{{risk_number}}:** {{risk_title}} (Score: {{risk_score}})
  - **Traceability:** {{trace_status}}
  - **Implementation:** {{impl_status}}
  - **Tests:** {{test_status}}
  {{#if gaps}}
  - **Gaps:** {{gaps}}
  {{/if}}
{{/each}}

**Risk-Informed Gap Severity:**
- Gaps in high-risk areas (score ≥6) elevated to CRITICAL or HIGH
- Gaps with mitigations in place reduced to MEDIUM
- All security gaps treated as minimum HIGH severity
{{else}}
**Risk Profile:** Not available

**Note:** Gap severity assessment performed without risk profile data. Consider running risk-profile skill for more accurate severity ratings.
{{/if}}

### Test Design Integration

{{#if TEST_DESIGN_EXISTS}}
**Test Design:** `.claude/quality/assessments/{{TASK_ID}}-test-design-{{TEST_DATE}}.md`

**Cross-Reference:**
- Total Test Scenarios: {{TOTAL_TEST_SCENARIOS}}
- P0 Tests: {{P0_TESTS}} (all mapped to AC)
- P1 Tests: {{P1_TESTS}} ({{P1_MAPPED}} mapped to AC, {{P1_UNMAPPED}} unmapped)
- P2 Tests: {{P2_TESTS}} ({{P2_MAPPED}} mapped to AC, {{P2_UNMAPPED}} unmapped)

**Coverage Validation:**
{{#each TEST_COVERAGE_VALIDATION}}
- **AC-{{ac_id}}:** {{test_count}} tests planned, {{test_implemented}} implemented, {{test_missing}} missing
{{/each}}

**Unmapped Tests:**
{{#if UNMAPPED_TESTS}}
{{#each UNMAPPED_TESTS}}
- {{test_name}} ({{priority}}) - Test not linked to any AC (potential over-testing or missing AC)
{{/each}}
{{else}}
✅ All tests mapped to acceptance criteria
{{/if}}
{{else}}
**Test Design:** Not available

**Note:** Traceability analysis performed without test design data. Test coverage based on actual implementation only.
{{/if}}

---

## Traceability Best Practices

### For Future Tasks:

**During Planning:**
1. Write clear, testable acceptance criteria
2. Number AC sequentially (AC-1, AC-2, etc.)
3. Ensure AC are SMART (Specific, Measurable, Achievable, Relevant, Testable)

**During Implementation:**
4. Reference AC IDs in code comments: `// Implements AC-1, AC-3`
5. Reference AC IDs in commit messages: `feat: user signup (AC-1, AC-2)`
6. Implement and test simultaneously (TDD approach)
7. Update Implementation Record section with file references

**During Testing:**
8. Reference AC IDs in test names: `it('should satisfy AC-1: user signup', ...)`
9. Use Given-When-Then format for clarity
10. Ensure each AC has at least one P0 test

**Before Review:**
11. Run traceability analysis: `@quinn *trace task-ID`
12. Close all P0 gaps
13. Document any waived gaps with rationale
14. Re-run traceability after closing gaps

### For This Task:

**Immediate Steps:**
1. Review detailed traceability matrix above
2. Prioritize P0 gaps ({{P0_GAP_COUNT}} gaps requiring immediate attention)
3. Close critical and high-severity gaps
4. Add missing tests for untested AC
5. Update Implementation Record with gap closure evidence

**Before Marking "Review":**
6. Re-run trace-requirements skill to verify all gaps closed
7. Ensure traceability score ≥80%
8. Verify implementation coverage ≥90% and test coverage ≥85%
9. Document any remaining gaps with waiver rationale

**During Quality Review:**
10. Provide traceability report to reviewer
11. Walk through gap closure evidence
12. Demonstrate AC → Implementation → Test chain

---

## Appendices

### Appendix A: Test Inventory

**Total Tests:** {{TOTAL_TESTS}}
**By Type:**
- Unit: {{UNIT_TESTS}} ({{UNIT_PERCENTAGE}}%)
- Integration: {{INTEGRATION_TESTS}} ({{INTEGRATION_PERCENTAGE}}%)
- E2E: {{E2E_TESTS}} ({{E2E_PERCENTAGE}}%)

**By Priority:**
- P0 (Critical): {{P0_TEST_COUNT}}
- P1 (High): {{P1_TEST_COUNT}}
- P2 (Medium): {{P2_TEST_COUNT}}

**Test Files:**
{{#each TEST_FILES}}
- {{file_path}} ({{test_count}} tests, {{test_types}})
{{/each}}

### Appendix B: Implementation File Inventory

**Files Created/Modified:** {{IMPL_FILE_COUNT}}

{{#each IMPL_FILES}}
**{{file_number}}. {{file_path}}**
- **Lines Changed:** {{lines_changed}}
- **Components:** {{components}}
- **Implements:** {{ac_list}}
- **Status:** {{status}}

{{/each}}

### Appendix C: Risk Cross-Reference

{{#if RISK_PROFILE_EXISTS}}
| Risk | Score | Related AC | Impl Status | Test Status | Gaps |
|------|-------|------------|-------------|-------------|------|
{{RISK_CROSS_REFERENCE_ROWS}}
<!-- Example:
| Brute force attacks | 8 | AC-4 | ❌ Not impl | ❌ No tests | GAP-1 (HIGH) |
| SQL injection | 6 | AC-2, AC-5 | ✅ Impl | ⚠️ Partial | GAP-3 (MED) |
-->
{{else}}
Risk profile not available. Run risk-profile skill for risk-informed traceability.
{{/if}}

### Appendix D: Acceptance Criteria Checklist

{{#each AC_CHECKLIST}}
- [{{checkbox}}] **AC-{{ac_id}}:** {{ac_text}}
  - Implementation: {{impl_status}}
  - Tests: {{test_status}}
  - Overall: {{overall_status}}
{{/each}}

**Progress:** {{AC_COMPLETE_COUNT}}/{{TOTAL_AC}} complete ({{AC_COMPLETE_PERCENTAGE}}%)

---

## Audit Trail

**Assessment History:**

{{#each ASSESSMENT_HISTORY}}
**{{version}}. {{date}} - {{assessor}}**
- Traceability Score: {{score}}%
- Gaps: {{gaps}} ({{critical}} Critical, {{high}} High, {{medium}} Medium, {{low}} Low)
- Status: {{status}}
- Changes: {{changes}}

{{/each}}

**Current Version:** {{CURRENT_VERSION}}
**Next Reassessment:** {{NEXT_REASSESSMENT}}  <!-- After gap closure, before quality gate, etc. -->

---

## Notes

{{ADDITIONAL_NOTES}}

---

## Version

**Traceability Report Version:** {{REPORT_VERSION}}
**Template Version:** 1.0
**Assessment Date:** {{DATE}}
**Next Review:** {{NEXT_REVIEW_DATE}}
**Report Status:** {{REPORT_STATUS}}  <!-- Draft | Final | Updated -->

---

<!-- End of Requirements Traceability Matrix -->
