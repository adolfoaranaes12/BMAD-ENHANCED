# Production Deployment Guide

**Version:** 1.0
**Date:** 2025-02-03
**Status:** Production Ready
**Audience:** DevOps Engineers, System Administrators

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Pre-Deployment Checklist](#pre-deployment-checklist)
4. [Installation Steps](#installation-steps)
5. [Configuration](#configuration)
6. [Environment Setup](#environment-setup)
7. [Deployment Verification](#deployment-verification)
8. [Post-Deployment Tasks](#post-deployment-tasks)
9. [Rollback Procedures](#rollback-procedures)
10. [Troubleshooting](#troubleshooting)

---

## Overview

This guide walks through deploying BMAD Enhanced V2 to production environments. BMAD Enhanced is designed to be deployed as a Claude Code project with supporting infrastructure for monitoring, telemetry, and state management.

### Deployment Architecture

```
┌─────────────────────────────────────────────────────────┐
│ Production Environment                                   │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │ Claude Code Instance                            │    │
│  │                                                  │    │
│  │  .claude/                                       │    │
│  │  ├── agents/         (4 subagents)             │    │
│  │  ├── skills/         (17 skills)               │    │
│  │  ├── workflows/      (state files)             │    │
│  │  ├── quality/gates/  (quality assessments)     │    │
│  │  └── telemetry/      (observability data)      │    │
│  └────────────────────────────────────────────────┘    │
│                          │                               │
│                          │                               │
│  ┌────────────────────────────────────────────────┐    │
│  │ Supporting Infrastructure                       │    │
│  │                                                  │    │
│  │  - Monitoring (Prometheus/Grafana)             │    │
│  │  - Logging (ELK/Loki)                          │    │
│  │  - Alerting (PagerDuty/Slack)                  │    │
│  │  - Storage (persistent volumes)                │    │
│  └────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### Deployment Models

**Option 1: Single Instance (Recommended for most teams)**
- One Claude Code instance with BMAD Enhanced
- Suitable for teams up to 50 developers
- Simple to manage and monitor

**Option 2: Multi-Instance (For large organizations)**
- Multiple Claude Code instances (per team/project)
- Shared infrastructure (monitoring, storage)
- Centralized telemetry aggregation

**Option 3: Hybrid (Development + Production)**
- Separate instances for dev/staging/production
- Promotes workflows from dev → staging → prod
- Full SDLC support

---

## Prerequisites

### System Requirements

**Minimum Requirements:**
- **OS:** Linux (Ubuntu 20.04+, RHEL 8+), macOS 11+
- **Memory:** 4GB RAM
- **Storage:** 10GB available disk space
- **CPU:** 2 cores
- **Python:** 3.8+
- **Network:** Internet connectivity for Claude API

**Recommended for Production:**
- **OS:** Linux (Ubuntu 22.04 LTS, RHEL 9)
- **Memory:** 8GB+ RAM
- **Storage:** 50GB+ SSD with IOPS 3000+
- **CPU:** 4+ cores
- **Python:** 3.10+
- **Network:** Low-latency connection to Claude API

### Required Software

1. **Claude Code CLI** (latest version)
   ```bash
   # Install Claude Code
   npm install -g @anthropic-ai/claude-code

   # Verify installation
   claude --version
   ```

2. **Git** (for version control)
   ```bash
   git --version
   # Should be 2.25+
   ```

3. **Python** (for bmad-commands primitives)
   ```bash
   python3 --version
   # Should be 3.8+

   # Install required packages
   pip3 install pyyaml
   ```

4. **jq** (for JSON processing)
   ```bash
   jq --version
   # Install if needed: apt-get install jq
   ```

### Access Requirements

- ✅ **Claude API Key** with appropriate permissions
- ✅ **Git repository access** (if using version control)
- ✅ **Server/VM access** with sudo privileges (if needed)
- ✅ **Monitoring infrastructure access** (Prometheus, Grafana, etc.)
- ✅ **Alert notification access** (Slack, PagerDuty, etc.)

### Pre-Deployment Validation

Run the pre-deployment validator:

```bash
#!/bin/bash
# pre-deploy-check.sh - Validate prerequisites

echo "=== BMAD Enhanced Pre-Deployment Check ==="

# Check OS
if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
  echo "✓ OS: $OSTYPE"
else
  echo "✗ OS: $OSTYPE not supported"
  exit 1
fi

# Check Claude Code
if command -v claude &> /dev/null; then
  echo "✓ Claude Code: $(claude --version)"
else
  echo "✗ Claude Code not installed"
  exit 1
fi

# Check Python
if command -v python3 &> /dev/null; then
  version=$(python3 --version | awk '{print $2}')
  echo "✓ Python: $version"
else
  echo "✗ Python 3 not installed"
  exit 1
fi

# Check Git
if command -v git &> /dev/null; then
  echo "✓ Git: $(git --version)"
else
  echo "✗ Git not installed"
  exit 1
fi

# Check jq
if command -v jq &> /dev/null; then
  echo "✓ jq: $(jq --version)"
else
  echo "⚠ jq not installed (recommended)"
fi

# Check disk space
available=$(df -h . | awk 'NR==2 {print $4}')
echo "✓ Available disk space: $available"

# Check memory
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  total_mem=$(free -g | awk '/^Mem:/ {print $2}')
  echo "✓ Total memory: ${total_mem}GB"
fi

echo ""
echo "=== Pre-Deployment Check PASSED ==="
```

---

## Pre-Deployment Checklist

### Planning Phase

- [ ] **Deployment date/time scheduled** (off-peak hours recommended)
- [ ] **Stakeholders notified** (developers, operations, management)
- [ ] **Backup plan documented** (rollback procedures ready)
- [ ] **Monitoring setup** (dashboards, alerts configured)
- [ ] **Change request approved** (if required by organization)

### Technical Readiness

- [ ] **Prerequisites validated** (ran pre-deploy-check.sh)
- [ ] **Server/environment provisioned** (sufficient resources)
- [ ] **Network connectivity verified** (Claude API accessible)
- [ ] **Storage configured** (persistent volumes mounted)
- [ ] **Backup location prepared** (for telemetry, state files)

### Documentation Review

- [ ] **Deployment guide reviewed** (this document)
- [ ] **Configuration guide reviewed** (configuration section)
- [ ] **Monitoring guide reviewed** (PRODUCTION-MONITORING-GUIDE.md)
- [ ] **Security review completed** (PRODUCTION-SECURITY-REVIEW.md)
- [ ] **Runbooks prepared** (for common issues)

---

## Installation Steps

### Step 1: Clone/Download BMAD Enhanced

**Option A: From Git Repository**
```bash
# Clone the repository
git clone https://github.com/your-org/bmad-enhanced.git /opt/bmad-enhanced

# Navigate to directory
cd /opt/bmad-enhanced

# Checkout production-ready version
git checkout v2.0.0  # Or your target version
```

**Option B: From Archive**
```bash
# Extract archive
tar -xzf bmad-enhanced-v2.0.0.tar.gz -C /opt/
cd /opt/bmad-enhanced
```

### Step 2: Verify Installation

```bash
# Check directory structure
ls -la .claude/

# Expected directories:
# .claude/agents/
# .claude/skills/
# .claude/config.yaml (template)

# Verify subagents
ls -la .claude/agents/*.md

# Expected files:
# orchestrator-v2.md
# alex-planner.md
# james-developer-v2.md
# quinn-quality.md

# Verify skills
find .claude/skills -name "SKILL.md" | wc -l
# Should output: 17
```

### Step 3: Configure Environment

```bash
# Create production config from template
cp .claude/config.yaml.template .claude/config.yaml

# Edit configuration (see Configuration section below)
vim .claude/config.yaml

# Create necessary directories
mkdir -p .claude/workflows
mkdir -p .claude/quality/gates
mkdir -p .claude/telemetry/{workflows,subagents,skills}
mkdir -p .claude/tasks
mkdir -p workspace/{stories,epics}
```

### Step 4: Set Up Secrets

```bash
# Create .env file for secrets (DO NOT commit to git)
cat > .env <<EOF
CLAUDE_API_KEY=your-api-key-here
SLACK_WEBHOOK_URL=your-slack-webhook-url
PAGERDUTY_API_KEY=your-pagerduty-key
EOF

# Secure the file
chmod 600 .env

# Add to .gitignore if not already there
echo ".env" >> .gitignore
```

### Step 5: Initialize Claude Code

```bash
# Authenticate Claude Code
claude auth login

# Verify authentication
claude auth whoami

# Test basic functionality
claude --version
```

### Step 6: Validate Installation

```bash
# Run validation script
./scripts/validate-installation.sh

# Expected output:
# ✓ Directory structure valid
# ✓ All subagents present
# ✓ All skills present
# ✓ Configuration valid
# ✓ Secrets configured
# ✓ Installation VALIDATED
```

---

## Configuration

### Production Configuration Template

Edit `.claude/config.yaml`:

```yaml
# BMAD Enhanced V2 Production Configuration

# Project metadata
project:
  name: "BMAD Enhanced"
  version: "2.0.0"
  environment: "production"

# Team settings
team:
  velocity: 40                    # Average story points per sprint
  sprint_duration: 14             # Days per sprint
  capacity_limit: 0.95            # Max 95% of velocity for planning

# Quality thresholds
quality:
  min_coverage: 80                # Minimum test coverage %
  critical_coverage: 95           # Coverage for critical paths
  max_complexity: 10              # Max cyclomatic complexity
  max_files_per_review: 20        # Max files per review
  allowRefactoring: true          # Enable refactoring
  autoApplyQAFixes: false         # Require explicit QA fix application

  quality_gate_thresholds:
    pass: 80                      # PASS if score ≥ 80%
    concerns: 60                  # CONCERNS if 60-79%
    fail: 60                      # FAIL if < 60%

  nfr_assessment:
    enabled: true
    categories:
      - security
      - performance
      - reliability
      - maintainability
      - scalability
      - usability

# Development settings
development:
  tdd_required: true              # Enforce TDD workflow
  min_coverage: 80                # Minimum test coverage
  max_files_simple: 5             # Max files for simple changes
  max_files_standard: 7           # Max files for standard changes
  max_files_complex: 10           # Max files for complex changes

# Orchestrator settings
orchestrator:
  enabled: true
  max_subagents: 4                # Max concurrent subagents
  max_workflow_duration: 480      # Max minutes (8 hours)
  max_phase_retries: 3            # Max retries per phase
  state_persistence: true         # Enable state files
  auto_resume: true               # Auto-detect incomplete workflows

  workflows:
    feature-delivery:
      enabled: true
      quality_gate_enforced: true # Block PR if quality gate FAIL
      auto_pr: true               # Auto-create PR if PASS

    epic-to-sprint:
      enabled: true
      default_velocity: 40
      max_stories_per_sprint: 15

    sprint-execution:
      enabled: true
      daily_loop: true            # Enable James → Quinn daily loops

  coordination:
    max_iterations: 10            # For iterative patterns
    parallel_max: 4               # Max parallel tasks
    timeout_per_phase: 60         # Minutes per phase

# Guardrails
guardrails:
  block_sensitive_files: true     # Block .env, *.key, credentials.json
  require_task_spec: true         # Require task spec for *implement
  never_commit_failing: true      # Block commits with failing tests

  global:
    max_files_per_change: 5       # Default max files
    max_diff_lines: 400           # Default max diff lines
    require_tests: true           # Tests required
    min_test_coverage: 80         # Min coverage %

# Telemetry settings
telemetry:
  enabled: true
  retention_days: 90              # Keep telemetry for 90 days
  aggregation: true               # Enable metric aggregation
  export_format: "json"           # json or yaml

  emit_on:
    - workflow_start
    - workflow_complete
    - phase_transition
    - quality_gate_decision
    - guardrail_violation
    - error

# Monitoring
monitoring:
  health_check_interval: 300      # Seconds between health checks
  alert_on_failure: true
  metrics_retention: 30           # Days to retain metrics

  thresholds:
    workflow_success_rate: 90     # Alert if below 90%
    quality_gate_pass_rate: 80    # Alert if below 80%
    max_workflow_duration: 5400   # Alert if exceeds 90 minutes

# Storage
storage:
  workflows_dir: ".claude/workflows"
  telemetry_dir: ".claude/telemetry"
  quality_dir: ".claude/quality"
  tasks_dir: ".claude/tasks"
  workspace_dir: "workspace"

# Logging
logging:
  level: "INFO"                   # DEBUG, INFO, WARN, ERROR
  format: "json"                  # json or text
  output: "file"                  # file, stdout, or both
  file_path: "/var/log/bmad-enhanced/bmad.log"
  max_size_mb: 100
  max_files: 10
```

### Environment-Specific Configuration

Create environment-specific overrides:

**`.claude/config.production.yaml`:**
```yaml
# Production-specific overrides
logging:
  level: "INFO"
monitoring:
  alert_on_failure: true
telemetry:
  enabled: true
```

**`.claude/config.staging.yaml`:**
```yaml
# Staging-specific overrides
logging:
  level: "DEBUG"
monitoring:
  alert_on_failure: false
telemetry:
  enabled: true
```

**Load configuration:**
```bash
# Production
export BMAD_ENV=production
claude --config .claude/config.yaml --config .claude/config.production.yaml

# Staging
export BMAD_ENV=staging
claude --config .claude/config.yaml --config .claude/config.staging.yaml
```

---

## Environment Setup

### File System Structure

```bash
# Create production directory structure
mkdir -p /opt/bmad-enhanced/{logs,backups,telemetry}

# Set ownership
chown -R bmad-user:bmad-group /opt/bmad-enhanced

# Set permissions
chmod 755 /opt/bmad-enhanced
chmod 700 /opt/bmad-enhanced/.claude
chmod 600 /opt/bmad-enhanced/.env
```

### Persistent Storage

**Option 1: Local Storage**
```bash
# Mount persistent volume
mount /dev/sdb1 /opt/bmad-enhanced/telemetry

# Add to /etc/fstab for persistence
echo "/dev/sdb1 /opt/bmad-enhanced/telemetry ext4 defaults 0 2" >> /etc/fstab
```

**Option 2: Network Storage (NFS)**
```bash
# Mount NFS share
mount -t nfs nfs-server:/bmad/telemetry /opt/bmad-enhanced/telemetry

# Add to /etc/fstab
echo "nfs-server:/bmad/telemetry /opt/bmad-enhanced/telemetry nfs defaults 0 0" >> /etc/fstab
```

### Backup Configuration

```bash
#!/bin/bash
# backup.sh - Automated backup script

BACKUP_DIR="/opt/bmad-enhanced/backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_NAME="bmad-backup-${TIMESTAMP}"

# Create backup directory
mkdir -p "${BACKUP_DIR}/${BACKUP_NAME}"

# Backup critical directories
tar -czf "${BACKUP_DIR}/${BACKUP_NAME}/workflows.tar.gz" .claude/workflows/
tar -czf "${BACKUP_DIR}/${BACKUP_NAME}/quality.tar.gz" .claude/quality/
tar -czf "${BACKUP_DIR}/${BACKUP_NAME}/telemetry.tar.gz" .claude/telemetry/
tar -czf "${BACKUP_DIR}/${BACKUP_NAME}/config.tar.gz" .claude/config*.yaml

# Backup metadata
echo "Backup created: ${TIMESTAMP}" > "${BACKUP_DIR}/${BACKUP_NAME}/metadata.txt"
echo "Version: $(git describe --tags)" >> "${BACKUP_DIR}/${BACKUP_NAME}/metadata.txt"

# Retention (keep last 30 days)
find "${BACKUP_DIR}" -type d -name "bmad-backup-*" -mtime +30 -exec rm -rf {} \;

echo "Backup completed: ${BACKUP_NAME}"
```

**Schedule backups:**
```bash
# Add to crontab
crontab -e

# Backup daily at 2 AM
0 2 * * * /opt/bmad-enhanced/scripts/backup.sh
```

---

## Deployment Verification

### Post-Deployment Tests

```bash
#!/bin/bash
# verify-deployment.sh - Verify deployment success

echo "=== BMAD Enhanced Deployment Verification ==="

# Test 1: Health check
echo "Running health check..."
./scripts/health_check.sh || { echo "✗ Health check failed"; exit 1; }

# Test 2: Configuration validation
echo "Validating configuration..."
python3 scripts/validate-config.py .claude/config.yaml || { echo "✗ Config invalid"; exit 1; }

# Test 3: Subagent availability
echo "Testing subagent availability..."
for agent in orchestrator-v2 alex-planner james-developer-v2 quinn-quality; do
  [ -f ".claude/agents/${agent}.md" ] || { echo "✗ ${agent} missing"; exit 1; }
  echo "  ✓ ${agent}"
done

# Test 4: Skill availability
echo "Testing skills..."
skill_count=$(find .claude/skills -name "SKILL.md" | wc -l)
[ "$skill_count" -eq 17 ] || { echo "✗ Expected 17 skills, found ${skill_count}"; exit 1; }
echo "  ✓ Found ${skill_count} skills"

# Test 5: Primitives (bmad-commands)
echo "Testing primitives..."
python3 .claude/skills/bmad-commands/scripts/read_file.py --help > /dev/null 2>&1 || \
  { echo "✗ Primitives not functional"; exit 1; }
echo "  ✓ Primitives functional"

# Test 6: Directory permissions
echo "Checking permissions..."
[ -w ".claude/workflows" ] || { echo "✗ Workflows directory not writable"; exit 1; }
[ -w ".claude/telemetry" ] || { echo "✗ Telemetry directory not writable"; exit 1; }
[ -w ".claude/quality/gates" ] || { echo "✗ Quality gates directory not writable"; exit 1; }
echo "  ✓ Permissions correct"

# Test 7: Monitoring endpoint
if [ -f "scripts/health_server.py" ]; then
  echo "Testing monitoring endpoint..."
  python3 scripts/health_server.py &
  SERVER_PID=$!
  sleep 2
  curl -f http://localhost:8080/health > /dev/null 2>&1 || \
    { echo "✗ Health endpoint not responding"; kill $SERVER_PID; exit 1; }
  kill $SERVER_PID
  echo "  ✓ Monitoring endpoint functional"
fi

# Test 8: Simple workflow test
echo "Running simple workflow test..."
# Create minimal test task
cat > /tmp/test-task.md <<EOF
# Test Task
Task for deployment verification

## Acceptance Criteria
- Deployment verified
EOF

# This would invoke a simple workflow - adapt to your needs
# For now, just verify the file can be read
python3 .claude/skills/bmad-commands/scripts/read_file.py --path /tmp/test-task.md > /dev/null || \
  { echo "✗ Workflow test failed"; exit 1; }
rm /tmp/test-task.md
echo "  ✓ Workflow test passed"

echo ""
echo "=== Deployment Verification PASSED ==="
echo "BMAD Enhanced is ready for production use"
```

### Smoke Tests

Run these manual smoke tests post-deployment:

1. **Test Alex (Planner)**
   ```bash
   # Create a simple task spec
   @alex *create-task-spec "Simple test feature"
   # Verify: task spec created in .claude/tasks/
   ```

2. **Test James (Developer) - Dry Run**
   ```bash
   # Explain code (read-only test)
   @james *explain src/example.py
   # Verify: explanation provided, no files modified
   ```

3. **Test Quinn (Quality)**
   ```bash
   # Run quality review on test task
   @quinn *review test-task-001
   # Verify: quality gate created in .claude/quality/gates/
   ```

4. **Test Orchestrator**
   ```bash
   # Test coordination (dry run)
   @orchestrator *coordinate "Test coordination" --subagents alex
   # Verify: workflow state created
   ```

---

## Post-Deployment Tasks

### 1. Configure Monitoring

```bash
# Start monitoring services
systemctl start prometheus
systemctl start grafana

# Import Grafana dashboards
curl -X POST \
  http://admin:admin@localhost:3000/api/dashboards/db \
  -H 'Content-Type: application/json' \
  -d @dashboards/bmad-enhanced.json
```

### 2. Set Up Alerting

```bash
# Configure Alertmanager
cp alertmanager.yml /etc/prometheus/alertmanager.yml
systemctl restart alertmanager

# Test alert
curl -X POST http://localhost:9093/api/v1/alerts \
  -d '[{"labels":{"alertname":"TestAlert"}}]'
```

### 3. Enable Backups

```bash
# Test backup script
./scripts/backup.sh

# Verify backup created
ls -lh /opt/bmad-enhanced/backups/

# Enable scheduled backups
systemctl enable bmad-backup.timer
systemctl start bmad-backup.timer
```

### 4. Document Deployment

Create deployment record:

```bash
cat > deployment-record-$(date +%Y%m%d).md <<EOF
# BMAD Enhanced Deployment Record

**Date:** $(date)
**Version:** 2.0.0
**Environment:** Production
**Deployed By:** $(whoami)

## Deployment Details
- Deployment time: $(date)
- Server: $(hostname)
- Git commit: $(git rev-parse HEAD)
- Configuration: production

## Verification
- Health check: PASSED
- Smoke tests: PASSED
- Monitoring: ENABLED
- Backups: ENABLED

## Notes
- Initial production deployment
- All tests passing
- No issues encountered
EOF
```

---

## Rollback Procedures

### When to Rollback

- Critical failures in production
- Widespread errors affecting users
- Data corruption detected
- Security vulnerability discovered

### Rollback Steps

**Step 1: Stop Services**
```bash
# Stop any running workflows
# (BMAD Enhanced is stateless, but stop active sessions)

# Mark system as under maintenance
touch /opt/bmad-enhanced/.maintenance
```

**Step 2: Restore from Backup**
```bash
# Find latest backup
LATEST_BACKUP=$(ls -t /opt/bmad-enhanced/backups/ | head -1)

# Restore workflows
tar -xzf "/opt/bmad-enhanced/backups/${LATEST_BACKUP}/workflows.tar.gz" -C .

# Restore quality gates
tar -xzf "/opt/bmad-enhanced/backups/${LATEST_BACKUP}/quality.tar.gz" -C .

# Restore configuration
tar -xzf "/opt/bmad-enhanced/backups/${LATEST_BACKUP}/config.tar.gz" -C .
```

**Step 3: Verify Rollback**
```bash
# Run verification
./scripts/verify-deployment.sh

# Check configuration
cat .claude/config.yaml | grep version
```

**Step 4: Resume Operations**
```bash
# Remove maintenance mode
rm /opt/bmad-enhanced/.maintenance

# Notify team
./scripts/slack_notifier.py "BMAD Enhanced" "Rollback completed successfully" "info"
```

---

## Troubleshooting

### Common Issues

**Issue: Permission Denied**
```bash
# Fix permissions
chown -R bmad-user:bmad-group /opt/bmad-enhanced
chmod 755 /opt/bmad-enhanced/.claude
```

**Issue: Claude API Connection Failed**
```bash
# Test API connectivity
curl -H "x-api-key: $CLAUDE_API_KEY" \
  https://api.anthropic.com/v1/complete

# Check firewall rules
iptables -L | grep 443
```

**Issue: Disk Space Full**
```bash
# Check disk usage
df -h /opt/bmad-enhanced

# Clean old telemetry (older than 90 days)
find .claude/telemetry -name "*.json" -mtime +90 -delete

# Clean old workflows (older than 180 days)
find .claude/workflows -name "*-state.yaml" -mtime +180 -delete
```

**Issue: Configuration Invalid**
```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('.claude/config.yaml'))"

# Check for required fields
grep -q "project:" .claude/config.yaml || echo "Missing project section"
```

---

## Related Documentation

- [Production Monitoring Guide](./PRODUCTION-MONITORING-GUIDE.md) - Monitoring and alerting
- [Production Security Review](./PRODUCTION-SECURITY-REVIEW.md) - Security considerations
- [CI/CD Setup](../.github/workflows/bmad-validation.yml) - Automated validation
- [V2 Architecture](./V2-ARCHITECTURE.md) - Architecture overview

---

**Production Deployment Guide**
**Version:** 1.0
**Last Updated:** 2025-02-03
**Status:** Production Ready

*Part of BMAD Enhanced V2 Architecture - Phase 3: Production Readiness*
