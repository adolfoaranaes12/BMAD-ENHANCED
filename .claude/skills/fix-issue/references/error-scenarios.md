# Error Scenarios

How to handle complex situations that arise during bug fixing.

---

## Scenario 1: Cannot Reproduce Issue

**Situation:**
Reporter says bug exists, but you cannot make it happen in your environment.

**Why This Happens:**
- Environment differences (dev vs production)
- Different data (test data vs real user data)
- Timing/concurrency issues (race conditions)
- Cached data masking issue
- Issue already fixed but reporter not updated
- Vague or incorrect bug report

**How to Handle:**

**Step 1: Gather More Information**
```markdown
Questions to ask reporter:
1. What exact steps did you take?
2. What exact error message did you see?
3. Which environment? (dev/staging/production)
4. Which browser/client? (if applicable)
5. What data were you using?
6. When did this happen? (date/time)
7. Is it still happening?
8. Can you provide screenshot/video?
9. Can you provide request/response logs?
10. Can you try again now?
```

**Step 2: Try Different Environments**
```bash
# Try in different environments
npm test  # Test environment
npm run dev  # Development
npm run build && npm start  # Production build

# Try with different data
USE_PRODUCTION_DATA=true npm test

# Try with different config
NODE_ENV=production npm test
```

**Step 3: Document Unable to Reproduce**
```markdown
## Issue: Login fails with + symbol in email

**Status:** Unable to reproduce

**Attempts Made:**
1. ✅ Created test with "user+tag@example.com"
2. ✅ Ran test - test PASSES (issue doesn't occur)
3. ✅ Manual test - login succeeds
4. ✅ Checked validation code - allows + symbol

**Environment Checked:**
- ✅ Development
- ✅ Test
- ⚠️ Production (cannot access)

**Hypothesis:**
- Issue may be specific to production environment
- Issue may be fixed already in main branch
- Reporter may be on older version

**Questions for Reporter:**
1. Which version/commit are you using?
2. Can you provide the exact email that failed?
3. Can you try again with latest version?
4. Can you provide production logs?

**Next Steps:**
- Waiting for reporter response
- If reproducible with info, will fix immediately
- If not reproducible after follow-up, will close
```

---

## Scenario 2: Fix Introduces Regression

**Situation:**
Your fix works for the reported bug, but breaks existing functionality.

**Example:**
```typescript
// Original validation (too strict, rejects + in email)
const EMAIL_REGEX = /^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

// First fix attempt (too permissive, accepts invalid emails)
const EMAIL_REGEX = /^.+@.+$/;  // Accepts "@" as valid!

// Tests:
✓ Bug test passes (accepts user+tag@example.com) ✅
✗ "should reject @ alone" - NOW PASSES (should fail) ❌
✗ "should reject missing domain" - NOW PASSES (should fail) ❌
```

**How to Handle:**

**Step 1: Analyze the Regression**
```markdown
**Regression Analysis:**

**What broke:**
- Test "should reject @ alone" now passes (should fail)
- Test "should reject missing domain" now passes (should fail)

**Why it broke:**
- New regex /.+@.+$/ is too permissive
- Accepts any characters before and after @
- No validation of email structure

**Root cause:**
- Tried to fix one edge case (+symbol)
- Made validation too loose
```

**Step 2: Find Balance**
```typescript
// Goal: Accept + symbol BUT still validate properly

// Too strict (original)
/^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/  // No + symbol

// Too loose (first fix)
/^.+@.+$/  // Accepts anything

// Balanced (final fix)
/^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/  // Adds + and % to allowed chars
```

**Step 3: Validate All Cases**
```typescript
describe('Email validation (comprehensive)', () => {
  // Should accept (bug fix cases)
  it('should accept + symbol', () => {
    expect(EMAIL_REGEX.test('user+tag@example.com')).toBe(true);
  });

  it('should accept % symbol', () => {
    expect(EMAIL_REGEX.test('user%test@example.com')).toBe(true);
  });

  // Should still reject (regression prevention)
  it('should reject @ alone', () => {
    expect(EMAIL_REGEX.test('@')).toBe(false);
  });

  it('should reject missing domain', () => {
    expect(EMAIL_REGEX.test('user@')).toBe(false);
  });

  it('should reject missing local part', () => {
    expect(EMAIL_REGEX.test('@example.com')).toBe(false);
  });

  it('should reject no @ symbol', () => {
    expect(EMAIL_REGEX.test('userexample.com')).toBe(false);
  });
});
```

**Decision Framework:**
```markdown
When fix causes regression:

1. ✅ **Refine fix** if both requirements can be met
   - Example: More precise regex that handles both cases

2. ⚠️ **Accept breaking change** if old behavior was incorrect
   - Document why old behavior was wrong
   - Update tests to reflect correct behavior
   - Notify stakeholders of intentional change

3. ❌ **Revert fix** if regression is worse than original bug
   - Example: Security regression to fix cosmetic bug
   - Document why fix was reverted
   - Create task to find better solution
```

