# Sprint Planning Templates and Output Formats

All output formats, examples, and templates for the sprint-plan skill.

---

## Step 0: Load Configuration and Sprint Context Output

**Complete Output Format:**
```
Sprint Planning Context:
- Sprint: Sprint 1
- Velocity: 20 points
- Buffer: 15% (3 points)
- Effective Capacity: 17 points
- Eligible Stories: 24 stories (78 total points)
- Dependencies: 8 blocking relationships identified
- Plan Ahead: 1 sprint
✓ Context loaded successfully
✓ Duration: 234ms
```

**Example with Multi-Sprint:**
```
Sprint Planning Context:
- Sprints: Sprint 1, Sprint 2, Sprint 3 (3 sprints ahead)
- Velocity: 20 points per sprint
- Buffer: 15% (3 points per sprint)
- Effective Capacity: 17 points per sprint
- Total Planning Capacity: 51 points across 3 sprints
- Eligible Stories: 45 stories (134 total points)
- Dependencies: 15 blocking relationships identified
✓ Multi-sprint context loaded
✓ Duration: 389ms
```

---

## Step 1: Prioritize and Sort Stories Output

**Complete Output Format:**
```
✓ Stories prioritized and sorted
✓ Sorting criteria applied:
  1. Priority Level (P0 > P1 > P2 > P3)
  2. Dependency Order (blockers before blocked)
  3. Risk Score (high-risk early)
  4. Story Points (smaller first for momentum)
✓ Sorted backlog: 24 stories
  ├─ P0 stories: 8 (28 points)
  ├─ P1 stories: 10 (32 points)
  ├─ P2 stories: 4 (12 points)
  └─ P3 stories: 2 (6 points)
✓ Duration: 156ms
```

**Example Sorted Backlog:**
```
Sorted Backlog (Top 10):

1. story-auth-001 (User Signup) - P0, 5 points, blocks 3 stories (auth-002, auth-003, profile-001)
2. story-auth-002 (User Login) - P0, 3 points, blocked by auth-001, blocks 2 stories
3. story-auth-003 (User Logout) - P0, 1 point, blocked by auth-002
4. story-profile-001 (View Profile) - P1, 2 points, blocked by auth-002, blocks profile-002
5. story-profile-002 (Edit Profile) - P1, 3 points, blocked by profile-001
6. story-settings-001 (Change Password) - P1, 2 points, blocked by auth-002
7. story-settings-002 (Update Email) - P1, 3 points, blocked by auth-002
8. story-admin-001 (User Management) - P1, 5 points, blocked by auth-002
9. story-notifications-001 (Email Notifications) - P2, 3 points, no dependencies
10. story-profile-003 (Avatar Upload) - P2, 5 points, blocked by profile-001

Dependency Chains Identified:
- Chain 1: auth-001 → auth-002 → profile-001 → profile-002 (4 stories, 13 points)
- Chain 2: auth-001 → auth-002 → auth-003 (3 stories, 9 points)
- Chain 3: auth-001 → auth-002 → settings-001 (3 stories, 10 points)
```

---

## Step 2: Select Stories for Sprint Output

**Complete Output Format:**
```
✓ Stories selected for Sprint 1
✓ Selection algorithm applied:
  1. P0 stories in dependency order
  2. Capacity constraints respected (≤17 points)
  3. Dependencies satisfied
  4. Feature completeness maintained
✓ Committed stories: 6
✓ Total points: 16 / 17 available (94% utilization)
✓ Remaining capacity: 1 point
✓ Duration: 187ms
```

**Example Selection:**
```
Sprint 1 Commitment:

Selected Stories (in execution order):

1. story-auth-001 (User Signup) - P0, 5 points
   Dependencies: None
   Reason: Top priority, blocks multiple features

2. story-auth-002 (User Login) - P0, 3 points
   Dependencies: auth-001 (included)
   Reason: Blocked by auth-001, enables rest of auth flow

3. story-auth-003 (User Logout) - P0, 1 point
   Dependencies: auth-002 (included)
   Reason: Completes core auth feature

4. story-profile-001 (View Profile) - P1, 2 points
   Dependencies: auth-002 (included)
   Reason: Enables profile feature, blocks profile-002

5. story-profile-002 (Edit Profile) - P1, 3 points
   Dependencies: profile-001 (included)
   Reason: Completes profile feature (avoid orphans)

6. story-settings-001 (Change Password) - P1, 2 points
   Dependencies: auth-002 (included)
   Reason: Fills remaining capacity

Capacity Analysis:
- Committed: 16 points
- Available: 17 points
- Utilization: 94%
- Buffer: 1 point (6% remaining for unknowns)

Stories Not Selected (next sprint candidates):
- story-settings-002 (Update Email) - P1, 3 points (would exceed capacity)
- story-admin-001 (User Management) - P1, 5 points (too large for remaining capacity)
- story-notifications-001 (Email Notifications) - P2, 3 points (lower priority)
```

