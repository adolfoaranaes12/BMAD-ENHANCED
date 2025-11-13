/**
 * Approval Workflow Template (Human-in-the-Loop)
 *
 * Use this template for workflows that require human approval or interaction.
 * Common n8n pattern: Trigger → Process → Wait for Manual Action → Continue
 *
 * Replace TODO comments with your specific implementation.
 */

import { inngest } from './client'; // TODO: Update import path

// TODO: Define your event types
type ApprovalRequestEvent = {
  name: 'approval/request'; // TODO: Update event name
  data: {
    // TODO: Define request data structure
    requestId: string;
    requestedBy: string;
    action: string;
  };
};

type ApprovalResponseEvent = {
  name: 'approval/response';
  data: {
    requestId: string;
    approved: boolean;
    approver: string;
    reason?: string;
  };
};

export const approvalWorkflow = inngest.createFunction(
  {
    id: 'approval-workflow', // TODO: Update function ID
    name: 'Approval Workflow', // TODO: Update function name
    retries: 3,
  },
  { event: 'approval/request' }, // TODO: Update trigger event
  async ({ event, step }) => {
    // Step 1: Prepare data for approval
    const requestData = await step.run('prepare-request', async () => {
      // TODO: Implement request preparation logic
      console.log('Preparing approval request');

      // Example: Fetch additional context, validate data
      return {
        requestId: event.data.requestId,
        action: event.data.action,
        requestedBy: event.data.requestedBy,
        requestedAt: new Date().toISOString(),
      };
    });

    // Step 2: Send approval notification
    await step.run('send-approval-notification', async () => {
      // TODO: Implement notification logic
      console.log('Sending approval notification');

      // Example: Send email, Slack message, or create approval ticket
      // await emailService.send({
      //   to: 'approver@example.com',
      //   subject: 'Approval Required',
      //   body: `Request ${requestData.requestId} needs your approval`,
      // });

      return { notificationSent: true };
    });

    // Step 3: Wait for approval response
    // TODO: Adjust timeout as needed (format: '1h', '1d', '7d', etc.)
    const approval = await step.waitForEvent('wait-for-approval', {
      event: 'approval/response',
      timeout: '7d', // TODO: Adjust timeout
      match: 'data.requestId', // Match on requestId field
    });

    // Handle timeout (no approval received)
    if (!approval) {
      await step.run('handle-timeout', async () => {
        // TODO: Implement timeout handling logic
        console.log('Approval request timed out');

        // Example: Send timeout notification, auto-reject
        return { status: 'timeout', approved: false };
      });

      return {
        success: false,
        status: 'timeout',
        requestId: requestData.requestId,
      };
    }

    // Step 4: Process approval decision
    if (approval.data.approved) {
      // Approved branch
      await step.run('execute-approved-action', async () => {
        // TODO: Implement approved action logic
        console.log('Request approved, executing action');

        // Example: Deploy changes, grant access, process payment
        return {
          status: 'approved',
          executedBy: approval.data.approver,
          executedAt: new Date().toISOString(),
        };
      });

      // Send approval confirmation
      await step.run('send-approval-confirmation', async () => {
        // TODO: Implement confirmation notification
        console.log('Sending approval confirmation');

        // Example: Notify requester of approval
        return { confirmationSent: true };
      });
    } else {
      // Rejected branch
      await step.run('handle-rejection', async () => {
        // TODO: Implement rejection handling logic
        console.log('Request rejected:', approval.data.reason);

        // Example: Rollback changes, notify requester
        return {
          status: 'rejected',
          rejectedBy: approval.data.approver,
          reason: approval.data.reason,
        };
      });

      // Send rejection notification
      await step.run('send-rejection-notification', async () => {
        // TODO: Implement rejection notification
        console.log('Sending rejection notification');

        return { notificationSent: true };
      });
    }

    // TODO: Return workflow result
    return {
      success: true,
      approved: approval.data.approved,
      approver: approval.data.approver,
      requestId: requestData.requestId,
      processedAt: new Date().toISOString(),
    };
  }
);

// Example: Approval endpoint handler
// This would be in your API/webhook handler
/*
import express from 'express';

const app = express();

app.post('/api/approve/:requestId', async (req, res) => {
  const { requestId } = req.params;
  const { approved, reason } = req.body;

  // TODO: Add authentication/authorization
  const approver = req.user?.email || 'unknown';

  // Send approval event
  await inngest.send({
    name: 'approval/response',
    data: {
      requestId,
      approved,
      approver,
      reason,
    },
  });

  res.json({ received: true });
});
*/