---

## Scenario 3: Multiple Root Causes

**Situation:**
Issue has multiple contributing factors, not just one root cause.

**Example:**
```
Issue: "Checkout sometimes fails with 500 error"

Investigation reveals:
1. Race condition when updating inventory
2. Missing error handling for out-of-stock
3. Validation doesn't check for negative quantities
4. Database transaction not used
```

**How to Handle:**

**Step 1: Prioritize Root Causes**
```markdown
**Priority 1 (Critical - Fix First):**
- Race condition causing data corruption
- Missing error handling causing 500 errors

**Priority 2 (Important - Fix Soon):**
- No validation for negative quantities
- Missing database transaction

**Priority 3 (Good to Have - Fix Later):**
- Better error messages
- Logging improvements
```

**Step 2: Fix One Root Cause at a Time**
```markdown
## Fix 1: Add error handling (prevents 500 errors)

Test:
```typescript
it('should return 400 when item out of stock', async () => {
  await Product.update(productId, { stock: 0 });

  const response = await checkout(orderId);

  expect(response.status).toBe(400);
  expect(response.error).toBe('Product out of stock');
});
```

Code:
```typescript
if (product.stock < quantity) {
  return { status: 400, error: 'Product out of stock' };
}
```

## Fix 2: Use database transaction (fixes race condition)

Test:
```typescript
it('should handle concurrent checkouts correctly', async () => {
  await Product.update(productId, { stock: 1 });

  const results = await Promise.all([
    checkout(order1Id),
    checkout(order2Id)
  ]);

  // Only one should succeed
  expect(results.filter(r => r.status === 200)).toHaveLength(1);
  expect(results.filter(r => r.status === 400)).toHaveLength(1);
});
```

Code:
```typescript
await db.transaction(async (trx) => {
  const product = await Product.findById(productId)
    .forUpdate()
    .transacting(trx);

  if (product.stock < quantity) {
    throw new OutOfStockError();
  }

  await Product.update(productId, {
    stock: product.stock - quantity
  }).transacting(trx);

  await Order.create({ productId, quantity }).transacting(trx);
});
```
```

**Step 3: Document All Root Causes**
```markdown
## Bug Fix: Checkout sometimes fails

**Root Causes Identified:** 4 total

**Fix 1: Added error handling**
- Date: 2025-01-15
- Addresses: 500 errors when out of stock
- Files: src/services/checkout.service.ts
- Tests: Added 3 tests

**Fix 2: Added database transaction**
- Date: 2025-01-15
- Addresses: Race condition on inventory
- Files: src/services/checkout.service.ts
- Tests: Added concurrency test

**Fix 3: Added quantity validation**
- Date: 2025-01-15
- Addresses: Negative quantities accepted
- Files: src/validators/order.validator.ts
- Tests: Added 2 tests

**Fix 4: Transaction rollback on error**
- Date: 2025-01-15
- Addresses: Partial checkouts on error
- Files: src/services/checkout.service.ts
- Tests: Added error handling test
```

---

## Scenario 4: Fix Requires Breaking Change

**Situation:**
Fixing the bug properly requires changing the API or behavior in a breaking way.

**Example:**
```
Bug: API returns inconsistent date formats (sometimes ISO string, sometimes timestamp)
Fix: Standardize to ISO 8601 strings
Impact: Clients expecting timestamps will break
```

**How to Handle:**

**Step 1: Assess Impact**
```markdown
**Breaking Change Assessment:**

**Change:** Standardize date format to ISO 8601

**Impact Analysis:**
- ✅ Internal services: No impact (all use ISO parser)
- ⚠️ Mobile app v2.x: Needs update (uses timestamp parser)
- ⚠️ Web app: Needs update (uses timestamp parser)
- ❌ External API clients: Unknown impact

**Risk Level:** HIGH
**Affected Users:** Potentially all external API clients
```

**Step 2: Choose Mitigation Strategy**

**Strategy A: Versioned API (Recommended)**
```typescript
// New endpoint with fix
app.get('/api/v2/orders', (req, res) => {
  const orders = await Order.findAll();
  res.json({
    orders: orders.map(o => ({
      ...o,
      createdAt: o.createdAt.toISOString()  // Always ISO string
    }))
  });
});

// Old endpoint (deprecated but functional)
app.get('/api/v1/orders', (req, res) => {
  const orders = await Order.findAll();
  res.json({
    orders: orders.map(o => ({
      ...o,
      createdAt: o.createdAt.getTime()  // Timestamp (legacy)
    }))
  });
});
```

