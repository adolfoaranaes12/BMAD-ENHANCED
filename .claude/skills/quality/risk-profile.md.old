# Quality Skill: Risk Profile Assessment

<!-- BMAD Enhanced Quality Skill -->
<!-- Inspired by BMAD-METHOD QA risk profiling pattern -->
<!-- Version: 1.0 -->

## Purpose

Assess implementation risks before or during development using Probability × Impact (P×I) scoring methodology. Identifies potential issues early, enables risk-based test prioritization, and informs quality gate decisions.

**Key Innovation (BMAD Pattern):**
- Risk assessed BEFORE implementation starts (earliest intervention point)
- P×I scoring (1-9 scale) for objective risk measurement
- Mitigation strategies for each identified risk
- Direct integration with test design and quality gates

## When to Use This Skill

Use this skill when you need to:
- Assess risks before starting implementation
- Prioritize test scenarios by risk level
- Identify potential issues early
- Inform quality gate decisions

**Best Used:**
- After task spec creation, before implementation
- For complex or high-risk features
- When planning test strategy
- During quality review for gate decision

**Can Skip For:**
- Simple CRUD operations with no external dependencies
- Bug fixes with clear root cause
- Well-established patterns with no unknowns

## Risk Scoring Methodology

### Probability (P): Likelihood of Risk Occurring

**Scale 1-3:**
- **1 - Low:** Unlikely to occur (< 20% chance)
- **2 - Medium:** May occur (20-60% chance)
- **3 - High:** Likely to occur (> 60% chance)

### Impact (I): Severity if Risk Occurs

**Scale 1-3:**
- **1 - Low:** Minor inconvenience, easy fix
- **2 - Medium:** Significant issue, moderate effort to fix
- **3 - High:** Critical failure, major effort to fix or business impact

### Risk Score: P × I

**Scale 1-9:**
- **9 (P:3 × I:3):** Critical - Likely high-impact failure
- **6-8:** High - Serious risks requiring mitigation
- **3-5:** Medium - Manageable risks, monitor closely
- **1-2:** Low - Minor risks, standard precautions

### Quality Gate Impact

**Configured in `.claude/config.yaml`:**
```yaml
quality:
  riskScoreThreshold: 6  # Default
```

**Auto-apply rules:**
- Risk score ≥9 → Quality gate FAIL (must mitigate)
- Risk score ≥6 → Quality gate CONCERNS (mitigation plan required)
- Risk score <6 → No automatic gate impact

## Risk Categories

### 1. Technical Risk
- Complexity of implementation
- Unknown technologies or APIs
- Integration challenges
- Dependencies on external systems
- Data structure changes

### 2. Security Risk
- Authentication/authorization vulnerabilities
- Data exposure risks
- Injection vulnerabilities (SQL, XSS, etc.)
- Privilege escalation
- Insecure data transmission

### 3. Performance Risk
- Response time degradation
- Scalability issues
- Resource consumption (memory, CPU)
- Database query inefficiency (N+1 queries)
- Network latency

### 4. Data Risk
- Data integrity issues
- Migration complexity
- Data loss potential
- Consistency problems
- Backup/recovery concerns

### 5. Business Risk
- User impact scope
- Revenue implications
- Compliance requirements
- User experience degradation
- Operational dependencies

### 6. Operational Risk
- Deployment complexity
- Rollback difficulty
- Monitoring gaps
- Alert configuration
- Documentation needs

## SEQUENTIAL Skill Execution

**CRITICAL:** Do not proceed to next step until current step is complete

### Step 0: Load Configuration and Task Context

**Actions:**

1. Load `.claude/config.yaml`:
   - Extract `quality.riskScoreThreshold`
   - Extract `quality.qualityLocation`

2. Get task file path from user:
   - Example: `.claude/tasks/task-006-user-signup.md`
   - Verify file exists

3. Read task specification:
   - Load objective and acceptance criteria
   - Load context (data models, APIs, components, constraints)
   - Load task breakdown
   - Understand what will be implemented

4. Determine assessment mode:
   - **Pre-implementation:** Task status is "Draft" or "Approved"
   - **During development:** Task status is "InProgress"
   - **Post-implementation:** Task status is "Review"

