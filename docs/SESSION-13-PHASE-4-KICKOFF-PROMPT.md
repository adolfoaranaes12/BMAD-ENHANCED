# Session 13: Phase 4 - Missing BMAD Agents Implementation

**Objective:** Implement 5 missing agent personas and 4 planning skills from BMAD Method v4 to achieve complete workflow parity

**Context:** Phase 3 (Integration & Production Readiness) is 100% complete. BMAD Enhanced V2 is production-ready with 4 subagents (Orchestrator, Alex, James, Quinn) and 17 skills. However, for real-world testing, we need the specialized agent personas from BMAD v4 that provide distinct workflows and capabilities.

---

## Current State

### What We Have ✅
- **4 Subagents:** Orchestrator, Alex (Planner), James (Developer), Quinn (Quality)
- **17 Skills:** All with V2 contracts (acceptance, inputs, outputs, telemetry)
- **19 Commands:** Across all subagents
- **Production Ready:** 100% test coverage, 83% better performance, 0 technical debt

### What's Missing ❌
According to `docs/ROADMAP.md` Phase 3 (Week 7-9), we're missing:

**5 Agent Personas:**
1. Mary (Analyst) - Business analysis, market research, brainstorming
2. John (PM) - Product management, PRD creation, brownfield PRDs
3. Sarah (PO) - Product owner, backlog management, story validation
4. Bob (SM) - Scrum master, story creation, developer handoff
5. Sally (UX Expert) - UX/UI design, wireframes, specifications

**4 Planning Skills:**
1. `create-prd` - Create Product Requirements Documents
2. `create-brownfield-prd` - Generate PRD from existing codebase
3. `shard-document` - Break large documents into manageable pieces
4. `interactive-checklist` - Interactive checklist-driven workflows

---

## Task Breakdown

### Phase 1: Create Missing Planning Skills (Priority: HIGH)
**Estimated Effort:** 20-26 hours across 4 skills

These skills will be used by Alex initially and can be leveraged by the new agent personas later.

#### Skill 1: `create-prd` (Planning Domain)
**File:** `.claude/skills/planning/create-prd/SKILL.md`
**Effort:** 6-8 hours

**Purpose:** Create Product Requirements Documents (PRD) from high-level product ideas

**Key Requirements:**
- YAML frontmatter with V2 contract (acceptance, inputs, outputs, telemetry)
- Progressive disclosure (SKILL.md → references/ → assets/)
- Integration with bmad-commands primitives where applicable
- Support both greenfield and brownfield contexts

**Inputs:**
- Product name and vision
- Target users and personas
- Problem statement
- Business objectives
- Success metrics (optional)
- Competitive landscape (optional)

**Process (5-step workflow):**
1. **Requirements Gathering:** Elicit product vision, users, problems, constraints
2. **Market Analysis:** Competitive landscape, positioning, differentiation
3. **Feature Definition:** Core features (MoSCoW prioritization)
4. **Success Metrics:** KPIs, adoption metrics, business impact
5. **PRD Generation:** Comprehensive document in `docs/prd.md`

**Outputs:**
- `docs/prd.md` or `workspace/prds/{product-name}-prd.md`
- Product overview, user personas, features, success criteria
- Ready for architecture phase (Winston) or epic breakdown (Alex)

**Template Reference:** Use BMAD v4's `prd-tmpl.yaml` structure adapted to markdown

---

#### Skill 2: `create-brownfield-prd` (Planning Domain)
**File:** `.claude/skills/planning/create-brownfield-prd/SKILL.md`
**Effort:** 8-10 hours

**Purpose:** Generate PRD for existing systems based on codebase analysis

**Key Requirements:**
- Leverages `document-project` skill for architecture analysis
- Extracts features from code structure
- Includes confidence scores (like `document-project`)
- V2 contract with telemetry

**Inputs:**
- Project root path
- Existing codebase
- Existing documentation (if any)
- Business context
- Technical stack

