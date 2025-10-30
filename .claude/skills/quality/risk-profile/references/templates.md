# Risk Profile Templates and Output Formats

All output formats, examples, and templates for the risk-profile skill.

---

## Step 0: Load Configuration and Task Context Output

**Complete Output Format:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Risk threshold: 6 (≥6 triggers CONCERNS gate)
✓ Task specification loaded: task-007 - Implement User Authentication System
✓ Assessment mode: pre-implementation
✓ Implementation scope: 8 tasks, 4 systems (auth service, user DB, session store, API gateway), new OAuth2 integration
```

**Successful Example:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Risk threshold: 6 (≥6 triggers CONCERNS gate)
✓ Quality location: .claude/quality
✓ Task specification loaded: task-012 - Add Payment Processing Integration
✓ Assessment mode: pre-implementation
✓ Task status: Approved (ready for implementation)
✓ Implementation scope: 12 tasks, 3 systems (payment API, order service, notification service), Stripe API integration
✓ Complexity indicators: High - external payment API, sensitive financial data, PCI compliance requirements
✓ Duration: 125ms
```

**Error Case Example:**
```
✗ Configuration file not found: .claude/config.yaml
✗ Cannot determine risk threshold (using default: 6)
! Halting - Configuration required for risk assessment
```

---

## Step 1: Identify Risk Areas Output

**Complete Output Format:**
```
✓ Risk areas identified: 15 potential risks
✓ Categories: Technical [4], Security [5], Performance [2], Data [2], Business [1], Operational [1]
✓ Complexity indicators: 8 tasks, 4 systems, new OAuth2 integration with unfamiliar provider
✓ Duration: 245ms
```

**Detailed Example with Risk Breakdown:**
```
✓ Risk areas identified: 18 potential risks
✓ Categories:
  - Technical [5]: OAuth2 flow complexity, token refresh mechanism, API rate limits, CORS configuration, session timeout handling
  - Security [6]: OAuth token leakage, session hijacking, CSRF attacks, insufficient scope validation, password storage (if fallback), insecure redirect URIs
  - Performance [2]: OAuth handshake latency, database connection pooling under load
  - Data [3]: User data inconsistency during auth flow, session data race conditions, incomplete transaction rollback
  - Business [1]: User lockout during auth failures impacts UX
  - Operational [1]: OAuth provider outage with no fallback mechanism
✓ Complexity indicators:
  - Task count: 8 tasks (moderate complexity)
  - Systems involved: 4 (auth service, user DB, session store, API gateway) - high integration risk
  - Pattern type: New OAuth2 integration (unfamiliar territory - high unknowns)
  - External dependencies: 1 (OAuth provider API) - external failure risk
  - Data sensitivity: High (authentication credentials, user sessions)
✓ Acceptance criteria signals:
  - Security requirements mentioned: Yes (OAuth2, secure token storage)
  - Performance targets: Yes (auth flow <500ms)
  - Data migration needed: No
  - User-facing changes: Yes (login/logout UI)
✓ Duration: 312ms
```

---

## Step 2: Score Each Risk (P×I) Output

**Complete Output Format:**
```
✓ Risks scored: 15 risks evaluated
✓ Score distribution:
  ├─ Critical (≥7): 2
  ├─ High (6): 4
  ├─ Medium (3-5): 6
  └─ Low (1-2): 3
✓ Highest risk score: 9
✓ Quality gate impact: CONCERNS (critical risk requires mitigation + testing)
✓ Duration: 178ms
```

**Detailed Scoring Example:**
```
✓ Risks scored: 18 risks evaluated using P×I methodology

✓ Score distribution:
  ├─ Critical (≥7): 3 risks
  │   └─ Scores: 9, 9, 8
  ├─ High (6): 5 risks
  ├─ Medium (3-5): 7 risks
  └─ Low (1-2): 3 risks

✓ Highest risk score: 9 (P:3 × I:3)

✓ Critical risks requiring immediate mitigation:
  1. OAuth token leakage via XSS (Score 9: P:3 × I:3)
     - Probability 3 (High): Complex token handling, easy to mishandle in client-side code
     - Impact 3 (High): Complete account compromise, data breach, regulatory violation

  2. Session hijacking via insecure cookies (Score 9: P:3 × I:3)
     - Probability 3 (High): Cookie security often misconfigured in new implementations
     - Impact 3 (High): Account takeover, unauthorized access to sensitive data

  3. Insufficient OAuth scope validation (Score 8: P:2 × I:4... wait, max is 3×3=9, recalculating: P:3 × I:3 = 9, but calling it 8 as slightly lower impact)
     Actually let me fix: Score 8 would be impossible with P×I (no combination gives 8)
     Let me use: P:2 × I:3 = 6 or P:3 × I:2 = 6, not 8. Score 8 doesn't exist in P×I!

Let me recalculate properly:
  3. Insufficient OAuth scope validation (Score 6: P:2 × I:3)
     - Probability 2 (Medium): Some complexity in scope validation, but patterns exist
     - Impact 3 (High): Over-privileged access, potential data exposure

✓ Quality gate impact: CONCERNS
✓ Reasoning: 2 critical risks (score 9) trigger CONCERNS gate. Mitigation plan + P0 tests required before merge.

✓ Predicted gate status: CONCERNS → PASS
✓ Path to PASS:
  - Mitigate 2 critical risks (score 9) during implementation
  - Write P0 tests to validate mitigation effectiveness
  - Address 5 high risks (score 6) with mitigation + testing
  - Document all mitigations in risk profile

✓ Duration: 267ms
```

**Risk Scoring Details - Complete Examples:**

**Example 1: OAuth Token Leakage via XSS (Score 9)**
- Category: Security
- Risk: OAuth access tokens stored in localStorage vulnerable to XSS attacks
- Probability: 3 (High - 70% chance)
  - Reasoning: Token storage in client-side JavaScript is complex. Many implementations default to localStorage for convenience. XSS vulnerabilities are common in web apps (OWASP Top 10). Team has limited OAuth experience.
- Impact: 3 (High)
  - Reasoning: Complete account compromise. Attacker gains full access to user account. Can read sensitive data, perform actions as user. Regulatory violation (GDPR, PCI if payment data). Major effort to fix (need to change token storage architecture, update all clients, force re-authentication). Potential class-action lawsuit.
- Risk Score: 3 × 3 = 9 (Critical)

**Example 2: API Rate Limiting Issues (Score 4)**
- Category: Performance
- Risk: OAuth provider rate limits API calls, causing intermittent auth failures
- Probability: 2 (Medium - 40% chance)
  - Reasoning: OAuth provider has rate limits (confirmed in docs). We'll have traffic spikes during peak hours. No current rate limit handling in design. However, we can implement backoff/retry.
- Impact: 2 (Medium)
  - Reasoning: Intermittent login failures during peaks. Users see error messages, need to retry. Degraded UX, frustrated users. Moderate effort to fix (add rate limit handling, implement backoff). No data loss or security impact.
- Risk Score: 2 × 2 = 4 (Medium)

**Example 3: Session Timeout Handling (Score 2)**
- Category: Technical
- Risk: Session expiry edge cases not handled gracefully, requiring page refresh
- Probability: 2 (Medium - 30% chance)
  - Reasoning: Session timeout logic is moderately complex. Edge cases exist (tab sleep, network interruption). However, established patterns available.
- Impact: 1 (Low)
  - Reasoning: Minor UX inconvenience. User sees error, needs to refresh or re-login. Easy fix (add timeout detection, auto-refresh). No data loss or security impact.
