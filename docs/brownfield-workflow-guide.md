# Brownfield Architecture Workflow Guide

**Complete guide to improving existing system architecture using BMAD Enhanced Phase 4 capabilities**

---

## Overview

This guide shows you how to analyze, improve, and modernize your existing (brownfield) applications using BMAD Enhanced's conversational architecture workflow.

**What You'll Learn:**
- How to analyze your current architecture
- How to get architecture options with trade-offs
- How to run complete modernization workflows
- When to use each approach
- Real-world examples and patterns

**Time Investment:**
- Quick assessment: 18-25 minutes
- Complete modernization workflow: 41-63 minutes
- Conversational consultation: 5-60 minutes (varies)

---

## The Problem: Brownfield Architecture Challenges

### Common Scenarios:

**Scenario 1: "I Built This With Less Capable Tools"**
> "I started my web app years ago with older tools/models. The architecture probably isn't optimal anymore. How do I improve it?"

**Scenario 2: "I Inherited This Codebase"**
> "I took over this project. No documentation. I need to understand what I have and how to improve it."

**Scenario 3: "Need to Scale/Add Features"**
> "My app works for 1,000 users, but I need to scale to 100,000. Also want to add real-time features. What's the best approach?"

**Scenario 4: "Should I Modernize or Rewrite?"**
> "My tech stack is outdated. Should I modernize what I have or start fresh? What are the trade-offs?"

---

## The Solution: BMAD Enhanced Phase 4 Workflow

### Three Approaches:

1. **Conversational Entry** - Start with `/winston-consult`
2. **Direct Analysis** - Use individual Winston commands
3. **Complete Workflow** - Run `/orchestrator *workflow modernize`

---

## Approach 1: Conversational Entry (Recommended for Beginners)

### When to Use:
- You're not sure where to start
- You want guidance through the process
- You have questions about your options
- You prefer interactive dialogue

### How It Works:

**Step 1: Start Conversation**
```bash
/winston-consult "I have a web app built with React and Express. Want to add real-time features and scale to 50K users."
```

**Step 2: Answer Winston's Questions**

Winston will ask clarifying questions like:
- What's your current tech stack? (versions, database, hosting)
- What problems are you facing? (performance, maintainability, scalability)
- What's your timeline? (weeks, months, year)
- What's your budget constraint? (tight, moderate, generous)
- What's your risk tolerance? (conservative, moderate, aggressive)

**Step 3: Get Tailored Recommendations**

Based on your answers, Winston will:
- Recommend appropriate workflow (analysis, design, comparison)
- Route you to the right commands
- Guide you through the process
- Provide follow-up options

**Example Conversation:**

```
You: /winston-consult "I have a React/Express app from 2020. Want to modernize."

Winston: I'd love to help you modernize! A few questions first:

1. What's your current tech stack?
   - Frontend: React version?
   - Backend: Express version?
   - Database?
   - Hosting?

2. What problems are you facing?
   - Slow performance?
   - Hard to maintain?
   - Can't scale?
   - Security concerns?

3. What's your vision for the modernized app?
   - New features needed?
   - Target user scale?
   - Performance requirements?

4. What are your constraints?
   - Timeline? (weeks, months, year)
   - Budget? (tight, moderate, generous)
   - Team size? (solo, small team, large team)

---

You:
1. React 16, Express 4, PostgreSQL, Heroku
2. Slow performance, hard to add features
3. Want real-time chat, 50K users, faster
4. 3-4 months, moderate budget, 3-person team

---

Winston: Perfect! Based on your situation, I recommend a complete
modernization workflow. Here's what we'll do:

**Phase 1: Architecture Analysis** (12 min)
Analyze your current React 16/Express 4 architecture to understand:
- Current production readiness score
- Technical debt
- Performance bottlenecks
- Scalability limitations

**Phase 2: Brownfield PRD** (8 min)
Document your current features and identify gaps for real-time + scale.

**Phase 3: Architecture Comparison** (10 min)
Generate 3 options:
- Option A: Upgrade to React 19 + add Socket.IO (fast, limited scale)
- Option B: Microservices + caching + real-time service (balanced)
- Option C: Full rewrite with Next.js + tRPC (best long-term)

**Phase 4: Architecture Design** (15 min)
Design complete architecture for your chosen option.

**Phase 5: Implementation Plan** (6 min)
Break down into epics with story points.

**Total time:** ~51 minutes

Shall I proceed with this workflow?

---

You: Yes, proceed

---

Winston: Excellent! Starting Phase 1: Architecture Analysis...

[Workflow begins...]
```

