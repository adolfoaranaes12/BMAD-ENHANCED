# Checklist Templates

## Overview

Ready-to-use templates for common workflow types. Customize these templates for your specific needs.

---

## Template 1: Linear Workflow Checklist

```markdown
# [Workflow Name]

**Type:** Linear
**Estimated Time:** [X hours/days]
**Owner:** [Person/Team]
**Last Updated:** [Date]

## Overview
[Brief description of workflow purpose and expected outcome]

## Prerequisites
- [ ] Prerequisite 1
- [ ] Prerequisite 2
- [ ] Prerequisite 3

---

## Progress Tracker

**Overall:** [█████░░░░░] 50% (5/10 steps)

**Current Step:** [Step N Name]

---

## Step 1: [Step Name]

**Status:** ⬜ Not Started | 🔄 In Progress | ✅ Complete
**Estimated Time:** [X minutes]
**Owner:** [Person]

**Description:**
[What needs to be done in this step]

**Instructions:**
1. [Action 1]
2. [Action 2]
3. [Action 3]

**Validation:**
- [ ] Success criterion 1
- [ ] Success criterion 2

**Resources:**
- [Link to documentation]
- [Tool/system access]

**Common Issues:**
- **Issue:** [Description] → **Solution:** [Fix]

**Next:** Proceed to Step 2

---

## Step 2: [Step Name]

[Repeat template for each step]

---

## Completion

- [ ] All steps complete
- [ ] All validations passed
- [ ] Documentation updated

**Completed By:** ____________
**Date:** ____________
**Notes:** ____________
```

---

## Template 2: Branching Workflow Checklist

```markdown
# [Workflow Name with Decisions]

**Type:** Branching
**Estimated Time:** [X hours/days]
**Last Updated:** [Date]

## Overview
[Workflow description with mention of decision points]

## Decision Tree

```
START
  │
  ├─ Step 1
  │
  ├─ DECISION: [Question]?
  │    ├─ Option A → Steps 3A, 4A → END
  │    └─ Option B → Steps 3B, 4B, 5B → END
```

---

## Step 1: [Initial Step]

**Status:** ⬜ Not Started | ✅ Complete

[Standard step template]

**Next:** Proceed to Decision Point

---

## Decision Point: [Question]

**Status:** ⬜ Awaiting Decision

**Question:** [What needs to be decided?]

**Options:**

### Option A: [Choice 1]
**When to choose:**
- Criterion 1
- Criterion 2

**Implications:**
- [What happens if you choose this]

**Next Steps:** Proceed to Step 3A

### Option B: [Choice 2]
**When to choose:**
- Criterion 1
- Criterion 2

**Implications:**
- [What happens if you choose this]

**Next Steps:** Proceed to Step 3B

**Decision Made:** [ ] Option A | [ ] Option B
**Decided By:** ____________
**Rationale:** ____________

---

## Path A: [If Option A chosen]

### Step 3A: [Step Name]
[Standard step template]

### Step 4A: [Step Name]
[Standard step template]

---

## Path B: [If Option B chosen]

### Step 3B: [Step Name]
[Standard step template]

### Step 4B: [Step Name]
[Standard step template]

---

## Completion
[Standard completion section]
```

---

## Template 3: Cyclic Workflow with Validation

```markdown
# [Iterative Workflow Name]

**Type:** Cyclic
**Max Iterations:** [N cycles]
**Current Iteration:** [X of N]

## Overview
[Description mentioning iterative nature and exit conditions]

## Iteration Tracker

| Iteration | Status | Started | Completed | Notes |
|-----------|--------|---------|-----------|-------|
| 1 | ✅ Complete | [Date] | [Date] | [Notes] |
| 2 | 🔄 In Progress | [Date] | ___ | ___ |
| 3 | ⬜ Not Started | ___ | ___ | ___ |

---

## Step 1: [Preparation]

**Status:** ⬜ Not Started | ✅ Complete
[Standard step template]

---

## Step 2: [Implementation]

**Status:** ⬜ Not Started | ✅ Complete
[Standard step template]

---

## Step 3: Validation Gate

**Purpose:** Verify quality before proceeding

**Validation Checklist:**
- [ ] Check 1: [Description] - ⬜ Pass | ❌ Fail
- [ ] Check 2: [Description] - ⬜ Pass | ❌ Fail
- [ ] Check 3: [Description] - ⬜ Pass | ❌ Fail

**Result:** ⬜ ALL PASS | ❌ SOME FAILED

---

## Decision: Validation Passed?

### If ALL PASS:
✅ **Proceed to Completion**
- Move to Step 4
- Mark workflow complete

### If ANY FAIL:
❌ **Return to Step 2**
- Document what failed
- Fix issues
- Increment iteration counter
- Re-run validation

**Failures This Iteration:**
- [List what failed and why]

**Actions Taken:**
- [What was done to address failures]

**Max Iterations Reached?**
- [ ] NO → Continue to next iteration
- [ ] YES → Escalate to [Person/Team]

---

## Step 4: [Finalization]

**Status:** ⬜ Not Started | ✅ Complete
[Standard step template]

---

## Completion
[Standard completion section]
```

---

## Template 4: Validation/Audit Checklist

