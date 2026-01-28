# Winston (Architect) Quick Start Guide

**Winston** is BMAD Enhanced's system architect subagent, specializing in architecture design, analysis, and modernization for frontend, backend, and fullstack systems.

---

## Overview

**Role:** System Architect + Technical Design Leader

**When to Use Winston:**
- Analyzing existing codebases (brownfield projects)
- Creating system architecture from requirements
- Comparing multiple architecture options
- Getting conversational architecture advice
- Validating proposed architecture designs
- Reviewing architectural decisions for risks
- Planning migrations or modernizations

**Commands:** 5 architecture commands + 1 slash command

---

## Quick Reference

### Commands

| Command | Purpose | Duration |
|---------|---------|----------|
| `*analyze-architecture` | Analyze existing codebase | 10-15 min |
| `*create-architecture` | Generate architecture from requirements | 12-18 min |
| `*compare-architectures` | Generate 3 options with trade-offs | 8-12 min |
| `*validate-architecture` | Validate architecture completeness | 3-5 min |
| `*review-architecture` | Peer review architecture | 5-8 min |

### Slash Command

| Command | Purpose |
|---------|---------|
| `/winston-consult` | Conversational architecture advisor |

---

## Getting Started

### For Brownfield Projects (Existing Code)

**Step 1: Analyze Your Current Architecture**
```bash
/winston *analyze-architecture .
```

**What you get:**
- Production readiness score (0-100)
- Quality assessment across 8 dimensions
- Technology stack analysis
- Architecture patterns identified
- Technical debt report
- Modernization opportunities (HIGH/MEDIUM/LOW priority)

**Duration:** 10-15 minutes

---

**Step 2: Get Architecture Options**
```bash
/winston *compare-architectures "Scale to 100K users + add real-time features"
```

**What you get:**
- **Option A:** Minimal Changes (fast, low cost, limited scale)
- **Option B:** Moderate Refactor (balanced approach) ✅ Usually recommended
- **Option C:** Full Modernization (best quality, highest cost)
- Trade-offs analysis (cost, timeline, risk, performance, maintainability)
- Clear recommendation with confidence score

**Duration:** 8-12 minutes

---

**Step 3: Get Complete Modernization Plan**
```bash
/orchestrator *workflow modernize . "Your modernization goals"
```

**What you get:**
- Architecture analysis
- Brownfield PRD (current features + gaps)
- 3 architecture options (you choose!)
- Detailed architecture design
- Implementation plan (epic breakdown)

**Duration:** 51 minutes for complete workflow

---

### For Greenfield Projects (New Systems)

**Step 1: Create Architecture from Requirements**
```bash
/winston *create-architecture docs/prd.md
```

**What you get:**
- Complete architecture document
- Technology stack with justifications
- Architecture Decision Records (ADRs)
- Security, performance, scalability design
- Deployment strategy
- Migration approach (if applicable)

**Duration:** 12-18 minutes

---

**Step 2: Validate Architecture**
```bash
/winston *validate-architecture docs/architecture.md
```

**What you get:**
- Completeness checklist
- Quality score (0-100)
- Missing elements identified
- Recommendations for improvement
- Pass/Fail verdict

**Duration:** 3-5 minutes

---

**Step 3: Peer Review**
```bash
/winston *review-architecture docs/architecture.md
```

**What you get:**
- Risk assessment (critical, major, minor)
- Scalability analysis
- Security review
- Performance optimization opportunities
- Cost-benefit analysis
- Prioritized action items

**Duration:** 5-8 minutes

---

## Conversational Mode

### Using `/winston-consult`

**Best for:**
- "I have an idea but don't know where to start"
- "Should I modernize or rewrite my system?"
- Quick technology advice
- Understanding your options

**How it works:**
1. You describe your situation
2. Winston asks clarifying questions
3. Winston routes to appropriate workflow
4. You get tailored recommendations

**Example:**
```bash
/winston-consult "I have a React/Express app. Want to add real-time features and scale to 50K users."
```