---

## Step 3: Validate Dependencies Output

**Complete Output Format:**
```
✓ Dependencies validated
✓ All blocking relationships satisfied:
  ├─ story-auth-001 blocks story-auth-002 ✓ (both in Sprint 1)
  ├─ story-auth-002 blocks story-auth-003 ✓ (both in Sprint 1)
  ├─ story-auth-002 blocks story-profile-001 ✓ (both in Sprint 1)
  └─ story-profile-001 blocks story-profile-002 ✓ (both in Sprint 1)
✓ No orphaned dependencies
✓ Feature completeness: 2 complete features (Auth, Profile)
✓ Validation passed
✓ Duration: 89ms
```

**Example with Issues:**
```
⚠️ Dependency validation warnings:

✓ All blocking relationships satisfied
  ├─ story-auth-001 blocks story-auth-002 ✓
  ├─ story-auth-002 blocks story-auth-003 ✓
  └─ story-auth-002 blocks story-profile-001 ✓

⚠️ Feature completeness concern:
  ├─ Profile feature partially complete (1 of 3 stories)
  │   ├─ Included: story-profile-001 (View Profile)
  │   ├─ Missing: story-profile-002 (Edit Profile) - blocked by profile-001
  │   └─ Missing: story-profile-003 (Avatar Upload) - blocked by profile-001
  └─ Recommendation: Include profile-002 (3 pts) to complete minimum viable feature

Suggested Action:
- Add story-profile-002 (3 pts) to sprint (utilization becomes 112% - adjust)
- OR: Remove story-settings-001 (2 pts), add story-profile-002 (3 pts) instead (utilization 100%)
```

---

## Step 4: Identify Risks and Mitigation Output

**Complete Output Format:**
```
✓ Sprint risks assessed
✓ Risk categories evaluated:
  ├─ Capacity Risk: MEDIUM (94% utilization)
  ├─ Dependency Risk: MEDIUM (longest chain: 4 stories)
  ├─ Technical Risk: LOW (1 high-risk story)
  └─ Scope Risk: LOW (50% P0 stories)
✓ Overall Sprint Risk: MEDIUM
✓ Mitigation strategies identified: 4
✓ Duration: 123ms
```

**Detailed Risk Assessment Example:**
```
Sprint Risks and Mitigation:

⚠️ MEDIUM: Capacity Risk
Score: 6/10
Issue: Sprint utilization at 94% leaves minimal buffer for unknowns
Impact: If any story takes longer than estimated, sprint goal at risk
Mitigation:
  - 1-point buffer available for small overruns
  - story-settings-001 (2 pts) is non-critical and can be dropped if needed
  - Daily progress tracking to catch delays early
  - Consider breaking down story-auth-001 (5 pts) into smaller tasks

⚠️ MEDIUM: Dependency Risk
Score: 7/10
Issue: Critical path is 4 stories long (auth-001 → auth-002 → profile-001 → profile-002)
Impact: Delay in any story cascades to dependent stories, threatens sprint completion
Mitigation:
  - Prioritize auth-001 on Day 1 (critical blocker)
  - Assign most experienced developer to auth-001
  - Daily dependency review in standup
  - Parallel work on story-settings-001 (no dependencies) to maintain momentum
  - Consider pairing on auth-002 to accelerate completion

⚠️ MEDIUM: Technical Risk
Score: 5/10
Issue: story-auth-001 has high risk score (7/10 from estimation)
Impact: Signup implementation has unknowns (OAuth, email verification, security)
Mitigation:
  - Technical spike planned (4 hours) before implementation
  - Pair programming for security-critical code
  - Security review of auth implementation
  - Use established library (Passport.js) to reduce custom code

✓ LOW: Scope Risk
Score: 3/10
Issue: 3 P0 stories out of 6 total (50%)
Impact: Sprint has flexibility - can defer lower-priority stories if needed
Mitigation:
  - Focus on P0 stories first (auth flow)
  - P1 stories (profile, settings) are "nice to have"
  - Can drop story-settings-001 if time constrained
  - Sprint goal still achievable with just P0 stories

Risk Matrix:
                Impact →
              Low    Med    High
Probability ↓
  Low         -      -      -
  Medium      -      C,D    T
  High        S      -      -

Legend:
  C = Capacity Risk
  D = Dependency Risk
  T = Technical Risk
  S = Scope Risk

Overall Sprint Risk: MEDIUM (2 medium risks, 2 low risks, 0 high risks)
Recommendation: Proceed with sprint, implement all mitigations, monitor daily
```

