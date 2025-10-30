# Implementation Examples

## Purpose

Code implementation patterns for TDD green phase, showing how to write minimum code to make tests pass.

---

## Service Layer Pattern

### Basic Service Implementation

```typescript
// src/services/auth.service.ts
import { User } from '../models/user.model';
import bcrypt from 'bcrypt';

export class AuthService {
  /**
   * Find user by email address
   */
  async findUserByEmail(email: string): Promise<User | null> {
    return await User.findByEmail(email);
  }

  /**
   * Verify password against hash
   */
  async verifyPassword(password: string, passwordHash: string): Promise<boolean> {
    return await bcrypt.compare(password, passwordHash);
  }

  /**
   * Authenticate user with email and password
   * Returns user if credentials are valid, null otherwise
   */
  async authenticateUser(email: string, password: string): Promise<User | null> {
    const user = await this.findUserByEmail(email);
    if (!user) return null;

    const isPasswordValid = await this.verifyPassword(password, user.password_hash);
    if (!isPasswordValid) return null;

    return user;
  }
}
```

---

## Controller Layer Pattern

### Basic Controller with Validation

```typescript
// src/controllers/auth.controller.ts
import { Request, Response } from 'express';
import { AuthService } from '../services/auth.service';
import { generateToken } from '../utils/jwt';
import { loginSchema } from '../schemas/auth.schema';

const authService = new AuthService();

export const login = async (req: Request, res: Response): Promise<Response> => {
  try {
    // Validate input
    const validationResult = loginSchema.safeParse(req.body);
    if (!validationResult.success) {
      return res.status(400).json({
        error: validationResult.error.errors[0].message,
        code: 'VALIDATION_ERROR'
      });
    }

    const { email, password } = validationResult.data;

    // Authenticate user
    const user = await authService.authenticateUser(email, password);
    if (!user) {
      return res.status(401).json({
        error: 'Invalid credentials',
        code: 'AUTH_INVALID_CREDENTIALS'
      });
    }

    // Generate token
    const token = generateToken(user.id);

    return res.status(200).json({
      token,
      expiresIn: 86400 // 24 hours in seconds
    });

  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({
      error: 'Internal server error',
      code: 'INTERNAL_ERROR'
    });
  }
};
```

---

## Validation Schema Pattern

### Zod Schema

```typescript
// src/schemas/auth.schema.ts
import { z } from 'zod';

export const loginSchema = z.object({
  email: z.string().email('Invalid email format'),
  password: z.string().min(1, 'Password is required'),
});

export type LoginInput = z.infer<typeof loginSchema>;
```

---

## Middleware Pattern

### Rate Limiting Middleware

```typescript
// src/middleware/rate-limit.ts
import { Request, Response, NextFunction } from 'express';
import { RateLimiterMemory } from 'rate-limiter-flexible';

const rateLimiter = new RateLimiterMemory({
  points: 5,        // 5 attempts
  duration: 600,    // per 10 minutes
  blockDuration: 600, // block for 10 minutes
});

export const loginRateLimiter = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    await rateLimiter.consume(req.ip);
    next();
  } catch (error) {
    res.status(429).json({
      error: 'Too many login attempts. Please try again later.',
      code: 'RATE_LIMIT_EXCEEDED'
    });
  }
};
```

---

## Utility Pattern

### JWT Utilities

```typescript
// src/utils/jwt.ts
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'dev_secret_change_in_production';
const JWT_EXPIRES_IN = '24h';

export interface TokenPayload {
  userId: string;
}

export const generateToken = (userId: string): string => {
  return jwt.sign(
    { userId } as TokenPayload,
    JWT_SECRET,
    { expiresIn: JWT_EXPIRES_IN }
  );
};

export const verifyToken = (token: string): TokenPayload => {
  return jwt.verify(token, JWT_SECRET) as TokenPayload;
};
```

---

## Route Configuration Pattern

### Express Router Setup

```typescript
// src/routes/auth.routes.ts
import { Router } from 'express';
import { login } from '../controllers/auth.controller';
import { loginRateLimiter } from '../middleware/rate-limit';

const router = Router();

router.post('/login', loginRateLimiter, login);

export default router;
```

### App Integration

```typescript
// src/app.ts (add to existing app)
import authRoutes from './routes/auth.routes';

// ... existing code

app.use('/api/auth', authRoutes);
```

---

## Error Handling Pattern

### Custom Error Classes

```typescript
// src/errors/auth.errors.ts
export class AuthenticationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'AuthenticationError';
  }
}

export class ValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ValidationError';
  }
}
```

### Error Handler Middleware

```typescript
// src/middleware/error-handler.ts
import { Request, Response, NextFunction } from 'express';
import { AuthenticationError, ValidationError } from '../errors/auth.errors';

export const errorHandler = (
  error: Error,
  req: Request,
  res: Response,
  next: NextFunction
): Response => {
  if (error instanceof AuthenticationError) {
    return res.status(401).json({
      error: error.message,
      code: 'AUTH_ERROR'
    });
  }

  if (error instanceof ValidationError) {
    return res.status(400).json({
      error: error.message,
      code: 'VALIDATION_ERROR'
    });
  }

  // Default error
  console.error('Unhandled error:', error);
  return res.status(500).json({
    error: 'Internal server error',
    code: 'INTERNAL_ERROR'
  });
};
```

---

## Implementation Strategy

### Start Simple, Then Enhance

**Phase 1: Minimum Implementation**
```typescript
// Just enough to make test pass
export const login = async (req: Request, res: Response) => {
  const user = await User.findByEmail(req.body.email);
  if (!user) return res.status(401).json({ error: 'Invalid credentials' });

  const valid = await bcrypt.compare(req.body.password, user.password_hash);
  if (!valid) return res.status(401).json({ error: 'Invalid credentials' });

  const token = jwt.sign({ userId: user.id }, SECRET, { expiresIn: '24h' });
  return res.status(200).json({ token, expiresIn: 86400 });
};
```

**Phase 2: Add Error Handling**
```typescript
export const login = async (req: Request, res: Response) => {
  try {
    // Same logic as Phase 1
  } catch (error) {
    return res.status(500).json({ error: 'Internal server error' });
  }
};
```

**Phase 3: Add Validation**
```typescript
export const login = async (req: Request, res: Response) => {
  try {
    const validationResult = loginSchema.safeParse(req.body);
    if (!validationResult.success) {
      return res.status(400).json({ error: validationResult.error });
    }
    // Rest of logic
  } catch (error) {
    // Error handling
  }
};
```

**Phase 4: Extract to Service (Refactor)**
```typescript
// Controller becomes thin
export const login = async (req: Request, res: Response) => {
  try {
    const validationResult = loginSchema.safeParse(req.body);
    if (!validationResult.success) {
      return res.status(400).json({ error: validationResult.error });
    }

    const { email, password } = validationResult.data;
    const user = await authService.authenticateUser(email, password);

    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = generateToken(user.id);
    return res.status(200).json({ token, expiresIn: 86400 });
  } catch (error) {
    // Error handling
  }
};
```

---

## Quick Reference

**Layer Responsibilities:**
- **Controller**: Handle HTTP (request/response, status codes)
- **Service**: Business logic (authentication, authorization)
- **Repository**: Data access (database queries)
- **Middleware**: Request processing (validation, rate limiting)
- **Utility**: Helpers (JWT, hashing, formatting)

**TDD Green Phase Rules:**
1. Write minimum code to make test pass
2. Don't optimize yet (refactor later)
3. Keep logic in services, not controllers
4. Handle errors explicitly
5. Run tests after each small change

---

*Part of implement-feature skill - Development Suite*
