# Usage Examples

Real-world examples of validate-story skill in action with GO and NO-GO scenarios.

---

## Example 1: Perfect Story (GO - High Confidence)

### Scenario

Product Owner validates well-crafted user authentication story before sprint planning.

### Story Summary

```
Epic: epic-001 (User Management)
Story: story-003 (User Authentication System)
Status: Draft
```

### Validation Invocation

```bash
@validate-story .claude/stories/epic-001/story-003.md
```

### Validation Execution

```
⏳ Validating story...

Step 1/10: Template Completeness ✅ PASS
- All 9 required sections present
- No unfilled placeholders
- Meaningful content in all sections

Step 2/10: File Structure ✅ PASS
- 8 files referenced, all match project structure
- Consistent directory naming
- Test files in correct location

Step 3/10: UI/Frontend ⏭️ N/A
- Not a UI story

Step 4/10: Acceptance Criteria ✅ PASS
- 5 ACs, all covered by tasks
- All ACs measurable and testable
- Edge cases addressed

Step 5/10: Testing & Validation ✅ PASS
- Comprehensive test strategy
- Test scenarios for all ACs
- Jest + Supertest specified

Step 6/10: Security Considerations ✅ PASS
- Bcrypt hashing specified (salt rounds: 10)
- JWT with 1-hour expiry
- Rate limiting mentioned

Step 7/10: Tasks Sequence ✅ PASS
- 12 tasks in logical order
- Clear dependencies
- Appropriate granularity

Step 8/10: Anti-Hallucination ✅ PASS
- All files verified in project structure
- All libraries (bcrypt, jsonwebtoken, express-rate-limit) in package.json
- No invented details

Step 9/10: Implementation Readiness ✅ READY
- Readiness score: 9/10
- Comprehensive Dev Notes
- All technical context provided

Step 10/10: Report Generation ✅ COMPLETE
```

### Validation Report

```markdown
# Story Validation Report

**Story:** epic-001/story-003 - User Authentication System
**Validated:** 2025-01-15 14:30:00
**Validation Mode:** full

## Executive Summary

**Decision:** ✅ GO
**Readiness Score:** 9/10
**Confidence Level:** High

**Critical Issues:** 0
**Should-Fix Issues:** 2
**Nice-to-Have:** 1
**Anti-Hallucination Findings:** 0

## Validation Results

[All steps PASS]

## Should-Fix Issues (2)

**Issue #1: [TESTING] Add integration test scenarios**
- Recommendation: Add end-to-end test for complete auth flow
- Benefit: Catches integration issues early

**Issue #2: [DEV NOTES] Specify error message formats**
- Recommendation: Define exact error response structure
- Benefit: Consistent error handling

## Recommendation

### Decision: ✅ GO

Story is comprehensive and ready for implementation. Zero critical issues, high readiness score (9/10), and high confidence.

**Next Steps:**
1. Hand to James: `@james *implement story-003`
2. Address should-fix issues during implementation
```

### Outcome

✅ Story approved for implementation
✅ Developer Agent can proceed immediately
✅ Should-fix issues tracked for implementation phase

---

## Example 2: Missing Sections (NO-GO - Critical)

### Scenario

Story creator forgot to add Testing section, has unfilled placeholders.

### Story Summary

```
Epic: epic-002 (Payment System)
Story: story-007 (Stripe Integration)
Status: Draft
```

### Validation Invocation

```bash
@validate-story .claude/stories/epic-002/story-007.md
```

### Validation Execution

```
⏳ Validating story...

Step 1/10: Template Completeness ❌ FAIL
- Missing section: "Testing & Validation"
- Unfilled placeholder: {{EpicNum}} in Objective
- Unfilled placeholder: _TBD_ in Dependencies
- Empty section: "Security Considerations"

[... remaining steps ...]

Step 10/10: Report Generation ✅ COMPLETE
```

### Validation Report

