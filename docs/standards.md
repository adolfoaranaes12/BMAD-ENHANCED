# Development Standards

## Security Standards

### Password Security
- **Hashing Algorithm:** bcrypt with cost factor 12
- **Password Requirements:**
  - Minimum 8 characters
  - Must contain uppercase, lowercase, number, and special character
  - Never store passwords in plain text
  - Never log passwords or include in error messages

### Input Validation
- All user inputs must be validated using Zod schemas
- Email validation must use Zod's email validator (RFC 5322 compliant)
- Reject invalid inputs with 400 status and clear error messages

### API Security
- Rate limiting: 5 requests per minute per IP for auth endpoints
- Use parameterized queries (Prisma) to prevent SQL injection
- Sanitize all user inputs before database operations

## Testing Standards

### Test Coverage
- **Minimum Coverage:** 80% for new code
- **Coverage Metrics:**
  - Statements: ≥80%
  - Branches: ≥75%
  - Functions: ≥90%

### Test Levels

**Unit Tests:**
- Test individual functions and methods in isolation
- Mock external dependencies (database, APIs, email services)
- Fast execution (<100ms per test)
- Framework: Jest

**Integration Tests:**
- Test API endpoints with real database (test database)
- Test service layer interactions with repositories
- Use Supertest for HTTP testing
- Framework: Jest + Supertest

**E2E Tests:**
- Test complete user journeys
- Use real services where possible
- Framework: Jest + Supertest (or Playwright for UI tests)

### Test Organization
```
src/services/auth/__tests__/
  └── signup.service.test.ts          # Unit tests

src/routes/auth/__tests__/
  └── signup.integration.test.ts      # Integration tests

tests/e2e/auth/
  └── signup.e2e.test.ts              # E2E tests
```

### Required Test Cases for User Signup

1. **Happy Path:** Valid email and password creates user and returns token
2. **Email Validation:** Invalid email format rejected with 400
3. **Password Validation:** Weak password rejected with validation errors
4. **Duplicate Prevention:** Duplicate email returns 409 error
5. **Error Handling:** Database errors handled gracefully with 500
6. **Security:** Password is hashed in database
7. **Security:** Password not included in response

## Performance Standards

### API Response Times
- **p50:** <100ms
- **p95:** <200ms
- **p99:** <500ms

### Database Queries
- Maximum 3 queries per endpoint (prevent N+1 problem)
- Use connection pooling (max 20 connections)
- Index all frequently queried fields

## Code Quality Standards

### TypeScript
- Strict mode enabled
- No `any` types (use `unknown` when type is truly unknown)
- Define interfaces for all data structures
- Use type guards for runtime type checking

### Error Handling
- Always catch and handle errors
- Use custom error classes for different error types
- Provide meaningful error messages to users
- Log detailed error information for debugging

### Code Style
- ESLint configuration enforced
- Prettier for formatting
- Meaningful variable and function names
- Comments for complex logic only (code should be self-documenting)
