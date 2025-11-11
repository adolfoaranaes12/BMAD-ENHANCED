# Risk Factors (0-3 Adjustment)

Risk represents uncertainty, unknowns, or factors that could cause the story to take longer than expected or require rework. This is an ADJUSTMENT (+0 to +3 points) to the base score (Complexity × Effort), not a multiplier.

**Formula:** `Story Points = (Complexity × Effort) + Risk`

---

## Risk Scale

### 0 - No Significant Risk

**Description:** Completely understood, minimal unknowns

**Characteristics:**
- Exact duplicate of existing work
- All dependencies in place and tested
- Well-tested approach
- No external dependencies
- Crystal-clear acceptance criteria
- Team highly familiar with tech
- No performance/security concerns

**Examples:**
- Adding a field to a form (done 100 times before)
- Updating static content
- Copy-paste with minor modifications

**When to Use:** Rare—only when absolutely certain there are no unknowns.

---

### +1 - Minor Risk

**Description:** Some uncertainty or minor unknowns

**Characteristics:**
- Slightly unfamiliar library (but well-documented)
- Minor unknowns in approach
- Some ambiguity in requirements
- Standard external dependencies
- Team has some experience
- Minor performance/security considerations

**Examples:**
- Using a new but well-documented library
- Integration with familiar third-party API
- Requirements have minor ambiguity
- New pattern but similar to existing patterns
- Minor security considerations (standard hashing, validation)

**When to Use:** Most stories fall here—some uncertainty but manageable.

---

### +2 - Moderate Risk

**Description:** Significant uncertainty or multiple unknowns

**Characteristics:**
- New pattern or architecture for team
- Integration with unfamiliar third-party service
- Ambiguous or changing requirements
- External dependencies with uncertainty
- Limited team experience
- Moderate performance concerns (may need optimization)
- Moderate security concerns (sensitive data handling)

**Examples:**
- First-time OAuth implementation for team
- Integration with poorly documented API
- Requirements still being clarified with stakeholders
- New state management pattern
- Real-time features (WebSockets) if team inexperienced
- Payment handling (sensitive, requires testing)
- Performance-critical feature (may need profiling)

**When to Use:** Stepping into less familiar territory with notable risks.

---

### +3 - High Risk

**Description:** High uncertainty, needs research or spike first

**Characteristics:**
- Completely new architecture or pattern
- Critical external dependencies (unreliable, undocumented)
- Very ambiguous or incomplete requirements
- Multiple external dependencies with unknowns
- Team has no experience
- Performance critical (requires extensive optimization)
- Security critical (encryption, PII, financial data)
- May require R&D, proof-of-concept, or spike

**Examples:**
- Implementing payment processing (Stripe) for first time
- Real-time collaborative editing (complex algorithms)
- Performance optimization with no clear solution
- Security implementation (encryption, key management)
- Integration with undocumented or unstable API
- Cutting-edge technology (new framework version, experimental library)
- Distributed transactions or complex data consistency
- Requirements are vague ("make it faster", "improve UX")

**When to Use:** High-stakes or highly uncertain work; consider spike story first.

**Warning:** Stories with +3 risk should often be preceded by a spike story for research.

---

## Risk Factor Categories

### 1. Technical Familiarity Risk

**Question:** How familiar is the team with the required technology?

```
Expert (done many times)           → +0 risk
Familiar (done a few times)        → +0 risk
Some experience (done once/twice)  → +1 risk
Little experience (watched tutorial) → +2 risk
No experience (never done)         → +3 risk
```

**Examples:**
- Building CRUD endpoints (expert) → +0
- Using new validation library (some experience) → +1
- Implementing WebSockets (little experience) → +2
- ML model integration (no experience) → +3

---

### 2. External Dependency Risk

**Question:** Do we depend on external systems/services?

```
No external dependencies           → +0 risk
Well-documented, stable API        → +0 risk
Some documentation, mostly stable  → +1 risk
Poor documentation or flaky        → +2 risk
Undocumented, unstable, or unknown → +3 risk
```

**Examples:**
- Internal database query → +0
- Stripe API (excellent docs) → +0 to +1
- Lesser-known API (okay docs) → +1 to +2
- Undocumented internal service → +2 to +3

---

### 3. Requirements Clarity Risk

**Question:** How clear and stable are the requirements?

```
Crystal clear, signed off          → +0 risk
Clear, minor questions             → +0 risk
Some ambiguity, needs clarification → +1 risk
Significant ambiguity or changing  → +2 risk
Vague or actively changing         → +3 risk
```

**Examples:**
- "Add email field to form" (clear) → +0
- "Improve user experience" (vague) → +3
- "Add payment processing" (needs details) → +1 to +2

---

### 4. Performance/Scalability Risk

**Question:** Are there performance concerns?