**Output:**
- Configuration loaded
- Task context understood
- Assessment mode determined

**Halt Conditions:**
- Configuration missing
- Task file missing or unreadable

### Step 1: Identify Risk Areas

**Actions:**

1. **Analyze task complexity:**
   - How many tasks/subtasks? (>10 = higher complexity)
   - How many systems involved? (>3 = higher integration risk)
   - New patterns or established patterns?
   - Unknown vs. familiar technologies?

2. **Review technical context:**
   - What data models are involved?
   - What external APIs/services?
   - What authentication/authorization?
   - What database operations?
   - What UI components (if applicable)?

3. **Check acceptance criteria for risk signals:**
   - Security requirements mentioned?
   - Performance targets specified?
   - Data migration needed?
   - Complex business logic?
   - User-facing changes?

4. **Identify previous issues:**
   - Check previous task completion notes
   - Any recurring problems in this area?
   - Known technical debt?

5. **Brainstorm potential risks in each category:**
   - Technical: What could go wrong technically?
   - Security: What security issues might arise?
   - Performance: What could be slow?
   - Data: What data issues possible?
   - Business: What business impact if wrong?
   - Operational: What deployment issues?

**Output:**
- List of potential risk areas (10-20 identified)
- Initial categorization
- Context for scoring

**Example for User Signup Task:**
```
Potential Risks Identified:
- SQL injection in email validation (Security)
- Weak password acceptance (Security)
- N+1 query on user listing (Performance)
- Email service failure (Technical)
- Duplicate email race condition (Data)
- No rate limiting on signup endpoint (Security)
- Plain text password logging (Security)
- Migration complexity (Data)
- User lockout if email service down (Business)
- No monitoring for failed signups (Operational)
```

**Halt Conditions:**
- Task too vague to assess (need more detail)
- Cannot identify any meaningful risks (task may be trivial)

### Step 2: Score Each Risk (P×I)

**Actions:**

For each identified risk:

1. **Assess Probability (P: 1-3):**
   - Consider: Technical skill required, complexity, unknowns
   - Ask: How likely is this to occur?
   - 1: Unlikely (good patterns, known approaches)
   - 2: Possible (some unknowns, moderate complexity)
   - 3: Likely (complex, many unknowns, new territory)

2. **Assess Impact (I: 1-3):**
   - Consider: User impact, business impact, fix difficulty
   - Ask: How severe if this happens?
   - 1: Minor (easy fix, low impact)
   - 2: Significant (moderate effort, notable impact)
   - 3: Critical (hard fix, high impact, security/data loss)

3. **Calculate Risk Score:**
   - Risk Score = P × I (1-9)

4. **Document reasoning:**
   - Why this probability?
   - Why this impact?
   - What evidence supports this?

**Output:**
- Each risk scored with P, I, and total score
- Reasoning documented
- Risks sorted by score (highest first)

**Example Scoring:**
```
Risk: SQL injection in email validation
Probability: 2 (Possible - using Zod but need to verify Prisma usage)
Impact: 3 (Critical - data breach, compliance violation)
Score: 6 (High Risk)
Reasoning: While using validation library, if raw SQL queries used
anywhere in user creation flow, injection possible. Impact is critical
due to potential data breach and compliance implications.

Risk: Weak password acceptance
Probability: 2 (Possible - need to verify regex strength)
Impact: 2 (Significant - account compromise, but limited to individual)
Score: 4 (Medium Risk)
Reasoning: Password validation strength depends on regex implementation.
Weak passwords enable brute force attacks. Impact moderate as affects
individual accounts, not entire system.

Risk: N+1 query on user listing
Probability: 3 (Likely - common ORM pitfall)
Impact: 2 (Significant - performance degradation, not data loss)
Score: 6 (High Risk)
Reasoning: Very common issue with ORMs when loading relationships.
Highly probable if not explicitly addressed. Impact significant for
scalability but not catastrophic.
```

**Halt Conditions:**
- Unable to assess probability (insufficient information)
- Unable to determine impact (unclear requirements)

### Step 3: Develop Mitigation Strategies

**Actions:**

For each risk (prioritize high scores first):

