# Estimation Report Templates

Templates for formal estimation reports used in planning meetings, audits, or documentation.

---

## Basic Estimation Report

Use for simple stories or internal documentation.

```markdown
# Story Estimation: [Story Title]

## Summary

- **Story ID:** [story-xxx-yyy]
- **Story Points:** [X]
- **Estimated By:** [Name]
- **Date:** [YYYY-MM-DD]
- **Confidence:** [High/Medium/Low] ([XX]%)

## Formula Breakdown

**Story Points = (Complexity × Effort) + Risk**

- **Complexity:** [X]/5 - [Trivial/Simple/Moderate/Complex/Very Complex]
- **Effort:** [X]/5 - [Minimal/Low/Medium/High/Very High]
- **Risk:** +[X]/3 - [No Risk/Minor/Moderate/High]

**Calculation:** ([C] × [E]) + [R] = [Result] points

## Rationale

**Complexity ([X]/5):**
- [Reason 1]
- [Reason 2]
- [Reason 3]

**Effort ([X]/5):**
- [Estimated LOC]
- [Number of tests]
- [Estimated time]

**Risk (+[X]/3):**
- [Risk factor 1]
- [Risk factor 2]

## Recommendation

[Ready for sprint/Needs clarification/Consider splitting]
```

---

## Comprehensive Estimation Report

Use for complex stories, formal reviews, or external stakeholders.

```markdown
# Story Estimation Report

**Story ID:** [story-xxx-yyy]
**Title:** [Story Title]
**Date:** [YYYY-MM-DD]
**Estimated By:** [Name (Role)]

---

## Executive Summary

**Story Points:** [X]
**Confidence Level:** [High/Medium/Low] ([XX]%)
**Recommendation:** [Ready for sprint planning / Needs spike / Consider splitting]
**Sprint Suitability:** [Can fit in single sprint / Needs 2 sprints / Too large]

**Quick Stats:**
- Estimated Implementation Time: [X] hours
- Number of Files Affected: [X]
- Number of Tests Required: [X]
- Acceptance Criteria: [X]

---

## Story Context

**User Story:**
> As a [role],
> I want to [goal]
> So that [benefit].

**Acceptance Criteria:**
- AC-1: [Description]
- AC-2: [Description]
- AC-3: [Description]
- [...]

**Priority:** [P0/P1/P2/P3]
**Business Value:** [High/Medium/Low]

---

## Estimation Breakdown

### Formula: Story Points = (Complexity × Effort) + Risk

```
Complexity: [X]/5 ([Label])
Effort: [X]/5 ([Label])
Risk: +[X]/3 ([Label])