**Winston's Response:**
```
I'd love to help! A few questions first:

1. What's your current tech stack? (versions, database, hosting)
2. What problems are you facing? (performance, maintainability, scalability)
3. What's your timeline? (weeks, months, year)
4. What's your budget constraint? (tight, moderate, generous)

[After gathering context]

Based on your answers, I recommend running a complete modernization workflow.
This will:
1. Analyze your current architecture (12 min)
2. Document your features and gaps (8 min)
3. Generate 3 architecture options (10 min)
4. Let you choose the best approach
5. Create detailed implementation plan (6 min)

Shall I proceed?
```

---

## Common Workflows

### Workflow 1: "Understand My Current Architecture"

```bash
# Step 1: Analyze codebase
/winston *analyze-architecture .

# What you get:
# - Production Readiness: 78/100 ⭐⭐⭐⭐
# - Architecture Quality: 85/100
# - Security: 88/100
# - Performance: 65/100 (needs improvement)
# - Top 3 Modernization Opportunities

# Step 2 (Optional): Review specific area
/winston *review-architecture docs/architecture-analysis-*.md --focus security
```

**Use when:** You inherited a codebase and need to understand its current state.

---

### Workflow 2: "Should I Modernize or Rewrite?"

```bash
# Step 1: Get options with trade-offs
/winston *compare-architectures "Your modernization goals"

# What you get:
# - Option A: Modernize current stack (4-6 weeks, $25K-$40K)
# - Option B: Hybrid approach (2-3 months, $60K-$90K) ✅ RECOMMENDED
# - Option C: Complete rewrite (4-6 months, $150K-$200K)

# Step 2: Design chosen option
/winston *create-architecture docs/brownfield-prd.md --option moderate
```

**Use when:** You know you need to improve but don't know the best approach.

---

### Workflow 3: "Complete Modernization from Start to Finish"

```bash
# Run complete workflow (51 minutes)
/orchestrator *workflow modernize . "Scale to 100K users + add real-time"

# Phases:
# 1. Architecture Analysis (winston) ✅
# 2. Brownfield PRD (alex) ✅
# 3. Architecture Comparison (winston) ✅ → You choose option
# 4. Detailed Architecture (winston) ✅
# 5. Implementation Plan (alex) ✅

# Output:
# - Architecture analysis report
# - Brownfield PRD with features/gaps
# - Architecture comparison (3 options)
# - Complete architecture document
# - Epic breakdown with story points
```

**Use when:** You want the complete package from analysis to implementation plan.

---

### Workflow 4: "Design Architecture for New Project"

```bash
# Step 1: Create architecture
/winston *create-architecture docs/prd.md

# Step 2: Validate
/winston *validate-architecture docs/architecture.md

# Step 3: Peer review
/winston *review-architecture docs/architecture.md

# Step 4: Create implementation plan
/alex *breakdown-epic docs/architecture.md
```

**Use when:** Starting a new project and need solid architecture foundation.

---

## Command Details

### `*analyze-architecture`

**Purpose:** Discover and assess existing codebase architecture

**Syntax:**
```bash
/winston *analyze-architecture [codebase-path]
/winston *analyze-architecture . --depth comprehensive
/winston *analyze-architecture packages/backend --focus security
/winston *analyze-architecture . --output json
```

**Parameters:**
- `codebase-path`: Path to analyze (default: current directory)
- `--depth`: `quick` | `standard` (default) | `comprehensive`
- `--focus`: `all` (default) | `architecture` | `security` | `performance` | `scalability` | `tech-debt`
- `--output`: `markdown` (default) | `json` | `both`

**Output:** `docs/architecture-analysis-{timestamp}.md`

**Analysis Includes:**
1. Project structure and organization
2. Technology stack with versions
3. Architecture patterns (DDD, CQRS, layered, microservices)
4. Domain model analysis
5. API architecture
6. Data architecture
7. Security posture
8. Performance characteristics
9. Scalability assessment
10. Technical debt identification
11. Testing infrastructure
12. External integrations
13. Production readiness score (0-100)
14. Prioritized recommendations

**Quality Dimensions Scored (0-100):**
- Architecture Quality (20%)
- Code Quality (15%)
- Security (15%)
- Performance (10%)
- Scalability (10%)
- Maintainability (15%)
- Testing (10%)
- Monitoring (5%)