1. **Identify mitigation approach:**
   - **Prevention:** How to prevent risk from occurring?
   - **Detection:** How to detect if risk occurs?
   - **Recovery:** How to recover if risk occurs?

2. **Specify concrete actions:**
   - What specific code/design changes?
   - What tests to write?
   - What monitoring to add?
   - What documentation needed?

3. **Assign to appropriate phase:**
   - **During Implementation:** Handle when coding
   - **Testing:** Validate through tests
   - **Deployment:** Address in deployment process
   - **Monitoring:** Detect in production

4. **Estimate effort:**
   - Minimal (< 1 hour)
   - Moderate (1-4 hours)
   - Significant (> 4 hours)

**Output:**
- Mitigation strategy for each risk
- Concrete actions specified
- Phase assignment
- Effort estimate

**Example Mitigations:**
```
Risk: SQL injection (Score: 6)
Mitigation Strategy:
  Prevention:
    - Use Prisma ORM exclusively (no raw SQL)
    - Validate all inputs with Zod schemas
    - Code review checklist: No string concatenation in queries
  Detection:
    - Unit tests with injection attempts
    - Integration tests with malicious payloads
    - Security audit before merge
  Recovery:
    - N/A (prevention-focused)

  Concrete Actions:
    1. Review all database operations for Prisma usage
    2. Add Zod validation schemas for all user inputs
    3. Write security tests in tests/security/injection.test.ts
    4. Run OWASP ZAP scan before production

  Phase: During Implementation + Testing
  Effort: Moderate (2-3 hours)

Risk: N+1 query (Score: 6)
Mitigation Strategy:
  Prevention:
    - Use Prisma's `include` for eager loading
    - Add pagination with `take` and `skip`
    - Document query patterns in architecture
  Detection:
    - Query logging in test environment
    - Performance tests with large datasets
    - Prisma query logging enabled
  Recovery:
    - Add eager loading if detected
    - Implement caching as backup

  Concrete Actions:
    1. Use `prisma.user.findMany({ include: { profile: true } })`
    2. Add query logging: PRISMA_QUERY_LOG=true in test
    3. Write performance test with 100+ users
    4. Document pattern in docs/architecture/database.md

  Phase: During Implementation + Testing
  Effort: Minimal (< 1 hour)
```

**Halt Conditions:**
- Cannot identify viable mitigation (risk may be too fundamental)
- Mitigation effort exceeds task scope (may need redesign)

### Step 4: Prioritize Test Scenarios

**Actions:**

1. **Map risks to test priorities:**
   - **P0 (Critical):** Risks with score ≥7
   - **P1 (High):** Risks with score 5-6
   - **P2 (Medium):** Risks with score 3-4
   - **P3 (Low):** Risks with score 1-2

2. **Identify must-have tests:**
   - Security risks → Security test scenarios
   - Performance risks → Performance test scenarios
   - Data risks → Data integrity test scenarios
   - Integration risks → Integration test scenarios

3. **Specify test scenarios:**
   - For each high-risk area (score ≥6)
   - Describe test scenario
   - Specify test level (unit/integration/E2E)
   - Assign priority

4. **Document test-risk mapping:**
   - Which tests validate which risks?
   - What coverage is needed?
   - What scenarios would expose the risk?

**Output:**
- Test scenarios prioritized by risk
- Test-risk mapping
- Must-have vs. nice-to-have tests clear

**Example Test Prioritization:**
```
P0 (Critical) Tests - Must Have:
- Security: SQL injection attempts in user creation
- Security: XSS attempts in user profile fields
- Data: Duplicate email race condition test

P1 (High) Tests - Should Have:
- Performance: N+1 query detection with 100+ users
- Security: Brute force password attempts with rate limiting
- Data: User data integrity after concurrent updates

P2 (Medium) Tests - Nice to Have:
- Performance: Response time under load (1000 req/s)
- Security: Session fixation attack prevention
- Data: Backup/restore validation

Test-Risk Mapping:
Security Risk: SQL injection (Score: 6)
→ Test: tests/security/injection.test.ts
  - Scenario: POST /api/users with SQL in email field
  - Level: Integration
  - Priority: P0
  - Expected: 400 Bad Request, sanitized error message

Performance Risk: N+1 query (Score: 6)
→ Test: tests/performance/user-listing.test.ts
  - Scenario: GET /api/users with 100+ users and profiles
  - Level: Integration
  - Priority: P1
  - Expected: Max 3 queries, response < 200ms
```

