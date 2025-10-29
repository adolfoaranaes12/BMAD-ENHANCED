# BMAD Enhanced for Claude Code

**Version:** 1.0 (Phase 1 - Foundation)
**Inspired by:** BMAD-METHOD v4 architecture patterns
**For:** Claude Code with subagents and skills

---

## Overview

BMAD Enhanced brings the proven patterns from BMAD-METHOD to Claude Code, creating a structured workflow that eliminates context loss and ensures systematic quality.

**Key Innovations:**

1. **Context-Rich Task Specifications**: All context embedded in task files, no mid-implementation searching
2. **Sequential Execution**: Validated checkpoints at each step
3. **Systematic Quality Assessment**: Structured reviews with advisory gates
4. **Clear Role Boundaries**: Planning → Implementation → Review phases

**Problem Solved:** AI agents lose context and make inconsistent decisions

**Solution:** Embed complete context in task specs, execute sequentially with validation, assess quality systematically

---

## Quick Start

### 1. Understand the Workflow

```
┌─────────────────┐
│  Planning Phase │  Create hyper-detailed task specification
│   (Skill 1)     │  - Embed all architectural context
└────────┬────────┘  - Map to requirements
         │           - Create sequential tasks
         ↓
┌─────────────────┐
│Implementation   │  Execute task specification
│   (Skill 2)     │  - Read ONLY task spec (no architecture lookup)
└────────┬────────┘  - Execute tasks sequentially with validation
         │           - Update implementation record
         ↓
┌─────────────────┐
│  Review Phase   │  Assess quality systematically
│   (Skill 3)     │  - Requirements traceability
└─────────────────┘  - Test coverage analysis
                     - NFR validation
                     - Advisory quality gate
```

### 2. Configure Your Project

Edit `.claude/config.yaml`:

```yaml
project:
  name: Your Project Name
  type: greenfield  # or brownfield

documentation:
  architecture: docs/architecture.md  # Your architecture doc
  standards: docs/standards.md        # Your coding standards

development:
  alwaysLoadFiles:
    - docs/standards.md  # Files implementation always loads
```

### 3. Create Your First Task

**Step 1: Use Planning Skill**

Ask Claude Code to use the planning skill:

```
Use the planning skill at .claude/skills/planning/create-task-spec.md
to create a task specification for user authentication.
```

The skill will:
- Ask for requirements and acceptance criteria
- Load architecture and standards
- Extract relevant technical context
- Create hyper-detailed task specification
- Save to `.claude/tasks/task-001-{feature}.md`

**Step 2: Review and Approve**

Review the generated task spec. If approved, update status from "Draft" to "Approved".

**Step 3: Use Implementation Skill**

Ask Claude Code to execute the task:

```
Use the implementation skill at .claude/skills/implementation/execute-task.md
to execute .claude/tasks/task-001-{feature}.md
```

The skill will:
- Read task spec (all context embedded)
- Execute tasks sequentially
- Write tests and validate at each step
- Update implementation record
- Mark status as "Review" when complete

**Step 4: Use Quality Skill (Optional but Recommended)**

Ask Claude Code to review:

```
Use the quality skill at .claude/skills/quality/review-task.md
to review .claude/tasks/task-001-{feature}.md
```

The skill will:
- Map requirements to tests
- Analyze test coverage
- Validate NFRs (security, performance, reliability, maintainability)
- Create quality gate with decision (PASS/CONCERNS/FAIL)
- Provide actionable recommendations

**Step 5: Mark Done and Commit**

If quality gate acceptable:
- Update task status to "Done"
- Commit your changes
- Move to next task

---

## Directory Structure

```
.claude/
├── config.yaml                    # Project configuration
├── skills/
│   ├── planning/
│   │   └── create-task-spec.md   # Planning skill (context embedding)
│   ├── implementation/
│   │   └── execute-task.md       # Implementation skill (sequential execution)
│   └── quality/
│       └── review-task.md        # Quality skill (systematic assessment)
├── templates/
│   ├── task-spec.md              # Task specification template
│   └── quality-gate.yaml         # Quality gate template
├── tasks/                         # Generated task specifications
├── quality/
│   └── gates/                    # Quality gate decisions
└── docs/                          # Additional documentation
```

---

## Skills Reference

### Planning Skill

**Purpose:** Create hyper-detailed task specifications with embedded context

**Location:** `.claude/skills/planning/create-task-spec.md`

**What it does:**
1. Gathers requirements from user
2. Loads architecture and standards documentation
3. Extracts specific technical details with source references
4. Creates sequential task breakdown
5. Generates complete task specification

