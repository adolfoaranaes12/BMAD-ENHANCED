# Fix Prioritization Rules

Deterministic rules for prioritizing QA fixes to ensure critical issues addressed first.

---

## Core Principle

**Deterministic Prioritization:** Given the same quality gate, always produce the same fix order.

**Why it matters:**
- Predictable behavior
- Consistent results
- Testable
- Auditable
- No subjective decisions

---

## Priority Levels (1-7)

### Priority 1: High Severity Issues

**Definition:** Critical issues that pose security risks, data loss, or system failures.

**Categories:**
- **Security vulnerabilities** - SQL injection, XSS, CSRF, authentication bypass
- **Data loss risks** - Data corruption, deletion without backup
- **Critical bugs** - System crashes, data integrity violations
- **Severe performance issues** - Infinite loops, memory leaks, deadlocks

**Examples:**
```
✅ P1: SQL injection vulnerability in user query
✅ P1: Missing authentication on admin endpoint
✅ P1: Data deletion without confirmation
❌ P1: Missing input validation (unless security-critical)
❌ P1: Slow query (unless causes timeouts)
```

**Selection Criteria:**
- `severity == "high"`
- OR `category == "security" AND impact contains ["compromise", "breach", "injection", "bypass"]`
- OR `category == "data_loss"`
- OR `category == "critical_bug"`

**Must Fix:** Yes, always address before lower priorities

---

### Priority 2: NFR Failures

**Definition:** Non-functional requirements with FAIL status (not CONCERNS).

**Categories:**
- `nfr_validation.security.status == "FAIL"`
- `nfr_validation.performance.status == "FAIL"`
- `nfr_validation.reliability.status == "FAIL"`
- `nfr_validation.maintainability.status == "FAIL"`
- `nfr_validation.scalability.status == "FAIL"`
- `nfr_validation.usability.status == "FAIL"`

**Severity Order Within P2:**
1. Security FAIL
2. Reliability FAIL
3. Performance FAIL
4. Maintainability FAIL
5. Scalability FAIL
6. Usability FAIL

**Examples:**
```
✅ P2: Security FAIL (no rate limiting, missing encryption)
✅ P2: Reliability FAIL (no error logging, no monitoring)
✅ P2: Performance FAIL (missing indexes, no caching)
❌ P2: Security CONCERNS (should use P4)
```

**Selection Criteria:**
- `nfr_validation.{category}.status == "FAIL"`

**Must Fix:** Yes, FAIL status indicates critical NFR gap

---

### Priority 3: Test Coverage Gaps (P0 Scenarios)

**Definition:** Missing tests for P0 (critical path) scenarios identified by test-design skill.

**What to Add:**
- Tests for P0 acceptance criteria
- Critical path test scenarios
- Security-critical test cases
- Data integrity validations

**Examples:**
```
✅ P3: AC2 - Missing tests for user authentication flow
✅ P3: AC4 - Missing tests for password hashing
✅ P3: AC1 - Missing integration tests for payment flow
❌ P3: P2 tests (add later in P4-7)
❌ P3: Nice-to-have edge cases
```

**Selection Criteria:**
- `test_design.coverage_gaps` where `priority == "P0"`
- OR `trace.ac_gaps` where `ac.priority == "critical"`

**How to Identify P0:**
- Acceptance criteria marked critical
- Security-related test scenarios
- Happy path / critical path tests
- Data integrity tests

**Must Fix:** Yes, P0 tests are critical for quality assurance

---

### Priority 4: NFR Concerns

**Definition:** Non-functional requirements with CONCERNS status (not FAIL).

**Categories:**
- `nfr_validation.security.status == "CONCERNS"`
- `nfr_validation.performance.status == "CONCERNS"`
- `nfr_validation.reliability.status == "CONCERNS"`
- `nfr_validation.maintainability.status == "CONCERNS"`
- `nfr_validation.scalability.status == "CONCERNS"`
- `nfr_validation.usability.status == "CONCERNS"`

**Severity Order Within P4:**
1. Security CONCERNS
2. Reliability CONCERNS
3. Performance CONCERNS
4. Maintainability CONCERNS
5. Scalability CONCERNS
6. Usability CONCERNS

