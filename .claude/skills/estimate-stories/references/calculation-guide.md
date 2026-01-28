# Story Point Calculation Guide

Complete guide to calculating story points using the formula: **Story Points = (Complexity × Effort) + Risk**

---

## The Formula

```
Story Points = (Complexity × Effort) + Risk

Where:
- Complexity: 1-5 scale (technical difficulty)
- Effort: 1-5 scale (time/volume of work)
- Risk: 0-3 adjustment (unknowns/uncertainty)
```

**Result:** Story points on a scale roughly from 1 (trivial) to 28 (must split).

---

## Step-by-Step Calculation

### Example Story: User Signup with Email/Password

**Step 1: Analyze Complexity (1-5)**

```
Acceptance Criteria:
- Email/password form
- Validation with Zod
- Password hashing with bcrypt
- Duplicate email check
- JWT token generation
- Save to PostgreSQL

Analysis:
- 6 files to modify (controller, service, model, validation, migration, tests)
- Multiple integration points (DB, bcrypt, JWT, Zod)
- Multiple error paths (validation, duplicate, DB errors)
- Standard patterns (team familiar)

Complexity: 3 (Moderate)
```

**Step 2: Analyze Effort (1-5)**

```
Code Estimate:
- Controller: 50 LOC
- Service: 60 LOC
- Model: 30 LOC
- Validation: 30 LOC
- Migration: 20 LOC
- Total: ~190 LOC

Tests:
- 6 unit tests
- 4 integration tests
- Total: ~10 tests

Time: 3-4 hours

Effort: 3 (Medium)
```

**Step 3: Analyze Risk (0-3)**

```
Risk Factors:
- Team familiar with all tech ✓
- Requirements clear ✓
- Minor: bcrypt configuration, JWT security

Risk: +1 (Minor)
```

**Step 4: Calculate**

```
Story Points = (Complexity × Effort) + Risk
Story Points = (3 × 3) + 1
Story Points = 9 + 1
Story Points = 10 points
```

---

## Story Point Scale Interpretation

| Points | Size | Typical Time | Should Fit In |
|--------|------|--------------|---------------|
| 1-2 | Trivial | < 1 hour | Any sprint |
| 3-5 | Small | 1-3 hours | Any sprint |
| 6-10 | Medium | Half day | Any sprint |
| 11-15 | Large | 1 day | Any sprint |
| 16-20 | Very Large | 1-2 days | May need split |
| 21+ | Too Large | >2 days | **MUST split** |

**Rule of Thumb:**
- **< 13 points:** Acceptable size, can be implemented in one go
- **13-20 points:** Consider splitting if natural break points exist
- **> 20 points:** Must split into smaller stories

---

## Complete Calculation Examples

### Example 1: Trivial Story (1 point)

**Story:** Update button text from "Submit" to "Save"

```
Complexity: 1 (Trivial)
- Single file change
- No logic, just text update
- No tests needed

Effort: 1 (Minimal)
- 1 line of code
- <5 minutes
- No tests

Risk: +0 (No risk)
- Zero unknowns
- Done 100 times before

Story Points = (1 × 1) + 0 = 1 point
```

---

### Example 2: Small Story (5 points)

**Story:** Add "remember me" checkbox to login

```
Complexity: 2 (Simple)
- 2 files (frontend form, backend token logic)
- Simple pattern (extend JWT expiry)
- 1-2 edge cases

Effort: 2 (Low)
- ~80 LOC
- 3 tests
- 1-2 hours

Risk: +1 (Minor)
- Token expiry handling needs care
- Security consideration

Story Points = (2 × 2) + 1 = 5 points
```

---

### Example 3: Medium Story (10 points)

**Story:** User signup with email/password (as shown above)

```
Complexity: 3 (Moderate)
Effort: 3 (Medium)
Risk: +1 (Minor)

Story Points = (3 × 3) + 1 = 10 points
```

---

### Example 4: Large Story (16 points)

**Story:** Multi-step checkout flow (3 steps: cart → shipping → payment)

```
Complexity: 4 (Complex)
- 10 files (3 frontend components, 3 backend endpoints, state management, tests)
- State machine (step transitions, validation per step)
- 5+ integration points
- Many error paths

Effort: 4 (High)
- ~400 LOC
- 12 tests
- 6-7 hours

Risk: +0 (No significant risk)
- Team familiar with patterns
- Clear requirements

Story Points = (4 × 4) + 0 = 16 points
```

