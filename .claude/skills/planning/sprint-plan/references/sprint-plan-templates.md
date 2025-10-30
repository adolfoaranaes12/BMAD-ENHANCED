# Sprint Plan Document Templates

## Purpose

Standard templates for generating sprint plan documents with comprehensive information for team review and execution.

---

## Basic Sprint Plan Template

**File:** `.claude/sprints/sprint-{number}-plan-{date}.md`

```markdown
# Sprint {number} Plan

**Sprint Duration:** {start_date} to {end_date} ({duration} weeks)
**Team Velocity:** {velocity} points
**Sprint Capacity:** {capacity} points ({buffer}% buffer reserved)
**Team Size:** {team_size} developers

---

## Sprint Goal

{Auto-generated based on committed stories, or user-defined}

Example: "Implement core authentication system allowing users to sign up, log in, and manage their profiles securely."

---

## Stories Committed

### {story-id}: {story-title}
- **Points:** {points}
- **Priority:** {priority}
- **Dependencies:** {dependencies or "None"}
- **Risk:** {risk_level} ({risk_score}/10)
- **Assignee:** TBD

{Repeat for each story}

---

## Capacity Summary

- **Total Points:** {total_points}
- **Utilization:** {utilization}% ({status})
- **Buffer Remaining:** {buffer_points} points
- **Story Count:** {story_count} stories

**By Priority:**
- P0: {p0_points} points ({p0_percentage}%)
- P1: {p1_points} points ({p1_percentage}%)
- P2: {p2_points} points ({p2_percentage}%)

**By Epic:**
- {epic_name}: {epic_points} points ({epic_percentage}%)
{Repeat for each epic}

---

## Risk Assessment

**Overall Risk Score:** {overall_risk}/10 ({risk_interpretation})

**High-Risk Stories:**
- {story_id} ({story_title}) - {risk_score}/10 risk ({risk_reason})
{Repeat for high-risk stories, or "None" if all low/medium risk}

**Mitigation:**
- {mitigation_strategy_1}
- {mitigation_strategy_2}

---

## Dependencies

**Dependency Chain:**
{Visualize dependency relationships}

**External Dependencies:**
- {external_dependency_1}
{Or "None" if no external dependencies}

---

## Notes

{Any additional context, concerns, or team agreements}

---

**Generated:** {date} by sprint-plan skill
```

---

## Multi-Sprint Roadmap Template

**File:** `.claude/sprints/roadmap-{start_sprint}-to-{end_sprint}-{date}.md`

```markdown
# Sprint Roadmap: Sprint {start} to Sprint {end}

**Planning Date:** {date}
**Team Velocity:** {velocity} points per sprint
**Total Capacity:** {total_capacity} points over {sprint_count} sprints

---

## Sprint {number} ({start_date} to {end_date})

**Capacity:** {capacity} points
**Theme:** {theme_description}

**Stories:**
- {story-id}: {story-title} ({points} pts, {priority})
- {story-id}: {story-title} ({points} pts, {priority})
{...}

**Milestones:**
- {milestone_1}

---

{Repeat for each sprint}

---

## Summary

**Total Sprints:** {sprint_count}
**Total Points Planned:** {total_points}
**Stories Planned:** {story_count}
**Stories Deferred:** {deferred_count} ({deferred_points} points)

**Epic Completion:**
- {epic_name}: Sprint {sprint_number} ✓
- {epic_name}: Sprint {sprint_number} - Sprint {sprint_number} (partial)
{...}

---

## Risks and Assumptions

**Assumptions:**
- Velocity remains stable at {velocity} points
- No major scope changes
- Team capacity stable (no extended leave)

**Risks:**
- {risk_1}
- {risk_2}

---

**Generated:** {date} by sprint-plan skill
```

---

## Compact Sprint Plan Template

**Use Case:** Quick reference, status displays