**Process (4-step workflow):**
1. **Codebase Analysis:** Use `document-project`, extract features, map data models
2. **Feature Extraction:** Identify core features, categorize (core/secondary/legacy)
3. **User Flow Reconstruction:** Reconstruct journeys, identify personas, document integrations
4. **PRD Generation:** Document existing state, gaps, modernization opportunities

**Outputs:**
- `docs/brownfield-prd.md`
- Existing features documented with confidence scores
- Known limitations and gaps
- Modernization opportunities

**Template Reference:** BMAD v4's `brownfield-prd-tmpl.yaml`

---

#### Skill 3: `shard-document` (Planning Domain)
**File:** `.claude/skills/planning/shard-document/SKILL.md`
**Effort:** 4-6 hours

**Purpose:** Break large documents (PRDs, architectures) into manageable pieces

**Key Requirements:**
- Supports multiple sharding strategies
- Maintains context and cross-references
- Creates index/navigation file
- V2 contract

**Inputs:**
- Document path (PRD, architecture, or large doc)
- Sharding strategy (by section, by epic, by feature, custom)
- Output directory

**Process (4-step workflow):**
1. **Document Analysis:** Parse structure, identify boundaries, calculate sizes
2. **Strategy Selection:** Choose sharding approach (section/epic/feature/custom)
3. **Document Sharding:** Split at boundaries, maintain cross-references, create index
4. **Validation:** All content accounted for, no orphans, cross-references updated

**Outputs:**
- Sharded document files in output directory
- Index file linking all shards
- Metadata file with relationships
- Cross-reference map

**Example Usage:**
```bash
@alex *shard-document "docs/prd.md" --strategy epic --output "workspace/prds/sharded"
```

---

#### Skill 4: `interactive-checklist` (Planning Domain)
**File:** `.claude/skills/planning/interactive-checklist/SKILL.md`
**Effort:** 4-5 hours

**Purpose:** Interactive checklist-driven workflows (PO master checklist, story draft checklist)

**Key Requirements:**
- Load checklists from `.claude/checklists/{name}.md`
- Interactive execution with user confirmation
- Pass/fail/skip tracking with rationale
- V2 contract

**Inputs:**
- Checklist name (po-master-checklist, story-draft-checklist, custom)
- Target file (story, epic, architecture, PRD)
- Checklist file path (optional)

**Process (4-step workflow):**
1. **Load Checklist:** Parse items, identify required vs optional
2. **Interactive Execution:** Present items, check satisfaction, record status
3. **Validation:** Required items must pass, optional can skip
4. **Report Generation:** Summary, pass/fail/skip counts, issues, recommendations

**Outputs:**
- Checklist execution report
- Pass/fail status
- Identified issues
- Recommended actions

**Checklists to Support:**
- `po-master-checklist` (from BMAD v4 Sarah)
- `story-draft-checklist` (from BMAD v4 Bob)
- `architect-checklist` (from BMAD v4 Winston)
- Custom checklists (user-defined)

---

### Phase 2: Create Agent Personas (Priority: MEDIUM)
**Estimated Effort:** 22-28 hours across 5 agents

Create specialized agent personas that leverage the new skills and provide unique workflows.

#### Agent 1: Mary (Analyst) - Business Analysis Specialist
**File:** `.claude/agents/mary-analyst.md`
**Effort:** 6-8 hours

**Persona (from BMAD v4):**
- **Name:** Mary
- **Title:** Business Analyst
- **Icon:** 📊
- **Identity:** Strategic analyst specializing in brainstorming, market research, competitive analysis
- **Style:** Analytical, inquisitive, creative, facilitative, objective, data-informed

**Responsibilities:**
- Market research and competitive analysis
- Brainstorming and ideation facilitation
- Project brief creation
- Initial project discovery
- Documenting existing projects (brownfield analysis)