---

### `*compare-architectures`

**Purpose:** Generate 3 architecture options with comprehensive trade-offs

**Syntax:**
```bash
/winston *compare-architectures "<requirements or goals>"
/winston *compare-architectures "Add real-time features and scale to 50K users"
/winston *compare-architectures docs/current-arch.md "Modernize stack"
```

**Parameters:**
- `requirements`: Your modernization goals, new features, or requirements
- `current_architecture` (optional): Path to current architecture document

**Output:** `docs/architecture-comparison-{timestamp}.md`

**Generates 3 Options:**

**Option A: Minimal Changes**
- Fastest timeline (2-6 weeks)
- Lowest cost ($)
- Lowest risk
- Keep current stack, upgrade versions
- Targeted fixes only
- Limited scalability improvements

**Option B: Moderate Refactor** ✅ Usually Recommended
- Balanced timeline (2-4 months)
- Moderate cost ($$)
- Medium risk
- Strategic improvements
- Selective modernization
- Good scalability

**Option C: Full Modernization**
- Longest timeline (4-8 months)
- Highest cost ($$$)
- Highest risk
- Modern best practices
- Complete redesign
- Excellent scalability

**Trade-offs Analysis:**
- **Cost:** Development + infrastructure + migration + training
- **Timeline:** Planning + development + testing + migration + stabilization
- **Risk:** Technical + migration + team + business (scored 0-100)
- **Performance:** Latency, throughput, concurrency
- **Maintainability:** Code quality, technical debt, future velocity

**Recommendation:**
- Clear recommendation (A, B, or C)
- Confidence score (0-100%)
- Justification based on constraints
- Alternative scenarios

---

### `*create-architecture`

**Purpose:** Generate comprehensive system architecture from requirements

**Syntax:**
```bash
/winston *create-architecture <requirements-file>
/winston *create-architecture docs/prd.md
/winston *create-architecture docs/epic-auth.md --type fullstack
```

**Parameters:**
- `requirements-file`: Path to PRD, epic, or requirements document
- `--type`: `frontend` | `backend` | `fullstack` (auto-detected if not provided)
- `--complexity`: `simple` | `medium` | `complex` (auto-assessed if not provided)

**Output:** `docs/architecture.md` + ADRs in `docs/adrs/`

**Architecture Document Includes:**

**For All Projects:**
- System Overview & Context
- Technology Stack (with justifications)
- Deployment Architecture
- Security Architecture
- Architecture Decision Records (ADRs)

**For Frontend:**
- Component Architecture
- State Management Strategy
- Routing Design
- Styling Approach
- Build & Bundle Strategy

**For Backend:**
- API Design (REST/GraphQL/tRPC)
- Service Layer Architecture
- Data Architecture & Modeling
- Business Logic Organization
- Integration Patterns

**For Fullstack:**
- End-to-End Integration
- API Contracts
- Authentication & Authorization Flow
- Deployment Strategy
- Monorepo/Polyrepo Structure

---

### `*validate-architecture`

**Purpose:** Validate architecture document for completeness and quality

**Syntax:**
```bash
/winston *validate-architecture docs/architecture.md
/winston *validate-architecture docs/architecture.md --strict
```

**Parameters:**
- `architecture-file`: Path to architecture document
- `--strict` (optional): Enforce strict validation rules

**Output:** Validation report with pass/fail verdict

**Validation Checks:**
- All required sections present (varies by project type)
- Technology decisions justified
- NFRs (non-functional requirements) addressed
- Risks identified and mitigated
- Scalability considerations documented
- Security posture defined
- Performance requirements addressed
- At least 3 ADRs documented

**Validation Score:** 0-100
- **90-100:** Excellent (production-ready)
- **80-89:** Very Good (minor improvements)
- **70-79:** Good (moderate improvements)
- **60-69:** Fair (significant work needed)
- **<60:** Poor (major rework required)

**Quality Gate:** Score ≥70 required to proceed to implementation

---

### `*review-architecture`

**Purpose:** Peer review architecture for quality, risks, and optimization opportunities

**Syntax:**
```bash
/winston *review-architecture docs/architecture.md
/winston *review-architecture docs/architecture.md --focus scalability
```

