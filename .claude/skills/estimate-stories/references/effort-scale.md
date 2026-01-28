# Effort Scale (1-5)

Effort measures the volume of work (time) required to implement, test, and document the story. This focuses on hours/days needed, regardless of difficulty.

**Key Distinction:** Effort = HOW MUCH work, Complexity = HOW HARD the work is.

---

## 1 - Minimal (<1 hour)

**Description:** Can be completed in under 1 hour

**Characteristics:**
- Very few lines of code (<50 lines)
- No tests needed OR trivial test update
- No documentation needed
- No review complexity
- Immediate deployment

**Examples:**
- Change button color or text
- Update static content
- Add simple log statement
- Fix typo in error message
- Update configuration value
- Add CSS class

**Code Volume:** <50 LOC
**Tests:** 0-1 trivial tests
**Time:** <1 hour

---

## 2 - Low (1-2 hours)

**Description:** Half day or less

**Characteristics:**
- 50-150 lines of code
- 2-4 simple unit tests
- Minimal documentation
- Quick review (15-30 min)
- Single component or layer

**Examples:**
- Add new API parameter with validation
- Simple form field addition
- Basic error message improvement
- Simple component styling
- Add new database column with migration
- Simple utility function

**Code Volume:** 50-150 LOC
**Tests:** 2-4 unit tests
**Time:** 1-2 hours

---

## 3 - Medium (2-4 hours)

**Description:** Half to full day

**Characteristics:**
- 150-300 lines of code
- 5-8 tests (unit + maybe integration)
- Some documentation needed (API docs, comments)
- Standard review (30-60 min)
- Multiple components/layers

**Examples:**
- New CRUD endpoint (controller + service + model)
- Form with multiple fields and validation
- API integration (well-documented third-party)
- State management for single feature
- Database migration with data transformation
- Standard authentication implementation

**Code Volume:** 150-300 LOC
**Tests:** 5-8 tests (unit + integration)
**Documentation:** API docs, code comments
**Time:** 2-4 hours (half to full day)

---

## 4 - High (4-8 hours)

**Description:** 1-2 full days

**Characteristics:**
- 300-600 lines of code
- 9-15 tests (unit + integration + E2E)
- Significant documentation (API, architecture decisions)
- Careful review needed (1-2 hours)
- Multiple components across layers

**Examples:**
- Complex feature with multiple components (frontend + backend + DB)
- Multi-step workflow (wizard, checkout flow)
- Advanced error handling with retry logic
- Performance optimization work (caching, query optimization)
- Complex data transformation pipeline
- Comprehensive API endpoint with multiple operations

**Code Volume:** 300-600 LOC
**Tests:** 9-15 tests (comprehensive coverage)
**Documentation:** API docs, ADR, architecture diagrams
**Time:** 4-8 hours (1-2 days)

---

## 5 - Very High (>8 hours)

**Description:** More than 2 days—consider splitting

**Characteristics:**
- 600+ lines of code
- 15+ comprehensive tests
- Extensive documentation (user guide, API docs, architecture)
- Multiple review rounds
- Cross-cutting changes affecting many components

**Examples:**
- Large feature spanning multiple modules
- Complex refactoring across codebase
- New architectural component (new service layer, caching layer)
- Security implementation with audit trail
- Complex reporting feature with multiple views
- Multi-tenant implementation across system

**Code Volume:** 600+ LOC
**Tests:** 15+ tests (unit + integration + E2E + performance)
**Documentation:** Comprehensive (user, API, architecture)
**Time:** >8 hours (>2 days)

**Warning:** If effort is 5, strongly consider splitting the story into smaller pieces.

---

## Effort Analysis Framework

### 1. Code Volume Estimation

**Count acceptance criteria and estimate LOC per criterion:**

