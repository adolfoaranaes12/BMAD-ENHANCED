# NFR Assessment Templates and Output Formats

This document contains all output templates, formats, and examples for the nfr-assess skill across all 6 NFR categories.

---

## Step 0: Configuration Loading Output

**Complete Output Format:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NFR Assessment - Configuration Loaded
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: task-auth-007 - Implement JWT authentication
✓ Related assessments:
  - Risk Profile: FOUND (.claude/quality/risk-profiles/task-auth-007-risk.md)
  - Traceability: FOUND (.claude/quality/traceability/task-auth-007-trace.md)
  - Test Design: NOT FOUND
✓ Implementation files: 12 files identified
  - Source files: 8 (.ts, .js)
  - Config files: 2 (.yaml, .env.example)
  - Infrastructure: 2 (Dockerfile, docker-compose.yml)
  - Dependencies: package.json
✓ Relevant NFR categories (priority):
  - Security: HIGH (auth implementation requires comprehensive security review)
  - Performance: HIGH (JWT verification impacts request latency)
  - Reliability: MEDIUM (error handling for auth failures)
  - Maintainability: MEDIUM (code quality and testability)
  - Scalability: LOW (stateless JWT design inherently scalable)
  - Usability: MEDIUM (API error messages and documentation)
✓ Automated checks available:
  - Security: npm audit, semgrep
  - Code quality: eslint
  - Test coverage: jest --coverage
  - Performance: NOT CONFIGURED
✓ Output: .claude/quality/assessments/task-auth-007-nfr-20251030.md

Ready to begin NFR assessment...
```

---

## Step 1: Security Assessment Output

**Complete Security Assessment Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Security Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Security Score: 75% (CONCERNS)

Criteria Evaluated: 10 total
  - PASS: 6 criteria
  - CONCERNS: 3 criteria
  - FAIL: 1 criterion
  - UNCLEAR: 0 criteria

Automated Checks Completed:
  - Dependency Vulnerabilities: 2 MODERATE, 3 LOW (0 critical, 0 high)
  - Code Security Scan: 1 MEDIUM finding (semgrep)
  - Secret Detection: 0 secrets found

Criteria Breakdown:
  ✅ Authentication: PASS - JWT implementation with bcrypt password hashing
  ✅ Authorization: PASS - Role-based access control (RBAC) middleware
  ⚠️  Input Validation: CONCERNS - Partial validation (Zod on /login, missing on /refresh)
  ⚠️  Output Encoding: CONCERNS - No XSS protection for error messages
  ❌ Dependency Vulnerabilities: FAIL - 2 moderate vulnerabilities in jsonwebtoken@8.5.1
  ✅ Secrets Management: PASS - Secrets in environment variables, no hardcoded
  ✅ HTTPS/TLS: PASS - Configured in nginx (production), localhost (dev)
  ⚠️  Rate Limiting: CONCERNS - Basic rate limiting (10 req/min), no exponential backoff
  ✅ CORS: PASS - CORS configured with allowlist
  ✅ Security Headers: PASS - helmet.js configured

Critical Gaps: 1
  1. [P0] Dependency Vulnerabilities - jsonwebtoken@8.5.1 has 2 moderate CVEs
     Remediation: Upgrade to jsonwebtoken@9.0.2 or later
     Files: package.json:23
     Estimated fix time: 15 minutes

High Gaps: 2
  2. [P1] Input Validation - /refresh endpoint lacks validation
     Remediation: Add Zod schema validation for refresh token requests
     Files: src/controllers/auth.controller.ts:89-104
     Estimated fix time: 20 minutes

  3. [P1] Output Encoding - Error messages may leak sensitive info
     Remediation: Sanitize error messages, remove stack traces in production
     Files: src/middleware/error-handler.ts:23-45
     Estimated fix time: 30 minutes

Medium Gaps: 1
  4. [P2] Rate Limiting - No exponential backoff for failed login attempts
     Remediation: Implement exponential backoff (e.g., 1min, 2min, 4min...)
     Files: src/middleware/rate-limit.ts:12-34
     Estimated fix time: 45 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Evidence Format:**
```markdown
## Security Evidence

### Authentication
- **Status:** PASS
- **Evidence:**
  - File: `src/services/auth.service.ts:45-67`
  - Implementation: bcrypt.hash() with salt rounds 10
  - Test: `src/__tests__/auth.service.test.ts:123-145` validates password hashing

### Authorization
- **Status:** PASS
- **Evidence:**
  - File: `src/middleware/auth.middleware.ts:23-56`
  - Implementation: Role-based access control (RBAC)
  - Roles: admin, user, guest
  - Test: `src/__tests__/auth.middleware.test.ts:78-112` validates RBAC

### Input Validation
- **Status:** CONCERNS
- **Evidence:**
  - File: `src/controllers/auth.controller.ts:34-42` (login endpoint)
  - Implementation: Zod schema validation for login
  - Gap: /refresh endpoint (lines 89-104) lacks validation
  - Recommendation: Add Zod schema for refresh token requests
