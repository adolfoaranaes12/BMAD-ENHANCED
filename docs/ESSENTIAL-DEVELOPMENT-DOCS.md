# Essential Development Documentation

**Purpose:** Core documentation for AI agents developing new subagents, primitives, skills, or features
**Last Updated:** 2025-11-04
**Version:** 2.0 (Post-Cleanup)

---

## Current Documentation (11 files)

### Core Architecture (2)
- **3-layer-architecture-for-skills.md** ✅
  - 3-layer architecture design principles
  - Layer 1: Primitives (bmad-commands)
  - Layer 2: Skills (17 with V2 contracts)
  - Layer 3: Subagents (4 with intelligent routing)

- **architecture-claude-code-compliance.md** ✅
  - Claude Code alignment and compliance
  - Integration patterns
  - Best practices

### Active Templates & Guides (3)
- **skill-refactoring-template.md** ✅
  - Skill refactoring guide and template
  - Progressive disclosure pattern
  - V2 contract structure

- **slash-commands-implementation-guide.md** ✅
  - Slash commands implementation guide
  - Command routing patterns

- **BROWNFIELD-GETTING-STARTED.md** ✅
  - Brownfield project onboarding
  - How to integrate BMAD Enhanced into existing projects

### Master Reference (3)
- **V2-ARCHITECTURE.md** ✅ ⭐ **MASTER DOCUMENT**
  - Complete V2 architecture overview
  - 7-step workflow pattern
  - Complexity assessment (0-100 scale)
  - Intelligent routing strategies
  - Guardrails framework
  - Telemetry & observability
  - All subagents and skills reference
  - Performance metrics
  - Best practices

- **standards.md** ✅
  - BMAD Enhanced coding standards
  - Quality requirements
  - Documentation standards

- **terminology-alignment-claude-code.md** ✅
  - Terminology standards and definitions
  - Claude Code alignment
  - Consistent naming conventions

### Planning & Roadmap (2)
- **ROADMAP.md** ✅
  - Complete project roadmap
  - All phases with status
  - Future development plans

- **PHASE-2-COMPLETION.md** ✅
  - Phase 2 final report
  - Complete V2 implementation details
  - All subagent specifications
  - Key achievements and metrics

### Quick Reference (1)
- **DOCUMENTATION-INDEX.md** ✅
  - Master index of all documentation
  - Quick navigation by role
  - Documentation statistics

---

## Usage Guidelines

### When Creating New Subagents

**Essential Reading Order:**
1. **V2-ARCHITECTURE.md** - Understand the V2 pattern
2. **3-layer-architecture-for-skills.md** - Understand layer responsibilities
3. **PHASE-2-COMPLETION.md** - See complete examples of all 4 subagents
4. **standards.md** - Follow coding and documentation standards
5. **terminology-alignment-claude-code.md** - Use correct terminology

**Templates to Follow:**
- Use existing subagents as templates (james-developer-v2.md, alex-planner.md, etc.)
- Follow 7-step workflow pattern
- Implement complexity assessment (5 factors, weighted)
- Define 3 routing options (simple/standard/complex)
- Add comprehensive guardrails
- Include full telemetry structures

### When Creating New Skills

**Essential Reading Order:**
1. **skill-refactoring-template.md** - Skill structure template
2. **V2-ARCHITECTURE.md** - V2 contract requirements
3. **3-layer-architecture-for-skills.md** - Layer 2 responsibilities
4. **standards.md** - Quality standards

**Key Requirements:**
- YAML frontmatter with V2 contract (acceptance, inputs, outputs, telemetry)
- Progressive disclosure (SKILL.md → references/ → assets/)
- Integration with bmad-commands primitives
- Clear acceptance criteria
- Telemetry emission points

### When Creating New Primitives

**Essential Reading Order:**
1. **3-layer-architecture-for-skills.md** - Layer 1 principles
2. **V2-ARCHITECTURE.md** - Primitive requirements
3. **standards.md** - Coding standards

**Key Requirements:**
- Deterministic operations
- JSON I/O format: `{success, outputs, telemetry, errors}`
- No side effects beyond stated purpose
- Comprehensive error handling
- Telemetry emission

### When Implementing New Features

**Essential Reading Order:**
1. **V2-ARCHITECTURE.md** - Architecture overview
2. **ROADMAP.md** - Understand project direction
3. **BROWNFIELD-GETTING-STARTED.md** - Integration patterns
4. **architecture-claude-code-compliance.md** - Compliance requirements

