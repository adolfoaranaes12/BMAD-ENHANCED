# Interactive Elements

## Overview

Enhance checklists with interactive features that improve usability, engagement, and tracking. This guide covers markdown-based interactive elements.

---

## Element 1: Checkboxes

### Basic Checkbox

```markdown
- [ ] Task not started
- [x] Task complete
```

**Renders as:**
- [ ] Task not started
- [x] Task complete

### Nested Checklists

```markdown
- [x] Phase 1: Planning
  - [x] Define requirements
  - [x] Create mockups
  - [x] Get approval
- [ ] Phase 2: Development
  - [x] Setup environment
  - [ ] Implement features
  - [ ] Write tests
```

**Use for:** Multi-level workflows, sub-tasks

---

## Element 2: Collapsible Sections

### Basic Collapsible

```markdown
<details>
<summary>Click to expand details</summary>

Hidden content goes here.
Can include:
- Lists
- Code blocks
- Images

</details>
```

**Renders as:** Expandable/collapsible section

### Collapsible Step Details

```markdown
## Step 3: Database Migration

**Status:** ⬜ Not Started

<details>
<summary>📖 View detailed instructions</summary>

### Prerequisites
- Database backup complete
- Migration scripts tested

### Commands
```bash
npm run migrate
npm run seed
```

### Validation
- [ ] Migration completed without errors
- [ ] All tables created
- [ ] Sample data loaded

### Troubleshooting
**Issue:** Migration fails with timeout
**Solution:** Increase connection timeout in config

</details>
```

**Use for:** Detailed instructions, reducing visual clutter

---

## Element 3: Progress Indicators

### ASCII Progress Bar

```markdown
**Progress:** [█████░░░░░] 50% (5/10 steps complete)
```

**Use for:** Visual progress tracking

### Percentage-Based

```markdown
**Completion:** 7/10 tasks (70%)

**Breakdown:**
- Critical: 3/3 (100%) ✅
- High: 2/4 (50%) 🔄
- Medium: 2/3 (67%) 🔄
```

### Status Icons

```markdown
⬜ Not Started
🔄 In Progress
✅ Complete
❌ Failed
⚠️ Blocked
🔁 Retry Needed
```

---

## Element 4: Tables

### Status Tracking Table

```markdown
| Step | Status | Owner | Due Date | Notes |
|------|--------|-------|----------|-------|
| 1 | ✅ | Alice | 2025-01-01 | Done |
| 2 | 🔄 | Bob | 2025-01-05 | In progress |
| 3 | ⬜ | Carol | 2025-01-10 | Waiting |
```

### Time Tracking Table

```markdown
| Task | Estimated | Actual | Variance |
|------|-----------|--------|----------|
| Setup | 1h | 1.5h | +30m |
| Dev | 4h | 3h | -1h |
| Test | 2h | ___ | ___ |
```

---

## Element 5: Status Badges

### Using Emojis

```markdown
🔴 Critical Priority
🟡 High Priority
🟢 Medium Priority
⚪ Low Priority

✅ Approved
⏳ Pending Review
❌ Rejected

🚀 Production
🧪 Staging
🛠️ Development
```

### Using Text Badges

```markdown
`STATUS: IN PROGRESS`
`PRIORITY: HIGH`
`ENVIRONMENT: PROD`
```

---

## Element 6: Links and References

### Internal Links (Within Checklist)

```markdown
See [Step 5](#step-5-verification) for validation details.

Jump to [Rollback Plan](#rollback-plan) if issues arise.
```

### External Links

```markdown
**Resources:**
- [Deployment Guide](https://docs.example.com/deploy)
- [Troubleshooting](https://wiki.example.com/troubleshoot)
- [Support Channel](slack://channel?id=C123456)
```

### Embedded Tools

```markdown
**Quick Access:**
- [Dashboard](https://app.example.com/dashboard) 🔗
- [Logs](https://logs.example.com) 🔗
- [Monitoring](https://monitor.example.com) 🔗
```

---

## Element 7: Code Blocks with Syntax Highlighting

### Executable Commands

```markdown
### Deploy Application

```bash
# Build production bundle
npm run build

# Deploy to server
rsync -avz dist/ user@server:/var/www/

# Restart service
ssh user@server 'systemctl restart app'
```

**Copy and paste commands above** ⬆️
```

### Configuration Examples

```markdown
### Example Configuration

```json
{
  "environment": "production",
  "database": {
    "host": "db.example.com",
    "port": 5432
  }
}
```
```

---

## Element 8: Alerts and Callouts

### Using Blockquotes

```markdown
> ⚠️ **Warning:** This action cannot be undone.
> Ensure backups are complete before proceeding.

> 💡 **Tip:** You can skip this step if using Docker.

> ❌ **Error:** If you see "Connection refused", check VPN connection.

> ✅ **Success Criteria:** All health checks return 200 OK.
```

### Using Emoji Sections

```markdown
🚨 **CRITICAL STEP**
This step is destructive. Double-check before running.

📝 **NOTE**
This process may take 10-15 minutes.

🎯 **GOAL**
At the end of this step, application should be running.
```

---

## Element 9: Time and Date Tracking

### Timestamp Template

```markdown
**Started:** [Date] at [Time]
**Estimated Completion:** [Date] at [Time]
**Actual Completion:** ____________

**Time Spent:** ___ hours ___ minutes
**Blocked Time:** ___ hours ___ minutes
```

### Timeline View

```markdown
## Timeline

```
2025-01-04 09:00 - Started deployment
2025-01-04 09:15 - Code pushed to server
2025-01-04 09:30 - Database migrated
2025-01-04 09:45 - Verification complete ✅
2025-01-04 10:00 - Deployment complete ✅
```
```

---