```

---

## Step 2: Performance Assessment Output

**Complete Performance Assessment Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Performance Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Performance Score: 82% (PASS)

Criteria Evaluated: 10 total
  - PASS: 7 criteria
  - CONCERNS: 2 criteria
  - FAIL: 0 criteria
  - UNCLEAR: 1 criterion

Performance Benchmarks:
  - Response Time (p50): 45ms (threshold: <100ms) ✅
  - Response Time (p95): 120ms (threshold: <200ms) ✅
  - Response Time (p99): 180ms (threshold: <500ms) ✅
  - Throughput: 850 req/s (threshold: >500 req/s) ✅
  - Load Test: 98.5% success rate at 1000 req/s ✅
  - Memory Usage: 145 MB avg (threshold: <200 MB) ✅

Criteria Breakdown:
  ✅ Response Time: PASS - p95 = 120ms (under 200ms threshold)
  ✅ Throughput: PASS - 850 req/s sustained
  ✅ Resource Usage: PASS - Memory 145MB avg, CPU 35% avg
  ⚠️  Database Queries: CONCERNS - 1 N+1 query detected in /users endpoint
  ✅ Caching: PASS - Redis caching for JWT public keys (TTL 1h)
  🔍 Asset Optimization: UNCLEAR - Not applicable (API-only)
  ✅ Algorithm Complexity: PASS - No O(n²) or worse in hot paths
  ✅ Connection Pooling: PASS - Database pool (min 5, max 20)
  ⚠️  Async Operations: CONCERNS - 1 blocking file write in request handler
  ✅ Load Testing: PASS - 98.5% success at 1000 req/s

High Gaps: 2
  1. [P1] N+1 Query - /users endpoint fetches roles in loop
     Remediation: Add JOIN to fetch users with roles in single query
     Files: src/controllers/user.controller.ts:67-89
     Impact: ~200ms latency increase at 100+ users
     Estimated fix time: 30 minutes

  2. [P1] Blocking File Write - Audit log writes block request thread
     Remediation: Move audit logging to async queue (Bull/BullMQ)
     Files: src/middleware/audit.middleware.ts:45-67
     Impact: ~50ms added latency per request
     Estimated fix time: 2 hours (queue setup)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Performance Benchmark Tables:**
```markdown
## Performance Benchmarks

### Response Time Distribution

| Percentile | Value  | Threshold | Status |
|------------|--------|-----------|--------|
| p50 (med)  | 45ms   | <100ms    | ✅ PASS |
| p75        | 78ms   | <150ms    | ✅ PASS |
| p95        | 120ms  | <200ms    | ✅ PASS |
| p99        | 180ms  | <500ms    | ✅ PASS |
| p99.9      | 450ms  | <1000ms   | ✅ PASS |

### Throughput Test Results

| Load (req/s) | Success Rate | Avg Latency | p95 Latency | Errors |
|--------------|--------------|-------------|-------------|--------|
| 100          | 100%         | 42ms        | 67ms        | 0      |
| 500          | 99.8%        | 56ms        | 98ms        | 1      |
| 1000         | 98.5%        | 78ms        | 145ms       | 15     |
| 2000         | 87.3%        | 245ms       | 890ms       | 254    |

