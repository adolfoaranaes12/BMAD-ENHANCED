# BMAD Enhanced: Automated Development Workflow

**Vision:** Transform high-level requirements into production-ready code through orchestrated subagent workflows with integrated quality assurance.

**Date:** 2025-10-28

---

## Vision Statement

**From This (Manual):**
```
User: "Build user authentication with email/password"
  ↓
Developer manually:
  1. Plans architecture
  2. Writes code
  3. Writes tests
  4. Reviews quality
  5. Creates PR
  6. Deploys
```

**To This (Automated):**
```
User: "Build user authentication with email/password"
  ↓
System automatically:
  1. Alex (Planner) → Creates detailed task spec
  2. James (Developer) → Implements with tests
  3. Quinn (Quality) → Reviews and validates
  4. GitHub MCP → Creates PR with quality reports
  5. User → Reviews and approves
  6. GitHub MCP → Merges and deploys
```

**Goal:** 10x faster delivery with higher quality through automation + AI + quality assurance.

---

## Complete Workflow Architecture

### Layer 1: User Interface (Human Input)

**Input Formats:**

1. **Scrum Story Format:**
```markdown
As a user, I want to sign up with email and password
so that I can create an account and access the system.

Acceptance Criteria:
- User can enter email and password
- Password must be at least 8 characters
- Email must be valid format
- Duplicate emails are rejected
- Confirmation email sent on successful signup
```

2. **Natural Language Prompt:**
```
"Build a user signup endpoint that validates email, hashes password with bcrypt,
stores in database, and sends confirmation email. Include rate limiting and tests."
```

3. **Feature Request:**
```
Feature: User Authentication
- POST /api/auth/signup
- POST /api/auth/login
- GET /api/auth/verify-email
Security: JWT tokens, bcrypt hashing
```

**Entry Point:**
```bash
# Single command kicks off entire workflow
@orchestrator *build "user authentication with email/password signup"
```

---

### Layer 2: Orchestrator (Workflow Coordinator)

**Role:** Routes work through subagents, manages handoffs, maintains context

**Orchestrator Decision Tree:**

```
User Input
    ↓
Classify Request Type:
  - New Feature → Alex (plan) → James (implement) → Quinn (review) → GitHub (PR)
  - Bug Fix → James (debug) → James (fix) → Quinn (review) → GitHub (PR)
  - Refactor → James (refactor) → Quinn (review) → GitHub (PR)
  - Quality Check → Quinn (review existing task)
  - Urgent Hotfix → James (implement) → Quick review → GitHub (PR, skip full review)
```

**State Management:**

```yaml
workflowState:
  requestId: "req-2025-10-28-001"
  currentPhase: "implementation"
  currentSubagent: "james"
  taskId: "task-007"

  history:
    - phase: "planning"
      subagent: "alex"
      startTime: "2025-10-28T10:00:00Z"
      endTime: "2025-10-28T10:03:00Z"
      output: ".claude/tasks/task-007-user-signup.md"
      status: "complete"

    - phase: "implementation"
      subagent: "james"
      startTime: "2025-10-28T10:03:00Z"
      endTime: null
      output: null
      status: "in_progress"

  nextPhase: "quality_review"
  estimatedCompletion: "2025-10-28T10:30:00Z"
```

---

### Layer 3: Subagents (Specialized Personas)

#### Alex (Planner) - Technical Planning Specialist

**Commands:**
- `@alex *plan "<feature description>"` → Create task specification
- `@alex *refine "<requirements>"` → Refine vague requirements
- `@alex *estimate task-007` → Estimate effort and complexity
- `@alex *breakdown task-007` → Break into subtasks

**Workflow Integration:**
```
Input: User story or feature request
  ↓
Skills Executed:
  1. create-task-spec.md
  2. estimate-effort.md (optional)
  ↓
Output: .claude/tasks/task-007-{slug}.md (hyper-detailed spec)
  ↓
Handoff: "Task spec ready for implementation. @james *implement task-007"
```

**Example:**
```
User: @orchestrator *build "user authentication"

Orchestrator: Routing to Alex for planning...

Alex: I'll create a detailed task specification for user authentication.

[Executes create-task-spec.md]

Task specification complete:
- Task ID: task-007
- Title: User Authentication with Email/Password
- 6 acceptance criteria
- Full context embedded (architecture, data models, APIs)
- Estimated effort: 4-6 hours

File: .claude/tasks/task-007-user-auth.md

Handing off to James for implementation...
```