**Parameters:**
- `architecture-file`: Path to architecture document
- `--focus`: `all` (default) | `scalability` | `security` | `performance` | `cost`

**Output:** Comprehensive review report

**Review Analysis:**
- **Scalability:** Bottlenecks, scaling strategies, capacity planning
- **Security:** Vulnerabilities, attack vectors, compliance requirements
- **Performance:** Optimization opportunities, caching strategies, query optimization
- **Maintainability:** Code organization, technical debt risks, team velocity impact
- **Technology Fit:** Alternatives considered, trade-offs, team capabilities
- **Cost:** Infrastructure costs, operational overhead, TCO analysis
- **Risks:** Technical risks, business risks, mitigation strategies

**Risk Assessment:**
- 🔴 **Critical:** Immediate action required
- 🟠 **Major:** Address before production
- 🟡 **Minor:** Nice to have improvements

**Recommendations:**
- Prioritized action items (high/medium/low)
- Alternative approaches
- Cost-benefit analysis
- Implementation roadmap

---

## Integration with Other Subagents

### Winston → Alex (Planner)
```bash
# Winston creates architecture
/winston *create-architecture docs/prd.md

# Hand off to Alex for implementation plan
/alex *breakdown-epic docs/architecture.md
```

### Winston → Quinn (Quality)
```bash
# Winston creates architecture
/winston *create-architecture docs/prd.md

# Quinn validates architecture quality
/quinn *review docs/architecture.md
```

### Winston → Orchestrator
```bash
# Complete workflow with Winston + Alex + Quinn
/orchestrator *workflow modernize . "Your goals"
```

---

## Best Practices

### 1. Start with Analysis (Brownfield)

Always analyze before designing:
```bash
# Step 1: Understand current state
/winston *analyze-architecture .

# Step 2: Based on analysis, decide next steps
# - If score >80: Targeted improvements
# - If score 60-80: Modernization opportunities
# - If score <60: Complete redesign
```

### 2. Compare Options Before Committing

Don't assume one approach is best:
```bash
# Get 3 options with trade-offs
/winston *compare-architectures "Your goals"

# Choose based on your constraints (timeline, budget, risk)
```

### 3. Validate Before Implementation

Catch issues early:
```bash
# Create architecture
/winston *create-architecture docs/prd.md

# Validate immediately
/winston *validate-architecture docs/architecture.md

# Fix gaps before implementation starts
```

### 4. Use Conversational Mode for Clarity

When unsure, start with conversation:
```bash
# Winston asks clarifying questions
/winston-consult "Your situation"

# Then routes to appropriate workflow
```

### 5. Review for Production Readiness

Get peer review before going live:
```bash
# Review architecture
/winston *review-architecture docs/architecture.md

# Address critical and major risks
# Then proceed to implementation
```

---

## Troubleshooting

### "Analysis taking too long"
Use quick mode:
```bash
/winston *analyze-architecture . --depth quick
```

### "Not sure which option to choose"
Use complete workflow with interactive checkpoints:
```bash
/orchestrator *workflow modernize . "Your goals" --interactive
```

### "Need help understanding current architecture"
Start conversationally:
```bash
/winston-consult "I inherited this codebase and need to understand it"
```

### "Architecture validation failed"
Check specific gaps:
```bash
/winston *validate-architecture docs/architecture.md --strict

# Address missing sections identified in report
```

---

## Next Steps

**After Winston's Work:**
1. Review generated architecture/analysis documents
2. Validate architecture completeness
3. Hand off to Alex for implementation planning
4. Hand off to James for implementation
5. Hand off to Quinn for quality review

**Related Guides:**
- [Alex Quick Start](./quickstart-alex.md) - Implementation planning
- [James Quick Start](./quickstart-james.md) - Implementation
- [Quinn Quick Start](./quickstart-quinn.md) - Quality review
- [Orchestrator Quick Start](./quickstart-orchestrator.md) - Complete workflows
- [Brownfield Workflow Guide](./brownfield-workflow-guide.md) - Complete modernization

---

**Winston is ready to design robust, scalable architectures for your applications** 🏗️