```
Story: User Signup

AC-1: User can enter email/password → 40 LOC (form component)
AC-2: Email validation → 20 LOC (validation schema)
AC-3: Password hashing → 30 LOC (service function)
AC-4: Duplicate email check → 25 LOC (DB query + error handling)
AC-5: JWT token generation → 30 LOC (service function)
AC-6: Save to database → 35 LOC (model + migration)

Total: ~180 LOC → Effort: 2-3
```

**Rule of thumb:** Each AC typically requires 20-50 LOC

### 2. Testing Requirements

**Estimate number and type of tests:**

```
Per AC, typical test count:
- Unit tests: 1-2 tests per function
- Integration tests: 1 test per happy path + 1-2 per error path
- E2E tests: 1 test per complete flow

Story with 6 AC:
- 6 unit tests (1 per AC)
- 3 integration tests (signup success, duplicate email, invalid input)
- 1 E2E test (complete signup flow)

Total: 10 tests → Effort: 3
```

**Rule of thumb:**
- 1-3 tests → Effort: 1
- 4-6 tests → Effort: 2
- 7-10 tests → Effort: 3
- 11-15 tests → Effort: 4
- 16+ tests → Effort: 5

### 3. Documentation Needs

**Assess documentation requirements:**

```
None → -1 to effort
Code comments only → +0 to effort
API documentation → +0.5 to effort
Architecture decisions → +0.5 to effort
User documentation → +1 to effort
```

### 4. Research/Learning Time

**Estimate time needed to learn new concepts:**

```
Familiar patterns → +0 to effort
New library (well-documented) → +0.5 to effort
New library (poor docs) → +1 to effort
New pattern/architecture → +1 to effort
Novel solution (R&D) → +2 to effort
```

### 5. Review/Iteration Time

**Consider review complexity:**

```
Simple change, quick review → +0 to effort
Standard review → +0.5 to effort
Complex change, careful review → +1 to effort
Security/performance review → +1.5 to effort
Multiple review rounds expected → +2 to effort
```

---

## Decision Tree: Determining Effort

```
How many acceptance criteria?
  ├─ 1 AC → Effort: 1-2
  ├─ 2-3 AC → Effort: 2-3
  ├─ 4-6 AC → Effort: 3-4
  └─ 7+ AC → Effort: 4-5 (consider splitting)

Estimate lines of code:
  ├─ <50 LOC → Effort: 1
  ├─ 50-150 LOC → Effort: 2
  ├─ 150-300 LOC → Effort: 3
  ├─ 300-600 LOC → Effort: 4
  └─ >600 LOC → Effort: 5

How many tests needed?
  ├─ 0-3 tests → +0 to effort
  ├─ 4-6 tests → +0.5 to effort
  ├─ 7-10 tests → +1 to effort
  ├─ 11-15 tests → +1.5 to effort
  └─ 16+ tests → +2 to effort

Documentation needed?
  ├─ None → +0 to effort
  ├─ Code comments → +0 to effort
  ├─ API docs → +0.5 to effort
  └─ Comprehensive docs → +1 to effort

Any learning required?
  ├─ No (familiar) → +0 to effort
  ├─ Minor (new library) → +0.5 to effort
  └─ Significant (new pattern) → +1 to effort

Final effort score: Sum all factors, cap at 5
```

---

## Example Effort Analysis

### Example 1: Simple Form Field

**Story:** Add "phone number" field to user profile

**Analysis:**
- **Code Volume:** ~30 LOC (form field + validation + model update)
- **Tests:** 2 unit tests (validation, save)
- **Documentation:** Code comments only
- **Learning:** None (standard pattern)
- **Review:** Quick (15 min)

**Effort:** 1 (Minimal - <1 hour)

---

### Example 2: CRUD Endpoint

**Story:** Create task management CRUD endpoints

**AC:** Create, Read, Update, Delete, List with pagination

**Analysis:**
- **Code Volume:** ~200 LOC
  - Controller: 60 LOC (5 endpoints)
  - Service: 70 LOC (business logic)
  - Model: 30 LOC (Prisma schema)
  - Validation: 40 LOC (Zod schemas)