---

## Approach 2: Direct Analysis (For Experienced Users)

### When to Use:
- You know exactly what you need
- You want specific analysis/output
- You prefer direct commands
- You're experienced with architecture work

### Commands to Use:

#### Command 1: Analyze Current Architecture

```bash
/winston *analyze-architecture .
```

**Duration:** 10-15 minutes

**Output:**
- Production Readiness Score: 78/100 ⭐⭐⭐⭐
- Quality Assessment (8 dimensions scored 0-100)
- Technology Stack Analysis
- Architecture Patterns Identified
- Technical Debt Report
- Top 3-5 Modernization Opportunities (HIGH/MEDIUM/LOW priority)

**Example Output:**
```markdown
# Architecture Analysis: MyApp

**Production Readiness:** 78/100 ⭐⭐⭐⭐

## Quality Dimensions

- Architecture Quality: 85/100 ⭐⭐⭐⭐⭐ (Excellent)
- Code Quality: 75/100 ⭐⭐⭐⭐ (Good)
- Security: 88/100 ⭐⭐⭐⭐ (Very Good)
- Performance: 65/100 ⭐⭐⭐ (Needs Improvement)
- Scalability: 60/100 ⭐⭐⭐ (Limited to ~10K users)
- Maintainability: 80/100 ⭐⭐⭐⭐ (Very Good)
- Testing: 70/100 ⭐⭐⭐ (Good)
- Monitoring: 50/100 ⭐⭐ (Basic)

## Top Modernization Opportunities

🔴 **HIGH PRIORITY** (1-2 weeks):
1. Add caching layer (Redis) - Performance improvement
2. Implement database read replicas - Scalability improvement
3. Add comprehensive monitoring - Observability improvement

🟡 **MEDIUM PRIORITY** (Next quarter):
4. Upgrade React 16 → React 19 - Modern features
5. Implement real-time infrastructure - New capability
6. Add E2E test coverage - Quality improvement

🟢 **LOW PRIORITY** (Future):
7. Microservices extraction - Architectural improvement
8. GraphQL layer - Developer experience
```

---

#### Command 2: Compare Architecture Options

```bash
/winston *compare-architectures "Add real-time features and scale to 50K users"
```

**Duration:** 8-12 minutes

**Output:**
- Option A: Minimal Changes (timeline, cost, risk, pros/cons)
- Option B: Moderate Refactor (timeline, cost, risk, pros/cons) ✅ Recommended
- Option C: Full Modernization (timeline, cost, risk, pros/cons)
- Trade-offs analysis across 5 dimensions
- Clear recommendation with confidence score