**Recommended max load:** 1000 req/s (98.5% success rate)
```

---

## Step 3: Reliability Assessment Output

**Complete Reliability Assessment Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reliability Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Reliability Score: 78% (PASS)

Criteria Evaluated: 10 total
  - PASS: 6 criteria
  - CONCERNS: 3 criteria
  - FAIL: 1 criterion

Criteria Breakdown:
  ✅ Error Handling: PASS - Try-catch in all async operations
  ✅ Input Validation Errors: PASS - Zod validation with detailed errors
  ⚠️  Graceful Degradation: CONCERNS - No fallback when Redis unavailable
  ⚠️  Retry Logic: CONCERNS - No retry for transient failures
  ❌ Circuit Breakers: FAIL - No circuit breaker pattern implemented
  ✅ Logging: PASS - winston with structured JSON logs
  🔍 Monitoring: CONCERNS - Health check exists, no metrics exported
  ✅ Idempotency: PASS - Idempotent POST with request IDs
  ✅ Data Integrity: PASS - Database transactions for multi-step operations
  ✅ Disaster Recovery: PASS - Database backups (daily), documented restore

Logging Configuration:
  - Framework: winston
  - Format: JSON (structured)
  - Levels: error, warn, info, debug
  - Transports: Console (dev), File (prod)
  - Log Aggregation: NOT CONFIGURED

Monitoring Configuration:
  - Health Check: ✅ /health endpoint
  - Metrics Export: ❌ NOT CONFIGURED
  - APM Integration: ❌ NOT CONFIGURED
  - Alerting: ❌ NOT CONFIGURED

Critical Gaps: 1
  1. [P0] Circuit Breakers - No protection against cascading failures
     Remediation: Implement circuit breaker for external API calls
     Files: src/services/external-api.service.ts:23-89
     Impact: Cascading failures when external API is slow/down
     Estimated fix time: 3 hours

High Gaps: 2
  2. [P1] Graceful Degradation - Redis failure breaks authentication
     Remediation: Add fallback to in-memory cache or bypass when Redis down
     Files: src/services/cache.service.ts:45-78
     Impact: Service unavailable when Redis down
     Estimated fix time: 1.5 hours

  3. [P1] Monitoring - No metrics exported (Prometheus, Datadog)
     Remediation: Add prometheus-client middleware for metrics export
     Files: src/app.ts
     Impact: No observability into production performance
     Estimated fix time: 2 hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Step 4: Maintainability Assessment Output

**Complete Maintainability Assessment Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Maintainability Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Maintainability Score: 85% (PASS)

Criteria Evaluated: 10 total
  - PASS: 8 criteria
  - CONCERNS: 2 criteria
  - FAIL: 0 criteria

Automated Checks:
  - Test Coverage: 87.5% (threshold: ≥80%) ✅
  - Linting: PASS - 0 errors, 3 warnings
  - Avg Cyclomatic Complexity: 4.2 (threshold: ≤10) ✅
  - Max Cyclomatic Complexity: 8 (threshold: ≤15) ✅
  - Code Duplication: 2.1% (threshold: <5%) ✅
  - Type Safety: TypeScript strict mode enabled ✅

Criteria Breakdown:
  ✅ Code Quality: PASS - Clean code, consistent style
  ✅ Test Coverage: PASS - 87.5% overall (statements, branches, functions, lines)
  ⚠️  Documentation: CONCERNS - API docs incomplete, missing JSDoc
  ✅ Modularity: PASS - Clear separation (controllers, services, middleware)
  ✅ Naming: PASS - Descriptive names, follows conventions
  ✅ Complexity: PASS - Avg 4.2, max 8 (well under thresholds)
  ✅ Duplication: PASS - 2.1% duplication (low)
  ✅ Type Safety: PASS - TypeScript strict mode, no 'any' types
  ⚠️  Dependencies: CONCERNS - 3 dependencies outdated (non-security)
  ✅ Technical Debt: PASS - 2 TODO comments (minor, documented)

Coverage Breakdown:
  - Statements: 88.2% (threshold: ≥80%) ✅
  - Branches: 85.7% (threshold: ≥80%) ✅
  - Functions: 89.5% (threshold: ≥80%) ✅
  - Lines: 87.5% (threshold: ≥80%) ✅

Complexity Metrics:
  - Average Complexity: 4.2 (excellent)
  - Median Complexity: 3
  - Max Complexity: 8 (in src/services/auth.service.ts:validateToken)
  - Functions >10: 0 (excellent)

Documentation Status:
  - README: ✅ EXISTS - Comprehensive
  - API Documentation: ⚠️  INCOMPLETE - Swagger spec only covers 60% of endpoints
  - JSDoc: ⚠️  SPARSE - 40% of functions documented
  - Architecture Docs: ✅ EXISTS

High Gaps: 2
  1. [P1] API Documentation - Swagger spec only covers 60% of endpoints
     Remediation: Complete OpenAPI spec for all endpoints
     Files: src/swagger.yaml
     Impact: Difficult for API consumers to discover all endpoints
     Estimated fix time: 3 hours

  2. [P1] JSDoc Comments - Only 40% of functions documented
     Remediation: Add JSDoc comments to public functions/methods
     Files: src/services/*.ts, src/controllers/*.ts
     Impact: Reduced code maintainability
     Estimated fix time: 4 hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Step 5: Scalability Assessment Output

**Complete Scalability Assessment Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scalability Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Scalability Score: 72% (CONCERNS)

Criteria Evaluated: 10 total
  - PASS: 5 criteria
  - CONCERNS: 3 criteria
  - FAIL: 1 criterion
  - UNCLEAR: 1 criterion

Criteria Breakdown:
  ✅ Stateless Design: PASS - JWT tokens, no in-memory session state
  ✅ Horizontal Scaling: PASS - Stateless, can run multiple instances
  ⚠️  Database Design: CONCERNS - Missing 3 indexes on foreign keys
  ✅ Connection Pooling: PASS - Configured (min 5, max 20)
  ⚠️  Caching: CONCERNS - Redis caching exists but limited coverage
  ⚠️  Async Processing: CONCERNS - No background job queue
  ✅ Rate Limiting: PASS - Implemented with redis-rate-limiter
  🔍 Load Balancing: UNCLEAR - Not in scope (deployment concern)
  ❌ Resource Limits: FAIL - No memory/CPU limits configured
  ✅ Auto-Scaling: PASS - Ready for horizontal scaling (stateless)

Database Analysis:
  - Total Tables: 5
  - Total Indexes: 12
  - Missing Indexes: 3 (foreign keys without indexes)
  - Query Analysis: 1 N+1 query detected

Missing Indexes:
  1. users.role_id (foreign key, no index)
  2. sessions.user_id (foreign key, no index)
  3. audit_logs.user_id (foreign key, no index)

Caching Analysis:
  - Cache Hit Rate: 78% (good)
  - Cache Coverage: 30% of queries (low)
  - Cache Strategy: Read-through
  - Cache Invalidation: TTL-based (1h)

Critical Gaps: 1
  1. [P0] Resource Limits - No memory/CPU limits (risk of OOM)
     Remediation: Configure Node.js --max-old-space-size and container limits
     Files: Dockerfile, docker-compose.yml
     Impact: Risk of out-of-memory crashes in production
     Estimated fix time: 30 minutes

High Gaps: 3
  2. [P1] Missing Database Indexes - 3 foreign keys unindexed
     Remediation: Add indexes on users.role_id, sessions.user_id, audit_logs.user_id
     Files: migrations/add-indexes.sql
     Impact: Slow queries when tables grow (>10k rows)
     Estimated fix time: 1 hour

  3. [P1] Async Processing - No background job queue
     Remediation: Implement Bull/BullMQ for email sending, audit logging
     Files: src/services/queue.service.ts (new)
     Impact: Slow request handling for operations that don't need immediate response
     Estimated fix time: 4 hours

  4. [P1] Limited Caching - Only 30% of queries cached
     Remediation: Expand caching to /users, /roles, frequent queries
     Files: src/services/cache.service.ts
     Impact: Higher database load, slower responses
     Estimated fix time: 2 hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Step 6: Usability Assessment Output

**Complete Usability Assessment Output (API):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Usability Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Usability Score: 80% (PASS)

API Type: REST API (no UI detected)

Criteria Evaluated: 10 total (API-focused)
  - PASS: 7 criteria
  - CONCERNS: 2 criteria
  - FAIL: 1 criterion

Criteria Breakdown:
  ✅ API Design: PASS - RESTful conventions followed
  ⚠️  Error Messages: CONCERNS - Error details too verbose (leak stack traces)
  ⚠️  Documentation: CONCERNS - Swagger spec incomplete (60% coverage)
  ✅ Versioning: PASS - /v1/ prefix, versioning strategy documented
  ✅ Pagination: PASS - Cursor-based pagination on /users
  ✅ Filtering: PASS - Query params for filtering (?role=admin)
  ✅ HTTP Status Codes: PASS - Correct codes (200, 201, 400, 401, 404, 500)
  ✅ Response Format: PASS - Consistent JSON structure
  ❌ HATEOAS: FAIL - No hypermedia links in responses
  ✅ Developer Experience: PASS - Clear README, example requests

API Design Review:
  - REST Conventions: ✅ Proper HTTP verbs (GET, POST, PUT, DELETE)
  - Resource Naming: ✅ Plural nouns (/users, /roles, /sessions)
  - URL Structure: ✅ Hierarchical (/users/:id/sessions)
  - Content Negotiation: ✅ application/json

Error Response Format:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request body",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ],
    "stack": "Error: Invalid request body\n    at..." // ❌ LEAKED IN PRODUCTION
  }
}
```

