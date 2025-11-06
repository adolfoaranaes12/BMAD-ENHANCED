# BMAD Enhanced - Complete Command Reference

**Quick reference for all subagent commands**

Version: 2.0
Last Updated: 2025-11-05

---

## Command Syntax

**General Form:**
```bash
/agent *task parameters
```

**Where:**
- `/agent` - Slash command routing to subagent
- `*task` - Skill command (asterisk prefix required)
- `parameters` - Arguments (files, strings, flags)

---

## Core Agents (5)

### Planning (Alex)

```bash
/alex *create-task-spec "<description>"
/alex *breakdown-epic "<epic-file>"
/alex *estimate <story-id>
/alex *refine-story "<vague-requirement>"
/alex *plan-sprint "<sprint-name>" --velocity 40
```

**Purpose:** Planning, requirements, estimation, story refinement

---

### Development (James)

```bash
/james *implement <task-file>
/james *fix <bug-description>
/james *test [path]
/james *refactor <file-path>
/james *apply-qa-fixes <task-id>
/james *debug "<issue-description>"
/james *explain <file-path>
```

**Purpose:** Implementation with TDD, bug fixes, refactoring, testing

---

### Quality (Quinn)

```bash
/quinn *review <task-file>
/quinn *assess-nfr <task-file>
/quinn *validate-quality-gate <task-file>
/quinn *trace-requirements <task-file>
/quinn *assess-risk <task-file>
```

**Purpose:** Quality assurance, NFR validation, risk assessment, compliance

---

### Architecture (Winston)

```bash
/winston *analyze-architecture [codebase-path] [--depth <mode>] [--output <format>]
/winston *create-architecture <requirements-file> [--type <type>] [--depth <mode>]
/winston *validate-architecture <architecture-file> [--strict]
/winston *review-architecture <architecture-file> [--focus <area>]
/winston *compare-architectures "<requirements>" [--current <path>]
/winston *create-adr "<decision-description>"
/winston *validate-patterns <codebase-path>
```

**Purpose:** System architecture design, analysis, technology decisions

**Special:**
```bash
/winston-consult ["<question>"]
```
Conversational architecture advisor (no *task needed)

---

### Orchestrator

```bash
/orchestrator *workflow <workflow-type> "<description>"
/orchestrator *coordinate "<task-description>" --subagents <agents>
/orchestrator *resume <workflow-id>
/orchestrator *status <workflow-id>
```

**Workflow Types:**
- `feature-delivery` - Complete feature (plan → implement → review)
- `epic-to-sprint` - Epic breakdown to sprint plan
- `sprint-execution` - Execute complete sprint
- `modernize` - Brownfield modernization
- `document-codebase` - Generate complete documentation (architecture, API, code, guides)

**Purpose:** Multi-agent workflow coordination, state management

---

## Persona Agents (5)

### Product Manager (John)

```bash
/john *create-prd "<product-idea>"
/john *create-brownfield-prd "<codebase-path>"
/john *shard-prd "<prd-file>"
/john *create-brownfield-epic "<feature-area>" --codebase "<path>"
/john *create-brownfield-story "<feature>" --epic "<epic-id>"
```

**Purpose:** PRD creation, brownfield documentation, product strategy

---

### Business Analyst (Mary)

```bash
/mary *brainstorm "<topic>"
/mary *create-competitor-analysis "<product/market>"
/mary *create-project-brief "<project-name>"
/mary *perform-market-research "<market/product>"
/mary *research-prompt "<topic>"
/mary *elicit "<initial-requirement>"
```

**Purpose:** Brainstorming, market research, competitive analysis, discovery

---

### UX Expert (Sally)

```bash
/sally *create-front-end-spec "<feature-description>"
/sally *generate-ui-prompt "<feature-description>" --tool "<v0|lovable|artifacts>"
```

**Purpose:** UI/UX design, frontend specifications, interaction design

---

### Product Owner (Sarah)