Calculation: ([C] × [E]) + [R] = [Result] points
```

### Complexity Analysis ([X]/5)

**Rating:** [X]/5 - [Trivial/Simple/Moderate/Complex/Very Complex]

**Technical Difficulty:**
- [Factor 1 with explanation]
- [Factor 2 with explanation]
- [Factor 3 with explanation]

**Integration Points:** [X]
- [Integration 1]
- [Integration 2]

**Error Scenarios:** [X]
- [Scenario 1]
- [Scenario 2]

**Architectural Impact:**
- [Description of system impact]

### Effort Analysis ([X]/5)

**Rating:** [X]/5 - [Minimal/Low/Medium/High/Very High]

**Code Volume Estimate:**
- Component A: ~[X] LOC
- Component B: ~[X] LOC
- Component C: ~[X] LOC
- **Total:** ~[X] LOC

**Testing Requirements:**
- Unit tests: [X]
- Integration tests: [X]
- E2E tests: [X]
- **Total:** [X] tests

**Documentation Needs:**
- [Doc type 1]
- [Doc type 2]

**Estimated Time:** [X] hours

### Risk Analysis (+[X]/3)

**Rating:** +[X]/3 - [No Risk/Minor/Moderate/High]

**Risk Factors:**
1. **[Risk Category]:** [Description] → +[X] risk
2. **[Risk Category]:** [Description] → +[X] risk
3. **[Risk Category]:** [Description] → +[X] risk

**Overall Risk Assessment:** [Description]

**Mitigation Strategies:**
- [Strategy 1]
- [Strategy 2]

---

## Confidence Assessment

**Confidence Level:** [High/Medium/Low] ([XX]%)

**Confidence Factors:**

**Increases Confidence (+):**
- [Factor that increases confidence]
- [Factor that increases confidence]

**Decreases Confidence (-):**
- [Factor that decreases confidence]
- [Factor that decreases confidence]

**Confidence Breakdown:**
- Requirements clarity: [High/Medium/Low]
- Technical familiarity: [High/Medium/Low]
- Dependency certainty: [High/Medium/Low]

---

## Comparable Stories

**Similar Stories for Reference:**

| Story ID | Title | Points | Similarity | Notes |
|----------|-------|--------|------------|-------|
| story-xxx-yyy | [Title] | [X] | [High/Medium] | [Note] |
| story-xxx-yyy | [Title] | [X] | [High/Medium] | [Note] |

**Why This Estimate Makes Sense:**
- [Comparison to similar story 1]
- [Comparison to similar story 2]

---

## Assumptions

**This estimation assumes:**
1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]
4. [Assumption 4]

**If assumptions change, re-estimation required.**

---

## Dependencies

**Technical Dependencies:**
- [Dependency 1] - [Status: Ready/Blocked/In Progress]
- [Dependency 2] - [Status]

**Team Dependencies:**
- [Team/Person 1] - [What's needed]
- [Team/Person 2] - [What's needed]

**External Dependencies:**
- [External service/API] - [Status]

---

## Splitting Recommendation

**Current Size:** [X] points

[ ] **No splitting needed** - Story is appropriately sized
[ ] **Optional split** - Could be split but not required
[ ] **Recommended split** - Story is large, splitting would improve predictability
[ ] **Required split** - Story is too large (>20 points), must be split

**If splitting recommended:**

### Proposed Split:

**Story 1:** [Title] - [X] points
- [AC-1]
- [AC-2]

**Story 2:** [Title] - [X] points
- [AC-3]
- [AC-4]

**Total after split:** [X] + [X] = [X] points (vs. [X] original)

---

## Sprint Planning Notes

**Sprint Suitability:**
- [ ] Can be completed in single sprint
- [ ] Requires multiple sprints
- [ ] Too large for sprint (needs splitting)

**Developer Level:**
- [ ] Junior developer suitable
- [ ] Mid-level developer recommended
- [ ] Senior developer required

**Pairing Recommended:** [Yes/No]
- Reason: [If yes, explain why]

**Blockers:**
- [Blocker 1, if any]
- [Blocker 2, if any]

**Prerequisites:**
- [Prerequisite 1]
- [Prerequisite 2]

---

## Risk Mitigation Plan

**For identified risks:**

| Risk | Severity | Mitigation Strategy | Owner |
|------|----------|---------------------|-------|
| [Risk 1] | [High/Med/Low] | [Strategy] | [Person] |
| [Risk 2] | [High/Med/Low] | [Strategy] | [Person] |

**Spike Stories Needed:**
- [ ] No spike needed
- [ ] Spike recommended ([X] hours)
- [ ] Spike required ([X] hours)

**Spike Details (if applicable):**
- **Goal:** [What to research/validate]
- **Time-box:** [X] hours
- **Deliverable:** [Document/Prototype/Decision]

---

## Approval

**Estimated By:**
- Name: [Name]
- Role: [Role]
- Date: [YYYY-MM-DD]

**Reviewed By:**
- Name: [Name]
- Role: [Role]
- Date: [YYYY-MM-DD]
- Status: [ ] Approved [ ] Needs Revision [ ] Rejected

**Comments:**
[Any reviewer comments]

---

## Changelog

| Date | Change | Reason | By |
|------|--------|--------|-----|
| [YYYY-MM-DD] | Initial estimation: [X] points | Story created | [Name] |
| [YYYY-MM-DD] | Revised to [X] points | [Reason] | [Name] |

---

*This estimation is based on current understanding and assumptions. Re-estimation may be required if scope, requirements, or dependencies change significantly.*
```