---

## Quick Reference Matrix

| Task | Essential Docs | Templates | Standards |
|------|---------------|-----------|-----------|
| **New Subagent** | V2-ARCHITECTURE.md<br>PHASE-2-COMPLETION.md | james-developer-v2.md<br>alex-planner.md | standards.md<br>terminology-alignment-claude-code.md |
| **New Skill** | skill-refactoring-template.md<br>3-layer-architecture-for-skills.md | implement-feature/SKILL.md<br>review-task/SKILL.md | standards.md<br>V2-ARCHITECTURE.md |
| **New Primitive** | 3-layer-architecture-for-skills.md<br>V2-ARCHITECTURE.md | read_file.py<br>run_tests.py | standards.md |
| **New Feature** | V2-ARCHITECTURE.md<br>ROADMAP.md | BROWNFIELD-GETTING-STARTED.md | architecture-claude-code-compliance.md |
| **Documentation** | DOCUMENTATION-INDEX.md<br>standards.md | skill-refactoring-template.md | terminology-alignment-claude-code.md |

---

## File Locations

All documentation files are located in:
```
/docs/
├── V2-ARCHITECTURE.md ⭐
├── 3-layer-architecture-for-skills.md
├── architecture-claude-code-compliance.md
├── skill-refactoring-template.md
├── slash-commands-implementation-guide.md
├── BROWNFIELD-GETTING-STARTED.md
├── standards.md
├── terminology-alignment-claude-code.md
├── ROADMAP.md
├── PHASE-2-COMPLETION.md
└── DOCUMENTATION-INDEX.md
```

---

## Additional Context Documents

While the 11 files above are essential, these additional documents provide valuable context:

### Quick Start Guides (Learn by Example)
- `quickstart-alex.md` - Alex (Planner) usage examples
- `quickstart-james.md` - James (Developer) usage examples
- `quickstart-quinn.md` - Quinn (Quality) usage examples
- `quickstart-orchestrator.md` - Orchestrator usage examples

### Testing & Validation
- `PHASE-3-INTEGRATION-TEST-REPORT.md` - Comprehensive test results
- `PHASE-3-PERFORMANCE-ANALYSIS.md` - Performance benchmarks

### Production Readiness
- `PRODUCTION-DEPLOYMENT-GUIDE.md` - Deployment procedures
- `PRODUCTION-READINESS-CHECKLIST.md` - Go-live checklist

### Examples
- `EXAMPLE-WORKFLOWS.md` - Practical workflow examples
- `UX-IMPROVEMENTS-GUIDE.md` - UX patterns and improvements

---

## Version History

### Version 2.0 (2025-11-04) - Post-Cleanup
- Removed 6 obsolete files from original list
- Added V2-ARCHITECTURE.md as master reference
- Added PHASE-2-COMPLETION.md for complete examples
- Updated to reflect current documentation structure
- Reduced from 15 to 11 essential files (more focused)

### Version 1.0 (Previous)
- Original list of 15 files
- Included prototype and historical documents
- Mixed current and completed work documentation

---

## Notes for AI Agents

### Critical Success Factors
1. **Always start with V2-ARCHITECTURE.md** - This is your master reference
2. **Follow existing patterns** - Don't invent new structures
3. **Use standards.md** - Quality is non-negotiable
4. **Check PHASE-2-COMPLETION.md** - See complete working examples
5. **Maintain terminology** - Use terminology-alignment-claude-code.md

### Common Pitfalls to Avoid
1. ❌ Don't skip YAML frontmatter in skills
2. ❌ Don't deviate from 7-step workflow in subagents
3. ❌ Don't create primitives without JSON I/O
4. ❌ Don't forget telemetry emission
5. ❌ Don't skip acceptance criteria
6. ❌ Don't use inconsistent terminology

### Quality Checklist
Before completing any development task, verify:
- [ ] Follows V2 architecture patterns
- [ ] Complies with standards.md requirements
- [ ] Uses correct terminology
- [ ] Includes complete documentation
- [ ] Has telemetry emission
- [ ] Includes acceptance criteria
- [ ] Tested and validated
- [ ] Updated relevant index/roadmap documents

---

**Essential Development Documentation**
**Version:** 2.0 (Post-Cleanup)
**Status:** Current and Complete
**Last Updated:** 2025-11-04

*Use this list as your primary reference when developing new components*
*All files are current, relevant, and maintained*
