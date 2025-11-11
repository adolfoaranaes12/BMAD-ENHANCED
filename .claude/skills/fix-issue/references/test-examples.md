# Test Examples for Bug Fixes

Comprehensive examples of writing tests that reproduce bugs and validate fixes.

---

## Pattern: Validation Bug

**Bug:** Validation rejects valid input

**Test Structure:**
1. Test the specific case that fails
2. Test related valid cases (edge cases)
3. Ensure invalid cases still rejected

**Example: Email Validation**

```typescript
describe('[Bug Fix] Email validation', () => {
  // Test the reported bug
  it('should accept email with + symbol', async () => {
    const result = validateEmail('user+tag@example.com');
    expect(result.valid).toBe(true);
  });

  // Test related edge cases
  it('should accept email with multiple + symbols', async () => {
    const result = validateEmail('user+tag+more@example.com');
    expect(result.valid).toBe(true);
  });

  it('should accept email with % symbol', async () => {
    const result = validateEmail('user%test@example.com');
    expect(result.valid).toBe(true);
  });

  it('should accept email with dots', async () => {
    const result = validateEmail('first.last@example.com');
    expect(result.valid).toBe(true);
  });

  // Ensure we didn't break existing validation
  it('should still reject email without @', async () => {
    const result = validateEmail('notanemail.com');
    expect(result.valid).toBe(false);
  });

  it('should still reject email without domain', async () => {
    const result = validateEmail('user@');
    expect(result.valid).toBe(false);
  });
});
```

---

## Pattern: Race Condition Bug

**Bug:** Intermittent failures under concurrent operations

**Test Structure:**
1. Set up race condition scenario
2. Run operations concurrently
3. Verify correct handling (locks, transactions)

**Example: Inventory Management**

```typescript
describe('[Bug Fix] Concurrent inventory updates', () => {
  beforeEach(async () => {
    await Product.create({ id: 'prod-1', stock: 100 });
  });

  it('should handle concurrent stock decreases correctly', async () => {
    // Simulate 5 concurrent purchases of 30 units each
    const purchases = Array(5).fill(null).map(() =>
      decreaseStock('prod-1', 30)
    );

    const results = await Promise.all(purchases);

    // Should succeed: 100 / 30 = 3 purchases (90 units)
    // Should fail: 2 purchases (not enough stock)
    const succeeded = results.filter(r => r.success).length;
    const failed = results.filter(r => !r.success).length;

    expect(succeeded).toBe(3);
    expect(failed).toBe(2);

    // Verify final stock is correct
    const product = await Product.findById('prod-1');
    expect(product.stock).toBe(10); // 100 - (3 * 30)
  });

  it('should not allow negative stock', async () => {
    // Try to purchase more than available
    const result = await decreaseStock('prod-1', 150);

    expect(result.success).toBe(false);
    expect(result.error).toBe('Insufficient stock');

    // Stock should be unchanged
    const product = await Product.findById('prod-1');
    expect(product.stock).toBe(100);
  });
});
```

---

## Pattern: Missing Error Handling

**Bug:** Unhandled errors causing 500 responses

**Test Structure:**
1. Test error conditions that should be handled
2. Verify appropriate error responses
3. Verify system state remains consistent

**Example: User Not Found**

```typescript
describe('[Bug Fix] Error handling for missing user', () => {
  it('should return 404 when user not found', async () => {
    const response = await request(app)
      .get('/api/users/nonexistent-id')
      .expect(404);

    expect(response.body).toEqual({
      error: 'User not found',
      code: 'USER_NOT_FOUND'
    });
  });

  it('should return 404 when updating nonexistent user', async () => {
    const response = await request(app)
      .put('/api/users/nonexistent-id')
      .send({ name: 'New Name' })
      .expect(404);

    expect(response.body).toEqual({
      error: 'User not found',
      code: 'USER_NOT_FOUND'
    });
  });

  it('should return 500 with safe message on database error', async () => {
    // Mock database error
    jest.spyOn(User, 'findById').mockRejectedValue(
      new Error('Database connection failed')
    );

    const response = await request(app)
      .get('/api/users/123')
      .expect(500);

    // Should not leak internal error details
    expect(response.body).toEqual({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });

    // But should log the actual error
    expect(console.error).toHaveBeenCalledWith(
      expect.stringContaining('Database connection failed')
    );
  });
});
```

