# Workflow Patterns

## Overview

Understanding workflow patterns helps create effective checklists. This guide covers four primary patterns: linear, branching, cyclic, and validation workflows.

---

## Pattern 1: Linear Workflow

### Description
Sequential steps executed in order, one after another. Most straightforward pattern.

### Structure
```
Step 1 → Step 2 → Step 3 → Step 4 → Complete
```

### Characteristics
- Fixed sequence
- No branching
- No loops
- Each step depends on previous

### Examples

**Software Deployment:**
```
1. Run tests
2. Build application
3. Create deployment package
4. Deploy to staging
5. Verify staging
6. Deploy to production
7. Verify production
8. Mark deployment complete
```

**Document Review:**
```
1. Draft document
2. Self-review
3. Submit for peer review
4. Incorporate feedback
5. Submit for approval
6. Publish
```

### When to Use
- Process has clear, fixed sequence
- No decision points
- No conditional logic
- No need to repeat steps

---

## Pattern 2: Branching Workflow

### Description
Workflow splits based on decisions or conditions. Different paths lead to different outcomes.

### Structure
```
Step 1 → Step 2 → Decision Point
                    ├─ Path A → Step 3A → Step 4 → Complete
                    └─ Path B → Step 3B → Step 4 → Complete
```

### Characteristics
- Contains decision points
- Multiple possible paths
- Paths may converge later
- Conditional logic

### Examples

**Code Review Process:**
```
1. Submit pull request
2. Automated checks run
3. Reviewer evaluates code
4. DECISION: Approve or Request Changes?

   Path A (Approved):
   4A. Merge pull request
   5A. Deploy changes
   6A. Complete

   Path B (Changes Requested):
   4B. Developer addresses feedback
   5B. Update pull request
   6B. Return to Step 2 (re-review)
```

**Customer Support Ticket:**
```
1. Ticket received
2. Categorize issue
3. DECISION: Ticket type?

   Path A (Bug):
   3A. Assign to engineering
   4A. Fix bug
   5A. Deploy fix
   6A. Notify customer

   Path B (Feature Request):
   3B. Add to product backlog
   4B. Prioritize
   5B. Notify customer of timeline

   Path C (Question):
   3C. Provide answer
   4C. Close ticket
```

### When to Use
- Workflow has decision points
- Different scenarios require different actions
- Outcomes depend on conditions
- Multiple valid paths to completion

---

## Pattern 3: Cyclic Workflow

### Description
Workflow includes loops where steps repeat until condition met.

### Structure
```
Step 1 → Step 2 → Validation
                    ├─ Pass → Step 3 → Complete
                    └─ Fail → Return to Step 1 (or Step 2)
```

### Characteristics
- Contains loops/cycles
- Validation gates
- Steps repeat until success
- May have max iterations

### Examples

**Test-Driven Development:**
```
1. Write failing test
2. Implement feature
3. Run tests
4. VALIDATION: Tests pass?

   Pass:
   4A. Refactor code
   5A. Commit changes
   6A. Complete

   Fail:
   4B. Debug issues
   5B. Return to Step 2 (fix implementation)
```

**Content Publishing:**
```
1. Draft content
2. Submit for review
3. VALIDATION: Approved?

   Pass:
   3A. Publish content
   4A. Complete

   Fail:
   3B. Review feedback
   4B. Revise content
   5B. Return to Step 2 (re-submit)

   Note: Max 3 revision cycles before escalation
```

### When to Use
- Success depends on passing validation
- Steps may need repeating
- Quality gates required
- Iterative process

---

## Pattern 4: Validation Checklist

### Description
Collection of independent validation items. Order doesn't matter, all must be checked.

### Structure
```
⬜ Item 1
⬜ Item 2
⬜ Item 3
⬜ Item 4

All items must be ✅ to complete
```

### Characteristics
- Items are independent
- No sequence required
- Parallel execution possible
- All-or-nothing completion

### Examples

