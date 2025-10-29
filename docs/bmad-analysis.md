# BMAD-METHOD v4 Architecture Analysis

**Analysis Date:** 2025-10-28
**Source Repository:** bmad-code-org/BMAD-METHOD
**Version Analyzed:** v4.x (stable)
**Purpose:** Understanding BMAD architecture to enhance Claude Code workflow with subagents and skills

---

## Executive Summary

BMAD-METHOD is a comprehensive **Agentic Agile Development framework** that uses specialized AI agents with defined personas, dependencies, and workflow orchestration. The core innovation is **two-phase context engineering**:

1. **Planning Phase (Web UI)**: Analyst → PM → Architect → PO create detailed PRD and Architecture
2. **Development Phase (IDE)**: SM → Dev → QA iterate through story-based implementation

**Key Insight:** BMAD solves context loss through **hyper-detailed story files** that embed complete implementation context, eliminating the need for Dev agents to search for information.

---

## Core Architecture Components

### 1. Directory Structure

```
bmad-core/
├── agents/              # Agent persona definitions (MD files with YAML headers)
├── agent-teams/         # Team bundles for web UI
├── workflows/           # Workflow orchestration definitions
├── templates/           # Document templates (YAML-based)
├── tasks/               # Executable task instructions
├── checklists/          # Quality assurance checklists
├── data/                # Knowledge base and preferences
└── core-config.yaml     # Project configuration
```

### 2. Agent Architecture Pattern

Each agent is a **markdown file** containing:

```yaml
# Agent Definition Structure (from dev.md, sm.md, qa.md)

IDE-FILE-RESOLUTION:
  - Dependencies map to {root}/{type}/{name}
  - Only load files when executing commands

activation-instructions:
  - STEP 1: Read entire agent file
  - STEP 2: Adopt persona
  - STEP 3: Load core-config.yaml
  - STEP 4: Greet + run *help + HALT

agent:
  name: <Agent Name>
  id: <agent-id>
  title: <Role Title>
  icon: <emoji>
  whenToUse: <Activation criteria>
  customization: <Optional overrides>

persona:
  role: <Specific expertise>
  style: <Communication style>
  identity: <Core identity>
  focus: <Primary focus area>
  core_principles:
    - <Principle 1>
    - <Principle 2>

commands:
  - help: Show commands
  - command-name: Execute task {task-name}
  - exit: Leave persona

dependencies:
  checklists: [file1.md, ...]
  tasks: [file1.md, ...]
  templates: [file1.md, ...]
  data: [file1.md, ...]
```

**Critical Design Patterns:**

- **Lazy Loading**: Agents only load dependencies when commands execute
- **Persona-Driven**: Each agent adopts specific identity and communication style
- **Command-Based**: Interaction through `*command` syntax
- **State Management**: Agents maintain persona until explicitly exited
- **Context Boundaries**: Strict rules about what sections agents can modify

### 3. Key Agents and Roles

| Agent | Persona | Primary Function | Key Commands |
|-------|---------|------------------|--------------|
| **Analyst** | Business Analyst | Market research, competitive analysis, project briefs | `*brainstorm`, `*research`, `*compete` |
| **PM** | Product Manager | PRD creation from briefs | `*create-prd`, `*refine` |
| **Architect** | System Architect | Architecture design from PRD | `*create-arch`, `*design` |
| **PO** | Product Owner | Document validation, sharding, alignment | `*shard`, `*validate`, `*checklist` |
| **SM** | Scrum Master | Story drafting with full context | `*draft`, `*correct-course` |
| **Dev** | Senior Developer | Sequential task execution | `*develop-story`, `*run-tests` |
| **QA** | Test Architect | Risk assessment, test design, quality gates | `*risk`, `*design`, `*trace`, `*nfr`, `*review`, `*gate` |
| **UX Expert** | UX Designer | Frontend specifications | `*create-spec`, `*generate-prompt` |

### 4. Workflow Orchestration

#### Planning Workflow (Typically Web UI)
```mermaid
Analyst → Project Brief
    ↓
PM → PRD (Epics + Stories with AC)
    ↓
Architect → Architecture (Tech Stack, Patterns, Standards)
    ↓
PO → Validation + Sharding
    ↓
SWITCH TO IDE
```

#### Development Workflow (IDE)
```mermaid
SM → Draft Story (with full context from PRD + Architecture)
    ↓
Dev → Implement Tasks Sequentially
    ↓
QA → Review + Quality Gate (optional)
    ↓
Mark Done → Next Story
```

**Critical Context Flow:**
- PRD contains: Epics → Stories → Acceptance Criteria
- Architecture contains: Tech stack, patterns, coding standards, project structure
- SM creates **hyper-detailed story file** that embeds:
  - All relevant architecture context
  - Previous story learnings
  - Specific data models, APIs, components
  - File paths and naming conventions
  - Testing requirements
- Dev agent reads **only the story file** + project-specific standards
  - Never loads PRD/Architecture during implementation
  - All context already embedded in story

