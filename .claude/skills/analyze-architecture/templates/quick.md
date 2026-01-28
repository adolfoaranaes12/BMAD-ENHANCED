# {{project_name}} - Architecture Analysis (Quick)

**Analysis Date**: {{analysis_date}}
**Analysis Mode**: Quick (5-7 minutes)
**Analyzer**: Winston (Architect) - BMAD Enhanced V2

---

## Executive Summary

**Project Type**: {{project_type}}
**Production Readiness Score**: {{production_readiness_score}}/100 {{score_stars}}
**Status**: {{production_status}}
**Success Probability**: {{success_probability}}

### Quick Stats

| Metric | Value | Assessment |
|--------|-------|------------|
| **Architecture Quality** | {{architecture_score}}/100 | {{architecture_assessment}} |
| **Type Safety** | {{type_safety_percentage}}% | {{type_safety_assessment}} |
| **Test Coverage** | {{test_file_count}} files | {{testing_assessment}} |
| **Documentation** | {{doc_file_count}} docs | {{documentation_assessment}} |

---

## 1. Architecture Overview

**Project Classification**: {{project_classification}}
**Build System**: {{build_system}}

### Structure

```
{{codebase_structure}}
```

### Identified Patterns

{{#each architecture_patterns}}
- **{{name}}**: {{confidence}} confidence - {{evidence}}
{{/each}}

---

## 2. Technology Stack

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
{{#each backend_stack}}
| **{{name}}** | {{version}} | {{purpose}} |
{{/each}}

### Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
{{#each frontend_stack}}
| **{{name}}** | {{version}} | {{purpose}} |
{{/each}}

**Stack Assessment**: {{stack_assessment_stars}} {{stack_assessment_text}}

---

## 3. Quality Scores

| Dimension | Score | Assessment |
|-----------|-------|------------|
| **Architecture** | {{architecture_score}}/100 | {{architecture_stars}} |
| **Code Quality** | {{code_quality_score}}/100 | {{code_quality_stars}} |
| **Security** | {{security_score}}/100 | {{security_stars}} |
| **Performance** | {{performance_score}}/100 | {{performance_stars}} |
| **Scalability** | {{scalability_score}}/100 | {{scalability_stars}} |
| **Maintainability** | {{maintainability_score}}/100 | {{maintainability_stars}} |
| **Testing** | {{testing_score}}/100 | {{testing_stars}} |
| **Monitoring** | {{monitoring_score}}/100 | {{monitoring_stars}} |

**Overall Score**: {{production_readiness_score}}/100 {{score_stars}}

---

## 4. Critical Findings

### Technical Debt

{{#if has_critical_debt}}
🔴 **Critical Issues**:
{{#each critical_debt}}
- {{description}} ({{count}} occurrences)
{{/each}}
{{/if}}

{{#if has_high_debt}}
🟡 **High Priority**:
{{#each high_priority_debt}}
- {{description}} ({{count}} occurrences)
{{/each}}
{{/if}}

**Total Technical Debt Items**: {{total_debt_count}}

### Security Findings

{{#each security_findings}}
- {{severity_icon}} **{{title}}**: {{description}}
{{/each}}

---

## 5. Top 5 Recommendations

{{#each top_recommendations}}
### {{priority_icon}} {{priority}}: {{title}}

**Problem**: {{problem}}

**Solution**: {{solution}}

**Impact**: {{impact}}
**Effort**: {{effort}}
**Priority**: {{priority_level}}

---
{{/each}}

## 6. Production Readiness

**Overall Status**: {{production_status}}

| Component | Status | Priority |
|-----------|--------|----------|
{{#each production_checklist}}
| {{component}} | {{status_icon}} {{status}} | {{priority}} |
{{/each}}

---

## 7. Next Steps

**Critical Path to Production**:

{{#each critical_path}}
{{step_number}}. **{{title}}** ({{duration}}) - {{description}}
{{/each}}

---

## 8. Conclusion

{{conclusion_summary}}

**Recommendation**: {{final_recommendation}}

---

**Report Generated**: {{timestamp}}
**Analysis Duration**: {{duration_ms}}ms
**Token Usage**: {{token_usage}} tokens
**Mode**: Quick

---

*For detailed analysis, run with `--depth comprehensive`*
