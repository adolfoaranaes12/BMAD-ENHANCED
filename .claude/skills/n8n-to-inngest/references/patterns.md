# n8n to Inngest Translation Patterns

This reference provides detailed code examples for common n8n workflow patterns and their Inngest equivalents.

## Table of Contents

1. [Simple Linear Workflow](#simple-linear-workflow)
2. [Conditional Logic (If Node)](#conditional-logic-if-node)
3. [Loops and Iteration](#loops-and-iteration)
4. [Error Handling](#error-handling)
5. [Wait/Delay Operations](#waitdelay-operations)
6. [Calling Other Workflows](#calling-other-workflows-execute-workflow)
7. [Complete Translation Example](#complete-translation-example)

---

## Simple Linear Workflow

**n8n Pattern:** Trigger → HTTP Request → Transform → Send Email

**Inngest Implementation:**

```typescript
import { inngest } from './client';

inngest.createFunction(
  {
    id: 'simple-workflow',
    name: 'Simple Workflow',
    retries: 3
  },
  { event: 'workflow/triggered' },
  async ({ event, step }) => {
    // Step 1: HTTP Request (n8n: HTTP Request node)
    const apiData = await step.run('fetch-data', async () => {
      const response = await fetch('https://api.example.com/data', {
        headers: {
          'Authorization': `Bearer ${process.env.API_KEY}`
        }
      });

      if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
      }

      return response.json();
    });

    // Step 2: Transform (n8n: Set/Function node)
    const transformed = await step.run('transform', async () => {
      return {
        name: apiData.user.name,
        email: apiData.user.email,
        processed: true,
        timestamp: new Date().toISOString()
      };
    });

    // Step 3: Send Email (n8n: Send Email node)
    await step.run('send-email', async () => {
      await emailService.send({
        to: transformed.email,
        subject: 'Processing Complete',
        body: `Hello ${transformed.name}, your data has been processed.`
      });

      return { sent: true, recipient: transformed.email };
    });

    return {
      success: true,
      processedUser: transformed.name
    };
  }
);
```

**Key Points:**
- Each n8n node becomes a separate `step.run()` for retry isolation
- External API calls and email sending are separate steps
- Return values from each step are automatically stored and available to subsequent steps
- The function returns a summary of the workflow execution

---

## Conditional Logic (If Node)

**n8n Pattern:** If Node with true/false branches based on conditions

**Inngest Implementation:**

### Simple If/Else

```typescript
inngest.createFunction(
  { id: 'conditional-workflow', name: 'Conditional Workflow' },
  { event: 'user/action' },
  async ({ event, step }) => {
    // Fetch user data (n8n: HTTP Request or Database node)
    const userData = await step.run('fetch-user', async () => {
      return await db.user.findUnique({
        where: { id: event.data.userId }
      });
    });

    // n8n: If node checking isPremium
    if (userData.isPremium) {
      // True branch
      await step.run('premium-flow', async () => {
        await sendPremiumWelcome(userData);
        await grantPremiumAccess(userData);
        return { tier: 'premium' };
      });
    } else {
      // False branch
      await step.run('standard-flow', async () => {
        await sendStandardWelcome(userData);
        await grantStandardAccess(userData);
        return { tier: 'standard' };
      });
    }

    return { userId: userData.id, processed: true };
  }
);
```

### Switch Statement (n8n: Switch Node)

```typescript
inngest.createFunction(
  { id: 'switch-workflow', name: 'Switch Workflow' },
  { event: 'resource/action' },
  async ({ event, step }) => {
    const action = event.data.action;

    // n8n: Switch node with multiple outputs
    switch (action) {
      case 'create':
        await step.run('create-resource', async () => {
          return await db.resource.create({
            data: event.data.resource
          });
        });
        break;

      case 'update':
        await step.run('update-resource', async () => {
          return await db.resource.update({
            where: { id: event.data.resourceId },
            data: event.data.resource
          });
        });
        break;

      case 'delete':
        await step.run('delete-resource', async () => {
          return await db.resource.delete({
            where: { id: event.data.resourceId }
          });
        });
        break;

      default:
        throw new Error(`Unknown action: ${action}`);
    }

    return { action, completed: true };
  }
);
```

### Object Map Pattern (Alternative to Switch)

```typescript
// More maintainable for complex branching
const handlers = {
  'create': async (step, data) =>
    step.run('create', async () => createResource(data)),

  'update': async (step, data) =>
    step.run('update', async () => updateResource(data)),

  'delete': async (step, data) =>
    step.run('delete', async () => deleteResource(data)),
};

inngest.createFunction(
  { id: 'action-handler', name: 'Action Handler' },
  { event: 'resource/action' },
  async ({ event, step }) => {
    const handler = handlers[event.data.action];

    if (!handler) {
      throw new Error(`Unknown action: ${event.data.action}`);
    }

    await handler(step, event.data);
    return { action: event.data.action, completed: true };
  }
);
```

---

## Loops and Iteration

**n8n Pattern:** Loop Over Items node processing multiple items

### Basic Loop with Individual Step IDs

```typescript
inngest.createFunction(
  { id: 'loop-workflow', name: 'Loop Workflow' },
  { event: 'batch/process' },
  async ({ event, step }) => {
    // Fetch items to process (n8n: Database or HTTP Request node)
    const items = await step.run('fetch-items', async () => {
      return await db.items.findMany({
        where: { status: 'pending' }
      });
    });

    // n8n: Loop Over Items node
    // Process each item in a separate step for retry isolation
    const results = [];

    for (let i = 0; i < items.length; i++) {
      const result = await step.run(`process-item-${i}`, async () => {
        const item = items[i];

        // Process the item
        const processed = await processItem(item);

        // Update in database
        await db.items.update({
          where: { id: item.id },
          data: {
            status: 'completed',
            result: processed
          }
        });

        return { itemId: item.id, result: processed };
      });

      results.push(result);
    }

    return {
      totalProcessed: results.length,
      results
    };
  }
);
```

### Batch Processing Pattern

```typescript
inngest.createFunction(
  { id: 'batch-processor', name: 'Batch Processor' },
  { event: 'batch/process-large' },
  async ({ event, step }) => {
    const BATCH_SIZE = 100;

    const totalItems = await step.run('count-items', async () => {
      return await db.items.count({
        where: { status: 'pending' }
      });
    });

    // Process in batches
    for (let offset = 0; offset < totalItems; offset += BATCH_SIZE) {
      await step.run(`process-batch-${offset}`, async () => {
        const batch = await db.items.findMany({
          where: { status: 'pending' },
          take: BATCH_SIZE,
          skip: offset
        });

        // Process batch (can include parallel operations within)
        const results = await Promise.all(
          batch.map(item => processItem(item))
        );

        // Update batch
        await db.items.updateMany({
          where: {
            id: { in: batch.map(item => item.id) }
          },
          data: { status: 'completed' }
        });

        return {
          batchSize: batch.length,
          processed: results.length
        };
      });
    }

    return { totalItems, batchSize: BATCH_SIZE };
  }
);
```

### Fan-out Pattern (Parallel Processing)

```typescript
inngest.createFunction(
  { id: 'fan-out-coordinator', name: 'Fan-out Coordinator' },
  { event: 'batch/fan-out' },
  async ({ event, step }) => {
    const items = await step.run('fetch-items', async () => {
      return await db.items.findMany({
        where: { status: 'pending' }
      });
    });

    // Send individual events for parallel processing
    await step.run('fan-out', async () => {
      await Promise.all(
        items.map(item =>
          inngest.send({
            name: 'item/process',
            data: { itemId: item.id }
          })
        )
      );

      return { fanned: items.length };
    });

    return { totalItems: items.length };
  }
);

// Separate function to process individual items (runs in parallel)
inngest.createFunction(
  { id: 'item-processor', name: 'Item Processor' },
  { event: 'item/process' },
  async ({ event, step }) => {
    const result = await step.run('process-item', async () => {
      return await processItem(event.data.itemId);
    });

    return { itemId: event.data.itemId, result };
  }
);
```

---

## Error Handling

**n8n Pattern:** Error Workflow trigger and error handling nodes

### Basic Error Handling with Retries

```typescript
inngest.createFunction(
  {
    id: 'workflow-with-retries',
    name: 'Workflow with Retries',
    retries: 3 // Retry the entire function up to 3 times
  },
  { event: 'workflow/start' },
  async ({ event, step }) => {
    // Individual steps also retry automatically on failure
    const data = await step.run('fetch-data', async () => {
      const response = await fetch('https://api.example.com/data');

      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }

      return response.json();
    });

    return { success: true, data };
  }
);
```

### Error Handling with onFailure (n8n: Error Workflow)

```typescript
// Main workflow
inngest.createFunction(
  {
    id: 'main-workflow',
    name: 'Main Workflow',
    retries: 3,
    // n8n: Error Workflow trigger equivalent
    onFailure: async ({ error, event, step }) => {
      // Send alert to monitoring system
      await step.run('send-error-alert', async () => {
        await monitoringService.alert({
          severity: 'error',
          message: `Workflow failed: ${error.message}`,
          event: event.name,
          data: event.data,
          stack: error.stack
        });
      });

      // Send event to error handling workflow
      await step.run('trigger-error-workflow', async () => {
        await inngest.send({
          name: 'workflow/failed',
          data: {
            originalEvent: event,
            error: {
              message: error.message,
              name: error.name,
              stack: error.stack
            },
            timestamp: Date.now()
          }
        });
      });
    }
  },
  { event: 'workflow/triggered' },
  async ({ event, step }) => {
    // Workflow logic that might fail
    const result = await step.run('risky-operation', async () => {
      return await performRiskyOperation(event.data);
    });

    return { result };
  }
);

// Error handling workflow (n8n: Error Workflow)
inngest.createFunction(
  { id: 'error-handler', name: 'Error Handler' },
  { event: 'workflow/failed' },
  async ({ event, step }) => {
    // Log error to database
    await step.run('log-error', async () => {
      return await db.errorLog.create({
        data: {
          eventName: event.data.originalEvent.name,
          errorMessage: event.data.error.message,
          errorStack: event.data.error.stack,
          timestamp: new Date(event.data.timestamp)
        }
      });
    });

    // Notify administrators
    await step.run('notify-admins', async () => {
      await emailService.send({
        to: 'admin@example.com',
        subject: 'Workflow Failure Alert',
        body: `Error: ${event.data.error.message}`
      });
    });

    return { handled: true };
  }
);
```

### Try/Catch Pattern for Graceful Degradation

```typescript
inngest.createFunction(
  { id: 'graceful-degradation', name: 'Graceful Degradation' },
  { event: 'workflow/start' },
  async ({ event, step }) => {
    // Critical operation - must succeed
    const userData = await step.run('fetch-user', async () => {
      return await db.user.findUnique({
        where: { id: event.data.userId }
      });
    });

    // Optional operation - gracefully handle failure
    let enrichedData = null;
    try {
      enrichedData = await step.run('enrich-data', async () => {
        // This might fail, but we don't want to fail the whole workflow
        const response = await fetch('https://enrichment-api.example.com/enrich', {
          method: 'POST',
          body: JSON.stringify({ userId: userData.id })
        });

        if (!response.ok) {
          throw new Error('Enrichment API failed');
        }

        return response.json();
      });
    } catch (error) {
      // Log the error but continue
      await step.run('log-enrichment-failure', async () => {
        console.error('Enrichment failed:', error);
        return { enrichmentFailed: true };
      });
    }

    // Continue with or without enriched data
    await step.run('process-user', async () => {
      return await processUser(userData, enrichedData);
    });

    return {
      success: true,
      enriched: enrichedData !== null
    };
  }
);
```

---

## Wait/Delay Operations

**n8n Pattern:** Wait node with time delay

### Simple Sleep

```typescript
inngest.createFunction(
  { id: 'delayed-workflow', name: 'Delayed Workflow' },
  { event: 'workflow/start' },
  async ({ event, step }) => {
    await step.run('initial-processing', async () => {
      return await processData(event.data);
    });

    // n8n: Wait node - wait 1 hour
    await step.sleep('wait-1-hour', '1h');

    // Continue after delay
    await step.run('delayed-processing', async () => {
      return await continueProcessing(event.data);
    });

    return { completed: true };
  }
);
```

### Sleep with Duration Options

```typescript
// Sleep durations can be specified in various formats:
// - '30s' - 30 seconds
// - '5m' - 5 minutes
// - '2h' - 2 hours
// - '3d' - 3 days
// - '1w' - 1 week

inngest.createFunction(
  { id: 'multi-delay-workflow', name: 'Multi-Delay Workflow' },
  { event: 'user/onboarding' },
  async ({ event, step }) => {
    // Send welcome email immediately
    await step.run('send-welcome', async () => {
      return await emailService.send({
        to: event.data.email,
        template: 'welcome'
      });
    });

    // Wait 1 day
    await step.sleep('wait-1-day', '1d');

    // Send follow-up email
    await step.run('send-follow-up-1', async () => {
      return await emailService.send({
        to: event.data.email,
        template: 'follow-up-day-1'
      });
    });

    // Wait 3 more days
    await step.sleep('wait-3-days', '3d');

    // Send tips email
    await step.run('send-tips', async () => {
      return await emailService.send({
        to: event.data.email,
        template: 'tips'
      });
    });

    // Wait 1 week
    await step.sleep('wait-1-week', '1w');

    // Send survey
    await step.run('send-survey', async () => {
      return await emailService.send({
        to: event.data.email,
        template: 'survey'
      });
    });

    return { onboardingComplete: true };
  }
);
```

### Sleep Until Specific Time

```typescript
inngest.createFunction(
  { id: 'scheduled-action', name: 'Scheduled Action' },
  { event: 'task/schedule' },
  async ({ event, step }) => {
    // Calculate duration until target time
    const now = Date.now();
    const targetTime = new Date(event.data.scheduledFor).getTime();
    const durationMs = targetTime - now;

    if (durationMs > 0) {
      // Sleep until scheduled time
      await step.sleep('wait-until-scheduled', `${durationMs}ms`);
    }

    // Execute scheduled action
    await step.run('execute-action', async () => {
      return await executeScheduledAction(event.data.action);
    });

    return { executed: true };
  }
);
```

---

## Calling Other Workflows (Execute Workflow)

**n8n Pattern:** Execute Workflow node

### Basic Workflow Invocation

```typescript
// Main workflow
inngest.createFunction(
  { id: 'main-workflow', name: 'Main Workflow' },
  { event: 'main/start' },
  async ({ event, step }) => {
    await step.run('prepare-data', async () => {
      return await prepareData(event.data);
    });

    // n8n: Execute Workflow node
    const subWorkflowResult = await step.invoke('call-sub-workflow', {
      function: 'sub-workflow-function',
      data: {
        userId: event.data.userId,
        action: 'process'
      }
    });

    // Use result from invoked workflow
    await step.run('use-result', async () => {
      return await processResult(subWorkflowResult);
    });

    return { success: true, subResult: subWorkflowResult };
  }
);

// Sub-workflow
inngest.createFunction(
  { id: 'sub-workflow-function', name: 'Sub Workflow' },
  { event: 'sub/workflow' },
  async ({ event, step }) => {
    const result = await step.run('sub-processing', async () => {
      return await performSubProcessing(event.data);
    });

    return { processed: true, data: result };
  }
);
```

### Parallel Workflow Invocation

```typescript
inngest.createFunction(
  { id: 'parallel-workflows', name: 'Parallel Workflows' },
  { event: 'parallel/start' },
  async ({ event, step }) => {
    // Invoke multiple workflows in parallel
    const [result1, result2, result3] = await Promise.all([
      step.invoke('call-workflow-1', {
        function: 'workflow-1',
        data: { type: 'A', ...event.data }
      }),
      step.invoke('call-workflow-2', {
        function: 'workflow-2',
        data: { type: 'B', ...event.data }
      }),
      step.invoke('call-workflow-3', {
        function: 'workflow-3',
        data: { type: 'C', ...event.data }
      })
    ]);

    // Combine results
    await step.run('combine-results', async () => {
      return await combineResults([result1, result2, result3]);
    });

    return {
      success: true,
      results: [result1, result2, result3]
    };
  }
);
```

---

## Complete Translation Example

This example shows a complete n8n workflow translated to Inngest.

### n8n Workflow (User Onboarding)

```json
{
  "name": "User Onboarding",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": { "path": "user-signup" }
    },
    {
      "name": "Validate Data",
      "type": "n8n-nodes-base.function",
      "parameters": {
        "functionCode": "// Validate email and name\nreturn items;"
      }
    },
    {
      "name": "Create User",
      "type": "n8n-nodes-base.postgres",
      "parameters": {
        "operation": "insert",
        "table": "users"
      }
    },
    {
      "name": "Send Welcome Email",
      "type": "n8n-nodes-base.sendgrid",
      "parameters": { "template": "welcome" }
    },
    {
      "name": "Wait 3 Days",
      "type": "n8n-nodes-base.wait",
      "parameters": { "amount": 3, "unit": "days" }
    },
    {
      "name": "Check User Activity",
      "type": "n8n-nodes-base.postgres",
      "parameters": {
        "operation": "select",
        "table": "user_activity"
      }
    },
    {
      "name": "If Active",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "boolean": [{ "value1": "={{$json.active}}", "value2": true }]
        }
      }
    },
    {
      "name": "Send Active User Email",
      "type": "n8n-nodes-base.sendgrid",
      "parameters": { "template": "active-user" }
    },
    {
      "name": "Send Inactive User Email",
      "type": "n8n-nodes-base.sendgrid",
      "parameters": { "template": "inactive-user" }
    }
  ]
}
```

### Inngest Translation

```typescript
import { inngest } from './client';
import { db } from './db';
import { emailService } from './services/email';
import { z } from 'zod';

// 1. Define event type
type UserSignupEvent = {
  name: 'user/signup';
  data: {
    email: string;
    name: string;
    company?: string;
  };
};

// 2. Define validation schema (n8n: Validate Data node)
const signupSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2),
  company: z.string().optional()
});

// 3. Create Inngest function
export const userOnboarding = inngest.createFunction(
  {
    id: 'user-onboarding',
    name: 'User Onboarding Workflow',
    retries: 3,
    onFailure: async ({ error, event, step }) => {
      await step.run('log-failure', async () => {
        console.error('Onboarding failed:', error);
        await db.errorLog.create({
          data: {
            workflow: 'user-onboarding',
            event: JSON.stringify(event),
            error: error.message
          }
        });
      });
    }
  },
  { event: 'user/signup' },
  async ({ event, step }) => {
    // Step 1: Validate Data (n8n: Validate Data node)
    const validatedData = await step.run('validate-data', async () => {
      try {
        return signupSchema.parse(event.data);
      } catch (error) {
        throw new Error(`Invalid signup data: ${error.message}`);
      }
    });

    // Step 2: Create User (n8n: Create User node)
    const user = await step.run('create-user', async () => {
      return await db.user.create({
        data: {
          email: validatedData.email,
          name: validatedData.name,
          company: validatedData.company,
          status: 'active',
          onboardedAt: new Date()
        }
      });
    });

    // Step 3: Send Welcome Email (n8n: Send Welcome Email node)
    await step.run('send-welcome-email', async () => {
      await emailService.send({
        to: user.email,
        template: 'welcome',
        data: {
          name: user.name,
          userId: user.id
        }
      });

      return { sent: true, template: 'welcome' };
    });

    // Step 4: Wait 3 Days (n8n: Wait node)
    await step.sleep('wait-3-days', '3d');

    // Step 5: Check User Activity (n8n: Check User Activity node)
    const activityData = await step.run('check-user-activity', async () => {
      const activityCount = await db.userActivity.count({
        where: {
          userId: user.id,
          createdAt: {
            gte: user.onboardedAt
          }
        }
      });

      return {
        userId: user.id,
        activityCount,
        isActive: activityCount > 0
      };
    });

    // Step 6: Conditional Email (n8n: If node)
    if (activityData.isActive) {
      // True branch (n8n: Send Active User Email)
      await step.run('send-active-user-email', async () => {
        await emailService.send({
          to: user.email,
          template: 'active-user',
          data: {
            name: user.name,
            activityCount: activityData.activityCount
          }
        });

        return { sent: true, template: 'active-user' };
      });
    } else {
      // False branch (n8n: Send Inactive User Email)
      await step.run('send-inactive-user-email', async () => {
        await emailService.send({
          to: user.email,
          template: 'inactive-user',
          data: {
            name: user.name,
            supportLink: 'https://support.example.com'
          }
        });

        return { sent: true, template: 'inactive-user' };
      });
    }

    // Return workflow result
    return {
      userId: user.id,
      email: user.email,
      isActive: activityData.isActive,
      onboardingComplete: true
    };
  }
);

// 4. Webhook handler (replaces n8n webhook trigger)
import express from 'express';

const app = express();

app.post('/webhook/user-signup', async (req, res) => {
  try {
    // Send event to Inngest (non-blocking)
    await inngest.send({
      name: 'user/signup',
      data: {
        email: req.body.email,
        name: req.body.name,
        company: req.body.company
      }
    });

    // Return 202 Accepted immediately
    res.status(202).json({
      message: 'Onboarding started',
      status: 'processing'
    });
  } catch (error) {
    res.status(500).json({
      error: 'Failed to start onboarding',
      message: error.message
    });
  }
});
```

### Key Translation Decisions

1. **Webhook Trigger** → Express endpoint that sends Inngest event
2. **Validate Data node** → Zod schema validation in a step
3. **Create User node** → Prisma database operation in a step
4. **Send Email nodes** → Email service calls in separate steps
5. **Wait node** → `step.sleep('wait-3-days', '3d')`
6. **Check Activity node** → Database query in a step
7. **If node** → JavaScript `if/else` statement
8. **Error Workflow** → `onFailure` handler in function config

### Testing the Translation

```typescript
// test/workflows/user-onboarding.test.ts
import { describe, it, expect, vi } from 'vitest';
import { inngest } from './client';
import { userOnboarding } from './workflows/user-onboarding';

describe('User Onboarding Workflow', () => {
  it('should successfully onboard an active user', async () => {
    // Test with mock event
    const result = await userOnboarding({
      event: {
        name: 'user/signup',
        data: {
          email: 'test@example.com',
          name: 'Test User',
          company: 'Test Co'
        }
      },
      step: mockStepHelpers,
      logger: mockLogger
    });

    expect(result.onboardingComplete).toBe(true);
    expect(result.isActive).toBe(true);
  });

  it('should handle invalid data gracefully', async () => {
    // Test validation failure
    await expect(async () => {
      await userOnboarding({
        event: {
          name: 'user/signup',
          data: {
            email: 'invalid-email',
            name: 'T' // Too short
          }
        },
        step: mockStepHelpers,
        logger: mockLogger
      });
    }).rejects.toThrow('Invalid signup data');
  });
});
```

This complete example demonstrates:
- Systematic translation of each n8n node
- Type-safe event definitions
- Error handling with `onFailure`
- Webhook endpoint integration
- Testing strategy
- Best practices for production use
