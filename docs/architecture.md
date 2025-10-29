# System Architecture

## Overview

This is a sample Node.js web application with user authentication features.

## Tech Stack

- **Runtime:** Node.js 20.x
- **Framework:** Express.js 4.x
- **Database:** PostgreSQL 15.x with Prisma ORM
- **Validation:** Zod 3.x
- **Testing:** Jest + Supertest
- **Password Hashing:** bcrypt 5.x

## Project Structure

```
src/
├── routes/          # Express route handlers
│   └── auth/        # Authentication routes
├── services/        # Business logic layer
│   └── auth/        # Authentication services
├── repositories/    # Database access layer
├── schemas/         # Zod validation schemas
├── types/           # TypeScript type definitions
└── utils/           # Shared utilities

tests/
├── unit/            # Unit tests
├── integration/     # Integration tests
└── e2e/             # End-to-end tests
```

## Data Models

### User Model

```typescript
interface User {
  id: string;          // UUID, primary key
  email: string;       // Unique, validated email
  password: string;    // bcrypt hashed, never exposed in responses
  emailVerified: boolean;  // Email verification status
  createdAt: Date;     // Auto-generated timestamp
  updatedAt: Date;     // Auto-updated timestamp
}
```

**Validation Rules:**
- Email: Must be valid RFC 5322 format, max 255 characters
- Password: Minimum 8 characters, must contain:
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 number
  - At least 1 special character (!@#$%^&*)

**Database Schema (Prisma):**
```prisma
model User {
  id            String   @id @default(uuid())
  email         String   @unique
  password      String
  emailVerified Boolean  @default(false)
  createdAt     DateTime @default(now())
  updatedAt     DateTime @updatedAt
}
```

## API Specifications

### Authentication Endpoints

#### POST /api/auth/signup

Creates a new user account.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (201 Created):**
```json
{
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "emailVerified": false
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Error Responses:**

400 Bad Request - Validation errors:
```json
{
  "error": "Validation failed",
  "details": [
    "Email format is invalid",
    "Password must be at least 8 characters"
  ]
}
```

409 Conflict - Email already exists:
```json
{
  "error": "Email already registered",
  "message": "An account with this email already exists"
}
```

500 Internal Server Error:
```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

**Authentication:** None (public endpoint)

**Rate Limiting:** 5 requests per minute per IP address

## Security Considerations

- Passwords must be hashed using bcrypt with cost factor 12
- Never log or expose passwords in error messages
- Use parameterized queries to prevent SQL injection
- Implement rate limiting on authentication endpoints
- Validate all inputs using Zod schemas before processing