**Example Output:**
```markdown
# Architecture Options Comparison

**Recommendation:** Option B - Moderate Refactor (Confidence: 85%)

## Option A: Minimal Changes

**Timeline:** 4-6 weeks
**Cost:** $25K-$40K
**Risk:** Low (18/100)
**Scale:** ~15K users max

**Approach:**
Add Socket.IO to existing Express backend + Redis for pub/sub

✅ **Pros:**
• Fast implementation
• Low risk (minimal changes)
• No migration needed

❌ **Cons:**
• Limited scalability (~15K users max)
• Technical debt increases
• Not optimal architecture for real-time

---

## Option B: Moderate Refactor ✅ RECOMMENDED

**Timeline:** 2-3 months
**Cost:** $60K-$90K
**Risk:** Medium (43/100)
**Scale:** 50K+ users

**Approach:**
Real-time microservice + Redis caching + DB read replicas

✅ **Pros:**
• Scales to 50K+ users (meets requirement)
• Reduces technical debt
• Modern architecture patterns
• Easier to hire developers

❌ **Cons:**
• More complex deployment
• Team needs to learn microservices
• Moderate migration effort

**Why Recommended:**
Given your constraints (3-4 months timeline, moderate budget,
need to scale to 50K users), Option B provides the best balance
of investment, risk, and future-proofing.

---

## Option C: Full Modernization

**Timeline:** 4-6 months
**Cost:** $150K-$200K
**Risk:** High (66/100)
**Scale:** 100K+ users

**Approach:**
Complete rebuild with Next.js 15 + tRPC + Serverless

✅ **Pros:**
• Modern, maintainable codebase
• Excellent scalability (100K+ users)
• Near-zero technical debt
• Best performance

❌ **Cons:**
• Long timeline (4-6 months)
• High cost ($150K-$200K)
• Complex migration from old system
• Team learning curve

---

## Trade-offs Summary

| Dimension | Option A | Option B ✅ | Option C |
|-----------|----------|------------|----------|
| **Timeline** | 4-6 weeks | 2-3 months | 4-6 months |
| **Cost** | $25K-$40K | $60K-$90K | $150K-$200K |
| **Risk** | Low (18) | Medium (43) | High (66) |
| **Scale** | ~15K users | ~50K users | ~100K users |
| **Tech Debt** | +10% | -20% | -90% |
```

---

#### Command 3: Create Detailed Architecture

```bash
/winston *create-architecture docs/brownfield-prd.md --option moderate
```

**Duration:** 12-18 minutes

**Output:**
- Complete architecture document
- Technology stack with justifications
- Architecture Decision Records (ADRs)
- Security architecture
- Performance strategy
- Scalability approach
- Migration plan (3-phase incremental)

---

#### Command 4: Validate Architecture

```bash
/winston *validate-architecture docs/architecture.md
```

**Duration:** 3-5 minutes

**Output:**
- Validation score: 85/100
- Completeness checklist (all sections present)
- Missing elements (if any)
- Recommendations for improvement
- Pass/Fail verdict

---

#### Command 5: Peer Review

```bash
/winston *review-architecture docs/architecture.md --focus scalability
```

**Duration:** 5-8 minutes

**Output:**
- Risk assessment (critical, major, minor)
- Scalability bottlenecks identified
- Optimization opportunities
- Cost-benefit analysis
- Prioritized action items

---

## Approach 3: Complete Workflow (For Full Modernization)

### When to Use:
- You want the complete package
- You prefer automated workflow
- You want all deliverables (analysis + PRD + architecture + plan)
- You're okay with 51-minute time investment

### How It Works:

**Single Command:**
```bash
/orchestrator *workflow modernize . "Add real-time features and scale to 50K users"
```

**What Happens:**

**Phase 1/5: Architecture Analysis** (winston) ⏳
- Analyzing codebase structure...
- Detecting project type: Fullstack (React + Express)
- Analyzing tech stack... 18 dependencies found
- Identifying patterns... DDD/CQRS detected
- Calculating quality scores...

✅ **Analysis Complete** (12 minutes)

**Output:**
```
Production Readiness: 78/100 ⭐⭐⭐⭐

Key Findings:
• Architecture Quality: 85/100 (Very Good)
• Performance: 65/100 (Needs improvement)
• Scalability: 60/100 (Limited to ~10K users)

Top 3 Modernization Opportunities:
1. Add WebSocket/real-time infrastructure (HIGH)
2. Implement caching layer (Redis) (HIGH)
3. Database read replicas for scaling (MEDIUM)

📄 Report: docs/architecture-analysis-2025-11-05.md
```

---

**Phase 2/5: Brownfield PRD** (alex) ⏳
- Extracting current features from codebase...
- Documenting 12 core features, 5 secondary features
- Identifying gaps and technical debt...

✅ **Brownfield PRD Created** (8 minutes)

**Output:**
```
📄 PRD: docs/brownfield-prd.md

Current Features:
• User Authentication (High confidence)
• Dashboard & Analytics (High confidence)
• Data Management (Medium confidence)
• [9 more features...]

Gaps Identified:
• No real-time capabilities (needed for your goal)
• Limited caching (performance bottleneck)
• No horizontal scaling (blocks 50K user goal)
```