---

#### James (Developer) - Senior Software Engineer

**Commands:**
- `@james *implement task-007` → Implement task specification
- `@james *refactor task-007` → Refactor existing code
- `@james *debug issue-123` → Debug and fix issue
- `@james *test task-007` → Write/run tests

**Workflow Integration:**
```
Input: Task specification (from Alex)
  ↓
Skills Executed:
  1. execute-task.md
  2. write-tests.md (integrated)
  ↓
Output:
  - Implementation files (src/, tests/)
  - Updated task file (Implementation Record)
  ↓
Handoff: "Implementation complete. @quinn *review task-007"
```

**Example:**
```
Alex: @james *implement task-007

James: I'll implement the user authentication feature.

[Executes execute-task.md - sequential steps]

Step 1/5: Creating user model with Prisma schema
✓ Created: prisma/schema.prisma (User model)

Step 2/5: Implementing signup endpoint
✓ Created: src/routes/auth/signup.ts
✓ Created: src/services/auth/signup.service.ts
✓ Created: src/validators/auth.validator.ts

Step 3/5: Implementing password hashing with bcrypt
✓ Updated: src/services/auth/signup.service.ts

Step 4/5: Writing unit and integration tests
✓ Created: src/services/auth/__tests__/signup.service.test.ts
✓ Created: src/routes/auth/__tests__/signup.integration.test.ts

Step 5/5: Running tests and validating
✓ All tests passing (15 tests, 94% coverage)

Implementation complete:
- Files changed: 8 (4 source, 4 test)
- Lines added: 450
- Tests: 15 (12 unit, 3 integration)
- Coverage: 94%

Task status: Ready for Review

Handing off to Quinn for quality review...
```

---

#### Quinn (Quality) - Test Architect & Quality Advisor

**Commands:**
- `@quinn *review task-007` → Full quality review (all 5 skills)
- `@quinn *risk task-007` → Risk assessment only
- `@quinn *trace task-007` → Traceability check only
- `@quinn *gate task-007` → Quality gate decision

**Workflow Integration:**
```
Input: Completed implementation (from James)
  ↓
Skills Executed:
  1. risk-profile.md
  2. test-design.md
  3. trace-requirements.md
  4. nfr-assess.md
  5. quality-gate.md
  ↓
Output:
  - 5 assessment reports
  - Quality gate decision (PASS/CONCERNS/FAIL)
  ↓
Handoff:
  - If PASS: "Quality gate passed. Ready for PR."
  - If CONCERNS: "Quality gate has concerns. Review recommended, but can proceed."
  - If FAIL: "Quality gate failed. Address critical issues before proceeding."
```

**Example:**
```
James: @quinn *review task-007

Quinn: I'll perform comprehensive quality review.

[Executes review-task.md orchestrator]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Quality Review Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quality Gate Decision: ⚠️ CONCERNS
Overall Quality Score: 75.5%

Key Findings:
✓ All 6 acceptance criteria implemented and tested
✓ Test coverage: 94% (excellent)
✓ Security: Good (input validation, password hashing)
⚠️ Performance: N+1 query in user listing (should fix)
⚠️ Missing: Rate limiting on login endpoint

Action Items (P1 - Should fix before release):
1. Add rate limiting (2 hours)
2. Optimize user listing query (1 hour)

My recommendation: Approve for merge with P1 items tracked.

Reports: .claude/quality/gates/task-007-gate-20251028.md

Ready for pull request creation.
```

---

### Layer 4: MCP Integration (External Systems)

#### GitHub MCP Server

**Automated Actions:**

1. **Create Pull Request:**
```
After Quinn approves (PASS or CONCERNS):
  ↓
GitHub MCP: Creates PR automatically
  ↓
PR Contents:
  - All code changes
  - Quality gate report as PR description
  - Action items as PR comments
  - Labels: quality-gate-pass / quality-gate-concerns
```

