# Inngest Workflow Templates

This directory contains template files for common n8n workflow patterns translated to Inngest.

## Available Templates

### 1. `linear-workflow.ts`
**Use for:** Simple sequential workflows where steps execute one after another.

**n8n Pattern:** Trigger → Node 1 → Node 2 → Node 3

**Example Use Cases:**
- Data fetch → Transform → Store
- API call → Process response → Send notification
- Fetch user → Update profile → Log activity

---

### 2. `conditional-workflow.ts`
**Use for:** Workflows with branching logic based on conditions.

**n8n Pattern:** Trigger → If/Switch Node → Branch A / Branch B

**Example Use Cases:**
- User tier-based processing (premium vs. standard)
- Status-based routing (active, inactive, pending)
- Action routing (create, update, delete)

---

### 3. `loop-workflow.ts`
**Use for:** Processing multiple items or batches of data.

**n8n Pattern:** Trigger → Fetch Items → Loop Over Items → Process Each

**Example Use Cases:**
- Batch email sending
- Bulk data processing
- Multi-item order fulfillment
- Database record migration

**Includes three patterns:**
- Individual item processing (best retry isolation)
- Batch processing (more efficient)
- Fan-out pattern (large-scale parallel processing)

---

### 4. `approval-workflow.ts`
**Use for:** Workflows requiring human approval or interaction.

**n8n Pattern:** Trigger → Process → Wait for Manual Action → Continue

**Example Use Cases:**
- Document approval workflows
- Expense report approvals
- Deployment approvals
- User access requests

**Features:**
- Configurable timeout
- Approval and rejection handling
- Notification system integration

---

### 5. `scheduled-workflow.ts`
**Use for:** Workflows triggered by cron schedules.

**n8n Pattern:** Schedule Trigger → Fetch Data → Process → Notify

**Example Use Cases:**
- Daily reports
- Hourly data synchronization
- Weekly cleanups
- Monthly billing runs

**Includes examples for:**
- Daily schedules
- Hourly schedules
- Weekday-only schedules
- Monthly schedules
- Custom intervals (every N minutes)

---

### 6. `webhook-workflow.ts`
**Use for:** Workflows triggered by external webhooks.

**n8n Pattern:** Webhook Trigger → Validate → Process → Respond

**Example Use Cases:**
- Payment provider webhooks (Stripe, PayPal)
- GitHub/GitLab webhooks
- Slack integration webhooks
- Custom API callbacks

**Includes examples for:**
- Signature validation
- Idempotent processing
- Specific integrations (Stripe, GitHub, Slack)
- Async response patterns

---

## How to Use Templates

1. **Choose the appropriate template** based on your workflow type
2. **Copy the template** to your project's workflow directory
3. **Search for `TODO` comments** in the file
4. **Replace placeholder code** with your specific implementation
5. **Update event types** and function IDs to match your naming conventions
6. **Test thoroughly** before deploying to production

## Combining Templates

Many real-world workflows combine multiple patterns. For example:

- **Scheduled + Loop:** Daily batch processing of pending items
- **Webhook + Conditional:** Process webhook and route based on event type
- **Approval + Conditional:** Different approval flows based on request value
- **Loop + Approval:** Process items with approval required for certain conditions

Simply combine the relevant sections from multiple templates into a single workflow.

## Template Conventions

All templates follow these conventions:

- **Event Types:** TypeScript types defined at the top
- **Step IDs:** kebab-case, descriptive names
- **Error Handling:** Retry configuration included
- **Comments:** `TODO` marks for customization points
- **Logging:** Console.log statements for visibility
- **Return Values:** Structured return objects with metadata

## Additional Resources

For more detailed examples and patterns, see:
- `references/patterns.md` - Comprehensive code examples
- `references/challenges.md` - Common challenges and solutions
- `SKILL.md` - Full translation methodology