**Strategy B: Gradual Migration**
```typescript
// Phase 1: Return both formats (transition period)
app.get('/api/orders', (req, res) => {
  const orders = await Order.findAll();
  res.json({
    orders: orders.map(o => ({
      ...o,
      createdAt: o.createdAt.toISOString(),  // New format
      createdAtTimestamp: o.createdAt.getTime()  // Deprecated
    }))
  });
});

// Phase 2 (after 6 months): Remove timestamp format
app.get('/api/orders', (req, res) => {
  const orders = await Order.findAll();
  res.json({
    orders: orders.map(o => ({
      ...o,
      createdAt: o.createdAt.toISOString()  // Only ISO string
    }))
  });
});
```

**Step 3: Communication Plan**
```markdown
## Breaking Change Communication

**To:** All API consumers
**Subject:** [Action Required] Date format standardization - Migration by 2025-07-01

**What's Changing:**
All API date fields will return ISO 8601 format (e.g., "2025-01-15T10:30:00Z")
instead of Unix timestamps (e.g., 1705318200000)

**Why:**
- Fixes inconsistent date formats across endpoints
- Aligns with industry standards (ISO 8601)
- Improves timezone handling

**Timeline:**
- 2025-01-15: v2 endpoint available with new format
- 2025-01-15 - 2025-07-01: Transition period (both formats available)
- 2025-07-01: v1 endpoint deprecated, only v2 available

**Action Required:**
1. Test your integration with new /api/v2/ endpoints
2. Update date parsing to handle ISO 8601 format
3. Migrate to v2 endpoints before 2025-07-01

**Migration Guide:**
- JavaScript: Use `new Date(isoString)` instead of `new Date(timestamp)`
- Python: Use `datetime.fromisoformat(iso_string)`
- Java: Use `Instant.parse(isoString)`

**Questions:** support@example.com
```

---

## Scenario 5: Root Cause is in Third-Party Library

**Situation:**
Bug is caused by third-party library, not your code.

**How to Handle:**

**Step 1: Verify It's Library Bug**
```typescript
// Create minimal reproduction without your code
describe('Library bug reproduction', () => {
  it('demonstrates Zod email validation issue', () => {
    const schema = z.object({
      email: z.string().email()
    });

    // This SHOULD pass per RFC 5322
    const result = schema.safeParse({
      email: 'user+tag@example.com'
    });

    expect(result.success).toBe(true);  // FAILS - library bug confirmed
  });
});
```

**Step 2: Check if Known Issue**
```bash
# Search library's GitHub issues
# https://github.com/colinhacks/zod/issues?q=email+plus+symbol

# Check if fixed in newer version
npm outdated zod
```

**Step 3: Choose Fix Strategy**

**Option A: Upgrade Library (if fixed)**
```bash
npm update zod@latest
npm test  # Verify fix works
```

**Option B: Workaround (if not fixed)**
```typescript
// Work around library limitation
const EMAIL_REGEX = /^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
const schema = z.object({
  email: z.string().regex(EMAIL_REGEX)  // Use custom validation
});
```

**Option C: File Issue + Workaround**
1. File issue in library's GitHub
2. Implement workaround
3. Add TODO to remove workaround when fixed

```typescript
// TODO: Remove when Zod email validation fixed
// See: https://github.com/colinhacks/zod/issues/12345
const EMAIL_REGEX = /^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
const schema = z.object({
  email: z.string().regex(EMAIL_REGEX)
});
```

---

## Decision Trees

### Should I Fix This Bug?

```
Is it actually a bug? (not expected behavior)
  ├─ NO → Close issue, explain expected behavior
  └─ YES → Continue

Can I reproduce it reliably?
  ├─ NO → Request more info (see Scenario 1)
  └─ YES → Continue

Is root cause in my code?
  ├─ NO → Third-party library issue (see Scenario 5)
  └─ YES → Continue

Will fix introduce breaking change?
  ├─ YES → Assess impact (see Scenario 4)
  └─ NO → Continue

Fix the bug!
```

### Should I Accept This Regression?

```
Does regression break security?
  └─ YES → Never accept, find different fix

Does regression break existing documented behavior?
  ├─ YES → Was documented behavior correct?
  │   ├─ NO → Accept, update docs
  │   └─ YES → Refine fix to handle both cases
  └─ NO → Continue

Does regression break undocumented behavior clients rely on?
  ├─ YES → Gradual migration or versioning required
  └─ NO → Accept regression, update tests

Is regression worse than original bug?
  ├─ YES → Revert fix, find better solution
  └─ NO → Accept regression
```

---

## Key Takeaways

1. **Not all issues are simple** - Complex scenarios require structured approach
2. **Document everything** - Especially when can't reproduce or has multiple causes
3. **Communicate breaking changes** - Give clients time to migrate
4. **One thing at a time** - Fix one root cause, validate, then move to next
5. **Know when to escalate** - Some issues need team discussion or architectural changes