```markdown
# Story Validation Report

**Story:** epic-002/story-007 - Stripe Integration
**Validated:** 2025-01-15 15:00:00
**Validation Mode:** full

## Executive Summary

**Decision:** ❌ NO-GO
**Readiness Score:** 4/10
**Confidence Level:** Low

**Critical Issues:** 4
**Should-Fix Issues:** 3
**Nice-to-Have:** 1
**Anti-Hallucination Findings:** 0

## Critical Issues (4) - MUST FIX

**Issue #1: [TEMPLATE] Missing "Testing & Validation" Section**
- Location: Required section not found
- Problem: Story has no testing section
- Impact: No test strategy, developer won't know how to validate
- Fix: Add "Testing & Validation" section with strategy, scenarios, tools

**Issue #2: [TEMPLATE] Unfilled Placeholder in Objective**
- Location: Objective section, line 8
- Problem: "Integrate {{EpicNum}} with Stripe"
- Impact: Objective is incomplete
- Fix: Replace {{EpicNum}} with "Payment System"

**Issue #3: [TEMPLATE] Unfilled Placeholder in Dependencies**
- Location: Dependencies section
- Problem: "_TBD_ - Need to verify Stripe SDK version"
- Impact: Dependencies unclear
- Fix: Specify Stripe SDK: "stripe ^12.0.0"

**Issue #4: [TEMPLATE] Empty "Security Considerations" Section**
- Location: Security Considerations section
- Problem: Section exists but has no content (payment handling requires security)
- Impact: Critical security requirements missing
- Fix: Add security requirements: PCI-DSS compliance, tokenization, no card storage

## Recommendation

### Decision: ❌ NO-GO

Story has 4 critical issues including missing required section and unfilled placeholders. Must fix before implementation.

**Next Steps:**
1. Add "Testing & Validation" section
2. Replace all {{placeholders}}
3. Complete Security Considerations section
4. Re-validate: `@validate-story .claude/stories/epic-002/story-007.md`
```

### Outcome

❌ Story blocked from implementation
❌ Creator must fix 4 critical issues
🔄 Re-validation required after fixes

---

## Example 3: Hallucinated Library (NO-GO - Anti-Hallucination)

### Scenario

Story mentions using "stripe-payments-sdk" library that doesn't exist in package.json.

### Validation Execution

```
Step 8/10: Anti-Hallucination ❌ FAIL
- Hallucinated library: "stripe-payments-sdk" not in package.json
- Hallucinated file: "src/services/payment-processor.ts" not in project structure
- Project uses: "src/payments/" not "src/services/"
```

### Critical Issues

```markdown
**Issue #1: [HALLUCINATION] Claims "stripe-payments-sdk" Library**
- Claimed: Dev Notes mention "using stripe-payments-sdk library"
- Reality: package.json has "stripe" not "stripe-payments-sdk"
- Fix: Change to official "stripe" library OR add to dependencies

**Issue #2: [HALLUCINATION] References Non-Existent File**
- Claimed: File List includes "src/services/payment-processor.ts"
- Reality: Project structure has "src/payments/" directory, not "src/services/"
- Fix: Update to "src/payments/stripe-processor.ts"
```

### Decision

```
Decision: ❌ NO-GO
Confidence: Low

Critical anti-hallucination findings. Story references non-existent library and incorrect file structure.
```

---

## Example 4: Uncovered Acceptance Criteria (NO-GO)

### Scenario

Story has AC4 "Password reset flow" but no tasks implement it.

### Validation Execution

```
Step 4/10: Acceptance Criteria ❌ FAIL

Coverage Analysis:
- AC1 "User can register" → Task 1.1, Task 1.2, Task 1.3 ✅
- AC2 "User can log in" → Task 2.1, Task 2.2 ✅
- AC3 "User can log out" → Task 3.1 ✅
- AC4 "Password reset flow" → No tasks found ❌
- AC5 "Session timeout" → Task 5.1 ✅
```

### Critical Issue

```markdown
**Issue #1: [AC] AC4 "Password reset flow" Has No Implementing Tasks**
- Location: Acceptance Criteria section
- Problem: AC4 is listed but no tasks address it
- Impact: Critical functionality won't be implemented
- Fix: Add tasks:
  - Task 4.1: Create password reset endpoint
  - Task 4.2: Generate reset tokens
  - Task 4.3: Send reset email
  - Task 4.4: Validate reset token
  - Task 4.5: Update password
```