---

**Phase 3/5: Architecture Comparison** (winston) ⏳
- Generating 3 modernization options...

✅ **Comparison Complete** (10 minutes)

**Output:**
```
Option A: Minimal Changes (4-6 weeks, $25K-$40K, Risk: Low)
✅ Fast, low risk
❌ Limited scalability (~15K users max)

Option B: Moderate Refactor (2-3 months, $60K-$90K, Risk: Medium) ✅ RECOMMENDED
✅ Scales to 50K+ users, reduces tech debt
⚖️ Moderate complexity

Option C: Full Modernization (4-6 months, $150K-$200K, Risk: High)
✅ Best long-term, scales to 100K+
❌ High cost, long timeline

📄 Comparison: docs/architecture-comparison-2025-11-05.md
```

**❓ USER INPUT REQUIRED:**
```
Which option would you like to proceed with?
A) Option A - Minimal Changes (fast, limited scale)
B) Option B - Moderate Refactor (recommended, balanced)
C) Option C - Full Modernization (best quality, highest cost)

> [You select: B]
```

---

**Phase 4/5: Detailed Architecture Design** (winston) ⏳
- Designing complete architecture for Option B...
- Creating ADRs for technology decisions...
- Designing migration strategy...

✅ **Architecture Complete** (15 minutes)

**Output:**
```
📄 Architecture: docs/architecture.md

Technology Stack:
• Real-time: Dedicated Node.js microservice + Socket.IO
• Caching: Redis (sessions + data cache)
• Database: PostgreSQL (existing) + Read replicas (new)
• API Gateway: Kong (route management)

Migration Strategy:
Phase 1 (Month 1): Redis caching layer
Phase 2 (Month 2): Real-time microservice
Phase 3 (Month 3): Database read replicas + API gateway
```

---

**Phase 5/5: Implementation Plan** (alex) ⏳
- Breaking down architecture into epics...
- Creating implementation roadmap...

✅ **Implementation Plan Complete** (6 minutes)

**Output:**
```
📄 Plan: .claude/epics/modernization-plan.md

Epic Breakdown:
Epic 1: Redis Caching Infrastructure (13 points)
Epic 2: Real-time Microservice (21 points)
Epic 3: Database Read Replicas (8 points)
Epic 4: API Gateway Setup (13 points)
Epic 5: Migration & Testing (13 points)

Total: 68 story points (~3 sprints at 20-25 velocity)
```

---

🎉 **Modernization Workflow Complete!**

**Summary:**
- Analysis: Production Readiness 78/100
- Approach: Option B - Moderate Refactor
- Timeline: 2-3 months (3 sprints)
- Cost Estimate: $60K-$90K
- Expected Outcome: Scale to 50K+ users, reduce tech debt

**Next Steps:**
1. Review architecture: docs/architecture.md
2. Review implementation plan: .claude/epics/modernization-plan.md
3. Start Epic 1: /alex *breakdown-epic .claude/epics/modernization-plan.md
4. Begin sprint planning: /alex *plan-sprint --velocity 25

**Files Generated:**
• Architecture Analysis: docs/architecture-analysis-2025-11-05.md
• Brownfield PRD: docs/brownfield-prd.md
• Architecture Comparison: docs/architecture-comparison-2025-11-05.md
• Final Architecture: docs/architecture.md
• Implementation Plan: .claude/epics/modernization-plan.md

**Total Duration:** 51 minutes

---

## Workflow Variants

### Variant 1: Quick Assessment (--quick)

**Use when:** You want fast recommendations without full analysis

```bash
/orchestrator *workflow modernize packages/backend --quick
```

**Phases (3 instead of 5):**
1. Architecture Analysis (8 min)
2. Architecture Comparison (6 min)
3. High-Level Plan (4 min)

**Total:** 18 minutes

**Output:**
- Production readiness score
- 3 architecture options
- High-level recommendations
- No detailed PRD or implementation plan

---

### Variant 2: Analysis Only (--analysis-only)