**Example PR Description (Auto-generated):**
```markdown
## User Authentication Implementation

**Task:** task-007 - User Authentication with Email/Password
**Quality Gate:** ⚠️ CONCERNS (75.5%)

### Summary
Implements user signup with email/password authentication, password hashing,
and email validation. All acceptance criteria met with comprehensive test coverage.

### Quality Assessment
- **Test Coverage:** 94% ✓
- **Security:** Input validation, bcrypt hashing ✓
- **Performance:** N+1 query identified ⚠️
- **Traceability:** All ACs implemented and tested ✓

### Action Items (P1)
- [ ] Add rate limiting to login endpoint (2h)
- [ ] Optimize user listing query (1h)

### Files Changed
- `src/routes/auth/signup.ts` (new)
- `src/services/auth/signup.service.ts` (new)
- `src/validators/auth.validator.ts` (new)
- `prisma/schema.prisma` (modified)
- 4 test files (new)

### Quality Reports
- [Quality Gate Report](/.claude/quality/gates/task-007-gate-20251028.md)
- [Risk Assessment](/.claude/quality/assessments/task-007-risk-20251028.md)
- [NFR Assessment](/.claude/quality/assessments/task-007-nfr-20251028.md)

---

🤖 Generated with BMAD Enhanced
Reviewed by: Quinn (Quality Advisor)
```

2. **Auto-merge (if configured):**
```yaml
autoMergeRules:
  - condition: qualityGate == "PASS"
    action: merge
    requireApprovals: 1

  - condition: qualityGate == "CONCERNS" AND actionItems.p0.count == 0
    action: merge
    requireApprovals: 1
    createFollowupIssues: true

  - condition: qualityGate == "FAIL"
    action: block
    requireReview: true
```

3. **Create Follow-up Issues:**
```
For each P1/P2 action item from quality gate:
  ↓
GitHub MCP: Creates issue automatically
  ↓
Issue Contents:
  - Title: "[Technical Debt] Add rate limiting to login endpoint"
  - Labels: technical-debt, security, p1
  - Milestone: Next Sprint
  - Linked to original PR
  - Estimated effort from quality report
```

---

### Layer 5: Complete Workflow Example

**User Story:**
```
As a user, I want to sign up with email and password
so that I can create an account.

Acceptance Criteria:
- User can enter email and password
- Password must be at least 8 characters
- Email validation required
- Duplicate emails rejected
```

**Execution:**

```bash
# User kicks off workflow
@orchestrator *build "User signup with email/password"
```

**Step-by-Step Execution:**

```
[00:00] Orchestrator: Request received, routing to Alex for planning...

[00:01] Alex: Creating detailed task specification...
        [Executing create-task-spec.md]
        ✓ Task spec created: task-007-user-signup.md
        ✓ 4 acceptance criteria defined
        ✓ Architecture context embedded
        ✓ Estimated effort: 4-6 hours

        Handing off to James for implementation...

[00:04] James: Implementing task-007...
        [Executing execute-task.md]

        Step 1/5: Database Schema
        ✓ Created Prisma model for User

        Step 2/5: Validation
        ✓ Created Zod schemas for email/password
        ✓ Implemented validation middleware

        Step 3/5: Signup Endpoint
        ✓ Created POST /api/auth/signup route
        ✓ Implemented signup service (bcrypt hashing)
        ✓ Added duplicate email check

        Step 4/5: Tests
        ✓ Unit tests: 12 tests
        ✓ Integration tests: 3 tests
        ✓ Coverage: 94%

        Step 5/5: Validation
        ✓ All tests passing
        ✓ Linting passed

        Implementation complete. Handing off to Quinn...

[00:15] Quinn: Performing quality review...
        [Executing review-task.md orchestrator]

        [00:16] Risk Assessment...
        ✓ 12 risks identified, 3 high-risk
        ✓ Mitigation strategies developed

        [00:18] Test Design Review...
        ✓ 15 tests designed (8 P0, 5 P1, 2 P2)
        ✓ Coverage strategy validated

        [00:21] Requirements Traceability...
        ✓ All 4 ACs implemented and tested
        ✓ Traceability score: 87.5%

        [00:24] NFR Assessment...
        ✓ Security: 95% (excellent)
        ⚠️ Performance: 80% (N+1 query found)
        ✓ Reliability: 90%
        ✓ Maintainability: 85%

        [00:27] Quality Gate Decision...
        ⚠️ CONCERNS (75.5%)

        Quality Review Complete:
        - Can proceed with merge
        - 2 P1 action items identified
        - Reports generated

        Ready for pull request creation.

[00:28] Orchestrator: Quality gate approved (CONCERNS), creating PR...
        [Using GitHub MCP]

        ✓ Branch created: feature/task-007-user-signup
        ✓ Files pushed to branch
        ✓ Pull request created: #42
        ✓ Quality reports attached
        ✓ Action items added as comments
        ✓ Labels applied: quality-gate-concerns, ready-for-review

        PR URL: https://github.com/user/repo/pull/42

        Workflow complete! 🎉

[00:30] User: Review PR #42, approve, merge

        [GitHub MCP auto-creates follow-up issues for P1 items]

        ✓ Issue #43: Add rate limiting
        ✓ Issue #44: Optimize user listing query
```

