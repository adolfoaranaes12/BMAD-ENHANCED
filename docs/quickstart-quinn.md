# Quinn (Quality) Quick Start Guide

**Subagent:** quinn-quality
**Role:** Quality Assurance & Non-Functional Requirements Specialist
**Commands:** 5
**Version:** 2.0

---

## Overview

**Quinn** is your intelligent quality assurance assistant that ensures high standards through comprehensive reviews, NFR assessments, quality gates, requirements tracing, and risk analysis using complexity-based routing.

### What Quinn Does

- ✅ Performs comprehensive quality reviews
- ✅ Assesses non-functional requirements (NFRs)
- ✅ Makes quality gate decisions (PASS/CONCERNS/FAIL/WAIVED)
- ✅ Traces requirements to implementation and tests
- ✅ Assesses implementation risks using P×I methodology
- ✅ Enforces quality standards and best practices

### V2 Features

- **Intelligent Routing:** Automatically selects review depth (simple/standard/comprehensive)
- **Complexity Assessment:** 0-100 scale using 5 weighted factors per command
- **Guardrails:** Enforces quality thresholds and escalation triggers
- **Full Telemetry:** Every assessment tracked and observable
- **Objective Quality Gates:** Data-driven PASS/FAIL decisions

---

## Commands

### 1. `*review` - Comprehensive Quality Review

**Purpose:** Perform comprehensive quality review including code quality, NFRs, and quality gate decision

**Syntax:**
```bash
/quinn *review <task-id>
/quinn *review task-auth-002
/quinn *review task-payment-001
```

**Examples:**
```bash
/quinn *review task-login-001
/quinn *review task-checkout-flow
/quinn *review task-api-auth
```

**What You Get:**
- Quality gate file (`.claude/quality/gates/{task-id}-gate-{timestamp}.yaml`)
- Code quality analysis (linting, complexity, formatting)
- NFR assessment (all 6 categories)
- Test coverage report with gaps
- Quality gate decision (PASS/CONCERNS/FAIL)
- Action items for improvements
- Overall quality score (0-100%)

**Complexity Factors:**
- Files to review (30%)
- Quality issues (25%)
- NFR requirements (20%)
- Test coverage (15%)
- Codebase size (10%)

**When to Use:**
- After James implements features
- Before merging to main branch
- During code review process
- Prior to deployment

---

### 2. `*assess-nfr` - Assess Non-Functional Requirements

**Purpose:** Assess non-functional requirements across 6 critical categories

**Syntax:**
```bash
/quinn *assess-nfr <task-id>
/quinn *assess-nfr task-auth-002
```

**Examples:**
```bash
/quinn *assess-nfr task-login-001
/quinn *assess-nfr task-payment-gateway
/quinn *assess-nfr task-api-performance
```

**What You Get:**
- NFR assessment report
- Status for each NFR category (PASS/CONCERN/FAIL)
- Specific findings and recommendations
- Test coverage for NFRs
- Mitigation strategies
- Priority-based action items

**6 NFR Categories:**

1. **Security** - Authentication, authorization, input validation, data protection
2. **Performance** - Response times, throughput, resource usage
3. **Reliability** - Error handling, logging, monitoring, recovery
4. **Maintainability** - Code quality, documentation, testability
5. **Scalability** - Load handling, resource scaling, bottlenecks
6. **Usability** - API design, error messages, user experience

**Complexity Factors:**
- NFR count (30%)
- System complexity (25%)
- Impact (20%)
- Test requirements (15%)
- Documentation (10%)

**When to Use:**
- When task spec includes explicit NFRs
- For critical systems (auth, payment, APIs)
- Performance-sensitive features
- Security-critical implementations

---

### 3. `*validate-quality-gate` - Quality Gate Decision

**Purpose:** Make final quality gate decision based on all quality assessments

**Syntax:**
```bash
/quinn *validate-quality-gate <task-id>
/quinn *validate-quality-gate task-auth-002
```

**Examples:**
```bash
/quinn *validate-quality-gate task-login-001
/quinn *validate-quality-gate task-checkout-flow
```

**What You Get:**
- Quality gate decision (PASS/CONCERNS/FAIL/WAIVED)
- Objective rationale with evidence
- Quality score (0-100%)
- Issue summary by severity
- Action items if not PASS
- Recommendation to proceed or block

**Quality Gate Decisions:**