### Decision

```
Decision: ❌ NO-GO
Readiness Score: 6/10
Confidence: Medium

AC4 is critical but has no implementing tasks. Must add before implementation.
```

---

## Example 5: Vague Tasks (NO-GO - Low Readiness)

### Scenario

Story has ambiguous tasks like "Implement authentication" without specifics.

### Validation Execution

```
Step 9/10: Implementation Readiness ❌ NOT READY

Readiness Score: 4/10

Vague Instructions (5):
1. Task 1: "Implement authentication"
   - Should specify: Which method? JWT? Sessions? OAuth?
2. Task 2: "Add database stuff"
   - Should specify: Which tables? Which columns? Schema migration?
3. Task 3: "Handle errors"
   - Should specify: Which errors? How to handle? Error response format?
4. Task 5: "Add tests"
   - Should specify: Which tests? Unit? Integration? Test scenarios?
5. Task 7: "Use best practices"
   - Should specify: Which practices? Security? Performance?
```

### Critical Issues

```markdown
**Issue #1: [READINESS] Vague Task Instructions**
- Location: Tasks section
- Problem: 5 tasks use ambiguous language
- Impact: Developer doesn't know what to implement
- Fix: Make tasks specific:
  - ❌ "Implement authentication"
  - ✅ "Implement JWT authentication with jsonwebtoken library, 1-hour expiry, refresh tokens"
```

### Decision

```
Decision: ❌ NO-GO
Readiness Score: 4/10
Confidence: Low

Too many vague tasks. Story not implementable without clarification.
```

---

## Example 6: GO with Warnings (Medium Confidence)

### Scenario

Story is mostly ready but has some should-fix issues.

### Validation Report

```markdown
## Executive Summary

**Decision:** ✅ GO (with warnings)
**Readiness Score:** 7/10
**Confidence Level:** Medium

**Critical Issues:** 0
**Should-Fix Issues:** 5
**Nice-to-Have:** 2

## Should-Fix Issues (5)

1. [TESTING] No integration test scenarios specified
2. [SECURITY] Missing rate limiting requirements
3. [FILES] Test file locations inconsistent
4. [TASKS] Task 3 slightly vague ("add validation")
5. [DEV NOTES] Integration points could be more detailed

## Recommendation

### Decision: ✅ GO (with caution)

Zero critical issues allows proceeding to implementation. However, 5 should-fix issues suggest story could be improved. Recommend addressing during development.

**Proceed with:**
- Regular check-ins during implementation
- Address should-fix issues as encountered
- May need clarifications during development
```

### Outcome

✅ Story approved for implementation
⚠️ Monitor should-fix issues during development
📝 Track issues for improvement

---

## Example 7: UI Story Complete (GO)

### Scenario

Frontend story with comprehensive component specifications.

### Validation Execution

```
Step 3/10: UI/Frontend Completeness ✅ PASS

Component Specifications:
- 4 components named (LoginForm, RegisterForm, AuthButton, ErrorMessage)
- Component hierarchy clear (AuthPage → LoginForm/RegisterForm → AuthButton)
- Props documented for all components

Styling/Design:
- Design system referenced (Material-UI)
- Responsive behavior specified (mobile/tablet/desktop)
- Accessibility addressed (ARIA labels, keyboard nav)

User Interactions:
- Form validation rules specified (email format, password length)
- Submit behavior documented
- Error states defined

Frontend-Backend Integration:
- API endpoints specified (POST /api/auth/login, POST /api/auth/register)
- Request/response formats documented
```

### Decision

```
Decision: ✅ GO
Readiness Score: 9/10
Confidence: High

Comprehensive UI specifications. Developer has all context needed.
```

---

## Example 8: Security Story (GO with Security Validation)

### Scenario

Authentication story with comprehensive security requirements.

### Validation Execution

