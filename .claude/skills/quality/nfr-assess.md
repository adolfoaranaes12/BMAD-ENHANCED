# Skill: Non-Functional Requirements Assessment

## Metadata

**Skill Name:** nfr-assess
**Version:** 1.0
**Category:** Quality
**Purpose:** Assess non-functional requirements (NFRs) including security, performance, reliability, maintainability, scalability, and usability with measurable criteria and evidence-based evaluation
**Output:** `.claude/quality/assessments/{task-id}-nfr-{YYYYMMDD}.md`

---

## Overview

This skill performs **comprehensive Non-Functional Requirements (NFR) assessment** to ensure the implementation meets quality attributes beyond functional correctness. NFRs are cross-cutting concerns that determine system quality, reliability, and long-term viability.

**Key Capabilities:**
- Multi-dimensional NFR assessment across 6 categories
- Measurable criteria with quantitative thresholds
- Evidence-based evaluation with code/config references
- Gap identification with severity ratings
- Integration with risk profile and traceability
- Compliance validation (OWASP, WCAG, performance budgets)
- Automated checks where possible (linting, security scans)
- Actionable recommendations with implementation guidance

**NFR Categories:**
1. **Security**: Authentication, authorization, encryption, input validation, dependency vulnerabilities
2. **Performance**: Response times, throughput, resource usage, caching, optimization
3. **Reliability**: Error handling, fault tolerance, recovery, monitoring, logging
4. **Maintainability**: Code quality, documentation, testability, modularity, technical debt
5. **Scalability**: Horizontal/vertical scaling, load handling, database design, caching strategy
6. **Usability**: API design, error messages, documentation, accessibility (if UI)

**When to Use:**
- During implementation review to validate NFRs
- Before quality gate to ensure comprehensive quality
- After functional testing to assess non-functional aspects
- When preparing for production deployment
- During architectural review for quality attributes

**Integration Points:**
- Reads task specification for NFR requirements
- Reads risk profile for security/performance risks
- Reads traceability matrix for implementation evidence
- Executes automated checks (linting, security scans, performance tests)
- Reads architecture documentation for design patterns
- Generates compliance reports for audit

---

## Execution Process

This skill executes **sequentially** through 8 steps. Each step must complete successfully before proceeding to the next. If any halt condition is met, execution stops and the user is informed.

### Halt Conditions
- Task specification file not found or invalid
- Cannot read implementation files
- Output directory not writable
- Critical NFR failures with no mitigation plan (advisory only, does not halt)

---

## Step 0: Load Configuration and Context

**Purpose:** Load project configuration, task specification, and all relevant context for NFR assessment.

**Actions:**

1. **Load Project Configuration**
   ```yaml
   # Read .claude/config.yaml
   quality:
     qualityLocation: .claude/quality
     riskScoreThreshold: 6

   nfr:
     # Optional NFR thresholds
     security:
       vulnerabilityScanRequired: true
       maxCriticalVulns: 0
       maxHighVulns: 2
     performance:
       maxResponseTime: 500ms
       minThroughput: 100 req/s
       maxMemoryUsage: 512MB
     maintainability:
       minTestCoverage: 80%
       maxCyclomaticComplexity: 10
       maxFunctionLength: 50
   ```

2. **Load Task Specification**
   ```bash
   TASK_FILE=".claude/tasks/{task-id}-{slug}.md"
   ```
   Extract:
   - Task ID, title, type
   - Objective and context
   - **NFR requirements** (explicit or implicit)
   - Acceptance criteria (may include NFRs)
   - Implementation Record
   - Architecture context

3. **Load Related Assessments** (if available)
   ```bash
   RISK_FILE=".claude/quality/assessments/{task-id}-risk-{date}.md"
   TRACE_FILE=".claude/quality/assessments/{task-id}-trace-{date}.md"
   TEST_FILE=".claude/quality/assessments/{task-id}-test-design-{date}.md"
   ```
   - Risk profile: Security/performance risks
   - Traceability: Implementation evidence
   - Test design: Performance/load tests

4. **Identify Implementation Files**
   From Implementation Record:
   - Source code files
   - Configuration files
   - Infrastructure files (Dockerfile, docker-compose, etc.)
   - Dependency files (package.json, requirements.txt, etc.)

5. **Identify Relevant NFR Categories**
   Based on task type and context:
   ```typescript
   // Example: API endpoint task
   Relevant NFRs:
     - Security (HIGH): Auth, input validation, rate limiting
     - Performance (HIGH): Response time, caching
     - Reliability (MEDIUM): Error handling, logging
     - Maintainability (MEDIUM): Code quality, tests
     - Scalability (LOW): Not critical for single endpoint
     - Usability (MEDIUM): Error messages, API docs
   ```

6. **Prepare Automated Checks**
   ```bash
   # Security scan
   npm audit --json > security-audit.json

   # Code quality (if applicable)
   npm run lint --format json > lint-report.json

   # Test coverage (if applicable)
   npm run test:coverage --json > coverage.json

   # Performance tests (if available)
   npm run test:perf --json > perf-results.json
   ```

