# Command Audit & Categorization

**Date:** 2025-11-06
**Objective:** Categorize commands for hybrid architecture (skill-direct vs subagent routing)

---

## Audit Summary

**Total Skills:** 32
**Total Commands:** 15
**Current Architecture:** Most commands route to subagents (via Task tool)
**Target Architecture:** Hybrid (skill-direct for deterministic, subagent for flexible)

---

## Category 1: SKILL-DIRECT Commands (Deterministic)

These should invoke skills directly in main context for reliability and efficiency.

### Architecture Skills

| Current Command | Target Command | Skill | Rationale |
|----------------|----------------|-------|-----------|
| `/winston *analyze-architecture` | `/analyze-architecture` | `analyze-architecture` | Fixed 15-step workflow, structured report |
| `/winston *create-architecture` | `/create-architecture` | `create-architecture` | Deterministic: PRD → tech stack → ADRs |
| `/design-architecture` | ✅ Keep | `create-architecture` | Already direct (verify) |
| `/winston *review-architecture` | `/review-architecture` | `architecture-review` | Structured peer review process |
| `/review-architecture` | ✅ Keep | `architecture-review` | Already direct (verify) |
| `/winston *validate-architecture` | `/validate-architecture` | `validate-architecture` | Validation checklist execution |
| `/winston *compare-architectures` | `/compare-architectures` | `compare-architectures` | Generate 3 options, compare trade-offs |
| `/winston *create-adr` | `/create-adr` | `create-adr` | Structured ADR creation |

### Planning Skills

| Current Command | Target Command | Skill | Rationale |
|----------------|----------------|-------|-----------|
| `/alex *create-task-spec` | `/create-task-spec` | `create-task-spec` | Fixed workflow: requirements → breakdown → spec |
| `/alex *breakdown-epic` | `/breakdown-epic` | `breakdown-epic` | Algorithm-based story breakdown |
| `/alex *estimate-stories` | `/estimate-stories` | `estimate-stories` | Fibonacci estimation with complexity analysis |
| `/alex *sprint-plan` | `/sprint-plan` | `sprint-plan` | Allocation algorithm based on velocity |
| `/alex *refine-story` | `/refine-story` | `refine-story` | Structured refinement checklist |
| `/validate-story` | ✅ Keep | `validate-story` | Already direct (verify) |
| `/alex *create-prd` | `/create-prd` | `create-prd` | Structured PRD creation from requirements |
| `/alex *create-brownfield-prd` | `/create-brownfield-prd` | `create-brownfield-prd` | Codebase → PRD generation |

### Development Skills

| Current Command | Target Command | Skill | Rationale |
|----------------|----------------|-------|-----------|
| `/james *implement` | `/implement-feature` | `implement-feature` | Structured: spec → code → tests → validation |
| `/james *run-tests` | `/run-tests` | `run-tests` | Execute test suite, analyze coverage, identify gaps |
| `/james *apply-qa-fixes` | `/apply-qa-fixes` | `apply-qa-fixes` | Apply fixes from quality gate report |
| `/james *refactor` | `/refactor-code` | `refactor-code` | Structured refactoring with safety checks |

### Quality Skills

| Current Command | Target Command | Skill | Rationale |
|----------------|----------------|-------|-----------|
| `/quinn *quality-gate` | `/quality-gate` | `quality-gate` | Deterministic: checks → score → pass/fail |
| `/quinn *nfr-assess` | `/nfr-assess` | `nfr-assess` | Fixed assessment across 8 dimensions |
| `/quinn *review-task` | `/review-task` | `review-task` | Structured review checklist |
| `/quinn *risk-profile` | `/risk-profile` | `risk-profile` | Risk assessment framework |
| `/quinn *test-design` | `/test-design` | `test-design` | Test strategy generation |
| `/quinn *trace-requirements` | `/trace-requirements` | `trace-requirements` | Requirements traceability matrix |

### Brownfield/Documentation Skills

| Current Command | Target Command | Skill | Rationale |
|----------------|----------------|-------|-----------|
| `/james *document-project` | `/document-project` | `document-project` | Codebase → documentation generation |
| `/alex *index-docs` | `/index-docs` | `index-docs` | Create searchable documentation index |
| `/alex *shard-document` | `/shard-document` | `shard-document` | Break large docs into manageable shards |

---

## Category 2: SUBAGENT Commands (Flexible/Conversational)

These should route to subagents for exploration, conversation, and dynamic workflows.

### Consultation & Guidance