Medium Gaps: 3
  1. [P2] Error Stack Traces - Leaked in production responses
     Remediation: Remove stack traces in production, only in dev
     Files: src/middleware/error-handler.ts:34-45
     Impact: Security information disclosure
     Estimated fix time: 15 minutes

  2. [P2] Incomplete API Docs - Swagger spec only 60% complete
     Remediation: Document all endpoints in OpenAPI spec
     Files: src/swagger.yaml
     Impact: Difficult API discovery for consumers
     Estimated fix time: 3 hours

  3. [P2] No HATEOAS - No hypermedia links in responses
     Remediation: Add _links object to responses (HAL format)
     Files: src/middleware/hateoas.middleware.ts (new)
     Impact: Reduced API discoverability
     Estimated fix time: 4 hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Complete Usability Assessment Output (UI):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Usability Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Overall Usability Score: 68% (CONCERNS)

UI Type: React SPA detected

Criteria Evaluated: 10 total (UI-focused)
  - PASS: 4 criteria
  - CONCERNS: 4 criteria
  - FAIL: 2 criteria

Criteria Breakdown:
  ⚠️  Accessibility (WCAG 2.1 AA): CONCERNS - 8 violations detected
  ✅ Responsive Design: PASS - Mobile, tablet, desktop breakpoints
  ⚠️  Loading States: CONCERNS - Inconsistent loading indicators
  ⚠️  Error Handling: CONCERNS - Generic error messages
  ❌ Keyboard Navigation: FAIL - Modals not keyboard accessible
  ⚠️  Color Contrast: CONCERNS - 3 elements fail contrast ratio
  ❌ Screen Reader Support: FAIL - Missing ARIA labels
  ✅ Form Validation: PASS - Real-time validation with clear messages
  ✅ Intuitive Navigation: PASS - Clear nav menu, breadcrumbs
  ✅ Performance: PASS - LCP 1.8s, FID 45ms, CLS 0.05