7. **Prepare Output**
   ```bash
   OUTPUT_DIR="{qualityLocation}/assessments"
   OUTPUT_FILE="{task-id}-nfr-{YYYYMMDD}.md"
   TEMPLATE=".claude/templates/nfr-assessment.md"
   ```

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
✓ Relevant NFR categories: {categories}
✓ Automated checks: {checks available}
✓ Output: {output-file}
```

---

## Step 1: Security Assessment

**Purpose:** Evaluate security posture including authentication, authorization, input validation, dependency vulnerabilities, and security best practices.

**Actions:**

1. **Define Security Criteria:**
   ```markdown
   Security Criteria:
   1. Authentication: Proper auth mechanism (JWT, OAuth, session)
   2. Authorization: Role-based access control, permission checks
   3. Input Validation: All inputs validated and sanitized
   4. Output Encoding: Prevent XSS, SQL injection
   5. Dependency Security: No critical/high vulnerabilities
   6. Secrets Management: No hardcoded secrets, env vars used
   7. HTTPS/TLS: Secure communication enforced
   8. Rate Limiting: Protection against brute force
   9. CORS: Proper CORS configuration
   10. Security Headers: CSP, HSTS, X-Frame-Options, etc.
   ```

2. **Run Automated Security Checks:**
   ```bash
   # Dependency vulnerability scan
   npm audit --json

   # Code security scan (if tool available)
   semgrep --config=auto --json

   # Secret detection
   git secrets --scan || truffleHog
   ```

3. **Manual Code Review for Security:**
   - Search for authentication/authorization code
   - Check input validation (Zod, Joi, class-validator)
   - Check for SQL injection risks (parameterized queries?)
   - Check for XSS risks (output encoding?)
   - Check for hardcoded secrets (API keys, passwords)
   - Check CORS configuration
   - Check rate limiting implementation

4. **Evidence Collection:**
   ```markdown
   ## Security Evidence

   ### Authentication ✅ PASS
   - **Criterion:** Proper authentication mechanism
   - **Evidence:**
     - File: src/middleware/auth.ts:15-30
     - Implementation: JWT-based authentication with bcrypt password hashing
     - Code:
       ```typescript
       export const authenticateToken = (req, res, next) => {
         const token = req.headers['authorization']?.split(' ')[1];
         if (!token) return res.sendStatus(401);
         jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
           if (err) return res.sendStatus(403);
           req.user = user;
           next();
         });
       };
       ```
   - **Status:** PASS
   - **Notes:** JWT secret stored in environment variable (good practice)

   ### Input Validation ⚠️ CONCERNS
   - **Criterion:** All inputs validated and sanitized
   - **Evidence:**
     - File: src/validators/auth.ts:10-25
     - Implementation: Zod schema validation for email and password
     - Code:
       ```typescript
       export const signupSchema = z.object({
         email: z.string().email(),
         password: z.string().min(8)
       });
       ```
   - **Status:** CONCERNS
   - **Gap:** No validation for special characters, SQL keywords, XSS payloads
   - **Risk:** SQL injection, XSS attacks possible
   - **Recommendation:** Add sanitization: `z.string().email().transform(sanitize)`

   ### Dependency Vulnerabilities ❌ FAIL
   - **Criterion:** No critical/high vulnerabilities in dependencies
   - **Evidence:**
     - Audit: npm audit (run: {date})
     - Results: 3 critical, 5 high, 12 moderate vulnerabilities
     - Critical:
       1. lodash@4.17.15 - Prototype Pollution (CVE-2020-8203)
       2. express@4.16.0 - DoS vulnerability (CVE-2019-5476)
       3. jsonwebtoken@8.5.0 - Signature verification bypass (CVE-2022-23529)
   - **Status:** FAIL
   - **Risk:** Critical security vulnerabilities expose application to attacks
   - **Recommendation:** Update dependencies immediately:
     ```bash
     npm update lodash express jsonwebtoken
     npm audit fix --force
     ```
   ```

5. **Security Assessment Scoring:**
   ```
   For each criterion:
   - ✅ PASS: Criterion met, evidence strong
   - ⚠️ CONCERNS: Criterion partially met, some gaps
   - ❌ FAIL: Criterion not met, critical issue
   - ❓ UNCLEAR: Insufficient evidence to assess

   Overall Security Score = (PASS × 100 + CONCERNS × 50 + FAIL × 0) / Total Criteria

   Example:
   - 6 PASS, 2 CONCERNS, 2 FAIL, 0 UNCLEAR
   - Score = (6×100 + 2×50 + 2×0) / 10 = 700/10 = 70%
   ```

6. **Security Gap Identification:**
   ```markdown
   Security Gaps:
   1. **GAP-SEC-1**: Dependency vulnerabilities (CRITICAL)
      - 3 critical vulnerabilities in dependencies
      - Action: Update dependencies, run npm audit fix
      - Priority: P0 (must fix before merge)

   2. **GAP-SEC-2**: Incomplete input validation (HIGH)
      - No sanitization for XSS/SQL injection
      - Action: Add input sanitization layer
      - Priority: P0 (security risk)

   3. **GAP-SEC-3**: Missing rate limiting (MEDIUM)
      - No rate limiting on login endpoint
      - Action: Add express-rate-limit middleware
      - Priority: P1 (should fix before release)
   ```

**Output Data Structure:**
```typescript
interface SecurityAssessment {
  overallScore: number;              // 0-100
  status: 'PASS' | 'CONCERNS' | 'FAIL';
  criteria: {
    name: string;                    // "Authentication"
    status: 'PASS' | 'CONCERNS' | 'FAIL' | 'UNCLEAR';
    evidence: {
      file?: string;
      lines?: string;
      description: string;
      code?: string;
    }[];
    gaps?: string[];
    recommendations?: string[];
  }[];
  automatedChecks: {
    vulnerabilityScan: {
      critical: number;
      high: number;
      moderate: number;
      low: number;
    };
    secretDetection: {
      secretsFound: number;
      files: string[];
    };
  };
  gaps: CoverageGap[];              // Reuse gap structure from traceability
}
```

**Output:**
```
✓ Security assessment complete
✓ Overall Security Score: {score}%
✓ Status: {PASS/CONCERNS/FAIL}
✓ Criteria Evaluated: {count}
✓ Critical Gaps: {count}
✓ Automated Checks: {checks run}
```

---

## Step 2: Performance Assessment

**Purpose:** Evaluate performance characteristics including response times, throughput, resource usage, caching, and optimization.

**Actions:**

1. **Define Performance Criteria:**
   ```markdown
   Performance Criteria:
   1. Response Time: API endpoints respond within threshold (default: 500ms p95)
   2. Throughput: System handles expected load (default: 100 req/s)
   3. Resource Usage: Memory/CPU within limits (default: <512MB, <50% CPU)
   4. Database Queries: Optimized queries, proper indexing, N+1 avoided
   5. Caching: Appropriate caching strategy (Redis, in-memory, CDN)
   6. Asset Optimization: Minification, compression, lazy loading (if UI)
   7. Algorithm Complexity: O(n log n) or better for hot paths
   8. Connection Pooling: Database connection pooling configured
   9. Async Operations: Non-blocking I/O for expensive operations
   10. Load Testing: Performance validated under expected load
   ```

2. **Run Automated Performance Checks:**
   ```bash
   # Performance tests (if available)
   npm run test:perf

   # Load tests (if available)
   artillery run load-test.yml

   # Bundle size analysis (if UI)
   npm run build -- --analyze

   # Database query analysis
   EXPLAIN ANALYZE queries
   ```

3. **Manual Code Review for Performance:**
   - Check database queries for N+1 problems
   - Check for blocking operations in request handlers
   - Check algorithm complexity in hot paths
   - Check caching implementation
   - Check connection pooling configuration
   - Check for synchronous file I/O
   - Check for memory leaks (event listeners, closures)

4. **Evidence Collection:**
   ```markdown
   ## Performance Evidence

   ### Response Time ✅ PASS
   - **Criterion:** API endpoints respond within 500ms (p95)
   - **Evidence:**
     - Test: Performance test suite (src/__tests__/performance/)
     - Results:
       - POST /api/auth/signup: 120ms avg, 200ms p95
       - POST /api/auth/login: 80ms avg, 150ms p95
       - GET /api/user/profile: 50ms avg, 100ms p95
     - All endpoints well below 500ms threshold
   - **Status:** PASS

   ### Database Queries ⚠️ CONCERNS
   - **Criterion:** Optimized queries, proper indexing, N+1 avoided
   - **Evidence:**
     - File: src/routes/user/profile.ts:25-40
     - Code:
       ```typescript
       export async function getProfile(req, res) {
         const user = await prisma.user.findUnique({
           where: { id: req.user.id },
           include: { posts: true }  // N+1 risk if posts include authors
         });
         return res.json(user);
       }
       ```
   - **Status:** CONCERNS
   - **Gap:** Potential N+1 query if posts include nested relations
   - **Recommendation:** Use `include: { posts: { include: { author: true } } }` with proper indexing

   ### Caching ❌ FAIL
   - **Criterion:** Appropriate caching strategy
   - **Evidence:** No caching implementation found
   - **Status:** FAIL
   - **Gap:** No caching for frequently accessed data (user profiles, static content)
   - **Impact:** Higher latency, increased database load, poor scalability
   - **Recommendation:** Implement Redis caching for:
     - User profiles (TTL: 5 minutes)
     - JWT token validation (TTL: token expiry)
     - Static API responses (TTL: 1 hour)
   ```

5. **Performance Benchmark Results:**
   ```markdown
   ## Load Test Results

   **Test Configuration:**
   - Tool: Artillery
   - Duration: 60 seconds
   - Ramp-up: 0 → 100 req/s over 10s
   - Sustained: 100 req/s for 50s

   **Results:**
   | Endpoint | Avg (ms) | p95 (ms) | p99 (ms) | Success Rate | Errors |
   |----------|----------|----------|----------|--------------|--------|
   | POST /api/auth/signup | 120 | 200 | 350 | 99.5% | 5/6000 |
   | POST /api/auth/login | 80 | 150 | 280 | 100% | 0/6000 |
   | GET /api/user/profile | 50 | 100 | 180 | 99.8% | 12/6000 |

   **Analysis:**
   - ✅ All endpoints meet p95 threshold (<500ms)
   - ✅ High success rate (>99%)
   - ⚠️ p99 latency elevated (possible database contention)
   - ⚠️ 17 total errors (investigate timeout/connection issues)
   ```

6. **Performance Assessment Scoring:**
   Same as security: PASS/CONCERNS/FAIL for each criterion, compute overall score.

7. **Performance Gap Identification:**
   ```markdown
   Performance Gaps:
   1. **GAP-PERF-1**: No caching implementation (HIGH)
      - Impact: Poor scalability, high database load
      - Action: Implement Redis caching layer
      - Priority: P1 (should fix before release)

   2. **GAP-PERF-2**: Potential N+1 queries (MEDIUM)
      - Impact: Increased latency under load
      - Action: Review and optimize Prisma includes
      - Priority: P1 (performance optimization)
   ```

**Output:**
```
✓ Performance assessment complete
✓ Overall Performance Score: {score}%
✓ Status: {PASS/CONCERNS/FAIL}
✓ Response Time (p95): {avg_p95}ms (threshold: {threshold}ms)
✓ Load Test: {success_rate}% success at {load} req/s
✓ Performance Gaps: {count}
```

---

## Step 3: Reliability Assessment

**Purpose:** Evaluate system reliability including error handling, fault tolerance, recovery, monitoring, and logging.

**Actions:**

1. **Define Reliability Criteria:**
   ```markdown
   Reliability Criteria:
   1. Error Handling: All errors caught and handled gracefully
   2. Input Validation: Invalid inputs rejected with clear errors
   3. Graceful Degradation: System remains functional when dependencies fail
   4. Retry Logic: Transient failures retried with exponential backoff
   5. Circuit Breakers: Failed services circuit-broken to prevent cascading
   6. Logging: Comprehensive logging for debugging (structured logs)
   7. Monitoring: Health checks, metrics, alerting configured
   8. Idempotency: Repeated requests don't cause data corruption
   9. Data Integrity: Transactions, constraints, validation ensure consistency
   10. Disaster Recovery: Backup, restore procedures documented
   ```

2. **Manual Code Review for Reliability:**
   - Check try-catch blocks in async operations
   - Check error response formatting
   - Check validation error handling
   - Check database transaction usage
   - Check logging implementation (winston, pino, etc.)
   - Check health check endpoints
   - Check monitoring integration (Prometheus, Datadog, etc.)

3. **Evidence Collection:**
   ```markdown
   ## Reliability Evidence

   ### Error Handling ✅ PASS
   - **Criterion:** All errors caught and handled gracefully
   - **Evidence:**
     - File: src/middleware/errorHandler.ts:5-30
     - Implementation: Global error handler with proper status codes
     - Code:
       ```typescript
       export const errorHandler = (err, req, res, next) => {
         logger.error('Request error', { error: err, path: req.path });

         if (err instanceof ValidationError) {
           return res.status(400).json({ error: err.message, details: err.details });
         }

         if (err instanceof AuthError) {
           return res.status(401).json({ error: 'Unauthorized' });
         }

         // Generic 500 error
         res.status(500).json({ error: 'Internal server error' });
       };
       ```
   - **Status:** PASS
   - **Notes:** Comprehensive error handling with proper logging

   ### Logging ⚠️ CONCERNS
   - **Criterion:** Comprehensive structured logging
   - **Evidence:**
     - File: src/utils/logger.ts:1-15
     - Implementation: Winston logger with console transport
     - Code:
       ```typescript
       export const logger = winston.createLogger({
         level: 'info',
         format: winston.format.json(),
         transports: [new winston.transports.Console()]
       });
       ```
   - **Status:** CONCERNS
   - **Gap:** No log aggregation (ELK, CloudWatch, etc.), only console logs
   - **Impact:** Difficult to debug production issues
   - **Recommendation:** Add log aggregation transport, implement request ID tracking

   ### Monitoring ❌ FAIL
   - **Criterion:** Health checks, metrics, alerting configured
   - **Evidence:** No monitoring implementation found
   - **Status:** FAIL
   - **Gap:** No health check endpoint, no metrics collection, no alerting
   - **Impact:** Cannot detect issues in production, no observability
   - **Recommendation:**
     1. Add health check endpoint: GET /health
     2. Integrate metrics: Prometheus client
     3. Add request tracking: express-prometheus-middleware
     4. Configure alerting: Alert when error rate >1% or latency >1s
   ```

4. **Reliability Assessment Scoring:**
   Same as previous: PASS/CONCERNS/FAIL per criterion.

5. **Reliability Gap Identification:**
   ```markdown
   Reliability Gaps:
   1. **GAP-REL-1**: No monitoring/observability (CRITICAL)
      - Impact: Cannot detect production issues
      - Action: Add health checks, metrics, alerting
      - Priority: P0 (required for production)

   2. **GAP-REL-2**: No log aggregation (HIGH)
      - Impact: Difficult to debug production issues
      - Action: Add CloudWatch/ELK transport to logger
      - Priority: P1 (operational requirement)
   ```

**Output:**
```
✓ Reliability assessment complete
✓ Overall Reliability Score: {score}%
✓ Status: {PASS/CONCERNS/FAIL}
✓ Error Handling: {status}
✓ Logging: {status}
✓ Monitoring: {status}
✓ Reliability Gaps: {count}
```

---

## Step 4: Maintainability Assessment

**Purpose:** Evaluate code maintainability including code quality, documentation, testability, modularity, and technical debt.

**Actions:**

1. **Define Maintainability Criteria:**
   ```markdown
   Maintainability Criteria:
   1. Code Quality: Linting passing, no code smells
   2. Test Coverage: ≥80% line coverage, ≥90% on critical paths
   3. Documentation: README, API docs, inline comments for complex logic
   4. Modularity: Single Responsibility Principle, loose coupling
   5. Naming: Clear, descriptive names for variables/functions/classes
   6. Complexity: Cyclomatic complexity ≤10, function length ≤50 lines
   7. Duplication: DRY principle, minimal code duplication
   8. Type Safety: TypeScript strict mode, no `any` types
   9. Dependencies: Minimal dependencies, up-to-date versions
   10. Technical Debt: No TODO/FIXME without tracking tickets
   ```

2. **Run Automated Maintainability Checks:**
   ```bash
   # Linting
   npm run lint

   # Test coverage
   npm run test:coverage

   # Complexity analysis
   npx complexity-report src/

   # Duplication detection
   npx jscpd src/

   # Type checking
   npx tsc --noEmit
   ```

3. **Manual Code Review for Maintainability:**
   - Check code structure and organization
   - Check naming conventions
   - Check function/class sizes
   - Check documentation completeness
   - Check for code duplication
   - Check TypeScript usage (`any` types, proper interfaces)
   - Check for technical debt (TODO/FIXME comments)

4. **Evidence Collection:**
   ```markdown
   ## Maintainability Evidence

   ### Test Coverage ✅ PASS
   - **Criterion:** ≥80% line coverage, ≥90% critical paths
   - **Evidence:**
     - Report: coverage/lcov-report/index.html
     - Results:
       - Statements: 85% (170/200)
       - Branches: 82% (45/55)
       - Functions: 90% (18/20)
       - Lines: 85% (165/194)
     - Critical paths: 95% coverage (auth, validation)
   - **Status:** PASS

   ### Code Complexity ⚠️ CONCERNS
   - **Criterion:** Cyclomatic complexity ≤10
   - **Evidence:**
     - Tool: complexity-report
     - Results:
       - Average complexity: 4.2 (GOOD)
       - Max complexity: 15 (in src/routes/user/profile.ts:getUserProfile)
       - Functions >10: 2 functions
   - **Status:** CONCERNS
   - **Gap:** 2 functions exceed complexity threshold
   - **Recommendation:** Refactor getUserProfile() and updateUserSettings() to reduce complexity

   ### Documentation ❌ FAIL
   - **Criterion:** README, API docs, inline comments
   - **Evidence:**
     - README.md: Missing (file not found)
     - API docs: None (no OpenAPI/Swagger spec)
     - Inline comments: Sparse (10% of functions documented)
   - **Status:** FAIL
   - **Gap:** No project documentation, no API documentation
   - **Impact:** Difficult for new developers to onboard, API consumers lack documentation
   - **Recommendation:**
     1. Create README.md with setup instructions
     2. Generate OpenAPI spec from route definitions
     3. Add JSDoc comments to public functions
   ```

5. **Maintainability Assessment Scoring:**
   Same scoring system.

6. **Maintainability Gap Identification:**
   ```markdown
   Maintainability Gaps:
   1. **GAP-MAINT-1**: Missing documentation (HIGH)
      - Impact: Poor developer experience, slow onboarding
      - Action: Create README, API docs, JSDoc comments
      - Priority: P1 (should have before release)

   2. **GAP-MAINT-2**: High complexity functions (MEDIUM)
      - Impact: Difficult to maintain, test, debug
      - Action: Refactor 2 functions to reduce complexity
      - Priority: P2 (technical debt)
   ```

**Output:**
```
✓ Maintainability assessment complete
✓ Overall Maintainability Score: {score}%
✓ Test Coverage: {coverage}%
✓ Avg Complexity: {avg_complexity}
✓ Linting: {pass/fail}
✓ Maintainability Gaps: {count}
```

---

## Step 5: Scalability Assessment

**Purpose:** Evaluate system scalability including horizontal/vertical scaling, load handling, database design, and caching strategy.

**Actions:**

1. **Define Scalability Criteria:**
   ```markdown
   Scalability Criteria:
   1. Stateless Design: No server-side state (or external session store)
   2. Horizontal Scaling: Can add more instances to increase capacity
   3. Database Design: Normalized schema, proper indexing, sharding-ready
   4. Connection Pooling: Database connection pool configured properly
   5. Caching: Multi-tier caching (in-memory, Redis, CDN)
   6. Async Processing: Background jobs for expensive operations (queues)
   7. Rate Limiting: Per-user/IP rate limits to prevent abuse
   8. Load Balancing: Ready for load balancer (health checks, graceful shutdown)
   9. Resource Limits: Memory/CPU limits configured
   10. Auto-scaling: Metrics-based auto-scaling configured (if cloud)
   ```

2. **Review Architecture for Scalability:**
   - Check if application is stateless
   - Check database schema and indexing
   - Check for in-memory state (should use Redis/external store)
   - Check for file uploads (should use object storage like S3)
   - Check for background job processing (should use queue)
   - Check for proper shutdown handlers

3. **Evidence Collection:**
   ```markdown
   ## Scalability Evidence

   ### Stateless Design ✅ PASS
   - **Criterion:** No server-side state
   - **Evidence:**
     - Auth: JWT tokens (stateless)
     - Sessions: None (JWT-based)
     - File uploads: Stored in S3 (not local disk)
   - **Status:** PASS
   - **Notes:** Application is fully stateless, can scale horizontally

   ### Database Design ⚠️ CONCERNS
   - **Criterion:** Normalized schema, proper indexing
   - **Evidence:**
     - File: prisma/schema.prisma
     - Indexes: 3 indexes defined (email, userId, createdAt)
     - Analysis:
       - User.email: Indexed (GOOD)
       - Post.userId: Not indexed (CONCERN - frequent joins)
       - Post.createdAt: Indexed (GOOD)
   - **Status:** CONCERNS
   - **Gap:** Missing index on frequently queried foreign keys
   - **Recommendation:** Add index on Post.userId:
     ```prisma
     model Post {
       id Int @id @default(autoincrement())
       userId Int
       user User @relation(fields: [userId], references: [id])
       @@index([userId])
     }
     ```

   ### Async Processing ❌ FAIL
   - **Criterion:** Background jobs for expensive operations
   - **Evidence:** No queue/job system implemented
   - **Status:** FAIL
   - **Gap:** Email sending, report generation done synchronously
   - **Impact:** Request handlers blocked by expensive I/O, poor scalability
   - **Recommendation:** Implement Bull/BullMQ with Redis:
     ```typescript
     // Queue email sending
     await emailQueue.add('sendWelcome', { userId: user.id });
     ```
   ```

4. **Scalability Assessment Scoring:**
   Same scoring system.

5. **Scalability Gap Identification:**
   ```markdown
   Scalability Gaps:
   1. **GAP-SCALE-1**: No async job processing (HIGH)
      - Impact: Poor scalability, request timeouts
      - Action: Implement Bull queue with Redis
      - Priority: P1 (required for scale)

   2. **GAP-SCALE-2**: Missing database indexes (MEDIUM)
      - Impact: Slow queries under load
      - Action: Add indexes on foreign keys
      - Priority: P1 (performance at scale)
   ```

**Output:**
```
✓ Scalability assessment complete
✓ Overall Scalability Score: {score}%
✓ Stateless Design: {status}
✓ Database Indexing: {status}
✓ Async Processing: {status}
✓ Scalability Gaps: {count}
```

---

## Step 6: Usability Assessment

**Purpose:** Evaluate system usability including API design, error messages, documentation, and accessibility (if UI).

**Actions:**

1. **Define Usability Criteria:**
   ```markdown
   Usability Criteria (API):
   1. API Design: RESTful conventions, consistent resource naming
   2. Error Messages: Clear, actionable error messages with details
   3. Documentation: OpenAPI/Swagger spec, usage examples
   4. Versioning: API versioning strategy (v1, v2, etc.)
   5. Pagination: Consistent pagination for list endpoints
   6. Filtering: Query parameters for filtering/sorting
   7. HTTP Status Codes: Proper status codes (200, 400, 404, 500, etc.)
   8. Response Format: Consistent JSON structure
   9. HATEOAS: Hypermedia links for navigation (optional)
   10. Developer Experience: Easy to use, intuitive, well-documented

   Usability Criteria (UI, if applicable):
   1. Accessibility: WCAG 2.1 AA compliance
   2. Responsive Design: Mobile, tablet, desktop support
   3. Loading States: Feedback for async operations
   4. Error Handling: User-friendly error messages
   5. Keyboard Navigation: Full keyboard support
   ```

2. **Review API Design:**
   - Check REST conventions (GET, POST, PUT, DELETE)
   - Check resource naming (plural nouns: /users, /posts)
   - Check error response format
   - Check HTTP status code usage
   - Check pagination implementation
   - Check API documentation (OpenAPI spec)

3. **Evidence Collection:**
   ```markdown
   ## Usability Evidence

   ### API Design ✅ PASS
   - **Criterion:** RESTful conventions, consistent naming
   - **Evidence:**
     - Routes:
       - POST /api/auth/signup (create user)
       - POST /api/auth/login (authenticate)
       - GET /api/users/:id (get user)
       - PUT /api/users/:id (update user)
       - DELETE /api/users/:id (delete user)
     - Conventions: RESTful, proper HTTP verbs, consistent /api prefix
   - **Status:** PASS

   ### Error Messages ⚠️ CONCERNS
   - **Criterion:** Clear, actionable error messages
   - **Evidence:**
     - Example error:
       ```json
       { "error": "Invalid input" }
       ```
   - **Status:** CONCERNS
   - **Gap:** Generic error messages, no field-specific details
   - **Recommendation:** Provide detailed validation errors:
     ```json
     {
       "error": "Validation failed",
       "details": [
         { "field": "email", "message": "Must be a valid email address" },
         { "field": "password", "message": "Must be at least 8 characters" }
       ]
     }
     ```

   ### Documentation ❌ FAIL
   - **Criterion:** OpenAPI/Swagger spec
   - **Evidence:** No API documentation found
   - **Status:** FAIL
   - **Gap:** No OpenAPI spec, no usage examples
   - **Impact:** Difficult for API consumers to integrate
   - **Recommendation:** Generate OpenAPI spec using tsoa or swagger-jsdoc
   ```

4. **Usability Assessment Scoring:**
   Same scoring system.

5. **Usability Gap Identification:**
   ```markdown
   Usability Gaps:
   1. **GAP-USE-1**: Missing API documentation (HIGH)
      - Impact: Poor developer experience
      - Action: Generate OpenAPI spec
      - Priority: P1 (should have for API)

   2. **GAP-USE-2**: Generic error messages (MEDIUM)
      - Impact: Difficult to debug for API consumers
      - Action: Enhance error responses with field details
      - Priority: P2 (nice to have)
   ```

**Output:**
```
✓ Usability assessment complete
✓ Overall Usability Score: {score}%
✓ API Design: {status}
✓ Error Messages: {status}
✓ Documentation: {status}
✓ Usability Gaps: {count}
```

---

## Step 7: Generate NFR Assessment Report

**Purpose:** Create comprehensive NFR assessment report using template.

**Actions:**

1. **Load Template:**
   ```bash
   TEMPLATE=".claude/templates/nfr-assessment.md"
   ```

2. **Compute Overall NFR Score:**
   ```
   Overall NFR Score = (
     Security Score × 0.25 +
     Performance Score × 0.20 +
     Reliability Score × 0.20 +
     Maintainability Score × 0.15 +
     Scalability Score × 0.10 +
     Usability Score × 0.10
   )

   Example:
   - Security: 70%
   - Performance: 80%
   - Reliability: 60%
   - Maintainability: 75%
   - Scalability: 70%
   - Usability: 65%

   Overall = (70×0.25) + (80×0.20) + (60×0.20) + (75×0.15) + (70×0.10) + (65×0.10)
          = 17.5 + 16 + 12 + 11.25 + 7 + 6.5
          = 70.25%
   ```

3. **Determine Overall NFR Status:**
   ```
   Overall NFR Status:
   - ≥90%: PASS (Excellent)
   - 75-89%: PASS (Good)
   - 60-74%: CONCERNS (Needs improvement)
   - <60%: FAIL (Critical issues)

   Individual Category Status:
   - <50%: FAIL (blocks quality gate)
   - 50-74%: CONCERNS (significant gaps)
   - ≥75%: PASS (acceptable)
   ```

4. **Populate Template:**
   Replace all template variables with assessment data from Steps 1-6.

5. **Generate Full Report:**
   Write to output file with all sections populated.

**Output:**
```
✓ NFR assessment report generated
✓ Output: .claude/quality/assessments/{task-id}-nfr-{date}.md
✓ Overall NFR Score: {score}% ({status})
✓ Report size: {lines} lines
```

---

## Step 8: Present Summary to User

**Purpose:** Provide concise summary with key metrics and next steps.

**Actions:**

1. **Display Summary:**
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Non-Functional Requirements Assessment Complete
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Task: task-007 - User Authentication API
   Date: 2025-10-28

   📊 Overall NFR Score: 70% (CONCERNS)

   Category Scores:
   ├─ Security: 70% (CONCERNS) - 2 critical gaps
   ├─ Performance: 80% (PASS) - 1 high gap
   ├─ Reliability: 60% (CONCERNS) - 1 critical gap
   ├─ Maintainability: 75% (PASS) - 1 high gap
   ├─ Scalability: 70% (CONCERNS) - 1 high gap
   └─ Usability: 65% (CONCERNS) - 1 high gap

   ⚠️  Critical Gaps (P0 - Must Fix):
   1. GAP-SEC-1: Dependency vulnerabilities (3 critical CVEs)
   2. GAP-REL-1: No monitoring/observability

   🔴 High Gaps (P1 - Should Fix):
   3. GAP-SEC-2: Incomplete input sanitization
   4. GAP-PERF-1: No caching implementation
   5. GAP-MAINT-1: Missing documentation
   6. GAP-SCALE-1: No async job processing
   7. GAP-USE-1: Missing API documentation

   🎯 Quality Gate Impact: CONCERNS

   Reasoning:
   - 2 critical NFR gaps (security, reliability)
   - 5 high-severity gaps across multiple categories
   - Overall score 70% (below 75% threshold)
   - Security and reliability concerns block production readiness

   ✅ To Achieve PASS:
   1. Fix GAP-SEC-1: Update dependencies [30 min]
   2. Fix GAP-REL-1: Add monitoring/health checks [2-3h]
   3. Fix GAP-SEC-2: Add input sanitization [1-2h]
   4. Fix GAP-PERF-1: Implement caching layer [3-4h]

   Estimated effort: 7-10 hours

   📄 Full Report:
   .claude/quality/assessments/task-007-nfr-20251028.md

   💡 Next Steps:
   1. Review detailed NFR assessment in report
   2. Prioritize P0 gaps (before merge)
   3. Create tickets for P1 gaps
   4. Re-run nfr-assess after closing gaps
   5. Proceed to quality-gate skill when NFR score ≥75%

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

2. **Ask User:**
   ```
   Would you like me to:
   A) Show details of specific NFR category (security, performance, etc.)
   B) Generate implementation plan for closing gaps
   C) Re-run assessment after you close gaps
   D) Continue with next skill (quality-gate)
   ```

**Execution Complete.**

---

## Integration with Other Skills

### Integration with risk-profile.md

**Input from risk-profile:**
- Security risks → Inform security assessment severity
- Performance risks → Inform performance assessment priorities
- Reliability risks → Inform reliability criteria

**How NFR assessment uses it:**
```markdown
Risk Profile says:
  Risk #2: SQL injection (Score: 6, HIGH)