---

## Step 5: Define Sprint Goal Output

**Complete Output Format:**
```
✓ Sprint goal defined
✓ Goal: "Implement core authentication and basic profile management so that users can securely register, log in, and view/edit their profiles"
✓ Success criteria: 4 defined
✓ Goal validated:
  ├─ Specific: ✓ Clear deliverables (auth + profile)
  ├─ Measurable: ✓ Can verify completion
  ├─ Valuable: ✓ Business value clear (user access)
  ├─ Achievable: ✓ Fits within velocity
  └─ Focused: ✓ 2 main themes (auth, profile)
✓ Duration: 45ms
```

**Sprint Goal Examples:**

**Example 1: Core Authentication Sprint**
```
Sprint Goal:
"Implement core authentication so that users can securely register, log in, and access the platform."

Success Criteria:
- Users can sign up with email and password
- Users can log in with credentials and receive JWT token
- Users can log out and invalidate their session
- All authentication flows use bcrypt for password hashing
- Rate limiting prevents brute force attacks

Business Value:
- Enables user accounts (prerequisite for all features)
- Secures platform access
- Establishes trust with users

Theme: Foundation - Authentication
```

**Example 2: User Profile Management Sprint**
```
Sprint Goal:
"Enable comprehensive user profile management so that users can personalize their experience and manage their account settings."

Success Criteria:
- Users can view their profile (name, email, avatar)
- Users can edit profile information
- Users can upload and update profile avatar
- Users can change their password
- Users can update email address with verification

Business Value:
- Personalizes user experience
- Increases engagement
- Empowers users to manage their own data

Theme: User Experience - Profile Management
```

**Example 3: Payment Integration Sprint**
```
Sprint Goal:
"Complete payment integration so that customers can purchase products and subscriptions securely."

Success Criteria:
- Customers can enter payment information (Stripe integration)
- System can process one-time payments
- System can create and manage subscriptions
- Payment failures handled gracefully with retry logic
- Payment receipts sent via email

Business Value:
- Enables revenue generation
- Supports subscription business model
- Provides secure payment processing

Theme: Monetization - Payment Processing
```

---

## Step 6: Calculate Sprint Metrics Output

**Complete Output Format:**
```
✓ Sprint metrics calculated
✓ Capacity metrics:
  ├─ Velocity: 20 points
  ├─ Buffer: 3 points (15%)
  ├─ Effective Capacity: 17 points
  ├─ Commitment: 16 points
  ├─ Utilization: 94%
  └─ Remaining: 1 point
✓ Story metrics:
  ├─ Total stories: 6
  ├─ P0 stories: 3 (50%)
  ├─ P1 stories: 3 (50%)
  └─ Average story size: 2.7 points
✓ Dependency metrics:
  ├─ Total relationships: 4
  ├─ Longest chain: 4 stories
  └─ Average depth: 2 stories
✓ Risk metrics:
  ├─ Average risk score: 4.2/10
  ├─ High-risk stories: 1
  └─ Overall risk: MEDIUM
✓ Duration: 67ms
```

