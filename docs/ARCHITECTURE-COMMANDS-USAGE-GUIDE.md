# Architecture Commands Usage Guide
## Comprehensive Guide to BMAD Enhanced Architecture Commands

**Version**: 2.0 (With Depth Modes)
**Date**: 2025-11-05
**Status**: Production Ready

---

## Executive Summary

All BMAD Enhanced architecture commands now support **three depth modes** with **comprehensive as the default** for intelligent, detailed, and thorough architecture work.

### Key Changes

| Aspect | Before | After (V2) |
|--------|--------|------------|
| **Default Mode** | Standard (10-12 min) | **Comprehensive** (15-20 min) |
| **Token Budget** | 100K | **120K** (comprehensive) |
| **Depth Options** | Single mode | **3 modes** (quick/standard/comprehensive) |
| **Intelligence Level** | Good | **Maximum** (comprehensive by default) |

---

## Part 1: The Three Depth Modes

### Quick Mode (`--depth quick`)

**Purpose**: Rapid assessments when time is critical

**Characteristics**:
- ⏱️ Duration: 5-7 minutes
- 🔢 Token Usage: ~50,000 tokens
- 📊 Analysis Depth: High-level overview
- 📝 Output: Essential findings only

**Best For**:
- Initial explorations
- Gate checks
- Fast feedback loops
- Proof of concepts
- Time-sensitive decisions

**Trade-offs**:
- ✅ Fast and efficient
- ✅ Low token cost
- ⚠️ Less detailed
- ⚠️ May miss edge cases

---

### Standard Mode (`--depth standard`)

**Purpose**: Balanced analysis for regular development

**Characteristics**:
- ⏱️ Duration: 10-12 minutes
- 🔢 Token Usage: ~80,000 tokens
- 📊 Analysis Depth: Practical, actionable
- 📝 Output: Comprehensive without deep-dives

**Best For**:
- Regular assessments
- Iterative development
- Pre-production reviews
- Architecture validation
- MVP development

**Trade-offs**:
- ✅ Balanced time/quality
- ✅ Moderate token cost
- ✅ Covers most scenarios
- ⚠️ Less rigorous than comprehensive

---

### Comprehensive Mode (`--depth comprehensive`) [DEFAULT]

**Purpose**: Maximum intelligence and detail for production systems

**Characteristics**:
- ⏱️ Duration: 15-20 minutes
- 🔢 Token Usage: ~120,000 tokens
- 📊 Analysis Depth: Rigorous, thorough, complete
- 📝 Output: Production-ready documentation

**Best For**:
- **Production systems** (recommended)
- Architecture audits
- Enterprise applications
- Compliance reviews
- Critical systems
- **Default for all architecture work** ✨

**Trade-offs**:
- ✅ Maximum intelligence
- ✅ Most thorough analysis
- ✅ Production-ready output
- ⚠️ Higher token cost
- ⚠️ Takes more time

---

## Part 2: Command Reference

### /analyze-architecture

Analyze existing (brownfield) codebase architecture.

#### Syntax

```bash
/analyze-architecture [codebase-path] [--depth <mode>] [--output <format>] [--focus <area>] [--budget <tokens>]
```

#### Parameters

| Parameter | Options | Default | Description |
|-----------|---------|---------|-------------|
| `codebase-path` | Any path | `.` (current) | Path to codebase root |
| `--depth` | `quick`, `standard`, `comprehensive` | **`comprehensive`** | Analysis depth mode |
| `--output` | `markdown`, `json`, `both` | `markdown` | Output format |
| `--focus` | `all`, `architecture`, `security`, `performance`, `scalability`, `tech-debt` | `all` | Focus area |
| `--budget` | Number | `120000` | Token budget |

#### Examples

```bash
# Comprehensive analysis (default - recommended for all architecture work)
/analyze-architecture

# Quick assessment (when time is critical)
/analyze-architecture --depth quick

# Standard analysis (for iterative development)
/analyze-architecture --depth standard

# Comprehensive security focus
/analyze-architecture --focus security

# Analyze specific package with comprehensive depth
/analyze-architecture packages/backend

# Quick analysis with JSON output
/analyze-architecture --depth quick --output json

# Standard analysis with lower token budget
/analyze-architecture --depth standard --budget 60000
```

#### Depth Mode Behavior

| Mode | Steps | Diagrams | Integration Analysis | Cost Analysis |
|------|-------|----------|---------------------|---------------|
| **Quick** | 1-8 | Basic | ❌ No | ❌ No |
| **Standard** | 1-12 | Extended | ⚠️ Partial | ✅ Yes |
| **Comprehensive** | All 15 | Complete | ✅ Full | ✅ Full |