**Total Time:** 30 minutes (vs 4-6 hours manual)
**Quality:** Higher (comprehensive automated review)
**Documentation:** Complete (all reports generated)

---

## Implementation Roadmap

### Phase 1: Foundation (Complete ✅)
- [x] Skills architecture (planning, implementation, quality)
- [x] Quality skills complete (5 skills + orchestrator)
- [x] Quinn subagent defined
- [x] Templates and configuration

### Phase 2: Core Subagents (Next - 8-10 hours)

**2A. Build Alex (Planner)** - 2 hours
- [ ] Create `.claude/subagents/alex-planner.md`
- [ ] Define persona and communication style
- [ ] Map commands to skills:
  - `*plan` → `create-task-spec.md`
  - `*refine` → `refine-requirements.md` (new skill)
  - `*estimate` → `estimate-effort.md` (new skill)
- [ ] Define handoff protocols (Alex → James)

**2B. Build James (Developer)** - 2 hours
- [ ] Create `.claude/subagents/james-developer.md`
- [ ] Define persona and communication style
- [ ] Map commands to skills:
  - `*implement` → `execute-task.md`
  - `*refactor` → `refactor-code.md` (new skill)
  - `*debug` → `debug-issue.md` (new skill)
  - `*test` → Integrated in execute-task.md
- [ ] Define handoff protocols (James → Quinn)

**2C. Build Orchestrator** - 4-6 hours
- [ ] Create `.claude/subagents/orchestrator.md`
- [ ] Define workflow routing logic
- [ ] Implement state management
- [ ] Create handoff protocols
- [ ] Build command parser: `@orchestrator *build "<feature>"`
- [ ] Define auto-routing rules

### Phase 3: Integration (8-12 hours)

**3A. Command Routing System** - 4-6 hours
- [ ] Research Claude Code's native subagent system
- [ ] Implement `@subagent *command args` routing
- [ ] Build command parser and validator
- [ ] Error handling and fallback
- [ ] Test with all subagents

**3B. GitHub MCP Integration** - 3-4 hours
- [ ] PR creation from quality gate
- [ ] Auto-populate PR description with reports
- [ ] Action items as PR comments
- [ ] Follow-up issue creation (P1/P2 items)
- [ ] Auto-merge rules (optional)

**3C. Workflow State Management** - 2-3 hours
- [ ] Track current phase and subagent
- [ ] Maintain handoff history
- [ ] Enable resume/restart
- [ ] Progress reporting

### Phase 4: Testing & Refinement (4-6 hours)

**4A. Create Working Examples** - 3-4 hours
- [ ] Example 1: User authentication (complete workflow)
- [ ] Example 2: Payment integration (complex feature)
- [ ] Example 3: Bug fix workflow
- [ ] Document each example end-to-end

**4B. Refinement** - 2-3 hours
- [ ] Fix issues found in examples
- [ ] Improve error messages
- [ ] Enhance handoff clarity
- [ ] Optimize skill execution time

### Phase 5: Production Ready (4-6 hours)

**5A. Documentation** - 2-3 hours
- [ ] User guide (how to use the system)
- [ ] Command reference (all subagents and commands)
- [ ] Workflow patterns (common scenarios)
- [ ] Troubleshooting guide

**5B. Configuration & Customization** - 2-3 hours
- [ ] Project-specific configuration
- [ ] Custom quality thresholds
- [ ] Auto-merge rules customization
- [ ] MCP server configuration

---

## Total Effort Estimate

| Phase | Tasks | Effort | Priority |
|-------|-------|--------|----------|
| Phase 1 | Foundation | COMPLETE ✅ | - |
| Phase 2 | Core Subagents | 8-10 hours | CRITICAL |
| Phase 3 | Integration | 8-12 hours | CRITICAL |
| Phase 4 | Testing | 4-6 hours | HIGH |
| Phase 5 | Production | 4-6 hours | MEDIUM |
| **Total** | **All Phases** | **24-34 hours** | - |

**To MVP (Phases 2-3):** 16-22 hours
**To Production (All):** 24-34 hours

---

## Success Metrics