**Detailed Metrics Example:**
```yaml
Sprint Metrics:

Capacity:
  velocity: 20                    # Team's story point capacity per sprint
  buffer_percentage: 15           # Reserve for unknowns and interruptions
  buffer_points: 3                # Calculated buffer (20 × 0.15)
  effective_capacity: 17          # Available points for commitment (20 - 3)
  commitment: 16                  # Total points committed
  utilization_percentage: 94      # Percentage of capacity used (16 / 17)
  remaining_points: 1             # Unused capacity
  status: "Healthy"               # 85-95% utilization ideal

Stories:
  total_count: 6                  # Number of committed stories
  by_priority:
    p0: 3                         # Critical priority (50%)
    p1: 3                         # High priority (50%)
    p2: 0                         # Medium priority
    p3: 0                         # Low priority
  by_size:
    small (1-2 pts): 3            # Quick wins
    medium (3-5 pts): 3           # Standard stories
    large (>5 pts): 0             # Large stories avoided
  average_size: 2.7               # Mean story points
  size_distribution: "Balanced"   # Mix of small and medium stories

Dependencies:
  total_relationships: 4          # Number of blocking relationships
  longest_chain: 4                # auth-001 → auth-002 → profile-001 → profile-002
  average_chain_length: 2         # Mean dependency depth
  stories_with_dependencies: 5    # Stories that depend on others
  blocking_stories: 3             # Stories that block others
  independent_stories: 1          # Stories with no dependencies
  dependency_health: "Moderate"   # Long chain is a concern

Risk:
  average_risk_score: 4.2         # Mean risk score across all stories (scale 1-10)
  risk_distribution:
    high (7-10): 1                # story-auth-001 (score 7)
    medium (4-6): 3               # 3 stories in medium range
    low (1-3): 2                  # 2 low-risk stories
  highest_risk_story:
    id: "story-auth-001"
    title: "User Signup"
    risk_score: 7
    risk_factors: "OAuth integration, email verification, security unknowns"
  overall_risk: "MEDIUM"          # Sprint-level risk assessment
  risk_mitigation_count: 4        # Number of mitigation strategies planned

Timeline:
  sprint_duration_days: 10        # 2-week sprint (excluding weekends)
  estimated_completion: "Day 9"   # Based on point burn-down
  slack_days: 1                   # Buffer days before sprint end
  critical_path_duration: 7       # Days to complete longest dependency chain

Velocity Tracking:
  historical_velocity: [18, 20, 19, 20]  # Last 4 sprints
  average_velocity: 19.25         # Mean of historical data
  velocity_trend: "Stable"        # Team velocity is consistent
  confidence: "High"              # Predictable capacity
```

---

## Step 7: Generate Sprint Plan Document Output

**Complete Output Format:**
```
✓ Sprint plan document generated
✓ File: .claude/sprints/sprint-sprint-1-20250120.md
✓ Sections created:
  ├─ Sprint Goal
  ├─ Committed Stories (6 stories)
  ├─ Sprint Metrics
  ├─ Risks and Mitigation
  ├─ Sprint Schedule
  └─ Definition of Done
✓ File size: 3,456 bytes
✓ Duration: 234ms
```

**Complete Sprint Plan Document Template:**

**File:** `.claude/sprints/sprint-sprint-1-20250120.md`

