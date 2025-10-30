---
name: nfr-assess
description: Assess non-functional requirements across 6 quality categories with measurable criteria, evidence-based evaluation, and automated checks
version: 2.0
category: Quality
acceptance:
  all_categories_assessed: "All 6 NFR categories (Security, Performance, Reliability, Maintainability, Scalability, Usability) scored with evidence"
  gaps_identified: "NFR gaps documented with severity ratings (CRITICAL/HIGH/MEDIUM) and remediation guidance"
  automated_checks_executed: "Automated checks run where available (security scans, linting, test coverage, performance tests)"
  report_generated: "Complete NFR assessment report generated with overall score, category scores, gap summary, and recommendations"
inputs:
  task_id:
    required: true
    description: "Task identifier to assess (e.g., 'task-007')"
  task_file:
    required: true
    description: "Path to task specification file"
  config_file:
    required: false
    description: "Path to project configuration (defaults to .claude/config.yaml)"
  nfr_thresholds:
    required: false
    description: "Custom NFR thresholds (security, performance, maintainability)"
outputs:
  overall_nfr_score:
    description: "Weighted overall NFR score (0-100)"
  category_scores:
    description: "Individual scores for each of 6 NFR categories"
  overall_status:
    description: "Overall NFR status (PASS/CONCERNS/FAIL)"
  critical_gaps_count:
    description: "Number of critical NFR gaps (P0)"
  high_gaps_count:
    description: "Number of high-severity NFR gaps (P1)"
  report_path:
    description: "Path to generated NFR assessment report"
  quality_gate_impact:
    description: "Predicted impact on quality gate (PASS/CONCERNS/FAIL)"
telemetry:
  emit: "skill.nfr-assess.completed"
  track:
    - task_id
    - overall_nfr_score
    - overall_status
    - security_score
    - performance_score
    - reliability_score
    - maintainability_score
    - scalability_score
    - usability_score
    - critical_gaps_count
    - high_gaps_count
    - automated_checks_run
    - assessment_duration_ms
---

# Non-Functional Requirements Assessment

The **nfr-assess** skill performs comprehensive evaluation of non-functional requirements (NFRs) to ensure the implementation meets quality attributes beyond functional correctness. NFRs are cross-cutting concerns that determine system quality, reliability, and long-term viability. This skill assesses 6 critical quality categories with measurable criteria, evidence-based evaluation, and automated checks where possible.

Unlike functional requirements that define *what* the system does, non-functional requirements define *how well* the system performs. This skill provides objective assessment across Security (authentication, encryption, vulnerabilities), Performance (response times, throughput, resource usage), Reliability (error handling, monitoring, fault tolerance), Maintainability (code quality, documentation, testability), Scalability (horizontal scaling, database design, async processing), and Usability (API design, error messages, documentation).

The assessment produces a weighted overall NFR score, individual category scores, identifies gaps with severity ratings, and provides actionable recommendations. Results feed directly into the quality-gate skill to inform merge/release decisions. Automated checks (security scans, linting, test coverage, performance tests) are integrated where available to provide objective, reproducible metrics.

## When to Use This Skill

**Use nfr-assess when you need to:**
- Validate non-functional quality attributes during implementation review
- Assess system-wide quality concerns (security, performance, reliability)
- Identify gaps in quality attributes with severity ratings
- Generate evidence-based NFR reports for audit/compliance
- Feed NFR metrics into quality gate decision-making
- Validate production readiness from quality perspective

**This skill is particularly valuable:**
- Before quality gate review (identifies issues early)
- After functional testing completes (assess non-functional aspects)
- During architectural review (validate design patterns for NFRs)
- When preparing for production deployment (ensure production readiness)
- For compliance validation (OWASP, WCAG, performance budgets)

**Do NOT use nfr-assess when:**
- Functional requirements haven't been implemented yet (assess functionality first)
- Task is purely planning/design (no implementation to assess)
- You only need to test functional behavior (use run-tests instead)

## Prerequisites

Before running nfr-assess, ensure you have:

1. **Task specification file** with implementation record
2. **Project configuration** (.claude/config.yaml) with quality settings
3. **Implementation files** accessible for code review
4. **Automated tools available** (optional but recommended):
   - Security: `npm audit`, `semgrep`, or equivalent
   - Code quality: linter (eslint, pylint, etc.)
   - Test coverage: coverage tools (jest --coverage, pytest-cov, etc.)
   - Performance: load testing tools (artillery, k6, etc.)

**Dependencies on other skills:**
- Optional: risk-profile (provides security/performance risk context)
- Optional: trace-requirements (provides implementation evidence)
- Optional: test-design (provides performance/load test specifications)

## Sequential NFR Assessment Process

This skill executes through 9 sequential steps. Each step must complete successfully before proceeding. The process is designed to systematically evaluate all 6 NFR categories with evidence collection, automated checks, and gap identification.

### Step 0: Load Configuration and Context

**Purpose:** Load project configuration, task specification, and all relevant context needed for NFR assessment. Identify implementation files, prepare automated checks, and determine which NFR categories are most relevant based on task type.

**Actions:**
1. Load project configuration from `.claude/config.yaml` (quality settings, NFR thresholds)
2. Read task specification file (extract task ID, title, type, NFR requirements, implementation record)
3. Load related assessments if available (risk profile, traceability matrix, test design)
4. Identify implementation files from implementation record (source, config, infrastructure, dependencies)
5. Identify relevant NFR categories based on task type (e.g., API tasks prioritize Security/Performance)
6. Prepare automated checks (security scans, linting, test coverage, performance tests)
7. Prepare output file path (`.claude/quality/assessments/{task-id}-nfr-{YYYYMMDD}.md`)

**Halt If:**
- Config file missing or invalid
- Task file not found
- Cannot create output directory

**Output:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: {task-id} - {title}
✓ Related assessments: Risk [{found/not found}], Trace [{found/not found}]
✓ Implementation files: {count} files identified
✓ Relevant NFR categories: Security (HIGH), Performance (HIGH), Reliability (MEDIUM), ...
✓ Automated checks: {checks available}
✓ Output: {output-file}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md) for detailed category descriptions and relevance criteria.

---

### Step 1: Security Assessment

**Purpose:** Evaluate security posture including authentication, authorization, input validation, dependency vulnerabilities, and security best practices. Leverage automated security scans (npm audit, semgrep) and manual code review to identify security gaps with evidence.

**Actions:**
1. Define security criteria (10 criteria: authentication, authorization, input validation, output encoding, dependency vulnerabilities, secrets management, HTTPS/TLS, rate limiting, CORS, security headers)
2. Run automated security checks:
   - Dependency vulnerability scan (`npm audit --json` or equivalent)
   - Code security scan (`semgrep --config=auto` if available)
   - Secret detection (check for hardcoded credentials)
3. Manual code review for security:
   - Search for authentication/authorization code
   - Check input validation implementation (Zod, Joi, etc.)
   - Check for SQL injection risks (parameterized queries?)
   - Check for XSS risks (output encoding?)
   - Check CORS configuration and rate limiting
4. Collect evidence for each criterion (file paths, line numbers, code snippets, scan results)
5. Score each criterion (PASS/CONCERNS/FAIL/UNCLEAR)
6. Calculate overall security score (weighted average: PASS=100, CONCERNS=50, FAIL=0)
7. Identify security gaps with severity ratings (CRITICAL/HIGH/MEDIUM)