**Halt Conditions:**
- None (prioritization always possible)

### Step 5: Generate Risk Profile Report

**Actions:**

1. Load risk profile template:
   - Read `.claude/templates/risk-profile.md`

2. Populate risk matrix:
   - List all risks sorted by score (highest first)
   - Include category, P, I, score, mitigation

3. Create high-risk summary:
   - Risks with score ≥6
   - Mitigation strategies
   - Validation approach

4. Document test prioritization:
   - P0/P1/P2 test scenarios
   - Test-risk mapping

5. Add quality gate impact:
   - Will any risks trigger FAIL? (score ≥9)
   - Will any risks trigger CONCERNS? (score ≥6)
   - What's needed for PASS?

6. Generate file path:
   - Format: `{qualityLocation}/assessments/{taskId}-risk-{YYYYMMDD}.md`
   - Example: `.claude/quality/assessments/task-006-risk-20251028.md`

7. Write risk profile file

**Output:**
- Risk profile file created
- All risks documented with scores
- Mitigation strategies specified
- Test priorities established

**File Structure:**
```markdown
# Risk Profile: User Signup Implementation

**Task:** task-006-user-signup.md
**Date:** 2025-10-28
**Assessor:** risk-profile-skill-v1.0
**Status:** Pre-Implementation

---

## Risk Summary

**Total Risks Identified:** 10
**Critical (≥7):** 1
**High (6):** 3
**Medium (3-5):** 4
**Low (1-2):** 2

**Quality Gate Impact:**
- Risk score threshold: 6 (from config)
- Risks ≥6: 4 risks identified
- **Predicted Gate Status:** CONCERNS (due to 4 high-risk areas)
- **To Achieve PASS:** Mitigate or test all high-risk areas

---

## Risk Matrix

| # | Category | Risk | P | I | Score | Mitigation |
|---|----------|------|---|---|-------|------------|
| 1 | Security | Plain text password in logs | 3 | 3 | **9** | Never log password field, audit logging |
| 2 | Security | SQL injection in email validation | 2 | 3 | **6** | Prisma ORM only, Zod validation, security tests |
| 3 | Performance | N+1 query on user listing | 3 | 2 | **6** | Eager loading, pagination, performance tests |
| 4 | Security | No rate limiting on signup | 2 | 3 | **6** | Add express-rate-limit, 5 req/min |
| 5 | Data | Duplicate email race condition | 2 | 2 | **4** | Unique constraint, error handling test |
| 6 | Technical | Email service failure | 2 | 2 | **4** | Try-catch, retry logic, queue for resilience |
| 7 | Security | Weak password acceptance | 2 | 2 | **4** | Strong regex, test with weak passwords |
| 8 | Data | Database migration complexity | 2 | 2 | **4** | Migration script, rollback plan, test data |
| 9 | Business | User lockout if email down | 1 | 2 | **2** | Queue emails, allow signup without confirmation |
| 10 | Operational | No monitoring for failures | 1 | 2 | **2** | Add metrics, alert on error rate >5% |

---

## Critical Risks (Score ≥7)

### Risk 1: Plain text password in logs (Score: 9)

**Category:** Security
**Probability:** 3 (High) - Common mistake, easy to accidentally log
**Impact:** 3 (Critical) - Compliance violation, account compromise, reputation damage

**Description:**
If password field is logged anywhere (error logs, debug logs, request logs),
passwords will be exposed in plain text. Critical security vulnerability.

**Mitigation Strategy:**

**Prevention:**
- Audit all logging statements in authentication flow
- Use separate logger with password field exclusion
- Code review checklist: No logging of `password`, `token`, `secret` fields
- Configure log sanitization middleware

**Detection:**
- Unit test: Trigger error and verify logs don't contain password
- Code search: grep -r "console.log.*password" src/
- Security audit: Review all log statements before merge

**Recovery:**
- N/A (prevention critical)

**Concrete Actions:**
1. Add log sanitization middleware that redacts sensitive fields
2. Audit all logger calls in src/services/auth/
3. Add test: "error logs do not contain password field"
4. Document in docs/standards.md: Never log passwords

**Phase:** During Implementation
**Effort:** Moderate (2 hours)
**Validation:** Security test must pass before merge

---

## High-Risk Areas (Score ≥6)

### Risk 2: SQL injection (Score: 6)
[Detailed mitigation as shown in previous example]

### Risk 3: N+1 query (Score: 6)
[Detailed mitigation as shown in previous example]

### Risk 4: No rate limiting (Score: 6)
[Detailed mitigation as shown in previous example]

---

## Test Prioritization

### P0 (Critical) - Must Have Before Merge

**Security Tests:**
1. Password not logged in error scenarios
   - Test: tests/security/logging.test.ts
   - Scenario: Trigger auth error, verify logs
   - Expected: Password field redacted or absent

2. SQL injection attempts rejected
   - Test: tests/security/injection.test.ts
   - Scenario: POST with SQL in email field
   - Expected: 400 error, no database impact

**Data Tests:**
3. Duplicate email race condition handled
   - Test: tests/integration/signup.test.ts
   - Scenario: Concurrent signups with same email
   - Expected: One succeeds, others get 409

### P1 (High) - Should Have Before Merge

**Performance Tests:**
4. N+1 query not present in user listing
   - Test: tests/performance/listing.test.ts
   - Scenario: GET /api/users with 100+ users
   - Expected: Max 3 queries logged

**Security Tests:**
5. Rate limiting prevents abuse
   - Test: tests/security/rate-limit.test.ts
   - Scenario: 6+ signup attempts in 1 minute
   - Expected: 429 Too Many Requests after 5

### P2 (Medium) - Nice to Have

[Additional tests for medium-risk areas]

---

## Quality Gate Impact

**Current Risk Score Distribution:**
- Critical (≥7): 1 risk
- High (6): 3 risks
- Medium (3-5): 4 risks
- Low (1-2): 2 risks

**Quality Gate Prediction:**

**If all high-risk items mitigated and tested:**
→ **PASS** (no remaining critical risks)

**If high-risk items not fully addressed:**
→ **CONCERNS** (4 high-risk items require mitigation plans)

**If critical risk not mitigated:**
→ **FAIL** (password logging risk is critical security issue)

**Recommendation:**
Address critical risk (password logging) during implementation.
Test high-risk items (SQL injection, N+1 query, rate limiting).
Quality gate should be PASS with all mitigations in place.

---

## Implementation Guidance

**Before Starting Implementation:**
1. Review this risk profile with team
2. Confirm mitigation strategies acceptable
3. Add high-risk areas to implementation notes

**During Implementation:**
4. Address critical risk first (password logging)
5. Implement mitigations for high-risk items
6. Write P0/P1 tests as you implement

**Before Marking Ready for Review:**
7. Verify all P0 tests passing
8. Verify all high-risk mitigations implemented
9. Run security audit checklist

**During Quality Review:**
10. Quality skill will reference this risk profile
11. Gate decision will consider risk mitigation
12. Unmitigated high risks will trigger CONCERNS

---

## Risk-Test Mapping

| Risk | Score | Test(s) | Priority | Status |
|------|-------|---------|----------|--------|
| Plain text password | 9 | logging.test.ts | P0 | Not Implemented |
| SQL injection | 6 | injection.test.ts | P0 | Not Implemented |
| N+1 query | 6 | listing.test.ts | P1 | Not Implemented |
| Rate limiting | 6 | rate-limit.test.ts | P1 | Not Implemented |
| Duplicate email | 4 | signup.test.ts | P1 | Not Implemented |
| Email service failure | 4 | email-resilience.test.ts | P2 | Not Implemented |

---

## Version

**Risk Profile Version:** 1.0
**Template Version:** 1.0
**Assessment Date:** 2025-10-28
**Reassess If:** Requirements change, new dependencies added, critical risk discovered during implementation
```

