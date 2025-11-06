# BMAD Enhanced - Advanced Workflow Customization

**Version:** 2.0
**Last Updated:** 2025-11-05
**Status:** Production Ready

## Overview

This guide demonstrates advanced workflow customization techniques for BMAD Enhanced. Learn how to create custom workflows, chain commands, build automation pipelines, and extend the system with your own skills and subagents.

---

## Table of Contents

1. [Custom Skill Creation](#custom-skill-creation)
2. [Workflow Orchestration Patterns](#workflow-orchestration-patterns)
3. [Command Chaining & Pipelines](#command-chaining--pipelines)
4. [Custom Subagent Development](#custom-subagent-development)
5. [Integration with External Tools](#integration-with-external-tools)
6. [Advanced Templating](#advanced-templating)
7. [Workflow State Management](#workflow-state-management)
8. [Real-World Examples](#real-world-examples)

---

## Custom Skill Creation

### Example 1: Custom Deployment Skill

Create a custom deployment skill that integrates with your CI/CD pipeline.

#### Step 1: Create Skill Structure

```bash
mkdir -p .claude/skills/deployment/deploy-production
cd .claude/skills/deployment/deploy-production
```

#### Step 2: Define Skill (SKILL.md)

```markdown
---
name: deploy-production
description: Deploy application to production with safety checks
version: 1.0
category: deployment
complexity: complex
inputs:
  - name: version
    type: string
    required: true
    description: Version tag to deploy (e.g., v1.2.3)
  - name: environment
    type: string
    required: false
    default: production
    description: Target environment
  - name: dry_run
    type: boolean
    required: false
    default: false
    description: Perform dry run without actual deployment
outputs:
  - name: deployment_url
    type: string
    description: URL of deployed application
  - name: deployment_id
    type: string
    description: Unique deployment identifier
  - name: rollback_command
    type: string
    description: Command to rollback if needed
telemetry:
  command: deploy-production
  track_duration: true
  track_success: true
  alert_on_failure: true
---

# Skill: deploy-production

## Description
Deploys application to production environment with comprehensive safety checks,
monitoring, and automatic rollback capabilities.

## Pre-requisites
- CI/CD pipeline configured
- Production credentials available
- Health check endpoints defined
- Rollback procedure documented

## Workflow Steps

### 1. Pre-Deployment Validation
**Command:** `python scripts/validate-deployment.py --version ${version} --env ${environment}`
**Acceptance:**
- Exit code 0
- All health checks pass
- No blocking issues reported
- Version exists and is signed

**Error Handling:**
If validation fails, abort deployment and report specific issue.

**Telemetry:**
```json
{
  "step": "validate",
  "version": "${version}",
  "checks_passed": 15,
  "checks_failed": 0,
  "duration_ms": 2500
}
```

---

### 2. Create Backup
**Command:** `python scripts/backup.py --env ${environment} --backup-type full`
**Acceptance:**
- Backup created successfully
- Backup verified (checksum matches)
- Backup stored in S3
- Backup size reasonable (< 10GB)

**Error Handling:**
If backup fails, abort deployment.

**Telemetry:**
```json
{
  "step": "backup",
  "backup_id": "backup-20251105-001",
  "backup_size_mb": 250,
  "duration_ms": 8000
}
```

---

### 3. Enable Maintenance Mode
**Command:** `python scripts/maintenance-mode.py --enable --message "Deploying ${version}"`
**Acceptance:**
- Maintenance page visible to users
- API returns 503 status
- Background jobs paused

**Error Handling:**
If maintenance mode fails, continue but warn ops team.

---

### 4. Deploy Application
**Command:** `python scripts/deploy.py --version ${version} --env ${environment} --strategy blue-green`
**Acceptance:**
- Deployment completes successfully
- All pods/instances healthy
- Database migrations applied
- Static assets deployed

**Error Handling:**
If deployment fails:
1. Disable maintenance mode
2. Trigger automatic rollback
3. Alert on-call engineer
4. Create incident report

**Telemetry:**
```json
{
  "step": "deploy",
  "version": "${version}",
  "strategy": "blue-green",
  "instances_deployed": 10,
  "migration_count": 3,
  "duration_ms": 45000
}
```

---

### 5. Run Smoke Tests
**Command:** `python scripts/smoke-tests.py --env ${environment} --endpoint ${deployment_url}`
**Acceptance:**
- All critical endpoints respond 200
- Response times < 500ms
- No errors in logs
- Database connectivity confirmed

**Error Handling:**
If smoke tests fail:
1. Trigger rollback immediately
2. Keep maintenance mode enabled
3. Alert engineering team

**Telemetry:**
```json
{
  "step": "smoke_tests",
  "tests_run": 25,
  "tests_passed": 25,
  "tests_failed": 0,
  "avg_response_ms": 180,
  "duration_ms": 12000
}
```

---

### 6. Gradual Traffic Shift
**Command:** `python scripts/traffic-shift.py --from blue --to green --steps "10,25,50,100" --step-duration 300`
**Acceptance:**
- Traffic shifts gradually (10% → 25% → 50% → 100%)
- Error rates stable at each step
- No increase in latency
- Canary analysis passes

**Error Handling:**
If error rate increases or latency spikes:
1. Stop traffic shift
2. Shift all traffic back to blue
3. Investigate issue

**Telemetry:**
```json
{
  "step": "traffic_shift",
  "shift_steps": [10, 25, 50, 100],
  "current_step": 100,
  "error_rate_pct": 0.02,
  "avg_latency_ms": 120,
  "duration_ms": 900000
}
```

---

### 7. Disable Maintenance Mode
**Command:** `python scripts/maintenance-mode.py --disable`
**Acceptance:**
- Maintenance page removed
- Users can access application
- Background jobs resumed

---

### 8. Post-Deployment Verification
**Command:** `python scripts/verify-deployment.py --version ${version} --env ${environment}`
**Acceptance:**
- Version tag matches deployed version
- All services healthy
- Metrics within normal range
- No critical errors in logs

**Error Handling:**
If verification fails, alert team but don't rollback automatically.

---

### 9. Update Documentation
**Command:** `python scripts/update-deployment-log.py --version ${version} --deployment-id ${deployment_id}`
**Acceptance:**
- Deployment logged in wiki
- Changelog updated
- Release notes published
- Team notified

---

## Rollback Procedure

If deployment fails at any step:

```bash
# Automatic rollback
python scripts/rollback.py \
  --deployment-id ${deployment_id} \
  --restore-backup backup-20251105-001 \
  --reason "Deployment failed at step 5"

# Rollback command stored in output for manual execution
```

## Monitoring

Post-deployment monitoring for 24 hours:
- Error rates
- Response times
- CPU/Memory usage
- Database connections
- User complaints

## Success Criteria

Deployment considered successful when:
- All 9 steps completed successfully
- Smoke tests pass
- Traffic shift to 100% complete
- No rollback triggered
- Post-deployment verification passes
- Error rates < 0.1%
- Latency < 200ms (p95)

## References

- [Deployment Checklist](/references/deployment-checklist.md)
- [Rollback Procedure](/references/rollback-procedure.md)
- [Monitoring Dashboard](https://monitoring.example.com/production)
- [Incident Response](/references/incident-response.md)
```

#### Step 3: Create Supporting Scripts

```python
# scripts/deploy.py
#!/usr/bin/env python3
"""Production deployment script"""
import sys
import json
import argparse
from datetime import datetime

def deploy(version: str, environment: str, strategy: str = "blue-green"):
    """Deploy application with specified strategy"""
    start_time = datetime.now()

    try:
        # Deployment logic here
        # ... (kubectl apply, docker deploy, etc.)

        deployment_id = f"deploy-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        deployment_url = f"https://{environment}.example.com"

        # Return success
        result = {
            "success": True,
            "outputs": {
                "deployment_url": deployment_url,
                "deployment_id": deployment_id,
                "rollback_command": f"python scripts/rollback.py --deployment-id {deployment_id}"
            },
            "telemetry": {
                "command": "deploy",
                "version": version,
                "environment": environment,
                "strategy": strategy,
                "duration_ms": int((datetime.now() - start_time).total_seconds() * 1000),
                "timestamp": datetime.now().isoformat()
            },
            "errors": []
        }

        print(json.dumps(result, indent=2))
        return 0

    except Exception as e:
        # Return failure
        result = {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "deploy",
                "duration_ms": int((datetime.now() - start_time).total_seconds() * 1000),
                "timestamp": datetime.now().isoformat()
            },
            "errors": [f"deployment_failed: {str(e)}"]
        }
        print(json.dumps(result, indent=2), file=sys.stderr)
        return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--env", required=True)
    parser.add_argument("--strategy", default="blue-green")
    args = parser.parse_args()

    sys.exit(deploy(args.version, args.env, args.strategy))
```

#### Step 4: Use Custom Skill

```bash
# Execute custom deployment skill
/orchestrator *execute-skill deployment/deploy-production \
  --version=v1.2.3 \
  --environment=production \
  --dry-run=false
```

---

### Example 2: Custom Code Generation Skill

Create a skill that generates code from templates with AI assistance.

```markdown
---
name: generate-component
description: Generate React component with tests and stories
version: 1.0
category: development
complexity: standard
inputs:
  - name: component_name
    type: string
    required: true
  - name: component_type
    type: string
    required: false
    default: functional
    enum: [functional, class, custom-hook]
  - name: with_tests
    type: boolean
    default: true
  - name: with_storybook
    type: boolean
    default: true
outputs:
  - name: component_file
    type: string
  - name: test_file
    type: string
  - name: story_file
    type: string
---

# Skill: generate-component

## Workflow Steps

### 1. Generate Component File
**Command:** `python scripts/generate-component.py --name ${component_name} --type ${component_type}`
**Acceptance:** Component file created with proper structure

### 2. Generate Tests
**Condition:** `if ${with_tests}`
**Command:** `python scripts/generate-tests.py --component ${component_file}`
**Acceptance:** Test file created with coverage > 80%

### 3. Generate Storybook Story
**Condition:** `if ${with_storybook}`
**Command:** `python scripts/generate-story.py --component ${component_file}`
**Acceptance:** Story file created with all component states

### 4. Format Code
**Command:** `npm run format ${component_file} ${test_file} ${story_file}`
**Acceptance:** All files formatted according to style guide

### 5. Validate Component
**Command:** `npm run lint ${component_file} && npm test ${test_file}`
**Acceptance:** No lint errors, all tests pass
```

---

## Workflow Orchestration Patterns

### Pattern 1: Sequential Workflow

Execute steps one after another, stopping on failure.

```yaml
# .claude/workflows/sequential-review.yaml
name: Sequential Code Review
description: Thorough code review with multiple quality checks

steps:
  - name: lint
    subagent: james
    command: *lint
    args:
      path: src/
    on_failure: abort

  - name: type_check
    subagent: james
    command: *type-check
    args:
      path: src/
    on_failure: abort

  - name: test
    subagent: james
    command: *test
    args:
      scope: all
      coverage: true
    on_failure: abort

  - name: quality_review
    subagent: quinn
    command: *review-code
    args:
      path: src/
      focus: all
    on_failure: continue

  - name: quality_gate
    subagent: quinn
    command: *validate-quality-gate
    on_failure: warn

outputs:
  - name: review_report
    from: quality_review.outputs.report_path
  - name: quality_score
    from: quality_gate.outputs.score
```

**Usage:**
```bash
/orchestrator *workflow sequential-review
```

---

### Pattern 2: Parallel Workflow

Execute independent steps in parallel for speed.

```yaml
# .claude/workflows/parallel-analysis.yaml
name: Parallel Codebase Analysis
description: Run multiple analysis tasks concurrently

parallel_steps:
  - name: security_scan
    subagent: quinn
    command: *review-code
    args:
      path: .
      focus: security

  - name: architecture_analysis
    subagent: winston
    command: *analyze-architecture
    args:
      path: .
      depth: standard

  - name: dependency_audit
    subagent: james
    command: *audit-dependencies
    args:
      path: .

  - name: test_coverage
    subagent: james
    command: *test
    args:
      scope: all
      coverage: true

# After all parallel steps complete
sequential_steps:
  - name: aggregate_report
    command: python scripts/aggregate-reports.py
    args:
      reports:
        - ${security_scan.outputs.report}
        - ${architecture_analysis.outputs.report}
        - ${dependency_audit.outputs.report}
        - ${test_coverage.outputs.coverage_report}

outputs:
  - name: combined_report
    from: aggregate_report.outputs.report_path
```

**Usage:**
```bash
/orchestrator *workflow parallel-analysis
# Completes 4x faster than sequential
```

---

### Pattern 3: Conditional Workflow

Execute steps based on conditions.

```yaml
# .claude/workflows/conditional-deployment.yaml
name: Conditional Deployment
description: Deploy based on environment and test results

steps:
  - name: run_tests
    subagent: james
    command: *test
    args:
      scope: all
      coverage: true

  - name: check_coverage
    condition: ${run_tests.outputs.coverage_pct} >= 80
    command: echo "Coverage sufficient"
    on_failure: abort

  - name: deploy_staging
    condition: ${environment} == "staging"
    command: python scripts/deploy.py --env staging

  - name: deploy_production
    condition: ${environment} == "production" AND ${run_tests.success} == true
    subagent: orchestrator
    command: *execute-skill
    args:
      skill: deployment/deploy-production
      version: ${version}

  - name: notify_team
    condition: ${deploy_production.success} == true OR ${deploy_staging.success} == true
    command: python scripts/notify.py
    args:
      message: "Deployment to ${environment} successful"
```

**Usage:**
```bash
# Staging deployment
/orchestrator *workflow conditional-deployment --environment=staging --version=v1.2.3

# Production deployment (runs extra checks)
/orchestrator *workflow conditional-deployment --environment=production --version=v1.2.3
```

---

### Pattern 4: Loop Workflow

Iterate over items (e.g., multiple microservices).

```yaml
# .claude/workflows/multi-service-deploy.yaml
name: Multi-Service Deployment
description: Deploy multiple microservices in order

variables:
  services:
    - name: auth-service
      port: 3001
      dependencies: []
    - name: user-service
      port: 3002
      dependencies: [auth-service]
    - name: api-gateway
      port: 3000
      dependencies: [auth-service, user-service]

loop:
  items: ${services}
  variable: service
  steps:
    - name: wait_for_dependencies
      condition: ${service.dependencies} != []
      command: python scripts/wait-for-services.py
      args:
        services: ${service.dependencies}

    - name: deploy_service
      command: python scripts/deploy-service.py
      args:
        name: ${service.name}
        port: ${service.port}

    - name: health_check
      command: curl http://localhost:${service.port}/health
      retry: 5
      retry_delay: 10

outputs:
  - name: deployed_services
    from: loop.completed_items
```

---

## Command Chaining & Pipelines

### Example 1: Feature Implementation Pipeline

Complete pipeline from requirements to deployment.

```bash
#!/bin/bash
# feature-pipeline.sh

set -e  # Exit on error

FEATURE_NAME=$1
REQUIREMENTS_FILE=$2

echo "🚀 Feature Implementation Pipeline: $FEATURE_NAME"

# Step 1: Create task specification
echo "📝 Step 1: Creating task specification..."
/alex *create-task-spec "$REQUIREMENTS_FILE" \
  --title "$FEATURE_NAME" \
  --complexity auto

TASK_SPEC=".claude/tasks/$(ls -t .claude/tasks/*.md | head -1)"
echo "✓ Task spec created: $TASK_SPEC"

# Step 2: Implement feature
echo "💻 Step 2: Implementing feature..."
/james *implement "$TASK_SPEC" --test-first

# Step 3: Run tests
echo "🧪 Step 3: Running tests..."
/james *test --scope=all --coverage
TEST_RESULT=$?

if [ $TEST_RESULT -ne 0 ]; then
  echo "❌ Tests failed, aborting pipeline"
  exit 1
fi

# Step 4: Quality review
echo "🔍 Step 4: Running quality review..."
/quinn *review-code src/ --focus=all

# Step 5: Quality gate
echo "🚦 Step 5: Validating quality gate..."
/quinn *validate-quality-gate
QUALITY_RESULT=$?

if [ $QUALITY_RESULT -ne 0 ]; then
  echo "⚠️  Quality gate failed, manual review required"
  # Continue but flag for review
fi

# Step 6: Architecture review
echo "🏗️  Step 6: Architecture review..."
/winston *review-architecture docs/architecture.md

# Step 7: Create PR
echo "📦 Step 7: Creating pull request..."
BRANCH_NAME="feature/$FEATURE_NAME"
git checkout -b "$BRANCH_NAME"
git add .
git commit -m "feat: Implement $FEATURE_NAME

Automated implementation via BMAD Enhanced pipeline.

Task spec: $TASK_SPEC
Test coverage: Passing
Quality gate: $([ $QUALITY_RESULT -eq 0 ] && echo 'Passed' || echo 'Manual review required')
"
git push origin "$BRANCH_NAME"

gh pr create \
  --title "feat: $FEATURE_NAME" \
  --body "$(cat <<EOF
## Feature Implementation

**Task Spec:** \`$TASK_SPEC\`
**Branch:** \`$BRANCH_NAME\`

### Pipeline Results
- ✅ Implementation complete
- ✅ Tests passing
- $([ $QUALITY_RESULT -eq 0 ] && echo '✅' || echo '⚠️') Quality gate $([ $QUALITY_RESULT -eq 0 ] && echo 'passed' || echo 'requires review')
- ✅ Architecture reviewed

### Next Steps
- [ ] Code review by team
- [ ] Manual testing
- [ ] Merge and deploy

🤖 Generated with [BMAD Enhanced](https://github.com/your-org/bmad-enhanced)
EOF
)"

PR_URL=$(gh pr view --json url -q .url)
echo "✅ Pipeline complete! PR created: $PR_URL"
```

**Usage:**
```bash
chmod +x scripts/feature-pipeline.sh
./scripts/feature-pipeline.sh "User Authentication" docs/requirements/auth-requirements.md
```

---

### Example 2: Data Pipeline for Analysis

```bash
#!/bin/bash
# analysis-pipeline.sh

# Parallel execution of multiple analyses
{
  /winston *analyze-architecture . --output json > arch-analysis.json &
  PID1=$!

  /quinn *review-code src/ --output json > code-review.json &
  PID2=$!

  /james *test --scope=all --coverage --output json > test-results.json &
  PID3=$!

  python scripts/analyze-tech-stack.py > tech-stack.json &
  PID4=$!
}

# Wait for all to complete
wait $PID1 $PID2 $PID3 $PID4

# Aggregate results
python scripts/aggregate-analysis.py \
  --arch arch-analysis.json \
  --review code-review.json \
  --tests test-results.json \
  --tech tech-stack.json \
  --output final-report.html

echo "📊 Analysis complete: final-report.html"
```

---

## Custom Subagent Development

### Example: Custom Database Migration Subagent

Create a specialized subagent for database operations.

#### Step 1: Define Subagent

```markdown
# .claude/agents/david-dba.md

---
name: david-dba
role: Database Administrator
description: Specialized subagent for database operations, migrations, and optimization
version: 1.0
skills:
  - create-migration
  - run-migration
  - rollback-migration
  - optimize-queries
  - backup-database
routing:
  keywords:
    - database
    - migration
    - schema
    - query
    - backup
  complexity_threshold: 50
---

# David (Database Administrator)

## Overview
David specializes in database operations including:
- Creating and running migrations
- Database backup and restore
- Query optimization
- Schema design
- Data integrity checks

## Skills

### 1. create-migration
**Description:** Create database migration from schema changes
**Usage:** `/david *create-migration --description "Add users table"`

### 2. run-migration
**Description:** Execute database migrations
**Usage:** `/david *run-migration --direction up --steps 1`

### 3. rollback-migration
**Description:** Rollback database migrations
**Usage:** `/david *rollback-migration --steps 1`

### 4. optimize-queries
**Description:** Analyze and optimize slow queries
**Usage:** `/david *optimize-queries --threshold 1000ms`

### 5. backup-database
**Description:** Create database backup
**Usage:** `/david *backup-database --env production`

## Routing Logic

David is routed when:
- User mentions database-related keywords
- Task involves schema changes
- Query optimization needed
- Backup/restore operations

## Example Workflows

### Complete Migration Workflow
```bash
# 1. Create migration
/david *create-migration --description "Add email verification"

# 2. Review migration
/quinn *review-code db/migrations/001_add_email_verification.sql

# 3. Test migration (dev)
/david *run-migration --env development

# 4. Run tests
/james *test --scope=integration

# 5. Deploy to production
/david *run-migration --env production --dry-run false
```
```

#### Step 2: Implement Skills

```bash
mkdir -p .claude/skills/database/create-migration
cat > .claude/skills/database/create-migration/SKILL.md << 'EOF'
---
name: create-migration
description: Generate database migration from schema changes
category: database
complexity: standard
inputs:
  - name: description
    type: string
    required: true
  - name: orm
    type: string
    default: sql
    enum: [sql, sequelize, prisma, typeorm]
outputs:
  - name: migration_file
    type: string
  - name: migration_id
    type: string
---

# Skill: create-migration

## Workflow Steps

### 1. Analyze Schema Changes
Detect schema differences between current and desired state

### 2. Generate Migration
Create migration file with up/down functions

### 3. Validate Migration
Check for common issues (missing indexes, foreign keys, etc.)

### 4. Generate Tests
Create migration tests

EOF
```

#### Step 3: Register Subagent

```yaml
# .claude/config.yaml
subagents:
  david:
    enabled: true
    agent_file: .claude/agents/david-dba.md
    skills:
      - database/*
    routing:
      keywords: [database, migration, schema, sql]
      auto_route: true
```

---

## Integration with External Tools

### Example 1: Jira Integration

Automatically create Jira tickets from task specs.

```python
# scripts/integrations/jira-sync.py
#!/usr/bin/env python3
"""Sync BMAD tasks with Jira"""

import os
import yaml
from jira import JIRA

def sync_task_to_jira(task_spec_path):
    """Create Jira ticket from task spec"""

    # Read task spec
    with open(task_spec_path) as f:
        content = f.read()

    # Parse YAML frontmatter
    import re
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        frontmatter = yaml.safe_load(match.group(1))
        body = match.group(2)

    # Connect to Jira
    jira = JIRA(
        server=os.getenv('JIRA_SERVER'),
        basic_auth=(os.getenv('JIRA_USER'), os.getenv('JIRA_TOKEN'))
    )

    # Create issue
    issue = jira.create_issue(
        project='PROJ',
        summary=frontmatter['title'],
        description=body,
        issuetype={'name': 'Story'},
        labels=['bmad-enhanced', 'automated'],
        customfield_10001=frontmatter.get('complexity', 'medium'),  # Story points
        customfield_10002=frontmatter.get('estimated_hours', 0)     # Time estimate
    )

    print(f"Created Jira ticket: {issue.key}")
    print(f"URL: {jira_server}/browse/{issue.key}")

    # Update task spec with Jira link
    with open(task_spec_path, 'a') as f:
        f.write(f"\n\n**Jira Ticket:** [{issue.key}]({jira_server}/browse/{issue.key})\n")

    return issue.key

if __name__ == "__main__":
    import sys
    task_spec = sys.argv[1]
    sync_task_to_jira(task_spec)
```

**Usage in Workflow:**
```bash
# After creating task spec
/alex *create-task-spec requirements.md
python scripts/integrations/jira-sync.py .claude/tasks/task-001-spec.md
```

---

### Example 2: Slack Notifications

Send workflow updates to Slack.

```python
# scripts/integrations/slack-notify.py
#!/usr/bin/env python3
"""Send BMAD workflow notifications to Slack"""

import os
import json
import requests

def send_slack_notification(message, channel="#engineering", level="info"):
    """Send notification to Slack"""

    webhook_url = os.getenv('SLACK_WEBHOOK_URL')

    # Color based on level
    colors = {
        "info": "#36a64f",      # Green
        "warning": "#ff9900",   # Orange
        "error": "#ff0000",     # Red
        "success": "#00ff00"    # Bright green
    }

    payload = {
        "channel": channel,
        "attachments": [{
            "color": colors.get(level, "#36a64f"),
            "text": message,
            "footer": "BMAD Enhanced",
            "ts": int(time.time())
        }]
    }

    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200

# Example usage
send_slack_notification(
    "✅ Feature implementation complete: User Authentication\n"
    "📊 Quality Score: 87/100\n"
    "🧪 Test Coverage: 92%\n"
    "📝 PR: https://github.com/org/repo/pull/123",
    level="success"
)
```

**Integration in Pipeline:**
```bash
# Add to feature-pipeline.sh
python scripts/integrations/slack-notify.py \
  --message "Feature '$FEATURE_NAME' implemented" \
  --level success \
  --channel "#deployments"
```

---

### Example 3: GitHub Actions Integration

```yaml
# .github/workflows/bmad-enhanced.yml
name: BMAD Enhanced Workflow

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  bmad-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install BMAD Enhanced
        run: |
          pip install -r requirements.txt

      - name: Run Code Review
        run: |
          /quinn *review-code . --output json > review.json

      - name: Run Quality Gate
        run: |
          /quinn *validate-quality-gate --output json > quality-gate.json

      - name: Post Comment to PR
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json'));
            const qualityGate = JSON.parse(fs.readFileSync('quality-gate.json'));

            const comment = `
            ## BMAD Enhanced Review

            **Quality Score:** ${qualityGate.outputs.score}/100
            **Decision:** ${qualityGate.outputs.decision}

            ### Issues Found
            ${review.outputs.issues.map(i => `- ${i.severity}: ${i.message}`).join('\n')}

            ### Recommendations
            ${review.outputs.recommendations.join('\n- ')}
            `;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

---

## Advanced Templating

### Dynamic Template Generation

```python
# scripts/generate-template.py
#!/usr/bin/env python3
"""Generate custom templates based on project structure"""

import os
import json
from pathlib import Path
from jinja2 import Template

def generate_task_spec_template(project_info):
    """Generate task spec template customized for project"""

    template_str = """---
task_id: {{ task_id }}
title: {{ title }}
status: ready
priority: {{ priority }}
complexity: {{ complexity }}
estimated_hours: {{ estimated_hours }}
project: {{ project_name }}
team: {{ team }}
---

# Task: {{ title }}

## Context
{{ context }}

## Requirements
{% for req in requirements %}
- {{ req }}
{% endfor %}

## Acceptance Criteria
{% for criterion in acceptance_criteria %}
- [ ] {{ criterion }}
{% endfor %}

## Technical Approach

### Architecture
{{ architecture_notes }}

### Files to Modify
{% for file in files %}
- \`{{ file }}\`
{% endfor %}

### Dependencies
{% for dep in dependencies %}
- {{ dep }}
{% endfor %}

## Testing Strategy
- Unit tests: {{ unit_test_approach }}
- Integration tests: {{ integration_test_approach }}
- E2E tests: {{ e2e_test_approach }}

## Risks
{% for risk in risks %}
- **{{ risk.severity }}**: {{ risk.description }}
  - *Mitigation*: {{ risk.mitigation }}
{% endfor %}

## Related Tasks
{% for related in related_tasks %}
- {{ related }}
{% endfor %}
"""

    template = Template(template_str)
    return template.render(**project_info)

# Example usage
project_info = {
    "task_id": "PROJ-123",
    "title": "Add User Authentication",
    "priority": "high",
    "complexity": "medium",
    "estimated_hours": 8,
    "project_name": "Web Application",
    "team": "Backend Team",
    "context": "Users need to authenticate before accessing protected resources",
    "requirements": [
        "JWT-based authentication",
        "Password hashing with bcrypt",
        "Token refresh mechanism"
    ],
    "acceptance_criteria": [
        "Users can login with email/password",
        "Tokens expire after 24 hours",
        "Password reset flow implemented"
    ],
    "architecture_notes": "Use Express middleware for auth, Redis for token storage",
    "files": [
        "src/api/auth.js",
        "src/middleware/authenticate.js",
        "src/models/User.js"
    ],
    "dependencies": [
        "jsonwebtoken@9.0.0",
        "bcrypt@5.1.0",
        "redis@4.5.0"
    ],
    "unit_test_approach": "Test auth functions in isolation",
    "integration_test_approach": "Test login flow end-to-end",
    "e2e_test_approach": "Test complete user journey",
    "risks": [
        {
            "severity": "High",
            "description": "Security vulnerabilities in auth flow",
            "mitigation": "Security review by senior engineer"
        }
    ],
    "related_tasks": ["PROJ-122: Setup database", "PROJ-124: Add user profile"]
}

output = generate_task_spec_template(project_info)
print(output)
```

---

## Workflow State Management

### Stateful Workflow with Checkpoints

```python
# scripts/stateful-workflow.py
#!/usr/bin/env python3
"""Stateful workflow with checkpoint/resume capability"""

import json
import pickle
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class WorkflowState:
    """Workflow state"""
    workflow_id: str
    current_step: int
    total_steps: int
    completed_steps: List[int]
    step_outputs: Dict[int, Any]
    variables: Dict[str, Any]
    status: str  # running, paused, completed, failed

class StatefulWorkflow:
    """Workflow with state management"""

    def __init__(self, workflow_id: str, state_file: str = None):
        self.workflow_id = workflow_id
        self.state_file = state_file or f".claude/workflows/state/{workflow_id}.pkl"
        self.state = self.load_state() or WorkflowState(
            workflow_id=workflow_id,
            current_step=0,
            total_steps=0,
            completed_steps=[],
            step_outputs={},
            variables={},
            status="initialized"
        )

    def load_state(self):
        """Load workflow state from disk"""
        if Path(self.state_file).exists():
            with open(self.state_file, 'rb') as f:
                return pickle.load(f)
        return None

    def save_state(self):
        """Save workflow state to disk"""
        Path(self.state_file).parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'wb') as f:
            pickle.dump(self.state, f)

    def execute_step(self, step_func, *args, **kwargs):
        """Execute workflow step with checkpointing"""
        self.state.current_step += 1
        self.state.status = "running"
        self.save_state()  # Checkpoint before execution

        try:
            result = step_func(*args, **kwargs)
            self.state.completed_steps.append(self.state.current_step)
            self.state.step_outputs[self.state.current_step] = result
            self.save_state()  # Checkpoint after success
            return result

        except Exception as e:
            self.state.status = "failed"
            self.save_state()
            raise

    def resume(self):
        """Resume workflow from last checkpoint"""
        return self.state.current_step, self.state.step_outputs

    def complete(self):
        """Mark workflow as complete"""
        self.state.status = "completed"
        self.save_state()

# Example usage
workflow = StatefulWorkflow("feature-impl-001")

# Define steps
def step1_create_spec():
    print("Creating task spec...")
    return {"spec_file": "task-001.md"}

def step2_implement():
    print("Implementing feature...")
    return {"implementation": "complete"}

def step3_test():
    print("Running tests...")
    return {"tests": "passed", "coverage": 95}

# Execute workflow (can be interrupted and resumed)
try:
    result1 = workflow.execute_step(step1_create_spec)
    result2 = workflow.execute_step(step2_implement)
    result3 = workflow.execute_step(step3_test)
    workflow.complete()
except KeyboardInterrupt:
    print("Workflow paused. Run with --resume to continue.")

# Resume workflow
if args.resume:
    last_step, outputs = workflow.resume()
    print(f"Resuming from step {last_step}")
    # Continue from last step...
```

---

## Real-World Examples

### Example 1: Complete Microservice Implementation

```bash
#!/bin/bash
# microservice-implementation.sh

SERVICE_NAME=$1
API_SPEC=$2

echo "🚀 Implementing Microservice: $SERVICE_NAME"

# 1. Architecture Design
echo "🏗️  Step 1: Designing architecture..."
/winston *design-architecture "$API_SPEC" \
  --type backend \
  --complexity medium \
  --output docs/architecture/$SERVICE_NAME-architecture.md

# 2. Create Task Specs for Each Component
echo "📝 Step 2: Breaking down into tasks..."
/alex *breakdown-epic docs/architecture/$SERVICE_NAME-architecture.md

# 3. Implement Each Component
for task in .claude/tasks/$SERVICE_NAME-*.md; do
  echo "💻 Implementing: $task"
  /james *implement "$task" --test-first

  echo "🧪 Testing: $task"
  /james *test --scope=unit

  echo "🔍 Reviewing: $task"
  /quinn *review-code --changed-only
done

# 4. Integration Testing
echo "🔗 Step 4: Integration testing..."
/james *test --scope=integration

# 5. Quality Gate
echo "🚦 Step 5: Quality validation..."
/quinn *validate-quality-gate

# 6. Architecture Review
echo "🏛️  Step 6: Architecture review..."
/winston *review-architecture docs/architecture/$SERVICE_NAME-architecture.md

# 7. Documentation
echo "📚 Step 7: Generating documentation..."
/orchestrator *workflow document-codebase . --depth comprehensive

# 8. Deployment Preparation
echo "📦 Step 8: Preparing deployment..."
python scripts/build-docker-image.py --service $SERVICE_NAME

# 9. Deploy to Staging
echo "🚢 Step 9: Deploying to staging..."
/orchestrator *execute-skill deployment/deploy-production \
  --version latest \
  --environment staging

echo "✅ Microservice implementation complete!"
echo "📊 Next steps:"
echo "  1. Manual testing in staging"
echo "  2. Performance testing"
echo "  3. Security review"
echo "  4. Deploy to production"
```

---

### Example 2: Automated Release Process

```bash
#!/bin/bash
# automated-release.sh

VERSION=$1
RELEASE_NOTES=$2

echo "🎉 Automated Release Process: v$VERSION"

# 1. Verify Clean State
git diff-index --quiet HEAD || {
  echo "❌ Working directory not clean"
  exit 1
}

# 2. Run Full Test Suite
echo "🧪 Running full test suite..."
/james *test --scope=all --coverage
TEST_EXIT=$?

if [ $TEST_EXIT -ne 0 ]; then
  echo "❌ Tests failed, aborting release"
  exit 1
fi

# 3. Quality Gate
echo "🚦 Validating quality gate..."
/quinn *validate-quality-gate --strict
QUALITY_EXIT=$?

if [ $QUALITY_EXIT -ne 0 ]; then
  echo "❌ Quality gate failed, aborting release"
  exit 1
fi

# 4. Architecture Review
echo "🏗️  Architecture review..."
/winston *review-architecture docs/architecture.md --depth comprehensive

# 5. Security Scan
echo "🔒 Security scan..."
/quinn *review-code . --focus security --depth thorough

# 6. Update Version
echo "📝 Updating version..."
npm version $VERSION --no-git-tag-version
git add package.json package-lock.json
git commit -m "chore: Bump version to $VERSION"

# 7. Generate Changelog
echo "📋 Generating changelog..."
python scripts/generate-changelog.py --version $VERSION > CHANGELOG-$VERSION.md

# 8. Create Git Tag
git tag -a "v$VERSION" -m "Release v$VERSION

$(cat CHANGELOG-$VERSION.md)
"

# 9. Build Release Artifacts
echo "🏗️  Building release artifacts..."
npm run build
python scripts/package-release.py --version $VERSION

# 10. Deploy to Production
echo "🚀 Deploying to production..."
/orchestrator *execute-skill deployment/deploy-production \
  --version v$VERSION \
  --environment production

# 11. Push to GitHub
git push origin main
git push origin "v$VERSION"

# 12. Create GitHub Release
gh release create "v$VERSION" \
  --title "Release v$VERSION" \
  --notes-file CHANGELOG-$VERSION.md \
  dist/*

# 13. Notify Team
python scripts/integrations/slack-notify.py \
  --message "🎉 Release v$VERSION deployed to production!" \
  --level success \
  --channel "#releases"

echo "✅ Release v$VERSION complete!"
```

---

## Best Practices

### 1. Always Add Error Handling
```bash
set -e  # Exit on error
set -u  # Error on undefined variable
set -o pipefail  # Pipe failures fail the whole chain
```

### 2. Use Telemetry
```python
# Always include telemetry
result = {
    "success": True,
    "telemetry": {
        "command": "custom-command",
        "duration_ms": elapsed,
        "timestamp": datetime.now().isoformat()
    }
}
```

### 3. Document Everything
- Add README to custom skills
- Include usage examples
- Document prerequisites
- Explain error handling

### 4. Test Workflows
```bash
# Dry-run mode
/orchestrator *workflow my-workflow --dry-run

# Test in non-production environment first
/orchestrator *workflow deploy --environment staging
```

### 5. Version Control Workflows
```bash
git add .claude/workflows/
git commit -m "feat: Add custom deployment workflow"
```

---

## Related Documentation

- [V2-ARCHITECTURE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md) - System architecture
- [EXAMPLE-WORKFLOWS.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/EXAMPLE-WORKFLOWS.md) - Example workflows
- [WORKFLOW-GUIDE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/WORKFLOW-GUIDE.md) - Workflow guide
- [BEST-PRACTICES.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/BEST-PRACTICES.md) - Best practices

---

**Maintained by:** BMAD Enhanced Development Team
**Last Updated:** 2025-11-05