```
No performance concerns            → +0 risk
Standard performance (no issues)   → +0 risk
May need optimization             → +1 risk
Performance critical              → +2 risk
Extreme performance requirements  → +3 risk
```

**Examples:**
- Admin dashboard (low traffic) → +0
- Public API endpoint → +1
- Real-time updates (latency-sensitive) → +2
- High-frequency trading system → +3

---

### 5. Security/Compliance Risk

**Question:** Are there security or compliance concerns?

```
No sensitive data                  → +0 risk
Standard security (authentication) → +0 risk
Sensitive data (passwords, emails) → +1 risk
Financial or PII data              → +2 risk
Highly regulated (HIPAA, PCI-DSS)  → +3 risk
```

**Examples:**
- Public blog post → +0
- User login → +1
- Payment processing → +2
- Healthcare records → +3

---

### 6. Integration Complexity Risk

**Question:** How many integrations, and how reliable are they?

```
No integrations                    → +0 risk
1-2 internal integrations          → +0 risk
3-4 integrations, all internal     → +1 risk
Multiple external integrations     → +2 risk
Many integrations + orchestration  → +3 risk
```

**Examples:**
- Single database query → +0
- Database + cache → +0
- Database + external API + message queue → +1
- Multiple APIs + webhooks + background jobs → +2 to +3

---

### 7. Testing Difficulty Risk

**Question:** How difficult is it to test this story?

```
Easy to unit test                  → +0 risk
Standard testing                   → +0 risk
Requires mocking/stubs             → +1 risk
Difficult to test (async, timing)  → +2 risk
Extremely difficult (distributed)  → +3 risk
```

**Examples:**
- Pure function → +0
- API endpoint with DB → +0
- WebSocket connection → +1
- Race condition fix → +2
- Distributed transaction → +3

---

## Risk Assessment Framework

### Step 1: Identify Risk Sources

List all sources of risk:

```markdown
Story: Stripe Payment Integration

Risk Sources:
1. Team has never integrated Stripe
2. Stripe webhook handling (external dependency)
3. Security critical (handling financial data)
4. Testing requires Stripe test environment
5. Requirements include refund/dispute handling (complex)
```

### Step 2: Assess Each Risk

Evaluate each risk source:

```markdown
1. Team unfamiliarity: +1 risk (first time, but docs are good)
2. External dependency: +1 risk (Stripe is stable, good docs)
3. Security critical: +1 risk (financial data, PCI concerns)
4. Testing complexity: +1 risk (need test environment setup)
5. Requirements complexity: +1 risk (refunds add scenarios)

Total: +5 risk factors identified
```

### Step 3: Calculate Total Risk

Map identified risks to 0-3 scale:

```markdown
0-1 risk factors   → +0 risk
2-3 risk factors   → +1 risk
4-5 risk factors   → +2 risk
6+ risk factors    → +3 risk

5 risk factors identified → +2 risk
```

**Alternative:** Take highest individual risk:

```markdown
Each factor above is +1
Highest individual risk: +1
But many risks compound → Increase to +2 risk
```

---

## Example Risk Analyses

### Example 1: Simple Feature (0 Risk)

**Story:** Add "bio" text field to user profile

**Risk Assessment:**
```
Technical Familiarity: Expert (done many times) → +0
External Dependencies: None → +0
Requirements Clarity: Crystal clear → +0
Performance: No concerns → +0
Security: Standard (user data, already secured) → +0
Integration: Single database update → +0
Testing: Easy (standard unit/integration tests) → +0

Total Risk: +0
```

**Risk Adjustment:** +0

---

### Example 2: Moderate Feature (+1 Risk)

**Story:** OAuth login with Google

**Risk Assessment:**
```
Technical Familiarity: Some experience (seen it done) → +1
External Dependencies: Google OAuth (stable, good docs) → +0
Requirements Clarity: Clear → +0
Performance: No concerns → +0
Security: Sensitive (authentication) → +1
Integration: Google + our auth system → +0
Testing: Requires Google test accounts → +1

Risk Factors: 3 total → +1 risk
```

**Risk Adjustment:** +1

---

### Example 3: Risky Feature (+2 Risk)

**Story:** Real-time collaborative document editing

**Risk Assessment:**
```
Technical Familiarity: No experience (never done) → +3
External Dependencies: WebSocket server → +1
Requirements Clarity: Some ambiguity (conflict resolution?) → +1
Performance: Critical (real-time latency) → +2
Security: Standard → +0
Integration: Multiple (WebSocket, DB, cache) → +1
Testing: Difficult (concurrency, race conditions) → +2

Risk Factors: Many, highest is +3
But team can research → Adjusted to +2
```

**Risk Adjustment:** +2

---

### Example 4: Very Risky Feature (+3 Risk)

**Story:** Implement payment processing with Stripe

