# Risk Assessment & Filtering Guide

## Purpose

Assess refactoring risk levels and filter opportunities based on aggressiveness settings.

---

## Risk Levels

### Low Risk

**Characteristics:**
- Local changes (single file, small scope)
- No behavioral impact
- Simple transformations
- Easy to understand and verify
- Quick to apply (<2 minutes)

**Examples:**
- Rename variable/function
- Extract variable (no side effects)
- Inline unnecessary method
- Fix formatting/whitespace
- Add/improve comments

**When safe:**
- Good test coverage exists
- Tests cover affected code
- No external dependencies
- Clear, isolated change

---

### Medium Risk

**Characteristics:**
- Multiple files or moderate scope
- Behavioral preservation critical
- Moderate complexity
- Requires careful verification
- Takes 5-15 minutes

**Examples:**
- Extract method
- Simplify conditionals
- Remove duplication
- Move method within same module
- Refactor class structure

**When safe:**
- Comprehensive test coverage
- Tests cover all branches
- Dependencies well-understood
- Incremental application possible

---

### High Risk

**Characteristics:**
- Large scope (multiple files/modules)
- Complex transformations
- Many dependencies
- Significant structural changes
- Takes 15+ minutes

**Examples:**
- Extract class
- Change method signature
- Move method between modules
- Restructure inheritance
- Large-scale duplication removal

**When safe:**
- Excellent test coverage (>90%)
- All dependencies mapped
- Can be broken into smaller refactorings
- Multiple developers review

---

## Priority Levels

### P0 - Critical

**When to assign:**
- Addresses critical quality issue
- Fixes high severity problem
- Required for production readiness
- Blocks other work

**Examples:**
- Validation in route handler (security issue)
- Sensitive data logged (security issue)
- Blocking performance bottleneck
- Critical maintainability problem

**Always include in:** Conservative, Moderate, Aggressive

---

### P1 - High

**When to assign:**
- Reduces significant technical debt
- Improves maintainability substantially
- Addresses medium severity issue
- Recommended by quality review

**Examples:**
- Password hashing inline (should be utility)
- Repeated business logic (DRY violation)
- God object (too many responsibilities)
- Complex method (>50 lines, hard to understand)

**Include in:** Moderate, Aggressive

---

### P2 - Medium

**When to assign:**
- Improves code quality
- Nice-to-have improvement
- Minor technical debt
- Proactive improvement

**Examples:**
- Unclear variable names
- Minor code duplication
- Missing type annotations
- Suboptimal structure

**Include in:** Aggressive

---

### P3 - Low

**When to assign:**
- Optional improvement
- Cosmetic changes
- Future-proofing
- Not blocking anything

**Examples:**
- Formatting inconsistencies
- Documentation improvements
- Minor naming improvements

**Include in:** Never (manual only)

---

## Aggressiveness Levels

### Conservative

**Philosophy:** Safety first, only critical fixes

**Selection criteria:**
- P0 priority only
- Low risk only
- Clear, obvious improvements
- High confidence in test coverage

**Example selection:**
```
Available refactorings:
1. P0, Low Risk: Rename unclear variable
2. P0, Medium Risk: Extract validation logic
3. P1, Low Risk: Extract password hashing
4. P1, Medium Risk: Simplify conditionals

Conservative selection: #1 only
```

**Use when:**
- First time using automated refactoring
- Project lacks comprehensive tests
- High-stakes production code
- Team prefers manual review

**Typical count:** 1-3 refactorings per session

---

### Moderate (Recommended)

**Philosophy:** Balanced approach, recommended improvements

**Selection criteria:**
- P0 + P1 priorities
- Low + medium risk
- Clear quality benefits
- Good test coverage required

**Example selection:**
```
Available refactorings:
1. P0, Low Risk: Rename unclear variable
2. P0, Medium Risk: Extract validation logic
3. P1, Low Risk: Extract password hashing
4. P1, Medium Risk: Simplify conditionals
5. P2, Low Risk: Add interface for DI

Moderate selection: #1, #2, #3, #4
```

**Use when:**
- Reasonable test coverage (>70%)
- Quality review identifies issues
- Systematic debt reduction needed
- Team comfortable with automation

**Typical count:** 3-8 refactorings per session

---

### Aggressive

**Philosophy:** Comprehensive improvements, all opportunities

**Selection criteria:**
- P0 + P1 + P2 priorities
- All risk levels
- Any quality improvement
- Excellent test coverage required (>85%)

**Example selection:**
```
Available refactorings:
1. P0, Low Risk: Rename unclear variable
2. P0, Medium Risk: Extract validation logic
3. P1, Low Risk: Extract password hashing
4. P1, Medium Risk: Simplify conditionals
5. P1, High Risk: Extract class for auth logic
6. P2, Low Risk: Add interface for DI
7. P2, Medium Risk: Move methods to better classes

Aggressive selection: All 7
```

**Use when:**
- Excellent test coverage (>85%)
- Major refactoring needed
- Team experienced with patterns
- Time allocated for review

**Typical count:** 5-15 refactorings per session

---

## Risk Assessment Process

### Step 1: Identify Pattern

Match code issue to refactoring pattern:
- Extract Method → Medium Risk
- Rename → Low Risk
- Extract Class → High Risk

**See:** `refactoring-patterns.md` for pattern catalog

---

### Step 2: Assess Scope

**Single file, local change:**
- Risk -1 level (Medium → Low)

**Multiple files, cross-module:**
- Risk +1 level (Medium → High)

