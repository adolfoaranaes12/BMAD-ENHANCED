# Phase 2 & 3 Implementation Plan

**Date:** January 31, 2025
**Status:** 🚧 **IN PROGRESS**
**Estimated Duration:** 4-6 weeks total (Phase 2: 2-3 weeks, Phase 3: 2-3 weeks)

---

## Overview

Building on Phase 1's success (james-developer-v2 with 5 commands), Phase 2 will upgrade remaining subagents to V2 architecture, and Phase 3 will add story-based workflow support.

---

## Phase 2: Upgrade Remaining Subagents (2-3 weeks)

### Objectives

1. Upgrade alex-planner to V2 with intelligent routing and guardrails
2. Upgrade quinn-quality to V2 with intelligent routing and guardrails
3. Upgrade orchestrator to V2 with cross-subagent routing
4. Add *debug and *explain commands to james-developer-v2
5. Add V2 contracts to all planning and quality skills

### 2.1: alex-planner V2 (1 week)

**Current State:**
- Basic planning agent
- No complexity assessment
- No intelligent routing
- Limited guardrails
- No telemetry

**Target V2 Features:**
- Intelligent routing based on planning complexity
- Comprehensive guardrails (scope, timeline, dependencies)
- Automated verification of planning outputs
- Full telemetry for all commands
- Automated escalation paths

**Commands to Implement/Upgrade:**

1. **`*create-task-spec`** ⭐ High Priority
   - Purpose: Create task specifications from user requirements
   - Complexity factors: Requirements clarity (30%), Dependencies (25%), Scope size (20%), Technical risk (15%), Time constraints (10%)
   - Routes: Simple spec (≤30), Standard spec (31-60), Complex spec (>60)
   - Skills: create-task-spec
   - Guardrails: Clear acceptance criteria, feasible scope, dependencies identified

2. **`*breakdown-epic`** ⭐ High Priority
   - Purpose: Break down large epics into manageable tasks
   - Complexity factors: Epic size (30%), Dependencies (25%), Team size (20%), Timeline (15%), Uncertainty (10%)
   - Routes: Small epic (≤30), Medium epic (31-60), Large epic (>60)
   - Skills: breakdown-epic
   - Guardrails: Max 10 tasks per epic, clear dependencies, realistic estimates

3. **`*estimate-story`** ⭐ Medium Priority
   - Purpose: Estimate effort for stories/tasks
   - Complexity factors: Story complexity (30%), Dependencies (25%), Team experience (20%), Risk (15%), Uncertainty (10%)
   - Routes: Simple estimation (≤30), Standard estimation (31-60), Complex estimation (>60)
   - Skills: estimate-stories
   - Guardrails: Estimate ranges, confidence levels, risk factors

4. **`*refine-story`** ⭐ Medium Priority
   - Purpose: Refine and improve story specifications
   - Complexity factors: Story clarity (30%), Acceptance criteria (25%), Dependencies (20%), Technical details (15%), NFRs (10%)
   - Routes: Minor refinement (≤30), Standard refinement (31-60), Major refinement (>60)
   - Skills: refine-story
   - Guardrails: Maintain intent, improve clarity, add missing details

5. **`*plan-sprint`** ⭐ Low Priority
   - Purpose: Plan sprint with capacity and velocity
   - Complexity factors: Team size (30%), Story count (25%), Dependencies (20%), Capacity (15%), Velocity (10%)
   - Routes: Small sprint (≤30), Standard sprint (31-60), Large sprint (>60)
   - Skills: sprint-plan
   - Guardrails: Capacity limits, velocity trends, dependency management

**Deliverables:**
- alex-planner.md upgraded to V2 (estimated 1,500-2,000 lines)
- 5 commands with 7-step workflow
- Complexity assessment for each command
- Comprehensive guardrails
- Full telemetry structures

**Estimated Effort:** 8-10 hours

---

### 2.2: quinn-quality V2 (1 week)

**Current State:**
- Basic quality agent
- No complexity assessment
- No intelligent routing
- Limited guardrails
- No telemetry

