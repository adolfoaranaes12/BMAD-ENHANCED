---
description: Peer review system architecture for completeness, quality, security risks, scalability bottlenecks, performance optimizations, cost analysis, and provide prioritized action items with pass/fail decision
argument-hint: <architecture-file> [--focus <area>] [--depth <mode>]
allowed-tools: Read, Skill, Bash
---

# Review Architecture Command

Peer review system architecture for quality, risks, and optimization opportunities.

## Usage

```bash
/review-architecture <architecture-file> [--focus <area>] [--depth <mode>]
```

## Parameters

- `architecture-file` - Path to architecture document (required)
- `--focus` - Focus area: `all` (default), `security`, `scalability`, `performance`, `cost`, `completeness`
- `--depth` - Review depth: `quick` (high-level, 5-7 min), `standard` (balanced, 10-12 min), `comprehensive` (rigorous, 15-20 min, **default**)

## Examples

```bash
# Comprehensive review (default - most rigorous)
/review-architecture docs/architecture.md

# Quick review (high-level assessment)
/review-architecture docs/architecture.md --depth quick

# Standard review (balanced)
/review-architecture docs/architecture.md --depth standard

# Security-focused comprehensive review
/review-architecture docs/architecture.md --focus security

# Quick scalability check
/review-architecture docs/architecture.md --focus scalability --depth quick
```

## Depth Modes

**Quick Mode** (`--depth quick`):
- Duration: 5-7 minutes
- Checks: Completeness, critical issues only
- Analysis: High-level scoring, major gaps
- Report: Pass/fail with top 3 issues
- Best For: Initial assessments, fast feedback loops, gate checks

**Standard Mode** (`--depth standard`):
- Duration: 10-12 minutes
- Checks: All dimensions, standard rigor
- Analysis: Balanced depth, practical recommendations
- Report: Full scoring with prioritized action items
- Best For: Regular reviews, pre-implementation validation, iteration cycles

**Comprehensive Mode** (`--depth comprehensive`) [DEFAULT]:
- Duration: 15-20 minutes
- Checks: All dimensions with deep analysis
- Analysis: Rigorous scoring, detailed action items, risk modeling, cost analysis
- Report: Complete assessment with mitigation strategies
- Best For: Production readiness, architecture audits, compliance reviews, enterprise systems

## Architecture Review Process

Execute depth-dependent review workflow (steps adapted by depth mode):

1. Load architecture document and requirements (if available)
2. Completeness check (all required sections present)
3. Technology justification review (alternatives considered, rationale provided)
4. ADR quality assessment (minimum count, quality score per ADR)
5. NFR coverage analysis (performance, scalability, security, reliability, maintainability)
6. Security review (auth, authorization, encryption, compliance) - **depth-dependent rigor**
7. Scalability assessment (growth projections, horizontal scaling, bottlenecks) - **comprehensive mode only**
8. Performance optimization opportunities (caching, CDN, query optimization) - **comprehensive mode only**
9. Cost analysis (infrastructure costs, operational overhead) - **standard+ modes**
10. Risk identification and mitigation strategies - **depth-dependent detail**

## Focus Area Deep-Dives

- **Security**: Vulnerabilities, attack vectors, compliance gaps, security testing
- **Scalability**: Bottleneck analysis, scaling triggers, database scaling, cost scaling
- **Performance**: Response time optimization, caching strategy, CDN, bundle size
- **Cost**: Infrastructure costs, operational overhead, cost-benefit analysis
- **All**: Comprehensive review across all dimensions

## Output Review Report

- Overall architecture quality score (0-100)
- Dimension scores (completeness, tech justification, NFRs, security, scalability, documentation)
- Critical issues (must fix before implementation)
- High priority recommendations (should fix)
- Medium priority recommendations (nice to have)
- Low priority improvements (optional)
- Risk assessment (critical, major, minor risks)
- Action items prioritized by impact

## Validation Scoring

- **Completeness**: 25% weight
- **Technology Justification**: 20% weight
- **NFRs Coverage**: 20% weight
- **Security & Compliance**: 15% weight
- **Scalability Planning**: 10% weight
- **Documentation Quality**: 10% weight

## Pass/Fail Criteria

- **Score ≥85**: PASS (Excellent) - Ready for implementation
- **Score 70-84**: PASS (Good) - Address recommendations, proceed
- **Score 50-69**: FAIL (Needs Work) - Fix critical + high priority, re-validate
- **Score 0-49**: FAIL (Inadequate) - Major rework required

## Quality Gates

- No critical issues blocking implementation
- Validation score ≥70 to proceed
- All NFRs addressed
- Security risks have mitigation plans
- ADR minimum count met

## Implementation

Parse command using structured parser:

```bash
# Use parse_command.py for type-safe parsing
python .claude/skills/bmad-commands/scripts/parse_command.py \
  review-architecture \
  $ARGUMENTS
```

Expected output:
```json
{
  "command": "review-architecture",
  "architecture_file": "docs/architecture.md",
  "focus_area": "all",
  "depth": "comprehensive",
  "skill": "review-architecture"
}
```

Route to architecture-review skill:
Use .claude/skills/quality/architecture-review/SKILL.md with parsed parameters:
- Input: architecture_file (from parser)
- Input: focus_area (from parser, default: "all")
- Input: depth (from parser, default: "comprehensive")

Emit telemetry:
- skill.architecture-review.completed
- Track: validation_score, depth_mode, critical_issues_count, recommendations_count, focus_area, review_result, duration_ms