**PASS (Quality Score ≥ 80%):**
- ✅ No critical issues
- ✅ Coverage ≥ 80%
- ✅ All P0 NFRs met
- ✅ No security vulnerabilities
- **Recommendation:** Proceed to deployment

**CONCERNS (Quality Score 60-79%):**
- ⚠️ Some issues (not critical)
- ⚠️ Coverage 60-79%
- ⚠️ P0 NFRs met, P1 may have concerns
- **Recommendation:** May proceed with action items tracked

**FAIL (Quality Score < 60%):**
- ❌ Critical issues present
- ❌ Coverage < 60%
- ❌ P0 NFR failures
- ❌ Security vulnerabilities
- **Recommendation:** Do NOT proceed, fix issues first

**WAIVED:**
- 🔓 User overrides CONCERNS/FAIL
- Requires written justification
- Action items tracked
- **Use with caution**

**Complexity Factors:**
- Issue severity (30%)
- NFR failures (25%)
- Coverage gaps (20%)
- Technical debt (15%)
- Risk (10%)

**When to Use:**
- After comprehensive review
- Before deployment decisions
- When multiple assessments exist
- For final go/no-go decisions

---

### 4. `*trace-requirements` - Trace Requirements

**Purpose:** Trace requirements (acceptance criteria) to implementation and tests for compliance verification

**Syntax:**
```bash
/quinn *trace-requirements <task-id>
/quinn *trace-requirements task-auth-002
```

**Examples:**
```bash
/quinn *trace-requirements task-login-001
/quinn *trace-requirements task-payment-001
```

**What You Get:**
- Traceability matrix (AC → Implementation → Tests)
- Implementation coverage percentage
- Test coverage percentage
- Gap analysis with severity
- Recommendations for closing gaps
- Compliance report

**Traceability Matrix:**
```
AC-1: User can login with email
  → Implementation: ✅ src/auth/login.ts:45-78
  → Tests: ✅ tests/auth/login.test.ts:12-45
  → Coverage: 95%

AC-2: Invalid credentials show error
  → Implementation: ✅ src/auth/login.ts:80-92
  → Tests: ⚠️ Missing edge case tests
  → Coverage: 65%
```

**Complexity Factors:**
- Requirement count (30%)
- Implementation complexity (25%)
- Test coverage (20%)
- Documentation (15%)
- Traceability gaps (10%)

**When to Use:**
- Verifying acceptance criteria met
- Before marking tasks complete
- For compliance audits
- When coverage concerns exist

---

### 5. `*assess-risk` - Assess Implementation Risks

**Purpose:** Assess implementation risks using P×I (Probability × Impact) methodology

**Syntax:**
```bash
/quinn *assess-risk <task-id>
/quinn *assess-risk task-auth-002
```

**Examples:**
```bash
/quinn *assess-risk task-new-payment-gateway
/quinn *assess-risk task-database-migration
/quinn *assess-risk task-third-party-api
```

**What You Get:**
- Risk assessment report
- Risk profile by category
- P×I scores for each risk (1-9)
- Mitigation strategies
- Test prioritization recommendations
- Escalation plan for critical risks

**Risk Categories:**

1. **Security** - Authentication, authorization, data protection
2. **Performance** - Bottlenecks, scalability, resource usage
3. **Reliability** - Error handling, recovery, monitoring
4. **Data Integrity** - Validation, consistency, corruption
5. **Integration** - External dependencies, APIs, services
6. **Deployment** - Configuration, rollback, downtime

**P×I Risk Scoring:**
- **Probability (P):** 1=Low, 2=Medium, 3=High
- **Impact (I):** 1=Low, 2=Medium, 3=High
- **Score = P × I (range 1-9)**

**Risk Levels:**
- **Critical (≥7):** Requires immediate mitigation, escalate to user
- **High (6):** Needs mitigation before deployment
- **Medium (4-5):** Monitor and mitigate if possible
- **Low (1-3):** Accept with monitoring

**Complexity Factors:**
- Technology risk (30%)
- Scope size (25%)
- Dependencies (20%)
- Team experience (15%)
- Impact (10%)

**When to Use:**
- Before starting complex implementations
- When using new technologies
- For critical systems
- Large scope or many dependencies

---

## Common Workflows

### Workflow 1: Standard Quality Review

**Goal:** Review implementation before deployment

```bash
# Step 1: Comprehensive review
/quinn *review task-login-001
# Output: Quality gate with PASS/CONCERNS/FAIL

# If PASS → Deploy
# If CONCERNS → Apply fixes
# If FAIL → Fix critical issues first

# Step 2 (if needed): Apply fixes
/james *apply-qa-fixes task-login-001

# Step 3: Re-review
/quinn *review task-login-001
# Output: Quality gate PASS
```

