# Non-Functional Requirements Assessment: {{TASK_TITLE}}

**Task:** {{TASK_ID}}
**Date:** {{DATE}}
**Assessor:** {{ASSESSOR}}
**Status:** {{STATUS}}  <!-- Draft | Final | Updated -->

---

## Executive Summary

**Overall NFR Score:** {{OVERALL_NFR_SCORE}}% ({{OVERALL_STATUS}})

**Category Scores:**
- Security: {{SECURITY_SCORE}}% ({{SECURITY_STATUS}})
- Performance: {{PERFORMANCE_SCORE}}% ({{PERFORMANCE_STATUS}})
- Reliability: {{RELIABILITY_SCORE}}% ({{RELIABILITY_STATUS}})
- Maintainability: {{MAINTAINABILITY_SCORE}}% ({{MAINTAINABILITY_STATUS}})
- Scalability: {{SCALABILITY_SCORE}}% ({{SCALABILITY_STATUS}})
- Usability: {{USABILITY_SCORE}}% ({{USABILITY_STATUS}})

**Critical NFR Gaps:** {{CRITICAL_NFR_GAPS}} (require immediate attention)
**High NFR Gaps:** {{HIGH_NFR_GAPS}} (should be addressed before release)

**Quality Gate Impact:** {{QUALITY_GATE_STATUS}}
**Estimated Effort to Achieve PASS:** {{PASS_EFFORT_HOURS}} hours

---

## NFR Score Summary

| Category | Score | Status | Critical Gaps | High Gaps | Weight |
|----------|-------|--------|---------------|-----------|--------|
| Security | {{SECURITY_SCORE}}% | {{SECURITY_STATUS}} | {{SECURITY_CRITICAL}} | {{SECURITY_HIGH}} | 25% |
| Performance | {{PERFORMANCE_SCORE}}% | {{PERFORMANCE_STATUS}} | {{PERFORMANCE_CRITICAL}} | {{PERFORMANCE_HIGH}} | 20% |
| Reliability | {{RELIABILITY_SCORE}}% | {{RELIABILITY_STATUS}} | {{RELIABILITY_CRITICAL}} | {{RELIABILITY_HIGH}} | 20% |
| Maintainability | {{MAINTAINABILITY_SCORE}}% | {{MAINTAINABILITY_STATUS}} | {{MAINTAINABILITY_CRITICAL}} | {{MAINTAINABILITY_HIGH}} | 15% |
| Scalability | {{SCALABILITY_SCORE}}% | {{SCALABILITY_STATUS}} | {{SCALABILITY_CRITICAL}} | {{SCALABILITY_HIGH}} | 10% |
| Usability | {{USABILITY_SCORE}}% | {{USABILITY_STATUS}} | {{USABILITY_CRITICAL}} | {{USABILITY_HIGH}} | 10% |
| **Overall** | **{{OVERALL_NFR_SCORE}}%** | **{{OVERALL_STATUS}}** | **{{TOTAL_CRITICAL}}** | **{{TOTAL_HIGH}}** | **100%** |

**Legend:**
- ✅ PASS (≥75%): Acceptable quality level
- ⚠️ CONCERNS (60-74%): Needs improvement
- ❌ FAIL (<60%): Critical issues, blocks production

---

## 1. Security Assessment

**Overall Security Score:** {{SECURITY_SCORE}}% ({{SECURITY_STATUS}})

### Security Criteria Evaluation