```markdown
# [Validation/Audit Name]

**Type:** Validation Checklist
**Total Items:** [N]
**Completion Required:** [All | X of N]
**Due Date:** [Date]

## Overview
[Purpose of validation/audit]

## Summary

**Progress:** [█████░░░░░] 50% (10/20 items)

**Status:**
- ✅ Passed: 8
- ❌ Failed: 2
- ⬜ Not Checked: 10

**Overall Result:** ⬜ PASS | ⬜ FAIL | ⬜ IN PROGRESS

---

## Category 1: [Category Name]

**Items:** [N items]
**Status:** [X/N complete]

### Item 1.1: [Item Name]

**Priority:** 🔴 Critical | 🟡 High | 🟢 Medium | ⚪ Low
**Status:** ⬜ Not Checked | ✅ Pass | ❌ Fail

**Requirement:**
[What must be true for this to pass]

**How to Verify:**
1. [Step to check]
2. [Step to check]

**Result:** ⬜ Pass | ❌ Fail

**If Fail:**
- **Issue:** [What's wrong]
- **Impact:** [Why it matters]
- **Remediation:** [How to fix]
- **Owner:** [Who fixes it]
- **Due Date:** [When to fix by]

**Evidence:** [Link to proof, screenshot, etc.]

---

### Item 1.2: [Item Name]
[Repeat for each item]

---

## Category 2: [Category Name]
[Repeat for each category]

---

## Action Items

**Failed Items Requiring Action:**

| ID | Item | Priority | Owner | Due Date | Status |
|----|------|----------|-------|----------|--------|
| 1.1 | [Name] | 🔴 Critical | [Person] | [Date] | ⬜ Open |
| 2.3 | [Name] | 🟡 High | [Person] | [Date] | 🔄 In Progress |

---

## Sign-Off

**Audit Complete:** ⬜ YES | ⬜ NO

**Overall Assessment:**
- **Total Items:** [N]
- **Passed:** [N]
- **Failed:** [N]
- **Pass Rate:** [X%]

**Result:** ⬜ APPROVED | ⬜ CONDITIONAL (with action items) | ⬜ REJECTED

**Audited By:** ____________
**Date:** ____________
**Approved By:** ____________
**Date:** ____________
**Notes:** ____________
```

---

## Template 5: Deployment Checklist

```markdown
# Deployment Checklist: [Application Name]

**Environment:** Production | Staging | Development
**Version:** [v1.2.3]
**Deployment Date:** [Date]
**Deployment Time:** [Time]
**Deployed By:** [Person]

## Overview
Deploy [Application] version [X] to [Environment]

---

## Pre-Deployment

### Code Readiness
- [ ] All tests passing (link: [CI Results])
- [ ] Code reviewed and approved
- [ ] Version tagged in git
- [ ] Changelog updated

### Infrastructure Readiness
- [ ] Server resources available
- [ ] Database migrations prepared
- [ ] SSL certificates valid
- [ ] DNS records configured

### Communication
- [ ] Stakeholders notified
- [ ] Maintenance window scheduled (if needed)
- [ ] Rollback plan documented

---

## Deployment Steps

### Step 1: Backup Current State
**Status:** ⬜ Not Started | ✅ Complete

- [ ] Database backup created
- [ ] Application files backed up
- [ ] Configuration files backed up

**Backup Location:** ____________
**Backup Verified:** ⬜ YES

---

### Step 2: Deploy New Code
**Status:** ⬜ Not Started | ✅ Complete

**Commands:**
```bash
git pull origin main
npm install
npm run build
pm2 restart app
```

- [ ] Code pulled successfully
- [ ] Dependencies installed
- [ ] Build completed without errors
- [ ] Application restarted

---

### Step 3: Run Migrations
**Status:** ⬜ Not Started | ✅ Complete

**Commands:**
```bash
npm run migrate
```

- [ ] Migrations ran successfully
- [ ] No migration errors
- [ ] Database schema updated

---

### Step 4: Verify Deployment
**Status:** ⬜ Not Started | ✅ Complete

**Health Checks:**
- [ ] Application responding (curl [URL])
- [ ] Database connections working
- [ ] API endpoints responding
- [ ] Static assets loading

**Smoke Tests:**
- [ ] User login works
- [ ] Core feature 1 works
- [ ] Core feature 2 works

---

## Post-Deployment

### Monitoring
- [ ] Application logs checked (last 15 min)
- [ ] Error rates normal
- [ ] Response times normal
- [ ] CPU/Memory usage normal

### Validation
- [ ] 10 min monitoring passed
- [ ] No customer issues reported
- [ ] All systems green

### Rollback Decision

**Deployment Successful?**
- [✅] YES → Mark complete, monitor for 24h
- [❌] NO → Execute rollback plan

---

## Rollback Plan (If Needed)

### Step 1: Rollback Code
```bash
git reset --hard [previous-commit]
npm install
npm run build
pm2 restart app
```

### Step 2: Rollback Database
```bash
npm run migrate:rollback
```

### Step 3: Verify Rollback
- [ ] Application responding
- [ ] Previous version active
- [ ] Stability restored

---

## Completion

**Deployment Status:** ⬜ SUCCESS | ⬜ FAILED (Rolled Back)

**Deployed By:** ____________
**Verified By:** ____________
**Date/Time:** ____________
**Notes:** ____________

**Post-Deployment Monitoring:** ⬜ 24h | ⬜ 48h | ⬜ 1 week
```

---

## Template Customization Tips

1. **Add Your Branding** - Company logo, colors, style
2. **Adjust Time Estimates** - Based on your team's velocity
3. **Include Your Tools** - Specific systems, links, commands
4. **Add Team Context** - Roles, contact info, escalation paths
5. **Embed Examples** - Show what "good" looks like
6. **Link Resources** - Documentation, runbooks, playbooks
7. **Track Metrics** - Add fields for time tracking, success rates
8. **Iterate** - Update templates based on actual usage

---

**Checklist Templates - Part of interactive-checklist skill**
