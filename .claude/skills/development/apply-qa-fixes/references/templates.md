# Templates and Schemas

Reference schemas and templates for apply-qa-fixes skill.

---

## Quality Gate Schema

Quality gate YAML file structure from Quinn's quality-gate skill.

### Gate File Location

```
.claude/quality/gates/{task-id}-gate-{date}.yaml
```

### Gate YAML Structure

```yaml
task_id: "task-001"
date: "2025-01-15"
decision: "CONCERNS"  # PASS | CONCERNS | FAIL | WAIVED
overall_score: 72
can_proceed: true
waiver_required: false

# Quality Dimensions (each 0-100)
dimensions:
  risk_management: 85
  test_coverage: 65
  traceability: 90
  nfr_compliance: 60
  implementation_quality: 75
  project_compliance: 95

# Top Issues (high/medium/low severity)
top_issues:
  - id: "SEC-001"
    category: "security"
    severity: "high"
    description: "Missing input validation on user registration endpoint"
    location: "src/api/user.ts:45"
    recommendation: "Add Joi schema validation for email, password, username"
    impact: "Allows malformed data to reach database"

  - id: "SEC-002"
    category: "security"
    severity: "high"
    description: "SQL injection vulnerability in user query"
    location: "src/db/queries.ts:23"
    recommendation: "Use parameterized queries instead of string concatenation"
    impact: "Potential database compromise"

  - id: "PERF-001"
    category: "performance"
    severity: "medium"
    description: "N+1 query pattern in data fetching"
    location: "src/services/data.ts:67"
    recommendation: "Use eager loading or batch queries"
    impact: "Poor performance with large datasets"

# NFR Validation Results
nfr_validation:
  security:
    status: "FAIL"  # PASS | CONCERNS | FAIL
    score: 45
    concerns:
      - "Missing input validation (src/api/user.ts:45)"
      - "SQL injection risk (src/db/queries.ts:23)"
      - "No rate limiting on API endpoints"
    recommendations:
      - "Add validation middleware"
      - "Use parameterized queries"
      - "Implement rate limiting (express-rate-limit)"

  performance:
    status: "CONCERNS"
    score: 65
    concerns:
      - "N+1 query pattern (src/services/data.ts:67)"
    recommendations:
      - "Use eager loading or batch queries"

  reliability:
    status: "PASS"
    score: 85

  maintainability:
    status: "PASS"
    score: 90

  scalability:
    status: "CONCERNS"
    score: 70

  usability:
    status: "PASS"
    score: 80

# Traceability Data
trace:
  traceability_score: 90
  implementation_coverage: 100
  test_coverage: 85
  ac_gaps:
    - ac_id: "AC4"
      description: "Secure password storage"
      coverage: "partial"
      missing:
        - "bcrypt hashing not implemented"
        - "Salt rounds not configurable"

# Test Design Data
test_design:
  total_tests: 35
  p0_tests: 12
  p1_tests: 15
  p2_tests: 8
  coverage_gaps:
    - ac_id: "AC2"
      description: "User authentication flow"
      missing_tests:
        - "Should reject invalid credentials"
        - "Should handle expired tokens"
        - "Should refresh tokens correctly"
    - ac_id: "AC4"
      description: "Secure password storage"
      missing_tests:
        - "Should hash passwords with bcrypt"
        - "Should use configurable salt rounds"

# Action Items (from all assessments)
action_items:
  p0:
    - "Fix SQL injection vulnerability (SEC-002)"
    - "Add input validation (SEC-001)"
  p1:
    - "Implement rate limiting"
    - "Add missing tests for AC2, AC4"
  p2:
    - "Optimize N+1 queries"
    - "Add error logging"

# Report Paths
reports:
  risk_profile: ".claude/quality/assessments/task-001-risk-2025-01-15.md"
  test_design: ".claude/quality/assessments/task-001-test-design-2025-01-15.md"
  traceability: ".claude/quality/assessments/task-001-trace-2025-01-15.md"
  nfr_assessment: ".claude/quality/assessments/task-001-nfr-2025-01-15.md"
  gate_report: ".claude/quality/gates/task-001-gate-2025-01-15.md"
```

---

## Parsed Findings Structure

After parsing quality gate (Step 1), structure findings as:

```typescript
interface ParsedFindings {
  high_severity_issues: Issue[]
  medium_severity_issues: Issue[]
  low_severity_issues: Issue[]
  nfr_failures: NFRIssue[]
  nfr_concerns: NFRIssue[]
  coverage_gaps: CoverageGap[]
  trace_gaps: TraceGap[]
}

interface Issue {
  id: string              // "SEC-001"
  category: string        // "security"
  severity: "high" | "medium" | "low"
  description: string
  location: string        // "src/api/user.ts:45"
  recommendation: string
  impact: string
}

interface NFRIssue {
  category: string        // "security"
  status: "FAIL" | "CONCERNS"
  score: number          // 0-100
  concerns: string[]
  recommendations: string[]
}

interface CoverageGap {
  ac_id: string          // "AC2"
  description: string
  missing_tests: string[]
}

interface TraceGap {
  ac_id: string          // "AC4"
  description: string
  coverage: "none" | "partial" | "full"
  missing: string[]
}
```