---

### /design-architecture

Design system architecture from requirements (PRD/epic).

#### Syntax

```bash
/design-architecture <requirements-file> [--type <type>] [--depth <mode>] [--complexity <complexity>]
```

#### Parameters

| Parameter | Options | Default | Description |
|-----------|---------|---------|-------------|
| `requirements-file` | File path | **(required)** | Path to requirements/PRD |
| `--type` | `auto`, `frontend`, `backend`, `fullstack` | `auto` | System type |
| `--depth` | `quick`, `standard`, `comprehensive` | **`comprehensive`** | Design depth mode |
| `--complexity` | `auto`, `low`, `medium`, `high` | `auto` | Complexity override |

#### Examples

```bash
# Comprehensive architecture design (default - most detailed)
/design-architecture docs/prd.md

# Quick architecture (minimal ADRs, fast turnaround)
/design-architecture docs/prd.md --depth quick

# Standard architecture (balanced)
/design-architecture docs/prd.md --depth standard

# Fullstack with comprehensive depth (explicit)
/design-architecture docs/epic.md --type fullstack

# Backend with quick mode
/design-architecture docs/requirements.md --type backend --depth quick

# Comprehensive frontend with high complexity
/design-architecture docs/spa-requirements.md --type frontend --complexity high
```

#### Depth Mode Behavior

| Mode | ADRs | Diagrams | Details | Duration |
|------|------|----------|---------|----------|
| **Quick** | 3 minimum | Context only | Essential | 5-7 min |
| **Standard** | 5-7 | Context + Container | Balanced | 10-12 min |
| **Comprehensive** | 8-15 | Full C4 model | Complete | 15-20 min |

---

### /review-architecture

Peer review system architecture for quality and risks.

#### Syntax

```bash
/review-architecture <architecture-file> [--focus <area>] [--depth <mode>]
```

#### Parameters

| Parameter | Options | Default | Description |
|-----------|---------|---------|-------------|
| `architecture-file` | File path | **(required)** | Path to architecture doc |
| `--focus` | `all`, `completeness`, `quality`, `security`, `scalability`, `performance`, `cost` | `all` | Focus area |
| `--depth` | `quick`, `standard`, `comprehensive` | **`comprehensive`** | Review depth mode |

#### Examples

```bash
# Comprehensive review (default - most rigorous)
/review-architecture docs/architecture.md

# Quick review (pass/fail with top issues)
/review-architecture docs/architecture.md --depth quick

# Standard review (balanced depth)
/review-architecture docs/architecture.md --depth standard

# Comprehensive security review
/review-architecture docs/architecture.md --focus security

# Quick scalability check
/review-architecture docs/architecture.md --focus scalability --depth quick

# Comprehensive cost analysis
/review-architecture docs/architecture.md --focus cost
```

#### Depth Mode Behavior

| Mode | Analysis | Report | Risk Modeling | Cost Analysis |
|------|----------|--------|---------------|---------------|
| **Quick** | Critical only | Pass/fail + top 3 | ❌ No | ❌ No |
| **Standard** | All dimensions | Full scoring | ⚠️ Basic | ✅ Yes |
| **Comprehensive** | Deep analysis | Complete | ✅ Full | ✅ Full |

---

## Part 3: When to Use Each Mode

### Use Quick Mode When:

- ✅ Time is critical (need results in <10 minutes)
- ✅ Doing initial exploration or proof of concept
- ✅ Running frequent iterations with fast feedback
- ✅ Performing gate checks or preliminary assessments
- ✅ Token budget is constrained (<60K tokens)
- ✅ Need high-level overview only

**Examples**:
```bash
# Quick health check before sprint planning
/analyze-architecture --depth quick

# Rapid architecture sketch for POC
/design-architecture docs/poc-requirements.md --depth quick

# Fast gate check before proceeding
/review-architecture docs/design.md --depth quick
```

---

### Use Standard Mode When:

- ✅ Working on regular projects (not critical systems)
- ✅ Iterative development with regular validation
- ✅ MVP or prototype development
- ✅ Need balanced time/quality trade-off
- ✅ Token budget is moderate (60-90K tokens)
- ✅ Comprehensive analysis not required

**Examples**:
```bash
# Regular iteration assessment
/analyze-architecture --depth standard

# Balanced architecture for MVP
/design-architecture docs/mvp-requirements.md --depth standard

# Regular pre-production review
/review-architecture docs/architecture.md --depth standard
```