**Halt Conditions:**
- Template missing
- File write fails

### Step 6: Present Summary to User

**Actions:**

1. Generate concise summary:

   ```markdown
   ## Risk Profile Complete

   **Task:** User Signup Implementation
   **File:** .claude/quality/assessments/task-006-risk-20251028.md

   ---

   ### Risk Summary

   **Total Risks:** 10 identified
   - 🔴 Critical (≥7): 1 risk
   - 🟠 High (6): 3 risks
   - 🟡 Medium (3-5): 4 risks
   - 🟢 Low (1-2): 2 risks

   ---

   ### Critical Risk (Must Address)

   **Plain text password in logs (Score: 9)**
   - Probability: High (common mistake)
   - Impact: Critical (compliance violation, breach)
   - Mitigation: Log sanitization middleware, audit all logging
   - Effort: 2 hours

   ---

   ### High-Risk Areas (Score ≥6)

   1. **SQL injection** (Score: 6)
      - Mitigation: Prisma ORM only, Zod validation, security tests

   2. **N+1 query on user listing** (Score: 6)
      - Mitigation: Eager loading, pagination, performance test

   3. **No rate limiting on signup** (Score: 6)
      - Mitigation: express-rate-limit at 5 req/min

   ---

   ### Test Priorities

   **P0 (Critical) - Must Have:**
   - Password not logged in error scenarios
   - SQL injection attempts rejected
   - Duplicate email race condition handled

   **P1 (High) - Should Have:**
   - N+1 query not present in listing
   - Rate limiting prevents abuse

   ---

   ### Quality Gate Impact

   **Predicted Status:** CONCERNS → PASS
   - With mitigations: PASS
   - Without mitigations: CONCERNS (4 high-risk areas)
   - If critical risk unaddressed: FAIL

   **Recommendation:**
   ✅ Address critical risk (password logging) immediately
   ✅ Implement high-risk mitigations during development
   ✅ Write P0/P1 tests to validate
   ✅ Expected gate: PASS with all mitigations

   ---

   ### Next Steps

   1. Review full risk profile file
   2. Confirm mitigation strategies acceptable
   3. Begin implementation with risk awareness
   4. Reference this profile during quality review

   **Ready to proceed with implementation? (yes/no)**
   ```

