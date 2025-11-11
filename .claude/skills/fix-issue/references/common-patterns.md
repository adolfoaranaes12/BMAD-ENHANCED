# Common Issue Patterns

This reference file catalogs frequent bug patterns, their symptoms, debugging steps, and typical fixes.

---

## Pattern 1: Validation Too Strict

**Symptoms:**
- Valid input rejected
- Error message: "Invalid [field]"
- Works with some inputs, fails with others

**Debug Steps:**
1. Check validation schema/regex
2. Test with various valid inputs according to spec
3. Compare against standard (RFC, ISO, etc.)
4. Check if validation was copied from unreliable source

**Typical Fix:**
- Relax validation to match official specification
- Add tests for edge cases that should be valid
- Document which standard is being followed

**Example:**
```typescript
// Too strict: rejects + in email (valid per RFC 5322)
email: z.string().email()

// Correct: accepts RFC 5322-compliant emails
const EMAIL_REGEX = /^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
email: z.string().regex(EMAIL_REGEX)
```

---

## Pattern 2: Missing Error Handling

**Symptoms:**
- Uncaught exception crashes server
- 500 Internal Server Error with no details
- No error message in response
- Unhandled promise rejection

**Debug Steps:**
1. Check stack trace for unhandled error location
2. Identify missing try-catch blocks
3. Check for unhandled promise rejections
4. Look for synchronous code in async contexts

**Typical Fix:**
- Add try-catch blocks around error-prone operations
- Handle expected errors explicitly with appropriate status codes
- Add fallback error handler at application level
- Log errors for debugging while returning safe messages to client

**Example:**
```typescript
// Before: No error handling
export const getUser = async (req, res) => {
  const user = await User.findById(req.params.id);
  return res.json(user);
};

// After: Proper error handling
export const getUser = async (req, res) => {
  try {
    const user = await User.findById(req.params.id);

    if (!user) {
      return res.status(404).json({
        error: 'User not found',
        code: 'USER_NOT_FOUND'
      });
    }

    return res.json(user);
  } catch (error) {
    console.error('Error fetching user:', error);
    return res.status(500).json({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });
  }
};
```

---

## Pattern 3: Race Condition

**Symptoms:**
- Works sometimes, fails other times
- Flaky tests that pass/fail randomly
- Inconsistent behavior under load
- Issues disappear when debugging (timing changes)

**Debug Steps:**
1. Add logging with high-precision timestamps
2. Check for concurrent operations on shared state
3. Identify resources accessed without synchronization
4. Check for proper database transaction handling
5. Look for assumptions about operation order

**Typical Fix:**
- Wrap related operations in database transactions
- Use proper locking mechanisms (mutex, semaphore)
- Make operations atomic where possible
- Use queue for sequential processing
- Add appropriate rate limiting

**Example:**
```typescript
// Before: Race condition when checking and creating
const existingUser = await User.findByEmail(email);
if (!existingUser) {
  await User.create({ email }); // Another request might create between check and insert
}

// After: Use database constraint + error handling
try {
  await User.create({ email });
} catch (error) {
  if (error.code === 'UNIQUE_VIOLATION') {
    // User already exists, handle appropriately
    return res.status(409).json({ error: 'User already exists' });
  }
  throw error;
}

// Or: Use transaction with SELECT FOR UPDATE
await db.transaction(async (trx) => {
  const existing = await User.findByEmail(email).forUpdate().transacting(trx);
  if (!existing) {
    await User.create({ email }).transacting(trx);
  }
});
```

---

## Pattern 4: Memory Leak

**Symptoms:**
- Performance degrades over time
- Memory usage continuously increases
- Application crashes after running for hours/days
- Garbage collection pauses increase

**Debug Steps:**
1. Profile memory usage over time
2. Check for event listener leaks (listeners added but never removed)
3. Check for unclosed connections (database, file handles, network)
4. Check for large data structures held in closure scope
5. Look for global caches that grow unbounded

**Typical Fix:**
- Remove event listeners when component unmounts
- Close database connections and file handles
- Clear caches periodically or use LRU cache with size limit
- Use weak references for caches where appropriate
- Avoid holding references in closure scope unnecessarily