**Commands (6 total):**
1. `*brainstorm {topic}` - Facilitate structured brainstorming session
2. `*create-competitor-analysis` - Generate competitor analysis
3. `*create-project-brief` - Create initial project brief
4. `*perform-market-research` - Market research with templates
5. `*research-prompt {topic}` - Generate deep research prompts
6. `*elicit` - Advanced elicitation for requirements gathering

**Skills Used:**
- Advanced elicitation (requirements gathering)
- Brainstorming facilitation
- Competitor analysis generation
- Project brief creation
- Deep research prompt generation

**Unique Value:**
- Persona-driven ideation and discovery
- Structured brainstorming workflows
- Market research templates
- Investigative "why?" questioning style
- Discovery phase focus (before PRD)

**When to Use:**
- At project inception (before PRD creation)
- During market research phase
- For brainstorming and ideation
- Competitive analysis needs
- Brownfield project discovery

**V2 Architecture Requirements:**
- Follow 7-step workflow pattern
- Implement complexity assessment (5 factors, weighted)
- Define 3 routing options (simple/standard/complex)
- Add comprehensive guardrails
- Include full telemetry structures

---

#### Agent 2: John (PM) - Product Manager
**File:** `.claude/agents/john-pm.md`
**Effort:** 5-6 hours

**Persona (from BMAD v4):**
- **Name:** John
- **Title:** Product Manager
- **Icon:** 📋
- **Identity:** Investigative product strategist, market-savvy PM
- **Style:** Analytical, inquisitive, data-driven, user-focused, pragmatic

**Responsibilities:**
- Product strategy and feature prioritization
- PRD creation (greenfield and brownfield)
- Epic creation for brownfield projects
- Stakeholder communication
- Roadmap planning

**Commands (5 total):**
1. `*create-prd` - Create PRD (uses create-prd skill) ⭐ NEW SKILL
2. `*create-brownfield-prd` - Brownfield PRD (uses create-brownfield-prd skill) ⭐ NEW SKILL
3. `*create-brownfield-epic` - Brownfield epic creation
4. `*create-brownfield-story` - Brownfield story from context
5. `*shard-prd` - Break PRD into pieces (uses shard-document skill) ⭐ NEW SKILL

**Skills Used:**
- `create-prd` (NEW - Phase 1)
- `create-brownfield-prd` (NEW - Phase 1)
- `shard-document` (NEW - Phase 1)
- Brownfield epic/story creation (adapt from BMAD v4)

