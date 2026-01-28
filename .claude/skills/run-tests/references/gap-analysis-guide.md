# Coverage Gap Analysis Guide

## Purpose

Analyze uncovered code, categorize by type and criticality, and prioritize for testing.

---

## Gap Categories

### Category 1: Error Handling

**What:** Try-catch blocks, error responses, exception handling

**Example:**
```typescript
try {
  await service.doSomething();
} catch (error) {
  console.error('Error:', error);  // ❌ Uncovered
  return res.status(500).json({ error: 'Internal error' });
}
```

**Why Test:** Expected errors should be handled gracefully

**Priority:** HIGH

---

### Category 2: Edge Cases

**What:** Boundary conditions, unusual inputs, rare scenarios

**Example:**
```typescript
if (user.lastLogin && Date.now() - user.lastLogin > MAX_AGE) {
  return res.status(401).json({ error: 'Session expired' });  // ❌ Uncovered
}
```

**Why Test:** Edge cases often expose bugs

**Priority:** HIGH to MEDIUM

---

### Category 3: Rare Branches

**What:** Environment-specific code, debug code, development paths

**Example:**
```typescript
if (process.env.NODE_ENV === 'development') {  // ❌ Uncovered
  console.log('Debug info');
}
```

**Why Test:** Less critical, rarely executed

**Priority:** LOW

---

### Category 4: Dead Code

**What:** Unreachable code, impossible conditions

**Example:**
```typescript
if (false) {  // ❌ Uncovered (impossible)
  doSomething();
}
```

**Why Test:** Don't test - remove the code!

**Priority:** N/A (should be removed)

---

## Criticality Assessment

### Critical (Must Test)

**Security-related:**
- Authentication logic
- Authorization checks
- Data encryption/decryption
- Password handling
- Token generation/validation

**Data integrity:**
- Database transactions
- Data validation
- Payment processing
- User data deletion/modification

### High (Should Test)

**Error handling:**
- Expected errors (database, network)
- Invalid input handling
- State transitions
- Business logic edge cases

### Medium (Nice to Test)

**Supporting code:**
- Logging statements
- Non-critical error handling
- Minor edge cases
- Convenience methods

### Low (Optional)

**Rarely executed:**
- Debug code
- Development-only code
- Trivial getters/setters
- Framework integration code

---

## Gap Analysis Process

### Step 1: Identify Uncovered Lines

```json
{
  "file": "src/controllers/auth.controller.ts",
  "uncovered_lines": [48, 49, 50, 67],
  "total_lines": 120,
  "covered_lines": 116,
  "coverage_percent": 96.67
}
```

### Step 2: Extract Code Context

```typescript
// Lines 48-50 (uncovered)
if (!isDatabaseConnected()) {
  return res.status(503).json({ error: 'Service unavailable' });
}
```

### Step 3: Categorize

**Category:** Error Handling
**Scenario:** Database connection failure

### Step 4: Assess Criticality

**Question checklist:**
- Is this security-related? No
- Does it affect data integrity? No
- Is it expected in production? Yes (databases can fail)
- What's the impact if untested? Medium (503 errors might not work correctly)

**Criticality:** HIGH

### Step 5: Create Gap Record

```json
{
  "id": 1,
  "file": "src/controllers/auth.controller.ts",
  "lines": "48-50",
  "category": "error_handling",
  "criticality": "HIGH",
  "description": "Database connection error handling",
  "impact": "Service may not return correct 503 status on DB failure",
  "test_suggestion": "Mock database connection failure, verify 503 response"
}
```

---

## Gap Prioritization

### Priority 1: Critical Gaps (Fix Now)

- Security vulnerabilities
- Data integrity issues
- Payment processing
- Authentication/authorization

### Priority 2: High Gaps (Fix Soon)

- Error handling for expected errors
- Business logic edge cases
- State transitions
- Important validation

### Priority 3: Medium Gaps (Fix Eventually)

- Non-critical error handling
- Logging failures
- Minor edge cases
- Less important validation

### Priority 4: Low Gaps (Optional)

- Debug code
- Development-only paths
- Trivial code
- Framework code

---

## Gap Report Format

```markdown
## Coverage Gap Analysis

**File:** src/controllers/auth.controller.ts
**Coverage:** 96.67% (116/120 lines)
**Uncovered Lines:** 48-50, 67
**Gaps Identified:** 2

---

### Gap 1: Database Connection Error Handling

**Lines:** 48-50
**Category:** Error Handling
**Criticality:** HIGH

**Code:**
```typescript
if (!isDatabaseConnected()) {
  return res.status(503).json({ error: 'Service unavailable' });
}
```

**Why Uncovered:**
- No test mocks database connection failure
- Rare scenario but important for production

**Impact:**
- Users may get wrong error code
- Monitoring alerts may not trigger correctly

**Suggested Test:**
```typescript
it('should return 503 when database unavailable', async () => {
  jest.spyOn(db, 'isConnected').mockReturnValue(false);
  const response = await request(app).post('/api/auth/login')...
  expect(response.status).toBe(503);
});
```

---

### Gap 2: Unexpected Error Logging

**Lines:** 67
**Category:** Error Handling
**Criticality:** MEDIUM

**Code:**
```typescript
catch (error) {
  console.error('Unexpected error:', error);
  return res.status(500).json({ error: 'Internal error' });
}
```

**Why Uncovered:**
- No test triggers unexpected errors
- Catch-all for unforeseen issues

**Impact:**
- Unknown if error logging works
- 500 responses might not format correctly

**Suggested Test:**
```typescript
it('should return 500 for unexpected errors', async () => {
  jest.spyOn(authService, 'login').mockRejectedValue(new Error('Unexpected'));
  const response = await request(app).post('/api/auth/login')...
  expect(response.status).toBe(500);
});
```
```

---

## Decision Trees

### Should I Test This Uncovered Code?

```
Is it security-related?
├─ YES → Test (CRITICAL)
└─ NO
   ├─ Is it data/payment-related?
   │  ├─ YES → Test (CRITICAL)
   │  └─ NO
   │     ├─ Is it error handling?
   │     │  ├─ YES → Test if error is expected (HIGH)
   │     │  └─ NO → Is it business logic?
   │     │     ├─ YES → Test if important edge case (HIGH/MEDIUM)
   │     │     └─ NO → Is it debug/dev code?
   │        ├─ YES → Don't test (LOW)
   │        └─ NO → Test if time allows (MEDIUM)
```

---

## Quick Reference

**Category by Pattern:**
- `catch (error)` → Error Handling (HIGH)
- `if (edge case)` → Edge Case (HIGH/MEDIUM)
- `if (process.env.NODE_ENV)` → Rare Branch (LOW)
- `if (false)` → Dead Code (REMOVE)

**Criticality by Impact:**
- Security/payment → CRITICAL
- Data integrity → CRITICAL
- Expected errors → HIGH
- Edge cases → HIGH/MEDIUM
- Logging → MEDIUM
- Debug code → LOW

---

*Part of run-tests skill - Development Suite*