---

### Use Comprehensive Mode When:

- ✅ **Working on production systems** (always recommended)
- ✅ **Enterprise or critical applications**
- ✅ Architecture audits or compliance reviews
- ✅ **Need maximum intelligence and thoroughness**
- ✅ Token budget allows (100-150K tokens)
- ✅ **Default for all serious architecture work** ✨

**This is the DEFAULT mode - use it unless you have a specific reason not to!**

**Examples**:
```bash
# Production system analysis (default)
/analyze-architecture

# Production architecture design (default)
/design-architecture docs/production-requirements.md

# Production readiness review (default)
/review-architecture docs/architecture.md

# Enterprise system with comprehensive depth (explicit)
/analyze-architecture --depth comprehensive

# Critical system with full rigor
/design-architecture docs/banking-system.md --depth comprehensive
```

---

## Part 4: Practical Workflows

### Workflow 1: New Feature Development

**Scenario**: Building a new authentication system

```bash
# Step 1: Quick analysis of existing auth (5-7 min)
/analyze-architecture packages/auth --depth quick --focus security

# Step 2: Comprehensive architecture design (15-20 min)
/design-architecture docs/auth-v2-requirements.md

# Step 3: Comprehensive review before implementation (15-20 min)
/review-architecture docs/auth-v2-architecture.md

# Step 4: Standard analysis after implementation (10-12 min)
/analyze-architecture packages/auth --depth standard --focus security
```

**Total Time**: ~50-60 minutes
**Token Usage**: ~220K tokens
**Quality**: Production-ready

---

### Workflow 2: Emergency Bug Fix

**Scenario**: Critical security issue needs immediate attention

```bash
# Step 1: Quick analysis to identify scope (5-7 min)
/analyze-architecture --depth quick --focus security

# Step 2: Quick review of proposed fix (5-7 min)
/review-architecture docs/security-fix-design.md --depth quick

# Step 3: Standard analysis after fix (10-12 min)
/analyze-architecture --depth standard --focus security
```

**Total Time**: ~25 minutes
**Token Usage**: ~130K tokens
**Quality**: Fast + sufficient for emergency

---

### Workflow 3: Production Readiness Assessment

**Scenario**: Final validation before go-live

```bash
# Step 1: Comprehensive full analysis (15-20 min)
/analyze-architecture

# Step 2: Comprehensive architecture review (15-20 min)
/review-architecture docs/architecture.md

# Step 3: Comprehensive security deep-dive (15-20 min)
/review-architecture docs/architecture.md --focus security

# Step 4: Comprehensive scalability assessment (15-20 min)
/review-architecture docs/architecture.md --focus scalability
```

**Total Time**: ~70-80 minutes
**Token Usage**: ~480K tokens
**Quality**: Maximum rigor for production

---

### Workflow 4: Iterative Development

**Scenario**: Sprint-based feature development

```bash
# Sprint Start: Comprehensive planning (15-20 min)
/design-architecture docs/sprint-N-requirements.md

# Mid-Sprint: Standard check-in (10-12 min)
/analyze-architecture --depth standard

# Sprint End: Comprehensive validation (15-20 min)
/review-architecture docs/architecture.md
```

**Total Time per Sprint**: ~45 minutes
**Token Usage per Sprint**: ~320K tokens
**Quality**: Balanced for agile development

---

## Part 5: Token Budget Management

### Token Budget by Mode

| Mode | Base Tokens | With Focus | Full Analysis |
|------|-------------|------------|---------------|
| **Quick** | ~50K | ~40K | ~50K |
| **Standard** | ~80K | ~70K | ~80K |
| **Comprehensive** | ~120K | ~100K | ~120K |

### Cost Optimization Strategies

#### Strategy 1: Mode Selection

```bash
# Instead of always using comprehensive (120K tokens):
/analyze-architecture

# Use quick mode for non-critical work (50K tokens, 58% savings):
/analyze-architecture --depth quick
```

**Savings**: 70K tokens per analysis

---

#### Strategy 2: Focus Areas

```bash
# Instead of comprehensive full analysis (120K tokens):
/analyze-architecture

# Use focused comprehensive analysis (100K tokens, 17% savings):
/analyze-architecture --focus security
```

**Savings**: 20K tokens per analysis

---

#### Strategy 3: Explicit Token Budgets

```bash
# Set explicit lower budget to force optimization:
/analyze-architecture --budget 80000

# System adapts analysis to fit budget
```

---

## Part 6: Best Practices

### DO ✅