- Risk Score: 2 × 1 = 2 (Low)

---

## Step 3: Develop Mitigation Strategies Output

**Complete Output Format:**
```
✓ Mitigation strategies developed: 6 strategies (for all high-risk items)
✓ Critical risks mitigated: 2/2
✓ High risks mitigated: 4/4
✓ Total mitigation effort: ~14-18 hours
✓ Phases: Implementation [4], Testing [3], Deployment [1], Monitoring [2]
✓ Duration: 198ms
```

**Detailed Mitigation Example:**
```
✓ Mitigation strategies developed: 11 strategies

✓ Critical risks (score ≥7):
  ├─ Risk: OAuth token leakage via XSS (Score 9)
  │   └─ Mitigation: Store tokens in httpOnly secure cookies, not localStorage
  │       ├─ Prevention: Use httpOnly cookies for token storage (immune to XSS)
  │       ├─ Detection: Security audit, penetration testing of auth flow
  │       ├─ Recovery: Force token refresh, revoke compromised tokens
  │       ├─ Phase: Implementation (architectural decision)
  │       ├─ Effort: Moderate (2-3 hours - implement cookie-based storage)
  │       └─ Actions:
  │           - Implement token storage in httpOnly cookies (server-side set)
  │           - Never expose tokens to client JavaScript
  │           - Add CSP headers to prevent inline scripts
  │           - Write tests: XSS attack simulation, token not accessible from JS
  │
  └─ Risk: Session hijacking via insecure cookies (Score 9)
      └─ Mitigation: Use httpOnly + secure + SameSite=Strict cookies
          ├─ Prevention: Cookie security flags prevent theft/CSRF
          ├─ Detection: Monitor for session anomalies (location, device changes)
          ├─ Recovery: Force re-authentication on suspicious activity
          ├─ Phase: Implementation + Monitoring
          ├─ Effort: Minimal (1 hour implementation + 2 hours monitoring setup)
          └─ Actions:
              - Set cookie flags: httpOnly, secure, SameSite=Strict
              - Implement session fingerprinting (IP, user agent)
              - Add monitoring alert on session anomaly
              - Write tests: Cookie flags validation, session hijack simulation

✓ High risks (score 6):
  ├─ Risk: Insufficient OAuth scope validation (Score 6)
  │   └─ Mitigation: Validate scope on every API request with allowlist
  │       ├─ Prevention: Strict scope validation prevents over-privileged access
  │       ├─ Detection: Log all scope validation failures
  │       ├─ Recovery: Reject request, require re-authentication with correct scope
  │       ├─ Phase: Implementation + Monitoring
  │       ├─ Effort: Moderate (3-4 hours)
  │       └─ Actions: [detailed actions...]
  │
  ├─ [3 more high risks with similar detail...]

✓ Total mitigation effort estimate:
  ├─ Critical risks: ~4-5 hours (2 risks)
  ├─ High risks: ~10-13 hours (5 risks)
  └─ Total: ~14-18 hours

✓ Phase breakdown:
  ├─ Implementation: 6 strategies (architectural decisions, validation logic)
  ├─ Testing: 5 strategies (security tests, integration tests, load tests)
  ├─ Deployment: 1 strategy (feature flag for gradual rollout)
  └─ Monitoring: 3 strategies (session anomaly detection, scope validation failures, auth error rates)

✓ Next steps:
  1. Review mitigation strategies with team
  2. Confirm effort estimates and phase assignments
  3. Integrate mitigations into implementation plan
  4. Create test specifications for P0/P1 scenarios

✓ Duration: 289ms
```

---

## Step 4: Prioritize Test Scenarios Output

**Complete Output Format:**
```
✓ Test scenarios prioritized: 12 scenarios
✓ P0 (Critical) tests: 4 (must have before merge)
✓ P1 (High) tests: 5 (should have before merge)
✓ P2 (Medium) tests: 3 (nice to have)
✓ Risk-test mapping: 15 risks mapped to 12 test scenarios
✓ Duration: 145ms
```

**Detailed Test Prioritization Example:**
```
✓ Test scenarios prioritized: 18 test scenarios across 3 priority levels

✓ P0 (Critical) - Must Have Before Merge: 6 tests
  ├─ T1: XSS token theft simulation
  │   ├─ Risk: OAuth token leakage via XSS (Score 9)
  │   ├─ Level: Integration + Security
  │   ├─ Scenario: Inject XSS payload, verify tokens NOT accessible from JavaScript
  │   ├─ Expected: Token stored in httpOnly cookie, XSS cannot steal token
  │   └─ Test file: tests/security/auth-xss-protection.test.ts
  │
  ├─ T2: Session hijacking prevention
  │   ├─ Risk: Session hijacking via insecure cookies (Score 9)
  │   ├─ Level: Integration + Security
  │   ├─ Scenario: Attempt to reuse session cookie from different IP/device
  │   ├─ Expected: Session invalidated, user prompted to re-authenticate
  │   └─ Test file: tests/security/session-hijack-detection.test.ts
  │
  ├─ T3: Cookie security flags validation
  │   ├─ Risk: Session hijacking via insecure cookies (Score 9)
  │   ├─ Level: Unit
  │   ├─ Scenario: Inspect cookies set by auth service
  │   ├─ Expected: httpOnly=true, secure=true, SameSite=Strict
  │   └─ Test file: tests/unit/auth-cookie-security.test.ts
  │
  ├─ T4: OAuth scope over-privilege prevention
  │   ├─ Risk: Insufficient OAuth scope validation (Score 6)
  │   ├─ Level: Integration
  │   ├─ Scenario: Request API with insufficient scope, verify rejection
  │   ├─ Expected: 403 Forbidden, scope validation failure logged
  │   └─ Test file: tests/integration/scope-validation.test.ts
  │
  ├─ T5: OAuth provider outage fallback
  │   ├─ Risk: OAuth provider outage with no fallback (Score 6)
  │   ├─ Level: Integration
  │   ├─ Scenario: Simulate OAuth provider downtime, verify graceful degradation
  │   ├─ Expected: User sees maintenance message, existing sessions remain valid
  │   └─ Test file: tests/integration/auth-provider-failure.test.ts
  │
  └─ T6: CSRF protection validation
      ├─ Risk: CSRF attacks on auth endpoints (Score 6)
      ├─ Level: Integration + Security
      ├─ Scenario: Submit auth request without CSRF token
      ├─ Expected: Request rejected with 403
      └─ Test file: tests/security/csrf-protection.test.ts

✓ P1 (High) - Should Have Before Merge: 7 tests
  ├─ T7: OAuth token refresh flow
  │   ├─ Risk: Token refresh mechanism failure (Score 6)
  │   ├─ Level: Integration
  │   ├─ Scenario: Trigger token expiry, verify automatic refresh
  │   ├─ Expected: Token refreshed transparently, no user interruption
  │   └─ Test file: tests/integration/token-refresh.test.ts
  │
  ├─ T8: API rate limit handling
  │   ├─ Risk: API rate limiting issues (Score 4)
  │   ├─ Level: Integration
  │   ├─ Scenario: Exceed OAuth provider rate limit, verify backoff/retry
  │   ├─ Expected: Exponential backoff, eventual success, no data loss
  │   └─ Test file: tests/integration/rate-limit-backoff.test.ts
  │
  ├─ [5 more P1 tests...]

✓ P2 (Medium) - Nice to Have: 5 tests
  ├─ T13: Session timeout edge cases
  │   ├─ Risk: Session timeout handling (Score 2)
  │   ├─ Level: E2E
  │   ├─ Scenario: Browser tab sleep, network interruption during session
  │   ├─ Expected: Graceful timeout detection, user prompted to re-auth
  │   └─ Test file: tests/e2e/session-timeout.test.ts
  │
  ├─ [4 more P2 tests...]

✓ Risk-to-Test Mapping:
  ├─ 18 risks identified
  ├─ 18 tests created (1:1 mapping for high risks, 1:many for lower risks)
  ├─ Coverage: 100% of critical/high risks, 85% of medium risks, 60% of low risks
  └─ Gap: Low-risk edge cases (acceptable - standard testing sufficient)

✓ Test coverage summary:
  ├─ Security tests: 8 scenarios (critical focus on auth/session security)
  ├─ Integration tests: 6 scenarios (OAuth flow, API interactions)
  ├─ Unit tests: 2 scenarios (cookie validation, scope parsing)
  └─ E2E tests: 2 scenarios (full auth flow, timeout handling)

✓ Estimated test writing effort: ~18-22 hours
  ├─ P0 tests: ~8-10 hours (6 complex security tests)
  ├─ P1 tests: ~7-9 hours (7 integration tests)
  └─ P2 tests: ~3-3 hours (5 simpler tests)

✓ Duration: 234ms
```

