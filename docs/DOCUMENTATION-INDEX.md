# BMAD Enhanced Documentation Index

**Version:** 5.0 (Simplified)
**Last Updated:** 2025-11-10
**Status:** Documentation simplified - unnecessary files removed

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Quick Start Guides](#quick-start-guides)
3. [Core Documentation](#core-documentation)
4. [Architecture & Design](#architecture--design)
5. [Development Guides](#development-guides)
6. [Production Guides](#production-guides)
7. [API Reference](#api-reference)
8. [Workflow Guides](#workflow-guides)
9. [Advanced Topics](#advanced-topics)

---

## Getting Started

**Start here if you're new to BMAD Enhanced:**

### 🎯 Essential First Steps

| Guide | Description | Read Time |
|-------|-------------|-----------|
| **[README.md](../README.md)** ⭐ | Project overview and quick start | 5 min |
| **[CHOOSING-YOUR-APPROACH.md](./CHOOSING-YOUR-APPROACH.md)** ⭐ **NEW** | Which approach to use (Direct Skills vs Subagents) | 10 min |
| **[QUICK-START.md](./QUICK-START.md)** ⭐ | Get started in 10 minutes | 10 min |
| **[INSTALLATION-GUIDE.md](./INSTALLATION-GUIDE.md)** | Installation and setup | 15 min |
| **[WHY-BMAD-ENHANCED.md](./WHY-BMAD-ENHANCED.md)** | Vision and benefits | 10 min |

### 📚 Comprehensive User Documentation

| Guide | Description | Lines | Read Time |
|-------|-------------|-------|-----------|
| **[USER-GUIDE.md](./USER-GUIDE.md)** ⭐ | Complete user manual for all agents | 1,878 | 45 min |
| **[WORKFLOW-GUIDE.md](./WORKFLOW-GUIDE.md)** ⭐ | 15+ detailed workflow scenarios | 3,360 | 60 min |
| **[BEST-PRACTICES.md](./BEST-PRACTICES.md)** ⭐ | World-class patterns & anti-patterns | 1,103 | 30 min |
| **[TROUBLESHOOTING.md](./TROUBLESHOOTING.md)** ⭐ | Common issues & solutions | 1,309 | 20 min |

---

## Quick Start Guides

Learn how to use each subagent with practical examples:

### Core Subagents

- **[quickstart-alex.md](./quickstart-alex.md)** - Alex (Planner) - 5 commands
  - Create task specs, break down epics, estimate stories, refine requirements, plan sprints

- **[quickstart-james.md](./quickstart-james.md)** - James (Developer) - 7 commands
  - Implement features, fix bugs, run tests, refactor, apply QA fixes, debug, explain code
  - Framework-agnostic testing (Jest, Pytest, JUnit, GTest, Cargo, Go)

- **[quickstart-quinn.md](./quickstart-quinn.md)** - Quinn (Quality) - 5 commands
  - Review code, assess NFRs, validate quality gates, trace requirements, assess risks

- **[quickstart-winston.md](./quickstart-winston.md)** - Winston (Architect) - 5 commands
  - Analyze architecture, design systems, review architecture, create ADRs, consult

- **[quickstart-orchestrator.md](./quickstart-orchestrator.md)** - Orchestrator - 2 commands
  - Execute complete workflows, coordinate multiple subagents

### Additional Resources

- **[HOW-TO-USE-AGENTS-CORRECTLY.md](./HOW-TO-USE-AGENTS-CORRECTLY.md)** - Correct command syntax
- **[AGENT-ROUTING-GUIDE.md](./AGENT-ROUTING-GUIDE.md)** - Understanding agent routing

---

## Core Documentation

### Command References

- **[COMMAND-REFERENCE-SUMMARY.md](./COMMAND-REFERENCE-SUMMARY.md)** ⭐ - Quick command lookup (50+ commands) - 5 min
- **[AGENT-REFERENCE.md](./AGENT-REFERENCE.md)** ⭐ - Complete command reference (detailed) - 30 min

### Current Status

- **[ROADMAP.md](./ROADMAP.md)** - Complete project roadmap with all phases
- **[ESSENTIAL-DEVELOPMENT-DOCS.md](./ESSENTIAL-DEVELOPMENT-DOCS.md)** - Critical files for developers

---

## Architecture & Design

### V2 Hybrid Architecture Documentation ⭐ **NEW**

**Essential Reading:**
- **[COMMAND-ROUTING-GUIDE.md](./COMMAND-ROUTING-GUIDE.md)** ⭐ **Start Here** - Complete routing guide (300+ lines)
  - When to use skill-direct vs subagent commands
  - Decision trees and examples
  - Command reference (50+ commands)
  - Troubleshooting guide

- **[HYBRID-ARCHITECTURE-IMPLEMENTATION.md](./HYBRID-ARCHITECTURE-IMPLEMENTATION.md)** - Implementation summary
  - Problem statement and solution
  - Implementation details
  - Testing results
  - Files created/modified

- **[COMMAND-AUDIT.md](./COMMAND-AUDIT.md)** - Complete command audit
  - Categorization (skill-direct vs subagent)
  - Migration strategy
  - Action items

### V2 Core Architecture

- **[V2-ARCHITECTURE.md](./V2-ARCHITECTURE.md)** ⭐ **Master Reference** - Complete V2 architecture
  - 3-layer architecture (Primitives → Skills → Subagents)
  - Hybrid execution paths (skill-direct + subagent)
  - Intelligent routing and complexity assessment
  - Guardrails framework
  - Quality gates
  - Telemetry and observability

- **[3-layer-architecture-for-skills.md](./3-layer-architecture-for-skills.md)** - Deep dive into skill architecture

### Architecture Documentation

- **[architecture/ARCHITECTURE-OVERVIEW.md](./architecture/ARCHITECTURE-OVERVIEW.md)** - System architecture overview (844 lines)
- **[architecture/COMPONENT-CATALOG.md](./architecture/COMPONENT-CATALOG.md)** - Complete component catalog (872 lines)

---

## Development Guides

### Standards & Templates

- **[standards.md](./standards.md)** - Development standards and conventions
- **[skill-refactoring-template.md](./skill-refactoring-template.md)** - Template for skill refactoring

### Testing

- **[FRAMEWORK-SUPPORT-MATRIX.md](./FRAMEWORK-SUPPORT-MATRIX.md)** - Test framework support (Jest, Pytest, JUnit, etc.)

### Workflow Development

- **[EXAMPLE-WORKFLOWS.md](./EXAMPLE-WORKFLOWS.md)** - 11 copy-paste ready workflows
- **[ADVANCED-WORKFLOW-CUSTOMIZATION.md](./ADVANCED-WORKFLOW-CUSTOMIZATION.md)** ⭐ **NEW** - Advanced workflow customization (2,800 lines)
  - Custom skill creation
  - Workflow orchestration patterns
  - Command chaining & pipelines
  - Custom subagent development
  - Integration with external tools
  - Real-world examples

### Subagent Development

- **[SUBAGENT-SKILL-LOADING-FIX.md](./SUBAGENT-SKILL-LOADING-FIX.md)** ⚠️ **CRITICAL** - How subagents must load skills
  - Common mistake: Using Read() instead of Skill() tool
  - Correct skill invocation patterns
  - Fix templates for agent files
  - Command-to-skill mapping examples

### Brownfield Projects

- **[BROWNFIELD-GETTING-STARTED.md](./BROWNFIELD-GETTING-STARTED.md)** - Onboarding brownfield projects
- **[brownfield-workflow-guide.md](./brownfield-workflow-guide.md)** - Brownfield architecture analysis and improvement

---

## Production Guides

### Deployment & Operations

- **[PRODUCTION-DEPLOYMENT-GUIDE.md](./PRODUCTION-DEPLOYMENT-GUIDE.md)** - Deployment procedures
- **[PRODUCTION-MONITORING-GUIDE.md](./PRODUCTION-MONITORING-GUIDE.md)** - Monitoring and observability
- **[PRODUCTION-READINESS-CHECKLIST.md](./PRODUCTION-READINESS-CHECKLIST.md)** - 209-item production checklist
- **[PRODUCTION-SECURITY-REVIEW.md](./PRODUCTION-SECURITY-REVIEW.md)** - Security review and hardening

### Performance & Optimization

- **[PERFORMANCE-TUNING-GUIDE.md](./PERFORMANCE-TUNING-GUIDE.md)** ⭐ **NEW** - Performance tuning guide (2,000 lines)
  - Quick wins (30-70% improvement)
  - Configuration optimization
  - Command-level optimization
  - Caching strategies
  - Resource management
  - Monitoring & profiling

---

## API Reference

### Error Handling

- **[ERROR-CODES.md](./ERROR-CODES.md)** ⭐ **NEW** - Complete error codes reference (1,400 lines)
  - Error categories and severity levels
  - 30+ specific error codes
  - Remediation steps for each error
  - Exit codes for all commands
  - Error handling best practices

### Parameters & Functions

- **[api/PARAMETER-DOCUMENTATION.md](./api/PARAMETER-DOCUMENTATION.md)** ⭐ **NEW** - Complete parameter documentation (2,100 lines)
  - All utility function parameters
  - Type specifications
  - Validation rules
  - Return value structures
  - Usage examples

---

## Workflow Guides

### Complete Workflows

- **[WORKFLOW-GUIDE.md](./WORKFLOW-GUIDE.md)** ⭐ - 15+ detailed workflow scenarios (3,360 lines)
  - Feature implementation
  - Bug fixing
  - Code review
  - Architecture design
  - Quality validation

- **[EXAMPLE-WORKFLOWS.md](./EXAMPLE-WORKFLOWS.md)** - 11 copy-paste ready workflows
  - Quick reference
  - Common patterns
  - Best practices

### UX Improvements

- **[UX-IMPROVEMENTS-GUIDE.md](./UX-IMPROVEMENTS-GUIDE.md)** - UX tools and improvements
  - Interactive command wizard
  - Progress visualization
  - Error handling

---

## Advanced Topics

### Migration

- **[MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md)** ⭐ **NEW** - Migration from BMAD v4 to Enhanced (1,900 lines)
  - Breaking changes
  - Migration checklist
  - Step-by-step migration
  - Command mapping
  - Configuration migration
  - Rollback plan

### AI & Agent Development

- **[AI-AGENT-HANDOFF-PROMPT.md](./AI-AGENT-HANDOFF-PROMPT.md)** - AI agent handoff procedures

---

## Documentation Statistics

### Current Documentation (38 files)

| Category | Files | Total Lines |
|----------|-------|-------------|
| **Getting Started** | 5 | 2,100+ |
| **Quick Start Guides** | 5 | 1,500+ |
| **Core Documentation** | 6 | 9,500+ |
| **Architecture** | 3 | 2,500+ |
| **Development Guides** | 5 | 4,000+ |
| **Production Guides** | 5 | 3,500+ |
| **API Reference** | 2 | 3,500+ |
| **Workflow Guides** | 3 | 4,000+ |
| **Advanced Topics** | 2 | 2,000+ |
| **Other** | 2 | 800+ |
| **TOTAL** | **38** | **34,000+** |

### Recent Updates (2025-11-10)

**Cleanup:**
- ✅ Removed `docs/archive/` folder (12 historical files)
- ✅ Removed backup files (USER-GUIDE.md.backup)
- ✅ Removed internal analysis files (2 files)
- ✅ Removed historical phase completion docs (1 file)
- ✅ Removed architecture analysis report from root
- ✅ Simplified README.md from 1,230 to 398 lines (68% reduction)

**Improvements:**
- ✅ **NEW:** Created [CHOOSING-YOUR-APPROACH.md](./CHOOSING-YOUR-APPROACH.md) - Beginner-friendly guide
- ✅ Updated README.md with clear two-approach explanation
- ✅ Updated QUICK-START.md with simplified decision guide
- ✅ Updated COMMAND-ROUTING-GUIDE.md with simpler introduction
- ✅ All docs now clearly explain: Direct Skills vs Subagents

### Documentation Quality

- ✅ **100% coverage** of all system features
- ✅ **Production-ready** with comprehensive guides
- ✅ **Up-to-date** as of 2025-11-10
- ✅ **Well-organized** by audience and use case
- ✅ **Cross-referenced** with internal links
- ✅ **Examples-rich** with 100+ code examples
- ✅ **Simplified** - Removed 20+ unnecessary files

---

## Finding What You Need

### By Role

**Developers:**
1. Start with [QUICK-START.md](./QUICK-START.md)
2. Read [USER-GUIDE.md](./USER-GUIDE.md)
3. Reference [quickstart-james.md](./quickstart-james.md)
4. Follow [WORKFLOW-GUIDE.md](./WORKFLOW-GUIDE.md)

**Product Managers:**
1. Start with [WHY-BMAD-ENHANCED.md](./WHY-BMAD-ENHANCED.md)
2. Read [quickstart-alex.md](./quickstart-alex.md)
3. Explore [WORKFLOW-GUIDE.md](./WORKFLOW-GUIDE.md)

**Architects:**
1. Start with [V2-ARCHITECTURE.md](./V2-ARCHITECTURE.md)
2. Read [quickstart-winston.md](./quickstart-winston.md)
3. Review [architecture/ARCHITECTURE-OVERVIEW.md](./architecture/ARCHITECTURE-OVERVIEW.md)

**QA Engineers:**
1. Start with [quickstart-quinn.md](./quickstart-quinn.md)
2. Read [FRAMEWORK-SUPPORT-MATRIX.md](./FRAMEWORK-SUPPORT-MATRIX.md)
3. Follow [PRODUCTION-READINESS-CHECKLIST.md](./PRODUCTION-READINESS-CHECKLIST.md)

**DevOps/SRE:**
1. Start with [PRODUCTION-DEPLOYMENT-GUIDE.md](./PRODUCTION-DEPLOYMENT-GUIDE.md)
2. Read [PRODUCTION-MONITORING-GUIDE.md](./PRODUCTION-MONITORING-GUIDE.md)
3. Reference [PERFORMANCE-TUNING-GUIDE.md](./PERFORMANCE-TUNING-GUIDE.md)

### By Task

**Implementing a Feature:**
[QUICK-START.md](./QUICK-START.md) → [quickstart-alex.md](./quickstart-alex.md) → [quickstart-james.md](./quickstart-james.md) → [WORKFLOW-GUIDE.md](./WORKFLOW-GUIDE.md)

**Fixing a Bug:**
[quickstart-james.md](./quickstart-james.md) → [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) → [ERROR-CODES.md](./ERROR-CODES.md)

**Reviewing Code:**
[quickstart-quinn.md](./quickstart-quinn.md) → [BEST-PRACTICES.md](./BEST-PRACTICES.md) → [PRODUCTION-READINESS-CHECKLIST.md](./PRODUCTION-READINESS-CHECKLIST.md)

**Designing Architecture:**
[quickstart-winston.md](./quickstart-winston.md) → [V2-ARCHITECTURE.md](./V2-ARCHITECTURE.md) → [architecture/ARCHITECTURE-OVERVIEW.md](./architecture/ARCHITECTURE-OVERVIEW.md)

**Deploying to Production:**
[PRODUCTION-DEPLOYMENT-GUIDE.md](./PRODUCTION-DEPLOYMENT-GUIDE.md) → [PRODUCTION-SECURITY-REVIEW.md](./PRODUCTION-SECURITY-REVIEW.md) → [PRODUCTION-MONITORING-GUIDE.md](./PRODUCTION-MONITORING-GUIDE.md)

**Customizing Workflows:**
[EXAMPLE-WORKFLOWS.md](./EXAMPLE-WORKFLOWS.md) → [ADVANCED-WORKFLOW-CUSTOMIZATION.md](./ADVANCED-WORKFLOW-CUSTOMIZATION.md)

**Migrating from BMAD v4:**
[MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md) → [QUICK-START.md](./QUICK-START.md) → [USER-GUIDE.md](./USER-GUIDE.md)

**Troubleshooting Issues:**
[TROUBLESHOOTING.md](./TROUBLESHOOTING.md) → [ERROR-CODES.md](./ERROR-CODES.md) → [PRODUCTION-MONITORING-GUIDE.md](./PRODUCTION-MONITORING-GUIDE.md)

---

## Documentation Maintenance

### Adding New Documentation

1. Create document in appropriate directory
2. Follow naming conventions (UPPERCASE for major docs, lowercase for guides)
3. Add YAML frontmatter with version and date
4. Update this index
5. Add cross-references to related docs
6. Update README.md if major addition

### Updating Existing Documentation

1. Update "Last Updated" date in frontmatter
2. Increment version if significant changes
3. Update cross-references if structure changes
4. Archive old version if major breaking changes

### Removing Old Documentation

When documentation becomes obsolete:
1. Remove the file from the repository
2. Update this index to reflect removal
3. Document the removal in the "Recent Cleanup" section
4. Keep git history for reference if needed

---

## Contributing to Documentation

See [standards.md](./standards.md) for documentation standards and [BEST-PRACTICES.md](./BEST-PRACTICES.md) for writing guidelines.

---

**Maintained by:** BMAD Enhanced Development Team
**Last Review:** 2025-11-10
**Next Review:** 2025-12-10

**Documentation Repository:** All documentation is version-controlled alongside code.
