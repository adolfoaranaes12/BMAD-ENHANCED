# Debugging Techniques

Systematic approaches for identifying root causes when fixing issues.

---

## Technique 1: Binary Search Debugging

**When to Use:**
- Large codebase with unclear error source
- Regression introduced by recent changes
- Error occurs deep in call stack

**How it Works:**
1. Identify working version and broken version
2. Test midpoint commit between them
3. If midpoint works, bug is in second half
4. If midpoint broken, bug is in first half
5. Repeat until you find the exact commit

**Example:**
```bash
# Using git bisect
git bisect start
git bisect bad HEAD  # Current version is broken
git bisect good v1.2.0  # This version worked

# Git checks out middle commit
npm test  # Test if bug exists

git bisect good  # If works
# or
git bisect bad  # If broken

# Repeat until git identifies the exact commit
git bisect reset  # When done
```

---

## Technique 2: Rubber Duck Debugging

**When to Use:**
- Stuck on issue with no clear next step
- Code looks correct but doesn't work
- Need to clarify understanding

**How it Works:**
1. Explain code line-by-line to rubber duck (or person)
2. Describe what each line should do
3. Describe what it actually does
4. Often spot the issue while explaining

**Tips:**
- Don't skip "obvious" lines
- Explain assumptions out loud
- Question every assumption
- Write explanation if no duck available

---

## Technique 3: Add Logging

**When to Use:**
- Execution path unclear
- Need to see intermediate values
- Timing-related issues

**How it Works:**
1. Add console.log at key points
2. Log inputs, outputs, intermediate values
3. Add timestamps for timing issues
4. Run code and analyze logs

**Example:**
```typescript
export const processOrder = async (orderId: string) => {
  console.log('[1] Starting order processing:', orderId);

  const order = await Order.findById(orderId);
  console.log('[2] Order fetched:', order?.id, 'status:', order?.status);

  const items = await OrderItem.findByOrderId(orderId);
  console.log('[3] Items fetched:', items.length);

  const total = items.reduce((sum, item) => sum + item.price, 0);
  console.log('[4] Total calculated:', total);

  const payment = await Payment.create({ orderId, amount: total });
  console.log('[5] Payment created:', payment.id);

  await Order.update(orderId, { status: 'paid' });
  console.log('[6] Order updated to paid');

  return payment;
};
```

**Remove logging after debugging!**

---

## Technique 4: Use Debugger

**When to Use:**
- Need to inspect complex state
- Want to step through execution
- Multiple variables to check

**How it Works:**
1. Add `debugger;` statement or set breakpoint
2. Run in debug mode
3. Step through code line by line
4. Inspect variables at each step
5. Watch expressions evaluate

**Example:**
```typescript
export const calculateDiscount = (items: Item[], coupon?: Coupon) => {
  debugger;  // Execution pauses here

  let subtotal = items.reduce((sum, item) => sum + item.price, 0);

  if (coupon) {
    debugger;  // Check coupon state
    if (coupon.type === 'percentage') {
      subtotal *= (1 - coupon.value / 100);
    } else {
      subtotal -= coupon.value;
    }
  }

  return Math.max(0, subtotal);
};
```

**VS Code Debugger:**
```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Tests",
      "program": "${workspaceFolder}/node_modules/jest/bin/jest",
      "args": ["--runInBand", "--no-cache"],
      "console": "integratedTerminal"
    }
  ]
}
```

---

## Technique 5: Isolate the Problem

**When to Use:**
- Complex system with many components
- Unclear which component is failing
- Integration test failing

**How it Works:**
1. Create minimal reproduction case
2. Remove unrelated code
3. Stub out dependencies
4. Test isolated component
5. Add complexity back gradually

**Example:**
```typescript
// Full system test failing - too complex
test('checkout flow', async () => {
  await createUser();
  await login();
  await addToCart();
  await applyDiscount();
  await enterShipping();
  await processPayment();  // Fails here - but why?
  await confirmOrder();
});

// Isolate payment processing
test('payment processing isolated', async () => {
  const mockOrder = { id: '123', total: 100 };
  const mockPaymentMethod = { type: 'card', token: 'tok_123' };

  const result = await processPayment(mockOrder, mockPaymentMethod);

  expect(result).toHaveProperty('id');
  expect(result.status).toBe('succeeded');
});
```

---

## Technique 6: Diff Against Working Version

**When to Use:**
- Regression introduced recently
- Code worked before, broken now
- Know which version worked

**How it Works:**
1. Identify last known working version
2. Compare current code with working version
3. Focus on changed areas
4. Identify suspicious changes

**Example:**
```bash
# Compare current branch with last working version
git diff v1.2.0 src/services/payment.service.ts

# Or compare with specific commit
git diff abc123 -- src/services/payment.service.ts

# Show changes in specific function
git log -p -S "processPayment" -- src/services/payment.service.ts
```

---

## Technique 7: Check Assumptions

**When to Use:**
- Code looks correct but doesn't work
- "This should work" but doesn't
- Intermittent failures