**Target V2 Features:**
- Intelligent routing based on quality assessment complexity
- Comprehensive guardrails (quality thresholds, coverage requirements)
- Automated quality gate decisions
- Full telemetry for all commands
- Risk-based prioritization

**Commands to Implement/Upgrade:**

1. **`*review`** ⭐ High Priority
   - Purpose: Comprehensive quality review (code quality + NFRs + gate decision)
   - Complexity factors: Files to review (30%), Quality issues (25%), NFR requirements (20%), Test coverage (15%), Codebase size (10%)
   - Routes: Simple review (≤30), Standard review (31-60), Comprehensive review (>60)
   - Skills: review-task → nfr-assess → refactor-code → quality-gate
   - Guardrails: Min coverage thresholds, quality score requirements, NFR compliance

2. **`*assess-nfr`** ⭐ Medium Priority
   - Purpose: Assess non-functional requirements (performance, security, scalability)
   - Complexity factors: NFR count (30%), System complexity (25%), Impact (20%), Test requirements (15%), Documentation (10%)
   - Routes: Simple assessment (≤30), Standard assessment (31-60), Comprehensive assessment (>60)
   - Skills: nfr-assess
   - Guardrails: All NFRs addressed, test plans for P0/P1, risk identification

3. **`*validate-quality-gate`** ⭐ High Priority
   - Purpose: Make quality gate decision (PASS/CONCERNS/FAIL/WAIVED)
   - Complexity factors: Issue severity (30%), NFR failures (25%), Coverage gaps (20%), Technical debt (15%), Risk (10%)
   - Routes: Clear pass/fail (≤30), Borderline (31-60), Complex decision (>60)
   - Skills: quality-gate
   - Guardrails: Objective criteria, waiver justification, escalation for FAIL

4. **`*trace-requirements`** ⭐ Low Priority
   - Purpose: Trace requirements to implementation and tests
   - Complexity factors: Requirement count (30%), Implementation complexity (25%), Test coverage (20%), Documentation (15%), Traceability gaps (10%)
   - Routes: Simple tracing (≤30), Standard tracing (31-60), Complex tracing (>60)
   - Skills: trace-requirements
   - Guardrails: All requirements traced, gaps identified, coverage verified

5. **`*assess-risk`** ⭐ Low Priority
   - Purpose: Assess technical and business risks
   - Complexity factors: Risk count (30%), Impact (25%), Likelihood (20%), Mitigation complexity (15%), Dependencies (10%)
   - Routes: Low risk (≤30), Medium risk (31-60), High risk (>60)
   - Skills: risk-profile
   - Guardrails: All risks identified, mitigation plans, escalation for high risks

**Deliverables:**
- quinn-quality.md upgraded to V2 (estimated 1,500-2,000 lines)
- 5 commands with 7-step workflow
- Complexity assessment for each command
- Quality gate automation
- Full telemetry structures

**Estimated Effort:** 8-10 hours

---

### 2.3: orchestrator V2 (3-4 days)

**Current State:**
- Basic orchestration logic
- No complexity assessment
- No cross-subagent routing
- No guardrails
- No telemetry

**Target V2 Features:**
- Intelligent cross-subagent routing
- Workflow orchestration (plan → implement → review)
- Guardrails for cross-subagent operations
- Full telemetry for orchestration
- Automated workflow management

**Commands to Implement/Upgrade:**

1. **`*workflow`** ⭐ High Priority
   - Purpose: Execute complete workflow (plan → implement → review)
   - Complexity factors: Workflow stages (30%), Dependencies (25%), Team involvement (20%), Timeline (15%), Risk (10%)
   - Routes: Simple workflow (≤30), Standard workflow (31-60), Complex workflow (>60)
   - Subagents: alex-planner → james-developer-v2 → quinn-quality
   - Guardrails: Stage completion, quality gates, timeline adherence

2. **`*coordinate`** ⭐ Medium Priority
   - Purpose: Coordinate multiple subagents for cross-cutting concerns
   - Complexity factors: Subagent count (30%), Coordination points (25%), Dependencies (20%), Timeline (15%), Risk (10%)
   - Routes: Simple coordination (≤30), Standard coordination (31-60), Complex coordination (>60)
   - Guardrails: Clear handoffs, state management, conflict resolution

