---
description: Generate comprehensive system architecture from requirements (PRD/epic) with technology stack selection, architecture patterns, ADRs, diagrams, security design, and NFR mapping for frontend, backend, or fullstack systems
argument-hint: <requirements-file> [--type <type>] [--depth <mode>] [--complexity <complexity>]
allowed-tools: Read, Write, Edit, Skill, Bash
---

# Design Architecture Command

Generate comprehensive system architecture from requirements with technology selection and ADRs.

## Usage

```bash
/design-architecture <requirements-file> [--type <type>] [--depth <mode>] [--complexity <complexity>]
```

## Parameters

- `requirements-file` - Path to requirements/PRD file (required)
- `--type` - Project type: `auto` (default), `frontend`, `backend`, `fullstack`
- `--depth` - Design depth: `quick` (minimal ADRs, 5-7 min), `standard` (balanced, 10-12 min), `comprehensive` (all details, 15-20 min, **default**)
- `--complexity` - Override complexity: `auto` (default, calculated), `simple`, `medium`, `complex`

## Examples

```bash
# Comprehensive architecture (default - most detailed)
/design-architecture docs/prd.md

# Quick architecture (minimal ADRs, faster)
/design-architecture docs/prd.md --depth quick

# Standard architecture (balanced)
/design-architecture docs/prd.md --depth standard

# Fullstack with comprehensive depth
/design-architecture docs/epic-user-auth.md --type fullstack

# Backend with quick turnaround
/design-architecture docs/requirements.md --type backend --depth quick
```

## Depth Modes

**Quick Mode** (`--depth quick`):
- Duration: 5-7 minutes
- ADRs: Minimum 3 (most critical decisions only)
- Diagrams: Context diagram only
- Details: High-level overview, essential sections
- Best For: Proof of concepts, rapid iterations, initial explorations

**Standard Mode** (`--depth standard`):
- Duration: 10-12 minutes
- ADRs: 5-7 (key architectural decisions)
- Diagrams: Context + Container diagrams
- Details: Balanced coverage, practical depth
- Best For: Regular projects, MVP development, iterative design

**Comprehensive Mode** (`--depth comprehensive`) [DEFAULT]:
- Duration: 15-20 minutes
- ADRs: 8-15 (all major decisions with alternatives)
- Diagrams: Full C4 model (Context, Container, Component, Deployment)
- Details: Complete coverage, production-ready documentation
- Best For: Production systems, complex projects, enterprise architecture

## Architecture Creation Process

Execute comprehensive 10-step workflow (steps adapted by depth mode):

1. Requirements analysis (functional, NFRs, constraints)
2. Project type detection (frontend/backend/fullstack)
3. Complexity assessment (0-100 scoring)
4. Technology stack selection with justification
5. Architecture pattern selection
6. ADR generation (depth-dependent: 3 quick, 5-7 standard, 8-15 comprehensive)
7. NFR architecture mapping (performance, scalability, security)
8. Diagram generation (depth-dependent: 1-4 diagrams)
9. Security architecture design
10. Validation and completeness check

## Output Artifacts

- `docs/architecture.md` - Comprehensive architecture document
- `docs/adrs/ADR-00X-*.md` - Architecture Decision Records
- `docs/diagrams/*.mmd` - Mermaid architecture diagrams
- Architecture summary with key decisions

## Quality Gates

- All required sections present (based on project type)
- Technology stack justified with alternatives
- Minimum ADR count met (simple: 3, medium: 5, complex: 10)
- NFRs addressed (performance, scalability, security, reliability)
- Security considerations documented
- Scalability approach defined

## Architecture Document Sections

**All Project Types:**
- System Overview & Context
- Technology Stack (with justification)
- Deployment Architecture
- Security Architecture
- Architecture Decision Records (ADRs)

**Frontend-Specific:**
- Component Architecture
- State Management Strategy
- Routing Design
- Styling Approach
- Build & Bundle Strategy

**Backend-Specific:**
- API Design (REST/GraphQL/tRPC)
- Service Layer Architecture
- Data Architecture & Modeling
- Business Logic Organization
- Integration Patterns

**Fullstack-Specific:**
- End-to-End Integration
- API Contracts
- Authentication & Authorization Flow
- Deployment Strategy
- Monorepo/Polyrepo Structure

## Implementation

Parse command using structured parser:

```bash
# Use parse_command.py for type-safe parsing
python .claude/skills/bmad-commands/scripts/parse_command.py \
  design-architecture \
  $ARGUMENTS
```

Expected output:
```json
{
  "command": "design-architecture",
  "requirements_file": "docs/prd.md",
  "system_type": "fullstack",
  "depth": "comprehensive",
  "complexity": "auto",
  "skill": "design-architecture"
}
```

Route to create-architecture skill:
Use .claude/skills/planning/create-architecture/SKILL.md with parsed parameters:
- Input: requirements_file (from parser)
- Input: system_type (from parser, default: "auto")
- Input: depth (from parser, default: "comprehensive")
- Input: complexity (from parser, default: "auto")

Emit telemetry:
- skill.create-architecture.completed
- Track: project_type, depth_mode, complexity_score, adrs_count, technologies_count, validation_score, duration_ms
