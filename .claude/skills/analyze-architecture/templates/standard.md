# {{project_name}} - Architecture Analysis (Standard)

**Analysis Date**: {{analysis_date}}
**Analysis Mode**: Standard (10-12 minutes)
**Analyzer**: Winston (Architect) - BMAD Enhanced V2
**Project**: {{project_description}}

---

## Executive Summary

**Project Type**: {{project_type}}
**Production Readiness Score**: {{production_readiness_score}}/100 {{score_stars}}
**Category**: {{production_category}}
**Status**: {{production_status}}
**Success Probability**: {{success_probability}}

### Quick Stats

| Metric | Value | Assessment |
|--------|-------|------------|
| **Architecture Quality** | {{architecture_score}}/100 | {{architecture_assessment}} |
| **Code Quality** | {{code_quality_score}}/100 | {{code_quality_assessment}} |
| **Security** | {{security_score}}/100 | {{security_assessment}} |
| **Type Safety** | {{type_safety_percentage}}% | {{type_safety_assessment}} |
| **Test Coverage** | {{test_file_count}} files | {{testing_assessment}} |
| **Documentation** | {{doc_file_count}} docs | {{documentation_assessment}} |

### Critical Path to Production

{{#each critical_blockers}}
🔴 **{{title}}** ({{duration}}) - {{description}}
{{/each}}

---

## 1. Architecture Overview

### 1.1 Project Classification

**Type**: {{project_classification}}
**Build System**: {{build_system}}
**Complexity Score**: {{complexity_score}}/100

### 1.2 Codebase Structure

```
{{codebase_structure}}
```

**Package Inventory**:
{{#each packages}}
- **{{name}}**: {{description}} ({{file_count}} files)
{{/each}}

### 1.3 Architectural Patterns

{{#each architecture_patterns}}
#### {{name}}

**Evidence**: {{evidence_count}} files
**Confidence**: {{confidence}}
**Quality**: {{quality_stars}}

**Key Files**:
{{#each key_files}}
- {{path}}
{{/each}}

---
{{/each}}

**Architecture Complexity**: {{architecture_complexity}}/100

---

## 2. Technology Stack

### 2.1 Backend Technologies

| Technology | Version | Purpose | Quality |
|------------|---------|---------|---------|
{{#each backend_stack}}
| **{{name}}** | {{version}} | {{purpose}} | {{quality_icon}} {{quality}} |
{{/each}}

**Backend Assessment**: {{backend_stack_assessment}}

### 2.2 Frontend Technologies

| Technology | Version | Purpose | Quality |
|------------|---------|---------|---------|
{{#each frontend_stack}}
| **{{name}}** | {{version}} | {{purpose}} | {{quality_icon}} {{quality}} |
{{/each}}

**Frontend Assessment**: {{frontend_stack_assessment}}

### 2.3 Database & Infrastructure

| Component | Technology | Assessment |
|-----------|------------|------------|
{{#each infrastructure}}
| **{{component}}** | {{technology}} | {{assessment}} |
{{/each}}

**Stack Assessment**: {{overall_stack_assessment}}

---

## 3. Domain Model Analysis

{{#if has_domain_model}}

### 3.1 Domain Entities

**Count**: {{entity_count}}

{{#each entities}}
- **{{name}}**: {{description}}
{{/each}}

### 3.2 Value Objects

**Count**: {{value_object_count}}

### 3.3 Domain Events

**Count**: {{domain_event_count}}

{{#each domain_events}}
- **{{name}}**: Triggers {{trigger_count}} handlers
{{/each}}

### 3.4 CQRS Implementation

**Command Handlers**: {{command_handler_count}}
**Query Handlers**: {{query_handler_count}}
**Total Handlers**: {{total_handler_count}}

**CQRS Quality**: {{cqrs_quality_assessment}}

{{else}}
No Domain-Driven Design patterns detected.
{{/if}}

---

## 4. API Architecture

### 4.1 API Style

**Primary Style**: {{api_style}}
**Endpoint Count**: {{endpoint_count}}

### 4.2 Middleware Stack

{{#each middleware}}
- **{{name}}**: {{purpose}} {{status_icon}}
{{/each}}

### 4.3 API Quality

**Score**: {{api_quality_score}}/100

**Strengths**:
{{#each api_strengths}}
- ✅ {{description}}
{{/each}}

**Gaps**:
{{#each api_gaps}}
- ⚠️ {{description}}
{{/each}}

---

## 5. Security Posture

### 5.1 Authentication

**Method**: {{auth_method}}
**Assessment**: {{auth_assessment}}

### 5.2 Authorization

**Approach**: {{authz_approach}}
**Assessment**: {{authz_assessment}}

### 5.3 Security Measures

| Layer | Implementation | Status |
|-------|---------------|--------|
{{#each security_layers}}
| **{{layer}}** | {{implementation}} | {{status_icon}} {{status}} |
{{/each}}

### 5.4 Security Score

**Overall**: {{security_score}}/100 {{security_stars}}

**Strengths**:
{{#each security_strengths}}
- ✅ {{description}}
{{/each}}

**Gaps**:
{{#each security_gaps}}
- 🟡 {{description}}
{{/each}}

---

## 6. Quality Assessment

### 6.1 Weighted Scores

| Dimension | Score | Weight | Weighted | Assessment |
|-----------|-------|--------|----------|------------|
{{#each quality_dimensions}}
| **{{name}}** | {{score}} | {{weight}}% | {{weighted_score}} | {{assessment}} |
{{/each}}
| **TOTAL** | | **100%** | **{{production_readiness_score}}** | **{{overall_assessment}}** |

### 6.2 Production Readiness Category

**Score**: {{production_readiness_score}}/100
**Category**: {{production_category}} ({{category_range}})
**Status**: {{production_status}}

**Scoring Rubric**:
- **90-100**: Excellent - Production ready, best practices
- **80-89**: Very Good - Production ready with minor improvements ← **{{#if_in_range}}YOU ARE HERE{{/if_in_range}}**
- **70-79**: Good - Significant work needed before production
- **60-69**: Fair - Major improvements required
- **0-59**: Poor - Not production ready

---

## 7. Technical Debt Analysis

### 7.1 Current Debt

**Total Debt Items**: {{total_debt_count}}

| Category | Count | % | Priority | Est. Effort |
|----------|-------|---|----------|-------------|
{{#each debt_categories}}
| **{{name}}** | {{count}} | {{percentage}}% | {{priority_icon}} {{priority}} | {{effort}} |
{{/each}}

### 7.2 Priority Breakdown

{{#if has_critical_debt}}
**🔴 CRITICAL** ({{critical_count}} items):
{{#each critical_debt}}
- {{description}} ({{count}} occurrences) - {{effort}}
{{/each}}
{{/if}}

{{#if has_high_debt}}
**🟡 HIGH PRIORITY** ({{high_count}} items):
{{#each high_priority_debt}}
- {{description}} ({{count}} occurrences) - {{effort}}
{{/each}}
{{/if}}

{{#if has_medium_debt}}
**🟢 MEDIUM PRIORITY** ({{medium_count}} items):
{{#each medium_priority_debt}}
- {{description}} ({{count}} occurrences) - {{effort}}
{{/each}}
{{/if}}

---

## 8. Testing Infrastructure

### 8.1 Test Organization

**Total Test Files**: {{total_test_files}}

| Test Type | Count | Coverage |
|-----------|-------|----------|
| **Unit Tests** | {{unit_test_count}} | {{unit_coverage}} |
| **Integration Tests** | {{integration_test_count}} | {{integration_coverage}} |
| **E2E Tests** | {{e2e_test_count}} | {{e2e_coverage}} |

### 8.2 Testing Score

**Overall**: {{testing_score}}/100 {{testing_stars}}

**Strengths**:
{{#each testing_strengths}}
- ✅ {{description}}
{{/each}}

**Gaps**:
{{#each testing_gaps}}
- 🟡 {{description}}
{{/each}}

---

## 9. Performance & Scalability

### 9.1 Performance Characteristics

**Score**: {{performance_score}}/100

{{#each performance_metrics}}
- **{{metric}}**: {{assessment}}
{{/each}}

### 9.2 Scalability Assessment

**Score**: {{scalability_score}}/100

**Horizontal Scaling**: {{horizontal_scaling_assessment}}
**Vertical Scaling**: {{vertical_scaling_assessment}}

**Bottlenecks**:
{{#each bottlenecks}}
- {{description}} (Impact: {{impact}})
{{/each}}

---

## 10. Prioritized Recommendations

### 🔴 CRITICAL (Must Complete Before Production Launch)

{{#each critical_recommendations}}
**{{number}}. {{title}}** ({{duration}})

**Problem**: {{problem}}

**Solution**: {{solution}}

**Impact**: {{impact}}
**Cost**: {{cost}}
**Effort**: {{effort}}
**ROI**: {{roi}}

---
{{/each}}

### 🟡 HIGH PRIORITY (Complete Within 1 Month)

{{#each high_priority_recommendations}}
**{{number}}. {{title}}** ({{duration}})

**Problem**: {{problem}}

**Solution**: {{solution}}

**Impact**: {{impact}}
**Effort**: {{effort}}

---
{{/each}}

### 🟢 MEDIUM PRIORITY (Within 3 Months)

{{#each medium_priority_recommendations}}
**{{number}}. {{title}}** ({{duration}})

**Solution**: {{solution}}
**Impact**: {{impact}}
**Effort**: {{effort}}

---
{{/each}}

---

## 11. Risk Assessment

### 11.1 Technical Risks

| Risk | Severity | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
{{#each technical_risks}}
| **{{name}}** | {{severity_icon}} {{severity}} | {{likelihood_icon}} {{likelihood}} | {{impact}} | {{mitigation}} |
{{/each}}

### 11.2 Operational Risks

| Risk | Severity | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
{{#each operational_risks}}
| **{{name}}** | {{severity_icon}} {{severity}} | {{likelihood_icon}} {{likelihood}} | {{impact}} | {{mitigation}} |
{{/each}}

---

## 12. Production Readiness Checklist

### Infrastructure: {{infrastructure_completion}}% Complete

| Component | Status | Priority |
|-----------|--------|----------|
{{#each infrastructure_checklist}}
| {{component}} | {{status_icon}} {{status}} | {{priority}} |
{{/each}}

### Security: {{security_completion}}% Complete

| Component | Status | Priority |
|-----------|--------|----------|
{{#each security_checklist}}
| {{component}} | {{status_icon}} {{status}} | {{priority}} |
{{/each}}

### Monitoring: {{monitoring_completion}}% Complete

| Component | Status | Priority |
|-----------|--------|----------|
{{#each monitoring_checklist}}
| {{component}} | {{status_icon}} {{status}} | {{priority}} |
{{/each}}

---

## 13. Timeline to Production

### Option A: Minimum Viable Production ({{mvp_timeline}})

{{#each mvp_timeline_phases}}
**{{phase_name}}** ({{duration}}):
{{#each tasks}}
- {{task_description}}
{{/each}}
{{/each}}

### Option B: Optimal Production ({{optimal_timeline}})

{{#each optimal_timeline_phases}}
**{{phase_name}}** ({{duration}}):
{{#each tasks}}
- {{task_description}}
{{/each}}
{{/each}}

---

## 14. Final Verdict

### Production Readiness Score: {{production_readiness_score}}/100 {{score_stars}}

**Category**: {{production_category}}
**Status**: {{production_status}}
**Confidence Level**: {{confidence_level}}

### What Makes This {{quality_level}}

{{conclusion_highlights}}

### The Critical Gap: {{critical_gap_title}}

{{critical_gap_description}}

### Recommended Action Plan

**Immediate** (This Week):
{{#each immediate_actions}}
{{number}}. {{action}}
{{/each}}

**Month 1** (Critical Path):
{{#each month1_actions}}
{{number}}. {{action}}
{{/each}}

**Month 2-3** (Quality & Scale):
{{#each month2_3_actions}}
{{number}}. {{action}}
{{/each}}

### Success Probability

With recommended enhancements: **{{success_with_enhancements}}%**
Without critical improvements: **{{success_without_improvements}}%**

### Final Words

{{final_conclusion}}

**Recommendation**: {{final_recommendation}}

---

## 15. Appendix: Complete Metrics

| Metric | Value | Source |
|--------|-------|--------|
{{#each all_metrics}}
| **{{metric_name}}** | {{value}} | {{source}} |
{{/each}}

---

**Report Generated**: {{timestamp}}
**Method**: Standard (10-12 minutes)
**Analyzer**: Winston (Architect) - BMAD Enhanced V2
**Analysis Duration**: {{duration_ms}}ms
**Token Usage**: {{token_usage}} tokens

---

*For quick overview, use `--depth quick`. For complete analysis, use `--depth comprehensive`*
