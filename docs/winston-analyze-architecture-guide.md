# Winston Architect - Analyze Architecture Guide

## Overview

The `*analyze-architecture` command enables Winston to perform comprehensive analysis of existing (brownfield) codebases. Unlike `*create-architecture` which starts from requirements, `*analyze-architecture` discovers the existing architecture, assesses quality, and provides actionable recommendations.

**Use when:**
- No formal architecture documentation exists
- You need to understand an existing codebase
- Preparing for modernization or migration
- Conducting architecture reviews
- Assessing production readiness

---

## Command Syntax

### Two Ways to Invoke

You can invoke architecture analysis using **two different methods**:

#### Method 1: Wildcard Command (via Winston)
```bash
@winston *analyze-architecture
@winston *analyze-architecture packages/backend
@winston *analyze-architecture . --focus security
```

#### Method 2: Slash Command (Direct)
```bash
/analyze-architecture
/analyze-architecture packages/backend
/analyze-architecture . --focus security
```

**Both execute the same skill**, but with different experiences. See [Slash vs Wildcard: Which to Use?](#slash-vs-wildcard-which-to-use) for detailed comparison.

### Basic Usage

```bash
# Analyze current directory (wildcard)
@winston *analyze-architecture

# Analyze current directory (slash)
/analyze-architecture

# Analyze specific path
@winston *analyze-architecture packages/backend
/analyze-architecture packages/backend
```

### Output Formats

```bash
# Markdown report (default)
@winston *analyze-architecture . --output markdown

# JSON report
@winston *analyze-architecture . --output json

# Both formats
@winston *analyze-architecture . --output both
```

### Focused Analysis

```bash
# Focus on specific area
@winston *analyze-architecture . --focus architecture
@winston *analyze-architecture . --focus security
@winston *analyze-architecture . --focus performance
@winston *analyze-architecture . --focus scalability
@winston *analyze-architecture . --focus tech-debt

# Comprehensive analysis (default)
@winston *analyze-architecture . --focus all
```

---

## What Gets Analyzed

### 1. Codebase Structure Discovery
- Monorepo vs standalone detection
- Package structure and organization
- Configuration files
- Documentation presence

### 2. Project Type Detection
- Frontend (React, Vue, Angular, Svelte)
- Backend (Node.js, Express, NestJS, Fastify)
- Fullstack (Next.js, Remix, SvelteKit)
- Monorepo (multiple packages)

### 3. Technology Stack Analysis
- **Backend:** Runtime, framework, ORM, database, caching, job queues
- **Frontend:** Framework, UI library, state management, data fetching
- **DevOps:** Package manager, monorepo tools, CI/CD, linting
- **All versions extracted** from package.json and lock files

### 4. Architectural Pattern Identification
- Domain-Driven Design (DDD)
- CQRS (Command Query Responsibility Segregation)
- Layered Architecture
- Microservices
- Event-Driven Architecture
- Hexagonal/Ports & Adapters
- Repository Pattern

### 5. Domain Model Evaluation (if DDD/CQRS)
- Entities and aggregate roots
- Value objects
- Domain events
- Application services
- Command handlers
- Query handlers

### 6. API Architecture Assessment
- API style (REST, GraphQL, tRPC, gRPC)
- Endpoint count
- Middleware stack
- Authentication method
- Authorization approach
- API versioning

### 7. Data Architecture Review
- Database schema analysis
- Index optimization
- Multi-tenancy design
- Caching strategy (Redis, in-memory)
- Real-time architecture (WebSocket, SSE)

### 8. Security Posture Analysis
- Authentication (JWT, OAuth, Clerk, Auth0)
- Authorization (RBAC, ABAC)
- Security headers (Helmet, CORS, CSP)
- Input validation (Zod, Joi, Yup)
- SQL injection protection
- XSS protection
- Secrets management

### 9. Performance Characteristics
- Database indexing
- Caching implementation
- Code splitting
- Memoization
- Query optimization
- Performance score (0-100)

### 10. Scalability Assessment
- Horizontal scaling readiness
- Vertical scaling concerns
- Stateless design
- Distributed caching
- Background job processing
- Scalability score (0-100)

### 11. Technical Debt Identification
- TypeScript error count and breakdown
- Deprecated patterns
- Missing tests
- Documentation gaps
- Technical debt priority (high/medium/low)

### 12. Testing Infrastructure
- Unit test coverage
- Integration test coverage
- E2E test setup (Playwright, Cypress)
- Test framework (Vitest, Jest)
- Coverage tracking

### 13. External Integrations
- Third-party services identified
- Integration methods (REST, SDK, webhooks)
- SDK versions

### 14. Production Readiness Score
- **8 quality dimensions** weighted and scored:
  - Architecture Quality (20%)
  - Code Quality (15%)
  - Security (15%)
  - Performance (10%)
  - Scalability (10%)
  - Maintainability (15%)
  - Testing (10%)
  - Monitoring (5%)

### 15. Comprehensive Report
- Executive summary
- Detailed findings per dimension
- Technical debt analysis
- Prioritized recommendations
- Risk assessment
- Production readiness checklist

---

## Output Report Structure

The generated report includes:

```markdown
# {Project Name} - Architecture Analysis Report

## Executive Summary
- Project overview
- Overall assessment (⭐⭐⭐⭐⭐)
- Production readiness score (0-100)
- Key verdict

## 1. Architecture Overview
- Project structure
- Architecture pattern
- Key characteristics

## 2. Technology Stack
- Backend stack with versions
- Frontend stack with versions
- Database & infrastructure

## 3. Domain Model Analysis
- Entities, value objects, aggregates
- Domain events
- CQRS handlers

## 4-7. [Additional Sections]

## 8. Quality Assessment
- 8 dimensions scored (0-100 each)
- Strengths and weaknesses
- Quality indicators

## 9. Technical Debt Analysis
- Current debt items
- Priority breakdown
- Effort estimates

## 10. External Integrations

## 11. Key Recommendations
- 🔴 HIGH PRIORITY (with effort)
- 🟡 MEDIUM PRIORITY (with effort)
- 🟢 LOW PRIORITY (with effort)

## 12. Risk Assessment
- Technical risks
- Operational risks
- Mitigation strategies

## 13. Production Readiness Checklist
- ✅ Completed items (%)
- 🔧 Needs completion (%)

## 14. Final Verdict
- Overall score with star rating
- Category breakdown table
- Success probability

## 15. Conclusion
- Key achievements
- Critical path to production
- Bottom line recommendation
```

---

## Use Cases

### Use Case 1: Onboarding to Existing Project

**Scenario:** You joined a new team and need to understand the codebase architecture.

```bash
# Run comprehensive analysis
@winston *analyze-architecture

# Review the generated report
# File: docs/architecture-analysis-{timestamp}.md

# Ask follow-up questions
@winston What architectural patterns are used in this codebase?
@winston How is multi-tenancy implemented?
```

**Benefits:**
- Understand project structure quickly
- Identify architectural patterns
- Know technology stack and versions
- See quality scores and technical debt

---

### Use Case 2: Pre-Production Readiness Assessment

**Scenario:** You need to assess if the application is ready for production.

```bash
# Run comprehensive analysis
@winston *analyze-architecture

# Review production readiness score
# Check: Critical items in recommendations
# Verify: No critical security issues
```

**Decision criteria:**
- Score 90-100: ✅ Production ready
- Score 80-89: ⚠️ Minor improvements needed
- Score 70-79: ⚠️ Moderate improvements needed
- Score <70: ❌ Significant work required

---

### Use Case 3: Security Audit

**Scenario:** You need to assess security posture before deployment.

```bash
# Run focused security analysis
@winston *analyze-architecture . --focus security

# Review security-specific report
# Check: Authentication, authorization, encryption
# Verify: No exposed secrets, SQL injection protection
# Validate: Input validation, XSS protection
```

**Action items from report:**
- Address all 🔴 HIGH PRIORITY security issues
- Plan remediation for ⚠️ warnings
- Document security controls

---

### Use Case 4: Performance Investigation

**Scenario:** Application is slow, need to find bottlenecks.

```bash
# Run focused performance analysis
@winston *analyze-architecture . --focus performance

# Review findings:
# - Database index optimization
# - Caching strategy
# - Code splitting
# - Query performance
```

**Action items:**
- Add missing database indexes
- Implement caching layer
- Optimize slow queries
- Enable code splitting

---

### Use Case 5: Modernization Planning

**Scenario:** Legacy codebase needs modernization.

```bash
# Analyze current state
@winston *analyze-architecture

# Review technical debt section
# Note deprecated patterns
# Check technology versions
# Assess migration risks

# Then create modernization plan
@alex *create-task-spec "Modernize {identified-issues}"
```

---

## Interpreting Quality Scores

### Architecture Quality (20% weight)
- **95-100:** World-class architecture (DDD, CQRS, clean boundaries)
- **85-94:** Excellent architecture (clear patterns, good separation)
- **70-84:** Good architecture (recognizable patterns, some coupling)
- **50-69:** Fair architecture (basic structure, needs improvement)
- **0-49:** Poor architecture (spaghetti code, no clear patterns)

### Code Quality (15% weight)
- **95-100:** Excellent (>95% type-safe, clean code, standards enforced)
- **85-94:** Very good (>90% type-safe, mostly clean)
- **70-84:** Good (>80% type-safe, some issues)
- **50-69:** Fair (<80% type-safe, many issues)
- **0-49:** Poor (significant type errors, inconsistent)

### Security (15% weight)
- **90-100:** Enterprise-grade (auth, authorization, encryption, compliance)
- **80-89:** Very good (strong security, minor gaps)
- **70-79:** Good (basic security, some gaps)
- **50-69:** Fair (security gaps, needs work)
- **0-49:** Critical (major vulnerabilities)

### Performance (10% weight)
- **85-100:** Excellent (optimized indexes, caching, code splitting)
- **70-84:** Good (some optimization, basic caching)
- **50-69:** Fair (minimal optimization)
- **0-49:** Poor (no optimization, bottlenecks)

### Scalability (10% weight)
- **85-100:** Excellent (stateless, distributed, load balancer ready)
- **70-84:** Good (mostly stateless, basic caching)
- **50-69:** Fair (some stateful components)
- **0-49:** Poor (stateful, no distributed components)

### Maintainability (15% weight)
- **95-100:** Excellent (clear structure, comprehensive docs, standards)
- **85-94:** Very good (good structure, decent docs)
- **70-84:** Good (recognizable structure, some docs)
- **50-69:** Fair (basic structure, minimal docs)
- **0-49:** Poor (unclear structure, no docs)

### Testing (10% weight)
- **85-100:** Excellent (high coverage, all test types, CI)
- **70-84:** Good (unit + integration, some E2E)
- **50-69:** Fair (basic unit tests)
- **0-49:** Poor (minimal or no tests)

### Monitoring (5% weight)
- **85-100:** Excellent (distributed tracing, centralized logs, alerting)
- **70-84:** Good (basic metrics, some logging)
- **50-69:** Fair (minimal metrics)
- **0-49:** Poor (no monitoring)

---

## Production Readiness Score Interpretation

| Score | Rating | Status | Interpretation |
|-------|--------|--------|----------------|
| 90-100 | ⭐⭐⭐⭐⭐ | Excellent | Production ready, world-class quality |
| 80-89 | ⭐⭐⭐⭐ | Very Good | Production ready with minor improvements |
| 70-79 | ⭐⭐⭐⭐ | Good | Production possible with moderate improvements |
| 60-69 | ⭐⭐⭐ | Fair | Significant work required before production |
| 50-59 | ⭐⭐ | Poor | Major rework needed |
| 0-49 | ⭐ | Critical | Not production ready |

---

## Recommendation Priority Levels

### 🔴 HIGH PRIORITY (Immediate - 1-2 weeks)
- Critical for production readiness
- Blocks deployment or creates significant risk
- Must be addressed before going live
- Typical effort: Hours to 1 week per item

**Examples:**
- Complete type error remediation
- Implement comprehensive monitoring
- Add database read replicas
- Fix critical security vulnerabilities

### 🟡 MEDIUM PRIORITY (Next Quarter)
- Important for long-term success
- Should be addressed after launch
- Improves quality and maintainability
- Typical effort: 1-3 weeks per item

**Examples:**
- Enhance real-time architecture
- Expand test coverage
- Infrastructure as Code
- Advanced caching strategy

### 🟢 LOW PRIORITY (Future Enhancements)
- Nice to have improvements
- Can be addressed as time permits
- Adds features or polish
- Typical effort: 2-4 weeks per item

**Examples:**
- Event sourcing for critical aggregates
- GraphQL API layer
- Performance micro-optimizations
- Additional monitoring dashboards

---

## Integration with Other Commands

### Workflow: Analyze → Document → Review → Implement

```bash
# Step 1: Analyze existing codebase (brownfield)
@winston *analyze-architecture

# Step 2: Create formal architecture document (if needed)
@winston *create-architecture docs/prd.md --existing docs/architecture-analysis.md

# Step 3: Validate the architecture
@winston *validate-architecture docs/architecture.md

# Step 4: Review for quality and risks
@winston *review-architecture docs/architecture.md

# Step 5: Implement recommendations
@james *implement <recommendation-from-analysis>
```

---

## Slash vs Wildcard: Which to Use?

### Understanding the Difference

Both invocation methods execute the **same skill** (`.claude/skills/planning/analyze-architecture/SKILL.md`), but they provide different user experiences:

---

### Wildcard Command: `@winston *analyze-architecture`

**What happens:**
1. Loads winston-architect subagent with full persona
2. Winston provides architectural context and guidance
3. Routes to analysis skill with expert interpretation
4. Winston explains results in architect persona
5. Provides follow-up recommendations and next steps

**Example interaction:**
```bash
User: @winston *analyze-architecture

Winston: I'll analyze your existing codebase architecture...

[Winston provides context]
Let me assess your project structure first...

Project Type: Monorepo (4 packages)
Complexity: High (DDD/CQRS implementation)

I'll perform a comprehensive analysis across 8 quality dimensions.
This will take about 2-5 minutes depending on codebase size.

[Executes analysis]

✅ Analysis complete!

**Key Findings:**
- World-class DDD/CQRS architecture (95/100)
- Production ready with minor improvements
- 4 high-priority recommendations

**My Recommendation as your architect:**
Focus on these 3 items first:
1. Complete type error remediation (3-4 hours)
2. Add comprehensive monitoring (1 week)
3. Implement read replicas (2-3 days)

Would you like me to help create a plan for addressing these?
Or should I validate your existing architecture document?
```

**Characteristics:**
- ✅ Conversational and contextual
- ✅ Expert guidance and interpretation
- ✅ Architect persona active
- ✅ Follow-up suggestions provided
- ✅ Can chain to other winston commands
- ⚠️ More verbose output
- ⚠️ Slightly longer execution time

---

### Slash Command: `/analyze-architecture`

**What happens:**
1. Directly executes analysis skill
2. No subagent context or persona
3. Returns raw analysis results
4. Quick and straightforward

**Example interaction:**
```bash
User: /analyze-architecture

Claude: [Executes skill directly]

✅ Analysis complete

Project Type: Monorepo (4 packages)
Architecture Patterns: DDD, CQRS, Layered, Event-Driven
Production Readiness Score: 85/100 ⭐⭐⭐⭐

Quality Scores:
- Architecture: 95/100
- Code Quality: 90/100
- Security: 88/100
- Performance: 78/100
- Scalability: 82/100
- Maintainability: 95/100
- Testing: 85/100
- Monitoring: 60/100

Report: docs/architecture-analysis-2025-11-04.md
```

**Characteristics:**
- ✅ Fast and direct
- ✅ Minimal output
- ✅ Good for automation/scripts
- ✅ No conversation overhead
- ⚠️ No expert guidance
- ⚠️ No follow-up suggestions
- ⚠️ No architectural context

---

### Technical Flow Comparison

#### Wildcard Command Flow
```
User → @winston *analyze-architecture
  ↓
Loads winston-architect subagent
  ↓
Winston's agent logic processes command
  ↓
Winston routes to skill with context
  ↓
Executes: .claude/skills/planning/analyze-architecture/SKILL.md
  ↓
Winston interprets results in architect persona
  ↓
Winston provides contextual recommendations
  ↓
Winston suggests next steps
```

#### Slash Command Flow
```
User → /analyze-architecture
  ↓
SlashCommand parser reads .claude/commands/analyze-architecture.md
  ↓
Routes directly to skill
  ↓
Executes: .claude/skills/planning/analyze-architecture/SKILL.md
  ↓
Returns results
```

---

### When to Use Wildcard Command (`@winston`)

**Use `@winston *analyze-architecture` when:**

✅ **First time analyzing** - You want guidance and context
✅ **Architectural decisions** - You need expert interpretation
✅ **Learning** - You're new to the command or architecture analysis
✅ **Conversational** - You're in an architecture-focused discussion
✅ **Follow-up actions** - You might need related commands (validate, review, create)
✅ **Recommendations** - You want Winston to prioritize and explain actions
✅ **Persona matters** - You value the architect expertise and personality

**Example scenarios:**
- "I need to understand this legacy codebase and decide if it's production-ready"
- "Help me assess our architecture and recommend improvements"
- "I'm new to this project, what should I know about its architecture?"
- "Analyze our security posture and tell me what to fix first"

---

### When to Use Slash Command (`/`)

**Use `/analyze-architecture` when:**

✅ **Quick analysis** - You just need the report, no conversation
✅ **Automation** - Running in scripts or CI/CD pipelines
✅ **Re-analysis** - You've run this before and know what to expect
✅ **Known parameters** - You know exactly what options you want
✅ **Raw data** - You want results without interpretation
✅ **Experienced user** - You're familiar with the output format

**Example scenarios:**
- "Quick analysis before I commit these changes"
- "Generate report for the weekly status meeting"
- "CI/CD pipeline needs production readiness score"
- "I just need to see if the score improved after my changes"

---

### Real-World Analogy

**Slash Command (`/`)** = Using a calculator app
- You know what calculation you want
- You just need the answer
- Quick in, quick out
- No explanation needed

**Wildcard Command (`@winston`)** = Consulting with an architect
- They explain the problem
- They guide you through the analysis
- They provide context and alternatives
- They help you understand the result
- They suggest next steps and priorities

---

### Side-by-Side Comparison

| Aspect | Wildcard (`@winston`) | Slash (`/`) |
|--------|----------------------|-------------|
| **Execution** | Via winston-architect subagent | Direct to skill |
| **Output Style** | Conversational, guided | Raw, concise |
| **Context** | Full architect persona | No persona |
| **Guidance** | Expert recommendations | Just results |
| **Follow-up** | Suggests next actions | None |
| **Verbosity** | More verbose | Minimal |
| **Speed** | Slightly slower | Faster |
| **Best for** | First-time use, learning | Re-runs, automation |
| **Persona** | Architect expertise active | No persona |
| **Interpretation** | Winston explains results | User interprets |

---

### My Recommendation for Analyze-Architecture

**For your first analysis:** Use `@winston *analyze-architecture`
- You'll get context, guidance, and recommendations
- Winston will help you understand what the scores mean
- You'll know exactly what to do next

**For subsequent analyses:** Either works, but consider:
- Use `@winston` if you want updated recommendations
- Use `/` if you just want to check the score

**For automation/CI/CD:** Always use `/analyze-architecture`
- Faster execution
- Consistent output format
- Easier to parse results

---

### Both Are Valid!

There's no "wrong" choice - **both execute the same skill** and produce the same analysis report. The difference is purely in the **user experience**:

- **Wildcard** = Guided experience with expert architect
- **Slash** = Direct execution with raw results

Choose based on your needs at the moment! 🎯

---

## Tips for Best Results

### 1. Run from Project Root
```bash
# ✅ Good - Analyzes entire project
@winston *analyze-architecture

# ⚠️ Limited - Only analyzes backend package
@winston *analyze-architecture packages/backend
```

### 2. Review Full Report
- Don't just look at the score
- Read the detailed findings
- Understand the "why" behind recommendations
- Check the risk assessment

### 3. Prioritize Actions
- Address all 🔴 HIGH PRIORITY items first
- Plan 🟡 MEDIUM PRIORITY for next quarter
- Defer 🟢 LOW PRIORITY items

### 4. Use Focus Mode for Deep Dives
```bash
# When investigating specific concerns
@winston *analyze-architecture . --focus security
@winston *analyze-architecture . --focus performance
@winston *analyze-architecture . --focus tech-debt
```

### 5. Generate JSON for Automation
```bash
# For CI/CD integration
@winston *analyze-architecture . --output json

# Parse JSON in scripts
jq '.production_readiness_score' docs/architecture-analysis.json
```

---

## Frequently Asked Questions

### Q: How long does analysis take?
**A:** Typically 2-5 minutes depending on codebase size.

### Q: Can I analyze a specific package in a monorepo?
**A:** Yes, specify the path: `@winston *analyze-architecture packages/backend`

### Q: What if no architecture patterns are found?
**A:** Winston will still analyze structure, tech stack, and provide recommendations for improvement.

### Q: Can I re-run analysis after making changes?
**A:** Yes! Run periodically to track improvement over time.

### Q: What format is the report?
**A:** Markdown by default (human-readable), optionally JSON (machine-readable).

### Q: Where is the report saved?
**A:** `docs/architecture-analysis-{timestamp}.md` (and `.json` if requested)

### Q: Can I customize the analysis?
**A:** Use `--focus` to deep-dive on specific areas (security, performance, etc.)

### Q: Does it modify my code?
**A:** No, it's read-only analysis. No code changes are made.

---

## Next Steps After Analysis

1. **Review the report** - Read the full analysis, not just the score
2. **Share with team** - Discuss findings and priorities
3. **Address critical items** - Fix 🔴 HIGH PRIORITY issues first
4. **Plan improvements** - Schedule 🟡 MEDIUM PRIORITY work
5. **Track progress** - Re-run analysis periodically to measure improvement

---

## Example: Complete Analysis Output

```bash
User: @winston *analyze-architecture

Winston: Analyzing existing codebase architecture...

[Discovers codebase structure]
Project Type: Monorepo (4 packages detected)

[Analyzes technology stack]
Backend: Node.js 20, TypeScript 5.8, Express 4.18, Prisma 6.9
Frontend: React 19, Material-UI 7.1, TanStack Query 5.81

[Identifies architectural patterns]
✅ Domain-Driven Design
✅ CQRS
✅ Layered Architecture
✅ Event-Driven
✅ Repository Pattern

[Calculates quality scores]
Architecture Quality: 95/100 ⭐⭐⭐⭐⭐
Code Quality: 90/100 ⭐⭐⭐⭐
Security: 88/100 ⭐⭐⭐⭐
Performance: 78/100 ⭐⭐⭐⭐
Scalability: 82/100 ⭐⭐⭐⭐
Maintainability: 95/100 ⭐⭐⭐⭐⭐
Testing: 85/100 ⭐⭐⭐⭐
Monitoring: 60/100 ⭐⭐⭐

Production Readiness Score: 85/100 ⭐⭐⭐⭐

[Identifies technical debt]
Technical Debt: 283 TypeScript errors (94.8% resolved)

[Generates recommendations]
🔴 HIGH PRIORITY (1-2 weeks):
1. Complete type error remediation (3-4 hours)
2. Implement comprehensive monitoring (1 week)
3. Add database read replicas (2-3 days)

🟡 MEDIUM PRIORITY (Next quarter):
4. Enhance real-time architecture (1 week)
5. Expand test coverage (2-3 weeks)

**Final Verdict:** ⭐⭐⭐⭐⭐ Excellent Architecture
Production-ready with minor enhancements needed.

✅ Report: docs/architecture-analysis-2025-11-04.md
```

---

**Related Commands:**
- `/design-architecture` - Create architecture from requirements
- `/validate-architecture` - Validate architecture document
- `/review-architecture` - Peer review architecture

**Related Skills:**
- `create-architecture` - Design new architecture
- `validate-architecture` - Quality validation
- `architecture-review` - Peer review

---

*Winston is ready to analyze your existing architecture!* 🔍