2. Wait for user acknowledgment

**Output:**
- Summary presented
- User awareness of risks
- Clear path forward

**Halt Conditions:**
- None (assessment complete)

## Completion Criteria

Risk profile assessment is complete when:

- [ ] All potential risks identified (10-20 typical)
- [ ] All risks scored with P×I methodology
- [ ] Mitigation strategies developed for high risks
- [ ] Test scenarios prioritized by risk
- [ ] Risk profile file created
- [ ] Summary presented to user

## Usage Examples

### Example 1: Pre-Implementation (Recommended)

**User:** "Assess risks for .claude/tasks/task-006-user-signup.md before I start implementing"

**Risk Profile Skill:**
1. Loads task spec (status: Approved)
2. Identifies 10 potential risks across categories
3. Scores each risk (P×I)
4. Finds 1 critical risk (score 9), 3 high risks (score 6)
5. Develops mitigation strategies
6. Prioritizes tests: 3 P0, 2 P1
7. Generates risk profile file
8. Presents summary with critical risk highlighted

**Result:** Developer knows what to watch for before writing code

### Example 2: During Development

**User:** "Check risks for the payment integration I'm working on"

**Risk Profile Skill:**
1. Loads task spec (status: InProgress)
2. Identifies 15 risks (external API, money handling, compliance)
3. Scores: 2 critical (scores 9), 4 high (score 6-8)
4. Critical: PCI compliance violation, transaction rollback failure
5. Develops mitigations: Use payment gateway SDK, implement idempotency
6. Prioritizes tests heavily toward P0 security and data integrity
7. Generates risk profile
8. Recommends halt until critical risks have mitigation plan

**Result:** Developer pauses to address critical risks properly

### Example 3: Post-Implementation (Quality Review)

**User:** "Include risk assessment in quality review for completed task"

**Risk Profile Skill:**
1. Loads task spec (status: Review)
2. Assesses what was implemented
3. Identifies 8 risks, scores each
4. Checks if high-risk areas have tests
5. Finds: N+1 query risk not tested (score 6)
6. Updates quality gate prediction: CONCERNS
7. Generates risk profile with recommendations
8. Integration with quality review: Gate includes risk findings

