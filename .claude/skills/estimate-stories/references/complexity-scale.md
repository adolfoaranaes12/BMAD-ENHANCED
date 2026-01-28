# Complexity Scale (1-5)

Complexity measures the technical difficulty and cognitive load required to implement a story. This is NOT about time/effort, but about the intricacy and sophistication of the solution.

---

## 1 - Trivial

**Description:** Straightforward implementation with well-known patterns

**Characteristics:**
- Single file change
- No new dependencies required
- Copy-paste from existing code possible
- No edge cases to handle
- No integration points
- No design decisions needed

**Examples:**
- Add a new static field to an existing form
- Update button text or label
- Add a simple CSS class or style tweak
- Create a basic GET endpoint that returns hardcoded data
- Change configuration value
- Update static content or text

**When to Use:**
- Implementation is obvious
- No thinking required
- Pattern already exists in codebase

---

## 2 - Simple

**Description:** Simple implementation requiring basic problem-solving

**Characteristics:**
- 2-3 file changes
- Uses existing patterns/libraries
- Minimal edge cases (1-2)
- Well-documented approach available
- 1-2 integration points (e.g., database, API)
- Straightforward error handling

**Examples:**
- Basic CRUD endpoint with validation
- Simple form with validation (email, password)
- Add new field to existing model/table
- Basic authentication check (is user logged in?)
- Simple data transformation (map one object to another)
- Standard API call with error handling

**When to Use:**
- Solution is straightforward but requires some coding
- Patterns exist and can be adapted
- Few variables to consider

---

## 3 - Moderate

**Description:** Moderate complexity requiring careful design and consideration

**Characteristics:**
- 4-6 file changes across layers
- May require new library or pattern
- Multiple edge cases to handle (3-5)
- 2-3 integration points
- Some architectural decisions needed
- Multiple error paths to consider

**Examples:**
- OAuth integration (third-party authentication)
- File upload with validation and storage
- Complex form with conditional logic (show/hide fields based on input)
- API integration with error handling and retries
- Multi-step wizard or flow
- State management for feature with multiple states
- Caching implementation for specific data

**When to Use:**
- Requires design thinking
- Multiple approaches possible
- Need to handle various scenarios
- Some uncertainty in approach

---

## 4 - Complex

**Description:** High complexity requiring significant design work and careful implementation

**Characteristics:**
- 7-12 file changes across multiple layers
- Multiple new patterns or abstractions needed
- Many edge cases and error paths (5-10)
- 4-6 integration points
- Significant architectural impact
- Performance considerations required
- Security considerations important
- May need coordination across teams

**Examples:**
- Real-time notification system (WebSocket, push, polling)
- Complex state management (multi-entity, transitions, consistency)
- Multi-tenant architecture changes (isolation, data segregation)
- Advanced caching strategy (invalidation, distributed cache)
- Complex data transformation pipeline (multiple stages, error handling)
- Search functionality with filters and faceting
- Payment flow with multiple states and rollback scenarios
- Complex authorization (roles, permissions, resources)

**When to Use:**
- Significant system impact
- Multiple subsystems affected
- Architecture changes required
- High stakes (performance, security, reliability)

---

## 5 - Very Complex

**Description:** Very high complexity, likely needs spike/research phase first

**Characteristics:**
- 12+ file changes across entire application
- New architectural patterns required
- Extensive edge cases and failure modes (10+)
- 6+ integration points
- Cross-cutting concerns (affects many systems)
- Performance critical (requires profiling, optimization)
- Security critical (requires security review)
- May require R&D or proof-of-concept first

**Examples:**
- Payment processing integration (Stripe, PayPal - handles money, refunds, disputes)
- Real-time collaborative editing (OT/CRDT, conflict resolution)
- Complex search with faceting, scoring, and relevance (Elasticsearch)
- Distributed transaction handling (2PC, saga pattern)
- Custom security implementation (encryption, key management)
- Real-time video/audio streaming
- ML model integration with training pipeline
- Microservices decomposition of monolith
- Complex data migration across systems

**When to Use:**
- Unknown territory for team
- Cutting-edge technology
- Mission-critical with high risk
- May need external expertise

**Warning:** Stories scoring 5 in complexity often need to be split or preceded by a spike story for research.

---

## Complexity Analysis Framework

When analyzing complexity, systematically consider these factors:

### 1. Integration Points

**Count the number of systems/components that must interact:**

```
1 integration point   → +0 to complexity
2-3 integration points → +1 to complexity
4-6 integration points → +2 to complexity
7+ integration points  → +3 to complexity
```

**Examples of integration points:**
- Database (PostgreSQL, MongoDB, etc.)
- External API (Stripe, SendGrid, Auth0, etc.)
- Message queue (RabbitMQ, Kafka, etc.)
- Cache (Redis, Memcached)
- File storage (S3, local filesystem)
- Search engine (Elasticsearch)
- Real-time service (WebSocket server)
- Background job processor
- Email service
- SMS service

### 2. Error Handling Paths

**Count distinct error scenarios that must be handled:**

```
Happy path only          → -1 to complexity (very simple)
1-2 error scenarios      → +0 to complexity (simple)
3-5 error scenarios      → +1 to complexity (moderate)
6-10 error scenarios     → +2 to complexity (complex)
10+ error scenarios      → +3 to complexity (very complex)
```