**Unique Value:**
- Product-focused (vs. Alex's task-focused)
- Investigative PM persona ("Why?" questioning)
- Brownfield specialization
- Template-based PRD workflows
- Stakeholder communication style

**When to Use:**
- PRD creation workflows (prefer template-based over Alex)
- Brownfield product planning
- When PM persona matters (stakeholder communication)

**V2 Architecture Requirements:**
- 7-step workflow pattern
- Complexity assessment
- Intelligent routing (simple/standard/complex)
- Guardrails framework
- Complete telemetry

---

#### Agent 3: Sarah (PO) - Product Owner
**File:** `.claude/agents/sarah-po.md`
**Effort:** 4-5 hours

**Persona (from BMAD v4):**
- **Name:** Sarah
- **Title:** Product Owner
- **Icon:** 📝
- **Identity:** Meticulous, quality guardian, process steward
- **Style:** Detail-oriented, systematic, collaborative

**Responsibilities:**
- Backlog management and story refinement
- Story validation (quality checks)
- Acceptance criteria definition
- Sprint planning support
- Process adherence

**Commands (5 total):**
1. `*create-epic` - Create brownfield epic
2. `*create-story` - Create story from requirements
3. `*validate-story-draft` - Validate story quality (uses validate-story skill - already exists)
4. `*shard-doc` - Break documents (uses shard-document skill) ⭐ NEW SKILL
5. `*execute-checklist-po` - PO master checklist (uses interactive-checklist skill) ⭐ NEW SKILL

**Skills Used:**
- `validate-story` (already exists in planning domain)
- `interactive-checklist` (NEW - Phase 1)
- `shard-document` (NEW - Phase 1)
- Brownfield epic/story creation (adapt from BMAD v4)

**Unique Value:**
- Quality guardian persona (meticulous validation)
- Interactive checklist workflows
- Process adherence emphasis
- Backlog grooming specialist
- Autonomous preparation style

**When to Use:**
- Interactive checklist-driven validation (prefer over Alex's automated validation)
- When quality guardian persona needed
- Process adherence emphasis required

**V2 Architecture Requirements:**
- 7-step workflow pattern
- Complexity assessment
- Routing strategies
- Guardrails
- Telemetry

---

#### Agent 4: Bob (SM) - Scrum Master
**File:** `.claude/agents/bob-sm.md`
**Effort:** 3-4 hours

**Persona (from BMAD v4):**
- **Name:** Bob
- **Title:** Scrum Master
- **Icon:** 🏃
- **Identity:** Task-oriented, developer handoff specialist
- **Style:** Efficient, precise, focused on clear developer handoffs

**Responsibilities:**
- Story creation for developer handoff
- Epic management
- Story quality checks (draft checklist)
- Agile process guidance

**Commands (2 total):**
1. `*draft` - Create developer-ready story (uses create-next-story task from BMAD v4)
2. `*story-checklist` - Story draft checklist (uses interactive-checklist skill) ⭐ NEW SKILL

**Skills Used:**
- `interactive-checklist` (NEW - Phase 1)
- `create-next-story` (adapt from BMAD v4 task)

**Unique Value:**
- Developer-focused story creation
- "Crystal-clear stories for dumb AI agents" philosophy
- Story draft checklist workflow
- Simple, focused scope (just story creation)

**When to Use:**
- Developer handoff emphasis
- Story draft checklist workflow
- Simple story creation (minimal overhead)

**V2 Architecture Requirements:**
- 7-step workflow pattern (simplified for 2 commands)
- Complexity assessment
- Routing (likely simpler than other agents)
- Guardrails
- Telemetry

---

#### Agent 5: Sally (UX Expert)
**File:** `.claude/agents/sally-ux-expert.md`
**Effort:** 4-5 hours

**Persona (from BMAD v4):**
- **Name:** Sally
- **Title:** UX Expert
- **Icon:** 🎨
- **Identity:** User experience designer, UI specialist
- **Style:** Empathetic, creative, detail-oriented, user-obsessed

**Responsibilities:**
- UI/UX design and wireframes
- Front-end specifications
- User experience optimization
- Interaction design
- Accessibility

**Commands (2 total):**
1. `*create-front-end-spec` - Create front-end specification
2. `*generate-ui-prompt` - Generate AI UI prompts (for v0, Lovable, etc.)

**Skills Used:**
- `create-doc` (with front-end-spec-tmpl.yaml from BMAD v4)
- `generate-ai-frontend-prompt` (adapt from BMAD v4 task)

**Unique Value:**
- UX/UI specialization
- Front-end specification workflows
- AI UI generation prompt crafting
- User-centric design focus
- Accessibility expertise

**When to Use:**
- UI/UX design phase
- Front-end specification needs
- AI UI generation (v0, Lovable integration)
- Accessibility requirements

**V2 Architecture Requirements:**
- 7-step workflow pattern
- Complexity assessment
- Routing strategies
- Guardrails
- Telemetry

---

## Implementation Guidelines

### Following V2 Architecture Standards

**Essential Reading (in order):**
1. `docs/V2-ARCHITECTURE.md` - Master reference for V2 pattern
2. `docs/ESSENTIAL-DEVELOPMENT-DOCS.md` - List of all essential docs
3. `docs/3-layer-architecture-for-skills.md` - Layer responsibilities
4. `docs/PHASE-2-COMPLETION.md` - Complete examples of all 4 existing subagents
5. `docs/skill-refactoring-template.md` - Skill structure template
6. `docs/standards.md` - Coding and documentation standards
7. `docs/terminology-alignment-claude-code.md` - Correct terminology

### Skill Creation Template (from skill-refactoring-template.md)

**File Structure:**
```
.claude/skills/{domain}/{skill-name}/
├── SKILL.md                    # Main skill file with V2 contract
├── references/
│   ├── process.md              # Detailed process steps
│   ├── examples.md             # Usage examples
│   ├── templates.md            # Document templates
│   └── troubleshooting.md      # Common issues
└── assets/                     # (if needed)
    └── diagrams/
```

**YAML Frontmatter (V2 Contract):**
```yaml
---
name: skill-name
description: One-line description of what this skill does

acceptance:
  - Clear acceptance criterion 1
  - Clear acceptance criterion 2
  - Clear acceptance criterion 3

inputs:
  - name: input1
    description: Description of input
    required: true
  - name: input2
    description: Description of optional input
    required: false

outputs:
  - name: output1
    description: Description of output
    location: path/to/output
  - name: output2
    description: Description of second output
    location: path/to/output2

telemetry:
  - event: skill_started
    data: [skill_name, inputs]
  - event: step_completed
    data: [step_name, duration, status]
  - event: skill_completed
    data: [skill_name, duration, outputs, success]
---
```

### Subagent Creation Template (from V2-ARCHITECTURE.md)

**File Structure:**
```
.claude/agents/{name}.md
```

**YAML Frontmatter:**
```yaml
---
name: agent-name
version: 2.0
description: One-line description of agent role
persona:
  name: Full Name
  title: Job Title
  icon: 🎭
  style: Personality traits
responsibilities:
  - Responsibility 1
  - Responsibility 2
commands:
  - name: "*command-name"
    skill: skill-name
    complexity: Low-Medium
    duration: 5-15 minutes
---
```

**7-Step Workflow Pattern (All Commands Must Follow):**
```markdown
## Workflow Pattern

### Step 1: Load Context
- Load task specification
- Read project configuration
- Initialize workspace

### Step 2: Assess Complexity
- Evaluate 5 complexity factors (weighted 0-100 scale)
- Calculate total complexity score
- Determine if task is within capability

### Step 3: Route Strategy
- Simple (0-30): Direct execution, minimal validation
- Standard (31-70): Balanced approach, standard guardrails
- Complex (71-100): Thorough analysis, comprehensive checks

### Step 4: Check Guardrails
- Verify preconditions met
- Check quality standards
- Validate inputs

### Step 5: Execute
- Perform core task operation
- Track progress with substeps
- Handle errors gracefully

### Step 6: Verify Results
- Validate outputs meet acceptance criteria
- Run quality checks
- Verify all requirements satisfied

### Step 7: Emit Telemetry
- Record execution metrics
- Log decisions and rationale
- Track outcomes for learning
```

**Complexity Assessment (5 Factors):**
```markdown
## Complexity Factors

Each factor scored 0-20, total 0-100:

1. **Domain Familiarity** (0-20)
   - 0: Well-known domain with established patterns
   - 10: Some new concepts, mostly familiar
   - 20: Unknown domain, no established patterns

2. **Scope Size** (0-20)
   - 0: Single file, <100 LOC
   - 10: Few files, 100-500 LOC
   - 20: Many files, >500 LOC

3. **Technical Risk** (0-20)
   - 0: Low risk, well-tested approach
   - 10: Moderate risk, needs validation
   - 20: High risk, critical system impact

4. **Dependency Complexity** (0-20)
   - 0: No external dependencies
   - 10: Few well-documented dependencies
   - 20: Many or poorly documented dependencies

5. **Testing Gaps** (0-20)
   - 0: Comprehensive test coverage
   - 10: Partial test coverage
   - 20: No existing tests
```

**Guardrails Framework:**
```markdown
## Guardrails

### Precondition Guardrails
- [ ] Required inputs provided
- [ ] Context loaded successfully
- [ ] Prerequisites met

### Execution Guardrails
- [ ] Complexity within acceptable range
- [ ] Quality standards maintained
- [ ] No security violations

### Postcondition Guardrails
- [ ] Outputs meet acceptance criteria
- [ ] Quality gates passed
- [ ] Telemetry recorded
```

---

## Success Criteria

### For Skills
- ✅ YAML frontmatter with complete V2 contract
- ✅ Progressive disclosure (SKILL.md → references/)
- ✅ Integration with bmad-commands primitives where applicable
- ✅ Clear acceptance criteria
- ✅ Telemetry emission points documented
- ✅ Follows skill-refactoring-template.md structure
- ✅ Grade A compliance (portable, no hardcoded paths)

### For Subagents
- ✅ YAML frontmatter with persona and commands
- ✅ 7-step workflow pattern for all commands
- ✅ Complexity assessment (5 factors, 0-100 scale)
- ✅ 3 routing strategies (simple/standard/complex)
- ✅ Comprehensive guardrails framework
- ✅ Complete telemetry structures
- ✅ Follows V2-ARCHITECTURE.md patterns
- ✅ Integration examples and usage documentation

### For Overall Implementation
- ✅ All 4 skills created to Grade A standard
- ✅ All 5 agents created following V2 architecture
- ✅ Skills properly referenced in subagent command definitions
- ✅ Documentation updated (skill count, agent count)
- ✅ Integration testing complete
- ✅ All files follow standards.md requirements
- ✅ Terminology consistent with terminology-alignment-claude-code.md

---

## Testing Strategy

### Skill Testing
1. **Acceptance Criteria:** Verify all acceptance criteria met
2. **Input Validation:** Test with valid and invalid inputs
3. **Output Validation:** Verify outputs created in correct locations
4. **Telemetry:** Confirm telemetry events emitted
5. **Integration:** Test skill used by subagent command

### Subagent Testing
1. **Workflow:** Execute complete 7-step workflow
2. **Complexity Assessment:** Test all 5 factors
3. **Routing:** Test simple, standard, and complex paths
4. **Guardrails:** Test precondition, execution, postcondition checks
5. **Commands:** Test all commands with realistic inputs

### Integration Testing
1. **End-to-End:** Test complete workflow from Mary → John → Alex → James → Quinn
2. **Cross-Agent:** Test handoffs between agents
3. **Skills Integration:** Verify skills work across multiple agents
4. **Real Project:** Test on a real brownfield project

---

## Deliverables Checklist

### Skills (4 total)
- [ ] `create-prd` skill created in `.claude/skills/planning/create-prd/`
- [ ] `create-brownfield-prd` skill created in `.claude/skills/planning/create-brownfield-prd/`
- [ ] `shard-document` skill created in `.claude/skills/planning/shard-document/`
- [ ] `interactive-checklist` skill created in `.claude/skills/planning/interactive-checklist/`

### Subagents (5 total)
- [ ] Mary (Analyst) created in `.claude/agents/mary-analyst.md`
- [ ] John (PM) created in `.claude/agents/john-pm.md`
- [ ] Sarah (PO) created in `.claude/agents/sarah-po.md`
- [ ] Bob (SM) created in `.claude/agents/bob-sm.md`
- [ ] Sally (UX Expert) created in `.claude/agents/sally-ux-expert.md`

### Documentation Updates
- [ ] Update `docs/ROADMAP.md` skill count (17 → 21)
- [ ] Update `docs/ROADMAP.md` agent count (4 → 9)
- [ ] Update `docs/V2-ARCHITECTURE.md` with new agents and skills
- [ ] Update `docs/DOCUMENTATION-INDEX.md` with new files
- [ ] Create quick start guides for new agents (5 files)
- [ ] Update `README.md` with new agent personas

### Testing Documentation
- [ ] Create test report for new skills
- [ ] Create test report for new agents
- [ ] Document integration test results
- [ ] Create brownfield project test case

---

## Execution Strategy

### Recommended Approach: Incremental Development

**Session 13 (This Session): Phase 1 - Skills Creation**
- Focus: Create all 4 planning skills
- Duration: ~20-26 hours (can be split across multiple sessions)
- Order:
  1. `create-prd` (most important, used by John)
  2. `create-brownfield-prd` (brownfield workflows)
  3. `shard-document` (used by John and Sarah)
  4. `interactive-checklist` (used by Sarah and Bob)

**Session 14-15: Phase 2 - Agent Creation (Part 1)**
- Focus: Create John, Sarah, Bob (planning/agile focused)
- Duration: ~12-15 hours
- These 3 agents work closely together in planning workflows

**Session 16: Phase 2 - Agent Creation (Part 2)**
- Focus: Create Mary, Sally (discovery/UX focused)
- Duration: ~10-13 hours
- These 2 agents are used earlier in the process (discovery/design)

**Session 17: Integration & Testing**
- Focus: End-to-end testing, brownfield project testing
- Duration: ~8-10 hours
- Create integration documentation and test reports

### Alternative Approach: Complete Agent-by-Agent

Create each agent with its required skills in sequence:
1. John + `create-prd` + `create-brownfield-prd` + `shard-document`
2. Sarah + `interactive-checklist`
3. Bob (reuses Sarah's `interactive-checklist`)
4. Mary (discovery workflows)
5. Sally (UX workflows)

---

## Important Notes

### Reusing Existing Components

**Skills that already exist (don't recreate):**
- `validate-story` - Used by Sarah's `*validate-story-draft`
- `document-project` - Used by `create-brownfield-prd` internally
- All other 17 existing skills

**Primitives available in bmad-commands:**
- File operations: `read_file.py`, `write_file.py`, `edit_file.py`
- Test operations: `run_tests.py`, `analyze_test_results.py`
- Architecture: `generate_architecture_diagram.py`, `analyze_tech_stack.py`
- Code analysis: Various analysis primitives

### BMAD v4 Reference Materials

The original BMAD Method v4 has these components we're adapting:
- Agent personas with distinct personalities
- Template-based workflows (YAML templates)
- Task-based skill system
- Checklist-driven validation

**Migration Strategy:**
- Keep personas and personalities intact
- Convert YAML templates to markdown with progressive disclosure
- Adapt tasks to Claude Code skills with V2 contracts
- Maintain checklist workflows but make them interactive

### Quality Standards

From `docs/standards.md`:
- **Code:** Follow project conventions, no hardcoded paths
- **Documentation:** Clear, concise, comprehensive
- **Testing:** All features must be testable and tested
- **Telemetry:** All operations emit telemetry
- **Error Handling:** Graceful failure with remediation guidance

---

## Key References

### Must-Read Documentation
1. **docs/V2-ARCHITECTURE.md** ⭐ MASTER REFERENCE
2. **docs/ESSENTIAL-DEVELOPMENT-DOCS.md** - All essential docs list
3. **docs/ROADMAP.md** - Phase 3 (Week 7-9) section for agent details
4. **docs/PHASE-2-COMPLETION.md** - Complete examples of existing 4 agents
5. **docs/skill-refactoring-template.md** - Skill creation template
6. **docs/3-layer-architecture-for-skills.md** - Architecture principles

### Existing Examples to Follow
- **Best Skill Example:** `.claude/skills/development/implement-feature/SKILL.md`
- **Best Subagent Example:** `.claude/agents/james-developer-v2.md`
- **Complex Workflow Example:** `.claude/agents/orchestrator-v2.md`

### Standards & Compliance
- **docs/standards.md** - Quality requirements
- **docs/terminology-alignment-claude-code.md** - Terminology standards
- **docs/architecture-claude-code-compliance.md** - Claude Code alignment

---

## Expected Outcomes

After completing this work, BMAD Enhanced will have:

### Complete Agent Coverage (9 total)
- **Discovery:** Mary (Analyst)
- **Product:** John (PM), Sarah (PO)
- **Agile:** Bob (SM)
- **Design:** Sally (UX Expert)
- **Planning:** Alex (existing)
- **Architecture:** Winston (existing, from Phase 2.5)
- **Development:** James (existing)
- **Quality:** Quinn (existing)
- **Orchestration:** Orchestrator (existing)

### Complete Skill Coverage (21 total)
- **Planning (8):** create-prd ⭐, create-brownfield-prd ⭐, shard-document ⭐, interactive-checklist ⭐, create-task-spec, breakdown-epic, estimate-stories, refine-story
- **Development (3):** implement-feature, fix-issue, run-tests
- **Quality (7):** review-task, quality-gate, nfr-assess, trace-requirements, risk-profile, test-design, refactor-code
- **Implementation (1):** execute-task
- **Brownfield (2):** document-project, index-docs

### Workflow Parity with BMAD v4
- ✅ Complete discovery phase (Mary)
- ✅ Complete planning phase (John, Sarah, Alex, Winston)
- ✅ Complete agile workflow (Bob, James, Quinn)
- ✅ Complete UX workflow (Sally)
- ✅ All BMAD v4 agent capabilities preserved
- ✅ Enhanced with V2 architecture benefits

---

## Session Start Checklist

Before beginning development, verify:

- [ ] Read `docs/V2-ARCHITECTURE.md` completely
- [ ] Review `docs/ESSENTIAL-DEVELOPMENT-DOCS.md`
- [ ] Review `docs/ROADMAP.md` Phase 3 (Week 7-9)
- [ ] Examine existing skill example: `.claude/skills/development/implement-feature/SKILL.md`
- [ ] Examine existing agent example: `.claude/agents/james-developer-v2.md`
- [ ] Understand 7-step workflow pattern
- [ ] Understand complexity assessment (5 factors)
- [ ] Understand V2 contract requirements (acceptance, inputs, outputs, telemetry)
- [ ] Understand progressive disclosure pattern (SKILL.md → references/)

---

## Questions to Answer During Development

1. **For each skill:**
   - What are the clear acceptance criteria?
   - What inputs are required vs optional?
   - What outputs are created and where?
   - What telemetry events should be emitted?
   - What references are needed (process, examples, templates)?

2. **For each agent:**
   - What is the agent's unique value proposition?
   - When should users choose this agent over Alex?
   - What are the complexity factors for each command?
   - What guardrails are needed?
   - How does this agent hand off to other agents?

3. **For integration:**
   - How do the new agents fit into existing workflows?
   - What are the common workflow paths?
   - How do the new skills integrate with existing skills?
   - What documentation do users need?

---

## Ready to Start!

You now have complete context for implementing Phase 4: Missing BMAD Agents.

**Recommended First Step:**
Start with Phase 1, Skill 1: `create-prd`

This is the highest-priority skill that will be used by John (PM) and provides the most value immediately.

**Development Process:**
1. Read V2-ARCHITECTURE.md and skill-refactoring-template.md
2. Create YAML frontmatter with V2 contract
3. Write SKILL.md with progressive disclosure
4. Create references/ subdirectory with process, examples, templates
5. Test the skill manually
6. Document testing results
7. Move to next skill

**Track Progress:**
Use the TodoWrite tool to track completion of:
- 4 skills (Phase 1)
- 5 agents (Phase 2)
- Documentation updates
- Testing and validation

Good luck! This is an exciting phase that will complete BMAD Enhanced's workflow parity with BMAD v4 while adding all the V2 architecture benefits. 🚀

---

**Session 13 Kickoff Prompt**
**Created:** 2025-11-04
**Version:** 1.0
**Status:** Ready for Development
**Estimated Total Effort:** 42-54 hours (can be split across multiple sessions)