**Example:**
```
Rename variable within single function:
Base risk: Low
Scope: Single file, local
Adjusted risk: Low

Extract class across 5 files:
Base risk: High
Scope: Multiple files, cross-module
Adjusted risk: High (no change, already high)
```

---

### Step 3: Check Dependencies

**No external dependencies:**
- Risk -1 level

**Many external dependencies:**
- Risk +1 level

**Example:**
```
Extract method with no external calls:
Base risk: Medium
Dependencies: None (self-contained)
Adjusted risk: Low

Extract method with database/API calls:
Base risk: Medium
Dependencies: Many (DB, APIs, external services)
Adjusted risk: High
```

---

### Step 4: Verify Test Coverage

**Excellent coverage (>85%):**
- Risk -1 level

**No coverage (<50%):**
- Risk +2 levels (often becomes too risky)

**Example:**
```
Simplify conditionals with 100% branch coverage:
Base risk: Medium
Test coverage: Excellent (100%)
Adjusted risk: Low

Simplify conditionals with 30% branch coverage:
Base risk: Medium
Test coverage: Poor (30%)
Adjusted risk: High (unsafe)
```

---

### Step 5: Final Risk Determination

**Calculate final risk:**
```
Final Risk = Base Risk + Scope Adjustment + Dependency Adjustment + Coverage Adjustment

If Final Risk > High:
  Mark as "Too Risky - Manual Only"
```

---

## Filtering Algorithm

### Input
- List of identified refactorings
- User's chosen aggressiveness level
- Test coverage metrics

### Process

**For each refactoring:**

1. **Assess risk (using process above)**
   ```
   base_risk = pattern_risk
   final_risk = base_risk + scope_adj + deps_adj + coverage_adj
   ```

2. **Check aggressiveness filter:**
   ```
   if aggressiveness == "conservative":
     include = (priority == P0) and (final_risk == Low)

   if aggressiveness == "moderate":
     include = (priority in [P0, P1]) and (final_risk in [Low, Medium])

   if aggressiveness == "aggressive":
     include = (priority in [P0, P1, P2]) and (final_risk in [Low, Medium, High])
   ```

3. **Add to selected list if included**

4. **Sort by priority (P0 first), then risk (Low first)**

### Output
- Filtered, sorted list of refactorings to apply

---

## Example Assessment

**Scenario:** Extract validation logic from signup route

**Step 1: Identify pattern**
- Pattern: Extract Method
- Base risk: Medium

**Step 2: Assess scope**
- Current: Validation in route handler (1 file)
- Target: Extract to validation utility (new file)
- Scope: 2 files (moderate)
- Adjustment: +0 (already medium risk for multi-file)

**Step 3: Check dependencies**
- Dependencies: None (pure validation logic)
- Adjustment: -1 level (no external dependencies)
- Risk: Medium → Low

**Step 4: Verify coverage**
- Route handler tests: 90% coverage
- Validation cases: All branches covered
- Coverage: Excellent
- Adjustment: -0 (already lowered by dependencies)
- Final risk: Low

**Step 5: Priority assignment**
- Quality finding: "High severity - Validation in route handler"
- Priority: P0 (addresses high severity issue)

**Final assessment:**
```
Refactoring: Extract validation logic
Pattern: Extract Method
Priority: P0
Risk: Low (final, adjusted from Medium)
Rationale: Addresses high severity issue, good coverage, no dependencies
```

**Filtering:**
- Conservative: ✅ Include (P0 + Low Risk)
- Moderate: ✅ Include (P0 + Low Risk)
- Aggressive: ✅ Include (P0 + Low Risk)

---

## Safety Checks

Before applying any refactoring, verify:

- [ ] **Tests exist** for affected code
- [ ] **Tests are passing** (100% pass rate)
- [ ] **Coverage adequate** for risk level:
  - Low Risk: >50% coverage
  - Medium Risk: >70% coverage
  - High Risk: >85% coverage
- [ ] **Dependencies mapped** and understood
- [ ] **Scope clear** (know what files will change)
- [ ] **Rollback plan** ready (backup created)

**If any check fails:**
- Mark refactoring as "Too Risky - Manual Only"
- Log reason in assessment
- Skip in automated session

---

## Risk Mitigation Strategies

### For Medium Risk Refactorings

1. **Break into smaller steps**
   - Split large extract method into multiple smaller extractions
   - Apply incrementally

2. **Add tests first**
   - Write additional tests for edge cases
   - Ensure 100% branch coverage

3. **Use feature flags**
   - Deploy refactored code behind flag
   - Enable gradually

---

### For High Risk Refactorings

1. **Manual review required**
   - Don't apply automatically
   - Create task for manual refactoring
   - Document rationale and approach

2. **Spike/prototype first**
   - Test approach in branch
   - Verify tests remain green
   - Review with team

3. **Break down aggressively**
   - Convert high-risk to multiple low/medium risk refactorings
   - Apply over multiple sessions

---

## Quick Reference

**Risk Levels:**
- Low: Local, simple, fast (<2 min)
- Medium: Multi-file, moderate complexity (5-15 min)
- High: Large scope, complex (15+ min)

**Priorities:**
- P0: Critical (always in Conservative)
- P1: High (Moderate and Aggressive)
- P2: Medium (Aggressive only)
- P3: Low (Manual only)

**Aggressiveness:**
- Conservative: P0 + Low Risk only
- Moderate: P0+P1 + Low+Medium Risk
- Aggressive: P0+P1+P2 + All Risk

**Coverage Requirements:**
- Low Risk: >50%
- Medium Risk: >70%
- High Risk: >85%

---

*Part of refactor-code skill - Quality Suite*