---

## Pattern: Wrong Assumptions

**Bug:** Code assumes data always in certain format

**Test Structure:**
1. Test with missing/null/undefined data
2. Test with unexpected formats
3. Test with edge cases

**Example: Nullable Profile**

```typescript
describe('[Bug Fix] Handle users without profile', () => {
  it('should handle user with null profile', async () => {
    const user = await User.create({
      email: 'user@example.com',
      profile: null  // Profile optional
    });

    const response = await request(app)
      .get(`/api/users/${user.id}`)
      .expect(200);

    expect(response.body).toEqual({
      id: user.id,
      email: 'user@example.com',
      name: 'Anonymous',  // Default value
      avatar: '/default-avatar.png'  // Default value
    });
  });

  it('should handle user with partial profile', async () => {
    const user = await User.create({
      email: 'user@example.com',
      profile: { name: 'John' }  // No avatar
    });

    const response = await request(app)
      .get(`/api/users/${user.id}`)
      .expect(200);

    expect(response.body).toEqual({
      id: user.id,
      email: 'user@example.com',
      name: 'John',
      avatar: '/default-avatar.png'  // Default for missing avatar
    });
  });

  it('should handle user with complete profile', async () => {
    const user = await User.create({
      email: 'user@example.com',
      profile: {
        name: 'John Doe',
        avatar: 'https://example.com/avatar.jpg'
      }
    });

    const response = await request(app)
      .get(`/api/users/${user.id}`)
      .expect(200);

    expect(response.body).toEqual({
      id: user.id,
      email: 'user@example.com',
      name: 'John Doe',
      avatar: 'https://example.com/avatar.jpg'
    });
  });
});
```

---

## Pattern: Timing/Async Issues

**Bug:** Operations complete in wrong order

**Test Structure:**
1. Test that async operations await correctly
2. Test operation ordering
3. Test with delays to catch timing bugs

**Example: Order Processing**

```typescript
describe('[Bug Fix] Order processing sequence', () => {
  it('should complete payment before sending confirmation', async () => {
    const events: string[] = [];

    // Track order of operations
    jest.spyOn(Payment, 'process').mockImplementation(async () => {
      events.push('payment-processed');
      return { id: 'pay-1', status: 'succeeded' };
    });

    jest.spyOn(Email, 'send').mockImplementation(async () => {
      events.push('email-sent');
      return { id: 'email-1', status: 'sent' };
    });

    await processOrder('order-1');

    // Verify operations happened in correct order
    expect(events).toEqual([
      'payment-processed',
      'email-sent'
    ]);
  });

  it('should not send email if payment fails', async () => {
    jest.spyOn(Payment, 'process').mockRejectedValue(
      new Error('Payment failed')
    );

    const sendEmailSpy = jest.spyOn(Email, 'send');

    await expect(processOrder('order-1')).rejects.toThrow('Payment failed');

    // Email should not be sent
    expect(sendEmailSpy).not.toHaveBeenCalled();
  });

  it('should rollback order if email fails', async () => {
    jest.spyOn(Payment, 'process').mockResolvedValue({
      id: 'pay-1',
      status: 'succeeded'
    });

    jest.spyOn(Email, 'send').mockRejectedValue(
      new Error('Email service unavailable')
    );

    await expect(processOrder('order-1')).rejects.toThrow(
      'Email service unavailable'
    );

    // Payment should be refunded
    const payment = await Payment.findById('pay-1');
    expect(payment.status).toBe('refunded');

    // Order should be cancelled
    const order = await Order.findById('order-1');
    expect(order.status).toBe('cancelled');
  });
});
```

---

## Pattern: Boundary Conditions

**Bug:** Code fails at limits/boundaries

**Test Structure:**
1. Test minimum valid value
2. Test maximum valid value
3. Test just below/above limits
4. Test zero, negative, null