**Output:**
```
✓ Security assessment complete
✓ Overall Security Score: {score}% ({status})
✓ Criteria Evaluated: {count} (PASS: {n}, CONCERNS: {n}, FAIL: {n})
✓ Automated Checks: Vulnerabilities [{critical}/{high}/{moderate}/{low}], Secrets [{found}]
✓ Critical Gaps: {count}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md#security-assessment) for detailed security criteria and [nfr-examples.md](references/nfr-examples.md#security-evidence) for evidence format examples.

---

### Step 2: Performance Assessment

**Purpose:** Evaluate performance characteristics including response times, throughput, resource usage, caching, and optimization. Run performance tests if available, analyze database queries for N+1 problems, and check algorithm complexity in hot paths.

**Actions:**
1. Define performance criteria (10 criteria: response time, throughput, resource usage, database queries, caching, asset optimization, algorithm complexity, connection pooling, async operations, load testing)
2. Run automated performance checks:
   - Performance tests (`npm run test:perf` if available)
   - Load tests (artillery, k6, etc. if available)
   - Bundle size analysis (if UI application)
   - Database query analysis (EXPLAIN ANALYZE)
3. Manual code review for performance:
   - Check database queries for N+1 problems
   - Check for blocking operations in request handlers
   - Check algorithm complexity in hot paths (O(n log n) or better?)
   - Check caching implementation (Redis, in-memory)
   - Check connection pooling configuration
4. Collect evidence (performance test results, query analysis, code review findings)
5. Score each criterion (PASS/CONCERNS/FAIL/UNCLEAR)
6. Calculate overall performance score
7. Identify performance gaps (e.g., missing caching, N+1 queries, no load testing)

**Output:**
```
✓ Performance assessment complete
✓ Overall Performance Score: {score}% ({status})
✓ Response Time (p95): {avg_p95}ms (threshold: {threshold}ms)
✓ Throughput: {req_per_sec} req/s (threshold: {threshold} req/s)
✓ Load Test: {success_rate}% success at {load} req/s
✓ Performance Gaps: {count}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md#performance-assessment) for performance criteria and thresholds, [nfr-examples.md](references/nfr-examples.md#performance-benchmarks) for benchmark examples.

---

### Step 3: Reliability Assessment

**Purpose:** Evaluate system reliability including error handling, fault tolerance, recovery, monitoring, and logging. Check for comprehensive error handling, graceful degradation when dependencies fail, and proper observability (logging, monitoring, health checks).

**Actions:**
1. Define reliability criteria (10 criteria: error handling, input validation errors, graceful degradation, retry logic, circuit breakers, logging, monitoring, idempotency, data integrity, disaster recovery)
2. Manual code review for reliability:
   - Check try-catch blocks in async operations
   - Check error response formatting
   - Check database transaction usage
   - Check logging implementation (winston, pino, structured logs?)
   - Check health check endpoints
   - Check monitoring integration (Prometheus, Datadog, etc.)
3. Collect evidence (error handlers, logging examples, monitoring configuration)
4. Score each criterion (PASS/CONCERNS/FAIL/UNCLEAR)
5. Calculate overall reliability score
6. Identify reliability gaps (e.g., no monitoring, no log aggregation, missing health checks)

**Output:**
```
✓ Reliability assessment complete
✓ Overall Reliability Score: {score}% ({status})
✓ Error Handling: {status}
✓ Logging: {status} (structured: {yes/no}, aggregation: {yes/no})
✓ Monitoring: {status} (health checks: {yes/no}, metrics: {yes/no})
✓ Reliability Gaps: {count}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md#reliability-assessment) for reliability criteria and [nfr-examples.md](references/nfr-examples.md#reliability-evidence) for evidence examples.

---

### Step 4: Maintainability Assessment

**Purpose:** Evaluate code maintainability including code quality, documentation, testability, modularity, and technical debt. Leverage automated tools (linting, test coverage, complexity analysis) and manual review for documentation, naming, and code organization.

**Actions:**
1. Define maintainability criteria (10 criteria: code quality, test coverage, documentation, modularity, naming, complexity, duplication, type safety, dependencies, technical debt)
2. Run automated maintainability checks:
   - Linting (`npm run lint` or equivalent)
   - Test coverage (`npm run test:coverage`)
   - Complexity analysis (cyclomatic complexity ≤10?)
   - Duplication detection (jscpd, etc.)
   - Type checking (TypeScript strict mode)
3. Manual code review for maintainability:
   - Check code structure and organization
   - Check naming conventions (clear, descriptive?)
   - Check function/class sizes (≤50 lines?)
   - Check documentation completeness (README, API docs, JSDoc)
   - Check for technical debt (TODO/FIXME comments)
4. Collect evidence (coverage reports, complexity metrics, lint results, documentation)
5. Score each criterion (PASS/CONCERNS/FAIL/UNCLEAR)
6. Calculate overall maintainability score
7. Identify maintainability gaps (e.g., missing documentation, high complexity, low coverage)

**Output:**
```
✓ Maintainability assessment complete
✓ Overall Maintainability Score: {score}% ({status})
✓ Test Coverage: {coverage}% (threshold: {threshold}%)
✓ Avg Complexity: {avg_complexity} (max: {max_complexity})
✓ Linting: {pass/fail} ({error_count} errors)
✓ Documentation: {status} (README: {yes/no}, API docs: {yes/no})
✓ Maintainability Gaps: {count}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md#maintainability-assessment) for maintainability criteria and thresholds, [nfr-scoring.md](references/nfr-scoring.md#maintainability-scoring) for scoring methodology.