---

## Batch Estimation Summary Report

Use when estimating multiple stories together.

```markdown
# Batch Estimation Summary

**Date:** [YYYY-MM-DD]
**Estimated By:** [Name]
**Stories Estimated:** [X]
**Total Story Points:** [X]

---

## Summary Table

| Story ID | Title | Points | C | E | R | Confidence |
|----------|-------|--------|---|---|---|------------|
| story-xxx-001 | [Title] | [X] | [X] | [X] | +[X] | [High/Med/Low] |
| story-xxx-002 | [Title] | [X] | [X] | [X] | +[X] | [High/Med/Low] |
| story-xxx-003 | [Title] | [X] | [X] | [X] | +[X] | [High/Med/Low] |
| **Total** | | **[X]** | | | | |

---

## Distribution Analysis

**By Size:**
- Trivial (1-2 points): [X] stories
- Small (3-5 points): [X] stories
- Medium (6-10 points): [X] stories
- Large (11-15 points): [X] stories
- Very Large (16-20 points): [X] stories
- Too Large (21+ points): [X] stories → **Require splitting**

**By Confidence:**
- High confidence (>75%): [X] stories
- Medium confidence (50-75%): [X] stories
- Low confidence (<50%): [X] stories → **May need spike**

---

## Sprint Planning Recommendations

**Sprint Capacity:** [X] points (team velocity)

**Suggested Sprint Grouping:**

**Sprint 1:** [X] points
- story-xxx-001 ([X] points)
- story-xxx-002 ([X] points)
- story-xxx-003 ([X] points)

**Sprint 2:** [X] points
- story-xxx-004 ([X] points)
- story-xxx-005 ([X] points)

---

## Issues and Actions

**Stories Requiring Attention:**
- **[Story ID]:** Too large, needs splitting
- **[Story ID]:** Low confidence, needs spike
- **[Story ID]:** Blocked by dependency

**Action Items:**
1. [Action 1]
2. [Action 2]
3. [Action 3]

---

## Notes

[Any additional notes or context]

---

*Estimations reviewed and approved by: [Name], [Date]*
```

---

## Quick Estimation Card (For Agile Boards)

Minimal format for story cards or agile tools.

```markdown
## Story: [Title]

**Points:** [X]
**Confidence:** [●●●○○] [XX]%

**Formula:** ([C] × [E]) + [R] = [X]

**Why [X] points:**
- C=[X]: [One-line reason]
- E=[X]: [One-line reason]
- R=+[X]: [One-line reason]

**Ready:** [✓/✗]
```

---

## Using These Templates

### When to Use Basic Report
- Internal estimation
- Well-understood stories
- Quick documentation

### When to Use Comprehensive Report
- Complex or risky stories
- Formal planning meetings
- External stakeholder communication
- Audit requirements
- High-value stories (P0/P1)

### When to Use Batch Summary
- Epic breakdown estimation
- Sprint planning sessions
- Velocity planning
- Portfolio management

### When to Use Quick Card
- Story cards on board
- Agile tools (Jira, etc.)
- Quick reference
- Team communication

---

## Customization Tips

1. **Adjust detail level** - Remove sections not relevant to your team
2. **Add project-specific fields** - Sprint assignment, component, etc.
3. **Include visuals** - Charts, diagrams if helpful
4. **Link to references** - Link to ACs, PRD, designs
5. **Version control** - Track estimation changes over time

---

**Remember:** The template should serve the team, not burden it. Use the level of detail appropriate for the story's complexity and importance.