```markdown
---
sprint_name: Sprint 1
start_date: 2025-01-20
end_date: 2025-02-02
duration_days: 10
velocity: 20
commitment: 16
utilization: 94
status: Planned
---

# Sprint Plan: Sprint 1

**Sprint Dates:** January 20 - February 2, 2025 (2 weeks)
**Velocity:** 20 points
**Commitment:** 16 points (94% utilization)
**Status:** Planned

---

## Sprint Goal

"Implement core authentication and basic profile management so that users can securely register, log in, and view/edit their profiles."

**Success Criteria:**
- ✅ Users can sign up with email and password
- ✅ Users can log in and log out
- ✅ Users can view their profile information
- ✅ Users can edit their profile information
- ✅ All authentication flows are secure (bcrypt, JWT, rate limiting)

**Business Value:**
- Enables user accounts (foundation for all features)
- Secures platform access
- Empowers users to manage their own data

---

## Committed Stories

| Story ID | Title | Priority | Points | Dependencies | Risk |
|----------|-------|----------|--------|--------------|------|
| story-auth-001 | User Signup | P0 | 5 | None | 7/10 (High) |
| story-auth-002 | User Login | P0 | 3 | auth-001 | 4/10 (Medium) |
| story-auth-003 | User Logout | P0 | 1 | auth-002 | 2/10 (Low) |
| story-profile-001 | View Profile | P1 | 2 | auth-002 | 3/10 (Low) |
| story-profile-002 | Edit Profile | P1 | 3 | profile-001 | 5/10 (Medium) |
| story-settings-001 | Change Password | P1 | 2 | auth-002 | 4/10 (Medium) |

**Total:** 16 points

**Execution Order (respecting dependencies):**
1. story-auth-001 (blocks 5 others)
2. story-auth-002 (blocks 4 others)
3. story-auth-003, story-profile-001, story-settings-001 (can be parallel)
4. story-profile-002 (after profile-001)

---

## Sprint Metrics

### Capacity

- **Velocity:** 20 points
- **Buffer:** 3 points (15%)
- **Effective Capacity:** 17 points
- **Commitment:** 16 points
- **Utilization:** 94% ✅ Healthy (85-95% ideal)
- **Remaining:** 1 point

### Stories

- **Total:** 6 stories
- **By Priority:** P0: 3 (50%), P1: 3 (50%)
- **Average Size:** 2.7 points
- **Size Distribution:** 3 small (1-2 pts), 3 medium (3-5 pts)

### Dependencies

- **Total Relationships:** 4 blocking relationships
- **Longest Chain:** 4 stories (auth-001 → auth-002 → profile-001 → profile-002)
- **Average Depth:** 2 stories
- **Independent Stories:** 1 (story-settings-001 can run parallel)

### Risk

- **Average Risk Score:** 4.2/10
- **High-Risk Stories:** 1 (story-auth-001)
- **Overall Sprint Risk:** MEDIUM

---

## Risks and Mitigation

### ⚠️ MEDIUM: Capacity Risk (Score: 6/10)

**Issue:** Sprint utilization at 94% leaves minimal buffer for unknowns

**Impact:** If any story takes longer than estimated, sprint goal at risk

**Mitigation:**
- 1-point buffer available for small overruns
- story-settings-001 (2 pts) is non-critical and can be dropped if needed
- Daily progress tracking to catch delays early
- Consider breaking down story-auth-001 (5 pts) into smaller tasks

---

### ⚠️ MEDIUM: Dependency Risk (Score: 7/10)

**Issue:** Critical path is 4 stories long (auth-001 → auth-002 → profile-001 → profile-002)

**Impact:** Delay in any story cascades to dependent stories, threatens sprint completion

**Mitigation:**
- Prioritize auth-001 on Day 1 (critical blocker)
- Assign most experienced developer to auth-001
- Daily dependency review in standup
- Parallel work on story-settings-001 (no dependencies) to maintain momentum

---

### ✅ LOW: Technical Risk (Score: 5/10)

**Issue:** story-auth-001 has high risk score (7/10 from estimation)

**Impact:** Signup implementation has unknowns (OAuth, email verification, security)

**Mitigation:**
- Technical spike planned (4 hours) before implementation
- Pair programming for security-critical code
- Security review of auth implementation
- Use established library (Passport.js) to reduce custom code

---

### ✅ LOW: Scope Risk (Score: 3/10)

**Issue:** 3 P0 stories out of 6 total (50%)

**Impact:** Sprint has flexibility - can defer lower-priority stories if needed

**Mitigation:**
- Focus on P0 stories first (auth flow)
- P1 stories (profile, settings) are "nice to have"
- Can drop story-settings-001 if time constrained
- Sprint goal still achievable with just P0 stories

---

## Sprint Schedule (Recommended)

### Week 1 (Days 1-5)

**Day 1-2 (8 hours):** story-auth-001 (User Signup) - 5 points
- Technical spike: OAuth flow design (4 hours)
- Implementation start: Signup endpoint (4 hours)
- **Blocker Alert:** This blocks 5 other stories

**Day 3-4 (6 hours):** story-auth-001 continued + story-auth-002 start
- Complete story-auth-001 (2 hours)
- Start story-auth-002 (Login) - 3 points (4 hours)

**Day 5 (6 hours):** story-auth-002 complete + story-auth-003
- Complete story-auth-002 (2 hours)
- Complete story-auth-003 (Logout) - 1 point (2 hours)
- **Milestone:** Core auth complete (9 points, 56% of sprint)

### Week 2 (Days 6-10)

**Day 6-7 (8 hours):** Parallel work
- Track A: story-profile-001 (View Profile) - 2 points (4 hours)
- Track B: story-settings-001 (Change Password) - 2 points (4 hours)

**Day 8-9 (6 hours):** story-profile-002 (Edit Profile) - 3 points
- Depends on profile-001 completing

**Day 10 (2 hours):** Buffer + Sprint wrap-up
- Final testing and code review
- Demo preparation
- Sprint retrospective
- **Sprint Complete:** 16 points delivered

---

## Dependency Graph

```
story-auth-001 (Signup) - 5 pts, P0
    ├─→ story-auth-002 (Login) - 3 pts, P0
    │       ├─→ story-auth-003 (Logout) - 1 pt, P0
    │       ├─→ story-profile-001 (View Profile) - 2 pts, P1
    │       │       └─→ story-profile-002 (Edit Profile) - 3 pts, P1
    │       └─→ story-settings-001 (Change Password) - 2 pts, P1