### MVP Success (End of Phase 3)
- [ ] User can trigger workflow with single command
- [ ] Alex creates task spec automatically
- [ ] James implements feature automatically
- [ ] Quinn reviews quality automatically
- [ ] GitHub PR created automatically with reports
- [ ] Complete workflow executes in < 1 hour
- [ ] Quality gate catches real issues

### Production Success (End of Phase 5)
- [ ] 10+ features delivered through automated workflow
- [ ] Time savings: 3-5x faster than manual
- [ ] Quality improvement: Fewer bugs in production
- [ ] User satisfaction: Developers prefer automated flow
- [ ] Documentation complete and accessible

---

## Key Design Decisions

### 1. Orchestrator vs Direct Handoffs

**Decision:** Use Orchestrator pattern (like BMAD's System Manager)

**Rationale:**
- Single entry point: `@orchestrator *build "<feature>"`
- Centralized workflow logic (easier to modify)
- State management in one place
- Can support complex workflows (conditionals, loops, parallel)
- User doesn't need to know which subagent to invoke

**Alternative:** Direct handoffs (Alex → James → Quinn)
- More explicit, less "magic"
- But requires user to know workflow
- Harder to manage complex flows

### 2. Command Routing Approach

**Decision:** Hybrid - Orchestrator routes, but subagents can be invoked directly

**Examples:**
```bash
# Full workflow (automated routing)
@orchestrator *build "user authentication"

# Specific subagent (manual routing)
@alex *plan "user authentication"
@james *implement task-007
@quinn *review task-007
```

**Rationale:**
- Flexibility: Users choose automation level
- Debugging: Can manually invoke steps
- Override: Can skip phases if needed

### 3. Quality Gate Auto-Merge

**Decision:** PASS = auto-merge, CONCERNS = require approval, FAIL = block

**Configuration:**
```yaml
autoMerge:
  enabled: true
  rules:
    - qualityGate: PASS
      action: merge_after_approval
      requiredApprovals: 1

    - qualityGate: CONCERNS
      action: require_review
      requiredApprovals: 1
      createFollowupIssues: true

    - qualityGate: FAIL
      action: block
      message: "Fix critical issues before merging"
```

**Rationale:**
- PASS: Safe to merge (but still require human approval)
- CONCERNS: Can merge but issues tracked
- FAIL: Should not merge (blocking critical issues)

### 4. MCP Server Usage

**Decision:** GitHub MCP for PR/issue automation, extensible for more

**Integrations:**
- **GitHub MCP:** PR creation, issue tracking, merge automation
- **Slack MCP (future):** Notifications, approvals
- **Linear MCP (future):** Issue sync, project management
- **Vercel MCP (future):** Deployment automation

---

## Open Questions & Next Steps

### Critical Questions to Resolve

1. **How does Claude Code's subagent system actually work?**
   - Can we use `@subagent` syntax natively?
   - Or do we need custom routing?
   - What's the integration pattern?

2. **State persistence across turns?**
   - How does Orchestrator maintain state between subagent invocations?
   - Is there session storage?
   - Or do we use files (workflow-state.yaml)?

3. **Error handling strategy?**
   - What if James's implementation fails?
   - Can we rollback or retry?
   - How do we communicate errors to user?

### Recommended Next Session

**Option A: Build Orchestrator First** (Recommended)
- Critical for automated workflow
- Unblocks all other work
- Can test routing logic immediately
- **Effort:** 4-6 hours

**Option B: Build Alex + James First**
- Enables full workflow (manually triggered)
- Proves subagent handoffs work
- Can test without orchestrator
- **Effort:** 4 hours

**Option C: Research Claude Code Integration**
- Understand native capabilities first
- Avoid building what's already provided
- Design better integration
- **Effort:** 1-2 hours

---

## Conclusion

The vision is clear: **High-level requirements → Automated workflow → Production-ready code**

**Architecture is sound:**
- Skills = Reusable executable logic ✅
- Subagents = Specialized personas with routing ✅
- Orchestrator = Workflow coordinator (to build)
- MCP Integration = External system automation (to build)

**Next Critical Steps:**
1. Build Orchestrator (workflow automation)
2. Build Alex + James (complete subagent set)
3. Implement command routing
4. Integrate GitHub MCP
5. Create working examples

**Estimated Time to MVP:** 16-22 hours
**Estimated Value:** 10x faster delivery with higher quality

**Ready to start building the Orchestrator?**
