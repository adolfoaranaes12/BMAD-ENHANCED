---
description: Analyze existing (brownfield) codebase to discover architecture, assess quality across 8 dimensions, identify technical debt, and provide production readiness score with actionable recommendations
argument-hint: [codebase-path] [--depth <mode>] [--output <format>] [--focus <area>] [--budget <tokens>]
allowed-tools: Read, Bash, Glob, Grep, Skill
---

# Analyze Architecture Command

Analyze existing codebase to discover architecture, assess quality, and identify technical debt.

## Usage

```bash
/analyze-architecture [codebase-path] [--depth <mode>] [--output <format>] [--focus <area>] [--budget <tokens>]
```

## Parameters

- `codebase-path` - Path to codebase root (default: current directory)
- `--depth` - Analysis depth: `quick` (5-7 min, ~50K tokens), `standard` (10-12 min, ~80K tokens), `comprehensive` (15-20 min, ~120K tokens, **default**)
- `--output` - Output format: `markdown` (default), `json`, `both`
- `--focus` - Focus area: `all` (default), `architecture`, `security`, `performance`, `scalability`, `tech-debt`
- `--budget` - Token budget in tokens (default: 120000)

## Examples

```bash
# Comprehensive analysis (default - most detailed and intelligent)
/analyze-architecture

# Quick analysis (fast assessment)
/analyze-architecture --depth quick

# Standard analysis (balanced)
/analyze-architecture --depth standard

# Focus on specific area with comprehensive depth
/analyze-architecture packages/backend --focus security

# JSON output
/analyze-architecture . --output json
```

## Analysis Process

Execute comprehensive 15-step brownfield architecture analysis:

1. Discover codebase structure (folders, packages, monorepo detection)
2. Detect project type (frontend, backend, fullstack, monorepo)
3. Analyze technology stack (frameworks, libraries, databases, tools)
4. Identify architectural patterns (DDD, CQRS, layered, microservices)
5. Evaluate domain model (entities, aggregates, value objects, services)
6. Assess API architecture (REST, GraphQL, endpoints, middleware)
7. Review data architecture (database schema, caching, real-time)
8. Analyze security posture (auth, authorization, encryption, vulnerabilities)
9. Evaluate performance characteristics (bottlenecks, optimization opportunities)
10. Assess scalability (horizontal/vertical scaling, limitations)
11. Identify technical debt (type errors, deprecated patterns, gaps)
12. Review testing infrastructure (unit, integration, E2E coverage)
13. Analyze external integrations (third-party services, APIs)
14. Calculate production readiness score (0-100)
15. Generate comprehensive analysis report

## Quality Dimensions Assessed

- **Architecture Quality** (20%): Patterns, boundaries, modularity
- **Code Quality** (15%): Type safety, consistency, standards
- **Security** (15%): Auth, vulnerabilities, compliance
- **Performance** (10%): Query performance, caching, optimization
- **Scalability** (10%): Horizontal scaling, bottleneck mitigation
- **Maintainability** (15%): Documentation, structure, clarity
- **Testing** (10%): Coverage, automation, quality
- **Monitoring** (5%): Observability, logging, alerting

## Output Report

Comprehensive analysis with:
- Executive Summary (overview, score, verdict)
- Architecture Overview (structure, patterns)
- Technology Stack (with versions)
- Domain Model Analysis (if DDD/CQRS)
- Quality Assessment (8 dimensions scored 0-100)
- Technical Debt Analysis (prioritized)
- Key Recommendations (high/medium/low priority)
- Risk Assessment (technical + operational)
- Production Readiness Checklist
- Final Verdict (score, breakdown, conclusion)

## Production Readiness Score

- **90-100**: Excellent ⭐⭐⭐⭐⭐ (Production Ready)
- **80-89**: Very Good ⭐⭐⭐⭐ (Minor improvements needed)
- **70-79**: Good ⭐⭐⭐⭐ (Moderate improvements needed)
- **60-69**: Fair ⭐⭐⭐ (Significant work required)
- **0-59**: Poor ⭐⭐ (Major rework needed)

## Depth Modes

**Quick Mode** (`--depth quick`):
- Duration: 5-7 minutes
- Token Usage: ~50,000 tokens
- Steps: 1-8 only (structure, type, stack, patterns, quality, tech debt, report, telemetry)
- Best For: Initial assessments, time-sensitive decisions, high-level overviews

**Standard Mode** (`--depth standard`):
- Duration: 10-12 minutes
- Token Usage: ~80,000 tokens
- Steps: 1-12 (excludes deep integration analysis)
- Best For: Regular assessments, iterative development, balanced analysis

**Comprehensive Mode** (`--depth comprehensive`) [DEFAULT]:
- Duration: 15-20 minutes
- Token Usage: ~120,000 tokens
- Steps: All 15 steps with deep analysis, complete integration review
- Best For: Production readiness assessments, architecture audits, detailed planning, enterprise systems

## Implementation

Parse command using structured parser:

```bash
# Use parse_command.py for type-safe parsing
python .claude/skills/bmad-commands/scripts/parse_command.py \
  analyze-architecture \
  $ARGUMENTS
```

Expected output:
```json
{
  "command": "analyze-architecture",
  "codebase_path": ".",
  "depth": "comprehensive",
  "output_format": "markdown",
  "focus_area": "all",
  "token_budget": 120000,
  "skill": "analyze-architecture"
}
```

Route to analyze-architecture skill:
Use .claude/skills/planning/analyze-architecture/SKILL.md with parsed parameters:
- Input: codebase_path (from parser)
- Input: depth (from parser, default: "comprehensive")
- Input: output_format (from parser, default: "markdown")
- Input: focus_area (from parser, default: "all")
- Input: token_budget (from parser, default: 120000)

Emit telemetry:
- skill.analyze-architecture.completed
- Track: project_type, depth_mode, complexity_score, production_readiness_score, tech_debt_count, focus_area, token_usage, analysis_duration_ms