---

## Key Innovations Worth Adopting

### 1. Context Engineering Through Story Files

**Problem Solved:** AI agents lose context and make inconsistent decisions

**BMAD Solution:**
- SM agent reads PRD + Architecture + Previous Story
- Creates detailed story file with:
  ```yaml
  Dev Notes:
    - Previous Story Insights: <key learnings>
    - Data Models: <specific schemas> [Source: architecture/data-models.md#section]
    - API Specifications: <endpoints> [Source: architecture/rest-api-spec.md#section]
    - Component Specifications: <UI details> [Source: architecture/components.md#section]
    - File Locations: <exact paths> [Source: architecture/project-structure.md]
    - Testing Requirements: <test strategy> [Source: architecture/testing-strategy.md]
  ```
- Every technical detail includes source reference
- Dev agent never needs to search for information

**Applicability to Claude Code:**
- Subagents/Skills could follow similar pattern
- Planning skill creates detailed task specs
- Implementation skill executes with complete context
- Eliminates redundant file reads and searches

### 2. Persona-Driven Agent Behavior

**BMAD Pattern:**
```yaml
persona:
  role: Technical Scrum Master - Story Preparation Specialist
  style: Task-oriented, efficient, precise
  identity: Story creation expert who prepares for AI developers
  focus: Creating crystal-clear stories that dumb AI agents can implement
  core_principles:
    - Rigorously follow create-next-story procedure
    - Ensure all info comes from PRD and Architecture
    - NOT allowed to implement stories EVER!
```

**Value:**
- Clear role boundaries prevent scope creep
- Consistent communication style
- Predictable behavior patterns
- Easy to debug when agents deviate

**Applicability to Claude Code:**
- Skills could define persona contexts
- Subagents inherit persona constraints
- Reduces need for repeated instructions

### 3. Dependency Declaration System

**BMAD Pattern:**
```yaml
dependencies:
  checklists:
    - story-draft-checklist.md
  tasks:
    - create-next-story.md
  templates:
    - story-tmpl.yaml
```

**Value:**
- Agents only load what they need (lean context)
- Clear capability boundaries
- Easy to trace what influences agent behavior
- Enables modular expansion packs

**Applicability to Claude Code:**
- Skills could declare required tools/files
- Lazy loading pattern reduces context bloat
- Clear dependency graph for debugging

### 4. Quality Gates with Advisory Authority

**BMAD QA Pattern:**
- `*risk`: Assess risks before development (P×I scoring)
- `*design`: Create test strategy (unit/integration/E2E)
- `*trace`: Map requirements to tests (coverage gaps)
- `*nfr`: Validate non-functionals (security, performance, reliability, maintainability)
- `*review`: Comprehensive assessment + active refactoring
- `*gate`: PASS/CONCERNS/FAIL/WAIVED with rationale

**Critical Design:** QA is **advisory, not blocking**
- Teams choose their quality bar
- WAIVED requires reason + approver + expiry
- Gates stored in `docs/qa/gates/` (parallel authority)

**Value:**
- Systematic quality assessment
- Risk-based prioritization
- Traceability for audits
- Active improvement (not just critique)

**Applicability to Claude Code:**
- Review skill with similar risk profiling
- Test design skill for comprehensive coverage
- Quality gate skill for go/no-go decisions

### 5. Configuration-Driven Workflow

**core-config.yaml:**
```yaml
markdownExploder: true
qa:
  qaLocation: docs/qa
prd:
  prdFile: docs/prd.md
  prdVersion: v4
  prdSharded: true
  prdShardedLocation: docs/prd
architecture:
  architectureFile: docs/architecture.md
  architectureVersion: v4
  architectureSharded: true
  architectureShardedLocation: docs/architecture
devLoadAlwaysFiles:
  - docs/architecture/coding-standards.md
  - docs/architecture/tech-stack.md
  - docs/architecture/source-tree.md
```

**Value:**
- Adapts to different project structures
- Dev agent knows exactly what to load
- Enables brownfield/greenfield differences
- Single source of truth for paths

**Applicability to Claude Code:**
- Project-level configuration file
- Skills read config for context
- Standardized paths across workflows

### 6. Task-Based Execution Pattern

**Task Files Structure:**
```markdown
# Task Name

## Purpose
[Clear statement of what this task accomplishes]

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 0. Pre-requisites
- Check config
- Validate inputs
- Load required files

### 1. Step Name
[Detailed instructions with decision points]

### 2. Next Step
[More instructions]

### 3. Completion
[Verification and outputs]
```

**Value:**
- Agents execute deterministically
- Clear decision points and halting conditions
- Built-in validation at each step
- Easy to debug where agents deviate

**Applicability to Claude Code:**
- Skills with structured execution phases
- Clear halt conditions
- Validation checkpoints

---

## Comparison: BMAD vs Current Claude Code