**Examples:**
```
✅ P4: Security CONCERNS (should add rate limiting)
✅ P4: Performance CONCERNS (could optimize queries)
✅ P4: Reliability CONCERNS (add more logging)
```

**Selection Criteria:**
- `nfr_validation.{category}.status == "CONCERNS"`

**Must Fix:** Recommended, but not blocking

---

### Priority 5: Traceability Gaps

**Definition:** Uncovered or partially covered acceptance criteria from traceability analysis.

**What to Fix:**
- Implement missing AC coverage
- Add tests for uncovered ACs
- Complete partial implementations

**Examples:**
```
✅ P5: AC4 - Secure password storage (partial coverage, missing bcrypt)
✅ P5: AC7 - Session management (no implementation found)
❌ P5: AC2 - Already fully covered
```

**Selection Criteria:**
- `trace.ac_gaps` where `coverage == "none" OR coverage == "partial"`

**Must Fix:** Recommended to complete acceptance criteria

---

### Priority 6: Medium Severity Issues

**Definition:** Non-critical issues affecting code quality, maintainability, or minor functionality.

**Categories:**
- Code quality issues
- Moderate performance issues
- Error handling improvements
- Documentation gaps
- Minor UX issues

**Examples:**
```
✅ P6: Missing error handling in helper function
✅ P6: Inconsistent naming conventions
✅ P6: Missing JSDoc comments
✅ P6: Inefficient algorithm (not critical path)
❌ P6: Security issues (should be P1)
```

**Selection Criteria:**
- `severity == "medium"`
- AND NOT in categories: security, data_loss, critical_bug

**Must Fix:** Optional, can defer if time-constrained

---

### Priority 7: Low Severity Issues

**Definition:** Minor issues, stylistic improvements, suggestions.

**Categories:**
- Code style
- Formatting
- Minor documentation updates
- Suggestions for optimization
- Nice-to-have features

**Examples:**
```
✅ P7: Use const instead of let
✅ P7: Add newline at end of file
✅ P7: Typo in comment
✅ P7: Could use arrow function
```

**Selection Criteria:**
- `severity == "low"`

**Must Fix:** Optional, defer if time-constrained

---

## Decision Tree

```
For each issue from quality gate:

1. Is severity == "high"?
   YES → Priority 1 (High Severity)
   NO  → Continue

2. Is NFR status == "FAIL"?
   YES → Priority 2 (NFR Failure)
   NO  → Continue

3. Is coverage_gap AND P0 scenario?
   YES → Priority 3 (Coverage Gap)
   NO  → Continue

4. Is NFR status == "CONCERNS"?
   YES → Priority 4 (NFR Concern)
   NO  → Continue

5. Is traceability gap (none/partial coverage)?
   YES → Priority 5 (Trace Gap)
   NO  → Continue

6. Is severity == "medium"?
   YES → Priority 6 (Medium Severity)
   NO  → Priority 7 (Low Severity)
```

---

## Tiebreakers (Within Same Priority)

When multiple issues have same priority:

### Tiebreaker 1: Category Severity

Order by category:
1. Security
2. Data Loss / Integrity
3. Performance
4. Reliability
5. Maintainability
6. Scalability
7. Usability
8. Code Quality
9. Documentation

**Example:**
```
Both Priority 1:
- SEC-001 (security) → Fix first
- PERF-001 (performance) → Fix second
```

### Tiebreaker 2: Impact Severity

If same priority AND same category, order by impact keywords:

**High impact keywords:**
- "critical"
- "severe"
- "major"
- "compromise"
- "breach"
- "failure"

**Medium impact keywords:**
- "moderate"
- "significant"
- "noticeable"

**Low impact keywords:**
- "minor"
- "slight"
- "negligible"

### Tiebreaker 3: Issue ID (Alphabetical)

If same priority, category, and impact → sort by issue ID alphabetically.

**Example:**
```
Both P1, both security, same impact:
- SEC-001 → Fix first
- SEC-002 → Fix second
```

---