```markdown
# Sprint {number} - Quick View

**Dates:** {start_date} - {end_date}
**Capacity:** {committed}/{capacity} points ({utilization}%)

## Committed Stories

| ID | Title | Points | Priority | Assignee |
|----|-------|--------|----------|----------|
| {story-id} | {title} | {pts} | {priority} | TBD |
{...}

## Status
- Risk: {risk_score}/10
- Dependencies: {dependency_count} ({satisfied} satisfied)
- Feasibility: {feasibility_status}
```

---

## Sprint Plan with Team Assignments Template

**Use Case:** After sprint planning meeting with team

```markdown
# Sprint {number} Plan

{Standard header...}

---

## Stories Committed

### {story-id}: {story-title}
- **Points:** {points}
- **Priority:** {priority}
- **Assignee:** {developer_name}
- **Estimated Hours:** {hours} hours
- **Skills Required:** {skills}
- **Dependencies:** {dependencies}
- **Acceptance Criteria:**
  - AC-1: {criterion_1}
  - AC-2: {criterion_2}
  - {...}

{Repeat for each story}

---

## Team Workload

### {Developer Name}
- **Total Points:** {points}
- **Estimated Hours:** {hours} hours
- **Stories:**
  - {story-id} ({points} pts)
  - {story-id} ({points} pts)
- **Workload:** {percentage}% of capacity

{Repeat for each developer}

---

## Daily Standup Schedule

**Time:** {time}
**Location:** {location/video_link}

**Format:**
1. What did I complete yesterday?
2. What will I work on today?
3. Any blockers?

---

## Definition of Done

- [ ] Code written and reviewed
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Acceptance criteria met
- [ ] Documentation updated
- [ ] Code merged to main branch
- [ ] Deployed to staging environment

---

{Rest of standard template...}
```

---

## Sprint Plan with Test Strategy Template

**Use Case:** Quality-focused teams

```markdown
# Sprint {number} Plan

{Standard header...}

---

## Test Strategy

### Unit Testing
- **Target Coverage:** {coverage}%
- **Frameworks:** {frameworks}
- **Owner:** {test_lead}

### Integration Testing
- **Test Scenarios:** {scenario_count}
- **Critical Paths:** {path_count}
- **Test Environment:** {environment}

### Acceptance Testing
- **Acceptance Criteria:** {total_ac_count} across {story_count} stories
- **Testing Approach:** {manual/automated/mixed}
- **Sign-off Required:** {stakeholder}

### Performance Testing
- **Performance Stories:** {story_count}
- **Performance Targets:**
  - Response time: {target}
  - Throughput: {target}
  - Concurrency: {target}

### Security Testing
- **Security Review Required:** {yes/no}
- **Security Stories:** {story_count}
- **Penetration Testing:** {scheduled/not_scheduled}

---

{Rest of standard template...}
```

---

## Sprint Plan with Burndown Tracking Template

**Use Case:** Teams tracking daily progress

```markdown
# Sprint {number} Plan

{Standard header...}

---

## Burndown Chart Data

**Ideal Burndown:**
| Day | Remaining Points (Ideal) |
|-----|--------------------------|
| Day 0 | {capacity} |
| Day 1 | {capacity - daily_burn} |
| Day 2 | {capacity - 2*daily_burn} |
| ... | ... |
| Day {duration} | 0 |

**Actual Burndown:**
| Day | Remaining Points | Completed Today | Notes |
|-----|------------------|-----------------|-------|
| Day 0 | {capacity} | 0 | Sprint starts |
| Day 1 | - | - | {To be updated daily} |

---

## Story Status Tracking

| Story ID | Title | Points | Status | % Complete | Blocker |
|----------|-------|--------|--------|------------|---------|
| {story-id} | {title} | {pts} | In Progress | 30% | None |
| {story-id} | {title} | {pts} | To Do | 0% | - |

**Status Legend:**
- To Do: Not started
- In Progress: Work begun
- In Review: Code review or testing
- Done: Meets definition of done

---

{Rest of standard template...}
```

---

## Sprint Plan with Risk Register Template

**Use Case:** High-risk or complex sprints