```

**Critical Path:** auth-001 → auth-002 → profile-001 → profile-002 (13 points, 7 days estimated)

---

## Definition of Done (Sprint-Level)

- [ ] All 6 committed stories meet their individual Definition of Done
- [ ] Sprint goal achieved (core auth + basic profile)
- [ ] No critical or high-severity bugs remain
- [ ] All code reviewed and approved by at least 1 team member
- [ ] All code merged to main branch
- [ ] Documentation updated (API docs, README)
- [ ] Demo prepared for stakeholders
- [ ] Retrospective completed with action items

---

## Sprint Backlog (Not Committed)

**Next Sprint Candidates:**

- story-settings-002 (Update Email) - P1, 3 points
- story-admin-001 (User Management) - P1, 5 points
- story-notifications-001 (Email Notifications) - P2, 3 points
- story-profile-003 (Avatar Upload) - P2, 5 points

**Why Not Included:**
- Would exceed velocity
- Lower priority than committed stories
- Can be deferred to Sprint 2

---

## Team Assignments (Recommended)

**Developer A (Senior):**
- story-auth-001 (Signup) - High risk, needs experience
- story-auth-002 (Login) - Critical path

**Developer B (Mid):**
- story-profile-001 (View Profile) - Lower risk
- story-profile-002 (Edit Profile) - Follow-on

**Developer C (Mid):**
- story-auth-003 (Logout) - Simple, good for learning
- story-settings-001 (Change Password) - Independent, can run parallel

---

## Daily Standup Focus

**Questions to address:**

1. Is auth-001 on track? (Days 1-2)
2. Are we respecting the critical path? (Days 3-5)
3. Can we start parallel work on profile/settings? (Days 6-7)
4. Are any stories at risk of not completing? (Days 8-9)
5. Do we need to drop story-settings-001 to meet sprint goal? (Day 9-10)

---

## Sprint Velocity Tracking

**Burn-down Target:**
- Day 1: 16 points remaining
- Day 3: 11 points remaining (auth-001 complete)
- Day 5: 7 points remaining (auth-002, auth-003 complete)
- Day 7: 3 points remaining (profile-001, settings-001 complete)
- Day 9: 0 points remaining (profile-002 complete)

**Actual burn-down:** [To be updated daily during sprint]

---

**Generated:** 2025-01-19 14:32:15
**Planner:** BMAD Sprint Planning Skill
**Version:** 1.0

---

*This sprint plan is a living document. Update as sprint progresses.*
```

---

## Step 8: Multi-Sprint Planning Output

**Complete Output Format:**
```
✓ Multi-sprint planning complete
✓ Sprints planned: 3
  ├─ Sprint 1: 16 points (6 stories)
  ├─ Sprint 2: 18 points (5 stories)
  └─ Sprint 3: 15 points (4 stories)
✓ Total roadmap: 49 points, 15 stories across 3 sprints
✓ Files generated:
  ├─ .claude/sprints/sprint-sprint-1-20250120.md
  ├─ .claude/sprints/sprint-sprint-2-20250203.md
  └─ .claude/sprints/sprint-sprint-3-20250217.md
✓ Duration: 1.2s
```

**Multi-Sprint Roadmap Example:**
```
Multi-Sprint Roadmap (3 Sprints):

Sprint 1 (Jan 20 - Feb 2): Core Authentication
Velocity: 20 points | Commitment: 16 points (94%)
Focus: Implement user signup, login, logout, basic profile
Stories: 6 (3 P0, 3 P1)
Goal: "Implement core authentication and basic profile management"

Sprint 2 (Feb 3 - Feb 16): Advanced Features
Velocity: 20 points | Commitment: 18 points (106% - adjusted)
Focus: User settings, admin panel, email notifications
Stories: 5 (2 P0, 2 P1, 1 P2)
Goal: "Enable user settings management and admin capabilities"

Sprint 3 (Feb 17 - Mar 2): Polish & Integration
Velocity: 20 points | Commitment: 15 points (88%)
Focus: Avatar uploads, advanced notifications, integrations
Stories: 4 (0 P0, 2 P1, 2 P2)
Goal: "Polish user experience and integrate third-party services"

Total Roadmap Summary:
- Duration: 6 weeks (3 sprints)
- Total Points: 49 points
- Total Stories: 15 stories
- Average Utilization: 96%
- Cross-Sprint Dependencies: 2 (Sprint 1 → Sprint 2)
```