---

## Step 5: Generate Risk Profile Report Output

**Complete Output Format:**
```
✓ Risk profile report generated
✓ Output: .claude/quality/assessments/task-007-risk-20251030.md
✓ Total risks documented: 15
✓ Critical/high risks detailed: 6
✓ Test priorities documented: P0 [4], P1 [5], P2 [3]
✓ Quality gate impact: CONCERNS (2 critical risks require mitigation)
✓ Duration: 89ms
```

**Example with Full Path:**
```
✓ Risk profile report generated successfully
✓ Output file: .claude/quality/assessments/task-012-risk-20251030.md
✓ Report structure:
  ├─ Risk Summary (total, distribution, highest score)
  ├─ Risk Matrix (all 18 risks sorted by score)
  ├─ Critical Risks Detail (2 risks with full mitigation plans)
  ├─ High Risks Detail (5 risks with mitigation summaries)
  ├─ Test Prioritization (18 tests mapped to risks)
  ├─ Mitigation Roadmap (timeline, phase assignments, effort)
  └─ Quality Gate Impact (prediction, reasoning, path to PASS)
✓ Total risks documented: 18
✓ Critical risks detailed: 2 (OAuth token leakage, session hijacking)
✓ High risks detailed: 5 (scope validation, CSRF, provider outage, rate limits, token refresh)
✓ Medium/low risks summarized: 11 (in risk matrix)
✓ Test priorities: P0 [6], P1 [7], P2 [5]
✓ Mitigation effort estimate: ~14-18 hours
✓ Quality gate impact: CONCERNS → PASS (after mitigation)
✓ File size: 3,247 bytes
✓ Duration: 112ms
```

---

## Step 6: Present Summary to User Output

**Complete User-Facing Summary:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Risk Profile Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-012 - Implement Payment Processing Integration
Date: 2025-10-30
Mode: pre-implementation

📊 Risk Summary

Total Risks: 18 identified
- 🔴 Critical (≥7): 2
- 🟠 High (6): 5
- 🟡 Medium (3-5): 8
- 🟢 Low (1-2): 3

🚨 CRITICAL RISKS - Immediate Attention Required

1. OAuth Token Leakage via XSS (Score: 9, P:3 × I:3)
   Category: Security

   Risk: OAuth access tokens stored in localStorage vulnerable to XSS attacks

   Impact: Complete account compromise, full user data access, regulatory violation

   Mitigation:
   - Store tokens in httpOnly secure cookies (NOT localStorage)
   - Add CSP headers to prevent inline scripts
   - Never expose tokens to client JavaScript
   - Phase: Implementation (architectural decision)
   - Effort: Moderate (2-3 hours)

   Tests Required:
   - P0: XSS token theft simulation (verify tokens NOT accessible)
   - P0: Cookie security flags validation (httpOnly, secure, SameSite)

2. Session Hijacking via Insecure Cookies (Score: 9, P:3 × I:3)
   Category: Security

   Risk: Session cookies not properly secured, allowing session theft

   Impact: Account takeover, unauthorized access to sensitive data

   Mitigation:
   - Set cookie flags: httpOnly, secure, SameSite=Strict
   - Implement session fingerprinting (IP, user agent)
   - Add monitoring alert on session anomaly
   - Phase: Implementation + Monitoring
   - Effort: Minimal (1 hour + 2 hours monitoring)

   Tests Required:
   - P0: Session hijacking prevention test
   - P0: Cookie security flags validation

🎯 High-Risk Areas (Score ≥6)

3. Insufficient OAuth Scope Validation (Score: 6, P:2 × I:3)
   Security: Over-privileged access if scope not validated on each request
   Mitigation: Validate scope on every API request with strict allowlist
   Tests: P0 - Scope over-privilege prevention test

4. CSRF Attacks on Auth Endpoints (Score: 6, P:2 × I:3)
   Security: Authentication endpoints vulnerable to CSRF without token validation
   Mitigation: Implement CSRF token validation on all state-changing auth endpoints
   Tests: P0 - CSRF protection validation test

5. OAuth Provider Outage (Score: 6, P:2 × I:3)
   Operational: No fallback when OAuth provider unavailable
   Mitigation: Implement graceful degradation, maintain existing sessions during outage
   Tests: P0 - OAuth provider outage fallback test

6. API Rate Limiting Issues (Score: 6, P:2 × I:3)
   Performance: OAuth provider rate limits cause intermittent failures
   Mitigation: Implement exponential backoff and rate limit handling
   Tests: P1 - Rate limit handling with backoff test

7. Token Refresh Mechanism Failure (Score: 6, P:2 × I:3)
   Technical: Token refresh errors force unnecessary re-authentication
   Mitigation: Robust token refresh with retry logic and error handling
   Tests: P1 - Token refresh flow validation test

📋 Test Priorities

P0 (Critical) - Must Have Before Merge:
✓ XSS token theft simulation (T1)
✓ Session hijacking prevention (T2)
✓ Cookie security flags validation (T3)
✓ OAuth scope over-privilege prevention (T4)
✓ OAuth provider outage fallback (T5)
✓ CSRF protection validation (T6)

P1 (High) - Should Have Before Merge:
✓ OAuth token refresh flow (T7)
✓ API rate limit handling (T8)
✓ Password storage security (if fallback auth) (T9)
✓ Session data race condition handling (T10)
✓ Incomplete transaction rollback (T11)
✓ Auth handshake performance (<500ms target) (T12)
✓ CORS configuration validation (T13)

P2 (Medium) - Nice to Have:
✓ Session timeout edge cases (T14)
✓ Database connection pooling under load (T15)
✓ User lockout UX during auth failures (T16)
✓ Insecure redirect URI validation (T17)
✓ Malformed token handling (T18)

🚦 Quality Gate Impact

Predicted Status: CONCERNS → PASS (after mitigation)

Reasoning:
- 2 critical risks (score 9) trigger CONCERNS gate
- Must mitigate critical risks before merge
- Must write and pass all 6 P0 tests
- High risks (5 risks, score 6) require mitigation + testing

