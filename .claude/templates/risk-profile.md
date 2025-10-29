# Risk Profile: {{TASK_TITLE}}

**Task:** {{TASK_ID}}
**Date:** {{DATE}}
**Assessor:** {{ASSESSOR}}
**Status:** {{STATUS}}  <!-- Pre-Implementation | During Development | Post-Implementation -->

---

## Risk Summary

**Total Risks Identified:** {{TOTAL_RISKS}}
**Critical (≥7):** {{CRITICAL_COUNT}}
**High (6):** {{HIGH_COUNT}}
**Medium (3-5):** {{MEDIUM_COUNT}}
**Low (1-2):** {{LOW_COUNT}}

**Quality Gate Impact:**
- Risk score threshold: {{THRESHOLD}} (from config)
- Risks ≥{{THRESHOLD}}: {{CONCERNING_RISKS}} risks identified
- **Predicted Gate Status:** {{PREDICTED_STATUS}}
- **To Achieve PASS:** {{PASS_REQUIREMENTS}}

---

## Risk Matrix

| # | Category | Risk | P | I | Score | Mitigation |
|---|----------|------|---|---|-------|------------|
{{RISK_MATRIX_ROWS}}
<!-- Example row:
| 1 | Security | SQL injection in input | 2 | 3 | **6** | Use parameterized queries, input validation |
-->

---

## Critical Risks (Score ≥7)

{{#each CRITICAL_RISKS}}
### Risk {{number}}: {{title}} (Score: {{score}})

**Category:** {{category}}
**Probability:** {{probability}} ({{probability_label}}) - {{probability_reasoning}}
**Impact:** {{impact}} ({{impact_label}}) - {{impact_reasoning}}

**Description:**
{{description}}

**Mitigation Strategy:**

**Prevention:**
{{prevention_steps}}

**Detection:**
{{detection_steps}}

**Recovery:**
{{recovery_steps}}

**Concrete Actions:**
{{concrete_actions}}

**Phase:** {{phase}}
**Effort:** {{effort}}
**Validation:** {{validation}}

---
{{/each}}

## High-Risk Areas (Score ≥6)

{{#each HIGH_RISKS}}
### Risk {{number}}: {{title}} (Score: {{score}})

**Category:** {{category}}
**Probability:** {{probability}} ({{probability_label}})
**Impact:** {{impact}} ({{impact_label}})

**Description:**
{{description}}

**Mitigation:**
{{mitigation_summary}}

**Validation:**
{{validation_approach}}

---
{{/each}}

## Medium-Risk Areas (Score 3-5)

{{#each MEDIUM_RISKS}}
### Risk {{number}}: {{title}} (Score: {{score}})

**Category:** {{category}}
**P×I:** {{probability}} × {{impact}}

**Description:** {{description}}

**Mitigation:** {{mitigation_summary}}

---
{{/each}}

## Low-Risk Areas (Score 1-2)

{{#each LOW_RISKS}}
- **{{title}}** ({{category}}, Score: {{score}}): {{description}}
{{/each}}

---

## Test Prioritization

### P0 (Critical) - Must Have Before Merge

{{#each P0_TESTS}}
**{{category}} Test {{number}}:**
{{title}}
- Test: {{test_file}}
- Scenario: {{scenario}}
- Expected: {{expected_result}}
- Validates Risk: #{{risk_number}} ({{risk_title}})

{{/each}}

### P1 (High) - Should Have Before Merge

{{#each P1_TESTS}}
**{{category}} Test {{number}}:**
{{title}}
- Test: {{test_file}}
- Scenario: {{scenario}}
- Expected: {{expected_result}}
- Validates Risk: #{{risk_number}} ({{risk_title}})

{{/each}}

### P2 (Medium) - Nice to Have

{{#each P2_TESTS}}
**{{category}} Test {{number}}:**
{{title}}
- Test: {{test_file}}
- Scenario: {{scenario}}
- Validates Risk: #{{risk_number}} ({{risk_title}})

{{/each}}

---

## Quality Gate Impact

**Current Risk Score Distribution:**
- Critical (≥7): {{CRITICAL_COUNT}} risk(s)
- High (6): {{HIGH_COUNT}} risk(s)
- Medium (3-5): {{MEDIUM_COUNT}} risk(s)
- Low (1-2): {{LOW_COUNT}} risk(s)

**Quality Gate Prediction:**

**If all high-risk items mitigated and tested:**
→ **PASS** ({{pass_reasoning}})

**If high-risk items not fully addressed:**
→ **CONCERNS** ({{concerns_reasoning}})

**If critical risk not mitigated:**
→ **FAIL** ({{fail_reasoning}})

**Recommendation:**
{{recommendation}}

---

## Implementation Guidance

**Before Starting Implementation:**
1. {{guidance_before_1}}
2. {{guidance_before_2}}
3. {{guidance_before_3}}

**During Implementation:**
4. {{guidance_during_1}}
5. {{guidance_during_2}}
6. {{guidance_during_3}}

**Before Marking Ready for Review:**
7. {{guidance_before_review_1}}
8. {{guidance_before_review_2}}
9. {{guidance_before_review_3}}

**During Quality Review:**
10. {{guidance_review_1}}
11. {{guidance_review_2}}
12. {{guidance_review_3}}

---

## Risk-Test Mapping

| Risk | Score | Test(s) | Priority | Status |
|------|-------|---------|----------|--------|
{{RISK_TEST_MAPPING_ROWS}}
<!-- Example row:
| SQL injection | 6 | injection.test.ts | P0 | Not Implemented |
-->

---

## Notes

{{ADDITIONAL_NOTES}}

---

## Version

**Risk Profile Version:** 1.0
**Template Version:** 1.0
**Assessment Date:** {{DATE}}
**Reassess If:** {{REASSESS_CONDITIONS}}

---

<!-- End of Risk Profile -->