---

## Fix Plan Structure

After building fix plan (Step 2), structure as:

```typescript
interface FixPlan {
  fixes: Fix[]
  estimated_impact: Impact
  guardrail_check: GuardrailCheck
}

interface Fix {
  priority: number        // 1-7
  issue_id: string       // "SEC-001"
  type: FixType          // "high_severity" | "nfr_fail" | "coverage_gap" | etc.
  category: string       // "security"
  description: string
  location: string       // "src/api/user.ts:45"
  action: string         // "Add Joi validation schema"
  files_to_modify: string[]
  estimated_diff_lines: number
  tests_to_add?: string[]
}

type FixType =
  | "high_severity"
  | "nfr_fail"
  | "coverage_gap"
  | "nfr_concern"
  | "trace_gap"
  | "medium_severity"
  | "low_severity"

interface Impact {
  total_fixes: number
  files_to_modify: number
  estimated_diff_lines: number
  tests_to_add: number
}

interface GuardrailCheck {
  passed: boolean
  violations: string[]
  max_files: number
  max_diff_lines: number
}
```

---

## Validation Results Structure

After validation (Step 4):

```typescript
interface ValidationResults {
  lint: {
    passed: boolean
    errors: number
    warnings: number
    output: string
  }
  tests: {
    passed: boolean
    total_tests: number
    tests_passed: number
    tests_failed: number
    coverage_percent: number
  }
  coverage: {
    before: number
    after: number
    improvement: number
  }
  validation_clean: boolean
  iterations: number
}
```

---

## Task File Update Template

Template for updating task Implementation Record section (Step 5):

```markdown
### QA Fixes Applied (2025-01-15)

**Quality Gate:** .claude/quality/gates/{task-id}-gate-{date}.yaml
**Status Before:** {CONCERNS|FAIL} ({score}/100)
**Status After:** Ready for re-review

**Fixes Applied ({total} total):**

**Priority 1 (High Severity): {count} issues**
{For each high severity fix:}
{index}. {issue_id}: {description} ({location})

**Priority 2 (NFR Failures): {count} issues**
{For each NFR failure:}
{index}. {issue_id}: {description}

**Priority 3 (Coverage Gaps): {count} tests added**
{For each coverage gap:}
{index}. {ac_id}: {description} ({test_count} tests)

**Priority 4-7: {count} issues**
{Summary of lower priority fixes}

**Validation Results:**
- {✅|❌} Lint: {errors} problems
- {✅|❌} Tests: {passed}/{total} passed
- {✅|❌} Coverage: {before}% → {after}% ({improvement:+}%)

**Files Modified:**
{For each file:}
- {file_path} {(new) if created}

**Next Steps:**
- Ready for Quinn re-review: @quinn *review {task-id}
```

### Example Task Update

```markdown
### QA Fixes Applied (2025-01-15)

**Quality Gate:** .claude/quality/gates/task-001-gate-2025-01-15.yaml
**Status Before:** CONCERNS (72/100)
**Status After:** Ready for re-review

**Fixes Applied (15 total):**

**Priority 1 (High Severity): 3 issues**
1. SEC-001: Missing input validation on user registration (src/api/user.ts:45)
2. SEC-002: SQL injection vulnerability in user query (src/db/queries.ts:23)
3. PERF-001: N+1 query pattern in data fetching (src/services/data.ts:67)

**Priority 2 (NFR Failures): 2 issues**
4. NFR-SEC-001: No rate limiting on API endpoints
5. NFR-REL-001: Missing error logging and monitoring

**Priority 3 (Coverage Gaps): 5 tests added**
6. AC2: User authentication flow (3 tests)
7. AC4: Secure password storage (2 tests)

**Priority 4-7: 5 issues**
8-10. NFR concerns (rate limiting, caching)
11-12. Medium severity (error handling improvements)
13-15. Low severity (code style, documentation)

**Validation Results:**
- ✅ Lint: 0 problems
- ✅ Tests: 45/45 passed
- ✅ Coverage: 82% → 89% (+7%)

**Files Modified:**
- src/api/user.ts
- src/db/queries.ts
- src/services/data.ts
- src/middleware/rate-limit.ts (new)
- src/middleware/validation.ts (new)
- tests/api/user.test.ts
- tests/api/user-auth.test.ts (new)
- tests/db/queries.test.ts

**Next Steps:**
- Ready for Quinn re-review: @quinn *review task-001
```

