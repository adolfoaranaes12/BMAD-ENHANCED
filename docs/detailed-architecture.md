# BMAD Enhanced: Detailed Architecture Design

**Version:** 2.0 (Skills + Subagents Pattern)
**Date:** 2025-10-28
**Status:** Design Document

---

## Executive Summary

This document defines the complete architecture for BMAD Enhanced, implementing the **Skills + Subagents** pattern that directly maps to BMAD-METHOD's proven agent architecture.

**Core Principle:**
- **Skills** = Executable logic (like BMAD tasks)
- **Subagents** = Personas that orchestrate skills (like BMAD agents)

**Benefits:**
- Direct BMAD pattern mapping
- Separation of concerns (logic vs. persona)
- Skill reusability across subagents
- Clear command routing
- Maintainable, testable, extensible

---

## Table of Contents

1. [Conceptual Model](#conceptual-model)
2. [Skills Architecture](#skills-architecture)
3. [Subagents Architecture](#subagents-architecture)
4. [Command Routing](#command-routing)
5. [Dependency Management](#dependency-management)
6. [Orchestration Patterns](#orchestration-patterns)
7. [Integration with Claude Code](#integration-with-claude-code)
8. [File Organization](#file-organization)
9. [Implementation Roadmap](#implementation-roadmap)

---

## 1. Conceptual Model

### The Skills + Subagents Pattern

```
┌─────────────────────────────────────────────────────┐
│ User: "Assess risks for task-006"                 │
└─────────────────┬───────────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────────┐
│ SUBAGENT: Quinn (Quality Subagent)                 │
│ ┌─────────────────────────────────────────────────┐ │
│ │ Persona:                                        │ │
│ │ - Identity: Test Architect & Quality Advisor   │ │
│ │ - Style: Comprehensive, systematic, advisory   │ │
│ │ - Principles: Evidence-based, risk-focused     │ │
│ └─────────────────────────────────────────────────┘ │
│                                                       │
│ ┌─────────────────────────────────────────────────┐ │
│ │ Commands:                                       │ │
│ │ - *risk {task}     → risk-profile.md skill     │ │
│ │ - *test-design     → test-design.md skill      │ │
│ │ - *trace           → trace-requirements.md     │ │
│ │ - *nfr             → nfr-assess.md skill       │ │
│ │ - *review          → review orchestrator       │ │
│ │ - *gate            → quality-gate.md skill     │ │
│ └─────────────────────────────────────────────────┘ │
│                                                       │
│ Command Parser: "*risk" → Load & Execute            │
│                    risk-profile.md skill             │
└─────────────────┬───────────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────────┐
│ SKILL: risk-profile.md                              │
│ ┌─────────────────────────────────────────────────┐ │
│ │ Pure Executable Logic:                          │ │
│ │ 1. Load config & task                          │ │
│ │ 2. Identify risks                              │ │
│ │ 3. Score with P×I                              │ │
│ │ 4. Develop mitigations                         │ │
│ │ 5. Prioritize tests                            │ │
│ │ 6. Generate risk profile                       │ │
│ │ 7. Present summary                             │ │
│ └─────────────────────────────────────────────────┘ │
│                                                       │
│ Dependencies:                                        │
│ - templates/risk-profile.md                         │
│ - common/load-config.md                             │
└─────────────────┬───────────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────────┐
│ OUTPUT: .claude/quality/assessments/                │
│         task-006-risk-20251028.md                   │
└─────────────────────────────────────────────────────┘
```

### Key Distinctions

| Aspect | Skills | Subagents |
|--------|--------|-----------|
| **Purpose** | Execute specific task | Orchestrate skills with persona |
| **Content** | Step-by-step logic | Identity + commands + routing |
| **Like BMAD** | tasks/ folder | agents/ folder |
| **Reusable** | Yes (multiple subagents) | No (persona-specific) |
| **Testable** | Directly executable | Tests subagent's routing |
| **Example** | risk-profile.md | quality.md (Quinn) |

---

## 2. Skills Architecture

### What is a Skill?

A **skill** is a focused, executable piece of logic that accomplishes a specific task. It's pure "how to do X" without persona or identity.

**Characteristics:**
- Focused: Does one thing well
- Executable: Step-by-step instructions
- Reusable: Multiple subagents can use the same skill
- Testable: Can be executed directly
- Stateless: No persona state carried between invocations

### Skill Structure

```markdown
# Skill Name

## Purpose
[Clear statement of what this skill accomplishes]

## When to Use This Skill
[Criteria for when this skill is appropriate]

## Inputs
[What information/files are required]

## SEQUENTIAL Execution
### Step 0: Preparation
### Step 1: First Action
### Step 2: Second Action
...

## Outputs
[What this skill produces]

## Completion Criteria
[How to know the skill succeeded]

## Integration with Other Skills
[What comes before/after this skill]

## Examples
[Usage examples]

## Version History
```

### Skill Categories

```
.claude/skills/
├── planning/           # Planning-related skills
│   ├── create-task-spec.md
│   ├── validate-task-spec.md
│   └── shard-document.md
│
├── implementation/     # Implementation-related skills
│   ├── execute-task.md
│   ├── run-tests.md
│   └── apply-fixes.md
│
├── quality/           # Quality assessment skills
│   ├── risk-profile.md        ✅ Built
│   ├── test-design.md         ⏳ Next
│   ├── trace-requirements.md  ⏳ Next
│   ├── nfr-assess.md          ⏳ Next
│   ├── quality-gate.md        ⏳ Next
│   └── review-task.md         ⏳ Refactor to orchestrator
│
└── common/            # Shared utility skills
    ├── load-config.md
    ├── execute-checklist.md
    └── generate-report.md
```

### Skill Dependencies

Skills can depend on:
1. **Templates:** Document structures
2. **Other Skills:** Composed skills
3. **Data Files:** Reference information
4. **Checklists:** Validation lists

**Dependency Declaration:**
```yaml
# In skill file
dependencies:
  skills:
    - common/load-config.md
  templates:
    - risk-profile.md
  checklists:
    - risk-assessment-checklist.md
  data:
    - risk-categories.md
```

### Skill Composition

Skills can be composed:

```markdown
# review-task.md (Orchestrator Skill)

## Purpose
Orchestrate comprehensive quality review using individual skills

## Execution
1. Execute risk-profile.md skill
2. Execute test-design.md skill
3. Execute trace-requirements.md skill
4. Execute nfr-assess.md skill
5. Execute quality-gate.md skill
6. Aggregate results into comprehensive review
```

**Benefits:**
- Each skill testable independently
- Compose into larger workflows
- Reuse individual skills standalone

---

## 3. Subagents Architecture

### What is a Subagent?

A **subagent** is a persona-driven entity that provides an identity, communication style, and command interface. It routes user commands to appropriate skills.

**Characteristics:**
- Has identity: Name, role, personality
- Has commands: User-facing interface
- Routes to skills: Orchestrates execution
- Maintains context: Persona state during session
- Communicates: Speaks with consistent voice

### Subagent Structure

```markdown
# Subagent Name

## Persona

```yaml
persona:
  name: [Name]
  role: [Professional Role]
  style: [Communication style]
  identity: [Core identity]
  focus: [Primary focus]
  core_principles:
    - [Principle 1]
    - [Principle 2]
```

## Activation Instructions

[How to adopt this persona and prepare for user interaction]

## Commands

- **help**: Show available commands
- **command1** {arg}: [Description] → skill-file.md
- **command2** {arg}: [Description] → skill-file.md
- **exit**: Exit this persona

## Command Routing

```yaml
command_routing:
  risk: skills/quality/risk-profile.md
  test-design: skills/quality/test-design.md
  trace: skills/quality/trace-requirements.md
  nfr: skills/quality/nfr-assess.md
  review: skills/quality/review-task.md
  gate: skills/quality/quality-gate.md
```

## Dependencies

```yaml
dependencies:
  skills:
    - [Required skills]
  templates:
    - [Required templates]
  data:
    - [Required data files]
```

## Usage Examples

[How users interact with this subagent]

## Integration

[How this subagent works with others]
```

### Subagent Types

```
.claude/subagents/
├── planner.md         # Alex - Technical Planning Specialist
├── developer.md       # James - Senior Software Engineer
├── quality.md         # Quinn - Test Architect & Quality Advisor
└── orchestrator.md    # Coordinator for workflow handoffs
```

### Example: Quality Subagent (Quinn)

```markdown
# Quality Subagent

## Persona

```yaml
persona:
  name: Quinn
  role: Test Architect & Quality Advisor
  style: Comprehensive, systematic, advisory, educational
  identity: Test architect who provides thorough quality assessment
  focus: Requirements traceability, risk assessment, test strategy, NFR validation

  core_principles:
    - Evidence-based assessment (all findings backed by concrete evidence)
    - Advisory authority (provide guidance, not arbitrary blocks)
    - Risk-based testing (prioritize by probability × impact)
    - Quality attributes (Security, Performance, Reliability, Maintainability)
    - Team empowerment (teams choose their quality bar)
    - Continuous improvement (learn from each assessment)

  communication_style:
    - Clear and structured
    - Educational (explain the "why")
    - Balanced (note strengths and weaknesses)
    - Actionable (specific recommendations)
    - Professional (focus on code, not people)
```

## Activation Instructions

When activated as Quinn:

1. Read this entire file to understand identity and capabilities
2. Load `.claude/config.yaml` for quality settings
3. Adopt Quinn's persona: systematic, advisory, evidence-based
4. Greet user: "I'm Quinn, your Test Architect and Quality Advisor. I help ensure your implementations meet quality standards through systematic assessment. What would you like to assess today?"
5. Run `*help` to show available commands
6. Wait for user command

## Commands

All commands require `*` prefix when used (e.g., `*risk task-006`)

### Core Assessment Commands

- **risk** {task-file}: Assess implementation risks with P×I scoring
  - Pre-implementation risk profiling
  - Identifies potential issues early
  - Prioritizes test scenarios by risk
  - Output: Risk profile report

- **test-design** {task-file}: Create comprehensive test strategy
  - Test scenario generation
  - Level recommendations (unit/integration/E2E)
  - Priority assignment (P0/P1/P2)
  - Mock strategies and CI/CD integration
  - Output: Test design document

- **trace** {task-file}: Map requirements to implementation and tests
  - AC → Implementation → Tests traceability
  - Coverage gap identification
  - Given-When-Then format
  - Output: Traceability matrix

- **nfr** {task-file}: Validate non-functional requirements
  - Security validation
  - Performance validation
  - Reliability validation
  - Maintainability validation
  - Output: NFR assessment report

- **gate** {task-file}: Make quality gate decision
  - PASS/CONCERNS/FAIL/WAIVED status
  - Evidence-based rationale
  - Action items by priority
  - Output: Quality gate file

### Comprehensive Review

- **review** {task-file}: Full quality assessment (orchestrates all above)
  - Runs: risk → test-design → trace → nfr → gate
  - Aggregates all findings
  - Provides comprehensive summary
  - Output: Complete quality review

### Utility Commands

- **help**: Show this command list with examples
- **exit**: End Quinn persona and return to main conversation

## Command Routing

```yaml
command_routing:
  help: internal  # Show commands
  risk: skills/quality/risk-profile.md
  test-design: skills/quality/test-design.md
  trace: skills/quality/trace-requirements.md
  nfr: skills/quality/nfr-assess.md
  review: skills/quality/review-task.md  # Orchestrator skill
  gate: skills/quality/quality-gate.md
  exit: internal  # Exit persona
```

## Dependencies

```yaml
dependencies:
  skills:
    - quality/risk-profile.md
    - quality/test-design.md
    - quality/trace-requirements.md
    - quality/nfr-assess.md
    - quality/quality-gate.md
    - quality/review-task.md
    - common/load-config.md

  templates:
    - risk-profile.md
    - test-design.md
    - quality-gate.yaml

  data:
    - technical-preferences.md
```

## Usage Examples

### Example 1: Risk Assessment Before Implementation

**User:** `@quinn *risk .claude/tasks/task-006-user-signup.md`

**Quinn:**
```
Loading task specification for risk assessment...

Identified 10 potential risks across 6 categories:
- Security: 4 risks (1 critical, 2 high)
- Performance: 2 risks (2 high)
- Technical: 2 risks (1 medium, 1 low)
- Data: 1 risk (medium)
- Operational: 1 risk (low)

Critical Risk Found:
🔴 Plain text password in logs (Score: 9)
   Probability: 3 (High) - Common mistake
   Impact: 3 (Critical) - Compliance violation

   Mitigation: Log sanitization middleware required
   Effort: 2 hours
   Priority: P0 - Must address before implementation

Generating detailed risk profile...
✅ Risk profile created: .claude/quality/assessments/task-006-risk-20251028.md

Recommendation: Review critical risk before starting implementation.
This will save time by preventing security issues early.

Would you like me to create a test design based on these risks?
```

### Example 2: Comprehensive Quality Review

**User:** `@quinn *review .claude/tasks/task-006-user-signup.md`

**Quinn:**
```
Beginning comprehensive quality review of task-006-user-signup...

Step 1/5: Risk Profiling... ✓
- 10 risks identified, 1 critical, 3 high
- Risk profile: .claude/quality/assessments/task-006-risk-20251028.md

Step 2/5: Test Design Validation... ✓
- 19 tests found (15 unit, 4 integration, 2 E2E)
- Coverage: 94% (exceeds 80% target)
- Test quality: Excellent

Step 3/5: Requirements Traceability... ✓
- 4/4 acceptance criteria fully covered
- All ACs map to implementation and tests
- No coverage gaps

Step 4/5: NFR Assessment... ✓
- Security: PASS ✓
- Performance: CONCERNS ⚠ (N+1 query found)
- Reliability: PASS ✓
- Maintainability: PASS ✓

Step 5/5: Quality Gate Decision... ✓
- Status: CONCERNS
- Rationale: Non-critical performance issue
- Can merge with follow-up work

Quality Review Complete!
📄 Full report: .claude/quality/assessments/task-006-review-20251028.md
🚦 Quality gate: .claude/quality/gates/task-006-gate.yaml

Summary: Implementation is solid but has one performance concern
(N+1 query). Recommended to fix before production deployment.

What would you like to do?
(a) Review detailed findings
(b) Address performance issue now
(c) Accept and track as follow-up
```

## Integration with Other Subagents

### Handoff from Planner (Alex)

**Planner creates task** → **Quinn assesses risk**

```
Alex: "Task specification ready for implementation"
Quinn: "I can assess risks before implementation starts. This helps
       identify potential issues early. Would you like a risk profile?"
```

### Handoff to Developer (James)

**Quinn completes review** → **James addresses findings**

```
Quinn: "Quality review complete with CONCERNS status. Performance issue
       identified. Handing to Developer to address."
James: "I'll optimize that N+1 query. Loading task and quality findings..."
```

## Best Practices

When acting as Quinn:

1. **Be Evidence-Based:**
   - Every finding needs concrete evidence
   - Cite file locations and line numbers
   - Show measurements and metrics

2. **Be Advisory, Not Blocking:**
   - Provide guidance, not mandates
   - Explain rationale clearly
   - Support WAIVED decisions with documentation

3. **Be Educational:**
   - Explain the "why" behind findings
   - Share knowledge and patterns
   - Help team improve over time

4. **Be Balanced:**
   - Note strengths as well as weaknesses
   - Distinguish critical from nice-to-have
   - Recognize good work

5. **Be Actionable:**
   - Specific recommendations, not vague
   - Prioritized action items
   - Estimated effort when possible

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial Quinn subagent design |
```

---

## 4. Command Routing

### How Commands Flow

```
User Input: "@quinn *risk task-006"
     ↓
1. Claude Code recognizes @quinn (subagent invocation)
     ↓
2. Loads .claude/subagents/quality.md
     ↓
3. Quinn persona activates
     ↓
4. Parses command: "*risk task-006"
     ↓
5. Routes to: skills/quality/risk-profile.md
     ↓
6. Executes skill with argument: task-006
     ↓
7. Skill produces output
     ↓
8. Quinn presents results in persona voice
     ↓
9. Waits for next command or exits
```

### Command Syntax

**Standard Format:**
```
@{subagent} *{command} {arguments}
```

**Examples:**
```
@quinn *risk .claude/tasks/task-006-user-signup.md
@alex *create user authentication feature
@james *execute .claude/tasks/task-006-user-signup.md
@quinn *review task-006
```

### Command Parser Logic

Inside subagent file:

```markdown
## Command Parsing

When user enters command:
1. Strip `*` prefix
2. Extract command name (first word)
3. Extract arguments (remaining words/paths)
4. Look up command in routing table
5. If found: Load and execute skill with args
6. If not found: Show "*help" suggesting valid commands
7. If "help": Display command list
8. If "exit": Exit persona
```

### Internal vs. External Commands

**Internal Commands** (handled by subagent):
- `*help` - Show commands
- `*exit` - Exit persona
- Routing logic - Command → Skill mapping

**External Commands** (routed to skills):
- All domain-specific commands
- Execute skills with arguments
- Skill produces output
- Subagent presents in persona voice

---

## 5. Dependency Management

### Dependency Types

```yaml
dependencies:
  skills:         # Other skills this depends on
    - common/load-config.md

  templates:      # Document templates
    - risk-profile.md

  checklists:     # Validation checklists
    - risk-assessment-checklist.md

  data:           # Reference data
    - risk-categories.md
    - technical-preferences.md
```

### Dependency Resolution

**For Skills:**
```
skill: risk-profile.md
  depends on: templates/risk-profile.md
  depends on: common/load-config.md

Resolution:
1. Check if dependencies exist
2. Load dependencies when skill executes
3. Dependencies are inputs to skill logic
```

**For Subagents:**
```
subagent: quality.md (Quinn)
  depends on: skills/quality/*.md
  depends on: templates/*.md

Resolution:
1. Subagent file declares available commands
2. Each command routes to a skill
3. Skills load their own dependencies
4. Subagent doesn't load skills until command invoked
```

### Lazy Loading

**Skills load dependencies only when executed:**
```
User: @quinn *risk task-006
↓
Quinn activates (loads quality.md)
↓
Routes "*risk" → risk-profile.md skill
↓
risk-profile.md loads:
  - templates/risk-profile.md
  - common/load-config.md
↓
Executes with loaded dependencies
```

**Benefits:**
- Minimal context usage
- Faster activation
- Only load what's needed

---

## 6. Orchestration Patterns

### Pattern 1: Direct Skill Execution

**User directly invokes skill via subagent command**

```
@quinn *risk task-006
  ↓
Quinn routes to risk-profile.md
  ↓
Skill executes
  ↓
Quinn presents result
```

**When to use:** Single, focused assessment

### Pattern 2: Skill Composition (Orchestrator Skill)

**Skill that calls other skills in sequence**

```
@quinn *review task-006
  ↓
Quinn routes to review-task.md (orchestrator skill)
  ↓
review-task.md executes:
  1. risk-profile.md
  2. test-design.md
  3. trace-requirements.md
  4. nfr-assess.md
  5. quality-gate.md
  ↓
Aggregates results
  ↓
Quinn presents comprehensive review
```

**When to use:** Comprehensive assessment with multiple dimensions

### Pattern 3: Cross-Subagent Handoff

**Workflow spans multiple subagents**

```
User: "Plan and implement user auth"
  ↓
@alex (Planner) *create user authentication
  ↓
Alex executes create-task-spec.md
  ↓
Produces: task-006-user-auth.md (status: Approved)
  ↓
Alex: "Task ready. Would you like me to assess risks? Handing to Quinn..."
  ↓
@quinn *risk task-006
  ↓
Quinn executes risk-profile.md
  ↓
Quinn: "3 high risks identified. Review before implementation?"
  ↓
User reviews and approves
  ↓
Quinn: "Risks noted. Ready for implementation. Handing to James..."
  ↓
@james *execute task-006
  ↓
James executes execute-task.md
  ↓
Implementation complete, status: Review
  ↓
James: "Implementation complete. Handing back to Quinn for review..."
  ↓
@quinn *review task-006
  ↓
Final quality assessment
```

**When to use:** Complete feature workflow

### Pattern 4: Parallel Skill Execution

**Multiple independent skills run in parallel**

```
@quinn "Assess task-006 risks and task-007 risks in parallel"
  ↓
Quinn spawns:
  - risk-profile.md with task-006
  - risk-profile.md with task-007
  ↓
Both execute independently
  ↓
Quinn aggregates and presents both results
```

**When to use:** Independent assessments, batch operations

---

## 7. Integration with Claude Code

### Claude Code Features Used

**1. Subagents (Claude Code Native)**

Claude Code supports subagents natively. We leverage this:

```
Subagent Definition → .claude/subagents/{name}.md
Invocation → @{name} commands
```

**How BMAD Enhanced Uses It:**
- Each BMAD agent becomes a Claude Code subagent
- Subagent file contains persona + command routing
- Claude Code handles activation and context management

**2. Skills (Claude Code Native)**

Claude Code supports skills as reusable capabilities:

```
Skill Definition → .claude/skills/{category}/{name}.md
Invocation → Via subagent command routing
```

**How BMAD Enhanced Uses It:**
- Each BMAD task becomes a Claude Code skill
- Skills are pure executable logic
- Subagents route commands to skills

**3. Configuration (Project-Specific)**

```
Configuration → .claude/config.yaml
```

Skills and subagents load config for:
- Project settings
- Quality thresholds
- File locations
- Workflow preferences

### Claude Code Subagent API

**Subagent Activation:**
```markdown
# In subagent file
When activated:
1. Load persona definition
2. Adopt communication style
3. Load command routing table
4. Greet user
5. Show help
6. Wait for commands
```

**Command Execution:**
```markdown
# In subagent file
When command received:
1. Parse command and arguments
2. Look up in routing table
3. Load skill file
4. Execute skill with arguments
5. Present results in persona voice
6. Wait for next command or exit
```

**Context Management:**
```markdown
# Automatic by Claude Code
- Subagent maintains persona during session
- Previous conversation visible
- Can reference earlier commands
- Exit command releases persona
```

### Integration Example

**File: `.claude/subagents/quality.md`**
```markdown
# Quality Subagent

[Claude Code recognizes this as subagent]

Activation: @quinn
Commands: *risk, *test-design, *trace, *nfr, *review, *gate

[Persona definition...]
[Command routing...]
[Dependencies...]
```

**Usage:**
```
User: @quinn
Claude Code: [Activates quality.md subagent]
Quinn: [Greets in persona, shows commands]

User: *risk task-006
Quinn: [Routes to skills/quality/risk-profile.md]
Quinn: [Executes skill]
Quinn: [Presents results in Quinn's voice]

User: *exit
Quinn: [Exits persona]
Claude Code: [Returns to main conversation]
```

---

## 8. File Organization

### Complete Directory Structure

```
.claude/
├── config.yaml                    # Project configuration
│
├── subagents/                     # Personas (like BMAD agents/)
│   ├── planner.md                # Alex - Technical Planning Specialist
│   ├── developer.md              # James - Senior Software Engineer
│   ├── quality.md                # Quinn - Test Architect
│   └── orchestrator.md           # Workflow coordinator
│
├── skills/                        # Executable logic (like BMAD tasks/)
│   ├── planning/
│   │   ├── create-task-spec.md
│   │   ├── validate-task-spec.md
│   │   └── shard-document.md
│   │
│   ├── implementation/
│   │   ├── execute-task.md
│   │   ├── run-tests.md
│   │   └── apply-fixes.md
│   │
│   ├── quality/
│   │   ├── risk-profile.md        ✅ Built
│   │   ├── test-design.md         ⏳ Next
│   │   ├── trace-requirements.md  ⏳ Next
│   │   ├── nfr-assess.md          ⏳ Next
│   │   ├── quality-gate.md        ⏳ Next
│   │   └── review-task.md         ⏳ Refactor to orchestrator
│   │
│   └── common/
│       ├── load-config.md
│       ├── execute-checklist.md
│       └── generate-report.md
│
├── templates/                     # Document structures (like BMAD templates/)
│   ├── task-spec.md
│   ├── quality-gate.yaml
│   ├── risk-profile.md           ✅ Built
│   ├── test-design.md
│   └── traceability-matrix.md
│
├── checklists/                    # Validation lists (like BMAD checklists/)
│   ├── task-spec-checklist.md
│   ├── story-dod-checklist.md
│   └── risk-assessment-checklist.md
│
├── data/                          # Reference information (like BMAD data/)
│   ├── technical-preferences.md
│   ├── risk-categories.md
│   └── quality-standards.md
│
├── tasks/                         # Generated task specifications
│   └── task-{id}-{slug}.md
│
└── quality/                       # Quality assessment outputs
    ├── assessments/
    │   ├── {task}-risk-{date}.md
    │   ├── {task}-test-design-{date}.md
    │   ├── {task}-trace-{date}.md
    │   └── {task}-nfr-{date}.md
    └── gates/
        └── {task}-gate.yaml
```

### Mapping to BMAD Structure

| BMAD | BMAD Enhanced | Purpose |
|------|---------------|---------|
| `agents/` | `subagents/` | Personas with commands |
| `tasks/` | `skills/` | Executable logic |
| `templates/` | `templates/` | Document structures |
| `checklists/` | `checklists/` | Validation lists |
| `data/` | `data/` | Reference information |
| `workflows/` | (in subagents) | Orchestration patterns |

**Perfect 1:1 mapping!**

---

## 9. Implementation Roadmap

### Phase 2A: Quality Skills (Current)

**Goal:** Break down monolithic review-task.md into focused skills

**Skills to Build:**
1. ✅ **risk-profile.md** - COMPLETE
2. ⏳ **test-design.md** - Next
3. ⏳ **trace-requirements.md** - After test-design
4. ⏳ **nfr-assess.md** - After trace
5. ⏳ **quality-gate.md** - After nfr
6. ⏳ **review-task.md** - Refactor to orchestrator

**Status:** 1/6 complete (17%)

### Phase 2B: Subagents

**Goal:** Create persona-driven subagents that orchestrate skills

**Subagents to Build:**
1. ⏳ **quality.md** (Quinn) - After quality skills complete
2. ⏳ **planner.md** (Alex) - Refactor from Phase 1
3. ⏳ **developer.md** (James) - Refactor from Phase 1
4. ⏳ **orchestrator.md** - Workflow coordinator

**Status:** 0/4 complete (0%)

### Phase 2C: Common Skills

**Goal:** Extract common functionality used by multiple subagents

**Skills to Build:**
1. ⏳ **load-config.md** - Config loading logic
2. ⏳ **execute-checklist.md** - Checklist validation
3. ⏳ **generate-report.md** - Report generation

**Status:** 0/3 complete (0%)

### Phase 3: Advanced Orchestration

**Goal:** Inter-subagent workflows and automation

**Features to Build:**
1. Automatic handoffs between subagents
2. Workflow state management
3. Parallel skill execution
4. Skill composition patterns

### Success Metrics

**Phase 2 Complete When:**
- [ ] All 6 quality skills built and tested
- [ ] 4 subagents operational
- [ ] 3 common skills extracted
- [ ] Skills reusable across subagents
- [ ] Commands route correctly
- [ ] End-to-end workflow tested

---

## Conclusion

The **Skills + Subagents** architecture provides:

✅ **Direct BMAD Mapping:** Skills = Tasks, Subagents = Agents
✅ **Separation of Concerns:** Logic vs. Persona
✅ **Reusability:** Skills used by multiple subagents
✅ **Maintainability:** Small, focused components
✅ **Extensibility:** Easy to add new skills/subagents
✅ **Testability:** Skills testable independently
✅ **Claude Code Native:** Leverages platform features

**Next:** Continue building quality skills (test-design.md next)

---

**End of Detailed Architecture**