```bash
/sarah *create-epic "<epic-name>" --source "<requirement-source>"
/sarah *create-story "<story-description>"
/sarah *validate-story-draft "<story-file>"
/sarah *shard-doc "<document-path>"
/sarah *execute-checklist-po "<workflow-type>"
```

**Purpose:** Backlog management, story validation, INVEST criteria enforcement

---

### Scrum Master (Bob)

```bash
/bob *create-dev-story "<feature-description>"
/bob *prepare-handoff <story-file>
```

**Purpose:** Developer-ready stories, clear handoffs, sprint facilitation

---

## Command Examples

### Simple Commands

```bash
/james *test                           # Run all tests
/alex *estimate story-001              # Estimate story points
/quinn *review task-001                # Quality review
```

### Commands with Descriptions

```bash
/alex *create-task-spec "User login with OAuth"
/james *fix "Button click not working on mobile"
/mary *brainstorm "Mobile app monetization strategies"
```

### Commands with Files

```bash
/james *implement .claude/tasks/task-001.md
/quinn *review .claude/tasks/task-001.md
/winston *review-architecture docs/architecture.md
```

### Commands with Flags

```bash
/winston *create-architecture docs/prd.md --type fullstack --depth comprehensive
/quinn *review task-001 --depth thorough
/alex *plan-sprint "Sprint 15" --velocity 40
```

### Orchestration Workflows

```bash
/orchestrator *workflow feature-delivery "Shopping cart checkout"
/orchestrator *workflow modernize . "Scale to 100K users + add real-time"
/orchestrator *workflow document-codebase . --depth comprehensive
/orchestrator *coordinate "Quality improvement" --subagents quinn,james
```

### Conversational (No *task)

```bash
/winston-consult "I have a React app. Want to add real-time features."
```

---

## Command Flow

```
User Types          Slash Expands       Subagent Loads     Routes to Skill
/alex *task   →    Task Tool Call  →   alex-planner-v2 →  create-task-spec/
                                                             SKILL.md
```

**7-Step Execution:**
1. User types `/agent *task`
2. Slash command expands to Task tool
3. Subagent loads (.claude/agents/)
4. Routing logic matches `*task`
5. Skill loads (.claude/skills/)
6. Skill executes workflow
7. Result returns to user

---

## Quick Reference by Use Case

### Planning a Feature
```bash
/alex *create-task-spec "Feature description"
/alex *estimate task-001
/quinn *assess-risk task-001
```

### Implementing a Feature
```bash
/james *implement task-001
/james *test task-001
/quinn *review task-001
```

### Fixing a Bug
```bash
/james *debug "Bug description"
/james *fix task-bug-001
/quinn *review task-bug-001
```

### Designing Architecture
```bash
/winston-consult "Architecture question"
/winston *create-architecture docs/requirements.md
/winston *review-architecture docs/architecture.md
```

### Complete Workflow
```bash
/orchestrator *workflow feature-delivery "Complete feature description"
```

### Documenting Codebase
```bash
/orchestrator *workflow document-codebase . --depth standard
/orchestrator *workflow document-codebase . --types api,code --update-existing
/orchestrator *workflow document-codebase packages/backend --depth quick
```

---

## Tips

✅ **Use slash** (`/`) for agent routing
✅ **Use asterisk** (`*`) for skill tasks  
✅ **Quote strings** with spaces
✅ **Use flags** for options (--type, --depth, --velocity)
✅ **Orchestrator** for multi-step workflows
✅ **Winston-consult** for interactive help

---

**See Also:**
- [QUICK-START.md](./QUICK-START.md) - Getting started guide
- [AGENT-REFERENCE.md](./AGENT-REFERENCE.md) - Detailed command reference
- [WORKFLOW-GUIDE.md](./WORKFLOW-GUIDE.md) - Workflow examples

---

**Version:** 2.1
**Status:** Production Ready
**Complete Command Count:** 55+ commands across 10 agents
**Workflows Available:** 5 (feature-delivery, epic-to-sprint, sprint-execution, modernize, document-codebase)