## Complete Priority Algorithm

```typescript
function prioritizeFixes(findings: ParsedFindings): Fix[] {
  const fixes: Fix[] = []

  // Priority 1: High severity
  findings.high_severity_issues.forEach(issue => {
    fixes.push({
      priority: 1,
      type: "high_severity",
      ...issue
    })
  })

  // Priority 2: NFR failures
  findings.nfr_failures.forEach(nfr => {
    fixes.push({
      priority: 2,
      type: "nfr_fail",
      ...nfr
    })
  })

  // Priority 3: Coverage gaps (P0 only)
  findings.coverage_gaps
    .filter(gap => gap.priority === "P0")
    .forEach(gap => {
      fixes.push({
        priority: 3,
        type: "coverage_gap",
        ...gap
      })
    })

  // Priority 4: NFR concerns
  findings.nfr_concerns.forEach(nfr => {
    fixes.push({
      priority: 4,
      type: "nfr_concern",
      ...nfr
    })
  })

  // Priority 5: Trace gaps
  findings.trace_gaps
    .filter(gap => gap.coverage === "none" || gap.coverage === "partial")
    .forEach(gap => {
      fixes.push({
        priority: 5,
        type: "trace_gap",
        ...gap
      })
    })

  // Priority 6: Medium severity
  findings.medium_severity_issues.forEach(issue => {
    fixes.push({
      priority: 6,
      type: "medium_severity",
      ...issue
    })
  })

  // Priority 7: Low severity
  findings.low_severity_issues.forEach(issue => {
    fixes.push({
      priority: 7,
      type: "low_severity",
      ...issue
    })
  })

  // Sort by priority, then category, then ID
  return fixes.sort((a, b) => {
    // First: by priority number
    if (a.priority !== b.priority) {
      return a.priority - b.priority
    }

    // Second: by category severity
    const categoryOrder = getCategoryOrder(a.category, b.category)
    if (categoryOrder !== 0) {
      return categoryOrder
    }

    // Third: by issue ID (alphabetical)
    return a.issue_id.localeCompare(b.issue_id)
  })
}

function getCategoryOrder(catA: string, catB: string): number {
  const order = [
    "security",
    "data_loss",
    "performance",
    "reliability",
    "maintainability",
    "scalability",
    "usability",
    "code_quality",
    "documentation"
  ]

  const indexA = order.indexOf(catA)
  const indexB = order.indexOf(catB)

  return indexA - indexB
}
```

---

## Example Prioritization

Given quality gate with:
- 3 high severity (SEC-001, SEC-002, PERF-001)
- 2 NFR failures (security FAIL, reliability FAIL)
- 5 coverage gaps (3 P0, 2 P1)
- 3 NFR concerns (performance CONCERNS, scalability CONCERNS, usability CONCERNS)
- 1 trace gap (AC4 partial coverage)
- 2 medium severity (ERR-001, DOC-001)
- 1 low severity (STYLE-001)

**Prioritized Fix Order:**

```
Priority 1 (High Severity): 3 fixes
1. SEC-001: SQL injection (security)
2. SEC-002: Missing auth (security)
3. PERF-001: N+1 queries (performance)

Priority 2 (NFR Failures): 2 fixes
4. NFR-SEC-001: No rate limiting (security FAIL)
5. NFR-REL-001: No error logging (reliability FAIL)

Priority 3 (Coverage Gaps): 3 fixes
6. TEST-AC2-001: Auth flow tests (P0)
7. TEST-AC2-002: Token refresh tests (P0)
8. TEST-AC4-001: Password hashing tests (P0)

Priority 4 (NFR Concerns): 3 fixes
9. NFR-PERF-001: Missing caching (performance CONCERNS)
10. NFR-SCALE-001: No horizontal scaling (scalability CONCERNS)
11. NFR-USE-001: API response format (usability CONCERNS)

Priority 5 (Trace Gaps): 1 fix
12. TRACE-AC4: Implement bcrypt hashing (partial coverage)

Priority 6 (Medium Severity): 2 fixes
13. ERR-001: Missing error handling
14. DOC-001: Missing API documentation

Priority 7 (Low Severity): 1 fix
15. STYLE-001: Inconsistent formatting

Total: 15 fixes
```