```markdown
# Sprint {number} Plan

{Standard header...}

---

## Risk Register

| ID | Risk | Probability | Impact | Score | Mitigation | Owner |
|----|------|-------------|--------|-------|------------|-------|
| R1 | Third-party API unavailable | Medium | High | 6 | Mock API for testing | {dev} |
| R2 | Database migration complex | High | Medium | 6 | Spike before starting | {dev} |
| R3 | Unclear requirements | Low | High | 4 | Refinement session | PO |

**Risk Score:** Probability (1-3) × Impact (1-3) = Score (1-9)

**Top 3 Risks:**
1. **R1:** Third-party API unavailable (Score: 6)
   - Mitigation: Create mock API for local testing
   - Contingency: Use cached data if API down

2. **R2:** Database migration complexity (Score: 6)
   - Mitigation: Time-boxed spike (4 hours) before starting story
   - Contingency: Rollback plan prepared

3. **R3:** Unclear requirements (Score: 4)
   - Mitigation: Schedule refinement session with PO on Day 1
   - Contingency: Defer story if not clarified

---

{Rest of standard template...}
```

---

## Sprint Planning Meeting Output Template

**Use Case:** Document outcomes from sprint planning ceremony

```markdown
# Sprint {number} Planning Meeting

**Date:** {date}
**Duration:** {duration} hours
**Attendees:** {attendee_list}

---

## Meeting Outcomes

### Sprint Goal (Team-Defined)
{team_agreed_sprint_goal}

### Commitment
**Team Capacity:** {capacity} points
**Team Commitment:** {committed} points
**Confidence Level:** {percentage}% (voted by team)

---

## Stories Discussed

### Accepted for Sprint
1. {story-id}: {story-title} ({points} pts) - {assignee}
   - Discussion: {summary}
   - Questions Resolved: {question_count}
   - Estimated by: {estimation_technique}

{Repeat for accepted stories}

### Deferred (Not Enough Capacity)
1. {story-id}: {story-title} ({points} pts)
   - Reason: {reason}

### Blocked (Clarification Needed)
1. {story-id}: {story-title} ({points} pts)
   - Blocker: {blocker_description}
   - Action: {action_item}
   - Owner: {owner}

---

## Action Items from Planning

- [ ] {action_1} - {owner} - Due: {date}
- [ ] {action_2} - {owner} - Due: {date}

---

## Assumptions and Agreements

1. {assumption_1}
2. {assumption_2}

---

## Next Steps

1. Team members pick stories (by EOD)
2. Create tasks for each story (Day 1)
3. Daily standup starts tomorrow at {time}
4. Sprint review scheduled for {date}

---

**Meeting Notes:** {link_to_detailed_notes}
**Generated:** {date} by sprint-plan skill
```

---

## File Naming Conventions

### Single Sprint Plans
```
.claude/sprints/sprint-{number}-plan-{YYYYMMDD}.md

Examples:
- sprint-1-plan-20250115.md
- sprint-2-plan-20250129.md
```

### Multi-Sprint Roadmaps
```
.claude/sprints/roadmap-sprint{start}-to-sprint{end}-{YYYYMMDD}.md

Examples:
- roadmap-sprint1-to-sprint3-20250115.md
- roadmap-Q1-20250101.md
```

### Sprint Reviews/Retrospectives
```
.claude/sprints/sprint-{number}-review-{YYYYMMDD}.md
.claude/sprints/sprint-{number}-retro-{YYYYMMDD}.md
```

---

## Template Selection Guide

| Use Case | Template | When to Use |
|----------|----------|-------------|
| Standard planning | Basic Sprint Plan | Most sprints, straightforward work |
| Release planning | Multi-Sprint Roadmap | Planning 2-3 sprints ahead |
| Quick reference | Compact Sprint Plan | Status displays, dashboards |
| After planning meeting | Sprint Plan with Assignments | Team has picked stories |
| Quality-focused | Sprint Plan with Test Strategy | High-quality requirements |
| Progress tracking | Sprint Plan with Burndown | Daily standup tracking |
| High-risk sprint | Sprint Plan with Risk Register | Complex or risky work |
| Planning ceremony | Sprint Planning Meeting Output | Document planning meeting |

---

*Part of sprint-plan skill - BMAD Enhanced*