NFR Security Assessment finds:
  Input Validation: ⚠️ CONCERNS
  Gap: No sanitization for SQL injection

Gap Severity Calculation:
  Base: HIGH (security gap)
  Risk amplification: +1 (matches high-risk from risk profile)
  Final: CRITICAL (must fix before merge)
```

### Integration with trace-requirements.md

**Input from traceability:**
- Implementation evidence → Validate NFR implementation
- Test coverage → Validate NFR testing

**Output to traceability:**
- NFR gaps → Additional coverage gaps for traceability

### Integration with quality-gate.md

**Output to quality-gate:**
- Overall NFR score (contributes to gate decision)
- Category scores (security/performance/reliability)
- NFR gaps (may block gate if critical)
- Evidence for NFR section of quality gate

**How quality-gate uses it:**
```markdown
Quality Gate Decision:
1. Check overall NFR score:
   - ≥90%: PASS (excellent)
   - 75-89%: PASS (good)
   - 60-74%: CONCERNS (needs improvement)
   - <60%: FAIL (critical issues)

2. Check critical NFR gaps:
   - 0 critical: continue evaluation
   - 1+ critical in security/reliability: FAIL
   - 1+ critical in other categories: CONCERNS

3. Check individual category minimums:
   - Security <50%: FAIL (not production-ready)
   - Reliability <50%: FAIL (not production-ready)
   - Performance <50%: CONCERNS (may need optimization)
