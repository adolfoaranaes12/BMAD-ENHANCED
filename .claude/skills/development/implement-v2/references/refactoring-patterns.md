# Refactoring Patterns

## Common Refactorings

### Extract Function

**When:** Code block appears multiple times or does something distinct

**Before:**
```typescript
function processOrder(order: Order) {
  // Calculate total
  let total = 0;
  for (const item of order.items) {
    total += item.price * item.quantity;
  }

  // Apply discount
  if (order.customer.isPremium) {
    total = total * 0.9;
  }

  return total;
}
```

**After:**
```typescript
function processOrder(order: Order) {
  const subtotal = calculateSubtotal(order.items);
  const total = applyDiscount(subtotal, order.customer);
  return total;
}

function calculateSubtotal(items: OrderItem[]): number {
  return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
}

function applyDiscount(amount: number, customer: Customer): number {
  return customer.isPremium ? amount * 0.9 : amount;
}
```

---

### Rename Variable/Function

**When:** Name doesn't clearly express intent

**Before:**
```typescript
function calc(u: User, o: Order): number {
  const t = o.items.reduce((s, i) => s + i.p * i.q, 0);
  return u.premium ? t * 0.9 : t;
}
```

**After:**
```typescript
function calculateOrderTotal(user: User, order: Order): number {
  const subtotal = order.items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );
  return user.isPremium ? subtotal * 0.9 : subtotal;
}
```

---

### Replace Conditional with Polymorphism

**When:** Complex conditional logic based on type

**Before:**
```typescript
function calculateShipping(order: Order): number {
  if (order.shippingMethod === 'standard') {
    return order.weight * 0.5;
  } else if (order.shippingMethod === 'express') {
    return order.weight * 1.5 + 10;
  } else if (order.shippingMethod === 'overnight') {
    return order.weight * 3.0 + 25;
  }
  return 0;
}
```

**After:**
```typescript
interface ShippingMethod {
  calculateCost(weight: number): number;
}

class StandardShipping implements ShippingMethod {
  calculateCost(weight: number): number {
    return weight * 0.5;
  }
}

class ExpressShipping implements ShippingMethod {
  calculateCost(weight: number): number {
    return weight * 1.5 + 10;
  }
}

class OvernightShipping implements ShippingMethod {
  calculateCost(weight: number): number {
    return weight * 3.0 + 25;
  }
}

function calculateShipping(order: Order): number {
  return order.shippingMethod.calculateCost(order.weight);
}
```

---

### Simplify Conditional

**When:** Nested or complex boolean logic

**Before:**
```typescript
function canProcessOrder(order: Order, user: User): boolean {
  if (order.items.length > 0) {
    if (user.isVerified) {
      if (order.total <= user.creditLimit) {
        if (!order.hasRestrictedItems) {
          return true;
        }
      }
    }
  }
  return false;
}
```

**After:**
```typescript
function canProcessOrder(order: Order, user: User): boolean {
  return (
    order.items.length > 0 &&
    user.isVerified &&
    order.total <= user.creditLimit &&
    !order.hasRestrictedItems
  );
}
```

---

### Extract Class

**When:** Class has too many responsibilities

**Before:**
```typescript
class User {
  name: string;
  email: string;
  street: string;
  city: string;
  zipCode: string;

  getFullAddress(): string {
    return `${this.street}, ${this.city} ${this.zipCode}`;
  }
}
```

**After:**
```typescript
class Address {
  constructor(
    public street: string,
    public city: string,
    public zipCode: string
  ) {}

  getFullAddress(): string {
    return `${this.street}, ${this.city} ${this.zipCode}`;
  }
}

class User {
  constructor(
    public name: string,
    public email: string,
    public address: Address
  ) {}
}
```

---

### Replace Magic Numbers

**When:** Literal numbers without context

**Before:**
```typescript
function calculateFee(amount: number): number {
  if (amount < 100) {
    return amount * 0.05;
  }
  return amount * 0.03;
}
```

**After:**
```typescript
const MIN_AMOUNT_FOR_DISCOUNT = 100;
const STANDARD_FEE_RATE = 0.05;
const DISCOUNTED_FEE_RATE = 0.03;

function calculateFee(amount: number): number {
  const rate = amount < MIN_AMOUNT_FOR_DISCOUNT
    ? STANDARD_FEE_RATE
    : DISCOUNTED_FEE_RATE;
  return amount * rate;
}
```

---

## Refactoring Workflow

1. **Identify code smell**
   - Duplication
   - Long functions
   - Complex conditionals
   - Poor naming

2. **Ensure tests are green**
   - All tests passing before refactoring
   - If no tests, write them first

3. **Make small change**
   - One refactoring at a time
   - Keep changes focused

4. **Run tests**
   - Tests must stay green
   - If red, revert and try different approach

5. **Commit**
   - Commit after successful refactor
   - Clear commit message describing refactoring

6. **Repeat**
   - Continue until code is clean

---

## Code Smells to Watch For

### Duplication
Same or similar code in multiple places

### Long Functions
Functions > 20 lines usually do too much

### Long Parameter Lists
Functions with > 3 parameters are hard to use

### Large Classes
Classes with > 300 lines or > 10 methods

### Divergent Change
Class changes for multiple different reasons

### Shotgun Surgery
One change requires edits to many classes

### Feature Envy
Method uses more data from another class than its own

### Data Clumps
Same group of data items appearing together

### Primitive Obsession
Using primitives instead of small objects

### Switch Statements
Complex conditionals that should use polymorphism

---

## Remember

- **Tests first**: Green tests before refactoring
- **Small steps**: One change at a time
- **Tests stay green**: Revert if tests break
- **Commit often**: After each successful refactor
- **Improve gradually**: Don't try to perfect everything at once