**How it Works:**
1. List all assumptions code makes
2. Validate each assumption with assertion or test
3. Check edge cases for each assumption
4. Question implicit assumptions

**Example:**
```typescript
// Assumption: user always has email
const sendWelcomeEmail = (user: User) => {
  // Add assertion to check assumption
  if (!user.email) {
    throw new Error('User must have email');
  }

  return sendEmail(user.email, 'Welcome!');
};

// Assumption: array is never empty
const getFirstItem = (items: Item[]) => {
  // Check assumption
  if (items.length === 0) {
    throw new Error('Items array is empty');
  }

  return items[0];
};

// Assumption: environment variable exists
const initDatabase = () => {
  const dbUrl = process.env.DATABASE_URL;

  // Validate assumption
  if (!dbUrl) {
    throw new Error('DATABASE_URL environment variable required');
  }

  return new Database(dbUrl);
};
```

---

## Technique 8: Read Error Messages Carefully

**When to Use:**
- Always! First step in any debugging

**How it Works:**
1. Read entire error message, not just first line
2. Note file path and line number
3. Read stack trace from bottom to top
4. Identify where error originated
5. Google exact error message

**Example:**
```
TypeError: Cannot read property 'name' of undefined
    at getUserName (src/services/user.service.ts:45:23)
    at formatUser (src/utils/formatter.ts:12:18)
    at handleRequest (src/controllers/user.controller.ts:78:25)
    at Layer.handle [as handle_request] (node_modules/express/lib/router/layer.js:95:5)
```

**Analysis:**
- Error: Trying to read `.name` property of undefined
- Where: user.service.ts:45:23
- Context: Called from formatter.ts:12, controller.ts:78
- **Start debugging at user.service.ts line 45**

---

## Technique 9: Reproduce Reliably

**When to Use:**
- Intermittent or flaky issue
- "Works on my machine"
- Timing-dependent bug

**How it Works:**
1. Document exact steps to reproduce
2. Note environment details
3. Try to make failure consistent
4. Write failing test
5. Fix becomes easier once reproduced reliably

**Example:**
```typescript
// Document reproduction steps
describe('Bug: Order total incorrect', () => {
  it('should calculate total correctly with concurrent updates', async () => {
    // Setup: Create order
    const order = await Order.create({ items: [] });

    // Reproduce: Add items concurrently (race condition)
    await Promise.all([
      OrderItem.create({ orderId: order.id, price: 10 }),
      OrderItem.create({ orderId: order.id, price: 20 }),
      OrderItem.create({ orderId: order.id, price: 30 })
    ]);

    // Calculate total
    const total = await calculateOrderTotal(order.id);

    // Expected: 60, Actual: varies (30, 40, 50, or 60)
    expect(total).toBe(60);
  });
});
```

---

## Technique 10: Read the Documentation

**When to Use:**
- Using library or API
- Unexpected behavior from third-party code
- Complex feature not working as expected

**How it Works:**
1. Read official documentation thoroughly
2. Check version-specific docs (versions differ!)
3. Look for "gotchas" or "known issues"
4. Check GitHub issues for similar problems
5. Read migration guides if recently upgraded

**Example:**
```typescript
// Bug: Zod email validation rejects valid emails
const schema = z.object({
  email: z.string().email()  // Rejects "user+tag@example.com"
});

// Read Zod docs:
// ".email() - Validates the string is an email (note: this uses a simple
//  regex and only covers most common cases)"

// Solution: Docs warn it's simple regex, use custom validation
const EMAIL_REGEX = /^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
const schema = z.object({
  email: z.string().regex(EMAIL_REGEX)
});
```

---

## Debugging Workflow (Systematic Approach)

For any bug, follow this systematic workflow:

1. **Read error message** (Technique 8)
2. **Reproduce reliably** (Technique 9)
3. **Isolate the problem** (Technique 5)
4. **Add logging** or use debugger (Techniques 3, 4)
5. **Check assumptions** (Technique 7)
6. **Compare with working version** if regression (Technique 6)
7. **Read documentation** if third-party code (Technique 10)
8. **Explain to rubber duck** if stuck (Technique 2)

Most bugs are found within steps 1-5. Steps 6-8 are for stubborn bugs.

---

## Tips for Effective Debugging

- **Start with simplest explanation** - Don't assume complex causes
- **Change one thing at a time** - Multiple changes hide the fix
- **Write tests as you debug** - Prevents regression
- **Take breaks** - Fresh eyes spot obvious issues
- **Ask for help** - Another person sees differently
- **Keep notes** - Track what you've tried
- **Read error messages completely** - All info is there
- **Trust the error message** - Computer is usually right about what broke

---

## When Debugging Takes Too Long

If debugging exceeds reasonable time:
1. Ask colleague for fresh perspective
2. Take break and come back later
3. Try rubber duck debugging
4. Search for similar issues online
5. Consider if bug is in your mental model, not code
6. Escalate if beyond your expertise level
