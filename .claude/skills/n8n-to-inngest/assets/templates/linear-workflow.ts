/**
 * Linear Workflow Template
 *
 * Use this template for simple sequential workflows where steps execute one after another.
 * Common n8n pattern: Trigger → Node 1 → Node 2 → Node 3
 *
 * Replace TODO comments with your specific implementation.
 */

import { inngest } from './client'; // TODO: Update import path

// TODO: Define your event type
type WorkflowEvent = {
  name: 'workflow/triggered'; // TODO: Update event name
  data: {
    // TODO: Define event data structure
    userId: string;
    action: string;
  };
};

export const linearWorkflow = inngest.createFunction(
  {
    id: 'linear-workflow', // TODO: Update function ID
    name: 'Linear Workflow', // TODO: Update function name
    retries: 3, // TODO: Adjust retry count as needed
  },
  { event: 'workflow/triggered' }, // TODO: Update trigger event
  async ({ event, step }) => {
    // Step 1: TODO: Replace with your first operation
    const stepOneResult = await step.run('step-one', async () => {
      // Example: Fetch data from API
      console.log('Executing step one with data:', event.data);

      // TODO: Implement your logic here
      return {
        success: true,
        data: {}, // TODO: Return your data
      };
    });

    // Step 2: TODO: Replace with your second operation
    const stepTwoResult = await step.run('step-two', async () => {
      // Example: Transform data
      console.log('Executing step two with result:', stepOneResult);

      // TODO: Implement your logic here
      // You can use stepOneResult from the previous step
      return {
        success: true,
        transformed: {}, // TODO: Return transformed data
      };
    });

    // Step 3: TODO: Replace with your third operation
    await step.run('step-three', async () => {
      // Example: Send notification or update database
      console.log('Executing step three with result:', stepTwoResult);

      // TODO: Implement your logic here
      // You can use results from previous steps
      return { completed: true };
    });

    // TODO: Return final workflow result
    return {
      success: true,
      processedAt: new Date().toISOString(),
    };
  }
);
