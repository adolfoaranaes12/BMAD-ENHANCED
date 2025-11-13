/**
 * Loop Workflow Template
 *
 * Use this template for workflows that process multiple items (Loop node in n8n).
 * Common n8n pattern: Trigger → Fetch Items → Loop Over Items → Process Each
 *
 * Replace TODO comments with your specific implementation.
 */

import { inngest } from './client'; // TODO: Update import path

// TODO: Define your event type
type LoopEvent = {
  name: 'batch/process'; // TODO: Update event name
  data: {
    // TODO: Define event data structure
    batchId: string;
  };
};

export const loopWorkflow = inngest.createFunction(
  {
    id: 'loop-workflow', // TODO: Update function ID
    name: 'Loop Workflow', // TODO: Update function name
    retries: 3,
  },
  { event: 'batch/process' }, // TODO: Update trigger event
  async ({ event, step }) => {
    // Step 1: Fetch items to process
    const items = await step.run('fetch-items', async () => {
      // TODO: Implement logic to fetch items
      console.log('Fetching items to process');

      // Example: Fetch from database
      // return await db.items.findMany({ where: { status: 'pending' } });

      // TODO: Replace with your data source
      return [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' },
      ];
    });

    // Pattern 1: Process each item individually with unique step IDs
    // Best for: Retry isolation (each item can retry independently)
    const results = [];

    for (let i = 0; i < items.length; i++) {
      const result = await step.run(`process-item-${i}`, async () => {
        const item = items[i];

        // TODO: Implement item processing logic
        console.log(`Processing item ${i}:`, item);

        // Example: Update database, call API, etc.
        return {
          itemId: item.id,
          processed: true,
          timestamp: new Date().toISOString(),
        };
      });

      results.push(result);
    }

    // Pattern 2: Process items in batches
    // Best for: Efficiency when items don't need individual retry isolation
    const BATCH_SIZE = 10; // TODO: Adjust batch size as needed

    for (let offset = 0; offset < items.length; offset += BATCH_SIZE) {
      await step.run(`process-batch-${offset}`, async () => {
        const batch = items.slice(offset, offset + BATCH_SIZE);

        // TODO: Implement batch processing logic
        console.log(`Processing batch starting at ${offset}`);

        // Process batch (can include parallel operations)
        const batchResults = await Promise.all(
          batch.map(async item => {
            // TODO: Process each item in batch
            return { itemId: item.id, processed: true };
          })
        );

        return {
          batchStart: offset,
          batchSize: batch.length,
          processed: batchResults.length,
        };
      });
    }

    // Pattern 3: Fan-out for large-scale parallel processing
    // Best for: Very large datasets (10,000+ items)
    // Note: Requires separate worker function (see template below)

    /* Uncomment to use fan-out pattern:
    await step.run('fan-out', async () => {
      const events = items.map(item => ({
        name: 'item/process',
        data: { itemId: item.id }
      }));

      await inngest.send(events);

      return { fanOutCount: items.length };
    });
    */

    // TODO: Return workflow result
    return {
      success: true,
      totalItems: items.length,
      processedItems: results.length,
      processedAt: new Date().toISOString(),
    };
  }
);

// Fan-out worker function (optional - use with Pattern 3)
/*
export const itemProcessor = inngest.createFunction(
  {
    id: 'item-processor',
    name: 'Item Processor',
    retries: 3,
  },
  { event: 'item/process' },
  async ({ event, step }) => {
    const result = await step.run('process-single-item', async () => {
      // TODO: Implement single item processing
      console.log('Processing item:', event.data.itemId);

      return { itemId: event.data.itemId, processed: true };
    });

    return result;
  }
);
*/