**Deliverables:**
- orchestrator.md upgraded to V2 (estimated 800-1,000 lines)
- 2 commands with cross-subagent routing
- Workflow state management
- Full telemetry structures

**Estimated Effort:** 6-8 hours

---

### 2.4: james-developer-v2 Additional Commands (3-4 days)

**Commands to Add:**

1. **`*debug`** ⭐ High Priority
   - Purpose: Interactive debugging workflow with systematic investigation
   - Complexity factors: Error clarity (30%), Reproduction (25%), System complexity (20%), Logs available (15%), Impact (10%)
   - Routes: Clear error (≤30), Investigation needed (31-60), Deep debugging (>60)
   - Skills: TBD (may need new debug skill)
   - Guardrails: Systematic investigation, hypothesis testing, documentation

2. **`*explain`** ⭐ Medium Priority
   - Purpose: Explain code functionality and generate documentation
   - Complexity factors: Code complexity (30%), Documentation needs (25%), Audience (20%), Scope (15%), Examples needed (10%)
   - Routes: Simple explanation (≤30), Standard documentation (31-60), Comprehensive docs (>60)
   - Skills: TBD (may need new explain skill)
   - Guardrails: Accuracy, clarity, completeness

**Deliverables:**
- 2 new commands in james-developer-v2.md (~800 lines)
- Full 7-step workflow for each
- Complexity assessment and routing
- Guardrails and telemetry

**Estimated Effort:** 6-8 hours

---

### 2.5: V2 Contracts for Planning and Quality Skills (1-2 days)

**Planning Skills (8 skills):**
- create-task-spec, breakdown-epic, refine-story, estimate-stories
- document-project, sprint-plan, create-architecture, validate-story

**Quality Skills (8 skills):**
- review-task, refactor-code, quality-gate, nfr-assess
- trace-requirements, risk-profile, test-design, validate-architecture, architecture-review

**For each skill, add:**
- Acceptance criteria (3-6 criteria)
- Inputs (required and optional parameters)
- Outputs (expected results)
- Telemetry (metrics to track)

**Estimated Effort:** 8-12 hours (30-60 minutes per skill)

---

## Phase 2 Summary

**Total Estimated Effort:** 40-50 hours (1-2 weeks at 20-25 hours/week)

**Deliverables:**
- 3 upgraded subagents (alex-planner, quinn-quality, orchestrator)
- 12 new/upgraded commands with V2 architecture
- 2 additional james-developer-v2 commands
- 16 skills with V2 contracts
- ~4,500-5,500 lines of specification

**Success Metrics:**
- All subagents follow V2 pattern
- All commands have intelligent routing
- All commands have comprehensive guardrails
- All commands emit telemetry
- All skills have V2 contracts

---

## Phase 3: Story-Based Workflow (2-3 weeks)

### 3.1: Workflow Decision (Day 1)

**Decision Point:** Task-centric vs Story-based vs Hybrid

**Option A: Task-Centric (Current)** ✅ Simpler
- Tasks are primary unit of work
- Stories can be modeled as collections of tasks
- Less overhead, more flexible
- Already working

**Option B: Story-Based** ⚠️ More complex
- Stories are primary unit with structured workflow
- Dev Agent Record sections (Status, Context, Implementation, QA)
- More aligned with REFERENCE implementation
- More ceremony, more structure

**Option C: Hybrid** 🤔 Balanced
- Support both workflows
- Tasks for simple work
- Stories for complex features with multiple tasks
- Best of both worlds, more to maintain

**Recommendation:** Start with Hybrid approach
- Keep existing task-centric workflow
- Add story-management skill for complex features
- Let users choose based on needs

---

### 3.2: Story Management Skill (1 week)

**If implementing story-based workflow:**

**Skill:** `story-management`
**Location:** `.claude/skills/planning/story-management/`

**Capabilities:**
1. Create story files with structured sections
2. Manage Dev Agent Record
3. Track story workflow (Draft → Approved → InProgress → Review → Done)
4. Coordinate multiple tasks within story
5. Maintain QA gate integration
6. Update story status based on task progress