---

## Telemetry Schema

Telemetry emitted after completion (Step 6):

```json
{
  "event": "skill.apply-qa-fixes.completed",
  "timestamp": "2025-01-15T10:30:00Z",
  "data": {
    "task_id": "task-001",
    "quality_gate": ".claude/quality/gates/task-001-gate-2025-01-15.yaml",
    "gate_decision_before": "CONCERNS",
    "gate_score_before": 72,

    "fixes_count": 15,
    "fixes_applied": {
      "high_severity": 3,
      "nfr_failures": 2,
      "coverage_gaps": 5,
      "nfr_concerns": 3,
      "trace_gaps": 0,
      "medium_severity": 2,
      "low_severity": 0
    },

    "tests_added": 5,
    "coverage_before": 82,
    "coverage_after": 89,
    "coverage_improvement": 7,

    "files_modified": 8,
    "files_created": 2,

    "validation": {
      "lint_passed": true,
      "tests_passed": true,
      "validation_clean": true,
      "iterations": 1
    },

    "duration_ms": 180000,
    "fixes_failed": 0,
    "escalations": 0
  }
}
```

---

## Configuration Schema

Expected configuration in `.claude/config.yaml`:

```yaml
quality:
  assessments_dir: ".claude/quality/assessments"
  gates_dir: ".claude/quality/gates"
  coverage_threshold: 80
  test_framework: "auto"  # or "pytest", "mocha", etc.

tasks:
  directory: ".claude/tasks"

testing:
  framework: "auto"
  coverage_threshold: 80
  test_directory: "tests"
  lint_command: "npm run lint"
  test_command: "npm test"
```

---

## Output Schema

Skill returns structured output:

```typescript
interface ApplyQAFixesOutput {
  success: boolean
  task_id: string

  fixes_applied: Fix[]
  fixes_failed: Fix[]

  tests_added: number
  coverage_improvement: {
    before: number
    after: number
    delta: number
  }

  validation_passed: boolean
  validation_results: ValidationResults

  files_modified: string[]
  task_updated: boolean

  telemetry: TelemetryData
}
```

---

## Error Scenarios

### Scenario 1: Quality Gate Not Found

**Error:**
```json
{
  "success": false,
  "error": "quality_gate_not_found",
  "message": "No quality gate found for task-001",
  "searched_paths": [
    ".claude/quality/gates/task-001-gate-*.yaml"
  ],
  "recommendation": "Run quality review first: @quinn *review task-001"
}
```

### Scenario 2: Gate Status is PASS

**Error:**
```json
{
  "success": false,
  "error": "no_fixes_needed",
  "message": "Quality gate status is PASS, no fixes required",
  "gate_decision": "PASS",
  "gate_score": 95,
  "recommendation": "Task is ready for merge"
}
```

### Scenario 3: Guardrail Violation

**Warning:**
```json
{
  "success": false,
  "error": "guardrail_violation",
  "message": "Fix plan exceeds guardrails",
  "violations": [
    "max_files: 15 files (limit: 10)"
  ],
  "recommendation": "Split into multiple fix sessions or escalate to user"
}
```

### Scenario 4: Tests Fail After Fixes

**Error:**
```json
{
  "success": false,
  "error": "validation_failed",
  "message": "Tests failing after fixes applied",
  "tests_failed": ["should handle invalid credentials", "should reject expired tokens"],
  "iteration": 2,
  "recommendation": "Debug failing tests or escalate"
}
```

---

## User Decision Handling

After fixes applied and validation complete, present options:

```
=== QA Fixes Applied ===

✅ 15 fixes applied
✅ 5 tests added
✅ Coverage: 82% → 89%
✅ Validation: All tests passing

Next steps:
1. [accept] - Accept fixes and proceed to re-review
2. [review] - Review fixes in detail before re-review
3. [revert] - Revert fixes and start over
4. [abort] - Abort and address manually

Your choice?
```

**User Decisions:**

1. **accept** - Mark task ready for Quinn re-review
2. **review** - Show detailed fix list for user review
3. **revert** - Git revert changes, restore to pre-fix state
4. **abort** - Stop, allow user to fix manually

---

## Quick Reference

### Priority Order (1-7)

1. High severity (security, data loss, critical bugs)
2. NFR failures (status = FAIL)
3. Test coverage gaps (P0 scenarios)
4. NFR concerns (status = CONCERNS)
5. Traceability gaps (uncovered ACs)
6. Medium severity
7. Low severity

### Guardrails

- Max 10 files per fix session
- Max 800 diff lines
- Must pass lint
- Must pass tests
- Must not decrease coverage

### File Permissions

**Can update:**
- Implementation Record section
- File List section
- Status (InProgress ↔ Review only)

**Cannot update:**
- Objective, AC, Context, Tasks
- Quality Review section

---