- **Tests:** 8 tests
  - 5 integration tests (one per operation)
  - 3 unit tests (service layer)
- **Documentation:** API documentation (Swagger annotations)
- **Learning:** None (standard CRUD pattern)
- **Review:** Standard (45 min)

**Effort:** 3 (Medium - 3-4 hours)

---

### Example 3: Complex Multi-Step Wizard

**Story:** Multi-step onboarding wizard (5 steps)

**AC:** 10 acceptance criteria (2 per step)

**Analysis:**
- **Code Volume:** ~450 LOC
  - Frontend: 250 LOC (5 step components + wizard logic)
  - Backend: 150 LOC (save progress, validation per step)
  - State management: 50 LOC (wizard state machine)
- **Tests:** 13 tests
  - 10 integration tests (one per AC)
  - 3 E2E tests (complete flow, backward navigation, save progress)
- **Documentation:** User guide + API docs
- **Learning:** New state machine pattern
- **Review:** Careful review (1.5 hours)

**Effort:** 4 (High - 6-7 hours)

---

## Common Mistakes

### Mistake 1: Forgetting Test Time

**Wrong:**
```
Story: API endpoint
Estimate: Just code time (1 hour)
Effort: 1
```

**Right:**
```
Story: API endpoint
Estimate: Code (1 hour) + Tests (1 hour) + Review (0.5 hour) = 2.5 hours
Effort: 2
```

### Mistake 2: Underestimating Documentation

**Wrong:**
```
Story: New public API endpoint
Effort: 2 (just code + tests)
```

**Right:**
```
Story: New public API endpoint
Effort: 3 (code + tests + API docs + examples + Swagger annotations)
```

### Mistake 3: Ignoring Learning Time

**Wrong:**
```
Story: Implement WebSockets (team never used)
Effort: 2 (code looks simple)
```

**Right:**
```
Story: Implement WebSockets (team never used)
Effort: 4 (includes 2 hours learning + experimentation + code + tests)
```

### Mistake 4: Optimistic LOC Estimation

**Wrong:**
```
Story: Simple form
Estimate: 50 LOC
Reality: 150 LOC (validation, error handling, styling, tests)
```

**Right:**
```
Story: Simple form
Estimate: 100-150 LOC (include all related code)
Account for error handling, edge cases, tests
```

---

## Effort Calibration

Track actual vs. estimated effort:

```markdown
Story: User Signup
Estimated Effort: 3 (2-4 hours)
Actual Time: 5.5 hours

Why longer?
- Underestimated test time (4 tests became 8 tests)
- Didn't account for bcrypt configuration time
- JWT library had poor documentation

Learning: Add +0.5 effort for authentication stories (security-sensitive)
```

---

## Effort vs. Complexity Examples

### High Effort, Low Complexity

```
Story: Add 20 similar form fields
Complexity: 1 (trivial pattern)
Effort: 4 (high volume, takes time)
Story Points: (1 × 4) + 0 = 4 points
```

### Low Effort, High Complexity

```
Story: Implement complex algorithm (with reference implementation)
Complexity: 4 (sophisticated logic)
Effort: 2 (code is short, ~100 LOC)
Story Points: (4 × 2) + 1 = 9 points (risk for testing edge cases)
```

### High Effort, High Complexity

```
Story: Real-time collaborative editing
Complexity: 5 (operational transformation, conflict resolution)
Effort: 5 (600+ LOC, extensive testing)
Story Points: (5 × 5) + 3 = 28 points → MUST SPLIT
```

---

## Using This Scale

1. **Count acceptance criteria** - More AC = more work
2. **Estimate LOC** - How much code to write?
3. **Count tests** - How many tests needed?
4. **Assess documentation** - What docs required?
5. **Consider learning** - Any new tech to learn?
6. **Factor in review** - How complex is review?
7. **Sum the time** - Total hours needed
8. **Map to effort scale** - Convert hours to 1-5 scale

**Remember:** Effort is about VOLUME of work, not difficulty. A complex story can have low effort if the code is small.