**Duration:** 10-20 minutes
**Output:** Quality gate decision

---

### Workflow 2: Deep NFR Assessment

**Goal:** Validate non-functional requirements

```bash
# Step 1: Assess NFRs
/quinn *assess-nfr task-api-endpoint
# Output: NFR report with 6 categories assessed

# Step 2: Trace requirements
/quinn *trace-requirements task-api-endpoint
# Output: Traceability matrix

# Step 3: Validate quality gate
/quinn *validate-quality-gate task-api-endpoint
# Output: Final PASS/CONCERNS/FAIL decision
```

**Duration:** 20-40 minutes
**Output:** Comprehensive quality assessment

---

### Workflow 3: Risk-Based Review

**Goal:** Review high-risk implementation

```bash
# Step 1: Assess risk BEFORE implementation
/quinn *assess-risk task-payment-gateway
# Output: Risk profile with mitigation strategies

# Step 2: Implement with mitigations
/james *implement task-payment-gateway
# (James follows mitigation strategies)

# Step 3: Review with risk focus
/quinn *review task-payment-gateway
# Output: Quality gate with risk verification

# Step 4: Validate all risks mitigated
/quinn *assess-risk task-payment-gateway
# Output: Updated risk profile (should show lower risks)
```

**Duration:** 40-90 minutes
**Output:** Risk-validated implementation

---

### Workflow 4: Compliance Verification

**Goal:** Verify full requirements compliance

```bash
# Step 1: Trace all requirements
/quinn *trace-requirements task-feature-001
# Output: Traceability matrix with gaps

# Step 2: Assess NFRs
/quinn *assess-nfr task-feature-001
# Output: NFR compliance report

# Step 3: Final quality gate
/quinn *validate-quality-gate task-feature-001
# Output: PASS (if compliant)
```

**Duration:** 15-30 minutes
**Output:** Full compliance report

---

## Quality Standards

### Code Quality Checks

Quinn evaluates code on multiple dimensions:

**Linting:**
- No errors allowed
- Warnings reviewed
- Style guide compliance

**Complexity:**
- Cyclomatic complexity < 10 (per function)
- Max file length: 300 lines
- Max function length: 50 lines

**Formatting:**
- Consistent indentation
- Naming conventions
- Comment quality

### Test Coverage Standards

**Minimum Requirements:**
- **Overall:** 80% coverage minimum
- **Critical paths:** 95% coverage
- **Edge cases:** Documented and tested
- **Integration tests:** For APIs and databases

**Coverage Types:**
- Line coverage
- Branch coverage
- Function coverage
- Statement coverage

---

## NFR Assessment Details

### Security NFRs

Quinn checks:
- ✅ Authentication implemented
- ✅ Authorization enforced
- ✅ Input validation present
- ✅ Data encryption used
- ✅ OWASP Top 10 addressed
- ✅ Secrets not in code

### Performance NFRs

Quinn validates:
- ✅ Response times < target
- ✅ Throughput meets requirements
- ✅ Resource usage reasonable
- ✅ No obvious bottlenecks
- ✅ Caching strategies used

### Reliability NFRs

Quinn verifies:
- ✅ Error handling comprehensive
- ✅ Logging implemented
- ✅ Monitoring hooks present
- ✅ Recovery mechanisms exist
- ✅ Graceful degradation

### Maintainability NFRs

Quinn assesses:
- ✅ Code is readable
- ✅ Documentation exists
- ✅ Tests are maintainable
- ✅ Low technical debt
- ✅ Modularity/separation of concerns

### Scalability NFRs

Quinn evaluates:
- ✅ Load handling tested
- ✅ Resource scaling possible
- ✅ Bottlenecks identified
- ✅ Database queries optimized
- ✅ Caching strategies

### Usability NFRs

Quinn reviews:
- ✅ API design intuitive
- ✅ Error messages clear
- ✅ Documentation complete
- ✅ Examples provided
- ✅ User experience smooth

---

## Tips & Best Practices

### ✅ Do's

- **Review early and often:** Catch issues before they compound
- **Use risk assessment:** For complex/critical features
- **Trust quality gates:** Data-driven decisions are objective
- **Apply fixes promptly:** Address CONCERNS before they become FAIL
- **Trace requirements:** Ensure nothing is missed
- **Document waivers:** If overriding gates, justify thoroughly