---

### Step 5: Scalability Assessment

**Purpose:** Evaluate system scalability including horizontal/vertical scaling capability, load handling, database design, and caching strategy. Check for stateless design, proper database indexing, async processing for expensive operations, and readiness for load balancing.

**Actions:**
1. Define scalability criteria (10 criteria: stateless design, horizontal scaling, database design, connection pooling, caching, async processing, rate limiting, load balancing readiness, resource limits, auto-scaling)
2. Review architecture for scalability:
   - Check if application is stateless (no in-memory session state)
   - Check database schema and indexing (foreign keys indexed?)
   - Check for file uploads (should use object storage like S3)
   - Check for background job processing (should use queue like Bull/BullMQ)
   - Check for proper shutdown handlers (graceful shutdown)
3. Collect evidence (architecture review, schema analysis, code review)
4. Score each criterion (PASS/CONCERNS/FAIL/UNCLEAR)
5. Calculate overall scalability score
6. Identify scalability gaps (e.g., stateful design, missing indexes, no async processing)

**Output:**
```
✓ Scalability assessment complete
✓ Overall Scalability Score: {score}% ({status})
✓ Stateless Design: {status}
✓ Database Indexing: {status} (indexes: {count}, missing: {count})
✓ Async Processing: {status} (queue: {yes/no})
✓ Horizontal Scaling: {ready/not ready}
✓ Scalability Gaps: {count}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md#scalability-assessment) for scalability criteria and [nfr-examples.md](references/nfr-examples.md#scalability-evidence) for architecture examples.

---

### Step 6: Usability Assessment

**Purpose:** Evaluate system usability including API design, error messages, documentation, and accessibility (if UI). For APIs, check RESTful conventions, error message clarity, and API documentation. For UIs, check WCAG compliance, responsive design, and user experience.

**Actions:**
1. Define usability criteria:
   - **For APIs** (10 criteria): API design, error messages, documentation, versioning, pagination, filtering, HTTP status codes, response format, HATEOAS, developer experience
   - **For UIs** (10 criteria): accessibility (WCAG 2.1 AA), responsive design, loading states, error handling, keyboard navigation, color contrast, screen reader support, form validation, intuitive navigation, performance
2. Review API/UI design:
   - Check REST conventions (proper HTTP verbs, resource naming)
   - Check error response format (clear, actionable messages?)
   - Check API documentation (OpenAPI/Swagger spec?)
   - Check pagination/filtering implementation
   - For UIs: Check accessibility with automated tools (axe, lighthouse)
3. Collect evidence (route definitions, error responses, documentation, accessibility scan results)
4. Score each criterion (PASS/CONCERNS/FAIL/UNCLEAR)
5. Calculate overall usability score
6. Identify usability gaps (e.g., missing API docs, generic error messages, accessibility issues)

**Output:**
```
✓ Usability assessment complete
✓ Overall Usability Score: {score}% ({status})
✓ API Design: {status} (RESTful: {yes/no})
✓ Error Messages: {status} (detailed: {yes/no})
✓ Documentation: {status} (API docs: {yes/no})
✓ Accessibility: {status} (WCAG 2.1 AA: {compliant/non-compliant}, if UI)
✓ Usability Gaps: {count}
```

**Reference:** See [nfr-categories.md](references/nfr-categories.md#usability-assessment) for usability criteria (API vs UI), [nfr-examples.md](references/nfr-examples.md#usability-evidence) for examples.

---

### Step 7: Generate NFR Assessment Report

**Purpose:** Create comprehensive NFR assessment report using template with all category assessments, overall score calculation, gap summary, and recommendations.

**Actions:**
1. Load NFR assessment template (`.claude/templates/nfr-assessment.md`)
2. Compute overall NFR score using weighted formula:
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
3. Determine overall NFR status:
   - ≥90%: PASS (Excellent)
   - 75-89%: PASS (Good)
   - 60-74%: CONCERNS (Needs improvement)
   - <60%: FAIL (Critical issues)
4. Aggregate all gaps across categories with priorities (P0/P1/P2)
5. Generate recommendations prioritized by severity and impact
6. Predict quality gate impact based on NFR score and critical gaps
7. Populate template with all assessment data from Steps 1-6
8. Write complete report to output file

**Output:**
```
✓ NFR assessment report generated
✓ Output: .claude/quality/assessments/{task-id}-nfr-{date}.md
✓ Overall NFR Score: {score}% ({status})
✓ Category Scores: Security {s}%, Performance {p}%, Reliability {r}%, Maintainability {m}%, Scalability {sc}%, Usability {u}%
✓ Total Gaps: {count} (Critical: {c}, High: {h}, Medium: {m})
✓ Report size: {lines} lines
```

**Reference:** See [nfr-scoring.md](references/nfr-scoring.md) for detailed scoring methodology and thresholds, [nfr-gaps.md](references/nfr-gaps.md) for gap categorization.

---

### Step 8: Present Summary to User

**Purpose:** Provide concise summary with key metrics, critical gaps, quality gate impact, and recommended next steps.

**Actions:**
1. Display formatted summary with:
   - Task metadata (ID, title, date)
   - Overall NFR score and status
   - Category scores (6 categories with individual status)
   - Critical gaps (P0 - must fix before merge)
   - High gaps (P1 - should fix before release)
   - Quality gate impact prediction (PASS/CONCERNS/FAIL)
   - Reasoning for quality gate impact
   - Actionable recommendations to achieve PASS status
   - Estimated effort to close critical gaps
   - Path to full report
2. Suggest next steps:
   - Review detailed assessment in report
   - Prioritize P0 gaps (security, reliability blockers)
   - Create tickets for P1 gaps
   - Re-run nfr-assess after closing gaps
   - Proceed to quality-gate when NFR score ≥75%
3. Emit telemetry event with all metrics

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Non-Functional Requirements Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id} - {title}
Date: {date}

📊 Overall NFR Score: {score}% ({status})

Category Scores:
├─ Security: {score}% ({status}) - {critical_gaps} critical gaps
├─ Performance: {score}% ({status}) - {high_gaps} high gaps
├─ Reliability: {score}% ({status}) - {critical_gaps} critical gaps
├─ Maintainability: {score}% ({status}) - {high_gaps} high gaps
├─ Scalability: {score}% ({status}) - {high_gaps} high gaps
└─ Usability: {score}% ({status}) - {high_gaps} high gaps

⚠️  Critical Gaps (P0 - Must Fix):
{list of P0 gaps with severity and action}

🔴 High Gaps (P1 - Should Fix):
{list of P1 gaps with severity and action}

🎯 Quality Gate Impact: {PASS/CONCERNS/FAIL}

Reasoning: {why this impacts quality gate}

✅ To Achieve PASS:
{prioritized action plan with time estimates}

📄 Full Report: {report_path}

💡 Next Steps:
1. Review detailed NFR assessment in report
2. Prioritize P0 gaps (before merge)
3. Create tickets for P1 gaps
4. Re-run nfr-assess after closing gaps
5. Proceed to quality-gate when NFR score ≥75%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Execution Complete.**

**Reference:** See [nfr-examples.md](references/nfr-examples.md#summary-formats) for summary format examples and [nfr-gaps.md](references/nfr-gaps.md#gap-prioritization) for gap prioritization logic.

---

## Integration with Other Skills

### Integration with risk-profile

**Input from risk-profile:**
- Security risks identified in risk profile inform security assessment severity
- Performance risks inform performance assessment priorities
- Reliability risks inform reliability criteria weighting

**How nfr-assess uses risk profile:**
When a risk is identified in risk profile (e.g., "SQL injection - Score 6, HIGH"), and the NFR assessment finds a related gap (e.g., "Input Validation: CONCERNS - No sanitization"), the gap severity is amplified. A HIGH security gap that matches a HIGH risk becomes CRITICAL (must fix before merge).

**Example:**
```
Risk Profile: Risk #2 - SQL injection (Score: 6, HIGH)
NFR Security: Input Validation (CONCERNS) - No SQL injection protection
→ Gap Severity: CRITICAL (base: HIGH + risk amplification: +1)
→ Priority: P0 (blocks merge)
```

### Integration with trace-requirements

**Input from traceability:**
- Implementation evidence validates NFR implementation (e.g., security controls, error handlers)
- Test coverage metrics inform reliability and maintainability assessments

**Output to traceability:**
- NFR gaps become additional coverage gaps in traceability matrix
- Missing NFR implementations flagged as uncovered requirements

### Integration with test-design

**Input from test-design:**
- Performance test specifications inform performance assessment
- Load test requirements validate scalability assessment
- Security test cases inform security assessment

### Integration with quality-gate

**Output to quality-gate:**
- Overall NFR score contributes to quality gate decision
- Category scores (especially Security and Reliability) influence gate status
- Critical NFR gaps may block quality gate (FAIL)
- NFR evidence feeds into quality gate report

**How quality-gate uses NFR assessment:**
```
Quality Gate Decision Logic:
1. Check overall NFR score:
   - ≥90%: PASS (excellent)
   - 75-89%: PASS (good)
   - 60-74%: CONCERNS (needs improvement)
   - <60%: FAIL (critical issues)