| Aspect | BMAD Method | Claude Code | Gap/Opportunity |
|--------|-------------|-------------|-----------------|
| **Agent Definition** | Markdown + YAML persona | Skills with prompts | Could add persona layer |
| **Dependency Management** | Explicit YAML declarations | Implicit tool access | Could add dependency declarations |
| **Context Loading** | Lazy, command-triggered | Eager tool use | Could optimize with lazy loading |
| **Workflow Orchestration** | Multi-agent handoffs (SM→Dev→QA) | Single session with tool calls | Could use subagents for phases |
| **Story Context** | Hyper-detailed embedded context | README + exploration | Could create context-rich task specs |
| **Quality Gates** | Structured QA workflow | Ad-hoc review | Could add systematic QA skill |
| **Configuration** | core-config.yaml | Implicit project scanning | Could add project config |
| **Role Boundaries** | Strict persona constraints | Flexible behavior | Could add role-based constraints |

---

## Migration Opportunities

### High Priority

1. **Context-Rich Task Specification Pattern**
   - Create planning skill that embeds full implementation context
   - Similar to SM agent's story drafting
   - Eliminates redundant file reads during implementation

2. **Structured Quality Review Skill**
   - Risk profiling before implementation
   - Test design guidance
   - Requirements traceability
   - NFR validation (security, performance, reliability)
   - Quality gates with rationale

3. **Project Configuration System**
   - `.claude-config.yaml` for project settings
   - Define always-load files
   - Document locations
   - Quality gate paths

### Medium Priority

4. **Persona-Driven Skills**
   - Add persona definitions to skills
   - Clear role boundaries
   - Consistent communication styles

5. **Dependency Declaration**
   - Skills declare required tools/files
   - Lazy loading pattern
   - Clear capability boundaries

6. **Workflow Orchestration**
   - Planning phase subagent
   - Implementation phase subagent
   - Review phase subagent
   - Clear handoff points

### Lower Priority

7. **Template System**
   - YAML-based document templates
   - Interactive elicitation
   - Standardized outputs

8. **Expansion Pack Pattern**
   - Domain-specific skill collections
   - Easy distribution and installation

---

## Recommended Architecture for Claude Code Enhancement

### Phase 1: Foundation (Immediate)

```
.claude/
├── config.yaml              # Project configuration
├── skills/
│   ├── planning/
│   │   └── task-spec.md    # Creates detailed task specifications
│   ├── quality/
│   │   ├── risk-profile.md # Pre-implementation risk assessment
│   │   ├── test-design.md  # Test strategy creation
│   │   └── review.md       # Comprehensive quality review
│   └── implementation/
│       └── develop.md      # Sequential task execution
└── templates/
    ├── task-spec.yaml      # Task specification template
    └── quality-gate.yaml   # Quality gate template
```

### Phase 2: Workflow Orchestration (Short-term)

- Planning subagent: Creates task specs with full context
- Implementation subagent: Executes with embedded context
- Review subagent: Systematic quality assessment

### Phase 3: Advanced Features (Long-term)

- Persona layer for skills
- Dependency management system
- Expansion pack pattern for domain-specific workflows

---

## Key Takeaways

### What Makes BMAD Effective

1. **Context Engineering**: SM embeds all needed context in story files
2. **Role Boundaries**: Agents have clear, limited responsibilities
3. **Sequential Execution**: Dev follows strict task order with validation
4. **Quality Systematization**: QA provides structured risk and test assessment
5. **Configuration-Driven**: Adapts to different project structures

### What to Avoid

1. **Over-prompting**: BMAD uses extensive persona instructions (can be heavy)
2. **Web UI Dependency**: Planning phase optimized for web chat (not IDE)
3. **Rigid Workflow**: Strong opinions about greenfield vs brownfield

### Best Practices to Adopt

1. **Hyper-detailed Task Context**: Eliminate need for implementation-time exploration
2. **Risk-Based Quality**: Assess risks early, design tests accordingly
3. **Traceability**: Map requirements → tests → implementation
4. **Advisory Gates**: Quality decisions with rationale, not blocks
5. **Lazy Loading**: Only load context when commands execute

---

## Next Steps

1. Design `.claude-config.yaml` schema
2. Create planning skill with context embedding pattern
3. Develop structured quality review skill
4. Prototype subagent workflow orchestration
5. Test on real project to validate approach

---

## References

- BMAD Repository: https://github.com/bmad-code-org/BMAD-METHOD
- Key Files Analyzed:
  - `bmad-core/agents/dev.md` - Developer agent pattern
  - `bmad-core/agents/sm.md` - Story drafting pattern
  - `bmad-core/agents/qa.md` - Quality assessment pattern
  - `bmad-core/tasks/create-next-story.md` - Context embedding workflow
  - `bmad-core/core-config.yaml` - Configuration pattern
  - `docs/user-guide.md` - Workflow orchestration
  - `docs/core-architecture.md` - System design

---

**Analysis Complete:** Ready to design migration plan