**Examples of error scenarios:**
- Validation errors (invalid input)
- Not found errors (resource doesn't exist)
- Permission errors (not authorized)
- Conflict errors (duplicate, constraint violation)
- Timeout errors (external service slow)
- Rate limit errors (too many requests)
- Network errors (connection failed)
- Partial failure errors (some operations succeed, others fail)
- Transaction rollback scenarios
- Data inconsistency errors

### 3. State Management

**Assess state complexity:**

```
Stateless                       → -1 to complexity
Simple state (on/off, loaded)   → +0 to complexity
Multiple states with transitions → +1 to complexity
Complex state machine           → +2 to complexity
Distributed state               → +3 to complexity
```

**Examples:**
- Stateless: Simple query endpoint (no state)
- Simple: Loading indicator (loading, loaded, error)
- Multiple states: Order status (pending, confirmed, shipped, delivered, cancelled)
- Complex: Multi-step wizard with validation at each step, can go forward/backward
- Distributed: Shopping cart synced across devices in real-time

### 4. Data Transformation Complexity

**Assess transformation intricacy:**

```
None (pass-through)              → -1 to complexity
Simple mapping (1:1)             → +0 to complexity
Aggregation or filtering         → +1 to complexity
Complex transformation (joins)   → +2 to complexity
Multi-stage pipeline             → +3 to complexity
```

**Examples:**
- Pass-through: Proxy endpoint, no transformation
- Simple: Map API response to DTO
- Aggregation: Calculate totals, group by category
- Complex: Join data from multiple sources, resolve conflicts
- Pipeline: ETL process with multiple transformations, validations, enrichments

### 5. Algorithm Complexity

**Consider computational complexity:**

```
O(1) or O(n) with small n        → +0 to complexity
O(n) with large n or O(n log n)  → +1 to complexity
O(n²) or complex algorithm       → +2 to complexity
Requires novel algorithm         → +3 to complexity
```

### 6. Architectural Impact

**Assess system-wide effects:**

```
Single component                 → +0 to complexity
Multiple related components      → +1 to complexity
Cross-cutting concern            → +2 to complexity
System-wide architectural change → +3 to complexity
```

---

## Decision Tree: Determining Complexity

```
Is this exact code already in the codebase?
  ├─ YES → Copy-paste possible → Complexity: 1
  └─ NO → Continue

How many files will change?
  ├─ 1 file → Complexity: 1-2
  ├─ 2-3 files → Complexity: 2-3
  ├─ 4-6 files → Complexity: 3-4
  └─ 7+ files → Complexity: 4-5

How many integration points?
  ├─ 0-1 → +0 to complexity
  ├─ 2-3 → +1 to complexity
  ├─ 4-6 → +2 to complexity
  └─ 7+ → +3 to complexity

How many error scenarios?
  ├─ 0-2 → +0 to complexity
  ├─ 3-5 → +1 to complexity
  ├─ 6-10 → +2 to complexity
  └─ 10+ → +3 to complexity

Does this require new architecture/patterns?
  ├─ NO → Keep current complexity
  └─ YES → +1 to complexity

Final complexity score: Sum all factors, cap at 5
```

---

## Common Mistakes

### Mistake 1: Confusing Complexity with Effort

**Wrong:**
```
Story: Add 10 similar fields to a form
Complexity: 5 (because it's a lot of work)
```

**Right:**
```
Story: Add 10 similar fields to a form
Complexity: 1 (trivial, copy-paste pattern)
Effort: 3 (medium, because of volume)
```

**Key:** Complexity is about HOW HARD, not HOW MUCH.

### Mistake 2: Underestimating Integration Complexity

**Wrong:**
```
Story: Add Stripe payment integration
Complexity: 2 (it's just an API call)
```

**Right:**
```
Story: Add Stripe payment integration
Complexity: 4 (webhooks, error handling, refunds, disputes, security, testing)
```

**Key:** External integrations have hidden complexity in error handling, edge cases, and testing.

### Mistake 3: Ignoring State Management

**Wrong:**
```
Story: Multi-step checkout flow
Complexity: 2 (just some forms)
```

**Right:**
```
Story: Multi-step checkout flow
Complexity: 3-4 (state transitions, validation per step, back/forward navigation, persistence)
```

**Key:** State management adds complexity beyond simple CRUD.

### Mistake 4: Assuming Familiarity

**Wrong:**
```
Story: Real-time notifications with WebSockets
Complexity: 3 (I've done this before in another project)
Team: Has never done WebSockets
```

**Right:**
```
Story: Real-time notifications with WebSockets
Complexity: 4 (new to team, requires learning, pattern establishment)
Team: Has never done WebSockets
```

**Key:** Complexity is relative to the TEAM's experience, not individual experience.

---

## Complexity Calibration

After completing stories, calibrate complexity scores:

```markdown
Story: OAuth Integration
Estimated Complexity: 3
Actual Complexity: 4

Why was it harder?
- Underestimated error handling (token refresh, expiry)
- Didn't account for multiple OAuth providers
- State management more complex than expected

Learning: OAuth integrations should start at complexity 4, not 3
```

Track these learnings to improve future estimations.

---

## Using This Scale

1. **Read acceptance criteria** - Understand what needs to be implemented
2. **Count integration points** - How many systems involved?
3. **List error scenarios** - What can go wrong?
4. **Assess state complexity** - Simple or state machine?
5. **Consider architectural impact** - Local or system-wide?
6. **Check team familiarity** - New or known patterns?
7. **Assign complexity score** - Use framework above
8. **Document rationale** - Explain why this score

**Remember:** Complexity is about technical difficulty, not time. A complex story might take less time than a simple but voluminous story.