**Example:**
```typescript
// Before: Event listener leak
export const setupWebSocket = (socket) => {
  socket.on('message', handleMessage);
  socket.on('close', handleClose);
  // Never removes listeners!
};

// After: Proper cleanup
export const setupWebSocket = (socket) => {
  const messageHandler = (data) => handleMessage(data);
  const closeHandler = () => {
    handleClose();
    // Clean up listeners when done
    socket.off('message', messageHandler);
    socket.off('close', closeHandler);
  };

  socket.on('message', messageHandler);
  socket.on('close', closeHandler);

  return () => {
    // Return cleanup function for external use
    socket.off('message', messageHandler);
    socket.off('close', closeHandler);
  };
};

// Before: Unbounded cache
const userCache = {};
export const cacheUser = (id, user) => {
  userCache[id] = user; // Grows forever!
};

// After: LRU cache with limit
import LRU from 'lru-cache';
const userCache = new LRU({ max: 1000, ttl: 1000 * 60 * 5 });
export const cacheUser = (id, user) => {
  userCache.set(id, user); // Auto-evicts old entries
};
```

---

## Pattern 5: Wrong Assumptions

**Symptoms:**
- Works in development, fails in production
- Works for some users/data, not others
- Works on developer's machine, fails elsewhere
- Timing-dependent behavior

**Debug Steps:**
1. Check environment differences (NODE_ENV, config, dependencies)
2. Check data differences (test data vs real data)
3. Identify implicit assumptions in code
4. Add explicit assertions for assumptions
5. Check for hardcoded values that should be configurable

**Typical Fix:**
- Validate assumptions with explicit checks
- Handle null/undefined explicitly (don't assume data always present)
- Check data types and formats before processing
- Add comprehensive input validation
- Use environment variables for environment-specific values

**Example:**
```typescript
// Before: Assumes user always has profile
export const getUserProfile = async (userId) => {
  const user = await User.findById(userId);
  return {
    name: user.profile.name, // Crashes if profile is null!
    avatar: user.profile.avatar
  };
};

// After: Handles missing data
export const getUserProfile = async (userId) => {
  const user = await User.findById(userId);

  if (!user) {
    throw new Error('User not found');
  }

  return {
    name: user.profile?.name ?? 'Anonymous',
    avatar: user.profile?.avatar ?? '/default-avatar.png'
  };
};

// Before: Assumes production database URL present
const db = new Database(process.env.DATABASE_URL);

// After: Validates required config
const DATABASE_URL = process.env.DATABASE_URL;
if (!DATABASE_URL) {
  throw new Error('DATABASE_URL environment variable is required');
}
const db = new Database(DATABASE_URL);
```

---

## Pattern 6: Incorrect Async Handling

**Symptoms:**
- Operations complete in wrong order
- Data not available when expected
- "Cannot read property of undefined"
- Promise rejection unhandled

**Debug Steps:**
1. Check for missing `await` keywords
2. Check for `async` functions not being awaited
3. Look for Promise chains with missing error handlers
4. Check for mixing callbacks and promises

**Typical Fix:**
- Add `await` where async operations must complete
- Use `Promise.all()` for parallel operations
- Add `.catch()` or try-catch for error handling
- Convert callbacks to promises for consistency

**Example:**
```typescript
// Before: Missing await
export const createOrder = async (userId, items) => {
  const user = User.findById(userId); // Missing await!
  const order = await Order.create({
    userId: user.id, // user is Promise, not User object!
    items
  });
  return order;
};

// After: Proper await
export const createOrder = async (userId, items) => {
  const user = await User.findById(userId);
  const order = await Order.create({
    userId: user.id,
    items
  });
  return order;
};

// Before: Sequential when could be parallel
const user = await User.findById(userId);
const orders = await Order.findByUserId(userId);
const payments = await Payment.findByUserId(userId);

// After: Parallel operations
const [user, orders, payments] = await Promise.all([
  User.findById(userId),
  Order.findByUserId(userId),
  Payment.findByUserId(userId)
]);
```

---

## Pattern 7: Incorrect State Management

**Symptoms:**
- State changes not reflected in UI
- Stale data displayed
- State resets unexpectedly
- Multiple sources of truth conflict

**Debug Steps:**
1. Check if state updates are immutable
2. Verify state updates trigger re-renders
3. Look for direct state mutations
4. Check for state stored in multiple places

**Typical Fix:**
- Use immutable updates for state
- Centralize state in single source of truth
- Use state management library (Redux, MobX, Zustand)
- Ensure state changes trigger appropriate updates

**Example:**
```typescript
// Before: Direct mutation (doesn't trigger re-render in React)
const addItem = (item) => {
  cart.items.push(item); // Direct mutation!
  setCart(cart); // Same reference, no re-render
};

// After: Immutable update
const addItem = (item) => {
  setCart({
    ...cart,
    items: [...cart.items, item]
  });
};
```

---

## Using This Reference

When debugging an issue:
1. Check if symptoms match any pattern
2. Follow debug steps for that pattern
3. Apply typical fix (adapted to your context)
4. Always validate fix doesn't introduce regressions
5. Add tests to prevent regression of this pattern

Remember: These are **patterns**, not exact solutions. Adapt them to your specific context.