**Example: Pagination**

```typescript
describe('[Bug Fix] Pagination boundary conditions', () => {
  beforeEach(async () => {
    // Create 25 items
    for (let i = 1; i <= 25; i++) {
      await Item.create({ name: `Item ${i}` });
    }
  });

  it('should handle page 1 correctly', async () => {
    const result = await getItems({ page: 1, perPage: 10 });

    expect(result.items).toHaveLength(10);
    expect(result.page).toBe(1);
    expect(result.totalPages).toBe(3);
    expect(result.hasMore).toBe(true);
  });

  it('should handle last page correctly', async () => {
    const result = await getItems({ page: 3, perPage: 10 });

    expect(result.items).toHaveLength(5); // Only 5 items on last page
    expect(result.page).toBe(3);
    expect(result.totalPages).toBe(3);
    expect(result.hasMore).toBe(false);
  });

  it('should handle page beyond last page', async () => {
    const result = await getItems({ page: 10, perPage: 10 });

    expect(result.items).toHaveLength(0);
    expect(result.page).toBe(10);
    expect(result.totalPages).toBe(3);
    expect(result.hasMore).toBe(false);
  });

  it('should handle page 0 (invalid)', async () => {
    await expect(getItems({ page: 0, perPage: 10 }))
      .rejects.toThrow('Page must be >= 1');
  });

  it('should handle negative page', async () => {
    await expect(getItems({ page: -1, perPage: 10 }))
      .rejects.toThrow('Page must be >= 1');
  });

  it('should handle perPage = 0', async () => {
    await expect(getItems({ page: 1, perPage: 0 }))
      .rejects.toThrow('perPage must be between 1 and 100');
  });

  it('should handle perPage > max (100)', async () => {
    await expect(getItems({ page: 1, perPage: 200 }))
      .rejects.toThrow('perPage must be between 1 and 100');
  });

  it('should handle empty dataset', async () => {
    await Item.deleteAll();

    const result = await getItems({ page: 1, perPage: 10 });

    expect(result.items).toHaveLength(0);
    expect(result.page).toBe(1);
    expect(result.totalPages).toBe(0);
    expect(result.hasMore).toBe(false);
  });
});
```

---

## Pattern: State Machine Bugs

**Bug:** Invalid state transitions allowed

**Test Structure:**
1. Test valid transitions
2. Test invalid transitions (should fail)
3. Test edge cases (concurrent transitions)

**Example: Order Status**

```typescript
describe('[Bug Fix] Order status transitions', () => {
  let order: Order;

  beforeEach(async () => {
    order = await Order.create({ status: 'pending' });
  });

  // Valid transitions
  it('should allow pending → confirmed', async () => {
    await order.transitionTo('confirmed');
    expect(order.status).toBe('confirmed');
  });

  it('should allow confirmed → shipped', async () => {
    await order.transitionTo('confirmed');
    await order.transitionTo('shipped');
    expect(order.status).toBe('shipped');
  });

  it('should allow shipped → delivered', async () => {
    await order.transitionTo('confirmed');
    await order.transitionTo('shipped');
    await order.transitionTo('delivered');
    expect(order.status).toBe('delivered');
  });

  // Invalid transitions (should be prevented)
  it('should not allow pending → shipped', async () => {
    await expect(order.transitionTo('shipped'))
      .rejects.toThrow('Cannot transition from pending to shipped');

    expect(order.status).toBe('pending'); // Status unchanged
  });

  it('should not allow pending → delivered', async () => {
    await expect(order.transitionTo('delivered'))
      .rejects.toThrow('Cannot transition from pending to delivered');
  });

  it('should not allow delivered → shipped', async () => {
    await order.transitionTo('confirmed');
    await order.transitionTo('shipped');
    await order.transitionTo('delivered');

    await expect(order.transitionTo('shipped'))
      .rejects.toThrow('Cannot transition from delivered to shipped');
  });

  // Cancellation allowed from most states
  it('should allow cancellation from pending', async () => {
    await order.transitionTo('cancelled');
    expect(order.status).toBe('cancelled');
  });

  it('should allow cancellation from confirmed', async () => {
    await order.transitionTo('confirmed');
    await order.transitionTo('cancelled');
    expect(order.status).toBe('cancelled');
  });

  it('should not allow cancellation after shipped', async () => {
    await order.transitionTo('confirmed');
    await order.transitionTo('shipped');

    await expect(order.transitionTo('cancelled'))
      .rejects.toThrow('Cannot cancel order after shipping');
  });
});
```

