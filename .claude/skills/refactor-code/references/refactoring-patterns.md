# Refactoring Patterns Guide

## Purpose

Common refactoring patterns with concrete examples for identifying and applying code improvements.

---

## Pattern 1: Extract Method

**When to use:**
- Method >50 lines
- Complex logic block that can be named
- Repeated code blocks
- Multiple levels of abstraction in one method

**Risk Level:** Medium

**Example:**

```typescript
// Before - Long signup route handler
async function signup(req: Request, res: Response) {
  // Validation (15 lines)
  if (!req.body.email) {
    return res.status(400).json({ error: 'Email required' });
  }
  if (!isValidEmail(req.body.email)) {
    return res.status(400).json({ error: 'Invalid email format' });
  }
  if (!req.body.password) {
    return res.status(400).json({ error: 'Password required' });
  }
  if (req.body.password.length < 8) {
    return res.status(400).json({ error: 'Password too short' });
  }
  // ... more validation

  // Business logic (20 lines)
  const existing = await db.users.findOne({ email: req.body.email });
  if (existing) {
    return res.status(409).json({ error: 'Email already exists' });
  }

  const hashedPassword = await bcrypt.hash(req.body.password, 12);
  const user = await db.users.create({
    email: req.body.email,
    password: hashedPassword,
  });

  const token = jwt.sign({ userId: user.id }, JWT_SECRET);
  res.status(201).json({ token, user });
}

// After - Extracted methods
async function signup(req: Request, res: Response) {
  const validation = validateSignupRequest(req.body);
  if (!validation.valid) {
    return res.status(400).json(validation.errors);
  }

  const result = await createUser(req.body);
  if (!result.success) {
    return res.status(result.statusCode).json({ error: result.error });
  }

  const token = generateToken(result.user);
  res.status(201).json({ token, user: result.user });
}
```

**Benefits:**
- Improved readability (high-level flow clear)
- Better testability (validate/create/generate independently testable)
- Reusability (validation/token generation reusable)
- Single Responsibility Principle

---

## Pattern 2: Extract Variable

**When to use:**
- Complex expression used multiple times
- Long conditional expressions
- Magic numbers or strings
- Expression that needs a descriptive name

**Risk Level:** Low

**Example:**

```typescript
// Before - Complex conditional
if (user.role === 'admin' &&
    user.permissions.includes('write') &&
    !user.suspended &&
    user.emailVerified) {
  performWriteOperation();
}

if (user.role === 'admin' &&
    user.permissions.includes('write') &&
    !user.suspended &&
    user.emailVerified) {
  performDeleteOperation();
}

// After - Extracted variable
const canModifyContent = user.role === 'admin' &&
                          user.permissions.includes('write') &&
                          !user.suspended &&
                          user.emailVerified;

if (canModifyContent) {
  performWriteOperation();
}

if (canModifyContent) {
  performDeleteOperation();
}
```

**Benefits:**
- Self-documenting code (intention clear)
- Reduced duplication
- Easier to modify logic (change in one place)
- Better readability

---

## Pattern 3: Rename

**When to use:**
- Variable/function name unclear
- Abbreviated names without context
- Misleading names
- Inconsistent naming conventions

**Risk Level:** Low

**Example:**

```typescript
// Before - Unclear naming
const u = await findUser(email);
if (!u) return null;

const p = await bcrypt.hash(pwd, 12);
const r = await db.users.create({ email: e, password: p });

return { u: r, t: generateToken(r.id) };

// After - Descriptive naming
const existingUserWithEmail = await findUserByEmail(email);
if (!existingUserWithEmail) return null;

const hashedPassword = await hashPassword(password);
const createdUser = await db.users.create({
  email: email,
  password: hashedPassword
});

return {
  user: createdUser,
  token: generateToken(createdUser.id)
};
```

**Benefits:**
- Self-documenting code
- Reduced cognitive load
- Easier for new developers
- Clearer intent

---

## Pattern 4: Remove Duplication

**When to use:**
- Same code appears 2+ times
- Similar logic with minor variations
- Copy-paste code
- Repeated patterns

**Risk Level:** Low to Medium

**Example:**

```typescript
// Before - Duplicated password hashing
// In signup.service.ts
const hashedPassword = await bcrypt.hash(password, 12);

// In password-reset.service.ts
const hashedPassword = await bcrypt.hash(newPassword, 12);

// In update-password.service.ts
const hashedPassword = await bcrypt.hash(updatedPassword, 12);

// After - Extracted to utility
// In password.util.ts
const BCRYPT_COST = 12;

export async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, BCRYPT_COST);
}

// In services
const hashedPassword = await hashPassword(password);
const hashedPassword = await hashPassword(newPassword);
const hashedPassword = await hashPassword(updatedPassword);
```

**Benefits:**
- Single source of truth
- Easier to update (change once)
- Consistent behavior
- Testable in isolation

---

## Pattern 5: Simplify Conditionals

**When to use:**
- Nested if/else chains (>3 levels)
- Complex boolean logic
- Multiple return statements
- Guard clauses missing

**Risk Level:** Medium

**Example:**

```typescript
// Before - Nested conditionals
function processUser(user: User) {
  if (user) {
    if (user.active) {
      if (user.emailVerified) {
        if (user.role === 'admin') {
          return 'admin';
        } else {
          return 'user';
        }
      } else {
        throw new Error('Email not verified');
      }
    } else {
      throw new Error('User inactive');
    }
  } else {
    throw new Error('User not found');
  }
}

// After - Guard clauses + early returns
function processUser(user: User) {
  if (!user) {
    throw new Error('User not found');
  }

  if (!user.active) {
    throw new Error('User inactive');
  }

  if (!user.emailVerified) {
    throw new Error('Email not verified');
  }

  return user.role === 'admin' ? 'admin' : 'user';
}
```