2. Check critical NFR gaps:
   - 0 critical: Continue evaluation
   - 1+ critical in Security/Reliability: FAIL (production blocker)
   - 1+ critical in other categories: CONCERNS

3. Check category minimums:
   - Security <50%: FAIL (not production-ready)
   - Reliability <50%: FAIL (not production-ready)
   - Performance <50%: CONCERNS (may need optimization)
```

---

## Best Practices

1. **Run NFR assessment before quality gate** - Identifies quality issues early in the review process, allowing time for remediation before merge decision.

2. **Integrate automated checks** - Leverage tools (security scans, linting, test coverage) for objective, reproducible metrics. Automated checks reduce manual effort and increase assessment reliability.

3. **Document evidence thoroughly** - Include file paths, line numbers, and code snippets for all assessments. Evidence makes findings actionable and defensible.

4. **Prioritize Security and Reliability** - These categories directly impact production readiness. Security vulnerabilities and reliability issues are production blockers (P0 priority).

5. **Set measurable thresholds** - Define clear pass/fail criteria in project configuration (e.g., "max critical vulnerabilities: 0", "min test coverage: 80%"). Measurable thresholds enable objective assessment.

6. **Re-run after fixes** - After closing NFR gaps, re-run nfr-assess to validate gap closure and update NFR score. Track score improvement over time.

7. **Customize category weights** - Adjust category weights in scoring formula based on project priorities (e.g., increase Security weight for security-critical systems).

8. **Review with stakeholders** - Share NFR assessment reports with technical leads, security teams, and product owners. NFR gaps often require cross-functional decisions.

---

## References

- **[nfr-categories.md](references/nfr-categories.md)** - Detailed assessment criteria for all 6 NFR categories (Security, Performance, Reliability, Maintainability, Scalability, Usability) with examples and thresholds

- **[nfr-scoring.md](references/nfr-scoring.md)** - Scoring methodology, weighting formulas, status determination thresholds, and automated check integration

- **[nfr-gaps.md](references/nfr-gaps.md)** - Gap identification methodology, severity levels (CRITICAL/HIGH/MEDIUM), prioritization logic (P0/P1/P2), and remediation guidance

- **[nfr-examples.md](references/nfr-examples.md)** - Complete example assessments, evidence formats, benchmark results, and summary outputs for all 6 categories

---

*NFR Assessment skill - Version 2.0 - Minimal V2 Architecture*
