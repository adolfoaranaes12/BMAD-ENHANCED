# {{project_name}} - Architecture Analysis (Comprehensive)

**Analysis Date**: {{analysis_date}}
**Analysis Mode**: Comprehensive (15-20 minutes)
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
| **Performance** | {{performance_score}}/100 | {{performance_assessment}} |
| **Scalability** | {{scalability_score}}/100 | {{scalability_assessment}} |
| **Maintainability** | {{maintainability_score}}/100 | {{maintainability_assessment}} |
| **Testing** | {{testing_score}}/100 | {{testing_assessment}} |
| **Monitoring** | {{monitoring_score}}/100 | {{monitoring_assessment}} |

### Critical Path to Production

{{#each critical_blockers}}
🔴 **BLOCKER {{number}}**: {{title}} ({{duration}}) - {{description}}
{{/each}}

{{#each high_priority_items}}
🟡 **HIGH PRIORITY {{number}}**: {{title}} ({{duration}}) - {{description}}
{{/each}}

---

## Part 1: Systematic Discovery

### 1. Codebase Structure Analysis

**Project Classification**: {{project_classification}}
**Build System**: {{build_system}}
**Monorepo Indicators**: {{monorepo_indicators}}

```
{{detailed_codebase_structure}}
```

**Package Inventory**:
{{#each packages}}
- **{{path}}**: {{description}}
  - Type: {{type}}
  - Files: {{file_count}}
  - Dependencies: {{dependency_count}}
{{/each}}

### 2. Project Type Detection

**Detected Type**: {{project_type}}
**Confidence**: {{detection_confidence}}%

**Frontend Indicators**:
{{#each frontend_indicators}}
- {{indicator}}: {{evidence}}
{{/each}}

**Backend Indicators**:
{{#each backend_indicators}}
- {{indicator}}: {{evidence}}
{{/each}}

### 3. Technology Stack Discovery

[Include complete technology stack with versions, categories, and quality assessments - same as standard template but with more details]

### 4. Architectural Pattern Identification

[Include detailed pattern analysis with evidence, quality scores, and implementation details - extended from standard template]

### 5. Domain Model Evaluation

[Include complete domain model analysis if DDD/CQRS - extended from standard template]

### 6. API Architecture Assessment

[Include complete API analysis with endpoints, middleware, versioning - extended from standard template]

### 7. Data Architecture Review

[Include database schema analysis, caching strategy, real-time infrastructure - new section]

### 8. Security Posture Analysis

[Include complete security analysis - extended from standard template]

### 9. Performance Characteristics Evaluation

[Include complete performance analysis with bottlenecks - extended from standard template]

### 10. Scalability Assessment

[Include detailed scalability analysis with capacity planning - extended from standard template]

### 11. Technical Debt Identification

[Include complete technical debt analysis - extended from standard template]

### 12. Testing Infrastructure Review

[Include detailed testing analysis - extended from standard template]

### 13. External Integrations Analysis

**Integration Count**: {{integration_count}}

{{#each integrations}}
#### {{name}}

**Category**: {{category}}
**Method**: {{integration_method}}
**Version**: {{version}}
**Purpose**: {{purpose}}
**Assessment**: {{assessment}}

{{/each}}

### 14. Production Readiness Score Calculation

[Include detailed scoring methodology - extended from standard template]

### 15. Comprehensive Analysis Report

[Complete report with all sections]

---

## Part 2: Deep-Dive Analysis

[This section includes manual analysis and contextual insights beyond systematic discovery]

### 2.1 Architecture Excellence

[Deep dive into why the architecture is excellent/good/needs work]

### 2.2 Security Deep Dive

[Extended security analysis with threat modeling]

### 2.3 Performance Deep Dive

[Extended performance analysis with optimization recommendations]

### 2.4 Scalability Deep Dive

[Extended scalability analysis with growth projections]

---

## Part 3: Production Readiness Assessment

[Complete production readiness assessment with checklist - extended from standard template]

---

## Part 4: Prioritized Recommendations

[Complete recommendations with ROI analysis - extended from standard template]

---

## Part 5: Timeline to Production

[Detailed timeline with multiple options - extended from standard template]

---

## Part 6: Risk Assessment

[Complete risk assessment with mitigation strategies - extended from standard template]

---

## Part 7: Final Verdict & Conclusion

[Comprehensive conclusion with detailed action plan - extended from standard template]

---

## Appendix: Complete Metrics

[All metrics with sources and verification methods]

---

**Report Generated**: {{timestamp}}
**Method**: Comprehensive (15-20 minutes)
**Analyzer**: Winston (Architect) - BMAD Enhanced V2
**Report Version**: 1.0 (Comprehensive)
**Analysis Duration**: {{duration_ms}}ms
**Token Usage**: {{token_usage}} tokens

---

**END OF COMPREHENSIVE REPORT**