### ❌ Don'ts

- **Don't skip reviews:** Quality issues accumulate
- **Don't ignore NFRs:** Non-functional requirements are critical
- **Don't waive without justification:** Gates exist for reasons
- **Don't deploy with FAIL:** Fix critical issues first
- **Don't skip risk assessment:** For high-risk implementations
- **Don't ignore coverage gaps:** They often hide bugs

---

## Guardrails & Escalation

### Global Quality Guardrails

- **Min test coverage:** 80% (escalate if <60%)
- **No critical security issues:** Zero tolerance
- **All acceptance criteria verified:** 100% traceability required
- **Performance requirements met:** Per task spec
- **Max files per review:** 20 (escalate if >20)

### Escalation Triggers

Quinn escalates to user when:
- ❗ Coverage < 60%
- ❗ Critical security vulnerabilities found
- ❗ Quality score < 60% (FAIL)
- ❗ Missing NFR validation for P0 requirements
- ❗ Critical risks (P×I ≥ 7)
- ❗ Multiple high risks (P×I ≥ 6)

---

## Configuration

### Quinn Settings

Configure in `.claude/config.yaml`:

```yaml
quality:
  min_coverage: 80                # Minimum test coverage %
  critical_coverage: 95           # Coverage for critical paths
  max_complexity: 10              # Max cyclomatic complexity
  max_files_per_review: 20        # Max files per review

  quality_gate_thresholds:
    pass: 80                      # PASS if score ≥ 80%
    concerns: 60                  # CONCERNS if 60-79%
    fail: 60                      # FAIL if < 60%

  nfr_assessment:
    enabled: true
    categories:
      - security
      - performance
      - reliability
      - maintainability
      - scalability
      - usability

  risk_assessment:
    enabled: true
    critical_threshold: 7         # P×I ≥ 7 is critical
    high_threshold: 6             # P×I ≥ 6 is high
```

---

## Troubleshooting

### Issue: "Quality Gate FAIL - Coverage Too Low"

**Solution:** Add tests to increase coverage
```bash
# Step 1: Review coverage report
/quinn *review task-id
# See which files/functions lack coverage

# Step 2: Add missing tests
/james *test task-id
# James will identify gaps and suggest tests

# Step 3: Implement missing tests
# Add tests for uncovered code paths

# Step 4: Re-review
/quinn *review task-id
# Should now PASS with sufficient coverage
```

### Issue: "Critical NFR Failure - Security"

**Solution:** Address security concerns immediately
```bash
# Step 1: Review NFR details
/quinn *assess-nfr task-id
# See specific security findings

# Step 2: Apply fixes
/james *apply-qa-fixes task-id --scope high_severity
# Focus on security issues

# Step 3: Re-assess
/quinn *assess-nfr task-id
# Verify security NFRs now PASS
```

### Issue: "Traceability Gaps - Missing Tests for AC"

**Solution:** Add tests for uncovered acceptance criteria
```bash
# Step 1: Identify gaps
/quinn *trace-requirements task-id
# See which ACs lack test coverage

# Step 2: Add tests for missing ACs
# Write tests that specifically verify each AC

# Step 3: Re-trace
/quinn *trace-requirements task-id
# Should show 100% coverage
```

### Issue: "High Risk Implementation"

**Solution:** Mitigate risks before proceeding
```bash
# Step 1: Assess risks
/quinn *assess-risk task-id
# Identify critical/high risks

# Step 2: Create mitigation plan
# Document how each risk will be addressed

# Step 3: Implement with mitigations
/james *implement task-id
# Follow mitigation strategies

# Step 4: Verify risks mitigated
/quinn *assess-risk task-id
# Risks should now be lower
```

---

## Next Steps

**After Quality Review:**
1. **Fix Issues:** Use James to apply QA fixes
2. **Deploy:** If quality gate PASS, proceed to deployment
3. **Monitor:** Track quality metrics over time

**Related Guides:**
- [James (Developer) Quick Start](./quickstart-james.md)
- [Alex (Planner) Quick Start](./quickstart-alex.md)
- [Orchestrator Quick Start](./quickstart-orchestrator.md)
- [V2 Architecture](./V2-ARCHITECTURE.md)

---

**Questions?** See [V2 Architecture Documentation](./V2-ARCHITECTURE.md)

**Quinn (Quality) Quick Start Guide**
*Part of BMAD Enhanced V2 Architecture*
