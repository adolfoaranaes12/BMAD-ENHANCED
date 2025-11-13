/**
 * Conditional Workflow Template
 *
 * Use this template for workflows with branching logic (If/Switch nodes in n8n).
 * Common n8n pattern: Trigger → If Node → Branch A / Branch B
 *
 * Replace TODO comments with your specific implementation.
 */

import { inngest } from './client'; // TODO: Update import path

// TODO: Define your event type
type ConditionalEvent = {
  name: 'conditional/triggered'; // TODO: Update event name
  data: {
    // TODO: Define event data structure
    userId: string;
    condition: string;
  };
};

export const conditionalWorkflow = inngest.createFunction(
  {
    id: 'conditional-workflow', // TODO: Update function ID
    name: 'Conditional Workflow', // TODO: Update function name
    retries: 3,
  },
  { event: 'conditional/triggered' }, // TODO: Update trigger event
  async ({ event, step }) => {
    // Step 1: Fetch or prepare data for conditional check
    const data = await step.run('fetch-data', async () => {
      // TODO: Implement data fetching logic
      console.log('Fetching data for condition check');

      return {
        // TODO: Return data needed for conditional logic
        status: 'active',
        value: 100,
      };
    });

    // Conditional Logic Pattern 1: Simple If/Else
    // TODO: Replace with your condition
    if (data.status === 'active') {
      // True branch
      await step.run('active-branch', async () => {
        // TODO: Implement logic for active status
        console.log('Processing active branch');
        return { branch: 'active' };
      });
    } else {
      // False branch
      await step.run('inactive-branch', async () => {
        // TODO: Implement logic for inactive status
        console.log('Processing inactive branch');
        return { branch: 'inactive' };
      });
    }

    // Conditional Logic Pattern 2: Multiple Conditions
    // TODO: Replace with your conditions
    if (data.value > 100) {
      await step.run('high-value-branch', async () => {
        console.log('High value processing');
        return { tier: 'premium' };
      });
    } else if (data.value > 50) {
      await step.run('medium-value-branch', async () => {
        console.log('Medium value processing');
        return { tier: 'standard' };
      });
    } else {
      await step.run('low-value-branch', async () => {
        console.log('Low value processing');
        return { tier: 'basic' };
      });
    }

    // Conditional Logic Pattern 3: Switch Statement
    // TODO: Replace with your switch logic
    const action = event.data.condition;

    switch (action) {
      case 'create':
        await step.run('create-action', async () => {
          // TODO: Implement create logic
          console.log('Creating resource');
          return { action: 'create' };
        });
        break;

      case 'update':
        await step.run('update-action', async () => {
          // TODO: Implement update logic
          console.log('Updating resource');
          return { action: 'update' };
        });
        break;

      case 'delete':
        await step.run('delete-action', async () => {
          // TODO: Implement delete logic
          console.log('Deleting resource');
          return { action: 'delete' };
        });
        break;

      default:
        throw new Error(`Unknown action: ${action}`);
    }

    // TODO: Return workflow result
    return {
      success: true,
      condition: event.data.condition,
      processedAt: new Date().toISOString(),
    };
  }
);
