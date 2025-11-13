---
description: Validate tests reflect production reality beyond specification compliance - generates edge cases and identifies reality gaps
argument-hint: <story-id> [--production-traffic <file>] [--no-vibe-check]
allowed-tools: Skill
---

Invoke the validate-test-reality skill to bridge the specification-reality gap:

Use Skill tool: `Skill tool with skill="validate-test-reality"`

This will execute the reality validation workflow:
1. Load story/task specification and test design
2. Generate 50+ edge cases beyond specification (Unicode, concurrency, failures, security)
3. Analyze test coverage against production reality scenarios
4. Identify specification-reality gaps
5. Generate test deficiency report with recommendations
6. Determine QA readiness (READY/NOT READY/NEEDS IMPROVEMENT)

The skill will parse $ARGUMENTS for:
- `story-id` - Story/task identifier (e.g., 'task-007' or 'story-1.2') (required)
- `--story-file` - Path to story/task specification file (auto-detected if not provided)
- `--test-design-file` - Path to test design file (auto-detected if not provided)
- `--production-traffic` - Path to production traffic patterns file (optional)
- `--no-vibe-check` - Disable vibe-check MCP validation (default: enabled)

Edge Case Categories Generated:
1. **Data Reality:** Unicode/emoji, email edge cases, null/undefined, injection characters, timezones
2. **Concurrency Reality:** Race conditions, simultaneous operations, connection pool exhaustion
3. **System Reality:** Database failures, API timeouts, disk space, network partitions
4. **Performance Reality:** 10x load, millions of records, cache cold starts
5. **Security Reality:** SQL injection variants, XSS payloads, auth bypass attempts
6. **Integration Reality:** API version changes, schema evolution, certificate expiration

Output:
- Test deficiency report: `.claude/quality/assessments/{story-id}-test-reality-{date}.md`
- Reality coverage percentage (target: >80%)
- Critical/high/medium gaps with specific test recommendations
- QA readiness decision

**CRITICAL:** Run this BEFORE /quinn *validate-quality-gate to ensure tests cover production reality, not just specification compliance.

**Integration with Quality Gate:**
Quinn automatically requires reality validation. If missing:
- Warning issued
- validate-test-reality runs automatically
- Critical gaps > 0: Auto-FAIL gate (production blockers)
- High gaps > 10: Set to CONCERNS

**Example Usage:**
```bash
# Basic usage
/validate-test-reality task-007

# With production traffic patterns
/validate-test-reality task-007 --production-traffic .claude/production/traffic.json

# Skip vibe-check validation
/validate-test-reality task-007 --no-vibe-check
```

**Expected Output:**
```
Test Reality Validation Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Story: task-007 - User Registration

Edge Cases Generated: 54
Reality Coverage: 62% (Target: 80%)

Specification-Reality Gaps:
❌ Critical (5):
  - Email with "+" not tested (Gmail aliasing)
  - Concurrent registration race condition not tested
  - Database connection failure mid-transaction not tested
  - SQL injection variants not tested
  - Password with null bytes not tested

⚠️ High (8):
  - Unicode in email addresses not tested
  - Email service timeout handling not tested
  - Extremely long password (1000 chars) not tested
  ...

ℹ️ Medium (12):
  - Rare email formats (subdomain dots) not tested
  ...

Recommended Tests: 13 minimum (5 critical + 8 high)
QA Readiness: NOT READY (5 critical gaps)

Next Steps:
1. Add recommended tests for critical gaps
2. Re-run /validate-test-reality to verify gaps closed
3. Proceed to /quinn *validate-quality-gate

Report: .claude/quality/assessments/task-007-test-reality-20251111.md
```
