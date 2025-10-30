# Story Quality Assessment Guide

## Purpose

Evaluation criteria for assessing user story quality using the INVEST model and quality scoring matrix.

---

## INVEST Criteria (Definition of Ready)

A story is ready for sprint when it meets all 6 INVEST criteria:

### 1. Independent
**Question:** Can this story be worked on without waiting for other stories?

**Good:**
- Story has no dependencies
- All dependencies are already complete
- Dependencies are clearly documented with workarounds

**Poor:**
- Story blocked by multiple incomplete stories
- Dependencies unclear or undocumented

---

### 2. Negotiable
**Question:** Is there flexibility on how to implement this?

**Good:**
- Story describes "what" not "how"
- Implementation approach is open to discussion
- Technical notes are guidance, not prescription

**Poor:**
- Story dictates exact implementation
- No room for developer creativity
- Overly prescriptive

---

### 3. Valuable
**Question:** Does this deliver clear value to user or business?

**Good:**
- Value articulated in "So that..." clause
- Solves real user problem
- Business case is clear

**Poor:**
- No clear value stated
- Technical story with no user benefit
- Circular value ("so that the system works")

---

### 4. Estimable
**Question:** Can the team estimate this with confidence?

**Good:**
- Story is clear and understood
- Technical approach is known
- Similar stories have been done before
- Team has 70%+ confidence in estimate

**Poor:**
- Story is vague or unclear
- Too many unknowns
- Never done anything like this before
- Team confidence <50%

---

### 5. Small
**Question:** Can this fit in one sprint?

**Good:**
- ≤13 story points
- 1-3 days of work
- Single developer can complete it
- Fits comfortably in sprint

**Poor:**
- >13 story points
- >3 days of work
- Would span multiple sprints
- Needs to be split

---

### 6. Testable
**Question:** Is it clear how to verify this works?

**Good:**
- Acceptance criteria are specific
- AC can be verified with tests
- Success/failure is unambiguous

**Poor:**
- AC are vague ("works well", "is fast")
- Not clear how to verify
- Subjective criteria

---

## Quality Scoring Matrix

Score each dimension on 1-4 scale:

| Dimension | Poor (1) | Fair (2) | Good (3) | Excellent (4) |
|-----------|----------|----------|----------|---------------|
| **Title** | Vague | Generic | Descriptive | Specific & action-oriented |
| **Narrative** | Missing/incomplete | Basic format | Clear value | Compelling value prop |
| **AC** | None or 1-2 vague | 2-3 generic | 3-5 specific | 5-8 comprehensive & testable |
| **Technical Notes** | None | Minimal | Moderate | Detailed with links |
| **Edge Cases** | None | 1-2 mentioned | Several identified | Comprehensive list |
| **Dependencies** | Unclear | Mentioned | Listed | Detailed with impact |

**Overall Quality Score = Average of all dimensions**

---

## Scoring Examples

### Example 1: Poor Quality (1.5/4)

```markdown
Title: Login Feature
User Story: Users should be able to login.
AC: 
- Login works
- Users can access their account
Priority: P0
```

**Scores:**
- Title: 1 (too generic, no "how")
- Narrative: 1 (missing As a.../I want.../So that...)
- AC: 1 (vague, untestable)
- Technical Notes: 1 (missing)
- Edge Cases: 1 (missing)
- Dependencies: 2 (not mentioned)

**Overall: 1.2/4** → Not ready for sprint ❌

---

### Example 2: Excellent Quality (3.8/4)

```markdown
Title: User Login with Email and Password

User Story:
As a registered user,
I want to log in with my email and password
So that I can access my personalized account and data securely.

Acceptance Criteria:
**Happy Path:**
- AC-1: User can enter email and password on login form
- AC-2: Valid credentials return 200 with JWT token
- AC-3: User redirected to dashboard after successful login

**Validation:**
- AC-4: Invalid email format returns 400 with "Invalid email format"
- AC-5: Empty password returns 400 with "Password is required"

**Error Handling:**
- AC-6: Wrong password returns 401 with "Invalid credentials"
- AC-7: Non-existent email returns 401 with "Invalid credentials"

**Security:**
- AC-8: Password never exposed in logs or responses
- AC-9: Login attempts logged with timestamp, IP, outcome
- AC-10: Account locked for 15 min after 5 failed attempts

**Performance:**
- AC-11: Login response time < 500ms for 95% of requests

Technical Notes:
- Node.js with TypeScript
- Express.js, PostgreSQL, Redis
- bcrypt (cost 12) for hashing
- jsonwebtoken for JWT
- Rate limiting: 5 attempts / 10 min

Edge Cases:
1. Password exactly 12 characters (minimum)
2. Email with + symbol (user+tag@domain.com)
3. Same user logs in from 2 browsers simultaneously
4. Database connection lost mid-login

Dependencies: story-auth-001 (Signup)

Priority: P0
```

**Scores:**
- Title: 4 (specific, clear mechanism)
- Narrative: 4 (complete format with clear value)
- AC: 4 (11 specific, testable AC across categories)
- Technical Notes: 3 (tech stack and key decisions documented)
- Edge Cases: 3 (several identified)
- Dependencies: 4 (clearly documented)

**Overall: 3.7/4** → Ready for sprint ✅

---

## Assessment Workflow

### Step 1: Read Story
Parse all components from story file.

### Step 2: Score Each Dimension
Use matrix above to score 1-4 for each dimension.

### Step 3: Calculate Overall Score
Average all dimension scores.

### Step 4: Check INVEST
Verify all 6 INVEST criteria are met.

### Step 5: Determine Readiness
- Score ≥3.0 AND all INVEST met → ✅ Ready
- Score 2.0-2.9 → ⚠️ Needs refinement
- Score <2.0 → ❌ Significant refinement needed

### Step 6: Identify Gaps
List specific issues to address during refinement.

---

## Gap Identification

Common gaps to look for:

**Narrative Issues:**
- Missing "As a..." persona
- Missing "I want..." action
- Missing "So that..." value
- Generic language
- Technical jargon

**AC Issues:**
- Too few AC (<3)
- Vague AC ("works", "fast")
- Not testable
- Missing categories (validation, errors, security)
- Not numbered

**Technical Issues:**
- No tech stack specified
- No architecture guidance
- Missing security considerations
- No data models
- No API contracts

**Edge Case Issues:**
- No edge cases identified
- Only happy path considered
- Boundary conditions not tested

**Dependency Issues:**
- Dependencies not mentioned
- Blocking relationships unclear
- No workarounds for blockers

---

## Confidence Levels

After scoring, assign confidence level:

| Score | Level | Confidence | Ready? |
|-------|-------|------------|--------|
| 3.5-4.0 | Excellent | High (90%+) | ✅ Yes |
| 3.0-3.4 | Good | High (80-89%) | ✅ Yes |
| 2.5-2.9 | Fair | Medium (65-79%) | ⚠️ Needs polish |
| 2.0-2.4 | Needs Work | Medium (50-64%) | ❌ Needs refinement |
| <2.0 | Poor | Low (<50%) | ❌ Significant refinement |

---

*Part of refine-story skill - BMAD Enhanced*