**Result:** Quality gate references actual risk assessment

## Integration with Other Skills

### Before This Skill

**Pre-implementation (Recommended):**
- Planning skill created task specification
- Task status: "Approved"
- Ready to start implementation

**During development:**
- Implementation skill working on tasks
- Want to validate risk mitigation

**Post-implementation:**
- Implementation complete, status: "Review"
- Quality review skill orchestrates risk profile

### After This Skill

**Pre-implementation:**
- Developer aware of risks before coding
- Mitigation strategies inform implementation
- Test priorities guide test writing

**During development:**
- Developer checks if mitigations in place
- Validates high-risk areas tested

**Post-implementation:**
- Quality review skill references risk profile
- Quality gate decision considers risk mitigation
- Unmitigated high risks trigger CONCERNS/FAIL

### Handoff to Test Design Skill

```markdown
Risk profile complete with test priorities:
- File: .claude/quality/assessments/task-006-risk-20251028.md
- P0 tests: 3 identified (security, data integrity)
- P1 tests: 2 identified (performance, security)

Next: Use test-design skill to create detailed test scenarios
based on risk priorities.
```

### Handoff to Quality Gate Skill

```markdown
Risk profile informs quality gate decision:
- Critical risks (≥7): 1 found, mitigation required
- High risks (≥6): 3 found, tests required
- Gate prediction: CONCERNS → PASS (with mitigations)

Quality gate skill will verify:
- Critical risks addressed
- High-risk areas tested
- Mitigation strategies implemented
```

## Best Practices

1. **Assess Early:**
   - Best after task spec creation, before implementation
   - Prevents rework due to unidentified risks
   - Informs implementation approach

2. **Be Honest About Probability:**
   - Don't assume "won't happen to me"
   - Consider team experience with similar work
   - Factor in complexity and unknowns

3. **Consider Real Impact:**
   - Think beyond "it might break"
   - Consider: Data loss? Security breach? Downtime? User impact?
   - Business and compliance implications

4. **Actionable Mitigations:**
   - Specific, not vague ("use Prisma ORM" not "be careful")
   - Assignable to phase (implementation, testing, deployment)
   - Effort-estimated for planning

5. **Risk-Driven Testing:**
   - High risks = high-priority tests
   - Critical risks = must-have tests
   - Low risks = nice-to-have tests

6. **Continuous Reassessment:**
   - Reassess if requirements change
   - Reassess if new dependencies added
   - Reassess if critical risk discovered during implementation

## Common Pitfalls to Avoid

1. **Underestimating Probability:**
   - ❌ Don't: "N+1 queries won't happen, I'm careful"
   - ✅ Do: "N+1 queries are common with ORMs (P:3), need explicit prevention"

2. **Underestimating Impact:**
   - ❌ Don't: "SQL injection is just a bug"
   - ✅ Do: "SQL injection is critical (I:3) - data breach, compliance violation"

3. **Vague Mitigations:**
   - ❌ Don't: "Be careful with SQL"
   - ✅ Do: "Use Prisma ORM exclusively, no raw SQL, add injection tests"

4. **Ignoring Low-Probability High-Impact:**
   - ❌ Don't: Skip risks with P:1, I:3 (score 3)
   - ✅ Do: Document mitigation even for unlikely but critical risks

5. **Not Linking to Tests:**
   - ❌ Don't: Identify risks without test plan
   - ✅ Do: Every high risk → specific test scenario

6. **Forgetting Operational Risks:**
   - ❌ Don't: Only focus on code risks
   - ✅ Do: Consider deployment, monitoring, rollback risks

## Configuration

### In `.claude/config.yaml`

```yaml
quality:
  # Risk score threshold for quality gate impact
  riskScoreThreshold: 6  # Default: 6
  # ≥9 → FAIL
  # ≥6 → CONCERNS
  # <6 → No auto-impact

  # Where risk profiles are stored
  qualityLocation: .claude/quality

  # Risk assessment enabled
  checks:
    riskAssessment: true
```

### In `.claude/templates/risk-profile.md`

Template for risk profile output (to be created if doesn't exist)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial risk profile skill based on BMAD QA risk assessment pattern |

---

**End of Risk Profile Skill**
