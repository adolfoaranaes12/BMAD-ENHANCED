# Production Monitoring & Alerting Guide

**Version:** 1.0
**Date:** 2025-02-03
**Status:** Production Ready
**Audience:** DevOps, SRE, Operations Teams

---

## Table of Contents

1. [Overview](#overview)
2. [What to Monitor](#what-to-monitor)
3. [Telemetry Architecture](#telemetry-architecture)
4. [Monitoring Setup](#monitoring-setup)
5. [Alerting Strategy](#alerting-strategy)
6. [Health Checks](#health-checks)
7. [Performance Metrics](#performance-metrics)
8. [Dashboard Recommendations](#dashboard-recommendations)
9. [Troubleshooting](#troubleshooting)
10. [Integration Examples](#integration-examples)

---

## Overview

BMAD Enhanced V2 provides comprehensive telemetry and observability out of the box. This guide helps you set up production monitoring, alerting, and dashboards to ensure system health and performance.

### Monitoring Goals

- **Availability:** Ensure all subagents and skills are operational
- **Performance:** Track execution times and identify bottlenecks
- **Quality:** Monitor quality gate pass/fail rates
- **Reliability:** Detect and alert on failures
- **Capacity:** Track resource usage and identify limits

### Key Metrics at a Glance

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Workflow Success Rate | >95% | <90% |
| Quality Gate Pass Rate | >80% | <70% |
| Avg Complexity Assessment Time | <100ms | >300ms |
| Avg Guardrail Validation Time | <150ms | >500ms |
| Workflow Resume Success Rate | >90% | <80% |
| Test Coverage (per task) | >80% | <70% |

---

## What to Monitor

### 1. Workflow Execution

**Metrics:**
- Workflow start/completion times
- Phase transition times
- Success/failure rates by workflow type
- Resume success rates

**Data Source:** `.claude/workflows/{workflow-id}-state.yaml`

**Example Monitoring:**
```bash
# Count workflows by status
grep -h "^status:" .claude/workflows/*-state.yaml | sort | uniq -c

# Average workflow duration
grep -h "total_duration:" .claude/telemetry/workflows/*.json | \
  awk -F': ' '{sum+=$2; count++} END {print sum/count " seconds"}'
```

---

### 2. Subagent Performance

**Metrics:**
- Command execution times per subagent
- Complexity assessment accuracy
- Routing decision times
- Guardrail validation times

**Data Source:** `.claude/telemetry/subagents/{subagent}-{timestamp}.json`

**Example Monitoring:**
```bash
# Track james-developer command execution times
jq '.phases[] | select(.subagent=="james-developer") | .duration' \
  .claude/telemetry/workflows/*.json
```

---

### 3. Quality Gates

**Metrics:**
- Quality gate decisions (PASS/CONCERNS/FAIL/WAIVED)
- Quality scores over time
- Issue severity distribution
- Coverage trends

**Data Source:** `.claude/quality/gates/{task-id}-gate-*.yaml`

**Example Monitoring:**
```bash
# Quality gate pass rate
grep -h "^decision:" .claude/quality/gates/*-gate-*.yaml | \
  grep -c "PASS" | awk '{print $1/NR*100 "%"}'

# Average quality scores
grep -h "^quality_score:" .claude/quality/gates/*-gate-*.yaml | \
  awk '{sum+=$2; count++} END {print sum/count}'
```

---

### 4. Test Coverage

**Metrics:**
- Overall test coverage %
- Coverage by task/feature
- Coverage trends over time
- Gap counts

**Data Source:** Test execution output, quality gate files

**Example Monitoring:**
```bash
# Track coverage trends
grep -h "coverage:" .claude/quality/gates/*-gate-*.yaml | \
  awk '{print $2}' | sort -n | tail -10
```

---

### 5. Error Rates

**Metrics:**
- Failed workflows
- Failed phases
- Guardrail violations
- Escalation triggers

**Data Source:** Telemetry files, workflow state files

**Example Monitoring:**
```bash
# Count failed workflows
grep -h "^status: failed" .claude/workflows/*-state.yaml | wc -l

# Recent errors
jq '.errors[]' .claude/telemetry/**/*.json | tail -20
```

---

## Telemetry Architecture

### Telemetry File Structure

```
.claude/
├── telemetry/
│   ├── workflows/
│   │   ├── wf-feature-login-20250203.json
│   │   └── wf-epic-auth-20250203.json
│   ├── subagents/
│   │   ├── alex-planner-20250203.json
│   │   ├── james-developer-20250203.json
│   │   ├── quinn-quality-20250203.json
│   │   └── orchestrator-20250203.json
│   └── skills/
│       ├── implement-feature-20250203.json
│       └── review-task-20250203.json
├── workflows/
│   └── {workflow-id}-state.yaml
└── quality/
    └── gates/
        └── {task-id}-gate-{timestamp}.yaml
```

### Telemetry Data Format

**Workflow Telemetry:**
```json
{
  "workflow_id": "wf-feature-login-20250203",
  "workflow_type": "feature-delivery",
  "start_time": "2025-02-03T10:30:00Z",
  "end_time": "2025-02-03T11:15:22Z",
  "total_duration": "45m 22s",
  "status": "completed",
  "phases": [
    {
      "phase": "planning",
      "subagent": "alex-planner",
      "start_time": "2025-02-03T10:30:00Z",
      "end_time": "2025-02-03T10:38:32Z",
      "duration": "8m 32s",
      "status": "completed",
      "complexity_score": 35,
      "route_selected": "standard"
    },
    {
      "phase": "implementation",
      "subagent": "james-developer",
      "start_time": "2025-02-03T10:38:35Z",
      "end_time": "2025-02-03T11:06:50Z",
      "duration": "28m 15s",
      "status": "completed",
      "complexity_score": 42,
      "route_selected": "standard",
      "test_coverage": 87,
      "files_changed": 4
    },
    {
      "phase": "quality_review",
      "subagent": "quinn-quality",
      "start_time": "2025-02-03T11:06:52Z",
      "end_time": "2025-02-03T11:15:27Z",
      "duration": "8m 35s",
      "status": "completed",
      "quality_gate": "PASS",
      "quality_score": 85,
      "issues_found": 2,
      "issues_severity": {"low": 2}
    }
  ],
  "metrics": {
    "total_files_changed": 4,
    "total_test_coverage": 87,
    "quality_score": 85,
    "success": true
  }
}
```

---

## Monitoring Setup

### Option 1: File-Based Monitoring (Simple)

**Best for:** Small teams, development environments

**Setup:**
```bash
#!/bin/bash
# monitor.sh - Simple file-based monitoring

# Check workflow success rate
TOTAL=$(ls .claude/workflows/*-state.yaml 2>/dev/null | wc -l)
SUCCESS=$(grep -l "^status: completed" .claude/workflows/*-state.yaml 2>/dev/null | wc -l)
SUCCESS_RATE=$(echo "scale=2; $SUCCESS / $TOTAL * 100" | bc)

echo "Workflow Success Rate: ${SUCCESS_RATE}%"

if (( $(echo "$SUCCESS_RATE < 90" | bc -l) )); then
  echo "⚠️ ALERT: Success rate below 90%"
fi

# Check quality gate pass rate
TOTAL_GATES=$(ls .claude/quality/gates/*-gate-*.yaml 2>/dev/null | wc -l)
PASS_GATES=$(grep -l "^decision: PASS" .claude/quality/gates/*-gate-*.yaml 2>/dev/null | wc -l)
PASS_RATE=$(echo "scale=2; $PASS_GATES / $TOTAL_GATES * 100" | bc)

echo "Quality Gate Pass Rate: ${PASS_RATE}%"

if (( $(echo "$PASS_RATE < 80" | bc -l) )); then
  echo "⚠️ ALERT: Quality gate pass rate below 80%"
fi
```

**Cron Setup:**
```bash
# Run monitoring every 15 minutes
*/15 * * * * /path/to/monitor.sh >> /var/log/bmad-monitoring.log 2>&1
```

---

### Option 2: Log Aggregation (Medium)

**Best for:** Medium teams, staging/production

**Recommended Tools:**
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Grafana Loki**
- **Datadog**

**Setup Example (Filebeat → Elasticsearch):**

```yaml
# filebeat.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /path/to/.claude/telemetry/**/*.json
    json.keys_under_root: true
    json.add_error_key: true
    fields:
      type: bmad_telemetry

  - type: log
    enabled: true
    paths:
      - /path/to/.claude/workflows/*-state.yaml
    fields:
      type: bmad_workflow_state

output.elasticsearch:
  hosts: ["localhost:9200"]
  index: "bmad-telemetry-%{+yyyy.MM.dd}"
```

**Kibana Dashboard:**
- Workflow success rate over time
- Quality gate decisions (pie chart)
- Average execution time by subagent (bar chart)
- Error rate trends (line chart)

---

### Option 3: Application Performance Monitoring (Advanced)

**Best for:** Large teams, production environments

**Recommended Tools:**
- **New Relic**
- **Datadog APM**
- **Prometheus + Grafana**

**Setup Example (Prometheus exporter):**

```python
#!/usr/bin/env python3
# bmad_exporter.py - Prometheus exporter for BMAD Enhanced

from prometheus_client import start_http_server, Gauge, Counter
import yaml
import json
import glob
import time

# Metrics
workflow_success_rate = Gauge('bmad_workflow_success_rate', 'Workflow success rate percentage')
quality_gate_pass_rate = Gauge('bmad_quality_gate_pass_rate', 'Quality gate pass rate percentage')
avg_workflow_duration = Gauge('bmad_avg_workflow_duration_seconds', 'Average workflow duration')
workflows_total = Counter('bmad_workflows_total', 'Total workflows executed')
quality_gates_total = Counter('bmad_quality_gates_total', 'Total quality gates', ['decision'])

def collect_metrics():
    # Workflow success rate
    workflow_files = glob.glob('.claude/workflows/*-state.yaml')
    total = len(workflow_files)
    success = 0

    for file in workflow_files:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
            if data.get('status') == 'completed':
                success += 1

    if total > 0:
        workflow_success_rate.set(success / total * 100)

    # Quality gate pass rate
    gate_files = glob.glob('.claude/quality/gates/*-gate-*.yaml')
    total_gates = len(gate_files)
    pass_gates = 0

    for file in gate_files:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
            decision = data.get('decision', '')
            quality_gates_total.labels(decision=decision).inc()
            if decision == 'PASS':
                pass_gates += 1

    if total_gates > 0:
        quality_gate_pass_rate.set(pass_gates / total_gates * 100)

    # Average workflow duration
    telemetry_files = glob.glob('.claude/telemetry/workflows/*.json')
    durations = []

    for file in telemetry_files:
        with open(file, 'r') as f:
            data = json.load(f)
            duration_str = data.get('total_duration', '0s')
            # Parse duration (simplified - handle "45m 22s" format)
            # Convert to seconds
            durations.append(parse_duration(duration_str))

    if durations:
        avg_workflow_duration.set(sum(durations) / len(durations))

def parse_duration(duration_str):
    """Parse duration string like '45m 22s' to seconds"""
    total_seconds = 0
    parts = duration_str.split()
    for part in parts:
        if 'h' in part:
            total_seconds += int(part.replace('h', '')) * 3600
        elif 'm' in part:
            total_seconds += int(part.replace('m', '')) * 60
        elif 's' in part:
            total_seconds += int(part.replace('s', ''))
    return total_seconds

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        collect_metrics()
        time.sleep(60)  # Update every minute
```

**Prometheus Configuration:**
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'bmad-enhanced'
    static_configs:
      - targets: ['localhost:8000']
```

---

## Alerting Strategy

### Alert Levels

**P0 (Critical) - Page immediately:**
- Workflow success rate < 80%
- Quality gate FAIL rate > 30%
- All subagents failing
- Data corruption detected

**P1 (High) - Alert within 15 minutes:**
- Workflow success rate < 90%
- Quality gate pass rate < 70%
- Multiple guardrail violations
- Test coverage < 60%

**P2 (Medium) - Alert within 1 hour:**
- Workflow success rate < 95%
- Quality gate pass rate < 80%
- Performance degradation > 50%
- Coverage < 80%

**P3 (Low) - Daily summary:**
- Individual workflow failures
- Quality concerns
- Performance variations

### Alert Routing

```yaml
# alerting_rules.yml (Prometheus)
groups:
  - name: bmad_enhanced_alerts
    interval: 1m
    rules:
      - alert: WorkflowSuccessRateLow
        expr: bmad_workflow_success_rate < 90
        for: 5m
        labels:
          severity: P1
        annotations:
          summary: "Workflow success rate below 90%"
          description: "Current success rate: {{ $value }}%"

      - alert: QualityGatePassRateLow
        expr: bmad_quality_gate_pass_rate < 80
        for: 10m
        labels:
          severity: P1
        annotations:
          summary: "Quality gate pass rate below 80%"
          description: "Current pass rate: {{ $value }}%"

      - alert: WorkflowDurationHigh
        expr: bmad_avg_workflow_duration_seconds > 5400  # 90 minutes
        for: 15m
        labels:
          severity: P2
        annotations:
          summary: "Average workflow duration exceeds 90 minutes"
          description: "Current avg duration: {{ $value }} seconds"
```

### Alert Channels

**Recommended integrations:**
- **Slack:** Real-time alerts to development channel
- **PagerDuty:** P0/P1 escalation
- **Email:** Daily summaries and P2/P3 alerts
- **Jira:** Auto-create tickets for P1/P2 alerts

---

## Health Checks

### System Health Check Script

```bash
#!/bin/bash
# health_check.sh - BMAD Enhanced health check

set -e

echo "=== BMAD Enhanced Health Check ==="
echo "Timestamp: $(date)"
echo ""

# Check directory structure
echo "✓ Checking directory structure..."
[ -d ".claude" ] || { echo "✗ .claude directory missing"; exit 1; }
[ -d ".claude/agents" ] || { echo "✗ .claude/agents missing"; exit 1; }
[ -d ".claude/skills" ] || { echo "✗ .claude/skills missing"; exit 1; }

# Check subagent files
echo "✓ Checking subagent files..."
for agent in orchestrator-v2 alex-planner james-developer-v2 quinn-quality; do
  [ -f ".claude/agents/${agent}.md" ] || { echo "✗ ${agent}.md missing"; exit 1; }
done

# Check skill directories
echo "✓ Checking skills..."
skill_count=$(find .claude/skills -name "SKILL.md" | wc -l)
echo "  Found ${skill_count} skills"
[ "$skill_count" -ge 17 ] || { echo "✗ Expected 17+ skills, found ${skill_count}"; exit 1; }

# Check recent activity
echo "✓ Checking recent activity..."
recent_workflows=$(find .claude/workflows -name "*-state.yaml" -mtime -7 2>/dev/null | wc -l)
echo "  Workflows in last 7 days: ${recent_workflows}"

recent_gates=$(find .claude/quality/gates -name "*-gate-*.yaml" -mtime -7 2>/dev/null | wc -l)
echo "  Quality gates in last 7 days: ${recent_gates}"

# Check telemetry
echo "✓ Checking telemetry..."
telemetry_files=$(find .claude/telemetry -name "*.json" -mtime -1 2>/dev/null | wc -l)
echo "  Telemetry files in last 24h: ${telemetry_files}"

# Performance check
echo "✓ Checking performance..."
if [ -f ".claude/telemetry/workflows/*.json" ]; then
  avg_duration=$(jq -s 'map(.total_duration) | add/length' .claude/telemetry/workflows/*.json 2>/dev/null || echo "N/A")
  echo "  Average workflow duration: ${avg_duration}"
fi

echo ""
echo "=== Health Check PASSED ==="
exit 0
```

**HTTP Health Endpoint (Optional):**

```python
#!/usr/bin/env python3
# health_server.py - Simple health check HTTP endpoint

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import glob

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            health = self.check_health()
            self.send_response(200 if health['healthy'] else 503)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(health, indent=2).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def check_health(self):
        checks = {
            'healthy': True,
            'checks': {}
        }

        # Check directories
        checks['checks']['directories'] = {
            'status': 'ok' if os.path.exists('.claude/agents') else 'fail'
        }

        # Check recent activity
        recent_workflows = len(glob.glob('.claude/workflows/*-state.yaml'))
        checks['checks']['workflows'] = {
            'status': 'ok' if recent_workflows > 0 else 'warn',
            'count': recent_workflows
        }

        # Overall health
        checks['healthy'] = all(
            c.get('status') == 'ok'
            for c in checks['checks'].values()
        )

        return checks

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    print('Health check server running on port 8080')
    server.serve_forever()
```

---

## Performance Metrics

### Key Performance Indicators (KPIs)

| KPI | Target | Current | Status |
|-----|--------|---------|--------|
| **Workflow Throughput** | 10-20 workflows/day | - | - |
| **Workflow Success Rate** | >95% | - | - |
| **Quality Gate Pass Rate** | >80% | - | - |
| **Avg Workflow Duration** | <60 min | - | - |
| **Avg Complexity Assessment** | <100ms | 20ms | ✅ |
| **Avg Guardrail Validation** | <150ms | 25ms | ✅ |
| **Avg Telemetry Overhead** | <50ms | 6ms | ✅ |
| **Test Coverage** | >80% | - | - |

### Performance Tracking Query Examples

```bash
# Workflow duration trends
jq -r '.total_duration' .claude/telemetry/workflows/*.json | \
  sort | uniq -c

# Complexity assessment times
jq -r '.phases[] | select(.phase=="assess") | .duration' \
  .claude/telemetry/**/*.json

# Quality scores over time
grep -h "^quality_score:" .claude/quality/gates/*-gate-*.yaml | \
  awk '{print $2}' | sort -n
```

---

## Dashboard Recommendations

### Grafana Dashboard Layout

**Row 1: Overview**
- Workflow success rate (gauge)
- Quality gate pass rate (gauge)
- Active workflows (stat)
- Workflows today (stat)

**Row 2: Performance**
- Avg workflow duration (line chart, 24h)
- Subagent execution times (bar chart)
- Complexity assessment times (histogram)

**Row 3: Quality**
- Quality scores distribution (histogram)
- Quality gate decisions (pie chart)
- Test coverage trends (line chart)
- Issue severity breakdown (bar chart)

**Row 4: Details**
- Recent workflow executions (table)
- Recent failures (table)
- Recent quality gates (table)

### Sample Grafana Queries

```promql
# Workflow success rate (%)
rate(bmad_workflows_total{status="completed"}[5m]) /
rate(bmad_workflows_total[5m]) * 100

# Average workflow duration
avg_over_time(bmad_avg_workflow_duration_seconds[1h])

# Quality gate pass rate
rate(bmad_quality_gates_total{decision="PASS"}[5m]) /
rate(bmad_quality_gates_total[5m]) * 100
```

---

## Troubleshooting

### Common Issues

**Issue: High workflow failure rate**

**Investigation:**
```bash
# Find failed workflows
grep -l "^status: failed" .claude/workflows/*-state.yaml

# Check error details
jq '.errors' .claude/telemetry/workflows/*.json
```

**Remediation:**
- Review error logs
- Check guardrail violations
- Verify prerequisites met
- Resume failed workflows if possible

---

**Issue: Quality gate failures increasing**

**Investigation:**
```bash
# Check FAIL decision details
grep -A 20 "^decision: FAIL" .claude/quality/gates/*-gate-*.yaml

# Analyze issue trends
grep -h "issue_severity:" .claude/quality/gates/*.yaml | sort | uniq -c
```

**Remediation:**
- Review code quality standards
- Increase test coverage
- Address high-severity issues promptly
- Update quality thresholds if needed

---

**Issue: Performance degradation**

**Investigation:**
```bash
# Check recent durations
jq '.total_duration' .claude/telemetry/workflows/*.json | tail -10

# Find slow phases
jq '.phases[] | select(.duration > "10m")' .claude/telemetry/**/*.json
```

**Remediation:**
- Identify bottleneck phases
- Review complexity scores
- Optimize slow skills
- Check for resource contention

---

## Integration Examples

### Slack Integration

```python
#!/usr/bin/env python3
# slack_notifier.py - Send BMAD alerts to Slack

import requests
import json
import sys

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

def send_alert(title, message, severity="info"):
    colors = {
        "critical": "#FF0000",
        "warning": "#FFA500",
        "info": "#0000FF"
    }

    payload = {
        "attachments": [{
            "color": colors.get(severity, "#808080"),
            "title": title,
            "text": message,
            "footer": "BMAD Enhanced Monitoring",
            "footer_icon": "https://example.com/bmad-icon.png"
        }]
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return response.status_code == 200

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: slack_notifier.py <title> <message> [severity]")
        sys.exit(1)

    title = sys.argv[1]
    message = sys.argv[2]
    severity = sys.argv[3] if len(sys.argv) > 3 else "info"

    if send_alert(title, message, severity):
        print("Alert sent successfully")
    else:
        print("Failed to send alert")
        sys.exit(1)
```

---

### PagerDuty Integration

```python
#!/usr/bin/env python3
# pagerduty_alert.py - Create PagerDuty incident

import requests
import json
import sys

PAGERDUTY_API_KEY = "YOUR_API_KEY"
PAGERDUTY_SERVICE_ID = "YOUR_SERVICE_ID"

def create_incident(title, description, severity="error"):
    headers = {
        "Authorization": f"Token token={PAGERDUTY_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.pagerduty+json;version=2"
    }

    payload = {
        "incident": {
            "type": "incident",
            "title": title,
            "service": {
                "id": PAGERDUTY_SERVICE_ID,
                "type": "service_reference"
            },
            "urgency": "high" if severity == "critical" else "low",
            "body": {
                "type": "incident_body",
                "details": description
            }
        }
    }

    response = requests.post(
        "https://api.pagerduty.com/incidents",
        headers=headers,
        json=payload
    )

    return response.status_code == 201

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: pagerduty_alert.py <title> <description> [severity]")
        sys.exit(1)

    title = sys.argv[1]
    description = sys.argv[2]
    severity = sys.argv[3] if len(sys.argv) > 3 else "error"

    if create_incident(title, description, severity):
        print("PagerDuty incident created")
    else:
        print("Failed to create incident")
        sys.exit(1)
```

---

## Best Practices

### DO's ✅

- **Monitor continuously:** Set up automated monitoring, don't rely on manual checks
- **Alert smartly:** Use appropriate alert levels (P0-P3) to avoid alert fatigue
- **Track trends:** Monitor metrics over time, not just current values
- **Document incidents:** Keep runbooks for common issues
- **Review regularly:** Weekly review of metrics and alerts
- **Test alerting:** Regularly test your alerting system

### DON'Ts ❌

- **Don't over-alert:** Too many alerts lead to alert fatigue
- **Don't ignore trends:** A slow degradation is still a problem
- **Don't skip health checks:** Regular health checks prevent surprises
- **Don't forget baselines:** Establish normal metrics to detect anomalies
- **Don't neglect telemetry:** Telemetry files contain valuable insights

---

## Next Steps

1. **Choose monitoring approach:** File-based, log aggregation, or APM
2. **Set up dashboards:** Create Grafana/Kibana dashboards
3. **Configure alerts:** Set up Slack/PagerDuty integrations
4. **Run health checks:** Schedule daily health check runs
5. **Review and iterate:** Adjust thresholds based on actual usage

---

## Related Documentation

- [Deployment Guide](./PRODUCTION-DEPLOYMENT-GUIDE.md) - How to deploy BMAD Enhanced
- [Security Review](./PRODUCTION-SECURITY-REVIEW.md) - Security considerations
- [CI/CD Setup](../github/workflows/bmad-validation.yml) - Automated validation
- [V2 Architecture](./V2-ARCHITECTURE.md) - Architecture overview

---

**Production Monitoring & Alerting Guide**
**Version:** 1.0
**Last Updated:** 2025-02-03
**Status:** Production Ready

*Part of BMAD Enhanced V2 Architecture - Phase 3: Production Readiness*
