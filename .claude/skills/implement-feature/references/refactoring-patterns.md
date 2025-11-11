# Refactoring Patterns

## Purpose

Common refactoring techniques for TDD refactor phase while keeping tests green.

---

## Pattern 1: Extract Method

### Before
```typescript
export const login = async (req: Request, res: Response) => {
  try {
    // Validation logic inline
    if (!req.body.email) {
      return res.status(400).json({ error: 'Email required' });
    }
    if (!req.body.password) {
      return res.status(400).json({ error: 'Password required' });
    }

    // Authentication logic
    const user = await User.findByEmail(req.body.email);
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });

    const valid = await bcrypt.compare(req.body.password, user.password_hash);
    if (!valid) return res.status(401).json({ error: 'Invalid credentials' });

    const token = jwt.sign({ userId: user.id }, SECRET);
    return res.status(200).json({ token });
  } catch (error) {
    return res.status(500).json({ error: 'Internal error' });
  }
};
```

### After
```typescript
// Extracted validation
function validateLoginInput(body: any) {
  if (!body.email) throw new ValidationError('Email required');
  if (!body.password) throw new ValidationError('Password required');
  return { email: body.email, password: body.password };
}

// Extracted authentication
async function authenticateUser(email: string, password: string) {
  const user = await User.findByEmail(email);
  if (!user) return null;

  const valid = await bcrypt.compare(password, user.password_hash);
  return valid ? user : null;
}

// Simplified controller
export const login = async (req: Request, res: Response) => {
  try {
    const { email, password } = validateLoginInput(req.body);
    const user = await authenticateUser(email, password);

    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign({ userId: user.id }, SECRET);
    return res.status(200).json({ token });
  } catch (error) {
    if (error instanceof ValidationError) {
      return res.status(400).json({ error: error.message });
    }
    return res.status(500).json({ error: 'Internal error' });
  }
};
```

**Run tests after refactor to verify still green!**

---

## Pattern 2: Remove Duplication

### Before
```typescript
async function loginUser(email: string, password: string) {
  const user = await User.findByEmail(email);
  if (!user) return null;
  // Logging
  await Log.create({
    action: 'login_attempt',
    email,
    success: false,
    timestamp: new Date()
  });
  return null;
}

async function logoutUser(userId: string) {
  const user = await User.findById(userId);
  if (!user) return null;
  // Logging
  await Log.create({
    action: 'logout',
    userId,
    success: true,
    timestamp: new Date()
  });
  return true;
}
```

### After
```typescript
// Extracted common logging
async function logAction(action: string, data: object, success: boolean) {
  await Log.create({
    action,
    ...data,
    success,
    timestamp: new Date()
  });
}

async function loginUser(email: string, password: string) {
  const user = await User.findByEmail(email);
  if (!user) {
    await logAction('login_attempt', { email }, false);
    return null;
  }
  await logAction('login_attempt', { email, userId: user.id }, true);
  return user;
}

async function logoutUser(userId: string) {
  const user = await User.findById(userId);
  if (!user) return null;
  await logAction('logout', { userId }, true);
  return true;
}
```

---

## Pattern 3: Simplify Conditionals

### Before
```typescript
function calculateDiscount(user: User, amount: number): number {
  if (user.isPremium) {
    if (amount > 100) {
      return amount * 0.20;
    } else if (amount > 50) {
      return amount * 0.15;
    } else {
      return amount * 0.10;
    }
  } else {
    if (amount > 100) {
      return amount * 0.10;
    } else if (amount > 50) {
      return amount * 0.05;
    } else {
      return 0;
    }
  }
}
```

### After
```typescript
function calculateDiscount(user: User, amount: number): number {
  const tier = user.isPremium ? 'premium' : 'regular';

  const discounts = {
    premium: { high: 0.20, medium: 0.15, low: 0.10 },
    regular: { high: 0.10, medium: 0.05, low: 0.00 }
  };

  if (amount > 100) return amount * discounts[tier].high;
  if (amount > 50) return amount * discounts[tier].medium;
  return amount * discounts[tier].low;
}
```

---

## Pattern 4: Replace Magic Numbers

### Before
```typescript
function generateToken(userId: string): string {
  return jwt.sign({ userId }, SECRET, { expiresIn: 86400 });
}

function isTokenExpired(token: DecodedToken): boolean {
  return Date.now() > (token.exp * 1000);
}

function rateLimitExceeded(attempts: number): boolean {
  return attempts >= 5;
}
```

### After
```typescript
const TOKEN_EXPIRY_SECONDS = 86400; // 24 hours
const MILLISECONDS_PER_SECOND = 1000;
const MAX_LOGIN_ATTEMPTS = 5;

function generateToken(userId: string): string {
  return jwt.sign({ userId }, SECRET, { expiresIn: TOKEN_EXPIRY_SECONDS });
}

function isTokenExpired(token: DecodedToken): boolean {
  return Date.now() > (token.exp * MILLISECONDS_PER_SECOND);
}

function rateLimitExceeded(attempts: number): boolean {
  return attempts >= MAX_LOGIN_ATTEMPTS;
}
```

---

## Pattern 5: Improve Naming

### Before
```typescript
async function process(d: any) {
  const r = await fetch(d.url);
  const j = await r.json();
  return j.data;
}

function calc(a: number, b: number): number {
  return a * b + (a * b * 0.1);
}
```

### After
```typescript
async function fetchUserData(request: UserRequest): Promise<UserData> {
  const response = await fetch(request.url);
  const json = await response.json();
  return json.data;
}

function calculatePriceWithTax(price: number, quantity: number): number {
  const TAX_RATE = 0.1;
  const subtotal = price * quantity;
  return subtotal + (subtotal * TAX_RATE);
}
```

---

## Refactoring Checklist

**Before Refactoring:**
- [ ] All tests are GREEN
- [ ] Identified code smell or improvement opportunity
- [ ] Know exactly what to refactor
- [ ] Have plan for how to refactor

**During Refactoring:**
- [ ] Make small, incremental changes
- [ ] Run tests after EACH change
- [ ] If tests fail, revert immediately
- [ ] Never refactor and add features simultaneously

**After Refactoring:**
- [ ] All tests still GREEN
- [ ] Code is more readable
- [ ] No duplication added
- [ ] Naming is clear
- [ ] Logic is simpler

---

## When to Stop Refactoring

**Stop when:**
- Tests are green and code is clear
- No obvious improvements remain
- Time budget exhausted (refactor later)
- Diminishing returns (over-engineering)

**Don't:**
- Refactor for its own sake
- Add unnecessary abstraction
- Optimize prematurely
- Change working code without tests

---

*Part of implement-feature skill - Development Suite*