**Note:** 16 points—consider splitting, but acceptable if no natural break points.

---

### Example 5: Very Large Story (28 points → SPLIT!)

**Story:** Real-time collaborative document editing

```
Complexity: 5 (Very Complex)
- Operational transformation or CRDT algorithm
- WebSocket connections
- Conflict resolution
- 15+ files

Effort: 5 (Very High)
- ~700 LOC
- 20+ tests
- 10+ hours

Risk: +3 (High)
- Team never done
- Complex algorithms
- Performance critical

Story Points = (5 × 5) + 3 = 28 points
```

**Action Required:** MUST split into smaller stories:

```
Split 1: Basic real-time connection (8 points)
- WebSocket setup
- Simple text synchronization
- No conflict resolution

Split 2: Conflict resolution (13 points)
- Implement OT/CRDT
- Handle concurrent edits
- Comprehensive testing

Split 3: Performance optimization (7 points)
- Optimize sync protocol
- Reduce latency
- Stress testing
```

---

## Edge Cases and Special Scenarios

### Scenario 1: High Complexity, Low Effort

**Story:** Implement sophisticated algorithm (with reference implementation)

```
Complexity: 4 (Complex algorithm)
Effort: 2 (Only ~100 LOC, 2 hours)
Risk: +1 (Testing edge cases)

Story Points = (4 × 2) + 1 = 9 points
```

**Why:** Short code but cognitively demanding.

---

### Scenario 2: Low Complexity, High Effort

**Story:** Add 15 similar form fields with validation

```
Complexity: 1 (Trivial, copy-paste)
Effort: 4 (Tedious, ~500 LOC, 6 hours)
Risk: +0 (No unknowns)

Story Points = (1 × 4) + 0 = 4 points
```

**Why:** Simple but time-consuming.

---

### Scenario 3: Very Risky But Simple

**Story:** Integrate with undocumented third-party API

```
Complexity: 2 (Simple once figured out)
Effort: 2 (Small codebase)
Risk: +3 (Huge unknowns, may not work)

Story Points = (2 × 2) + 3 = 7 points
```

**Recommendation:** Do spike story first to reduce risk.

---

### Scenario 4: Zero Complexity, Reasonable Effort

**Story:** Manual data migration (export, transform, import)

```
Complexity: 1 (Straightforward scripts)
Effort: 3 (Time-consuming, careful work)
Risk: +1 (Data integrity concerns)

Story Points = (1 × 3) + 1 = 4 points
```

---

## Validation Rules

### Rule 1: Story Points > 20 → MUST SPLIT

```
If calculated points > 20:
  → Story is too large
  → Find natural split points in acceptance criteria
  → Create multiple smaller stories
  → Re-estimate each part
```

### Rule 2: Complexity = 5 AND Effort = 5 → RECONSIDER

```
If both Complexity = 5 AND Effort = 5:
  → Likely an epic, not a story
  → Break down by features or layers
  → Consider spike story for research
```

### Rule 3: Risk = 3 → SPIKE FIRST

```
If Risk = 3:
  → Too much uncertainty
  → Create spike story (time-boxed research)
  → After spike, re-estimate with lower risk
```

**Example:**

```
Original Story: Payment with Stripe (28 points, Risk +3)

Spike Story: Research Stripe Integration (5 points, 4 hours time-boxed)
- Set up test account
- Test basic flow
- Understand webhooks
- Document findings

After Spike: Payment with Stripe (16 points, Risk +1)
- Risk reduced from +3 to +1 through research
```

---

## Common Calculation Mistakes

### Mistake 1: Confusing Multiplication and Addition

**Wrong:**
```
Complexity: 3
Effort: 3
Risk: 2

Story Points = 3 × 3 × 2 = 18 points ❌
```

**Right:**
```
Story Points = (3 × 3) + 2 = 11 points ✓
```

**Remember:** Risk is ADDED, not multiplied.

---

### Mistake 2: Ignoring the Formula

**Wrong:**
```
Story feels like 8 points
→ Estimate 8 points (gut feeling)
```

**Right:**
```
Complexity: 3 (analyze systematically)
Effort: 3 (estimate LOC, tests, time)
Risk: +2 (identify specific risks)

Story Points = (3 × 3) + 2 = 11 points ✓
```

**Remember:** Use the formula for consistency.

---

### Mistake 3: Rounding Inappropriately

**Wrong:**
```
Complexity: 2.5 (between 2 and 3)
Effort: 2.5
Risk: +1

Story Points = (2.5 × 2.5) + 1 = 7.25 → round to 7
```