---

## Integration Test Example

**Bug:** Feature works in unit tests but fails in integration

```typescript
describe('[Bug Fix] End-to-end checkout flow', () => {
  let user: User;
  let product: Product;
  let authToken: string;

  beforeEach(async () => {
    // Set up complete test environment
    user = await User.create({
      email: 'test@example.com',
      password: await bcrypt.hash('password', 10)
    });

    product = await Product.create({
      name: 'Test Product',
      price: 29.99,
      stock: 10
    });

    // Get auth token
    const loginResponse = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'password' });

    authToken = loginResponse.body.token;
  });

  it('should complete full checkout flow', async () => {
    // Step 1: Add to cart
    const cartResponse = await request(app)
      .post('/api/cart/items')
      .set('Authorization', `Bearer ${authToken}`)
      .send({ productId: product.id, quantity: 2 })
      .expect(200);

    expect(cartResponse.body.items).toHaveLength(1);
    expect(cartResponse.body.total).toBe(59.98);

    // Step 2: Create order
    const orderResponse = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        shippingAddress: {
          street: '123 Main St',
          city: 'San Francisco',
          state: 'CA',
          zip: '94102'
        }
      })
      .expect(200);

    const orderId = orderResponse.body.id;
    expect(orderResponse.body.status).toBe('pending');
    expect(orderResponse.body.total).toBe(59.98);

    // Step 3: Process payment
    const paymentResponse = await request(app)
      .post(`/api/orders/${orderId}/payment`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        method: 'card',
        token: 'tok_test_123'
      })
      .expect(200);

    expect(paymentResponse.body.status).toBe('succeeded');

    // Step 4: Verify order updated
    const finalOrderResponse = await request(app)
      .get(`/api/orders/${orderId}`)
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(finalOrderResponse.body.status).toBe('confirmed');
    expect(finalOrderResponse.body.paymentStatus).toBe('paid');

    // Step 5: Verify stock decreased
    const productAfter = await Product.findById(product.id);
    expect(productAfter.stock).toBe(8); // 10 - 2

    // Step 6: Verify cart cleared
    const cartAfter = await request(app)
      .get('/api/cart')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);

    expect(cartAfter.body.items).toHaveLength(0);
  });
});
```

---

## Tips for Writing Bug Reproduction Tests

1. **Test name should describe the bug**
   ```typescript
   ✅ it('should accept email with + symbol')
   ❌ it('test email validation')
   ```

2. **Keep tests focused on single issue**
   ```typescript
   ✅ One test per bug scenario
   ❌ One test checking multiple unrelated things
   ```

3. **Test should fail before fix, pass after fix**
   ```typescript
   // Run test before applying fix
   ❌ FAIL

   // Apply fix

   // Run test again
   ✅ PASS
   ```

4. **Add edge cases beyond reported bug**
   ```typescript
   // Bug report: "+" not working
   it('should accept +')  // Reported case
   it('should accept ++')  // Edge case
   it('should accept %')  // Related case
   it('should reject @')  // Ensure fix not too broad
   ```

5. **Use descriptive test data**
   ```typescript
   ✅ email: 'user+tag@example.com'  // Clear what's being tested
   ❌ email: 'test@test.com'  // Doesn't show the issue
   ```

6. **Document why test exists**
   ```typescript
   describe('[Bug Fix] Email validation rejects + symbol', () => {
     // Bug: Email validation incorrectly rejected valid RFC 5322 emails
     // Root cause: Zod email() validator too strict
     // Fix: Custom regex allowing + symbol
     it('should accept email with + symbol', () => { /* ... */ });
   });
   ```