---

## Guardrail Considerations

After prioritization, check if fix plan exceeds guardrails:

**Guardrails:**
- Max 10 files per session
- Max 800 diff lines per session

**If exceeded:**

**Option 1: Split by Priority Groups**
```
Session 1: Priority 1-2 (5 fixes, ~300 lines, 4 files)
Session 2: Priority 3-4 (6 fixes, ~400 lines, 5 files)
Session 3: Priority 5-7 (4 fixes, ~200 lines, 3 files)
```

**Option 2: Split Within Priority**
```
Session 1: Priority 1 + Priority 2 (5 fixes)
Session 2: Priority 3 (3 fixes)
Session 3: Priority 4-7 (7 fixes)
```

**Option 3: Escalate to User**
```
⚠️ Fix plan exceeds guardrails
Fixes: 15 total
Files: 12 (limit: 10)
Diff lines: ~900 (limit: 800)

Options:
1. Split into 2-3 sessions
2. Override guardrails (requires approval)
3. Defer low priority fixes (P5-7)
```

---

## Special Cases

### Case 1: Conflicting Fixes

If two fixes conflict (can't both be applied):

**Resolution:**
1. Apply higher priority fix first
2. Re-assess if lower priority still needed
3. Document conflict in fix summary
4. Escalate to user if critical

**Example:**
```
P1: SEC-001 requires refactoring auth module
P3: TEST-AUTH-001 tests current auth module

Resolution: Apply P1 (refactor), then update P3 tests for new implementation
```

### Case 2: Dependencies Between Fixes

If fix B depends on fix A:

**Resolution:**
1. Ensure A has higher priority than B, OR
2. If B has higher priority, apply B which implicitly applies A

**Example:**
```
P3: Add tests for rate limiting
P4: Implement rate limiting

Resolution: Apply P4 first (implement), then P3 (test)
Better: Re-prioritize P4 to P2 if NFR FAIL
```

### Case 3: Architectural Changes Required

If fix requires architectural refactoring:

**Resolution:**
1. Check if fix can be done without architecture change
2. If not, mark as "requires_architecture_change"
3. Escalate to user
4. Skip for now, continue with other fixes

**Example:**
```
P1: SEC-001 requires moving to microservices architecture

Resolution: Escalate to user, too complex for automated fix
```

### Case 4: Multiple Files for One Fix

If single fix requires modifying many files:

**Resolution:**
1. Group all file changes as single fix
2. Count toward total files modified
3. If exceeds guardrails, escalate

**Example:**
```
P1: SEC-001 requires updating validation in 8 API files

Resolution: Single fix, but 8 files
If guardrail = 10 files, allow (within limit)
If guardrail = 5 files, escalate or split
```

---

## Testing Priority Rules

To verify deterministic behavior:

**Test Case 1: Same Gate, Same Order**
```
Input: quality-gate-v1.yaml
Output: [fix-1, fix-2, fix-3, ...]
Run again with same input → Same output
```

**Test Case 2: Different Issues, Correct Order**
```
Input: Gate with P1 + P3 + P5
Output: [P1 fixes, P3 fixes, P5 fixes]
Verify: All P1 before all P3 before all P5
```

**Test Case 3: Tiebreaker Works**
```
Input: Gate with 3 P1 security issues
Output: [SEC-001, SEC-002, SEC-003]
Verify: Alphabetical order
```

---

## Quick Reference

### Priority Summary

1. **High severity** - Security, data loss, critical bugs
2. **NFR failures** - Status = FAIL
3. **Coverage gaps** - P0 scenarios
4. **NFR concerns** - Status = CONCERNS
5. **Trace gaps** - None/partial coverage
6. **Medium severity** - Non-critical issues
7. **Low severity** - Minor improvements

### Tiebreaker Order

1. Priority number (1-7)
2. Category severity (security > performance > ...)
3. Issue ID (alphabetical)

### Guardrails

- Max 10 files
- Max 800 lines
- Split if exceeded

---