**Right:**
```
Complexity must be 2 or 3 (no decimals)
If uncertain: discuss with team, pick one
If truly between: round UP for safety

Complexity: 3 (round up when uncertain)
Effort: 3 (round up)
Risk: +1

Story Points = (3 × 3) + 1 = 10 points ✓
```

**Remember:** Complexity and Effort are integers (1-5), not decimals.

---

### Mistake 4: Double-Counting

**Wrong:**
```
Complexity: 4 (includes thinking about testing difficulty)
Effort: 4 (includes testing time)
Risk: +2 (includes testing uncertainty)

→ Testing counted 3 times!
```

**Right:**
```
Complexity: 3 (technical difficulty of implementation only)
Effort: 4 (includes all work: code + tests + docs)
Risk: +1 (unknowns about approach, not testing effort)

→ Each factor is distinct
```

**Key Distinctions:**
- **Complexity:** How HARD is the logic/design?
- **Effort:** How MUCH work (including all activities)?
- **Risk:** What UNKNOWNS could increase time?

---

## Formula Rationale

### Why Multiply Complexity × Effort?

```
High Complexity + High Effort = Exponentially Harder

Example:
- Simple code, small volume: (2 × 2) = 4 points (easy)
- Simple code, large volume: (2 × 5) = 10 points (tedious)
- Complex code, small volume: (5 × 2) = 10 points (challenging)
- Complex code, large volume: (5 × 5) = 25 points (very hard, should split)
```

**Rationale:** Complex work over large codebase is multiplicatively harder due to:
- More places to get things wrong
- Harder to test comprehensively
- More cognitive load
- Higher chance of bugs

---

### Why Add Risk (Not Multiply)?

```
Risk represents EXTRA time for unknowns, not a multiplier

Example with multiplication (WRONG):
Complexity: 3, Effort: 3, Risk: 3
Points = 3 × 3 × 3 = 27 points (too high!)

Example with addition (CORRECT):
Complexity: 3, Effort: 3, Risk: +3
Points = (3 × 3) + 3 = 12 points ✓
```

**Rationale:** Risk adds buffer time for:
- Research and learning
- Trial and error
- Unexpected issues
- Extra testing

This is additive overhead, not multiplicative.

---

## Calibration and Adjustment

### After Sprint Completion

Compare estimated vs. actual story points:

```markdown
Story: User Signup
Estimated: 10 points (Complexity: 3, Effort: 3, Risk: +1)
Actual: Took 5 hours (instead of estimated 3.5 hours)

Analysis:
- Complexity was accurate (moderate difficulty)
- Effort was underestimated (took longer to write tests)
- Risk was underestimated (bcrypt config issues)

Learning:
- Increase Effort to 4 for auth stories (more test scenarios)
- Or increase Risk to +2 for first-time security implementations

Adjusted Formula:
Story Points = (3 × 4) + 1 = 13 points (more accurate)
```

### Track Over Time

```markdown
Sprint 1 Velocity: 30 points completed
- Stories took longer than estimated
- Team learning curve

Sprint 2 Velocity: 40 points completed
- Estimation improving
- Team more efficient

Sprint 3 Velocity: 45 points completed
- Consistent estimation
- Predictable velocity
```

Use historical data to improve future estimations.

---

## Quick Reference Card

```
┌─────────────────────────────────────────┐
│ Story Point Formula                     │
│                                         │
│ Story Points = (C × E) + R              │
│                                         │
│ C = Complexity (1-5)                    │
│ E = Effort (1-5)                        │
│ R = Risk (0-3)                          │
│                                         │
│ Result:                                 │
│ 1-2:   Trivial                          │
│ 3-5:   Small                            │
│ 6-10:  Medium                           │
│ 11-15: Large                            │
│ 16-20: Very Large (consider split)     │
│ 21+:   Too Large (MUST split)          │
└─────────────────────────────────────────┘
```

---

## Using This Guide

1. **Analyze Complexity (1-5)** using complexity-scale.md
2. **Analyze Effort (1-5)** using effort-scale.md
3. **Analyze Risk (0-3)** using risk-factors.md
4. **Calculate:** (Complexity × Effort) + Risk
5. **Validate:** If >20, must split
6. **Document:** Record rationale for future reference
7. **Calibrate:** Adjust based on actual results

**Remember:** The formula provides consistency. Use it every time, don't rely on gut feeling alone.