Accessibility Audit (axe-core):
  - Critical: 2 violations (keyboard traps, missing alt text)
  - Serious: 3 violations (ARIA labels, color contrast)
  - Moderate: 3 violations (heading order, landmarks)

WCAG 2.1 AA Compliance:
  - Perceivable: ⚠️  PARTIAL (color contrast issues)
  - Operable: ❌ FAIL (keyboard navigation broken)
  - Understandable: ✅ PASS (clear labels, error messages)
  - Robust: ⚠️  PARTIAL (missing ARIA attributes)

Performance Metrics (Lighthouse):
  - Performance: 92/100 ✅
  - Accessibility: 78/100 ⚠️
  - Best Practices: 95/100 ✅
  - SEO: 88/100 ✅

Critical Gaps: 2
  1. [P0] Keyboard Navigation - Modals trap focus, no ESC to close
     Remediation: Implement focus trap with escape key handling
     Files: src/components/Modal.tsx
     Impact: Blocks keyboard-only users from using modals
     Estimated fix time: 2 hours

  2. [P0] Screen Reader Support - Missing ARIA labels on interactive elements
     Remediation: Add aria-label, aria-describedby to buttons, inputs, modals
     Files: src/components/*.tsx
     Impact: Unusable for screen reader users
     Estimated fix time: 4 hours

High Gaps: 4
  3. [P1] Color Contrast - 3 elements fail WCAG AA (4.5:1 ratio)
     Remediation: Increase contrast for text on colored backgrounds
     Files: src/styles/colors.css
     Impact: Difficult to read for visually impaired users
     Estimated fix time: 1 hour

  [Additional gaps...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Step 7: Overall NFR Scoring Formula

**Weighted Scoring Formula:**
```
Overall NFR Score = (
  Security Score       × 0.25 (25% weight) +
  Performance Score    × 0.20 (20% weight) +
  Reliability Score    × 0.20 (20% weight) +
  Maintainability Score× 0.15 (15% weight) +
  Scalability Score    × 0.10 (10% weight) +
  Usability Score      × 0.10 (10% weight)
)
```

**Example Calculation:**
```
Security:       75% × 0.25 = 18.75
Performance:    82% × 0.20 = 16.40
Reliability:    78% × 0.20 = 15.60
Maintainability: 85% × 0.15 = 12.75
Scalability:    72% × 0.10 =  7.20
Usability:      80% × 0.10 =  8.00
                             -------
Overall NFR Score:           78.70%
```

**Status Determination:**
```
Overall NFR Score:
  ≥90%:  PASS (Excellent) - Production-ready, exemplary quality
  75-89%: PASS (Good)     - Production-ready, minor improvements recommended
  60-74%: CONCERNS        - Needs improvement before production
  <60%:  FAIL             - Critical issues, not production-ready
```

**Report Generation Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NFR Assessment Report Generated
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ NFR assessment report generated successfully

Output: .claude/quality/assessments/task-auth-007-nfr-20251030.md

Overall NFR Score: 78.7% (PASS - Good)

Category Scores:
  ├─ Security:       75% (CONCERNS) - 1 critical, 2 high gaps
  ├─ Performance:    82% (PASS)     - 2 high gaps
  ├─ Reliability:    78% (PASS)     - 1 critical, 2 high gaps
  ├─ Maintainability:85% (PASS)     - 2 high gaps
  ├─ Scalability:    72% (CONCERNS) - 1 critical, 3 high gaps
  └─ Usability:      80% (PASS)     - 3 medium gaps

Total Gaps: 18
  - Critical (P0): 3
  - High (P1):    11
  - Medium (P2):   4

Report Contents:
  - Executive Summary: ✓
  - Category Assessments: ✓ (6 categories)
  - Gap Analysis: ✓ (18 gaps with remediation)
  - Recommendations: ✓ (prioritized action plan)
  - Quality Gate Prediction: ✓

Report Size: 847 lines

Next: Present summary to user
```

---

## Step 8: Complete User Summary Format

**Full Summary Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Non-Functional Requirements Assessment Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: task-auth-007 - Implement JWT authentication
Date: 2025-10-30
Assessor: nfr-assess skill v2.0
Duration: 8m 45s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Overall NFR Score: 78.7% (PASS - Good)

Production-ready with recommended improvements. 3 critical gaps should be addressed
before release, 11 high-priority gaps should be resolved in follow-up tasks.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Category Scores:

├─ 🔒 Security: 75% (CONCERNS)
│  Status: Needs attention - 1 critical security gap
│  Strengths: JWT auth, RBAC, secrets management, CORS, security headers
│  Concerns: Outdated dependencies (CVEs), partial input validation
│  Critical: Dependency vulnerabilities (jsonwebtoken@8.5.1)
│
├─ ⚡ Performance: 82% (PASS)
│  Status: Good - Meets performance targets
│  Strengths: p95 latency 120ms, 850 req/s throughput, Redis caching
│  Concerns: 1 N+1 query, blocking file I/O in request handler
│  Impact: Slight latency increase at scale
│
├─ 🛡️  Reliability: 78% (PASS)
│  Status: Good - Solid error handling and logging
│  Strengths: Comprehensive error handling, structured logging, idempotency
│  Concerns: No circuit breakers, no graceful degradation, limited monitoring
│  Critical: Circuit breaker missing for external API calls
│
├─ 🔧 Maintainability: 85% (PASS)
│  Status: Excellent - High quality, testable code
│  Strengths: 87.5% test coverage, low complexity (avg 4.2), TypeScript strict
│  Concerns: Incomplete API docs (60%), sparse JSDoc comments (40%)
│  Impact: Reduced developer experience
│
├─ 📈 Scalability: 72% (CONCERNS)
│  Status: Needs improvement - Scalability concerns identified
│  Strengths: Stateless design, horizontal scaling ready, connection pooling
│  Concerns: Missing DB indexes, no background jobs, limited caching
│  Critical: No resource limits (risk of OOM crashes)
│
└─ 👤 Usability: 80% (PASS)
   Status: Good - Well-designed API
   Strengths: RESTful design, versioning, pagination, clear HTTP codes
   Concerns: Error details too verbose, incomplete API docs, no HATEOAS
   Impact: Minor developer experience gaps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  Critical Gaps (P0 - Must Fix Before Release):

1. [Security] Dependency Vulnerabilities - jsonwebtoken@8.5.1
   Risk: 2 moderate CVEs in JWT library (CVE-2022-23529, CVE-2022-23540)
   Impact: Potential token forgery vulnerability
   Fix: Upgrade to jsonwebtoken@9.0.2 or later
   File: package.json:23
   Estimated Time: 15 minutes
   ⚠️  BLOCKS RELEASE

2. [Reliability] Circuit Breakers Missing
   Risk: Cascading failures when external API is slow/unavailable
   Impact: Service becomes unavailable due to dependency failure
   Fix: Implement circuit breaker pattern (opossum library)
   File: src/services/external-api.service.ts:23-89
   Estimated Time: 3 hours
   ⚠️  PRODUCTION RISK

3. [Scalability] Resource Limits Not Configured
   Risk: Out-of-memory crashes in production under load
   Impact: Service crashes, requires manual restart
   Fix: Configure Node.js --max-old-space-size=512 and container limits
   File: Dockerfile, docker-compose.yml
   Estimated Time: 30 minutes
   ⚠️  PRODUCTION RISK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 High Priority Gaps (P1 - Should Fix Before Production):

4. [Security] Input Validation - /refresh endpoint lacks validation
   Fix: Add Zod schema validation for refresh token requests
   File: src/controllers/auth.controller.ts:89-104
   Time: 20 min

5. [Security] Output Encoding - Error messages may leak sensitive info
   Fix: Sanitize error messages, remove stack traces in production
   File: src/middleware/error-handler.ts:23-45
   Time: 30 min

6. [Performance] N+1 Query - /users endpoint fetches roles in loop
   Fix: Add JOIN to fetch users with roles in single query
   File: src/controllers/user.controller.ts:67-89
   Time: 30 min

7. [Performance] Blocking File Write - Audit log writes block requests
   Fix: Move audit logging to async queue (Bull/BullMQ)
   File: src/middleware/audit.middleware.ts:45-67
   Time: 2 hours

8. [Reliability] Graceful Degradation - Redis failure breaks auth
   Fix: Add fallback to in-memory cache when Redis unavailable
   File: src/services/cache.service.ts:45-78
   Time: 1.5 hours

9. [Reliability] Monitoring - No metrics exported
   Fix: Add prometheus-client middleware for metrics export
   File: src/app.ts
   Time: 2 hours

10. [Scalability] Missing Database Indexes - 3 foreign keys unindexed
    Fix: Add indexes on users.role_id, sessions.user_id, audit_logs.user_id
    File: migrations/add-indexes.sql
    Time: 1 hour

11. [Scalability] Async Processing - No background job queue
    Fix: Implement Bull/BullMQ for email sending, audit logging
    File: src/services/queue.service.ts (new)
    Time: 4 hours

12. [Scalability] Limited Caching - Only 30% of queries cached
    Fix: Expand caching to /users, /roles, frequent queries
    File: src/services/cache.service.ts
    Time: 2 hours

13. [Maintainability] API Documentation - Swagger spec 60% complete
    Fix: Complete OpenAPI spec for all endpoints
    File: src/swagger.yaml
    Time: 3 hours

14. [Maintainability] JSDoc Comments - Only 40% documented
    Fix: Add JSDoc comments to public functions/methods
    File: src/services/*.ts, src/controllers/*.ts
    Time: 4 hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Quality Gate Impact: CONCERNS

Reasoning:
  - Overall NFR score is 78.7% (within PASS range of 75-89%)
  - 3 critical (P0) gaps identified:
    1. Security: Dependency vulnerabilities (production blocker)
    2. Reliability: No circuit breakers (cascading failure risk)
    3. Scalability: No resource limits (OOM crash risk)
  - Security score is 75% (CONCERNS) due to dependency CVEs
  - Scalability score is 72% (CONCERNS) due to missing critical configs

Decision:
  - Quality gate will likely return CONCERNS (not FAIL)
  - Merge permitted with conditions: fix P0 gaps before release
  - Follow-up epic recommended for P1 gaps (11 items, ~20 hours)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ To Achieve Quality Gate PASS:

Immediate Actions (before merge):
  1. ⏱️  15 min - Upgrade jsonwebtoken to 9.0.2+ (fixes 2 CVEs)
  2. ⏱️  30 min - Configure resource limits (prevents OOM)
  3. ⏱️  3 hours - Implement circuit breakers (prevents cascading failures)

Total time to resolve P0 gaps: ~4 hours

Follow-up Actions (before production release):
  4. ⏱️  50 min - Fix remaining security gaps (input validation, output encoding)
  5. ⏱️  2.5 hours - Fix performance gaps (N+1 query, blocking I/O)
  6. ⏱️  3.5 hours - Fix reliability gaps (graceful degradation, monitoring)
  7. ⏱️  7 hours - Fix scalability gaps (indexes, async processing, caching)
  8. ⏱️  7 hours - Fix maintainability gaps (API docs, JSDoc)

Total time for P1 gaps: ~20.5 hours (2.5 sprints)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Full Report: .claude/quality/assessments/task-auth-007-nfr-20251030.md

Report includes:
  - Executive summary with overall assessment
  - Detailed assessment for each of 6 NFR categories
  - Evidence for all criteria (file paths, line numbers, code snippets)
  - Complete gap analysis with remediation guidance
  - Prioritized recommendations
  - Integration with risk profile and traceability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Recommended Next Steps:

1. 📖 Review detailed NFR assessment report
   → .claude/quality/assessments/task-auth-007-nfr-20251030.md

2. 🔥 Fix 3 CRITICAL (P0) gaps before merge (~4 hours)
   → Dependency upgrade, circuit breakers, resource limits

3. 📋 Create epic for 11 HIGH (P1) gaps (~20.5 hours)
   → Track in project management tool, schedule for next sprint

4. 🔄 Re-run nfr-assess after fixing P0 gaps
   → Validate gap closure, update NFR score

5. ✅ Proceed to quality-gate when:
   → All P0 gaps closed (NFR score ≥80%)
   → Security and Reliability scores ≥80%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Telemetry emitted: skill.nfr-assess.completed
```

---

## Integration Examples

### Integration with risk-profile

**Risk Amplification Example:**
```
Risk Profile Input:
  Risk #2: SQL Injection
  Score: 6 (HIGH)
  Likelihood: MEDIUM
  Impact: HIGH

NFR Security Assessment:
  Input Validation: CONCERNS
  Evidence: No parameterized queries in /search endpoint

Gap Severity Calculation:
  Base Severity: HIGH (from NFR assessment)
  Risk Amplification: +1 level (matching HIGH risk in risk profile)
  Final Severity: CRITICAL (P0)
  Priority: Must fix before merge

Result:
  Gap #1: [P0/CRITICAL] SQL Injection Risk - /search endpoint
  File: src/controllers/search.controller.ts:45-67
  Risk Profile Reference: Risk #2 (Score 6, HIGH)
  NFR Category: Security - Input Validation
  Remediation: Use parameterized queries or ORM query builders
  Estimated Time: 1 hour
```

### Integration with trace-requirements

**Traceability Input for NFR Assessment:**
```
Traceability Matrix Input:
  - Requirement: REQ-SEC-001 (JWT authentication)
    Implementation: ✅ src/middleware/auth.middleware.ts
    Tests: ✅ 12 tests, 95% coverage

  - Requirement: REQ-SEC-002 (Rate limiting)
    Implementation: ⚠️  src/middleware/rate-limit.ts (basic implementation)
    Tests: ⚠️  3 tests, 60% coverage

NFR Assessment Output:
  Security - Rate Limiting: CONCERNS
  Evidence: Basic rate limiting exists (from traceability)
  Gap: No exponential backoff, coverage 60% (below threshold)
  Traceability Reference: REQ-SEC-002
  Remediation: Implement exponential backoff, add tests to 80%+

Gap added to traceability:
  REQ-SEC-002: ⚠️  PARTIAL COVERAGE
  Missing: Exponential backoff implementation
  Gap Reference: NFR Assessment task-auth-007, Gap #4
```

### Integration with quality-gate

**NFR Input to Quality Gate:**
```json
{
  "overall_nfr_score": 78.7,
  "category_scores": {
    "security": 75,
    "performance": 82,
    "reliability": 78,
    "maintainability": 85,
    "scalability": 72,
    "usability": 80
  },
  "critical_gaps_count": 3,
  "high_gaps_count": 11,
  "gaps": [
    {
      "id": 1,
      "severity": "CRITICAL",
      "priority": "P0",
      "category": "security",
      "title": "Dependency vulnerabilities",
      "blocker": true
    }
  ]
}
```

**Quality Gate Decision Logic:**
```
Quality Gate Processing NFR Assessment:

1. Check Overall NFR Score:
   Score: 78.7% → Range: 75-89% → Status: PASS (Good)

2. Check Critical Gaps:
   Critical Gaps: 3
   Security Critical: 1 (dependency CVEs)
   Reliability Critical: 1 (circuit breakers)
   Scalability Critical: 1 (resource limits)

   Decision: Security critical gap is a BLOCKER
   → Downgrade quality gate to CONCERNS

3. Check Category Minimums:
   Security: 75% (≥50% threshold) ✅
   Reliability: 78% (≥50% threshold) ✅
   Performance: 82% (≥50% threshold) ✅

   All categories above minimums ✅

4. Final Quality Gate Decision:
   Status: CONCERNS
   Reasoning: Overall score is good (78.7%), but 3 critical gaps identified
   Merge: PERMITTED with conditions (fix P0 before release)
   Release: BLOCKED until P0 gaps resolved
```

---

## JSON Output Format

**Complete Skill Output Structure:**
```json
{
  "overall_nfr_score": 78.7,
  "overall_status": "PASS",
  "category_scores": {
    "security": {
      "score": 75,
      "status": "CONCERNS",
      "criteria_evaluated": 10,
      "criteria_pass": 6,
      "criteria_concerns": 3,
      "criteria_fail": 1,
      "critical_gaps": 1,
      "high_gaps": 2,
      "medium_gaps": 1
    },
    "performance": {
      "score": 82,
      "status": "PASS",
      "criteria_evaluated": 10,
      "criteria_pass": 7,
      "criteria_concerns": 2,
      "criteria_fail": 0,
      "critical_gaps": 0,
      "high_gaps": 2,
      "p95_latency_ms": 120,
      "throughput_req_per_sec": 850
    },
    "reliability": {
      "score": 78,
      "status": "PASS",
      "criteria_evaluated": 10,
      "criteria_pass": 6,
      "criteria_concerns": 3,
      "criteria_fail": 1,
      "critical_gaps": 1,
      "high_gaps": 2
    },
    "maintainability": {
      "score": 85,
      "status": "PASS",
      "criteria_evaluated": 10,
      "criteria_pass": 8,
      "criteria_concerns": 2,
      "criteria_fail": 0,
      "test_coverage_percent": 87.5,
      "avg_complexity": 4.2,
      "high_gaps": 2
    },
    "scalability": {
      "score": 72,
      "status": "CONCERNS",
      "criteria_evaluated": 10,
      "criteria_pass": 5,
      "criteria_concerns": 3,
      "criteria_fail": 1,
      "critical_gaps": 1,
      "high_gaps": 3
    },
    "usability": {
      "score": 80,
      "status": "PASS",
      "criteria_evaluated": 10,
      "criteria_pass": 7,
      "criteria_concerns": 2,
      "criteria_fail": 1,
      "medium_gaps": 3
    }
  },
  "critical_gaps_count": 3,
  "high_gaps_count": 11,
  "medium_gaps_count": 4,
  "gaps": [
    {
      "id": 1,
      "category": "security",
      "severity": "CRITICAL",
      "priority": "P0",
      "title": "Dependency Vulnerabilities - jsonwebtoken@8.5.1",
      "description": "Outdated JWT library with 2 moderate CVEs",
      "impact": "Potential token forgery vulnerability",
      "remediation": "Upgrade to jsonwebtoken@9.0.2 or later",
      "file": "package.json",
      "line": 23,
      "estimated_time_hours": 0.25,
      "blocker": true
    }
  ],
  "quality_gate_impact": "CONCERNS",
  "quality_gate_reasoning": "Overall score is good (78.7%), but 3 critical gaps require resolution before production release. Security and scalability categories have concerns.",
  "report_path": ".claude/quality/assessments/task-auth-007-nfr-20251030.md",
  "telemetry": {
    "skill": "nfr-assess",
    "task_id": "task-auth-007",
    "overall_nfr_score": 78.7,
    "overall_status": "PASS",
    "security_score": 75,
    "performance_score": 82,
    "reliability_score": 78,
    "maintainability_score": 85,
    "scalability_score": 72,
    "usability_score": 80,
    "critical_gaps_count": 3,
    "high_gaps_count": 11,
    "automated_checks_run": ["npm_audit", "semgrep", "eslint", "jest_coverage"],
    "assessment_duration_ms": 525000,
    "timestamp": "2025-10-30T14:45:23.456Z"
  }
}
```

---

*Complete templates and output formats for nfr-assess skill*