---

## Step 9: Present Sprint Plan Summary Output

**Complete Summary Format:**
```
✅ Sprint Plan Complete

Sprint: Sprint 1
Dates: Jan 20 - Feb 2, 2025 (2 weeks)

Commitment:
- Stories: 6 (3 P0, 2 P1, 1 P2)
- Points: 16 / 17 available (94% utilization)
- Buffer: 1 point remaining

Sprint Goal:
"Implement core authentication and basic profile management so that users can
securely register, log in, and view/edit their profiles."

Top Stories:
1. story-auth-001: User Signup (5 pts, P0)
2. story-auth-002: User Login (3 pts, P0)
3. story-auth-003: User Logout (1 pt, P0)
4. story-profile-001: View Profile (2 pts, P1)
5. story-profile-002: Edit Profile (3 pts, P1)
6. story-settings-001: Change Password (2 pts, P1)

Risks: 2 MEDIUM (capacity, dependencies), 2 LOW (technical, scope)

Sprint Plan: .claude/sprints/sprint-sprint-1-20250120.md

Next Steps:
1. Review sprint plan with team in Sprint Planning ceremony
2. Assign stories to team members
3. Begin Sprint 1 on Jan 20 with story-auth-001
4. Track progress daily in standups

✅ Ready to begin sprint!
```

---

## JSON Output Format

**Complete Skill Output:**
```json
{
  "skill": "sprint-plan",
  "version": "1.0",
  "status": "completed",
  "timestamp": "2025-01-19T14:32:15Z",
  "duration_ms": 1847,
  "sprint": {
    "name": "Sprint 1",
    "start_date": "2025-01-20",
    "end_date": "2025-02-02",
    "duration_days": 10,
    "status": "Planned"
  },
  "capacity": {
    "velocity": 20,
    "buffer_percentage": 15,
    "buffer_points": 3,
    "effective_capacity": 17,
    "commitment": 16,
    "utilization_percentage": 94,
    "remaining_points": 1
  },
  "stories": {
    "total_count": 6,
    "by_priority": {
      "p0": 3,
      "p1": 3,
      "p2": 0,
      "p3": 0
    },
    "average_size": 2.7,
    "committed": [
      {
        "id": "story-auth-001",
        "title": "User Signup",
        "priority": "P0",
        "points": 5,
        "dependencies": [],
        "risk_score": 7
      },
      {
        "id": "story-auth-002",
        "title": "User Login",
        "priority": "P0",
        "points": 3,
        "dependencies": ["story-auth-001"],
        "risk_score": 4
      }
    ]
  },
  "dependencies": {
    "total_relationships": 4,
    "longest_chain": 4,
    "average_depth": 2
  },
  "risks": {
    "overall_risk": "MEDIUM",
    "average_risk_score": 4.2,
    "categories": [
      {
        "category": "capacity",
        "level": "MEDIUM",
        "score": 6,
        "mitigation": "1-point buffer, can drop story-settings-001 if needed"
      },
      {
        "category": "dependency",
        "level": "MEDIUM",
        "score": 7,
        "mitigation": "Prioritize auth-001 early, daily dependency review"
      }
    ]
  },
  "sprint_goal": {
    "statement": "Implement core authentication and basic profile management so that users can securely register, log in, and view/edit their profiles",
    "success_criteria": [
      "Users can sign up with email and password",
      "Users can log in and log out",
      "Users can view and edit their profile",
      "All authentication flows are secure"
    ]
  },
  "files": {
    "sprint_plan": ".claude/sprints/sprint-sprint-1-20250120.md"
  },
  "telemetry": {
    "event": "skill.sprint-plan.completed",
    "sprint_name": "Sprint 1",
    "velocity": 20,
    "duration_ms": 1847,
    "stories_count": 6,
    "commitment_points": 16,
    "utilization_percent": 94,
    "p0_stories_count": 3,
    "dependencies_count": 4
  }
}
```

---

*Complete templates and output formats for sprint-plan skill*