**Story File Structure:**
```markdown
# Story: [Title]

## Status
**Current:** InProgress
**Created:** 2025-01-31
**Last Updated:** 2025-01-31

## Objective
[What this story aims to achieve]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Tasks
- [ ] task-001: [Description] (Status: Pending)
- [x] task-002: [Description] (Status: Complete)

## Dev Agent Record

### Context Analysis
[Analysis of requirements and constraints]

### Implementation Record
[Files modified, approach taken]

### QA Review
[Quality gate results, issues found/fixed]

## Notes
[Additional context, decisions, learnings]
```

**Commands Needed:**

1. **`*create-story`**
   - Create new story file from requirements
   - Initialize all sections
   - Link to tasks

2. **`*update-story`**
   - Update story status
   - Add implementation notes
   - Update task status

3. **`*link-tasks`**
   - Link tasks to story
   - Track task dependencies
   - Update story progress

**Integration Points:**
- alex-planner: Create stories, link tasks
- james-developer-v2: Update implementation record
- quinn-quality: Update QA review section
- orchestrator: Manage story workflow

**Estimated Effort:** 10-12 hours

---

### 3.3: Orchestrator Story Workflow (3-4 days)

**Add story workflow orchestration to orchestrator:**

**`*story-workflow` command:**
- Purpose: Execute complete story workflow
- Stages: Create → Plan tasks → Implement tasks → Review → Complete
- Coordinates: alex-planner, james-developer-v2, quinn-quality
- Guardrails: Story status progression, all tasks complete, quality gates pass

**Estimated Effort:** 6-8 hours

---

### 3.4: Integration and Testing (3-4 days)

**Integration work:**
1. Update subagents to support both task and story workflows
2. Add story-awareness to james-developer-v2 commands
3. Update quality gate to support stories
4. Test story → tasks → implementation → review flow

**Testing:**
1. Create test story
2. Break down into tasks
3. Implement tasks
4. Run quality reviews
5. Complete story
6. Validate all sections updated correctly

**Estimated Effort:** 6-8 hours

---

## Phase 3 Summary

**Total Estimated Effort:** 22-28 hours (1-1.5 weeks at 20 hours/week)

**Deliverables:**
- story-management skill
- Orchestrator story workflow
- Story file templates
- Integration with existing subagents
- Documentation and guides

**Success Metrics:**
- Stories can be created and managed
- Tasks can be linked to stories
- Story workflow executes end-to-end
- All sections automatically updated
- Works alongside task-centric workflow

---

## Overall Timeline

**Phase 2:** 2-3 weeks (40-50 hours)
- Week 1: alex-planner V2
- Week 2: quinn-quality V2
- Week 3: orchestrator V2 + james commands + skill contracts

**Phase 3:** 2-3 weeks (22-28 hours)
- Week 1: Story management skill + orchestrator story workflow
- Week 2: Integration and testing

**Total:** 4-6 weeks (62-78 hours)

---

## Success Criteria

### Phase 2 Complete When:
- [ ] alex-planner has 5 V2 commands
- [ ] quinn-quality has 5 V2 commands
- [ ] orchestrator has 2 V2 commands
- [ ] james-developer-v2 has 7 commands total
- [ ] All 16 skills have V2 contracts
- [ ] All commands have complexity assessment, routing, guardrails, telemetry
- [ ] Documentation complete

### Phase 3 Complete When:
- [ ] story-management skill implemented
- [ ] Orchestrator story workflow functional
- [ ] Story → tasks → implementation flow works
- [ ] All Dev Agent Record sections auto-update
- [ ] Both task and story workflows supported
- [ ] Documentation and examples complete

### Overall Success:
- [ ] All subagents follow V2 architecture
- [ ] 100% of workflow commands have intelligent routing
- [ ] Full observability with telemetry
- [ ] Story-based workflow option available
- [ ] Zero regressions from user perspective
- [ ] Production-ready for real-world use

---

**Plan Status:** 🚧 **READY TO START**
**Next Step:** Read and analyze alex-planner current implementation
**Document Version:** 1.0
**Last Updated:** January 31, 2025