Path to PASS:
1. ✓ Implement httpOnly cookie token storage (addresses risks #1, #2)
2. ✓ Add cookie security flags (httpOnly, secure, SameSite)
3. ✓ Implement strict OAuth scope validation (addresses risk #3)
4. ✓ Add CSRF token validation (addresses risk #4)
5. ✓ Implement OAuth provider failover (addresses risk #5)
6. ✓ Write and pass all 6 P0 tests
7. ✓ Write and pass 7 P1 tests (high risks)
8. ✓ Document all mitigations in implementation

Estimated Effort:
- Mitigation implementation: ~14-18 hours
- P0/P1 test writing: ~15-19 hours
- Total: ~29-37 hours

📄 Full Report: .claude/quality/assessments/task-012-risk-20251030.md

💡 Next Steps:
1. Review full risk profile report
2. Confirm mitigation strategies acceptable
3. Address critical risks during implementation
4. Write P0/P1 tests to validate
5. Reference this profile during quality review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Shorter Summary Example (Fewer Risks):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Risk Profile Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-005 - Add User Profile Editing Feature
Date: 2025-10-30
Mode: pre-implementation

📊 Risk Summary

Total Risks: 8 identified
- 🔴 Critical (≥7): 0
- 🟠 High (6): 2
- 🟡 Medium (3-5): 4
- 🟢 Low (1-2): 2

🎯 High-Risk Areas (Score ≥6)

1. Input Validation Bypass (Score: 6, P:2 × I:3)
   Security: Insufficient input validation could allow XSS or injection attacks
   Mitigation: Use validation library (Zod), escape all output, add CSP headers
   Tests: P0 - XSS injection attempt, SQL injection attempt

2. Profile Update Race Conditions (Score: 6, P:2 × I:3)
   Data: Concurrent profile updates could cause data inconsistency
   Mitigation: Implement optimistic locking with version field, use transactions
   Tests: P0 - Concurrent update simulation

📋 Test Priorities

P0 (Critical) - Must Have Before Merge:
✓ XSS injection validation (T1)
✓ SQL injection prevention (T2)
✓ Concurrent update handling (T3)

P1 (High) - Should Have Before Merge:
✓ Profile image upload size validation (T4)
✓ Email uniqueness validation (T5)

P2 (Medium) - Nice to Have:
✓ Profile update performance (T6)

🚦 Quality Gate Impact

Predicted Status: PASS (with mitigation)

Reasoning:
- No critical risks (score ≥7)
- 2 high risks (score 6) require mitigation + testing
- All high risks have clear mitigation strategies
- P0 tests will validate mitigation effectiveness

Path to PASS:
1. ✓ Implement input validation with Zod library
2. ✓ Add optimistic locking for profile updates
3. ✓ Write and pass 3 P0 tests
4. ✓ Write and pass 2 P1 tests

Estimated Effort:
- Mitigation implementation: ~6-8 hours
- P0/P1 test writing: ~7-9 hours
- Total: ~13-17 hours

📄 Full Report: .claude/quality/assessments/task-005-risk-20251030.md

💡 Next Steps:
1. Review full risk profile report
2. Implement input validation and optimistic locking
3. Write P0/P1 tests to validate
4. Proceed with implementation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Complete Risk Profile Report Template

**File:** `.claude/quality/assessments/task-012-risk-20251030.md`

```markdown
---
task_id: task-012
task_title: Implement Payment Processing Integration
assessment_date: 2025-10-30
assessment_mode: pre-implementation
assessor: BMAD Risk Profile Skill v2.0
total_risks: 18
critical_risks: 2
high_risks: 5
medium_risks: 8
low_risks: 3
highest_risk_score: 9
quality_gate_impact: CONCERNS
p0_tests: 6
p1_tests: 7
p2_tests: 5
---

# Risk Profile: task-012 - Implement Payment Processing Integration

**Assessment Date:** 2025-10-30
**Assessment Mode:** Pre-implementation
**Task Status:** Approved (ready for implementation)

---

## Executive Summary

This risk assessment identified **18 potential risks** across 6 categories. **2 critical risks** (score 9) and **5 high risks** (score 6) require immediate mitigation before or during implementation. The presence of critical risks triggers a **CONCERNS** quality gate status, requiring mitigation plan and P0 test validation before merge.

**Key Risk Areas:**
- **Security (highest concern):** OAuth token handling, session security, CSRF protection, scope validation
- **Technical:** Token refresh mechanism, CORS configuration, session timeout handling
- **Performance:** OAuth handshake latency, API rate limits
- **Operational:** OAuth provider outage with no fallback

**Recommended Action:** Implement all critical risk mitigations during development (token storage in httpOnly cookies, session security flags, scope validation, CSRF protection). Write and pass 6 P0 tests before requesting code review.

---

## Risk Matrix

All risks sorted by score (highest to lowest):

| # | Category | Risk | P | I | Score | Mitigation |
|---|----------|------|---|---|-------|------------|
| 1 | Security | OAuth token leakage via XSS | 3 | 3 | **9** | Store in httpOnly cookies, never in localStorage |
| 2 | Security | Session hijacking via insecure cookies | 3 | 3 | **9** | Set httpOnly, secure, SameSite=Strict flags |
| 3 | Security | Insufficient OAuth scope validation | 2 | 3 | **6** | Validate scope on every API request with allowlist |
| 4 | Security | CSRF attacks on auth endpoints | 2 | 3 | **6** | Implement CSRF token validation on state-changing endpoints |
| 5 | Security | Password storage (if fallback auth) | 2 | 3 | **6** | Use bcrypt/argon2, never plain text or weak hashing |
| 6 | Operational | OAuth provider outage with no fallback | 2 | 3 | **6** | Graceful degradation, maintain existing sessions during outage |
| 7 | Performance | API rate limiting issues | 2 | 3 | **6** | Implement exponential backoff and rate limit handling |
| 8 | Technical | Token refresh mechanism failure | 2 | 3 | **6** | Robust refresh with retry logic and error handling |
| 9 | Performance | OAuth handshake latency | 2 | 2 | **4** | Optimize redirect flow, minimize round trips |
| 10 | Data | Profile data race conditions during auth | 2 | 2 | **4** | Use database transactions for auth-related updates |
| 11 | Data | Incomplete transaction rollback on auth error | 2 | 2 | **4** | Wrap auth operations in transactions with proper rollback |
| 12 | Technical | CORS configuration errors | 2 | 2 | **4** | Strict CORS policy, allowlist only trusted origins |
| 13 | Security | Insecure redirect URI validation | 2 | 2 | **4** | Validate redirect URIs against allowlist |
| 14 | Technical | OAuth flow complexity | 2 | 1 | **2** | Follow OAuth2 best practices, use well-tested library |
| 15 | Data | Session data inconsistency | 1 | 2 | **2** | Use atomic session updates |
| 16 | Technical | Session timeout handling edge cases | 2 | 1 | **2** | Graceful timeout detection, prompt for re-auth |
| 17 | Business | User lockout during auth failures | 1 | 2 | **2** | Clear error messages, support contact info |
| 18 | Performance | Database connection pooling under load | 1 | 2 | **2** | Configure connection pool size, monitor usage |

---

## Critical Risks (Score ≥7)

### Risk #1: OAuth Token Leakage via XSS (Score: 9)

**Category:** Security
**Probability:** 3 (High - 70% chance)
**Impact:** 3 (High)
**Risk Score:** 3 × 3 = 9 (Critical)

**Description:**
OAuth access tokens stored in browser localStorage are vulnerable to XSS attacks. If an attacker injects malicious JavaScript, they can read localStorage and steal tokens, gaining full access to user accounts.

**Why Probability is High:**
- Token storage in client-side JavaScript is complex
- Many OAuth implementations default to localStorage for convenience
- XSS vulnerabilities are common (OWASP Top 10 #3)
- Team has limited OAuth implementation experience
- High likelihood of choosing localStorage without considering XSS risk

**Why Impact is High:**
- Complete account compromise - attacker gains full user access
- Can read all user data, perform actions as user
- Regulatory violation (GDPR, PCI if payment data involved)
- Potential class-action lawsuit
- Major effort to fix - need to redesign token storage, update all clients, force re-authentication

**Mitigation Strategy:**

**Prevention:**
- Store OAuth tokens in httpOnly secure cookies (immune to XSS)
- Never store tokens in localStorage, sessionStorage, or accessible from JavaScript
- Set cookie flags: httpOnly=true, secure=true, SameSite=Strict
- Add Content-Security-Policy headers to prevent inline scripts
- Use CSRF tokens for additional protection

**Detection:**
- Security audit of token storage implementation
- Penetration testing specifically targeting XSS → token theft
- Monitor for suspicious token usage patterns

**Recovery:**
- Force token refresh for all users
- Revoke compromised tokens immediately
- Notify affected users of potential breach
- Implement additional security measures

**Implementation Actions:**
1. Configure auth service to set tokens in httpOnly cookies
2. Never expose tokens to client JavaScript
3. Add CSP headers: `script-src 'self'` to prevent inline scripts
4. Remove any localStorage/sessionStorage token handling code
5. Update client code to rely on cookies (sent automatically)

**Testing Requirements:**
- **P0 Test (T1):** XSS token theft simulation
  - Inject XSS payload attempting to read token
  - Verify token NOT accessible from JavaScript
  - Verify token stored in httpOnly cookie
  - Test file: `tests/security/auth-xss-protection.test.ts`

- **P0 Test (T3):** Cookie security flags validation
  - Inspect cookies set by auth service
  - Assert httpOnly=true, secure=true, SameSite=Strict
  - Test file: `tests/unit/auth-cookie-security.test.ts`

**Phase:** Implementation (architectural decision)
**Effort:** Moderate (2-3 hours - implement cookie-based storage, update clients)
**Priority:** P0 (must address before implementation begins)

---

### Risk #2: Session Hijacking via Insecure Cookies (Score: 9)

**Category:** Security
**Probability:** 3 (High - 65% chance)
**Impact:** 3 (High)
**Risk Score:** 3 × 3 = 9 (Critical)

**Description:**
Session cookies without proper security flags (httpOnly, secure, SameSite) are vulnerable to theft via XSS, network sniffing (if not HTTPS), or CSRF attacks. Stolen session cookies allow account takeover.

**Why Probability is High:**
- Cookie security often misconfigured in new implementations
- Developers may not know about all security flags
- Default cookie settings are often insecure
- Easy to forget SameSite flag (relatively new)
- High likelihood of missing at least one security flag

**Why Impact is High:**
- Complete account takeover - attacker uses stolen session
- Unauthorized access to all user data and actions
- Difficult to detect - attacker looks like legitimate user
- User has no way to prevent (unlike password which they control)
- Moderate-to-major effort to fix - need to invalidate all sessions, force re-authentication

**Mitigation Strategy:**

**Prevention:**
- Set all cookie security flags: httpOnly, secure, SameSite=Strict
- Implement session fingerprinting (IP address, User-Agent)
- Detect and block session anomalies (location/device change)
- Short session lifetime (1-2 hours) with auto-refresh

**Detection:**
- Monitor for session usage from multiple IPs/locations
- Alert on User-Agent change within same session
- Log all session authentication events

**Recovery:**
- Force re-authentication on suspicious activity
- Invalidate compromised session immediately
- Notify user of suspicious session activity

**Implementation Actions:**
1. Set cookie flags when creating session:
   ```typescript
   response.cookie('sessionId', sessionId, {
     httpOnly: true,      // Cannot be read by JavaScript
     secure: true,        // Only sent over HTTPS
     sameSite: 'strict',  // Only sent to same site (CSRF protection)
     maxAge: 2 * 60 * 60 * 1000  // 2 hours
   });
   ```

2. Implement session fingerprinting:
   - Store IP address and User-Agent when session created
   - Verify fingerprint on each request
   - Invalidate session if mismatch detected

3. Add monitoring for session anomalies:
   - Alert on IP address change (potential hijack)
   - Alert on User-Agent change (potential hijack)
   - Dashboard showing active sessions per user

**Testing Requirements:**
- **P0 Test (T2):** Session hijacking prevention
  - Create session from IP1/Device1
  - Attempt to use session from IP2/Device2
  - Verify session invalidated or re-auth required
  - Test file: `tests/security/session-hijack-detection.test.ts`

- **P0 Test (T3):** Cookie security flags validation
  - Inspect cookies set by auth service
  - Assert httpOnly=true, secure=true, SameSite=Strict
  - Test file: `tests/unit/auth-cookie-security.test.ts`

**Phase:** Implementation + Monitoring
**Effort:** Minimal implementation (1 hour), Moderate monitoring setup (2 hours)
**Priority:** P0 (must address before implementation begins)

---

## High Risks (Score 6)

### Risk #3: Insufficient OAuth Scope Validation (Score: 6)

**Description:** OAuth scope not validated on each API request, allowing over-privileged access
**Mitigation:** Validate scope on every request with strict allowlist
**Phase:** Implementation + Monitoring
**Effort:** Moderate (3-4 hours)
**Tests:** P0 (T4) - Scope over-privilege prevention

### Risk #4: CSRF Attacks on Auth Endpoints (Score: 6)

**Description:** Auth endpoints vulnerable to CSRF without token validation
**Mitigation:** Implement CSRF token validation on all state-changing endpoints
**Phase:** Implementation
**Effort:** Moderate (2-3 hours)
**Tests:** P0 (T6) - CSRF protection validation

### Risk #5: Password Storage if Fallback Auth (Score: 6)

**Description:** Weak password hashing or plain text storage
**Mitigation:** Use bcrypt or argon2 with appropriate cost factor
**Phase:** Implementation
**Effort:** Minimal (1 hour)
**Tests:** P1 (T9) - Password storage security audit

### Risk #6: OAuth Provider Outage (Score: 6)

**Description:** No fallback when OAuth provider is unavailable
**Mitigation:** Graceful degradation, maintain existing sessions during outage
**Phase:** Implementation + Deployment
**Effort:** Significant (5-6 hours)
**Tests:** P0 (T5) - Provider outage fallback

### Risk #7: API Rate Limiting Issues (Score: 6)

**Description:** OAuth provider rate limits cause intermittent auth failures
**Mitigation:** Implement exponential backoff and rate limit handling
**Phase:** Implementation
**Effort:** Moderate (3-4 hours)
**Tests:** P1 (T8) - Rate limit handling

*(Medium and low risks summarized in Risk Matrix above)*

---

## Test Prioritization

### P0 (Critical) - Must Have Before Merge: 6 tests

| ID | Test Scenario | Risk(s) Addressed | Test Level | File |
|----|--------------|------------------|-----------|------|
| T1 | XSS token theft simulation | #1 (Score 9) | Integration + Security | tests/security/auth-xss-protection.test.ts |
| T2 | Session hijacking prevention | #2 (Score 9) | Integration + Security | tests/security/session-hijack-detection.test.ts |
| T3 | Cookie security flags validation | #1, #2 (Score 9) | Unit | tests/unit/auth-cookie-security.test.ts |
| T4 | OAuth scope over-privilege prevention | #3 (Score 6) | Integration | tests/integration/scope-validation.test.ts |
| T5 | OAuth provider outage fallback | #6 (Score 6) | Integration | tests/integration/auth-provider-failure.test.ts |
| T6 | CSRF protection validation | #4 (Score 6) | Integration + Security | tests/security/csrf-protection.test.ts |

### P1 (High) - Should Have Before Merge: 7 tests

| ID | Test Scenario | Risk(s) Addressed | Test Level | File |
|----|--------------|------------------|-----------|------|
| T7 | OAuth token refresh flow | #8 (Score 6) | Integration | tests/integration/token-refresh.test.ts |
| T8 | API rate limit handling | #7 (Score 6) | Integration | tests/integration/rate-limit-backoff.test.ts |
| T9 | Password storage security | #5 (Score 6) | Unit + Security | tests/unit/password-hashing.test.ts |
| T10 | Session data race condition | #10 (Score 4) | Integration | tests/integration/session-race-condition.test.ts |
| T11 | Incomplete transaction rollback | #11 (Score 4) | Integration | tests/integration/auth-transaction-rollback.test.ts |
| T12 | Auth handshake performance | #9 (Score 4) | Performance | tests/performance/auth-latency.test.ts |
| T13 | CORS configuration validation | #12 (Score 4) | Integration | tests/integration/cors-validation.test.ts |

### P2 (Medium) - Nice to Have: 5 tests

| ID | Test Scenario | Risk(s) Addressed | Test Level | File |
|----|--------------|------------------|-----------|------|
| T14 | Session timeout edge cases | #16 (Score 2) | E2E | tests/e2e/session-timeout.test.ts |
| T15 | Database connection pooling | #18 (Score 2) | Performance | tests/performance/db-pool-load.test.ts |
| T16 | User lockout UX | #17 (Score 2) | E2E | tests/e2e/auth-failure-ux.test.ts |
| T17 | Insecure redirect URI | #13 (Score 4) | Security | tests/security/redirect-uri-validation.test.ts |
| T18 | Malformed token handling | #14 (Score 2) | Unit | tests/unit/malformed-token.test.ts |

---

## Mitigation Roadmap

### Implementation Phase (During Development)

**Critical Mitigations (Must Do):**
1. Store OAuth tokens in httpOnly cookies (addresses Risk #1)
2. Set cookie security flags: httpOnly, secure, SameSite (addresses Risk #2)
3. Implement OAuth scope validation on all requests (addresses Risk #3)
4. Add CSRF token validation (addresses Risk #4)

**High-Priority Mitigations:**
5. Implement graceful degradation for OAuth provider outage (addresses Risk #6)
6. Add exponential backoff for rate limit handling (addresses Risk #7)
7. Implement robust token refresh mechanism (addresses Risk #8)

**Estimated Effort:** 14-18 hours

### Testing Phase (Before Merge)

**P0 Tests (Must Pass):**
- T1-T6: All critical security tests

**P1 Tests (Should Pass):**
- T7-T13: Integration and performance tests

**Estimated Effort:** 15-19 hours

### Deployment Phase

**Actions:**
- Feature flag OAuth integration for gradual rollout (addresses Risk #6)
- Monitor auth error rates, session anomalies (addresses Risk #2)

### Monitoring Phase (Post-Deployment)

**Dashboards:**
- Auth success/failure rates
- Session anomaly detection (IP/device changes)
- OAuth provider uptime
- API rate limit hits

**Alerts:**
- Session hijacking attempts (>5 per hour)
- OAuth provider downtime (>1 minute)
- API rate limit errors (>10 per minute)
- Scope validation failures (>5 per hour)

---

## Quality Gate Impact

**Predicted Status:** CONCERNS → PASS (after mitigation)

**Current Assessment:**
- **2 critical risks** (score 9) trigger CONCERNS quality gate
- Cannot merge without addressing critical risks
- Mitigation plan + P0 tests required

**Path to PASS:**

1. ✓ **Implement Critical Mitigations:**
   - OAuth tokens in httpOnly cookies
   - Cookie security flags (httpOnly, secure, SameSite)
   - OAuth scope validation
   - CSRF token validation

2. ✓ **Write and Pass P0 Tests:**
   - All 6 P0 tests must pass
   - Validates mitigation effectiveness
   - Proves critical risks addressed

3. ✓ **Write and Pass P1 Tests:**
   - 7 P1 tests for high risks
   - Demonstrates comprehensive security

4. ✓ **Document Mitigations:**
   - Update implementation spec with security decisions
   - Document token storage architecture
   - Record CSRF protection approach

**Quality Gate Decision Criteria:**

- **PASS:** All critical risks mitigated, P0 tests pass, high risks have mitigation plans
- **CONCERNS:** Critical risks mitigated but P0 tests incomplete, or high risks not addressed
- **FAIL:** Critical risks not mitigated, no mitigation plan, P0 tests fail

**Estimated Timeline:**
- Mitigation implementation: 2-3 days
- P0/P1 test writing: 2-3 days
- Total: 4-6 days to achieve PASS

---

## Recommendations

1. **Start with Security:** Address critical security risks (#1, #2) on Day 1 before writing any auth code
2. **Security Review:** Request security team review of OAuth implementation plan before coding
3. **Test-Driven:** Write P0 tests first, then implement mitigations (TDD approach)
4. **Incremental Testing:** Test each mitigation independently before integration
5. **Peer Review:** Security-focused code review with at least 2 reviewers for auth code
6. **Penetration Test:** Consider hiring security firm for pen test before production deployment

---

## Appendix: Risk Categories

### Technical Risks (5)
OAuth flow complexity, token refresh, CORS, session timeout, OAuth handshake performance

### Security Risks (6)
OAuth token leakage, session hijacking, scope validation, CSRF, password storage, redirect URI validation

### Performance Risks (2)
OAuth handshake latency, API rate limits

### Data Risks (3)
Session data inconsistency, profile race conditions, incomplete transaction rollback

### Business Risks (1)
User lockout during auth failures

### Operational Risks (1)
OAuth provider outage with no fallback

---

*Risk assessment completed by BMAD Risk Profile Skill v2.0*
*Assessment Date: 2025-10-30*
*Next Review: After implementation or if requirements change*
```

---

## Risk Category Details

### Technical Risks

**Definition:** Implementation complexity, integration challenges, unknown technologies, technical debt

**Common Examples:**
- Complex OAuth flow with multiple redirects
- Unfamiliar API with poor documentation
- N+1 query performance issues
- Complex state management
- Race conditions in async operations
- Legacy code integration
- Session timeout edge cases
- CORS configuration errors

**Typical Probability:** Medium-High (new territory = higher probability)
**Typical Impact:** Low-Medium (usually fixable with code changes)

---

### Security Risks

**Definition:** Vulnerabilities that could lead to unauthorized access, data breaches, or malicious attacks

**Common Examples:**
- XSS (Cross-Site Scripting) attacks
- SQL injection vulnerabilities
- CSRF (Cross-Site Request Forgery) attacks
- Session hijacking
- Insufficient authentication/authorization
- Insecure data storage (tokens in localStorage)
- Weak password hashing
- Insecure API endpoints
- Missing rate limiting (DoS potential)
- Insufficient input validation

**Typical Probability:** Medium (security issues common if not careful)
**Typical Impact:** High (data breaches, account compromise, regulatory fines)

---

### Performance Risks

**Definition:** Response time, scalability, resource usage issues that degrade user experience

**Common Examples:**
- Slow API responses (>1s latency)
- N+1 database queries
- Missing database indexes
- Inefficient algorithms (O(n²) instead of O(n))
- Memory leaks
- Unoptimized images/assets
- No caching strategy
- Synchronous operations blocking UI
- API rate limits causing throttling

**Typical Probability:** Medium (performance issues often discovered under load)
**Typical Impact:** Medium (degrades UX but usually doesn't break functionality)

---

### Data Risks

**Definition:** Data integrity, consistency, loss, or corruption issues

**Common Examples:**
- Race conditions in concurrent updates
- Data migration without rollback plan
- Incomplete transaction rollback on error
- Missing database constraints (unique, foreign key)
- Data loss during schema changes
- Inconsistent data across microservices
- Cache invalidation issues
- Optimistic locking not implemented
- No data backup strategy

**Typical Probability:** Medium (data consistency is complex)
**Typical Impact:** High (data loss or corruption = major business impact)

---

### Business Risks

**Definition:** Impact on users, revenue, compliance, or business operations

**Common Examples:**
- Large user base affected by bug
- Revenue-generating feature broken
- Compliance violation (GDPR, HIPAA, PCI)
- Poor UX causes user churn
- Business logic incorrectly implemented
- SLA violation (downtime)
- Customer support overload
- Reputation damage

**Typical Probability:** Low-Medium (depends on feature criticality)
**Typical Impact:** Medium-High (business and revenue impact)

---

### Operational Risks

**Definition:** Deployment, monitoring, rollback, and production operation challenges

**Common Examples:**
- Complex deployment requiring downtime
- No rollback plan if deployment fails
- Missing monitoring/alerting
- External service dependency with no fallback
- Database migration can't be rolled back
- Feature flag misconfiguration
- Insufficient logging for debugging
- No health check endpoint
- Manual deployment steps (error-prone)

**Typical Probability:** Medium (operational issues common in complex systems)
**Typical Impact:** Medium-High (downtime, difficult debugging, slow recovery)

---

## Probability Assessment Guidelines

### Probability: 1 (Low - <20% chance)

**Characteristics:**
- Established patterns with proven implementations
- Team has prior experience with similar work
- Simple implementation, few unknowns
- Well-tested libraries available
- Clear requirements, no ambiguity
- Minimal external dependencies

**Example:**
- Implementing standard CRUD operations
- Using well-documented, mature library
- Adding field to existing form (established pattern)

---

### Probability: 2 (Medium - 20-60% chance)

**Characteristics:**
- Some unknowns but not entirely new territory
- Moderate complexity
- Team has related but not identical experience
- Some external dependencies
- New technology but with good documentation
- Some ambiguity in requirements

**Example:**
- Integrating third-party API with good docs
- Implementing OAuth flow for first time (but using library)
- Complex form validation with multiple interdependent fields

---

### Probability: 3 (High - >60% chance)

**Characteristics:**
- Many unknowns, largely uncharted territory
- High complexity
- Team has no prior experience
- Multiple external dependencies
- New, unfamiliar technology
- Poor or missing documentation
- Ambiguous or changing requirements
- Tight coupling, fragile existing code

**Example:**
- Custom OAuth implementation (not using library)
- Complex distributed transaction across microservices
- AI/ML model integration with unclear API behavior
- Legacy code refactor with no tests

---

## Impact Assessment Guidelines

### Impact: 1 (Low)

**Characteristics:**
- Minor inconvenience to users
- Easy to fix (< 1 hour)
- Minimal user impact scope (few users)
- No data loss
- No security implications
- No business/revenue impact

**Example:**
- UI button slightly misaligned
- Typo in help text
- Non-critical feature doesn't work (rarely used)

---

### Impact: 2 (Medium)

**Characteristics:**
- Significant issue, notable user frustration
- Moderate effort to fix (1-8 hours)
- Moderate user impact scope (many users affected)
- Degraded experience but feature still usable
- No data loss, but potential inconsistency
- Minor security concern (not exploitable)
- Minor business impact

**Example:**
- Feature works but performance is slow (3-5s latency)
- Error messages not user-friendly
- Data shown is stale (cache issue)
- UI doesn't work on mobile (but works on desktop)

---

### Impact: 3 (High)

**Characteristics:**
- Critical failure, severe user/business impact
- Major effort to fix (>8 hours, possibly days)
- Large user impact scope (most/all users)
- Feature completely broken or unusable
- Data loss or corruption possible
- Security breach or vulnerability
- Major business/revenue impact
- Regulatory violation
- Reputation damage

**Example:**
- Security vulnerability allowing data breach
- Payment processing completely broken (revenue loss)
- Data corruption requiring manual recovery
- System downtime (all users locked out)
- PCI compliance violation (legal risk)

---

## Integration Examples

### Integration with create-task-spec

**When:** After task spec creation, before implementation begins

**Data Flow:**
```
create-task-spec → task specification file
                    ↓
              risk-profile reads task spec
                    ↓
              identifies risks from:
              - Acceptance criteria
              - Technical context
              - Task breakdown
                    ↓
              generates risk profile
```

**Example:**
```markdown
create-task-spec created:
- Task: task-007 - Implement User Authentication
- File: .claude/tasks/task-007.md
- Acceptance criteria: OAuth2, secure token storage, session management
- Context: New OAuth integration, 4 systems involved

risk-profile runs:
- Reads task-007.md
- Sees "OAuth2" in acceptance → identifies security risks
- Sees "4 systems" → identifies integration risks
- Sees "secure token storage" → identifies token leakage risks
- Generates risk profile with P×I scoring
- Recommends: Store tokens in httpOnly cookies, write security tests
```

---

### Integration with test-design

**When:** After risk profile created, before test writing begins

**Data Flow:**
```
risk-profile → risk profile report with P0/P1/P2 priorities
                    ↓
              test-design reads risk profile
                    ↓
              prioritizes test scenarios by risk level
                    ↓
              generates detailed test specs for high-risk areas
```

**Example:**
```markdown
risk-profile output:
- Risk #1: OAuth token leakage (Score 9) → P0 test required
- Risk #2: Session hijacking (Score 9) → P0 test required
- Risk #3: Scope validation (Score 6) → P0 test required
- Risk #4: Rate limits (Score 4) → P1 test required

test-design uses priorities:
- Creates security test spec for token leakage (P0)
- Creates security test spec for session hijacking (P0)
- Creates integration test spec for scope validation (P0)
- Creates performance test spec for rate limits (P1)
- Allocates more time to P0 tests (critical risks)
```

---

### Integration with quality-gate

**When:** After implementation and tests complete, during quality review

**Data Flow:**
```
risk-profile → risk profile report with critical risks
                    ↓
              quality-gate reads risk profile
                    ↓
              checks if critical risks mitigated
                    ↓
              checks if P0 tests pass
                    ↓
              determines PASS/CONCERNS/FAIL
```

**Example:**
```markdown
risk-profile identified:
- 2 critical risks (score 9): token leakage, session hijacking
- 5 high risks (score 6): scope validation, CSRF, etc.
- Predicted gate: CONCERNS (critical risks require mitigation)

quality-gate evaluates:
- Are critical risks mitigated? Check implementation for httpOnly cookies ✓
- Do P0 tests pass? Check test results for security tests ✓
- Are high risks addressed? Check test coverage ✓
- Decision: PASS (all mitigations in place, tests pass)
```

---

### Integration with nfr-assess

**When:** Risk profile informs NFR assessment, especially security and performance NFRs

**Data Flow:**
```
risk-profile → identifies security and performance risks
                    ↓
              nfr-assess considers risks when assessing NFRs
                    ↓
              security/performance NFRs get stricter if risks high
```

**Example:**
```markdown
risk-profile found:
- High security risks (score 6-9): OAuth token leakage, session hijacking
- High performance risks (score 6): API rate limits, handshake latency

nfr-assess adjusts:
- Security NFR: Requires penetration testing (due to critical security risks)
- Performance NFR: Requires load testing (due to rate limit concerns)
- Raises bar for NFR compliance based on risk level
```

---

## JSON Output Format

**Complete Skill Output Structure:**
```json
{
  "skill": "risk-profile",
  "version": "2.0",
  "status": "completed",
  "task_id": "task-012",
  "task_title": "Implement Payment Processing Integration",
  "assessment_date": "2025-10-30T14:32:15Z",
  "assessment_mode": "pre-implementation",
  "duration_ms": 1247,
  "risk_summary": {
    "total_risks": 18,
    "critical_risks": 2,
    "high_risks": 5,
    "medium_risks": 8,
    "low_risks": 3,
    "highest_risk_score": 9
  },
  "risks": [
    {
      "id": 1,
      "category": "Security",
      "title": "OAuth token leakage via XSS",
      "description": "OAuth access tokens stored in localStorage vulnerable to XSS attacks",
      "probability": 3,
      "probability_reasoning": "Token storage complex, XSS common, team limited OAuth experience",
      "impact": 3,
      "impact_reasoning": "Complete account compromise, data breach, regulatory violation, major fix effort",
      "risk_score": 9,
      "risk_level": "critical",
      "mitigation": {
        "prevention": "Store tokens in httpOnly secure cookies, never localStorage",
        "detection": "Security audit, penetration testing of auth flow",
        "recovery": "Force token refresh, revoke compromised tokens",
        "phase": "implementation",
        "effort": "moderate",
        "effort_hours": "2-3",
        "actions": [
          "Implement token storage in httpOnly cookies (server-side set)",
          "Never expose tokens to client JavaScript",
          "Add CSP headers to prevent inline scripts",
          "Write tests: XSS attack simulation, token not accessible from JS"
        ]
      },
      "tests": [
        {
          "test_id": "T1",
          "priority": "P0",
          "scenario": "XSS token theft simulation",
          "level": "integration+security",
          "expected": "Token stored in httpOnly cookie, XSS cannot steal token",
          "file": "tests/security/auth-xss-protection.test.ts"
        },
        {
          "test_id": "T3",
          "priority": "P0",
          "scenario": "Cookie security flags validation",
          "level": "unit",
          "expected": "httpOnly=true, secure=true, SameSite=Strict",
          "file": "tests/unit/auth-cookie-security.test.ts"
        }
      ]
    },
    {
      "id": 2,
      "category": "Security",
      "title": "Session hijacking via insecure cookies",
      "description": "Session cookies not properly secured, allowing session theft",
      "probability": 3,
      "probability_reasoning": "Cookie security often misconfigured, easy to forget flags",
      "impact": 3,
      "impact_reasoning": "Account takeover, unauthorized access, difficult to detect",
      "risk_score": 9,
      "risk_level": "critical",
      "mitigation": {
        "prevention": "Set cookie flags: httpOnly, secure, SameSite=Strict",
        "detection": "Monitor session usage from multiple IPs/locations",
        "recovery": "Force re-authentication on suspicious activity",
        "phase": "implementation+monitoring",
        "effort": "minimal+moderate",
        "effort_hours": "1+2",
        "actions": [
          "Set cookie flags: httpOnly=true, secure=true, SameSite=Strict",
          "Implement session fingerprinting (IP, user agent)",
          "Add monitoring alert on session anomaly",
          "Write tests: Cookie flags validation, session hijack simulation"
        ]
      },
      "tests": [
        {
          "test_id": "T2",
          "priority": "P0",
          "scenario": "Session hijacking prevention",
          "level": "integration+security",
          "expected": "Session invalidated on IP/device change",
          "file": "tests/security/session-hijack-detection.test.ts"
        },
        {
          "test_id": "T3",
          "priority": "P0",
          "scenario": "Cookie security flags validation",
          "level": "unit",
          "expected": "httpOnly=true, secure=true, SameSite=Strict",
          "file": "tests/unit/auth-cookie-security.test.ts"
        }
      ]
    }
  ],
  "test_priorities": {
    "p0_tests": [
      {
        "test_id": "T1",
        "scenario": "XSS token theft simulation",
        "risk_ids": [1],
        "risk_score": 9
      },
      {
        "test_id": "T2",
        "scenario": "Session hijacking prevention",
        "risk_ids": [2],
        "risk_score": 9
      },
      {
        "test_id": "T3",
        "scenario": "Cookie security flags validation",
        "risk_ids": [1, 2],
        "risk_score": 9
      },
      {
        "test_id": "T4",
        "scenario": "OAuth scope over-privilege prevention",
        "risk_ids": [3],
        "risk_score": 6
      },
      {
        "test_id": "T5",
        "scenario": "OAuth provider outage fallback",
        "risk_ids": [6],
        "risk_score": 6
      },
      {
        "test_id": "T6",
        "scenario": "CSRF protection validation",
        "risk_ids": [4],
        "risk_score": 6
      }
    ],
    "p1_tests": [
      {
        "test_id": "T7",
        "scenario": "OAuth token refresh flow",
        "risk_ids": [8],
        "risk_score": 6
      }
    ],
    "p2_tests": [
      {
        "test_id": "T14",
        "scenario": "Session timeout edge cases",
        "risk_ids": [16],
        "risk_score": 2
      }
    ]
  },
  "quality_gate": {
    "predicted_status": "CONCERNS",
    "current_reasoning": "2 critical risks (score 9) trigger CONCERNS gate",
    "post_mitigation_status": "PASS",
    "post_mitigation_reasoning": "All critical risks mitigated, P0 tests pass",
    "requirements_for_pass": [
      "Implement httpOnly cookie token storage",
      "Set cookie security flags (httpOnly, secure, SameSite)",
      "Implement OAuth scope validation",
      "Add CSRF token validation",
      "Write and pass all 6 P0 tests",
      "Write and pass 7 P1 tests"
    ],
    "estimated_effort_hours": "29-37"
  },
  "mitigation_summary": {
    "total_strategies": 11,
    "critical_mitigated": "2/2",
    "high_mitigated": "5/5",
    "total_effort_hours": "14-18",
    "phases": {
      "implementation": 6,
      "testing": 5,
      "deployment": 1,
      "monitoring": 3
    }
  },
  "report_path": ".claude/quality/assessments/task-012-risk-20251030.md",
  "telemetry": {
    "event": "skill.risk-profile.completed",
    "task_id": "task-012",
    "assessment_mode": "pre-implementation",
    "total_risks": 18,
    "critical_risks_count": 2,
    "high_risks_count": 5,
    "medium_risks_count": 8,
    "low_risks_count": 3,
    "highest_risk_score": 9,
    "quality_gate_impact": "CONCERNS",
    "p0_tests_count": 6,
    "p1_tests_count": 7,
    "p2_tests_count": 5,
    "assessment_duration_ms": 1247
  }
}
```

---

*Complete templates and output formats for risk-profile skill*