```

---

## Output Template Reference

The skill uses `.claude/templates/nfr-assessment.md` for report generation.

**Sections:**
1. Header: Task metadata
2. Executive Summary: Overall score, category scores, critical gaps
3. Security Assessment: Detailed security evaluation with evidence
4. Performance Assessment: Detailed performance evaluation with benchmarks
5. Reliability Assessment: Error handling, monitoring, logging
6. Maintainability Assessment: Code quality, documentation, technical debt
7. Scalability Assessment: Horizontal scaling, database design, async processing
8. Usability Assessment: API design, error messages, documentation
9. Gap Summary: All gaps across categories with priorities
10. Recommendations: Prioritized action plan
11. Quality Gate Impact: Predicted gate status

---

## Best Practices

1. **Run NFR assessment before quality gate** - Identifies issues early
2. **Integrate automated checks** - Leverage tools for objective metrics
3. **Document evidence** - File/line references for all assessments
4. **Prioritize security and reliability** - These are production blockers
5. **Set measurable thresholds** - Define clear pass/fail criteria
6. **Re-run after fixes** - Validate gap closure

---

## Skill Complete

This skill is now ready for use. To execute:

1. **Direct invocation** (when subagents built):
   ```
   @quinn *nfr task-007
   ```

2. **Manual invocation** (current):
   ```
   I'd like to run NFR assessment on task-007
   ```

---

<!-- End of Skill -->