**Risk Assessment:**
```
Technical Familiarity: No experience → +3
External Dependencies: Stripe (good docs but critical) → +1
Requirements Clarity: Clear but extensive → +1
Performance: Standard → +0
Security: CRITICAL (financial data, PCI) → +3
Integration: Stripe + webhooks + refunds + disputes → +2
Testing: Requires extensive test scenarios → +2

Risk Factors: Many, multiple +3 factors
Financial + security critical → +3 risk
```

**Risk Adjustment:** +3

**Recommendation:** Do spike story first to reduce risk.

---

## Risk Mitigation Strategies

### For +1 Risk (Minor)

**Strategies:**
- Pair programming (experienced + less experienced)
- Quick spike (1-2 hours) to validate approach
- Thorough code review
- Extra testing time

**Example:**
```
Story: OAuth with Google (+1 risk)
Mitigation:
- Pair with dev who's done OAuth before
- Set up Google test project before starting
- Extra time for security review
```

---

### For +2 Risk (Moderate)

**Strategies:**
- Dedicated spike story (4-8 hours)
- Prototype/proof-of-concept
- External expert consultation
- Comprehensive testing plan
- Architecture review

**Example:**
```
Story: Real-time collaboration (+2 risk)
Mitigation:
- Spike: Research OT vs CRDT algorithms (4 hours)
- Build small prototype with test data
- Review approach with senior architect
- Plan extensive concurrency testing
```

---

### For +3 Risk (High)

**Strategies:**
- REQUIRED spike story (8+ hours)
- External expert consultation or training
- Proof-of-concept with real integration
- Reduce scope if possible
- Consider vendor solution vs. build

**Example:**
```
Story: Payment with Stripe (+3 risk)
Mitigation:
- Spike: Stripe integration research (8 hours)
  - Set up test account
  - Test basic flow
  - Understand webhooks
  - Review security requirements
- Bring in security expert for review
- Start with minimal scope (charge only, no refunds)
- Add refunds/disputes in separate story
```

---

## Risk vs. Story Points

**Risk increases story points additively:**

```
Low Risk Story:
Complexity: 3, Effort: 3, Risk: +0
Story Points = (3 × 3) + 0 = 9 points

Same Story, Higher Risk:
Complexity: 3, Effort: 3, Risk: +2
Story Points = (3 × 3) + 2 = 11 points
```

**Effect:**
- +1 risk: Adds 1 point (small increase)
- +2 risk: Adds 2 points (moderate increase)
- +3 risk: Adds 3 points (significant increase)

**This reflects reality:** Risky stories take longer due to:
- Research time
- More careful implementation
- More thorough testing
- More review time
- Higher chance of rework

---

## Common Mistakes

### Mistake 1: Ignoring Team Familiarity

**Wrong:**
```
Story: Implement GraphQL (team never used)
Risk: +0 (GraphQL is well-known technology)
```

**Right:**
```
Story: Implement GraphQL (team never used)
Risk: +2 (new to TEAM, requires learning)
```

### Mistake 2: Underestimating External Dependencies

**Wrong:**
```
Story: Integrate with third-party API
Risk: +0 (API has docs)
```

**Right:**
```
Story: Integrate with third-party API
Risk: +1 (external dependency, may have rate limits, downtime, breaking changes)
```

### Mistake 3: Ignoring Security Implications

**Wrong:**
```
Story: Store credit card numbers
Risk: +1 (it's just a string field)
```

**Right:**
```
Story: Store credit card numbers
Risk: +3 (PCI-DSS compliance, encryption, security critical)
Alternative: Don't store, use Stripe tokens (risk: +1)
```

### Mistake 4: Confusing Risk with Complexity

**Wrong:**
```
Story: Complex algorithm (well-defined)
Complexity: 5
Risk: +3 (because it's complex)
```

**Right:**
```
Story: Complex algorithm (well-defined)
Complexity: 5 (hard to implement)
Risk: +0 (clearly defined, no unknowns)
```

**Key:** Risk is about UNKNOWNS, not difficulty.

---

## Risk Calibration

Track risk assessments:

```markdown
Story: OAuth Integration
Estimated Risk: +1
Actual Risk: +2

Why higher?
- OAuth provider docs outdated
- Token refresh flow more complex than expected
- Took 3 hours longer than estimated

Learning: OAuth integrations should be +2 risk by default
```

---

## Using This Scale

1. **Identify risk sources** - List all unknowns
2. **Assess each category** - Technical, dependencies, requirements, etc.
3. **Count risk factors** - How many significant risks?
4. **Map to 0-3 scale** - Total risk adjustment
5. **Document rationale** - Explain what contributes to risk
6. **Plan mitigation** - How to reduce or manage risk

**Remember:** Risk is about UNCERTAINTY and UNKNOWNS, not difficulty or volume. Complex work can have zero risk if it's well-understood.
