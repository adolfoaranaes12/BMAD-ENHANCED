# Command Mismatch Analysis

**Date:** 2025-11-05
**Status:** In Development

## Summary

Analysis of mismatches between documented commands in `COMMAND-REFERENCE-SUMMARY.md` and actual implementation in `.claude/commands/` and agent routing.

---

## Actual Slash Commands (18 total)

From `.claude/commands/` directory:

1. ✅ `/alex` - Routes to alex-planner-v2
2. ✅ `/analyze-architecture` - Standalone command
3. ❓ `/BMad` - Unknown purpose
4. ❓ `/bmad-cw` - Unknown purpose
5. ❓ `/bmadInfraDevOps` - Unknown purpose
6. ✅ `/bob` - Routes to bob-sm
7. ✅ `/design-architecture` - Standalone command
8. ✅ `/james` - Routes to james-developer-v2
9. ✅ `/john` - Routes to john-pm
10. ✅ `/mary` - Routes to mary-analyst
11. ✅ `/orchestrator` - Routes to orchestrator-v2
12. ✅ `/quinn` - Routes to quinn-quality-v2
13. ✅ `/review-architecture` - Standalone command
14. ✅ `/sally` - Routes to sally-ux-expert
15. ✅ `/sarah` - Routes to sarah-po
16. ✅ `/validate-story` - Standalone command
17. ✅ `/winston-consult` - Special conversational command
18. ✅ `/winston` - Routes to winston-architect

---

## Documented Winston Commands vs Reality

### Documented in COMMAND-REFERENCE-SUMMARY.md (Lines 72-78)

```bash
/winston *create-architecture <requirements-file> [--type <type>] [--depth <mode>]
/winston *review-architecture <architecture-file> [--focus <area>]
/winston *analyze-architecture [codebase-path] [--depth <mode>]
/winston *create-adr "<decision-description>"          # ⚠️ ISSUE
/winston *validate-patterns <codebase-path>            # ⚠️ UNKNOWN
```

### Actual Status

| Command | Slash Command | Skill Exists | Agent Routing | Status |
|---------|--------------|--------------|---------------|--------|
| `*create-architecture` | ✅ `/design-architecture` | ✅ Yes | ✅ Documented | ✅ Works (standalone) |
| `*review-architecture` | ✅ `/review-architecture` | ✅ Yes | ✅ Documented | ✅ Works (standalone) |
| `*analyze-architecture` | ✅ `/analyze-architecture` | ✅ Yes | ✅ Documented | ✅ Works (standalone) |
| `*create-adr` | ❌ No standalone | ✅ `.claude/skills/planning/create-adr/SKILL.md` | ⚠️ Documented but NO routing | ⛔ **BROKEN** |
| `*validate-patterns` | ❌ No standalone | ❓ Unknown | ⚠️ Documented but NO routing | ⛔ **BROKEN** |

---

## Issue #1: `/winston *create-adr` - Documented But Not Wired

### What's Missing

1. **Agent Routing:** `winston-architect.md` documents the command (line 380-479) but has NO routing logic
2. **Skill Exists:** `.claude/skills/planning/create-adr/SKILL.md` exists (11,465 bytes)
3. **Git Status:** Shows as untracked (`?? .claude/skills/planning/create-adr/`)

### What Needs to Happen

**Option A: Create standalone slash command**
```bash
# Create .claude/commands/create-adr.md
# Route directly to .claude/skills/planning/create-adr/SKILL.md
```

**Option B: Wire into winston agent routing**
```markdown
# In winston-architect.md, add routing logic that:
# - Detects `*create-adr` in ARGUMENTS
# - Loads .claude/skills/planning/create-adr/SKILL.md
# - Executes the skill workflow
```

**Option C: Use `/design-architecture` instead**
- Already creates ADRs as part of architecture creation
- Remove `*create-adr` from documentation

### Recommendation

**Choose Option A** (standalone command) because:
- Consistent with existing architecture commands pattern
- Users might want ADRs without full architecture
- Simpler maintenance

---

## Issue #2: `/winston *validate-patterns` - Unknown Status

### Investigation Needed

1. Does `.claude/skills/planning/validate-patterns/SKILL.md` exist?
2. Is this implemented in `bmad-commands` scripts?
3. Should this command exist or be removed from docs?

### Quick Check

```bash
find .claude/skills -name "*validate-patterns*" -o -name "*pattern*"
```

---

## Issue #3: Undocumented Slash Commands

These commands exist in `.claude/commands/` but are NOT in `COMMAND-REFERENCE-SUMMARY.md`:

1. `/BMad` - Purpose unknown
2. `/bmad-cw` - Purpose unknown
3. `/bmadInfraDevOps` - Purpose unknown

### Investigation Needed

1. Read these files to understand their purpose
2. Decide if they should be:
   - Documented in COMMAND-REFERENCE-SUMMARY.md
   - Removed if obsolete
   - Moved to a "utility commands" section

---

## Architecture Command Pattern

Winston's architecture commands have evolved to use **standalone slash commands** rather than subcommands:

### Current Pattern (Standalone)
```bash
/design-architecture docs/prd.md --type fullstack
/review-architecture docs/architecture.md --focus security
/analyze-architecture . --depth comprehensive
```

### Old Pattern (Subcommands) - NOT USED
```bash
/winston *create-architecture docs/prd.md
/winston *review-architecture docs/architecture.md
/winston *analyze-architecture .
```

### Why This Matters

The documentation still references the old subcommand pattern (`/winston *create-architecture`), but users should use:

- ✅ `/design-architecture` instead of `/winston *create-architecture`
- ✅ `/review-architecture` instead of `/winston *review-architecture`
- ✅ `/analyze-architecture` instead of `/winston *analyze-architecture`

---

## Recommended Actions

### High Priority (Blocking Users)

1. **Fix `/winston *create-adr`**
   - [ ] Create `.claude/commands/create-adr.md`
   - [ ] Route to `.claude/skills/planning/create-adr/SKILL.md`
   - [ ] Test the command
   - [ ] Update documentation

2. **Update COMMAND-REFERENCE-SUMMARY.md**
   - [ ] Replace `/winston *create-architecture` → `/design-architecture`
   - [ ] Replace `/winston *review-architecture` → `/review-architecture`
   - [ ] Replace `/winston *analyze-architecture` → `/analyze-architecture`
   - [ ] Fix or remove `/winston *validate-patterns`

### Medium Priority (Documentation Cleanup)

3. **Document missing commands**
   - [ ] Investigate `/BMad`, `/bmad-cw`, `/bmadInfraDevOps`
   - [ ] Add to docs or remove if obsolete

4. **Verify all agent subcommands**
   - [ ] Check all `/alex *` commands work
   - [ ] Check all `/james *` commands work
   - [ ] Check all `/quinn *` commands work
   - [ ] Check all `/orchestrator *` commands work

---

## Testing Checklist

After fixes, test these commands:

```bash
# Winston Commands
/design-architecture docs/prd.md --depth quick
/review-architecture docs/architecture.md
/analyze-architecture . --depth quick
/create-adr "Use PostgreSQL for relational data"  # NEW
/winston-consult "Help me choose a database"

# Verify broken commands give helpful errors
/winston *create-architecture  # Should suggest /design-architecture
/winston *validate-patterns    # Should give clear error or work
```

---

## Notes

- Winston's commands shifted from subcommands to standalone slash commands
- This improved UX but created documentation lag
- `create-adr` skill exists but was never wired up
- Git shows `create-adr/` as untracked, suggesting it's in development

