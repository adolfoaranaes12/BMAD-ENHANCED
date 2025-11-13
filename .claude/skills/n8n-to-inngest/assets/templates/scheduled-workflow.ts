/**
 * Scheduled Workflow Template
 *
 * Use this template for workflows triggered by cron schedules.
 * Common n8n pattern: Schedule Trigger → Fetch Data → Process → Notify
 *
 * Replace TODO comments with your specific implementation.
 */

import { inngest } from './client'; // TODO: Update import path

export const scheduledWorkflow = inngest.createFunction(
  {
    id: 'scheduled-workflow', // TODO: Update function ID
    name: 'Scheduled Workflow', // TODO: Update function name
    retries: 3,
  },
  {
    // TODO: Update cron schedule
    // Cron format: "minute hour day month weekday"
    // Examples:
    //   "0 9 * * *"        - Every day at 9:00 AM
    //   "0 */6 * * *"      - Every 6 hours
    //   "0 0 * * 1"        - Every Monday at midnight
    //   "*/15 * * * *"     - Every 15 minutes
    //   "0 9 * * 1-5"      - Weekdays at 9:00 AM
    //   "0 0 1 * *"        - First day of every month at midnight
    cron: '0 9 * * *', // TODO: Update schedule
  },
  async ({ event, step }) => {
    // Step 1: Fetch data for scheduled processing
    const data = await step.run('fetch-scheduled-data', async () => {
      // TODO: Implement data fetching logic
      console.log('Fetching data for scheduled run');

      // Example: Fetch pending tasks, new records, etc.
      // return await db.tasks.findMany({
      //   where: {
      //     scheduledFor: { lte: new Date() },
      //     status: 'pending'
      //   }
      // });

      return {
        timestamp: new Date().toISOString(),
        items: [], // TODO: Replace with actual data
      };
    });

    // Step 2: Process the fetched data
    const processedCount = await step.run('process-data', async () => {
      // TODO: Implement processing logic
      console.log('Processing scheduled data');

      let count = 0;

      // Example: Process each item
      // for (const item of data.items) {
      //   await processItem(item);
      //   count++;
      // }

      return count;
    });

    // Step 3: Generate and send report
    await step.run('send-report', async () => {
      // TODO: Implement reporting logic
      console.log('Sending scheduled report');

      // Example: Send email with summary
      // await emailService.send({
      //   to: 'admin@example.com',
      //   subject: 'Daily Report',
      //   body: `Processed ${processedCount} items`,
      // });

      return {
        reportSent: true,
        processedCount,
      };
    });

    // TODO: Return workflow result
    return {
      success: true,
      processedCount,
      executedAt: new Date().toISOString(),
    };
  }
);

// Example: Multiple schedule patterns

// Daily at specific time
export const dailyReport = inngest.createFunction(
  {
    id: 'daily-report',
    name: 'Daily Report',
  },
  { cron: '0 9 * * *' }, // Every day at 9:00 AM
  async ({ event, step }) => {
    // TODO: Implement daily report logic
    return { type: 'daily-report' };
  }
);

// Hourly processing
export const hourlySync = inngest.createFunction(
  {
    id: 'hourly-sync',
    name: 'Hourly Data Sync',
  },
  { cron: '0 * * * *' }, // Every hour
  async ({ event, step }) => {
    // TODO: Implement hourly sync logic
    return { type: 'hourly-sync' };
  }
);

// Weekday business hours
export const businessHoursCheck = inngest.createFunction(
  {
    id: 'business-hours-check',
    name: 'Business Hours Health Check',
  },
  { cron: '0 9-17 * * 1-5' }, // Weekdays 9 AM - 5 PM
  async ({ event, step }) => {
    // TODO: Implement health check logic
    return { type: 'health-check' };
  }
);

// Monthly cleanup
export const monthlyCleanup = inngest.createFunction(
  {
    id: 'monthly-cleanup',
    name: 'Monthly Data Cleanup',
  },
  { cron: '0 0 1 * *' }, // First day of month at midnight
  async ({ event, step }) => {
    // TODO: Implement cleanup logic
    return { type: 'monthly-cleanup' };
  }
);

// Every 15 minutes
export const frequentMonitoring = inngest.createFunction(
  {
    id: 'frequent-monitoring',
    name: 'Frequent System Monitoring',
  },
  { cron: '*/15 * * * *' }, // Every 15 minutes
  async ({ event, step }) => {
    // TODO: Implement monitoring logic
    return { type: 'monitoring' };
  }
);