{{#each SECURITY_CRITERIA}}
#### {{number}}. {{name}} {{status_icon}} {{status}}

**Criterion:** {{description}}

{{#if evidence}}
**Evidence:**
{{#each evidence}}
- **File:** {{file}}{{#if lines}}:{{lines}}{{/if}}
  {{#if function}}**Function:** {{function}}{{/if}}
  **Description:** {{description}}
  {{#if code}}
  **Code:**
  ```{{language}}
  {{code}}
  ```
  {{/if}}
{{/each}}
{{else}}
**Evidence:** None found
{{/if}}

**Status:** {{status}}

{{#if gaps}}
**Gaps:**
{{#each gaps}}
- {{this}}
{{/each}}
{{/if}}

{{#if recommendations}}
**Recommendations:**
{{#each recommendations}}
- {{this}}
{{/each}}
{{/if}}

{{#if notes}}
**Notes:** {{notes}}
{{/if}}

---

{{/each}}

### Automated Security Checks

**Dependency Vulnerability Scan:**
- Tool: {{vuln_scan_tool}} (npm audit, Snyk, etc.)
- Scan Date: {{vuln_scan_date}}
- Results:
  - Critical: {{vuln_critical}} vulnerabilities
  - High: {{vuln_high}} vulnerabilities
  - Moderate: {{vuln_moderate}} vulnerabilities
  - Low: {{vuln_low}} vulnerabilities

{{#if vuln_critical_details}}
**Critical Vulnerabilities:**
{{#each vuln_critical_details}}
{{number}}. **{{package}}@{{version}}** - {{vulnerability}}
   - CVE: {{cve}}
   - Severity: CRITICAL
   - Description: {{description}}
   - Fix: {{fix}}
{{/each}}
{{/if}}

**Secret Detection:**
- Tool: {{secret_scan_tool}}
- Scan Date: {{secret_scan_date}}
- Secrets Found: {{secrets_found}}
{{#if secrets_found > 0}}
- Files with Secrets:
{{#each secret_files}}
  - {{file}}: {{secret_type}}
{{/each}}
{{/if}}

### Security Gaps

{{#each SECURITY_GAPS}}
**GAP-SEC-{{number}}: {{title}} ({{severity}})**
- **Type:** {{type}}
- **Impact:** {{impact}}
- **Risk Score:** {{risk_score}}
- **Action:** {{action}}
- **Priority:** {{priority}}
- **Effort:** {{effort}} ({{effort_hours}})

{{/each}}

---

## 2. Performance Assessment

**Overall Performance Score:** {{PERFORMANCE_SCORE}}% ({{PERFORMANCE_STATUS}})

### Performance Criteria Evaluation

{{#each PERFORMANCE_CRITERIA}}
#### {{number}}. {{name}} {{status_icon}} {{status}}

**Criterion:** {{description}}

{{#if benchmarks}}
**Benchmark Results:**
{{#each benchmarks}}
- **Metric:** {{metric}}
- **Result:** {{result}}
- **Threshold:** {{threshold}}
- **Status:** {{status}}
{{/each}}
{{/if}}

{{#if evidence}}
**Evidence:**
{{#each evidence}}
- {{description}}
  {{#if code}}
  ```{{language}}
  {{code}}
  ```
  {{/if}}
{{/each}}
{{/if}}

**Status:** {{status}}

{{#if gaps}}
**Gaps:** {{gaps}}
{{/if}}

{{#if recommendations}}
**Recommendations:** {{recommendations}}
{{/if}}

---

{{/each}}

### Load Test Results

{{#if LOAD_TEST_AVAILABLE}}
**Test Configuration:**
- Tool: {{load_test_tool}}
- Duration: {{test_duration}}
- Target Load: {{target_load}} req/s
- Ramp-up: {{ramp_up}}

**Results:**

| Endpoint | Avg (ms) | p50 (ms) | p95 (ms) | p99 (ms) | Success Rate | Errors |
|----------|----------|----------|----------|----------|--------------|--------|
{{LOAD_TEST_RESULTS_ROWS}}

**Analysis:**
{{load_test_analysis}}

{{else}}
**Load Testing:** Not performed

**Recommendation:** Run load tests to validate performance under expected load.
{{/if}}

### Performance Gaps

{{#each PERFORMANCE_GAPS}}
**GAP-PERF-{{number}}: {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Metric:** {{metric}} (Current: {{current}}, Target: {{target}})
- **Action:** {{action}}
- **Priority:** {{priority}}
- **Effort:** {{effort}}

{{/each}}

---

## 3. Reliability Assessment

**Overall Reliability Score:** {{RELIABILITY_SCORE}}% ({{RELIABILITY_STATUS}})

### Reliability Criteria Evaluation

{{#each RELIABILITY_CRITERIA}}
#### {{number}}. {{name}} {{status_icon}} {{status}}

**Criterion:** {{description}}

**Evidence:**
{{#if evidence}}
{{#each evidence}}
- {{description}}
  {{#if code}}
  ```{{language}}
  {{code}}
  ```
  {{/if}}
{{/each}}
{{else}}
No evidence found
{{/if}}

**Status:** {{status}}

{{#if gaps}}
**Gaps:** {{gaps}}
{{/if}}

{{#if recommendations}}
**Recommendations:** {{recommendations}}
{{/if}}

---

{{/each}}

### Reliability Gaps

{{#each RELIABILITY_GAPS}}
**GAP-REL-{{number}}: {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Priority:** {{priority}}
- **Effort:** {{effort}}

{{/each}}

---

## 4. Maintainability Assessment

**Overall Maintainability Score:** {{MAINTAINABILITY_SCORE}}% ({{MAINTAINABILITY_STATUS}})

### Maintainability Criteria Evaluation

{{#each MAINTAINABILITY_CRITERIA}}
#### {{number}}. {{name}} {{status_icon}} {{status}}

**Criterion:** {{description}}

{{#if metrics}}
**Metrics:**
{{#each metrics}}
- {{metric}}: {{value}} (Threshold: {{threshold}}, Status: {{status}})
{{/each}}
{{/if}}

**Evidence:**
{{evidence}}

**Status:** {{status}}

{{#if gaps}}
**Gaps:** {{gaps}}
{{/if}}

{{#if recommendations}}
**Recommendations:** {{recommendations}}
{{/if}}

---

{{/each}}

### Code Quality Metrics

**Test Coverage:**
- Statements: {{coverage_statements}}% (Threshold: {{coverage_threshold_statements}}%)
- Branches: {{coverage_branches}}% (Threshold: {{coverage_threshold_branches}}%)
- Functions: {{coverage_functions}}% (Threshold: {{coverage_threshold_functions}}%)
- Lines: {{coverage_lines}}% (Threshold: {{coverage_threshold_lines}}%)

**Code Complexity:**
- Average Complexity: {{avg_complexity}} (Threshold: ≤10)
- Max Complexity: {{max_complexity}} (in {{max_complexity_file}})
- Functions >10: {{high_complexity_count}}

**Code Duplication:**
- Duplication Rate: {{duplication_rate}}% (Threshold: <5%)
- Duplicated Blocks: {{duplicated_blocks}}

**Linting:**
- Errors: {{lint_errors}}
- Warnings: {{lint_warnings}}
- Status: {{lint_status}}

### Maintainability Gaps

{{#each MAINTAINABILITY_GAPS}}
**GAP-MAINT-{{number}}: {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Priority:** {{priority}}
- **Effort:** {{effort}}

{{/each}}

---

## 5. Scalability Assessment

**Overall Scalability Score:** {{SCALABILITY_SCORE}}% ({{SCALABILITY_STATUS}})

### Scalability Criteria Evaluation

{{#each SCALABILITY_CRITERIA}}
#### {{number}}. {{name}} {{status_icon}} {{status}}

**Criterion:** {{description}}

**Evidence:**
{{evidence}}

**Status:** {{status}}

{{#if gaps}}
**Gaps:** {{gaps}}
{{/if}}

{{#if recommendations}}
**Recommendations:** {{recommendations}}
{{/if}}

---

{{/each}}

### Scalability Gaps

{{#each SCALABILITY_GAPS}}
**GAP-SCALE-{{number}}: {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Priority:** {{priority}}
- **Effort:** {{effort}}

{{/each}}

---

## 6. Usability Assessment

**Overall Usability Score:** {{USABILITY_SCORE}}% ({{USABILITY_STATUS}})

### Usability Criteria Evaluation

{{#each USABILITY_CRITERIA}}
#### {{number}}. {{name}} {{status_icon}} {{status}}

**Criterion:** {{description}}

**Evidence:**
{{evidence}}

**Status:** {{status}}

{{#if gaps}}
**Gaps:** {{gaps}}
{{/if}}

{{#if recommendations}}
**Recommendations:** {{recommendations}}
{{/if}}

---

{{/each}}

### Usability Gaps

{{#each USABILITY_GAPS}}
**GAP-USE-{{number}}: {{title}} ({{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Priority:** {{priority}}
- **Effort:** {{effort}}

{{/each}}

---

## Gap Summary

**Total NFR Gaps:** {{TOTAL_NFR_GAPS}}

**By Severity:**
- Critical: {{CRITICAL_NFR_GAPS}} (requires immediate action)
- High: {{HIGH_NFR_GAPS}} (should fix before release)
- Medium: {{MEDIUM_NFR_GAPS}} (can defer to follow-up)
- Low: {{LOW_NFR_GAPS}} (future enhancement)

**By Category:**
- Security: {{SECURITY_GAP_COUNT}} gaps ({{SECURITY_CRITICAL}} critical, {{SECURITY_HIGH}} high)
- Performance: {{PERFORMANCE_GAP_COUNT}} gaps ({{PERFORMANCE_CRITICAL}} critical, {{PERFORMANCE_HIGH}} high)
- Reliability: {{RELIABILITY_GAP_COUNT}} gaps ({{RELIABILITY_CRITICAL}} critical, {{RELIABILITY_HIGH}} high)
- Maintainability: {{MAINTAINABILITY_GAP_COUNT}} gaps ({{MAINTAINABILITY_CRITICAL}} critical, {{MAINTAINABILITY_HIGH}} high)
- Scalability: {{SCALABILITY_GAP_COUNT}} gaps ({{SCALABILITY_CRITICAL}} critical, {{SCALABILITY_HIGH}} high)
- Usability: {{USABILITY_GAP_COUNT}} gaps ({{USABILITY_CRITICAL}} critical, {{USABILITY_HIGH}} high)

### Critical Gaps (P0 - Must Fix Before Merge)

{{#each CRITICAL_GAPS}}
**{{gap_number}}. {{gap_id}}: {{title}} ({{category}})**
- **Severity:** CRITICAL
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Effort:** {{effort}} ({{effort_hours}})
- **Validation:** {{validation}}

{{/each}}

### High-Severity Gaps (P1 - Should Fix Before Release)

{{#each HIGH_GAPS}}
**{{gap_number}}. {{gap_id}}: {{title}} ({{category}})**
- **Severity:** HIGH
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Effort:** {{effort}} ({{effort_hours}})

{{/each}}

### Medium-Severity Gaps (P2 - Can Defer)

{{#each MEDIUM_GAPS}}
- **{{gap_id}}**: {{title}} ({{category}}) - {{action}} [{{effort}}]
{{/each}}

---

## Recommendations

### Immediate Actions (P0 - Before Merge)

{{#each P0_ACTIONS}}
**{{action_number}}. [{{gap_id}}] {{title}} ({{category}} - {{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Effort:** {{effort}} ({{effort_hours}})
- **Validation:** {{validation}}

{{/each}}

{{#if no_p0_actions}}
✅ No P0 actions required. All critical NFR gaps addressed.
{{/if}}

### Short-Term Actions (P1 - Before Release)

{{#each P1_ACTIONS}}
**{{action_number}}. [{{gap_id}}] {{title}} ({{category}} - {{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Effort:** {{effort}} ({{effort_hours}})

{{/each}}

### Long-Term Actions (P2 - Future Enhancement)

{{#each P2_ACTIONS}}
**{{action_number}}. [{{gap_id}}] {{title}} ({{category}} - {{severity}})**
- **Impact:** {{impact}}
- **Action:** {{action}}
- **Effort:** {{effort}}

{{/each}}

---

## Quality Gate Impact

**Current NFR Status:** **{{QUALITY_GATE_STATUS}}**

**Scoring Breakdown:**
- Security (25% weight): {{SECURITY_SCORE}}% × 0.25 = {{SECURITY_WEIGHTED}}
- Performance (20% weight): {{PERFORMANCE_SCORE}}% × 0.20 = {{PERFORMANCE_WEIGHTED}}
- Reliability (20% weight): {{RELIABILITY_SCORE}}% × 0.20 = {{RELIABILITY_WEIGHTED}}
- Maintainability (15% weight): {{MAINTAINABILITY_SCORE}}% × 0.15 = {{MAINTAINABILITY_WEIGHTED}}
- Scalability (10% weight): {{SCALABILITY_SCORE}}% × 0.10 = {{SCALABILITY_WEIGHTED}}
- Usability (10% weight): {{USABILITY_SCORE}}% × 0.10 = {{USABILITY_WEIGHTED}}

**Overall NFR Score:** {{OVERALL_NFR_SCORE}}%

**Gate Thresholds:**
- PASS: ≥75% overall, no category <50%, no critical gaps in security/reliability
- CONCERNS: 60-74% overall, or category <75%, or critical gaps present
- FAIL: <60% overall, or security/reliability <50%

**Reasoning:**
{{QUALITY_GATE_REASONING}}

{{#if QUALITY_GATE_STATUS == 'PASS'}}
**Excellent NFR compliance!**
→ All categories meet minimum thresholds
→ No critical gaps in security or reliability
→ Overall score exceeds 75%
→ Ready for quality gate review
{{/if}}

{{#if QUALITY_GATE_STATUS == 'CONCERNS'}}
**NFR concerns identified:**
→ {{CONCERNS_SUMMARY}}

**To Achieve PASS:**
{{#each PASS_REQUIREMENTS}}
{{step_number}}. {{requirement}} [{{effort}}]
{{/each}}

**Estimated Total Effort:** {{PASS_EFFORT_HOURS}} hours

**Recommendation:** {{RECOMMENDATION}}
{{/if}}

{{#if QUALITY_GATE_STATUS == 'FAIL'}}
**NFR failures:**
→ {{FAIL_SUMMARY}}

**Critical Issues:**
{{#each CRITICAL_ISSUES}}
- {{issue}} (Blocks production deployment)
{{/each}}

**Required Actions Before Re-Review:**
{{#each REQUIRED_ACTIONS}}
{{step_number}}. {{action}} [{{effort}}]
{{/each}}

**Estimated Total Effort:** {{REQUIRED_EFFORT_HOURS}} hours
{{/if}}

---

## Integration with Other Assessments

### Risk Profile Integration

{{#if RISK_PROFILE_EXISTS}}
**Risk Profile:** `.claude/quality/assessments/{{TASK_ID}}-risk-{{RISK_DATE}}.md`

**Risk-NFR Cross-Reference:**

{{#each RISK_NFR_CROSS_REFERENCE}}
**Risk #{{risk_number}}: {{risk_title}} (Score: {{risk_score}})**
- **NFR Category:** {{nfr_category}}
- **NFR Assessment:** {{nfr_assessment}}
- **NFR Gaps:** {{nfr_gaps}}
- **Alignment:** {{alignment_status}}

{{/each}}

**Risk-Informed Gap Prioritization:**
- High-risk areas with NFR gaps elevated to CRITICAL
- Risks with NFR mitigation validated against implementation
- All security gaps cross-referenced with security risks

{{else}}
**Risk Profile:** Not available

**Note:** NFR assessment performed without risk profile. Consider running risk-profile skill for risk-informed gap prioritization.
{{/if}}

### Traceability Integration

{{#if TRACEABILITY_EXISTS}}
**Traceability Matrix:** `.claude/quality/assessments/{{TASK_ID}}-trace-{{TRACE_DATE}}.md`

**NFR-Traceability Cross-Reference:**
- Implementation Coverage: {{IMPL_COVERAGE}}%
- Test Coverage: {{TEST_COVERAGE}}%
- NFR Evidence: {{NFR_EVIDENCE_COUNT}} references from traceability
- Coverage Gaps aligned with NFR gaps

{{else}}
**Traceability Matrix:** Not available

**Note:** NFR evidence collected independently. Run trace-requirements for full bidirectional traceability.
{{/if}}

---

## Best Practices

**For Future Tasks:**

**During Planning:**
1. Define explicit NFR requirements in task specification
2. Set measurable thresholds for performance, reliability, etc.
3. Identify NFR tools (security scanners, load testing, monitoring)

**During Implementation:**
4. Run security scans frequently (npm audit, Snyk)
5. Monitor performance metrics during development
6. Implement monitoring/logging from the start
7. Write tests for NFR scenarios (error handling, edge cases, performance)

**Before Review:**
8. Run all automated NFR checks
9. Fix critical security vulnerabilities
10. Validate performance under load
11. Ensure monitoring/observability in place
12. Run nfr-assess skill

**For This Task:**

**Immediate Steps:**
1. Review NFR assessment above
2. Prioritize P0 gaps ({{P0_GAP_COUNT}} gaps)
3. Fix critical security/reliability gaps
4. Update dependencies, add monitoring
5. Re-run automated checks

**Before Quality Gate:**
6. Achieve overall NFR score ≥75%
7. Ensure no category <50%
8. Close all critical gaps
9. Document any waived gaps
10. Re-run nfr-assess to verify improvements

---

## Audit Trail

**Assessment History:**

{{#each ASSESSMENT_HISTORY}}
**{{version}}. {{date}} - {{assessor}}**
- Overall NFR Score: {{score}}%
- Status: {{status}}
- Critical Gaps: {{critical_gaps}}
- High Gaps: {{high_gaps}}
- Changes: {{changes}}

{{/each}}

**Current Version:** {{CURRENT_VERSION}}
**Next Reassessment:** {{NEXT_REASSESSMENT}}

---

## Appendices

### Appendix A: Automated Check Outputs

**Security Scan Output:**
```json
{{SECURITY_SCAN_OUTPUT}}
```

**Lint Report:**
```json
{{LINT_REPORT}}
```

**Coverage Report:**
```
{{COVERAGE_REPORT}}
```

**Performance Test Output:**
```
{{PERFORMANCE_TEST_OUTPUT}}
```

### Appendix B: NFR Checklist

{{#each NFR_CHECKLIST}}
**{{category}}:**
{{#each items}}
- [{{checkbox}}] {{item}}
{{/each}}

{{/each}}

### Appendix C: Compliance Matrix

{{#if COMPLIANCE_REQUIREMENTS}}
| Standard | Requirement | Status | Evidence | Gaps |
|----------|-------------|--------|----------|------|
{{COMPLIANCE_MATRIX_ROWS}}
<!-- Example:
| OWASP Top 10 | A01:2021 - Broken Access Control | ⚠️ CONCERNS | auth.ts:15-30 | GAP-SEC-2 |
| OWASP Top 10 | A02:2021 - Cryptographic Failures | ✅ PASS | crypto.ts:10-25 | None |
-->
{{/if}}

---

## Notes

{{ADDITIONAL_NOTES}}

---

## Version

**NFR Assessment Version:** {{REPORT_VERSION}}
**Template Version:** 1.0
**Assessment Date:** {{DATE}}
**Next Review:** {{NEXT_REVIEW_DATE}}
**Report Status:** {{REPORT_STATUS}}

---

<!-- End of NFR Assessment -->
