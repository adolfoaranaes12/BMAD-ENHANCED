# NFR Assessment Categories

This reference provides detailed assessment criteria for all 6 Non-Functional Requirement (NFR) categories used by the nfr-assess skill. Each category includes specific criteria, evaluation methodology, evidence requirements, and relevance guidelines based on task type.

---

## Table of Contents

1. [Security Assessment](#security-assessment)
2. [Performance Assessment](#performance-assessment)
3. [Reliability Assessment](#reliability-assessment)
4. [Maintainability Assessment](#maintainability-assessment)
5. [Scalability Assessment](#scalability-assessment)
6. [Usability Assessment](#usability-assessment)
7. [Category Relevance by Task Type](#category-relevance-by-task-type)

---

## Security Assessment

Security assessment evaluates the implementation's security posture across authentication, authorization, data protection, and vulnerability management.

### Security Criteria (10 criteria)

#### 1. Authentication
- **Definition:** Proper authentication mechanism implemented
- **Evidence Required:**
  - Authentication middleware/handler implementation
  - Password hashing mechanism (bcrypt, argon2, etc.)
  - Token generation/validation (JWT, OAuth, session)
  - Multi-factor authentication (if applicable)
- **Evaluation:**
  - ✅ PASS: Strong authentication with proper hashing, secure token handling
  - ⚠️ CONCERNS: Authentication present but weak configuration (short JWT expiry, weak hash rounds)
  - ❌ FAIL: No authentication or insecure implementation (plain text passwords, weak tokens)
  - ❓ UNCLEAR: Authentication code not found or unclear implementation

#### 2. Authorization
- **Definition:** Role-based access control and permission checks
- **Evidence Required:**
  - Authorization middleware implementation
  - Role/permission definitions
  - Protected route configuration
  - Permission checks in business logic
- **Evaluation:**
  - ✅ PASS: Comprehensive RBAC with proper permission checks
  - ⚠️ CONCERNS: Basic authorization but missing fine-grained permissions
  - ❌ FAIL: No authorization checks or easily bypassed
  - ❓ UNCLEAR: Authorization logic unclear

#### 3. Input Validation
- **Definition:** All inputs validated and sanitized to prevent injection attacks
- **Evidence Required:**
  - Input validation schema (Zod, Joi, class-validator, etc.)
  - Sanitization functions
  - Type checking (TypeScript strict mode)
  - Boundary validation (length, format, range)
- **Evaluation:**
  - ✅ PASS: Comprehensive validation with sanitization, covers all inputs
  - ⚠️ CONCERNS: Validation present but incomplete (missing some inputs, no sanitization)
  - ❌ FAIL: No input validation or easily bypassed
  - ❓ UNCLEAR: Validation implementation unclear

#### 4. Output Encoding
- **Definition:** Outputs properly encoded to prevent XSS and injection attacks
- **Evidence Required:**
  - Template engine with auto-escaping (if UI)
  - Content Security Policy headers
  - Output sanitization for user-generated content
  - Parameterized queries (SQL) or ORM usage
- **Evaluation:**
  - ✅ PASS: All outputs properly encoded, CSP configured
  - ⚠️ CONCERNS: Basic encoding but CSP missing or incomplete
  - ❌ FAIL: No output encoding, vulnerable to XSS
  - ❓ UNCLEAR: Output handling unclear

#### 5. Dependency Vulnerabilities
- **Definition:** No critical or high-severity vulnerabilities in dependencies
- **Evidence Required:**
  - Dependency scan results (npm audit, Snyk, etc.)
  - Vulnerability counts by severity
  - Specific CVEs identified
  - Dependency update status
- **Evaluation:**
  - ✅ PASS: 0 critical, 0-2 high vulnerabilities
  - ⚠️ CONCERNS: 0 critical, 3-5 high vulnerabilities
  - ❌ FAIL: 1+ critical or 6+ high vulnerabilities
  - ❓ UNCLEAR: Dependency scan not run or failed

#### 6. Secrets Management
- **Definition:** No hardcoded secrets, proper environment variable usage
- **Evidence Required:**
  - Secret detection scan results
  - Environment variable configuration
  - Secrets manager integration (AWS Secrets Manager, Vault, etc.)
  - `.env.example` file with placeholders
- **Evaluation:**
  - ✅ PASS: No hardcoded secrets, environment variables used, secrets manager integrated
  - ⚠️ CONCERNS: Environment variables used but no secrets manager
  - ❌ FAIL: Hardcoded secrets found (API keys, passwords, tokens)
  - ❓ UNCLEAR: Cannot verify secret handling

#### 7. HTTPS/TLS
- **Definition:** Secure communication enforced (HTTPS, TLS 1.2+)
- **Evidence Required:**
  - HTTPS redirect configuration
  - TLS certificate configuration
  - Secure cookie flags (Secure, HttpOnly, SameSite)
  - HSTS header configuration
- **Evaluation:**
  - ✅ PASS: HTTPS enforced, TLS 1.2+, secure cookies, HSTS enabled
  - ⚠️ CONCERNS: HTTPS available but not enforced, or missing secure cookie flags
  - ❌ FAIL: HTTP only, no TLS configuration
  - ❓ UNCLEAR: Communication security unclear (infra-level?)

#### 8. Rate Limiting
- **Definition:** Protection against brute force and DoS attacks
- **Evidence Required:**
  - Rate limiting middleware (express-rate-limit, etc.)
  - Rate limit configuration (requests per window)
  - Per-user or per-IP rate limiting
  - Rate limit response (429 status)
- **Evaluation:**
  - ✅ PASS: Rate limiting configured on authentication and sensitive endpoints
  - ⚠️ CONCERNS: Rate limiting on some endpoints but not comprehensive
  - ❌ FAIL: No rate limiting implemented
  - ❓ UNCLEAR: Rate limiting unclear (infra-level?)

#### 9. CORS Configuration
- **Definition:** Proper Cross-Origin Resource Sharing configuration
- **Evidence Required:**
  - CORS middleware configuration
  - Allowed origins whitelist
  - Allowed methods and headers
  - Credentials handling
- **Evaluation:**
  - ✅ PASS: CORS properly configured with whitelist, appropriate methods
  - ⚠️ CONCERNS: CORS configured but overly permissive (`*` allowed origins)
  - ❌ FAIL: No CORS configuration or completely open
  - ❓ UNCLEAR: CORS configuration unclear

#### 10. Security Headers
- **Definition:** Security headers configured (CSP, HSTS, X-Frame-Options, etc.)
- **Evidence Required:**
  - Security headers middleware (helmet.js, etc.)
  - CSP policy configuration
  - HSTS configuration
  - X-Frame-Options, X-Content-Type-Options headers
- **Evaluation:**
  - ✅ PASS: Comprehensive security headers including CSP
  - ⚠️ CONCERNS: Some security headers but CSP missing or weak
  - ❌ FAIL: No security headers configured
  - ❓ UNCLEAR: Headers unclear (infra-level?)

### Security Automated Checks

1. **Dependency Vulnerability Scan:**
   ```bash
   npm audit --json
   # or
   snyk test --json
   ```
   Extracts: Critical, High, Moderate, Low vulnerability counts

2. **Code Security Scan:**
   ```bash
   semgrep --config=auto --json
   ```
   Detects: Injection vulnerabilities, hardcoded secrets, insecure patterns

3. **Secret Detection:**
   ```bash
   truffleHog filesystem . --json
   # or
   git-secrets --scan
   ```
   Detects: Hardcoded API keys, passwords, tokens

---

## Performance Assessment

Performance assessment evaluates response times, throughput, resource usage, and optimization strategies.

### Performance Criteria (10 criteria)

#### 1. Response Time
- **Definition:** API endpoints respond within acceptable thresholds
- **Default Threshold:** p95 < 500ms
- **Evidence Required:**
  - Performance test results (average, p95, p99 latency)
  - Load test results under expected traffic
  - Endpoint-specific response times
- **Evaluation:**
  - ✅ PASS: All endpoints meet p95 threshold
  - ⚠️ CONCERNS: Most endpoints meet threshold, some outliers
  - ❌ FAIL: Multiple endpoints exceed threshold significantly (p95 > 1s)
  - ❓ UNCLEAR: No performance tests run

#### 2. Throughput
- **Definition:** System handles expected load (requests per second)
- **Default Threshold:** 100 req/s (adjust based on requirements)
- **Evidence Required:**
  - Load test results (requests per second, success rate)
  - Concurrent user handling
  - System saturation point
- **Evaluation:**
  - ✅ PASS: Meets or exceeds throughput requirements with >99% success rate
  - ⚠️ CONCERNS: Approaches throughput limit, some failures under load
  - ❌ FAIL: Cannot sustain required throughput, high failure rate
  - ❓ UNCLEAR: No load tests run

#### 3. Resource Usage
- **Definition:** Memory and CPU usage within acceptable limits
- **Default Thresholds:** Memory < 512MB, CPU < 50% under normal load
- **Evidence Required:**
  - Resource monitoring data (memory, CPU usage over time)
  - Memory leak detection results
  - Resource usage under load
- **Evaluation:**
  - ✅ PASS: Resources within limits, no memory leaks detected
  - ⚠️ CONCERNS: Resources approach limits or gradual memory growth
  - ❌ FAIL: Resources exceed limits, memory leaks detected, OOM crashes
  - ❓ UNCLEAR: No resource monitoring

#### 4. Database Queries
- **Definition:** Optimized queries, proper indexing, N+1 queries avoided
- **Evidence Required:**
  - Query analysis (EXPLAIN ANALYZE results)
  - Index definitions in schema
  - ORM query patterns (includes, joins)
  - Query execution times
- **Evaluation:**
  - ✅ PASS: All queries optimized, proper indexes, no N+1 issues
  - ⚠️ CONCERNS: Most queries optimized, some missing indexes or minor N+1
  - ❌ FAIL: Multiple unindexed queries, significant N+1 problems, slow queries
  - ❓ UNCLEAR: Cannot analyze queries

#### 5. Caching
- **Definition:** Appropriate caching strategy implemented
- **Evidence Required:**
  - Caching layer implementation (Redis, in-memory, CDN)
  - Cache configuration (TTL, invalidation strategy)
  - Cache hit rate metrics
  - Cached data types (user profiles, static content, etc.)
- **Evaluation:**
  - ✅ PASS: Multi-tier caching with proper TTL and invalidation
  - ⚠️ CONCERNS: Basic caching but missing some opportunities
  - ❌ FAIL: No caching implemented where appropriate
  - ❓ UNCLEAR: Caching unclear (infra-level?)

#### 6. Asset Optimization (UI applications)
- **Definition:** Minification, compression, lazy loading, code splitting
- **Evidence Required:**
  - Build configuration (minification, tree-shaking)
  - Bundle size analysis
  - Lazy loading implementation
  - Image optimization (WebP, responsive images)
  - CDN usage
- **Evaluation:**
  - ✅ PASS: Comprehensive optimization (minification, compression, code splitting)
  - ⚠️ CONCERNS: Basic optimization but large bundles or missing lazy loading
  - ❌ FAIL: No optimization, large bundles, slow initial load
  - ❓ UNCLEAR: Not applicable (non-UI) or unclear

#### 7. Algorithm Complexity
- **Definition:** Efficient algorithms in hot paths (O(n log n) or better)
- **Evidence Required:**
  - Algorithm analysis in performance-critical code
  - Complexity annotations
  - Profiling results showing hot paths
- **Evaluation:**
  - ✅ PASS: Efficient algorithms throughout, no O(n²) in hot paths
  - ⚠️ CONCERNS: Some inefficient algorithms in non-critical paths
  - ❌ FAIL: O(n²) or worse in hot paths, significant performance impact
  - ❓ UNCLEAR: Cannot determine complexity

#### 8. Connection Pooling
- **Definition:** Database connection pooling properly configured
- **Evidence Required:**
  - Connection pool configuration
  - Pool size settings (min, max connections)
  - Connection timeout settings
  - Connection pool monitoring
- **Evaluation:**
  - ✅ PASS: Connection pooling configured with appropriate pool size
  - ⚠️ CONCERNS: Connection pooling present but misconfigured (too small/large)
  - ❌ FAIL: No connection pooling, new connection per request
  - ❓ UNCLEAR: Connection pooling unclear (ORM default?)

#### 9. Async Operations
- **Definition:** Non-blocking I/O for expensive operations
- **Evidence Required:**
  - Async/await usage in request handlers
  - Promise-based I/O operations
  - No synchronous blocking calls (fs.readFileSync, etc.)
  - Background job queue for long operations
- **Evaluation:**
  - ✅ PASS: All I/O operations async, background jobs for expensive operations
  - ⚠️ CONCERNS: Mostly async but some blocking operations
  - ❌ FAIL: Synchronous blocking operations in request handlers
  - ❓ UNCLEAR: Cannot determine I/O patterns

#### 10. Load Testing
- **Definition:** Performance validated under expected load
- **Evidence Required:**
  - Load test configuration (ramp-up, sustained load, duration)
  - Load test results (latency, throughput, errors)
  - Stress test results (system breaking point)
- **Evaluation:**
  - ✅ PASS: Comprehensive load testing, system meets requirements under load
  - ⚠️ CONCERNS: Basic load testing but limited scenarios
  - ❌ FAIL: No load testing performed
  - ❓ UNCLEAR: Load testing results not available

### Performance Automated Checks

1. **Performance Tests:**
   ```bash
   npm run test:perf
   ```
   Measures: Response times, throughput, resource usage

2. **Load Tests:**
   ```bash
   artillery run load-test.yml --output results.json
   # or
   k6 run load-test.js --out json=results.json
   ```
   Measures: Latency (avg, p95, p99), throughput, success rate, errors

3. **Bundle Size Analysis (UI):**
   ```bash
   npm run build -- --analyze
   ```
   Measures: Bundle sizes, code splitting effectiveness

---

## Reliability Assessment

Reliability assessment evaluates error handling, fault tolerance, monitoring, and operational readiness.

### Reliability Criteria (10 criteria)

#### 1. Error Handling
- **Definition:** All errors caught and handled gracefully
- **Evidence Required:**
  - Try-catch blocks in async operations
  - Global error handler middleware
  - Error response formatting
  - Error logging
- **Evaluation:**
  - ✅ PASS: Comprehensive error handling, graceful degradation
  - ⚠️ CONCERNS: Error handling present but incomplete coverage
  - ❌ FAIL: Unhandled errors, application crashes
  - ❓ UNCLEAR: Error handling unclear

#### 2. Input Validation Errors
- **Definition:** Invalid inputs rejected with clear error messages
- **Evidence Required:**
  - Validation error handling
  - Clear error messages for validation failures
  - Proper HTTP status codes (400 Bad Request)
- **Evaluation:**
  - ✅ PASS: Validation errors handled with clear messages
  - ⚠️ CONCERNS: Validation errors handled but generic messages
  - ❌ FAIL: Validation errors unhandled or cryptic messages
  - ❓ UNCLEAR: Validation error handling unclear

#### 3. Graceful Degradation
- **Definition:** System remains functional when dependencies fail
- **Evidence Required:**
  - Fallback mechanisms for external dependencies
  - Circuit breaker implementation
  - Degraded mode operation
- **Evaluation:**
  - ✅ PASS: Graceful degradation with circuit breakers, fallback mechanisms
  - ⚠️ CONCERNS: Some fallback handling but not comprehensive
  - ❌ FAIL: System fails when dependencies fail, no fallback
  - ❓ UNCLEAR: Degradation handling unclear

#### 4. Retry Logic
- **Definition:** Transient failures retried with exponential backoff
- **Evidence Required:**
  - Retry implementation for external API calls
  - Exponential backoff configuration
  - Max retry limits
  - Idempotency considerations
- **Evaluation:**
  - ✅ PASS: Retry logic with exponential backoff, proper limits
  - ⚠️ CONCERNS: Retry logic present but no exponential backoff
  - ❌ FAIL: No retry logic, fails on first error
  - ❓ UNCLEAR: Retry logic unclear

#### 5. Circuit Breakers
- **Definition:** Failed services circuit-broken to prevent cascading failures
- **Evidence Required:**
  - Circuit breaker implementation (Resilience4j, opossum, etc.)
  - Circuit state management (closed, open, half-open)
  - Circuit breaker configuration (failure threshold, timeout)
- **Evaluation:**
  - ✅ PASS: Circuit breakers implemented for external dependencies
  - ⚠️ CONCERNS: Some circuit breaking but not comprehensive
  - ❌ FAIL: No circuit breakers, cascading failures possible
  - ❓ UNCLEAR: Circuit breaking unclear

#### 6. Logging
- **Definition:** Comprehensive structured logging for debugging
- **Evidence Required:**
  - Logging library (winston, pino, bunyan)
  - Structured log format (JSON)
  - Log levels (error, warn, info, debug)
  - Request ID tracking
  - Log aggregation (CloudWatch, ELK, Splunk)
- **Evaluation:**
  - ✅ PASS: Structured logging with aggregation, request tracking
  - ⚠️ CONCERNS: Basic logging but no aggregation or request tracking
  - ❌ FAIL: Console.log only, no structured logging
  - ❓ UNCLEAR: Logging unclear

#### 7. Monitoring
- **Definition:** Health checks, metrics, alerting configured
- **Evidence Required:**
  - Health check endpoint (/health, /healthz)
  - Metrics collection (Prometheus, Datadog, CloudWatch)
  - Application metrics (request rate, error rate, latency)
  - Business metrics (signups, orders, etc.)
  - Alerting rules configured
- **Evaluation:**
  - ✅ PASS: Comprehensive monitoring with health checks, metrics, alerting
  - ⚠️ CONCERNS: Basic health checks but limited metrics or no alerting
  - ❌ FAIL: No monitoring, health checks, or metrics
  - ❓ UNCLEAR: Monitoring unclear (infra-level?)

#### 8. Idempotency
- **Definition:** Repeated requests don't cause data corruption
- **Evidence Required:**
  - Idempotency key handling
  - Database constraints (unique indexes)
  - Transaction usage for multi-step operations
  - Idempotent operation design
- **Evaluation:**
  - ✅ PASS: Idempotency guaranteed through keys and transactions
  - ⚠️ CONCERNS: Some idempotency but not comprehensive
  - ❌ FAIL: Repeated requests cause duplicate data or corruption
  - ❓ UNCLEAR: Idempotency unclear

#### 9. Data Integrity
- **Definition:** Transactions, constraints, validation ensure data consistency
- **Evidence Required:**
  - Database transaction usage
  - Database constraints (foreign keys, unique, not null)
  - Data validation before persistence
  - Referential integrity maintained
- **Evaluation:**
  - ✅ PASS: Transactions, constraints, comprehensive validation
  - ⚠️ CONCERNS: Some data integrity measures but incomplete
  - ❌ FAIL: No transactions, weak constraints, data consistency issues
  - ❓ UNCLEAR: Data integrity unclear

#### 10. Disaster Recovery
- **Definition:** Backup and restore procedures documented and tested
- **Evidence Required:**
  - Backup strategy documentation
  - Automated backup configuration
  - Restore procedure documentation
  - Recovery Time Objective (RTO) defined
  - Recovery Point Objective (RPO) defined
- **Evaluation:**
  - ✅ PASS: Documented and tested backup/restore procedures
  - ⚠️ CONCERNS: Backup exists but restore not tested
  - ❌ FAIL: No backup strategy
  - ❓ UNCLEAR: Disaster recovery unclear (infra-level?)

---

## Maintainability Assessment

Maintainability assessment evaluates code quality, documentation, testability, and technical debt management.

### Maintainability Criteria (10 criteria)

#### 1. Code Quality
- **Definition:** Linting passes, no code smells
- **Evidence Required:**
  - Linting configuration (eslint, pylint, etc.)
  - Linting results (0 errors target)
  - Code smell analysis (SonarQube, CodeClimate)
- **Evaluation:**
  - ✅ PASS: Linting passes with 0 errors, no significant code smells
  - ⚠️ CONCERNS: Some linting errors or warnings, minor code smells
  - ❌ FAIL: Many linting errors, significant code smells
  - ❓ UNCLEAR: No linting configured

#### 2. Test Coverage
- **Definition:** Adequate test coverage (≥80% line coverage, ≥90% on critical paths)
- **Evidence Required:**
  - Test coverage report
  - Line coverage percentage
  - Branch coverage percentage
  - Function coverage percentage
  - Critical path coverage
- **Evaluation:**
  - ✅ PASS: ≥80% overall coverage, ≥90% critical paths
  - ⚠️ CONCERNS: 60-79% coverage or critical paths <90%
  - ❌ FAIL: <60% coverage or critical paths untested
  - ❓ UNCLEAR: No coverage report

#### 3. Documentation
- **Definition:** README, API docs, inline comments for complex logic
- **Evidence Required:**
  - README.md with setup instructions
  - API documentation (OpenAPI/Swagger)
  - Architecture documentation
  - JSDoc/docstrings for public functions
- **Evaluation:**
  - ✅ PASS: Comprehensive documentation (README, API docs, inline comments)
  - ⚠️ CONCERNS: Basic README but missing API docs or comments
  - ❌ FAIL: No README or documentation
  - ❓ UNCLEAR: Documentation unclear

#### 4. Modularity
- **Definition:** Single Responsibility Principle, loose coupling
- **Evidence Required:**
  - Code organization (clear module boundaries)
  - Function/class responsibilities
  - Dependency injection usage
  - Interface segregation
- **Evaluation:**
  - ✅ PASS: Clear module boundaries, single responsibilities, loose coupling
  - ⚠️ CONCERNS: Some modularity but tight coupling in places
  - ❌ FAIL: Monolithic code, tight coupling, mixed responsibilities
  - ❓ UNCLEAR: Modularity unclear

#### 5. Naming
- **Definition:** Clear, descriptive names for variables, functions, classes
- **Evidence Required:**
  - Naming convention consistency
  - Descriptive variable names (avoid `x`, `data`, `temp`)
  - Function names describe actions (verbs)
  - Class names describe entities (nouns)
- **Evaluation:**
  - ✅ PASS: Consistent, descriptive naming throughout
  - ⚠️ CONCERNS: Mostly good naming, some unclear names
  - ❌ FAIL: Poor naming, cryptic abbreviations, inconsistent
  - ❓ UNCLEAR: Cannot assess naming

#### 6. Complexity
- **Definition:** Cyclomatic complexity ≤10, function length ≤50 lines
- **Evidence Required:**
  - Complexity analysis report
  - Average complexity metric
  - Maximum complexity per function
  - Functions exceeding threshold count
- **Evaluation:**
  - ✅ PASS: All functions complexity ≤10, length ≤50 lines
  - ⚠️ CONCERNS: 1-3 functions exceed thresholds
  - ❌ FAIL: Many functions exceed complexity/length thresholds
  - ❓ UNCLEAR: No complexity analysis

#### 7. Duplication
- **Definition:** DRY principle, minimal code duplication
- **Evidence Required:**
  - Duplication detection report (jscpd, etc.)
  - Duplication percentage
  - Duplicated blocks count
- **Evaluation:**
  - ✅ PASS: <5% duplication, no significant duplicated blocks
  - ⚠️ CONCERNS: 5-10% duplication, some duplicated blocks
  - ❌ FAIL: >10% duplication, extensive copy-paste
  - ❓ UNCLEAR: No duplication analysis

#### 8. Type Safety
- **Definition:** TypeScript strict mode, no `any` types (or equivalent for other languages)
- **Evidence Required:**
  - TypeScript configuration (strict: true)
  - Type coverage analysis
  - `any` usage count
  - Type errors count
- **Evaluation:**
  - ✅ PASS: Strict mode, <5% `any` usage, 0 type errors
  - ⚠️ CONCERNS: Not strict mode or 5-15% `any` usage
  - ❌ FAIL: No type checking or >15% `any` usage
  - ❓ UNCLEAR: Not applicable (non-typed language)

#### 9. Dependencies
- **Definition:** Minimal dependencies, up-to-date versions
- **Evidence Required:**
  - Dependency count
  - Outdated dependencies analysis
  - Unused dependencies detection
  - Dependency size impact
- **Evaluation:**
  - ✅ PASS: Minimal deps, all up-to-date, no unused deps
  - ⚠️ CONCERNS: Some outdated deps or unused deps
  - ❌ FAIL: Many outdated deps, bloated dependency tree
  - ❓ UNCLEAR: Cannot analyze dependencies

#### 10. Technical Debt
- **Definition:** No TODO/FIXME without tracking tickets
- **Evidence Required:**
  - TODO/FIXME comment scan
  - Linked issue tracking (TODO: #123)
  - Technical debt tracking system
- **Evaluation:**
  - ✅ PASS: No TODO/FIXME or all linked to tickets
  - ⚠️ CONCERNS: Some untracked TODO/FIXME comments
  - ❌ FAIL: Many untracked TODO/FIXME comments
  - ❓ UNCLEAR: Cannot scan for technical debt

### Maintainability Automated Checks

1. **Linting:**
   ```bash
   npm run lint --format json
   ```
   Checks: Code style, potential bugs, code smells

2. **Test Coverage:**
   ```bash
   npm run test:coverage --json
   ```
   Measures: Line, branch, function coverage percentages

3. **Complexity Analysis:**
   ```bash
   npx complexity-report src/ --format json
   ```
   Measures: Cyclomatic complexity per function

4. **Duplication Detection:**
   ```bash
   npx jscpd src/ --format json
   ```
   Measures: Duplication percentage, duplicated blocks

---

## Scalability Assessment

Scalability assessment evaluates the system's ability to handle growth through horizontal scaling, proper architecture, and resource management.

### Scalability Criteria (10 criteria)

#### 1. Stateless Design
- **Definition:** No server-side state (or external session store)
- **Evidence Required:**
  - Authentication mechanism (JWT/stateless tokens vs sessions)
  - Session storage (external Redis vs in-memory)
  - File upload handling (object storage vs local disk)
  - In-memory caches (external Redis vs process memory)
- **Evaluation:**
  - ✅ PASS: Fully stateless, can scale horizontally
  - ⚠️ CONCERNS: Mostly stateless but some in-memory state
  - ❌ FAIL: Stateful design, cannot scale horizontally
  - ❓ UNCLEAR: Cannot determine state management

#### 2. Horizontal Scaling
- **Definition:** Can add more instances to increase capacity
- **Evidence Required:**
  - Load balancer configuration
  - Session affinity requirements (none preferred)
  - Shared state management (Redis, database)
  - Docker/container configuration
- **Evaluation:**
  - ✅ PASS: Designed for horizontal scaling, no dependencies on single instance
  - ⚠️ CONCERNS: Can scale but with limitations (session affinity required)
  - ❌ FAIL: Cannot scale horizontally (stateful, single instance)
  - ❓ UNCLEAR: Scalability unclear

#### 3. Database Design
- **Definition:** Normalized schema, proper indexing, sharding-ready
- **Evidence Required:**
  - Database schema (normalization level)
  - Index definitions on foreign keys
  - Query patterns analysis
  - Sharding strategy (if applicable)
- **Evaluation:**
  - ✅ PASS: Normalized, all foreign keys indexed, sharding considered
  - ⚠️ CONCERNS: Normalized but missing some indexes
  - ❌ FAIL: Denormalized, no indexes, poor query performance
  - ❓ UNCLEAR: Cannot analyze database design

#### 4. Connection Pooling
- **Definition:** Database connection pool configured properly
- **Evidence Required:**
  - Connection pool size (min/max)
  - Connection timeout settings
  - Pool monitoring
- **Evaluation:**
  - ✅ PASS: Connection pooling with appropriate sizing
  - ⚠️ CONCERNS: Connection pooling but misconfigured
  - ❌ FAIL: No connection pooling
  - ❓ UNCLEAR: Connection pooling unclear

#### 5. Caching
- **Definition:** Multi-tier caching (in-memory, Redis, CDN)
- **Evidence Required:**
  - Caching layers identified
  - Cache invalidation strategy
  - Cache hit rate metrics
  - CDN usage (for static assets)
- **Evaluation:**
  - ✅ PASS: Multi-tier caching with proper invalidation
  - ⚠️ CONCERNS: Single-tier caching or weak invalidation
  - ❌ FAIL: No caching or caching anti-patterns
  - ❓ UNCLEAR: Caching unclear

#### 6. Async Processing
- **Definition:** Background jobs for expensive operations (queues)
- **Evidence Required:**
  - Job queue implementation (Bull, BullMQ, Celery, etc.)
  - Background job definitions
  - Queue configuration (Redis-backed)
  - Worker process configuration
- **Evaluation:**
  - ✅ PASS: Queue-based async processing for expensive operations
  - ⚠️ CONCERNS: Some async processing but synchronous expensive operations remain
  - ❌ FAIL: No async processing, expensive operations block requests
  - ❓ UNCLEAR: Async processing unclear

#### 7. Rate Limiting
- **Definition:** Per-user/IP rate limits to prevent abuse
- **Evidence Required:**
  - Rate limiting strategy (per-user, per-IP, per-endpoint)
  - Rate limit configuration
  - Rate limit storage (Redis for distributed)
- **Evaluation:**
  - ✅ PASS: Distributed rate limiting (Redis-backed)
  - ⚠️ CONCERNS: In-memory rate limiting (not distributed)
  - ❌ FAIL: No rate limiting
  - ❓ UNCLEAR: Rate limiting unclear

#### 8. Load Balancing Readiness
- **Definition:** Ready for load balancer (health checks, graceful shutdown)
- **Evidence Required:**
  - Health check endpoint implementation
  - Graceful shutdown handler (SIGTERM)
  - Connection draining
  - Ready for multiple instances
- **Evaluation:**
  - ✅ PASS: Health checks, graceful shutdown, load balancer ready
  - ⚠️ CONCERNS: Health checks present but no graceful shutdown
  - ❌ FAIL: No health checks or graceful shutdown
  - ❓ UNCLEAR: Load balancing readiness unclear

#### 9. Resource Limits
- **Definition:** Memory/CPU limits configured (Docker, Kubernetes)
- **Evidence Required:**
  - Container resource limits (memory, CPU)
  - Resource request specifications
  - Auto-scaling configuration based on resources
- **Evaluation:**
  - ✅ PASS: Resource limits configured appropriately
  - ⚠️ CONCERNS: Resource limits set but misconfigured
  - ❌ FAIL: No resource limits
  - ❓ UNCLEAR: Resource limits unclear (infra-level?)

#### 10. Auto-scaling
- **Definition:** Metrics-based auto-scaling configured (if cloud)
- **Evidence Required:**
  - Auto-scaling policy (CPU, memory, request rate)
  - Scaling thresholds
  - Min/max instance counts
  - Scaling cooldown periods
- **Evaluation:**
  - ✅ PASS: Auto-scaling configured with appropriate metrics
  - ⚠️ CONCERNS: Auto-scaling configured but suboptimal metrics
  - ❌ FAIL: No auto-scaling
  - ❓ UNCLEAR: Auto-scaling unclear (infra-level?)

---

## Usability Assessment

Usability assessment evaluates the developer experience for APIs or user experience for UIs.

### Usability Criteria - API (10 criteria)

#### 1. API Design
- **Definition:** RESTful conventions, consistent resource naming
- **Evidence Required:**
  - REST resource naming (plural nouns: /users, /posts)
  - HTTP verb usage (GET, POST, PUT, PATCH, DELETE)
  - URL structure consistency
  - API versioning (v1, v2)
- **Evaluation:**
  - ✅ PASS: RESTful conventions followed consistently
  - ⚠️ CONCERNS: Mostly RESTful but some inconsistencies
  - ❌ FAIL: Non-RESTful, inconsistent resource naming
  - ❓ UNCLEAR: Cannot assess API design

#### 2. Error Messages
- **Definition:** Clear, actionable error messages with details
- **Evidence Required:**
  - Error response format
  - Field-specific error details
  - Error codes/types
  - Actionable guidance in errors
- **Evaluation:**
  - ✅ PASS: Clear error messages with field details and guidance
  - ⚠️ CONCERNS: Generic error messages, minimal details
  - ❌ FAIL: Cryptic errors, no details
  - ❓ UNCLEAR: Error messages unclear

#### 3. Documentation
- **Definition:** OpenAPI/Swagger spec, usage examples
- **Evidence Required:**
  - OpenAPI/Swagger specification
  - API documentation site (Swagger UI, Redoc)
  - Code examples for each endpoint
  - Authentication documentation
- **Evaluation:**
  - ✅ PASS: Complete OpenAPI spec with examples
  - ⚠️ CONCERNS: Partial documentation or missing examples
  - ❌ FAIL: No API documentation
  - ❓ UNCLEAR: Documentation unclear

#### 4. Versioning
- **Definition:** API versioning strategy (v1, v2, etc.)
- **Evidence Required:**
  - Versioning scheme (URL path, header, query param)
  - Deprecation policy
  - Backwards compatibility strategy
- **Evaluation:**
  - ✅ PASS: Clear versioning strategy with deprecation policy
  - ⚠️ CONCERNS: Versioning present but no deprecation policy
  - ❌ FAIL: No versioning strategy
  - ❓ UNCLEAR: Versioning unclear

#### 5. Pagination
- **Definition:** Consistent pagination for list endpoints
- **Evidence Required:**
  - Pagination implementation (offset/limit, cursor)
  - Total count in responses
  - Next/previous links (HATEOAS)
  - Consistent pagination across endpoints
- **Evaluation:**
  - ✅ PASS: Consistent pagination with total count and links
  - ⚠️ CONCERNS: Pagination present but inconsistent or missing metadata
  - ❌ FAIL: No pagination on list endpoints
  - ❓ UNCLEAR: Pagination unclear

#### 6. Filtering
- **Definition:** Query parameters for filtering/sorting
- **Evidence Required:**
  - Filter parameter support
  - Sort parameter support
  - Search functionality
  - Consistent query parameter naming
- **Evaluation:**
  - ✅ PASS: Comprehensive filtering and sorting with consistent syntax
  - ⚠️ CONCERNS: Basic filtering but limited options
  - ❌ FAIL: No filtering or sorting
  - ❓ UNCLEAR: Filtering unclear

#### 7. HTTP Status Codes
- **Definition:** Proper status codes (200, 400, 404, 500, etc.)
- **Evidence Required:**
  - Status code usage analysis
  - 2xx for success, 4xx for client errors, 5xx for server errors
  - Specific codes (201 Created, 204 No Content, 401 Unauthorized, 403 Forbidden, etc.)
- **Evaluation:**
  - ✅ PASS: Appropriate status codes throughout
  - ⚠️ CONCERNS: Mostly correct but some inappropriate codes
  - ❌ FAIL: Always 200 or incorrect status codes
  - ❓ UNCLEAR: Cannot assess status codes

#### 8. Response Format
- **Definition:** Consistent JSON structure
- **Evidence Required:**
  - Response schema consistency
  - Envelope format (data, meta, errors)
  - Camel case vs snake case consistency
- **Evaluation:**
  - ✅ PASS: Consistent response format across all endpoints
  - ⚠️ CONCERNS: Mostly consistent but some variations
  - ❌ FAIL: Inconsistent response formats
  - ❓ UNCLEAR: Cannot assess response format

#### 9. HATEOAS (Optional)
- **Definition:** Hypermedia links for navigation
- **Evidence Required:**
  - Links in responses (self, next, prev, related)
  - Discoverable API structure
- **Evaluation:**
  - ✅ PASS: HATEOAS implemented, fully discoverable
  - ⚠️ CONCERNS: Partial HATEOAS
  - ❌ FAIL: No HATEOAS (not necessarily bad, depends on requirements)
  - ❓ UNCLEAR: HATEOAS not applicable

#### 10. Developer Experience
- **Definition:** Easy to use, intuitive, well-documented
- **Evidence Required:**
  - Postman/Insomnia collection
  - SDK availability
  - Quickstart guide
  - Interactive API explorer
- **Evaluation:**
  - ✅ PASS: Excellent DX with SDKs, collections, interactive docs
  - ⚠️ CONCERNS: Basic DX, documentation only
  - ❌ FAIL: Poor DX, difficult to integrate
  - ❓ UNCLEAR: Cannot assess DX

### Usability Criteria - UI (10 criteria)

#### 1. Accessibility (WCAG 2.1 AA)
- **Evidence:** Automated accessibility scan results
- **Evaluation:** PASS (compliant), CONCERNS (some issues), FAIL (non-compliant)

#### 2. Responsive Design
- **Evidence:** Mobile, tablet, desktop layouts
- **Evaluation:** PASS (fully responsive), CONCERNS (partial), FAIL (desktop only)

#### 3. Loading States
- **Evidence:** Skeleton screens, spinners, progress indicators
- **Evaluation:** PASS (comprehensive feedback), CONCERNS (basic), FAIL (no feedback)

#### 4. Error Handling
- **Evidence:** User-friendly error messages, error recovery
- **Evaluation:** PASS (clear errors + recovery), CONCERNS (basic errors), FAIL (cryptic errors)

#### 5. Keyboard Navigation
- **Evidence:** Full keyboard support, focus management, shortcuts
- **Evaluation:** PASS (full keyboard support), CONCERNS (partial), FAIL (mouse only)

#### 6-10: (Color Contrast, Screen Reader Support, Form Validation, Intuitive Navigation, Performance)
- Similar evidence-based evaluation methodology

### Usability Automated Checks

1. **API Documentation Check:**
   - Verify OpenAPI/Swagger spec exists
   - Validate spec completeness

2. **Accessibility Scan (UI):**
   ```bash
   npx axe-cli http://localhost:3000
   # or
   lighthouse --only-categories=accessibility
   ```
   Checks: WCAG 2.1 AA compliance

---

## Category Relevance by Task Type

Different task types have different NFR priorities:

### API Endpoint Task
- **Security:** HIGH (auth, input validation, rate limiting)
- **Performance:** HIGH (response time, caching)
- **Reliability:** MEDIUM (error handling, logging)
- **Maintainability:** MEDIUM (code quality, tests)
- **Scalability:** LOW (single endpoint)
- **Usability:** MEDIUM (error messages, API docs)

### Database Schema Task
- **Security:** HIGH (SQL injection, access control)
- **Performance:** HIGH (indexing, query optimization)
- **Reliability:** HIGH (data integrity, transactions)
- **Maintainability:** MEDIUM (migration strategy)
- **Scalability:** HIGH (sharding, partitioning)
- **Usability:** LOW (internal schema)

### UI Component Task
- **Security:** MEDIUM (XSS prevention)
- **Performance:** HIGH (render performance, bundle size)
- **Reliability:** MEDIUM (error states)
- **Maintainability:** HIGH (component reusability)
- **Scalability:** LOW (client-side)
- **Usability:** HIGH (accessibility, UX)

### Background Job Task
- **Security:** LOW (internal processing)
- **Performance:** MEDIUM (processing time)
- **Reliability:** HIGH (error handling, retries, idempotency)
- **Maintainability:** MEDIUM (code quality)
- **Scalability:** HIGH (queue-based, distributed)
- **Usability:** LOW (no user interaction)

---

*This reference provides comprehensive category definitions for NFR assessment.*