**Key Pattern (BMAD-inspired):**
- Embeds ALL context in task spec
- Implementation never needs to load architecture docs
- Every technical detail includes [Source: filename#section]
- Previous task learnings incorporated

**Output:** `.claude/tasks/task-{id}-{slug}.md` with status "Draft"

### Implementation Skill

**Purpose:** Execute task specifications sequentially with validation

**Location:** `.claude/skills/implementation/execute-task.md`

**What it does:**
1. Loads task spec and always-load files (standards)
2. Executes tasks sequentially (no skipping)
3. Writes tests before marking tasks complete
4. Runs validations after each task
5. Updates implementation record only

**Key Pattern (BMAD-inspired):**
- Reads ONLY task spec for context (no architecture lookup)
- Sequential execution with validation gates
- Halts on ambiguity or repeated failures
- Limited file permissions (Implementation Record only)

**Output:** Completed implementation with status "Review"

### Quality Review Skill

**Purpose:** Systematic quality assessment with advisory gates

**Location:** `.claude/skills/quality/review-task.md`

**What it does:**
1. Requirements traceability (AC → Implementation → Tests)
2. Test coverage analysis (unit/integration/E2E)
3. NFR assessment (Security, Performance, Reliability, Maintainability)
4. Code quality review
5. Quality gate decision (PASS/CONCERNS/FAIL/WAIVED)

**Key Pattern (BMAD-inspired):**
- Evidence-based assessment
- Advisory authority (not blocking)
- Actionable recommendations
- WAIVED option with rationale

**Output:** Quality gate file + Task file Quality Review section updated

---

## Configuration Reference

### Project Settings

```yaml
project:
  name: string           # Your project name
  type: greenfield | brownfield
  description: string    # Optional project description
```

### Documentation Paths

```yaml
documentation:
  architecture: path     # Main architecture document
  standards: path        # Coding standards document
  patterns: path         # Design patterns document
  custom_docs: []        # Additional docs (optional)
```

### Development Settings

```yaml
development:
  alwaysLoadFiles: []    # Files implementation skill always loads
                         # Keep minimal! Only essential standards
  taskLocation: path     # Where task specs are stored
  debugLog: path         # Debug log location
```

### Quality Settings

```yaml
quality:
  qualityLocation: path          # Quality assessment outputs
  gateThreshold: PASS | CONCERNS | FAIL  # Minimum acceptable
  requireReview: boolean         # Require review before done
  riskScoreThreshold: 1-9        # Risk score for auto-concerns
  checks:
    requirementsTraceability: boolean
    testCoverage: boolean
    nfrValidation: boolean
    riskAssessment: boolean
```

### Workflow Settings

```yaml
workflow:
  phases:
    planning: boolean            # Enable planning phase
    implementation: boolean      # Enable implementation phase
    review: boolean             # Enable review phase
  haltOn:
    consecutiveFailures: number  # Stop after N failures
    ambiguousRequirements: boolean
    missingDependencies: boolean
    regressionFailures: boolean
```

### Skill Behavior

```yaml
skills:
  planning:
    embedFullContext: boolean           # Embed all context
    includeSourceReferences: boolean    # Add [Source: ...] refs
    includePreviousLearnings: boolean   # Learn from previous tasks
    minTasksPerSpec: number            # Min task breakdown
    maxTasksPerSpec: number            # Max task breakdown

  implementation:
    sequentialOnly: boolean             # Enforce sequential execution
    validateBeforeCheckbox: boolean     # Validate before marking done
    updateOnlyRecordSection: boolean    # Limited file permissions
    requireTestsPerTask: boolean        # Tests required
    runAllTestsAtEnd: boolean          # Final validation

  review:
    performRiskProfiling: boolean       # Risk assessment
    performTestDesign: boolean          # Test design validation
    performTraceability: boolean        # AC → Code → Tests
    performNFRAssessment: boolean       # NFR validation
    autoFailOnCriticalRisk: boolean     # Risk ≥9 → FAIL
    autoConcernsOnHighRisk: boolean     # Risk ≥6 → CONCERNS
```

---

## Task Specification Format

### Basic Structure

```markdown
# Task: [Title]

## Metadata
- Task ID, created date, priority, epic/feature

## Status
Draft | Approved | InProgress | Review | Done

## Objective
As a [role], I want [action], so that [benefit]

## Acceptance Criteria
1-5 specific, testable criteria

## Context (Embedded from Architecture)
### Previous Task Insights
### Data Models [with source refs]
### API Specifications [with source refs]
### Component Specifications [with source refs]
### File Locations [exact paths]
### Testing Requirements [test strategy]
### Technical Constraints [security, performance]

## Tasks / Subtasks
- [ ] Task 1 (AC: 1, 2)
  - [ ] Subtask 1.1
  - [ ] Write tests
  - [ ] Validate

## Implementation Record
[Populated by implementation skill]

## Quality Review
[Populated by quality skill]
```

### Key Principles

1. **Context Embedding:** All technical details in Context section
2. **Source References:** Every claim has [Source: filename#section]
3. **Sequential Tasks:** 3-15 tasks in implementation order
4. **Validation Checkpoints:** After each task
5. **Limited Permissions:** Skills only update their sections

---

## Quality Gates

### Gate Statuses

**PASS:** All criteria met
- All ACs have adequate test coverage
- No critical issues in any category
- Standards compliance acceptable
- Ready to merge

**CONCERNS:** Non-critical issues
- Some test coverage gaps (P1/P2 level)
- Non-critical performance/security concerns
- Minor technical debt
- Can merge with follow-up work tracked

**FAIL:** Critical issues
- Critical security vulnerabilities
- Missing P0 test coverage
- ACs not fully implemented
- Major reliability concerns
- Must address before merge

**WAIVED:** Issues accepted
- Requires: reason, approver, expiry date
- Documents accepted risks
- Team decision to proceed

### Decision Rules

Configured in `.claude/config.yaml`:

```yaml
quality:
  riskScoreThreshold: 6  # Risk = Probability × Impact (1-9 scale)

  # Auto-apply rules:
  # - Risk ≥9 → FAIL
  # - Risk ≥6 → CONCERNS
  # - Critical security → FAIL
  # - Missing P0 tests → CONCERNS
  # - Performance issues → CONCERNS
```

### Quality Gate File

Location: `.claude/quality/gates/{task-id}-gate.yaml`

Contains:
- Requirements traceability matrix
- Test coverage analysis
- NFR assessment (Security, Performance, Reliability, Maintainability)
- Code quality findings
- Action items by priority
- Recommendations by timeline
- Gate decision with rationale

---

## Best Practices

### Planning Phase

1. **Be Specific:**
   - Don't: "Create user model"
   - Do: "Create User interface with id (UUID), email (string, unique), password (bcrypt) in src/types/user.ts [Source: docs/architecture/data-models.md#user]"

2. **Source Everything:**
   - Every technical detail needs [Source: ...]
   - If no source, note "No guidance in architecture docs"
   - Never invent technical details

3. **Learn from Previous:**
   - Read most recent task completion notes
   - Reuse established patterns
   - Avoid repeating mistakes

4. **Validation Checkpoints:**
   - Every task needs validation step
   - Every task needs tests written
   - Final validation checks all ACs

### Implementation Phase

1. **Trust the Task Spec:**
   - Context already embedded, don't search
   - Follow spec exactly as written
   - Halt if requirements unclear

2. **Sequential Execution:**
   - Complete current before next
   - Don't skip ahead
   - Validate before checking off

3. **Test Before Checking:**
   - Write tests before marking done
   - Run tests before next task
   - Ensure all pass

4. **Document As You Go:**
   - Update completion notes after each task
   - Record deviations and decisions
   - Note patterns for future

### Review Phase

1. **Be Evidence-Based:**
   - Every finding backed by evidence
   - Cite file locations and lines
   - Show measurements and metrics

2. **Be Fair and Balanced:**
   - Note strengths and weaknesses
   - Distinguish critical from nice-to-have
   - Provide clear rationale

3. **Be Actionable:**
   - Specific recommendations
   - Prioritized action items
   - Estimated effort when possible

4. **Be Advisory:**
   - Gates are guidance, not blocks
   - WAIVED option available
   - Teams choose quality bar

---

## Common Pitfalls

### Planning Phase

❌ **Inventing Technical Details**
- Don't assume database schema if not in docs
- Do note "No user schema found" and ask user

❌ **Generic Context**
- Don't: "Follow REST best practices"
- Do: "POST /api/auth/signup returns 201 with user object and JWT [Source: docs/architecture/rest-api-spec.md#auth]"

❌ **Missing Source References**
- Don't: "Password must be hashed with bcrypt"
- Do: "Password must be hashed with bcrypt, cost 12 [Source: docs/standards.md#security]"

### Implementation Phase

❌ **Loading Architecture Docs**
- Don't read docs/architecture/* during implementation
- Do use context already embedded in task spec

❌ **Skipping Validations**
- Don't mark task complete without running tests
- Do validate after each task, run full suite at end

❌ **Editing Wrong Sections**
- Don't modify acceptance criteria or context
- Do only update Implementation Record and checkboxes

### Review Phase

❌ **Being Too Strict**
- Don't fail for minor style issues
- Do distinguish critical from minor concerns

❌ **Missing Evidence**
- Don't: "Tests seem insufficient"
- Do: "Missing tests for error handling in signup.service.ts:42-67"

❌ **Vague Recommendations**
- Don't: "Improve performance"
- Do: "Add eager loading in list.service.ts:45 to eliminate N+1 query (2 hours)"

---

## Examples

### Example 1: Simple CRUD Feature

**Task:** User signup functionality

**Planning Phase Output:**
- 5 tasks (create model, service, endpoint, tests, docs)
- All data models embedded with validation rules
- API spec embedded with request/response formats
- File paths specified exactly
- Testing strategy embedded (unit/integration/E2E)
- Previous auth patterns referenced

**Implementation Phase:**
- Executes 5 tasks sequentially
- Writes 19 tests (15 unit, 4 integration, 2 E2E)
- All tests pass before marking complete
- Updates implementation record with learnings

**Review Phase:**
- Requirements traceability: 4/4 ACs fully covered
- Test coverage: 94% (exceeds 80% target)
- Security: PASS (validation, hashing, no vulnerabilities)
- Performance: CONCERNS (N+1 query identified)
- Gate: CONCERNS (can merge, track performance fix)

### Example 2: Complex Integration

**Task:** Payment processing integration

**Planning Phase Output:**
- 8 tasks (external API, webhooks, retry logic, security, testing)
- API integration details embedded with auth requirements
- Error handling patterns embedded
- Security constraints embedded (PCI compliance)
- Testing strategy includes mocking external service

**Implementation Phase:**
- Executes 8 tasks sequentially
- Halts at task 4 due to missing API credentials
- User provides credentials
- Resumes and completes
- 27 tests written with comprehensive mocking

**Review Phase:**
- Requirements traceability: 6/6 ACs covered
- Test coverage: 91%
- Security: PASS (PCI compliant, credentials encrypted)
- Performance: PASS (retry logic with backoff)
- Reliability: PASS (comprehensive error handling)
- Gate: PASS (ready to merge)

---

## Troubleshooting

### Planning Skill Issues

**Problem:** "Context insufficient for implementation"
- **Solution:** Add more details to architecture docs, re-run planning

**Problem:** "Too many tasks generated (>15)"
- **Solution:** Task too complex, split into multiple task specs

**Problem:** "Cannot find source for technical detail"
- **Solution:** Add to architecture docs or note "No guidance found"

### Implementation Skill Issues

**Problem:** "Halting on ambiguous requirements"
- **Solution:** Task spec needs more detail, update and re-approve

**Problem:** "Tests failing repeatedly"
- **Solution:** Review completion notes, may need planning input

**Problem:** "Cannot find files mentioned in task spec"
- **Solution:** File paths incorrect in task spec, update paths

### Review Skill Issues

**Problem:** "Cannot map AC to implementation"
- **Solution:** Implementation may not fully meet AC, needs fixes

**Problem:** "Quality gate too strict"
- **Solution:** Adjust `gateThreshold` in config or use WAIVED

**Problem:** "Review taking too long"
- **Solution:** Disable optional checks in config for faster reviews

---

## Phase 1 Limitations

Current implementation includes:
- ✅ Configuration system
- ✅ Planning skill (context embedding)
- ✅ Implementation skill (sequential execution)
- ✅ Quality skill (systematic assessment)
- ✅ Task specification template
- ✅ Quality gate template

Not yet implemented (future phases):
- ⏳ Subagent orchestration (Phase 2)
- ⏳ Risk profiling skill (Phase 3)
- ⏳ Test design skill (Phase 3)
- ⏳ Requirements traceability skill (Phase 3)
- ⏳ NFR assessment skill (Phase 3)
- ⏳ Expansion pack system (Phase 4)

---

## Next Steps

1. **Configure your project:** Edit `.claude/config.yaml`
2. **Create architecture docs:** Document your system design
3. **Try first task:** Use planning skill to create task spec
4. **Execute and review:** Use implementation and quality skills
5. **Iterate and improve:** Learn from completion notes
6. **Provide feedback:** Help us improve BMAD Enhanced!

---

## Resources

- **Migration Plan:** `docs/migration-plan.md` - Complete roadmap
- **BMAD Analysis:** `docs/bmad-analysis.md` - Architecture insights
- **Configuration:** `.claude/config.yaml` - Project settings
- **Skills:** `.claude/skills/` - All available skills
- **Templates:** `.claude/templates/` - Document templates

---

## Version History

| Version | Date | Phase | Description |
|---------|------|-------|-------------|
| 1.0 | 2025-10-28 | Phase 1 | Foundation: Config, planning, implementation, quality skills |

---

## Credits

**Inspired by:** [BMAD-METHOD v4](https://github.com/bmad-code-org/BMAD-METHOD)

**Key Patterns Adopted:**
- Context embedding (SM agent story creation)
- Sequential execution with validation (Dev agent)
- Systematic quality assessment (QA agent)
- Advisory quality gates (PO validation)

**Created for:** Claude Code with subagents and skills support

---

**Ready to eliminate context loss and build with confidence!**