```
Step 6/10: Security Considerations ✅ PASS

Security Requirements:
- Authentication method: JWT with refresh tokens
- Credential storage: bcrypt hashing, salt rounds 10
- Data protection: HTTPS required, JWT secret in env var
- Input validation: Joi schemas for email/password
- Vulnerability prevention:
  - SQL injection: Parameterized queries (Sequelize)
  - XSS: Input sanitization, output encoding
  - Rate limiting: express-rate-limit (100 req/15min)

Compliance:
- GDPR: User data deletion endpoint
- Session management: 1-hour access token, 7-day refresh token
```

### Decision

```
Decision: ✅ GO
Readiness Score: 9/10
Confidence: High

Comprehensive security requirements. All critical security aspects addressed.
```

---

## Example 9: Quick Validation Mode

### Scenario

User wants quick validation (critical issues only) during draft stage.

### Invocation

```bash
@validate-story .claude/stories/epic-003/story-010.md --mode quick
```

### Validation Execution

```
⏳ Quick validation (critical issues only)...

✅ Template Completeness: PASS
✅ File Structure: PASS
❌ Acceptance Criteria: FAIL (AC3 uncovered)
✅ Anti-Hallucination: PASS
⚠️ Implementation Readiness: 6/10

Critical Issues: 1
Decision: ❌ NO-GO
```

### Quick Report

```markdown
# Quick Validation Report

**Decision:** ❌ NO-GO
**Critical Issues:** 1

## Critical Issues

1. AC3 "User profile update" has no implementing tasks

## Recommendation

Fix critical issue and re-validate in full mode before implementation.
```

---

## Example 10: End-to-End Workflow

### Complete Story Lifecycle

```bash
# Step 1: Create story
@create-story epic-001 story-005 "User Profile Management"

# Story created at .claude/stories/epic-001/story-005.md

# Step 2: Validate story (draft)
@validate-story .claude/stories/epic-001/story-005.md --mode quick

# Result: NO-GO (missing Testing section)

# Step 3: Fix issues
# ... add Testing section ...

# Step 4: Re-validate (full)
@validate-story .claude/stories/epic-001/story-005.md

# Result: GO (readiness 8/10)

# Step 5: Proceed to implementation
@james *implement story-005

# James implements feature

# Step 6: Quality review
@quinn *review task-005

# Quinn finds issues, creates quality gate

# Step 7: Apply QA fixes
@james *apply-qa-fixes task-005

# Step 8: Re-review
@quinn *review task-005

# Result: PASS

# Step 9: Merge and deploy
git add .
git commit -m "Implement user profile management"
git push
```

---

## Common Patterns

### Pattern 1: Pre-Sprint Validation

```bash
# Validate all stories in sprint backlog
for story in .claude/stories/epic-*/story-*.md; do
  echo "Validating $story..."
  @validate-story $story --mode quick
done

# Result: Identify problematic stories before sprint planning
```

### Pattern 2: Auto-Validation Before Implementation

```bash
# James auto-validates before implementing
@james *implement story-012

# James internally runs:
# validate-story story-012
# If NO-GO: Report issues and block
# If GO: Proceed with implementation
```

### Pattern 3: Iterative Refinement

```bash
# Round 1: Draft
@validate-story story-draft.md --mode quick
# Result: NO-GO (3 critical issues)

# Fix critical issues

# Round 2: Full validation
@validate-story story-draft.md
# Result: GO (7/10, medium confidence)

# Address should-fix issues

# Round 3: Final validation
@validate-story story-final.md
# Result: GO (9/10, high confidence)

# Proceed to implementation
```

---

## Quick Reference

### Decision Guide

**GO if:**
- Readiness ≥ 7
- Critical issues ≤ 2
- No critical hallucinations

**NO-GO if:**
- Readiness < 7
- Critical issues > 2
- Any critical hallucination

### Common Critical Issues

1. Missing required section
2. Unfilled placeholder
3. Uncovered AC
4. Hallucinated file/library
5. Circular task dependencies
6. No testing section
7. Empty security section (for auth stories)

### Validation Modes

- `full`: All 10 steps (default)
- `quick`: Critical steps only (faster)
- `critical_only`: Blocking issues only

### Usage Patterns

```bash
# Standard validation
@validate-story {story-file}

# Quick validation
@validate-story {story-file} --mode quick

# Critical only
@validate-story {story-file} --mode critical_only
```

---