**Use when:** You just want to understand current state

```bash
/orchestrator *workflow modernize . --analysis-only
```

**Phases (1 only):**
1. Architecture Analysis (12 min)

**Total:** 12 minutes

**Output:**
- Complete architecture analysis
- Production readiness score
- Modernization opportunities
- No PRD, options, or implementation plan

---

### Variant 3: Auto-Select (--auto)

**Use when:** Trust the recommendation, no interactive input needed

```bash
/orchestrator *workflow modernize . "Your goals" --auto
```

**Phases (5, but no interruption):**
- Runs all 5 phases
- Auto-selects recommended option (usually Option B)
- No user input required
- Fully automated

**Total:** 51 minutes (uninterrupted)

---

## Real-World Examples

### Example 1: E-Commerce Platform Modernization

**Situation:**
- Legacy PHP/jQuery e-commerce platform (8 years old)
- 5,000 daily users, want to scale to 50,000
- Hard to maintain, slow performance
- Want modern SPA + mobile app

**Workflow Used:**
```bash
/orchestrator *workflow modernize . "Scale to 50K users + add mobile app + modern SPA"
```

**Result:**
- **Analysis:** Production Readiness 62/100 (needs improvement)
- **Options Generated:**
  - A: Modernize PHP with Laravel ($40K, 2 months)
  - B: Gradual migration to Node.js/React ($90K, 4 months) ✅ Selected
  - C: Complete rewrite Next.js ($180K, 6 months)
- **Chosen:** Option B (gradual migration)
- **Implementation Plan:** 5 epics, 85 story points, 4 sprints
- **Timeline:** 4 months
- **Outcome:** Successfully scaled to 60K users, 40% performance improvement

---

### Example 2: SaaS Dashboard Modernization

**Situation:**
- React 16 dashboard built in 2019
- Need real-time features (WebSocket)
- Performance issues with large datasets
- Want to scale to enterprise customers

**Workflow Used:**
```bash
/winston-consult "React 16 dashboard, need real-time + better performance"

[After conversation]

/orchestrator *workflow modernize packages/dashboard "Real-time + performance"
```

**Result:**
- **Analysis:** Production Readiness 75/100 (good, but needs improvement)
- **Options Generated:**
  - A: Add Socket.IO + pagination ($30K, 6 weeks)
  - B: React 19 + dedicated real-time service + caching ($70K, 3 months) ✅ Selected
  - C: Complete rebuild with Next.js + tRPC ($150K, 5 months)
- **Chosen:** Option B
- **Implementation Plan:** 4 epics, 52 story points, 2.5 sprints
- **Timeline:** 3 months
- **Outcome:** Real-time features added, 60% performance improvement, enterprise-ready

---

### Example 3: Inherited Codebase Assessment

**Situation:**
- Inherited Node.js/React monorepo, no documentation
- Need to understand current state before making changes
- Planning modernization roadmap

**Workflow Used:**
```bash
/winston *analyze-architecture . --depth comprehensive
```

**Result:**
- **Analysis:** Production Readiness 68/100 (fair)
- **Key Findings:**
  - Well-structured monorepo (Turbo repo)
  - Good TypeScript coverage (92%)
  - Limited testing (only 45% coverage)
  - No monitoring/observability
  - Performance bottlenecks identified
- **Recommendations:**
  - HIGH: Add monitoring + observability (2 weeks)
  - HIGH: Improve test coverage to 80% (3 weeks)
  - MEDIUM: Optimize database queries (1 week)
- **Next Steps:** Used recommendations to plan modernization sprints

---

## Decision Matrix: Which Approach to Use?

| Situation | Recommended Approach | Command |
|-----------|---------------------|---------|
| **Don't know where to start** | Conversational | `/winston-consult` |
| **Just want to understand current state** | Direct Analysis | `/winston *analyze-architecture` |
| **Need to compare options** | Direct Comparison | `/winston *compare-architectures` |
| **Want complete package** | Full Workflow | `/orchestrator *workflow modernize` |
| **Time-constrained (18 min)** | Quick Workflow | `/orchestrator *workflow modernize --quick` |
| **Already know what option you want** | Auto Workflow | `/orchestrator *workflow modernize --auto` |
| **Experienced, want control** | Direct Commands | Individual Winston commands |
| **Beginner, want guidance** | Conversational | `/winston-consult` |