1. **Use comprehensive by default** for all production work
   ```bash
   /analyze-architecture  # Comprehensive is default
   ```

2. **Use quick mode** for rapid iterations
   ```bash
   /analyze-architecture --depth quick
   ```

3. **Use focus areas** when you know what you need
   ```bash
   /analyze-architecture --focus security
   ```

4. **Test commands** with quick mode first
   ```bash
   /review-architecture docs/draft.md --depth quick
   ```

5. **Use standard mode** for regular development
   ```bash
   /analyze-architecture --depth standard
   ```

### DON'T ❌

1. **Don't use quick mode** for production systems
   ```bash
   # ❌ BAD: Quick mode for production
   /analyze-architecture --depth quick  # Production system

   # ✅ GOOD: Comprehensive for production
   /analyze-architecture  # Uses comprehensive by default
   ```

2. **Don't skip architecture validation**
   ```bash
   # ❌ BAD: No review before implementation
   # ✅ GOOD: Always review
   /review-architecture docs/architecture.md
   ```

3. **Don't ignore depth modes**
   ```bash
   # ❌ BAD: Always using quick to save tokens
   # ✅ GOOD: Use appropriate mode for context
   ```

---

## Part 7: Troubleshooting

### Issue 1: "Analysis taking too long"

**Problem**: Comprehensive mode takes 15-20 minutes

**Solutions**:
```bash
# Option 1: Use quick mode (5-7 min)
/analyze-architecture --depth quick

# Option 2: Use standard mode (10-12 min)
/analyze-architecture --depth standard

# Option 3: Use focus area to narrow scope
/analyze-architecture --focus security
```

---

### Issue 2: "Token budget exceeded"

**Problem**: Hitting token limits

**Solutions**:
```bash
# Option 1: Use quick mode (50K tokens)
/analyze-architecture --depth quick

# Option 2: Set explicit lower budget
/analyze-architecture --budget 60000

# Option 3: Use focus area
/analyze-architecture --focus architecture
```

---

### Issue 3: "Not enough detail in output"

**Problem**: Quick or standard mode insufficient

**Solution**:
```bash
# Always use comprehensive for production work
/analyze-architecture  # Defaults to comprehensive
```

---

### Issue 4: "Which mode should I use?"

**Decision Tree**:

```
Is this for production?
├─ YES → Use comprehensive (default)
└─ NO → Is time critical?
    ├─ YES → Use quick
    └─ NO → Use standard
```

**Quick Reference**:
- **Production systems**: Comprehensive (default) ✅
- **Quick checks**: Quick mode
- **Regular development**: Standard mode

---

## Part 8: Summary

### Key Takeaways

1. **Comprehensive is the default** for all architecture commands
2. **Use comprehensive** for production systems (recommended)
3. **Use quick** only when time is critical
4. **Use standard** for regular development
5. **All commands support** the same depth modes

### Command Quick Reference

```bash
# All three commands use comprehensive by default:

/analyze-architecture                    # Comprehensive (15-20 min, 120K tokens)
/design-architecture docs/prd.md         # Comprehensive (15-20 min, 120K tokens)
/review-architecture docs/arch.md        # Comprehensive (15-20 min, 120K tokens)

# Quick mode (5-7 min, 50K tokens):
/analyze-architecture --depth quick
/design-architecture docs/prd.md --depth quick
/review-architecture docs/arch.md --depth quick

# Standard mode (10-12 min, 80K tokens):
/analyze-architecture --depth standard
/design-architecture docs/prd.md --depth standard
/review-architecture docs/arch.md --depth standard
```

### Token Budget Guide

| Work Type | Recommended Mode | Token Budget | Duration |
|-----------|-----------------|--------------|----------|
| **Production Systems** | Comprehensive | 120K | 15-20 min |
| **Enterprise Apps** | Comprehensive | 120K | 15-20 min |
| **Regular Development** | Standard | 80K | 10-12 min |
| **MVP/Prototypes** | Standard | 80K | 10-12 min |
| **Quick Checks** | Quick | 50K | 5-7 min |
| **POCs** | Quick | 50K | 5-7 min |

---

## Conclusion

With **comprehensive as the default**, BMAD Enhanced architecture commands now provide **maximum intelligence and thoroughness** by default, while still offering **flexibility** for time-sensitive or iterative work through quick and standard modes.

**Use comprehensive (the default) for all serious architecture work.** ✨

---

**Guide Version**: 2.0
**Last Updated**: 2025-11-05
**Status**: Production Ready

**END OF USAGE GUIDE**