| Command | Subagent | Rationale |
|---------|----------|-----------|
| `/winston-consult` | `winston-architect` | ✅ Conversational architecture guidance, option exploration |
| `/alex consult` | `alex-planner-v2` | NEW: Planning strategy discussions |
| `/james consult` | `james-developer-v2` | NEW: Technical implementation discussions |
| `/quinn consult` | `quinn-quality-v2` | NEW: Quality strategy discussions |

### Debugging & Problem Solving

| Command | Subagent | Rationale |
|---------|----------|-----------|
| `/james debug <issue>` | `james-developer-v2` | ✅ Exploratory debugging, trial-error |
| `/james fix <issue>` | `james-developer-v2` | ✅ Problem diagnosis → solution → test → iterate |

### Workflow Orchestration

| Command | Subagent | Rationale |
|---------|----------|-----------|
| `/orchestrator *workflow <type>` | `orchestrator-v2` | ✅ Multi-agent coordination, state management |
| `/orchestrator *document-codebase` | `orchestrator-v2` | ✅ Flexible documentation generation with decisions |
| `/orchestrator *coordinate` | `orchestrator-v2` | ✅ Cross-subagent coordination |

### Product/UX (if applicable)

| Command | Subagent | Rationale |
|---------|----------|-----------|
| `/john <task>` | `john-pm` | Product strategy, PRD review (conversational) |
| `/sarah <task>` | `sarah-po` | Backlog management, story validation (conversational) |
| `/sally <task>` | `sally-ux-expert` | UX design, front-end specs (conversational) |
| `/bob <task>` | `bob-sm` | Scrum master tasks (conversational) |
| `/mary <task>` | `mary-analyst` | Business analysis, research (conversational) |

---

## Category 3: HYBRID Commands (Can be both)

Some commands might benefit from both approaches.

| Command | Skill-Direct Usage | Subagent Usage |
|---------|-------------------|----------------|
| `/implement` | `/implement-feature <spec-file>` (deterministic) | `/james implement "vague requirement"` (needs exploration) |
| `/fix` | `/fix-issue <task-id>` (known issue) | `/james fix "something broken"` (needs diagnosis) |
| `/document` | `/document-project .` (deterministic) | `/orchestrator *document-codebase` (flexible) |

---

## Migration Priority

### Phase 1: High-Impact, Low-Risk (Do First)
1. ✅ `/analyze-architecture` - heavily used, clear workflow
2. ✅ `/create-task-spec` - core BMAD workflow
3. ✅ `/implement-feature` - frequent operation
4. ✅ `/quality-gate` - clear pass/fail logic

### Phase 2: Planning & Architecture (Do Second)
5. `/create-architecture`
6. `/breakdown-epic`
7. `/estimate-stories`
8. `/sprint-plan`
9. `/review-architecture`

### Phase 3: Quality & Testing (Do Third)
10. `/nfr-assess`
11. `/review-task`
12. `/run-tests`
13. `/test-design`
14. `/trace-requirements`

### Phase 4: Specialized (Do Last)
15. Brownfield/documentation skills
16. Product/UX commands
17. Remaining edge cases

---

## Action Items

### 1. Create New Skill-Direct Commands
- [ ] Create 25+ new command files for direct skill invocation
- [ ] Use template: parse args → invoke Skill() → done

### 2. Update Subagent Commands
- [ ] Keep `/winston-consult`, `/orchestrator`, `/james debug`, `/james fix`
- [ ] Add graceful degradation when skills don't load
- [ ] Document when to use subagent vs skill-direct

### 3. Deprecation Strategy
- [ ] Keep old commands working (backward compatibility)
- [ ] Add deprecation warnings
- [ ] Update documentation with new patterns

### 4. Documentation
- [ ] Create COMMAND-ROUTING-GUIDE.md
- [ ] Update QUICK-START.md with new patterns
- [ ] Add examples to EXAMPLE-WORKFLOWS.md

---

## Notes

**Current Problem:**
- All `/winston`, `/alex`, `/james`, `/quinn` commands route to subagents via Task tool
- Skills sometimes don't load in Task subprocess
- Falls back to general knowledge (quality degradation)

**Solution:**
- Deterministic tasks → direct skill invocation (reliable)
- Flexible tasks → subagent with graceful degradation
- Clear naming: skill name for direct, agent name for flexible

**Benefits:**
- ✅ Reliability (skills load consistently in main context)
- ✅ Context efficiency (skills on-demand)
- ✅ Clarity (command name indicates execution path)
- ✅ Flexibility (subagents available for complex work)