**Pre-Launch Checklist:**
```
Security:
- [ ] Penetration testing complete
- [ ] Security audit passed
- [ ] Credentials rotated
- [ ] HTTPS enforced

Performance:
- [ ] Load testing complete
- [ ] Performance benchmarks met
- [ ] CDN configured
- [ ] Caching enabled

Operations:
- [ ] Monitoring configured
- [ ] Alerting setup
- [ ] Backup verified
- [ ] Rollback plan documented

Legal:
- [ ] Terms of service updated
- [ ] Privacy policy reviewed
- [ ] GDPR compliance verified
- [ ] Data retention policy set
```

**Compliance Audit:**
```
- [ ] Access controls reviewed
- [ ] Audit logs enabled
- [ ] Data encryption verified
- [ ] Incident response plan current
- [ ] Employee training completed
- [ ] Third-party assessments done
```

### When to Use
- Multiple independent requirements
- No dependencies between items
- All items must be satisfied
- Order doesn't matter

---

## Pattern Combinations

### Linear + Validation Gates

```
Step 1 → Validation Gate 1 → Step 2 → Validation Gate 2 → Step 3 → Complete
           ├─ Pass → Continue               ├─ Pass → Continue
           └─ Fail → Stop                   └─ Fail → Stop
```

**Example: Software Release**
```
1. Code complete
2. VALIDATION: Code review passed?
   - Fail → Block release
   - Pass → Continue
3. Build application
4. VALIDATION: Tests passed?
   - Fail → Block release
   - Pass → Continue
5. Deploy to production
6. VALIDATION: Health checks passed?
   - Fail → Rollback
   - Pass → Complete
```

### Branching + Cyclic

```
Step 1 → Decision → Path A → Validation
                       ├─ Pass → Complete
                       └─ Fail → Return to Step 1

                    Path B → Step 3 → Complete
```

**Example: Bug Fix Workflow**
```
1. Identify bug
2. DECISION: Severity?

   Path A (Critical):
   3A. Hotfix branch
   4A. Implement fix
   5A. Test fix
   6A. VALIDATION: Tests pass?
      - Pass → Deploy immediately
      - Fail → Return to 4A (fix again)

   Path B (Normal):
   3B. Add to sprint backlog
   4B. Fix in normal cycle
```

### Parallel Workflows

```
Start → Fork into parallel streams
         ├─ Workflow A → Complete A
         ├─ Workflow B → Complete B
         └─ Workflow C → Complete C

       All complete → Merge → Final Step → Done
```

**Example: Product Launch**
```
Launch Preparation:

Parallel Streams:
├─ Marketing (4 weeks)
│  ├─ Create launch materials
│  ├─ Schedule social media
│  └─ Prepare press release
│
├─ Engineering (4 weeks)
│  ├─ Final features
│  ├─ Performance testing
│  └─ Deploy to production
│
└─ Support (4 weeks)
   ├─ Train support team
   ├─ Create documentation
   └─ Setup monitoring

All streams complete → Launch Day → Go Live
```

---

## Pattern Selection Guide

**Choose Linear when:**
- Fixed sequence
- No decisions needed
- Simple, straightforward process

**Choose Branching when:**
- Multiple possible paths
- Decision points exist
- Conditional logic required

**Choose Cyclic when:**
- Validation/quality gates needed
- May need to retry steps
- Success not guaranteed first try

**Choose Validation when:**
- Multiple independent requirements
- All must be satisfied
- Order doesn't matter

**Combine patterns when:**
- Complex workflows
- Multiple concerns (quality + decisions)
- Real-world complexity requires it

---

## Best Practices

1. **Keep it Simple** - Use simplest pattern that works
2. **Minimize Branching** - Too many paths confuse users
3. **Limit Cycles** - Set max iterations (prevent infinite loops)
4. **Clear Decision Criteria** - Make choices obvious
5. **Document Pattern** - State which pattern used
6. **Test Paths** - Verify all branches work
7. **Handle Edge Cases** - What if validation always fails?
8. **Provide Examples** - Show pattern in context

---

**Workflow Patterns - Part of interactive-checklist skill**