**Benefits:**
- Reduced nesting (easier to read)
- Clearer error handling
- Easier to test each branch
- Improved maintainability

---

## Pattern 6: Extract Class

**When to use:**
- Class with too many responsibilities (>200 lines)
- Class has multiple unrelated methods
- Class has groups of related fields
- Class violates Single Responsibility Principle

**Risk Level:** High

**Example:**

```typescript
// Before - God object
class UserService {
  async signup(email: string, password: string) { /* ... */ }
  async login(email: string, password: string) { /* ... */ }
  async logout(userId: string) { /* ... */ }

  async sendVerificationEmail(email: string) { /* ... */ }
  async sendPasswordResetEmail(email: string) { /* ... */ }
  async sendWelcomeEmail(email: string) { /* ... */ }

  async hashPassword(password: string) { /* ... */ }
  async comparePasswords(plain: string, hashed: string) { /* ... */ }
  async generateToken(userId: string) { /* ... */ }
  async verifyToken(token: string) { /* ... */ }
}

// After - Extracted classes
class UserAuthService {
  constructor(
    private passwordService: PasswordService,
    private tokenService: TokenService,
    private emailService: EmailService
  ) {}

  async signup(email: string, password: string) { /* ... */ }
  async login(email: string, password: string) { /* ... */ }
  async logout(userId: string) { /* ... */ }
}

class EmailService {
  async sendVerificationEmail(email: string) { /* ... */ }
  async sendPasswordResetEmail(email: string) { /* ... */ }
  async sendWelcomeEmail(email: string) { /* ... */ }
}

class PasswordService {
  async hash(password: string) { /* ... */ }
  async compare(plain: string, hashed: string) { /* ... */ }
}

class TokenService {
  generate(userId: string) { /* ... */ }
  verify(token: string) { /* ... */ }
}
```

**Benefits:**
- Single Responsibility Principle
- Easier to test (smaller units)
- Improved modularity
- Better dependency management

---

## Pattern 7: Inline

**When to use:**
- Method/variable adds no value
- Unnecessary indirection
- Single-use private method
- Overly generic abstraction

**Risk Level:** Low

**Example:**

```typescript
// Before - Unnecessary indirection
function getUserEmail(user: User): string {
  return user.email;
}

function processUser(user: User) {
  const email = getUserEmail(user);
  sendEmail(email);
}

// After - Inlined
function processUser(user: User) {
  sendEmail(user.email);
}
```

**Benefits:**
- Reduced complexity
- Fewer files/methods to maintain
- Clearer direct flow

---

## Pattern 8: Move Method

**When to use:**
- Method uses more features of another class
- Method doesn't belong in current class
- Misplaced functionality
- Cross-cutting concerns

**Risk Level:** Medium to High

**Example:**

```typescript
// Before - Method in wrong class
class User {
  id: string;
  email: string;
  passwordHash: string;

  // This method doesn't belong here
  async hashPassword(password: string): Promise<string> {
    return bcrypt.hash(password, 12);
  }

  async comparePassword(password: string): Promise<boolean> {
    return bcrypt.compare(password, this.passwordHash);
  }
}

// After - Moved to appropriate class
class PasswordService {
  async hash(password: string): Promise<string> {
    return bcrypt.hash(password, 12);
  }

  async compare(password: string, hash: string): Promise<boolean> {
    return bcrypt.compare(password, hash);
  }
}

class User {
  id: string;
  email: string;
  passwordHash: string;

  async verifyPassword(password: string, passwordService: PasswordService): Promise<boolean> {
    return passwordService.compare(password, this.passwordHash);
  }
}
```

**Benefits:**
- Better class cohesion
- Clearer responsibilities
- Improved testability
- Reusability

---

## Pattern Identification Checklist

Use this checklist to identify refactoring opportunities:

**Extract Method:**
- [ ] Method >50 lines
- [ ] Nested logic (>3 levels)
- [ ] Repeated code blocks
- [ ] Multiple abstractions in one method

**Extract Variable:**
- [ ] Complex expression used multiple times
- [ ] Long conditionals
- [ ] Magic numbers/strings
- [ ] Expression needs descriptive name

**Rename:**
- [ ] Single-letter variable names
- [ ] Abbreviated names unclear
- [ ] Misleading names
- [ ] Inconsistent naming

**Remove Duplication:**
- [ ] Same code 2+ times
- [ ] Copy-paste code
- [ ] Similar logic with variations
- [ ] Repeated patterns

**Simplify Conditionals:**
- [ ] Nested if/else >3 levels
- [ ] Complex boolean logic
- [ ] Multiple return statements
- [ ] Missing guard clauses

**Extract Class:**
- [ ] Class >200 lines
- [ ] Multiple responsibilities
- [ ] Groups of related fields/methods
- [ ] Violates Single Responsibility

**Inline:**
- [ ] Single-use method
- [ ] Unnecessary indirection
- [ ] No added value

**Move Method:**
- [ ] Method uses other class more
- [ ] Method doesn't fit current class
- [ ] Misplaced functionality

---

## Quick Reference: Risk by Pattern

| Pattern | Risk Level | Safe When |
|---------|-----------|-----------|
| Rename | Low | Good test coverage |
| Extract Variable | Low | Expression has no side effects |
| Inline | Low | Single usage, no side effects |
| Remove Duplication | Low-Med | Duplication truly identical |
| Extract Method | Medium | Method has clear boundary |
| Simplify Conditionals | Medium | Tests cover all branches |
| Move Method | Medium-High | Dependencies are clear |
| Extract Class | High | Class boundaries well-defined |

---

*Part of refactor-code skill - Quality Suite*