---

## Best Practices

### 1. Always Analyze Before Designing

Don't skip analysis:
```bash
# ❌ BAD: Jumping to design without understanding current state
/winston *create-architecture "Add real-time features"

# ✅ GOOD: Analyze first, then design
/winston *analyze-architecture .
# [Review results]
/winston *compare-architectures "Add real-time features"
```

### 2. Get Options Before Committing

Don't assume one approach is best:
```bash
# ✅ GOOD: Compare options with trade-offs
/winston *compare-architectures "Your goals"
# [Review 3 options]
# [Choose based on your constraints]
```

### 3. Validate Before Implementation

Catch issues early:
```bash
# After Winston creates architecture
/winston *validate-architecture docs/architecture.md
# [Fix any gaps before implementation]
```

### 4. Use Interactive Mode for Big Decisions

Don't auto-select for major changes:
```bash
# ✅ GOOD: Interactive (you choose option)
/orchestrator *workflow modernize . "Goals" --interactive

# ❌ RISKY: Auto-select for major modernization
/orchestrator *workflow modernize . "Goals" --auto
```

### 5. Document Your Decision

After choosing an option, document why:
```markdown
# Decision Log

**Date:** 2025-11-05
**Decision:** Chose Option B (Moderate Refactor)
**Reasoning:**
- Timeline: 3-4 months (fits our schedule)
- Budget: $60K-$90K (within budget)
- Risk: Medium (acceptable for our team)
- Scale: 50K+ users (meets requirement)
- Tech debt: -20% reduction (important for long-term)

**Alternatives Considered:**
- Option A: Too limited (only ~15K users)
- Option C: Too expensive and long timeline
```

---

## Troubleshooting

### Issue: "Analysis taking too long"

**Solution:** Use quick mode
```bash
/winston *analyze-architecture . --depth quick
```

### Issue: "Not sure which option is best"

**Solution:** Use conversational mode
```bash
/winston-consult "I got 3 options but not sure which to choose"
```

### Issue: "Workflow interrupted, how do I continue?"

**Solution:** Resume workflow
```bash
/orchestrator *resume <workflow-id>
```

### Issue: "Architecture validation failed"

**Solution:** Check specific gaps and fix
```bash
/winston *validate-architecture docs/architecture.md --strict
# Address missing sections identified
# Re-validate after fixes
```

### Issue: "Want to change chosen option"

**Solution:** Re-run Phase 4 with different option
```bash
/winston *create-architecture docs/brownfield-prd.md --option full
```

---

## Next Steps

**After Brownfield Workflow:**

1. **Review All Generated Documents**
   - Architecture analysis
   - Brownfield PRD
   - Architecture comparison
   - Final architecture
   - Implementation plan

2. **Validate Architecture**
   ```bash
   /winston *validate-architecture docs/architecture.md
   ```

3. **Get Peer Review**
   ```bash
   /winston *review-architecture docs/architecture.md
   ```

4. **Create Implementation Plan**
   ```bash
   /alex *breakdown-epic docs/architecture.md
   ```

5. **Start Implementation**
   ```bash
   /james *implement task-001
   ```

6. **Quality Review**
   ```bash
   /quinn *review task-001
   ```

---

## Related Documentation

- [Winston Quick Start](./quickstart-winston.md) - All Winston commands
- [Orchestrator Quick Start](./quickstart-orchestrator.md) - Workflow orchestration
- [Alex Quick Start](./quickstart-alex.md) - Implementation planning
- [V2 Architecture](./V2-ARCHITECTURE.md) - Complete V2 architecture docs
- [Phase 4 Week 1 Summary](./PHASE-4-WEEK-1-SUMMARY.md) - Technical details

---

**Ready to modernize your brownfield application?** 🏗️

Start here:
```bash
/winston-consult "Describe your situation and goals"
```
