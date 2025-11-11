# NFR Gap Identification and Remediation

This reference provides detailed methodology for identifying NFR gaps, assigning severity levels, prioritizing remediation, and providing actionable recommendations.

---

## Table of Contents

1. [Gap Definition](#gap-definition)
2. [Gap Severity Levels](#gap-severity-levels)
3. [Gap Prioritization](#gap-prioritization)
4. [Risk Amplification](#risk-amplification)
5. [Gap Documentation Format](#gap-documentation-format)
6. [Category-Specific Gap Patterns](#category-specific-gap-patterns)
7. [Remediation Guidance](#remediation-guidance)
8. [Gap Tracking and Closure](#gap-tracking-and-closure)

---

## Gap Definition

An **NFR gap** is a deficiency where an NFR criterion is not fully met (scored as CONCERNS or FAIL). Gaps represent the difference between current implementation and desired state.

### Gap Identification Criteria

A gap exists when:
1. **Criterion scored as FAIL (0 points)**: Critical gap, criterion not met
2. **Criterion scored as CONCERNS (50 points)**: Moderate gap, criterion partially met
3. **Evidence shows risk**: Even if scored as PASS, if evidence shows potential risk (e.g., security vulnerability), flag as gap

### Gap vs Non-Gap

**Gap Example:**
```
Criterion: Input Validation
Score: CONCERNS (50 points)
Evidence: Zod validation present but no sanitization for XSS/SQL injection
→ GAP: Incomplete input validation poses security risk
```

**Non-Gap Example:**
```
Criterion: HTTPS/TLS
Score: UNCLEAR (excluded)
Evidence: Cannot determine (handled at infrastructure level)
→ NO GAP: Excluded from assessment, not a deficiency
```

---

## Gap Severity Levels

Gaps are classified into four severity levels: CRITICAL, HIGH, MEDIUM, LOW

### CRITICAL (Severity Level 0)

**Definition:** Immediate production blocker, poses significant security/reliability risk, must fix before merge.

**Characteristics:**
- Security vulnerability with exploitable risk (critical CVEs, SQL injection, XSS)
- Reliability failure causing system instability (no error handling, data corruption)
- Compliance violation (GDPR, HIPAA, PCI-DSS breach)
- Criterion scored as FAIL in Security or Reliability category
- Amplified by HIGH risk in risk profile

**Priority:** P0 - Must fix before merge/deployment

**Examples:**
- GAP-SEC-1: Critical dependency vulnerabilities (3 CVEs with CVSS 9.0+)
- GAP-SEC-2: No authentication on sensitive endpoints
- GAP-REL-1: No error handling, application crashes on errors
- GAP-SEC-3: Hardcoded secrets (API keys, passwords) in code

---

### HIGH (Severity Level 1)

**Definition:** Significant gap that should be addressed before release, poses moderate risk, degrades quality significantly.

**Characteristics:**
- Security weakness without immediate exploit (weak authentication, missing rate limiting)
- Performance degradation (no caching, N+1 queries, slow response times)
- Maintainability issues (missing documentation, no tests)
- Criterion scored as FAIL in Performance/Maintainability, or CONCERNS in Security/Reliability
- Amplified by MEDIUM risk in risk profile

**Priority:** P1 - Should fix before release

**Examples:**
- GAP-SEC-4: Incomplete input sanitization (XSS risk)
- GAP-PERF-1: No caching layer (high latency, poor scalability)
- GAP-REL-2: No monitoring/observability (cannot detect production issues)
- GAP-MAINT-1: Missing documentation (README, API docs)
- GAP-SCALE-1: No async job processing (expensive operations block requests)

---

### MEDIUM (Severity Level 2)

**Definition:** Moderate gap that should be addressed soon, quality improvement opportunity, technical debt.

**Characteristics:**
- Moderate issues that don't block release but affect quality
- Performance optimization opportunities
- Code quality improvements (complexity, duplication)
- Criterion scored as CONCERNS in Performance/Maintainability/Scalability
- May be amplified by LOW risk in risk profile

**Priority:** P2 - Should fix in next sprint

**Examples:**
- GAP-PERF-2: Potential N+1 queries (minor performance impact)
- GAP-MAINT-2: High complexity functions (cyclomatic complexity >10)
- GAP-MAINT-3: Code duplication (10-15% duplication)
- GAP-SCALE-2: Missing database indexes on foreign keys
- GAP-USE-2: Generic error messages (difficult to debug)

---

### LOW (Severity Level 3)

**Definition:** Minor gap, nice-to-have improvement, minimal impact, can be addressed when convenient.

**Characteristics:**
- Minor usability improvements
- Nice-to-have features (HATEOAS, advanced filtering)
- Documentation enhancements
- Criterion scored as CONCERNS in Usability or minor CONCERNS elsewhere

**Priority:** P3 - Nice to have, backlog

**Examples:**
- GAP-USE-3: Missing HATEOAS links (not critical for API usability)
- GAP-MAINT-4: Minor linting warnings
- GAP-DOC-1: Missing inline comments for simple functions
- GAP-PERF-3: Bundle size could be optimized further (but acceptable)

---

## Gap Prioritization

Gaps are prioritized using a combination of severity level and impact on quality gate.

### Priority Levels

| Priority | Label | Description | Timeline |
|----------|-------|-------------|----------|
| P0 | Must Fix | Blocks merge/deployment | Before merge |
| P1 | Should Fix | Significantly impacts quality | Before release |
| P2 | Nice to Fix | Moderate quality improvement | Next sprint |
| P3 | Backlog | Minor improvement | When convenient |

### Priority Assignment Rules

**P0 (Must Fix) - Assigned When:**
- Gap severity is CRITICAL
- Security category score <50%
- Reliability category score <50%
- Gap matches HIGH risk in risk profile (risk amplification)
- Compliance violation (legal/regulatory requirement)

**P1 (Should Fix) - Assigned When:**
- Gap severity is HIGH
- Overall NFR score 60-74% (CONCERNS status)
- Performance category score <60%
- Gap matches MEDIUM risk in risk profile
- Maintainability/Scalability gaps affecting long-term health

**P2 (Nice to Fix) - Assigned When:**
- Gap severity is MEDIUM
- Overall NFR score 75-89% (PASS but could be better)
- Gap in non-critical categories (Usability, Scalability)
- Technical debt that should be addressed

**P3 (Backlog) - Assigned When:**
- Gap severity is LOW
- Overall NFR score ≥90% (Excellent)
- Nice-to-have improvements
- Documentation enhancements

### Priority Matrix

| Gap Severity | Category | Risk Amplification | Priority |
|--------------|----------|-------------------|----------|
| CRITICAL | Security/Reliability | HIGH | P0 |
| CRITICAL | Other | MEDIUM | P0 |
| HIGH | Security/Reliability | MEDIUM | P0 |
| HIGH | Performance | MEDIUM | P1 |
| HIGH | Other | LOW | P1 |
| MEDIUM | Any | LOW | P2 |
| LOW | Any | None | P3 |

---

## Risk Amplification

When NFR gaps match risks identified in the risk profile, gap severity is amplified.

### Risk Profile Integration

**Risk Profile Input:**
```markdown
Risk #2: SQL Injection
- Probability: 3 (Medium)
- Impact: 4 (High)
- Score: 12 (HIGH risk)
- Category: Security
```

**NFR Gap Found:**
```markdown
Criterion: Input Validation
Status: CONCERNS (50 points)
Evidence: No sanitization for SQL injection
Base Severity: MEDIUM (CONCERNS in Security)
```

**Amplification Logic:**
```
Base Severity: MEDIUM
Risk Profile Match: HIGH risk (score 12)
Amplification: +2 levels (MEDIUM → HIGH → CRITICAL)
Final Severity: CRITICAL
Final Priority: P0 (must fix before merge)
```

### Amplification Rules

| Risk Score | Risk Level | Amplification |
|------------|------------|---------------|
| ≥9 | HIGH | +2 levels (MEDIUM→CRITICAL, HIGH→CRITICAL) |
| 6-8 | MEDIUM | +1 level (LOW→MEDIUM, MEDIUM→HIGH) |
| 3-5 | LOW | +0 levels (no change) |
| <3 | NEGLIGIBLE | +0 levels (no change) |

### Amplification Examples

**Example 1: Performance Gap + HIGH Performance Risk**
```
Base: MEDIUM gap (N+1 queries - CONCERNS in Performance)
Risk: HIGH performance risk (score 10) in risk profile
Amplification: +2 levels → CRITICAL
Priority: P0 (performance is production-critical)
```

**Example 2: Maintainability Gap + LOW Maintainability Risk**
```
Base: MEDIUM gap (missing documentation)
Risk: LOW maintainability risk (score 4) in risk profile
Amplification: +0 levels → MEDIUM
Priority: P2 (not critical)
```

---

## Gap Documentation Format

Each gap should be documented with a standardized format for tracking and remediation.

### Gap Template

```markdown
## GAP-{CATEGORY}-{NUMBER}: {Title}

**Category:** {Security/Performance/Reliability/Maintainability/Scalability/Usability}
**Severity:** {CRITICAL/HIGH/MEDIUM/LOW}
**Priority:** {P0/P1/P2/P3}
**Criterion:** {Criterion name}
**Status:** {FAIL/CONCERNS}

### Description
{Detailed description of the gap}

### Evidence
- **File:** {file-path}:{line-numbers}
- **Finding:** {What was found or missing}
- **Code Example:**
  ```{language}
  {Code snippet showing the issue}
  ```

### Impact
- **Risk:** {What could go wrong}
- **User Impact:** {How this affects users}
- **Business Impact:** {How this affects business}

### Recommendation
{Specific, actionable steps to close the gap}

### Estimated Effort
{Time estimate to fix: e.g., 30 min, 2-3h, 1-2 days}

### Dependencies
{Any dependencies or prerequisites for fixing}

### Related Risks
{Links to related risks from risk profile}

### Acceptance Criteria for Closure
- [ ] {Specific criterion 1}
- [ ] {Specific criterion 2}
- [ ] {Re-run NFR assessment and verify criterion now scores PASS}
```

### Example: Complete Gap Documentation

```markdown
## GAP-SEC-1: Critical Dependency Vulnerabilities

**Category:** Security
**Severity:** CRITICAL
**Priority:** P0 (must fix before merge)
**Criterion:** Dependency Vulnerabilities
**Status:** FAIL (0 points)

### Description
Dependency vulnerability scan identified 3 critical CVEs and 5 high-severity vulnerabilities in project dependencies. Critical vulnerabilities include:
1. lodash@4.17.15 - Prototype Pollution (CVE-2020-8203, CVSS 9.8)
2. express@4.16.0 - DoS vulnerability (CVE-2019-5476, CVSS 9.0)
3. jsonwebtoken@8.5.0 - Signature verification bypass (CVE-2022-23529, CVSS 9.8)

### Evidence
- **File:** package.json:12-35
- **Tool:** npm audit (run: 2025-10-28)
- **Finding:** 3 critical, 5 high, 12 moderate vulnerabilities
- **Scan Output:**
  ```json
  {
    "critical": 3,
    "high": 5,
    "moderate": 12,
    "low": 25
  }
  ```

### Impact
- **Risk:** Exploitable vulnerabilities allow attackers to:
  - Bypass authentication (jsonwebtoken bypass)
  - Execute arbitrary code (lodash prototype pollution)
  - Crash application (express DoS)
- **User Impact:** User accounts compromised, data exposed, service unavailable
- **Business Impact:** Data breach, regulatory fines (GDPR), reputation damage

### Recommendation
1. Update vulnerable dependencies immediately:
   ```bash
   npm update lodash express jsonwebtoken
   npm audit fix --force
   ```
2. Verify updates don't break existing functionality (run test suite)
3. Re-run npm audit to confirm vulnerabilities resolved
4. Consider using automated dependency updates (Dependabot, Renovate)

### Estimated Effort
30 minutes - 1 hour (update + test + verify)

### Dependencies
- None (can be fixed immediately)

### Related Risks
- Risk #1 from risk profile: "Dependency vulnerabilities" (Score: 12, HIGH)

### Acceptance Criteria for Closure
- [x] All critical vulnerabilities resolved (0 critical)
- [x] High vulnerabilities reduced to ≤2
- [x] Test suite passes after dependency updates
- [x] Re-run NFR assessment: "Dependency Vulnerabilities" scores PASS
```

---

## Category-Specific Gap Patterns

Common gap patterns by NFR category:

### Security Gap Patterns

**Pattern 1: Insufficient Input Validation**
```
Symptom: Input validation present but no sanitization
Severity: HIGH (potential XSS/SQL injection)
Fix: Add sanitization layer (DOMPurify for XSS, parameterized queries for SQL)
Effort: 1-2 hours
```

**Pattern 2: Missing Authentication/Authorization**
```
Symptom: Sensitive endpoints not protected
Severity: CRITICAL (unauthorized access)
Fix: Add authentication middleware, implement RBAC
Effort: 4-8 hours
```

**Pattern 3: Dependency Vulnerabilities**
```
Symptom: Outdated dependencies with known CVEs
Severity: CRITICAL if critical CVEs, HIGH otherwise
Fix: Update dependencies, test thoroughly
Effort: 30 min - 2 hours
```

---

### Performance Gap Patterns

**Pattern 1: No Caching Layer**
```
Symptom: Frequently accessed data fetched from database every request
Severity: HIGH (high latency, poor scalability)
Fix: Implement Redis caching with TTL and invalidation
Effort: 3-4 hours
```

**Pattern 2: N+1 Query Problem**
```
Symptom: ORM fetching related data in loop
Severity: MEDIUM-HIGH (increased latency under load)
Fix: Use includes/joins to fetch data in single query
Effort: 1-2 hours per query
```

**Pattern 3: No Load Testing**
```
Symptom: Performance not validated under expected load
Severity: MEDIUM (unknown performance characteristics)
Fix: Create and run load tests (Artillery, k6)
Effort: 2-3 hours
```

---

### Reliability Gap Patterns

**Pattern 1: No Monitoring/Observability**
```
Symptom: No health checks, metrics, or alerting
Severity: CRITICAL (cannot detect production issues)
Fix: Add /health endpoint, integrate Prometheus/Datadog, configure alerts
Effort: 2-3 hours
```

**Pattern 2: Insufficient Error Handling**
```
Symptom: Unhandled errors causing application crashes
Severity: CRITICAL (application instability)
Fix: Add try-catch blocks, global error handler, error logging
Effort: 2-4 hours
```

**Pattern 3: No Log Aggregation**
```
Symptom: Console logs only, no centralized logging
Severity: HIGH (difficult to debug production issues)
Fix: Add CloudWatch/ELK transport to logger, implement request ID tracking
Effort: 1-2 hours
```

---

### Maintainability Gap Patterns

**Pattern 1: Missing Documentation**
```
Symptom: No README, no API docs, sparse inline comments
Severity: HIGH (poor developer experience, slow onboarding)
Fix: Create README, generate OpenAPI spec, add JSDoc comments
Effort: 3-5 hours
```

**Pattern 2: Low Test Coverage**
```
Symptom: <60% test coverage, critical paths untested
Severity: MEDIUM-HIGH (difficult to refactor safely)
Fix: Add unit tests for critical paths, increase coverage to ≥80%
Effort: 4-8 hours
```

**Pattern 3: High Complexity Functions**
```
Symptom: Functions with cyclomatic complexity >10
Severity: MEDIUM (difficult to maintain, test, debug)
Fix: Refactor complex functions into smaller functions
Effort: 2-4 hours per function
```

---

### Scalability Gap Patterns

**Pattern 1: No Async Job Processing**
```
Symptom: Expensive operations (email, reports) executed synchronously
Severity: HIGH (request timeouts, poor scalability)
Fix: Implement job queue (Bull/BullMQ with Redis)
Effort: 4-6 hours
```

**Pattern 2: Missing Database Indexes**
```
Symptom: Foreign keys not indexed, slow queries under load
Severity: MEDIUM (performance degrades at scale)
Fix: Add indexes on foreign keys and frequently queried columns
Effort: 30 min - 1 hour per index
```

**Pattern 3: Stateful Design**
```
Symptom: In-memory sessions, local file storage
Severity: HIGH (cannot scale horizontally)
Fix: Use external session store (Redis), object storage (S3)
Effort: 4-8 hours
```

---

### Usability Gap Patterns

**Pattern 1: Missing API Documentation**
```
Symptom: No OpenAPI spec, no usage examples
Severity: HIGH (poor developer experience)
Fix: Generate OpenAPI spec (tsoa, swagger-jsdoc), create examples
Effort: 2-3 hours
```

**Pattern 2: Generic Error Messages**
```
Symptom: Errors like "Invalid input" with no field details
Severity: MEDIUM (difficult for API consumers to debug)
Fix: Enhance error responses with field-level details
Effort: 1-2 hours
```

**Pattern 3: Poor API Design**
```
Symptom: Non-RESTful endpoints, inconsistent naming
Severity: MEDIUM (confusing for API consumers)
Fix: Refactor endpoints to follow REST conventions
Effort: 4-6 hours (requires API versioning)
```

---

## Remediation Guidance

### Remediation Workflow

1. **Prioritize Gaps**: Sort by priority (P0 → P1 → P2 → P3)
2. **Address P0 Gaps**: Fix all P0 gaps before merge (production blockers)
3. **Plan P1 Gaps**: Create tickets for P1 gaps, fix before release
4. **Track P2/P3 Gaps**: Add to backlog, address when capacity allows
5. **Re-run Assessment**: After fixing gaps, re-run NFR assessment to validate closure
6. **Document Closure**: Update gap status, document remediation actions taken

### Effort Estimation Guidelines

| Complexity | Effort | Examples |
|------------|--------|----------|
| Trivial | 15-30 min | Update dependency, add simple config |
| Simple | 1-2 hours | Add validation, implement caching |
| Moderate | 3-4 hours | Add monitoring, refactor complex function |
| Complex | 1-2 days | Implement authentication, add job queue |
| Major | 3-5 days | Redesign API, implement comprehensive testing |

### Remediation Best Practices

1. **Fix P0 gaps first**: Don't merge with production blockers
2. **Test after fixing**: Ensure fix doesn't break existing functionality
3. **Document changes**: Update documentation affected by fixes
4. **Re-run automated checks**: Verify gaps are resolved objectively
5. **Update tracking**: Mark gaps as closed in issue tracker
6. **Re-assess**: Run nfr-assess again to confirm criterion now scores PASS

---

## Gap Tracking and Closure

### Gap Lifecycle

1. **Identified**: Gap discovered during NFR assessment
2. **Documented**: Gap documented with template, severity assigned
3. **Prioritized**: Priority assigned based on severity and impact
4. **Tracked**: Gap added to issue tracker (Jira, GitHub Issues, etc.)
5. **In Progress**: Developer working on fix
6. **Fixed**: Fix implemented and tested
7. **Verified**: Re-run NFR assessment, criterion now scores PASS
8. **Closed**: Gap marked as closed in tracker

### Gap Closure Criteria

A gap is considered closed when:
- [x] Remediation action completed (code fix, config change, etc.)
- [x] Tests pass (existing + new tests for the fix)
- [x] NFR assessment re-run, criterion now scores PASS (or CONCERNS → PASS for HIGH gaps)
- [x] Evidence documented (new evidence showing gap is closed)
- [x] Peer review completed (code review approved)
- [x] Gap marked as closed in issue tracker

### Re-Assessment After Fixes

After fixing gaps, re-run NFR assessment to verify:
1. **Criterion score improved**: FAIL → CONCERNS or PASS, CONCERNS → PASS
2. **Category score improved**: Overall category score increased
3. **Overall NFR score improved**: Overall score increased toward PASS threshold
4. **No new gaps introduced**: Fixes didn't create new issues

**Example:**
```
Before Fix:
- Security Score: 70% (CONCERNS)
- Criterion "Dependency Vulnerabilities": FAIL (0 points)
- Gap: GAP-SEC-1 (3 critical CVEs)

After Fix:
- Security Score: 85% (PASS)
- Criterion "Dependency Vulnerabilities": PASS (100 points)
- Gap: GAP-SEC-1 CLOSED ✅
```

---

*This reference provides comprehensive gap identification and remediation guidance for NFR assessment.*
