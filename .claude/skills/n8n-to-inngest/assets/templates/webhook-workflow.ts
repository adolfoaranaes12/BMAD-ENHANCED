/**
 * Webhook Workflow Template
 *
 * Use this template for workflows triggered by webhooks.
 * Common n8n pattern: Webhook Trigger → Validate → Process → Respond
 *
 * Replace TODO comments with your specific implementation.
 */

import { inngest } from './client'; // TODO: Update import path

// TODO: Define your event type
type WebhookEvent = {
  name: 'webhook/received'; // TODO: Update event name
  data: {
    // TODO: Define webhook data structure
    source: string;
    payload: any;
    headers?: Record<string, string>;
  };
};

export const webhookWorkflow = inngest.createFunction(
  {
    id: 'webhook-workflow', // TODO: Update function ID
    name: 'Webhook Workflow', // TODO: Update function name
    retries: 3,
  },
  { event: 'webhook/received' }, // TODO: Update trigger event
  async ({ event, step }) => {
    // Step 1: Validate webhook data
    const validatedData = await step.run('validate-webhook', async () => {
      // TODO: Implement validation logic
      console.log('Validating webhook data');

      const { payload } = event.data;

      // Example: Validate required fields
      // if (!payload.id || !payload.action) {
      //   throw new Error('Invalid webhook payload');
      // }

      return {
        valid: true,
        payload: payload,
      };
    });

    // Step 2: Process webhook data
    const result = await step.run('process-webhook', async () => {
      // TODO: Implement processing logic
      console.log('Processing webhook payload');

      // Example: Update database, trigger actions, etc.
      return {
        processed: true,
        timestamp: new Date().toISOString(),
      };
    });

    // Step 3: Send notification or callback
    await step.run('send-callback', async () => {
      // TODO: Implement callback logic
      console.log('Sending callback or notification');

      // Example: Send confirmation, update status, etc.
      return { callbackSent: true };
    });

    // TODO: Return workflow result
    return {
      success: true,
      processedAt: new Date().toISOString(),
    };
  }
);

// Example: Webhook endpoint handler
// This code would go in your Express/Fastify/Next.js API route
/*
import express from 'express';
import crypto from 'crypto';

const app = express();

// TODO: Update webhook path
app.post('/webhook/endpoint', async (req, res) => {
  try {
    // Pattern 1: Validate webhook signature (recommended for security)
    const signature = req.headers['x-webhook-signature'];
    const isValid = validateSignature(req.body, signature);

    if (!isValid) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Pattern 2: Send event to Inngest (non-blocking)
    await inngest.send({
      name: 'webhook/received',
      data: {
        source: 'external-service', // TODO: Update source
        payload: req.body,
        headers: req.headers,
      },
    });

    // Pattern 3: Return immediate response (202 Accepted)
    res.status(202).json({
      received: true,
      status: 'processing',
    });
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({
      error: 'Failed to process webhook',
    });
  }
});

// Helper: Validate webhook signature (example for HMAC)
function validateSignature(body: any, signature: string): boolean {
  const secret = process.env.WEBHOOK_SECRET!;
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(JSON.stringify(body))
    .digest('hex');

  return signature === expectedSignature;
}
*/

// Example: Specific webhook integrations

// Stripe webhook
export const stripeWebhook = inngest.createFunction(
  {
    id: 'stripe-webhook',
    name: 'Stripe Webhook Handler',
    retries: 3,
  },
  { event: 'stripe/webhook' },
  async ({ event, step }) => {
    const { type, data } = event.data.payload;

    switch (type) {
      case 'payment_intent.succeeded':
        await step.run('handle-payment-success', async () => {
          // TODO: Handle successful payment
          console.log('Payment succeeded:', data.object.id);
          return { handled: true };
        });
        break;

      case 'payment_intent.failed':
        await step.run('handle-payment-failure', async () => {
          // TODO: Handle failed payment
          console.log('Payment failed:', data.object.id);
          return { handled: true };
        });
        break;

      default:
        console.log('Unhandled event type:', type);
    }

    return { eventType: type, processed: true };
  }
);

// GitHub webhook
export const githubWebhook = inngest.createFunction(
  {
    id: 'github-webhook',
    name: 'GitHub Webhook Handler',
    retries: 3,
  },
  { event: 'github/webhook' },
  async ({ event, step }) => {
    const { action, repository } = event.data.payload;

    await step.run('process-github-event', async () => {
      // TODO: Handle GitHub event
      console.log('GitHub event:', action, repository?.name);

      // Example: Trigger CI/CD, update status, etc.
      return { action, repository: repository?.name };
    });

    return { action, processed: true };
  }
);

// Slack webhook
export const slackWebhook = inngest.createFunction(
  {
    id: 'slack-webhook',
    name: 'Slack Webhook Handler',
    retries: 3,
  },
  { event: 'slack/webhook' },
  async ({ event, step }) => {
    const { type, user } = event.data.payload;

    // Handle Slack verification challenge
    if (type === 'url_verification') {
      return { challenge: event.data.payload.challenge };
    }

    await step.run('process-slack-event', async () => {
      // TODO: Handle Slack event
      console.log('Slack event:', type, user?.id);

      // Example: Respond to slash commands, handle interactions, etc.
      return { type, processed: true };
    });

    return { type, processed: true };
  }
);

// Generic webhook with retry and idempotency
export const idempotentWebhook = inngest.createFunction(
  {
    id: 'idempotent-webhook',
    name: 'Idempotent Webhook Handler',
    retries: 3,
    idempotency: 'event.data.payload.id', // Prevent duplicate processing
  },
  { event: 'webhook/idempotent' },
  async ({ event, step }) => {
    const webhookId = event.data.payload.id;

    // Check if already processed
    const existing = await step.run('check-processed', async () => {
      // TODO: Check if webhook already processed
      // return await db.webhookLog.findUnique({ where: { id: webhookId } });
      return null;
    });

    if (existing) {
      console.log('Webhook already processed:', webhookId);
      return { alreadyProcessed: true };
    }

    // Process webhook
    await step.run('process-new-webhook', async () => {
      // TODO: Process webhook
      console.log('Processing new webhook:', webhookId);

      // Record processing
      // await db.webhookLog.create({
      //   data: { id: webhookId, processedAt: new Date() }
      // });

      return { processed: true };
    });

    return { webhookId, processed: true };
  }
);