## Element 10: Decision Trees (ASCII Art)

### Simple Tree

```markdown
```
Decision: Tests Passing?
  ├─ YES → Deploy to production → Complete
  └─ NO → Debug issues → Re-run tests
```
```

### Complex Tree

```markdown
```
START
  │
  ├─ Step 1: Build
  │
  ├─ VALIDATION: Build successful?
  │    ├─ YES → Step 2: Test
  │    └─ NO → Fix build errors → Return to Step 1
  │
  ├─ VALIDATION: Tests passing?
  │    ├─ YES → Step 3: Deploy
  │    └─ NO → Fix failing tests → Return to Step 2
  │
  ├─ DECISION: Deploy to staging or prod?
  │    ├─ STAGING → Deploy staging → Verify → END
  │    └─ PROD → Deploy prod → Verify → Monitor → END
```
```

---

## Element 11: Forms and Input Fields

### Fillable Template

```markdown
**Deployment Information:**

- **Version:** __v1.2.3__
- **Deployed By:** __John Smith__
- **Date:** __2025-01-04__
- **Time:** __14:30 UTC__
- **Environment:** [✅] Production [ ] Staging [ ] Dev

**Checklist Verification:**
- [ ] All prerequisites met
- [ ] Backup created
- [ ] Rollback plan ready

**Sign-Off:**

Name: ____________________
Date: ____________________
Signature: ____________________
```

---

## Element 12: Visual Separators

### Section Dividers

```markdown
---

***

---

═══════════════════════════════════════════

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
```

### Styled Headers

```markdown
## 🚀 Deployment Phase

## ✅ Validation Phase

## 📊 Monitoring Phase

## ⚙️ Configuration
```

---

## Element 13: Embedded Metrics

### Live Status Display

```markdown
## System Status

```
Last Update: 2025-01-04 14:30 UTC

┌─────────────────┬──────────┬────────────┐
│ Service         │ Status   │ Response   │
├─────────────────┼──────────┼────────────┤
│ Web Application │ ✅ UP    │ 120ms      │
│ API Server      │ ✅ UP    │ 45ms       │
│ Database        │ ✅ UP    │ 12ms       │
│ Cache           │ ✅ UP    │ 2ms        │
└─────────────────┴──────────┴────────────┘
```
```

### Key Metrics

```markdown
**Performance Metrics:**

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Response Time | <200ms | 150ms | ✅ |
| Error Rate | <1% | 0.3% | ✅ |
| CPU Usage | <70% | 45% | ✅ |
| Memory | <80% | 92% | ⚠️ |
```

---

## Element 14: Conditional Instructions

### If-Then Blocks

```markdown
**IF** you are deploying to production:
  ➜ Follow the production deployment checklist
  ➜ Require two-person approval
  ➜ Schedule maintenance window

**IF** you are deploying to staging:
  ➜ Follow the staging checklist
  ➜ Single-person approval sufficient
  ➜ No maintenance window needed
```

### Environment-Specific

```markdown
### Configuration

<details>
<summary>Production Settings</summary>

```env
NODE_ENV=production
DATABASE_URL=prod-db.example.com
CACHE_ENABLED=true
DEBUG=false
```

</details>

<details>
<summary>Development Settings</summary>

```env
NODE_ENV=development
DATABASE_URL=localhost
CACHE_ENABLED=false
DEBUG=true
```

</details>
```

---

## Best Practices

1. **Progressive Disclosure** - Use collapsible sections for details
2. **Visual Hierarchy** - Use headers, separators, indentation
3. **Clear Status** - Use consistent icons/colors
4. **Actionable** - Make next steps obvious
5. **Scannable** - Use tables, lists, short paragraphs
6. **Linked Resources** - Provide one-click access to tools
7. **Copy-Paste Friendly** - Format commands for easy execution
8. **Mobile Friendly** - Works on small screens
9. **Print Friendly** - Can be printed if needed
10. **Accessible** - Clear language, good contrast

---

## Interactive Checklist Example

```markdown
# Deployment Checklist: MyApp v1.2.3

<details>
<summary>📋 Quick Info</summary>

**Environment:** Production
**Version:** v1.2.3
**Deployed By:** Alice
**Date:** 2025-01-04

</details>

---

## Progress

[█████████░] 90% Complete

- [x] Pre-deployment checks
- [x] Backup created
- [x] Code deployed
- [x] Database migrated
- [x] Verification passed
- [ ] Post-deployment monitoring (in progress)

---

## Step 1: Pre-Deployment Checks

**Status:** ✅ Complete

<details>
<summary>View checklist</summary>

- [x] All tests passing
- [x] Code reviewed
- [x] Version tagged
- [x] Stakeholders notified

**Completed:** 2025-01-04 13:00

</details>

---

## Step 2: Create Backup

**Status:** ✅ Complete

<details>
<summary>View commands</summary>

```bash
pg_dump myapp_prod > backup-2025-01-04.sql
aws s3 cp backup-2025-01-04.sql s3://backups/
```

**Backup Location:** `s3://backups/backup-2025-01-04.sql`
**Verified:** ✅ YES

</details>

---

## Current Step: Post-Deployment Monitoring

**Status:** 🔄 In Progress (15 min elapsed)

### Metrics

| Metric | Status | Value |
|--------|--------|-------|
| Response Time | ✅ | 145ms |
| Error Rate | ✅ | 0.2% |
| Traffic | ✅ | Normal |
| Alerts | ✅ | None |

**Continue monitoring for 24 hours.**

---

> 🎯 **Next:** Mark deployment complete after 24h monitoring

[View Full Runbook](https://docs.example.com/runbook) | [Report Issue](https://jira.example.com)
```

---

**Interactive Elements - Part of interactive-checklist skill**
