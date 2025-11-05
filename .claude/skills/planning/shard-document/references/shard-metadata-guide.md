# Shard Metadata Guide

## Overview

Shard metadata provides context, relationships, and discovery information for each document shard. Rich metadata enables better navigation, search, and maintenance.

---

## Metadata Standard

### YAML Frontmatter Format

All shards should include YAML frontmatter at the top of the file:

```markdown
---
shard_id: unique-identifier
shard_type: category
parent: source-document
section: original-section-path
created_from: /path/to/source.md
created_at: 2025-01-04T10:30:00Z
updated_at: 2025-01-04T10:30:00Z
related:
  - other-shard-1.md
  - other-shard-2.md#section
dependencies:
  - required-shard-1.md
  - required-shard-2.md
tags:
  - tag1
  - tag2
  - tag3
status: draft | review | approved
version: 1.0
---

# Shard Content Starts Here

[Content...]
```

---

## Core Metadata Fields

### shard_id (Required)

**Purpose:** Unique identifier for the shard

**Format:** `kebab-case` string

**Examples:**
```yaml
shard_id: feature-authentication
shard_id: persona-sarah-saas-admin
shard_id: market-analysis-competitive-landscape
shard_id: api-users-get-endpoint
```

**Rules:**
- Must be unique across all shards
- Should be descriptive (not generic like shard-001)
- Use kebab-case (lowercase, hyphens)
- Max 50 characters recommended

---

### shard_type (Required)

**Purpose:** Categorize shard for filtering and organization

**Standard Types:**
```yaml
shard_type: overview          # High-level summary
shard_type: feature           # Feature specification
shard_type: persona           # User persona
shard_type: technical         # Technical specification
shard_type: analysis          # Market/competitive analysis
shard_type: metrics           # Success metrics, KPIs
shard_type: workflow          # Process or workflow
shard_type: api-endpoint      # API endpoint documentation
shard_type: component         # System component
shard_type: decision-record   # Architecture decision record
shard_type: guide             # How-to or tutorial
shard_type: reference         # Reference material
```

**Custom Types:** Projects can define additional types as needed

---

### parent (Required)

**Purpose:** Reference to original source document

**Format:** Filename or identifier of original document

**Examples:**
```yaml
parent: product-requirements-document.md
parent: api-documentation-v2.md
parent: architecture-overview.md
parent: prd-main
```

---

### section (Required)

**Purpose:** Original section path in source document

**Format:** Section hierarchy separated by ">"

**Examples:**
```yaml
section: 5.1 Feature: Authentication
section: 3.2 Persona: Mike (End User)
section: 4.1.2 Competitive Analysis > Key Competitors
section: API Reference > Resources > Users > GET /users/:id
```

**Benefits:**
- Trace shard back to original location
- Understand context in original document
- Facilitate re-merging if needed

---

### created_from (Required)

**Purpose:** Absolute or relative path to source file

**Format:** File path

**Examples:**
```yaml
created_from: docs/product-requirements-document.md
created_from: /home/user/docs/api-spec.md
created_from: ../original/architecture.md
```

---

### created_at / updated_at (Optional)

**Purpose:** Track when shard was created/modified

**Format:** ISO 8601 timestamp

**Examples:**
```yaml
created_at: 2025-01-04T10:30:00Z
updated_at: 2025-01-15T14:22:00Z
```

---

## Relationship Metadata Fields

### related (Optional but Recommended)

**Purpose:** Cross-reference related shards

**Format:** List of shard filenames (with optional anchors)

**Examples:**
```yaml
related:
  - technical-requirements.md
  - success-metrics.md#auth-metrics
  - persona-sarah.md
  - ../market-analysis.md
```

**When to Use:**
- Shards that provide additional context
- Cross-cutting concerns (e.g., security considerations)
- Alternative perspectives on same topic

---

### dependencies (Optional)

**Purpose:** Shards that must be read/understood first

**Format:** List of shard filenames

**Examples:**
```yaml
dependencies:
  - getting-started.md
  - authentication.md
  - user-management.md
```

**Difference from `related`:**
- `dependencies`: **Must** read first (prerequisite)
- `related`: **Should** read for additional context (optional)

**Example:**
```yaml
# Feature: Dashboard
dependencies:
  - feature-authentication.md  # Must auth before dashboard
related:
  - feature-reporting.md       # Dashboard shows reports
  - success-metrics.md         # Dashboard tracks metrics
```

---

### tags (Recommended)

**Purpose:** Enable topic-based discovery and filtering

**Format:** List of lowercase keywords

**Standard Tags:**
```yaml
# Priority
tags: [critical, high-priority, low-priority]

# Feature Category
tags: [core-feature, secondary-feature, legacy-feature]

# Domain
tags: [authentication, security, ui, api, database]

# Audience
tags: [user-facing, admin-only, developer-facing]

# Status
tags: [must-have, should-have, could-have, wont-have]

# Technical
tags: [frontend, backend, infrastructure, mobile]
```

**Examples:**
```yaml
# Authentication feature
tags:
  - core-feature
  - authentication
  - security
  - user-facing
  - must-have

# Admin dashboard
tags:
  - secondary-feature
  - ui
  - admin-only
  - should-have
  - frontend
```

**Best Practices:**
- Use 3-7 tags per shard
- Include at least one category tag
- Include at least one domain tag
- Be consistent across shards

---

## Document Management Fields

### status (Optional)

**Purpose:** Track review/approval status

**Format:** Enum

**Values:**
```yaml
status: draft       # Work in progress
status: review      # Ready for review
status: approved    # Reviewed and approved
status: archived    # No longer active
status: deprecated  # Superseded by newer version
```

---

### version (Optional)

**Purpose:** Track shard version

**Format:** Semantic versioning (major.minor.patch)

**Examples:**
```yaml
version: 1.0        # Initial version
version: 1.1        # Minor update
version: 2.0        # Major revision
```

---

### author (Optional)

**Purpose:** Document who created/maintains shard

**Format:** Name or identifier

**Examples:**
```yaml
author: John Smith
author: product-team
author: ai-generated
```

---

### reviewers (Optional)

**Purpose:** Track who reviewed the shard

**Format:** List of names

**Examples:**
```yaml
reviewers:
  - Sarah Johnson
  - Mike Chen
  - AI-Assistant
```

---

## Complete Metadata Examples

### Example 1: Feature Shard

```markdown
---
shard_id: feature-authentication
shard_type: feature
parent: product-requirements-document.md
section: 5.1 Feature: Authentication
created_from: docs/prd.md
created_at: 2025-01-04T10:30:00Z
updated_at: 2025-01-04T10:30:00Z
related:
  - technical-requirements.md#authentication
  - success-metrics.md#auth-metrics
  - persona-sarah.md
dependencies:
  - feature-user-management.md
tags:
  - core-feature
  - authentication
  - security
  - user-facing
  - must-have
  - backend
status: approved
version: 1.0
author: Product Team
reviewers:
  - Sarah Johnson (Product)
  - Mike Chen (Engineering)
---

# Feature: Authentication

[Feature content...]
```

---

### Example 2: API Endpoint Shard

```markdown
---
shard_id: api-users-get-by-id
shard_type: api-endpoint
parent: api-documentation-v2.md
section: API Reference > Resources > Users > GET /users/:id
created_from: docs/api-spec.md
created_at: 2025-01-04T11:00:00Z
related:
  - api-authentication.md
  - api-errors.md#404
  - api-users-list.md
dependencies:
  - api-getting-started.md
  - api-authentication.md
tags:
  - api
  - users
  - read
  - rest
  - backend
  - v2
status: approved
version: 2.0
---

# GET /users/:id

Retrieve a single user by ID.

[Endpoint documentation...]
```

---

### Example 3: Persona Shard

```markdown
---
shard_id: persona-sarah-saas-admin
shard_type: persona
parent: product-requirements-document.md
section: 3.1 Persona: Sarah (SaaS Admin)
created_from: docs/prd.md
created_at: 2025-01-04T10:45:00Z
related:
  - feature-admin-dashboard.md
  - feature-user-management.md
  - persona-mike-end-user.md
tags:
  - persona
  - admin
  - saas
  - primary-user
status: approved
version: 1.0
author: UX Research Team
---

# Persona: Sarah (SaaS Admin)

**Role:** SaaS Administrator
**Goal:** Manage team members and monitor usage

[Persona details...]
```

---

### Example 4: Technical Architecture Shard

```markdown
---
shard_id: architecture-backend-api
shard_type: component
parent: architecture-overview.md
section: 3. System Components > 3.2 Backend API
created_from: docs/architecture.md
created_at: 2025-01-04T12:00:00Z
related:
  - architecture-frontend.md
  - architecture-database.md
  - deployment.md
dependencies:
  - architecture-overview.md
tags:
  - architecture
  - backend
  - api
  - node.js
  - express
  - technical
status: approved
version: 1.0
---

# Backend API Architecture

[Architecture details...]
```

---

## Metadata Validation Rules

### Required Field Validation

```yaml
✅ VALID:
shard_id: feature-authentication
shard_type: feature
parent: prd.md
section: 5.1 Authentication
created_from: docs/prd.md

❌ INVALID (missing required fields):
shard_id: feature-authentication
# Missing: shard_type, parent, section, created_from
```

---

### shard_id Uniqueness

```yaml
# File 1: authentication.md
shard_id: feature-authentication  ✅

# File 2: dashboard.md
shard_id: feature-authentication  ❌ Duplicate!
```

**Validation:** No two shards can have same shard_id

---

### File References Validation

```yaml
# authentication.md
related:
  - technical-requirements.md  ✅ File exists
  - missing-file.md            ❌ File not found

dependencies:
  - user-management.md         ✅ File exists
```

**Validation:** All referenced files must exist

---

### Circular Dependency Detection

```yaml
# authentication.md
dependencies:
  - user-management.md

# user-management.md
dependencies:
  - authentication.md  ❌ Circular dependency!
```

**Validation:** Dependency graph must be acyclic

---

## Metadata Usage Patterns

### Pattern 1: Discovery by Tag

```bash
# Find all core features
grep -l "tags:.*core-feature" *.md

# Find all authentication-related shards
grep -l "tags:.*authentication" **/*.md
```

### Pattern 2: Dependency Chain

```yaml
# user wants to read: dashboard.md

dashboard.md dependencies: [authentication.md, reporting.md]
authentication.md dependencies: [getting-started.md]
reporting.md dependencies: [data-model.md]
getting-started.md dependencies: []
data-model.md dependencies: []

Reading order:
1. getting-started.md
2. authentication.md
3. data-model.md
4. reporting.md
5. dashboard.md
```

### Pattern 3: Related Content Network

```yaml
# From authentication.md
related:
  - technical-requirements.md#auth
  - security-guide.md
  - user-management.md

# Build network graph for visualization:
authentication.md ─┬─ technical-requirements.md
                   ├─ security-guide.md
                   └─ user-management.md ─ permissions.md
```

---

## Metadata Extraction Script

```python
import yaml
import re

def extract_metadata(shard_file):
    """Extract YAML frontmatter from shard"""
    with open(shard_file, 'r') as f:
        content = f.read()

    # Extract YAML between --- markers
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None

    metadata = yaml.safe_load(match.group(1))
    return metadata

def validate_metadata(metadata):
    """Validate required fields"""
    required = ['shard_id', 'shard_type', 'parent', 'section', 'created_from']
    missing = [field for field in required if field not in metadata]

    if missing:
        return False, f"Missing required fields: {missing}"

    return True, "Valid"

# Usage
metadata = extract_metadata('authentication.md')
valid, message = validate_metadata(metadata)
print(f"Validation: {message}")
```

---

## Metadata Generation Template

```yaml
---
# REQUIRED FIELDS
shard_id: [unique-kebab-case-id]
shard_type: [overview|feature|persona|technical|analysis|metrics|etc]
parent: [source-document-filename.md]
section: [original section path]
created_from: [path/to/source.md]

# TIMESTAMPS
created_at: [ISO 8601 timestamp]
updated_at: [ISO 8601 timestamp]

# RELATIONSHIPS
related:
  - [related-shard-1.md]
  - [related-shard-2.md#section]
dependencies:
  - [prerequisite-shard-1.md]
  - [prerequisite-shard-2.md]

# DISCOVERY
tags:
  - [category-tag]
  - [domain-tag]
  - [audience-tag]
  - [priority-tag]

# DOCUMENT MANAGEMENT (Optional)
status: [draft|review|approved|archived|deprecated]
version: [major.minor]
author: [name or team]
reviewers:
  - [reviewer-name-1]
  - [reviewer-name-2]
---
```

---

## Best Practices

1. **Always Include Required Fields** - shard_id, shard_type, parent, section, created_from
2. **Use Descriptive IDs** - `feature-authentication` not `shard-001`
3. **Consistent Tag Vocabulary** - Standardize tags across shards
4. **Document Dependencies** - Help readers understand prerequisites
5. **Cross-Reference Related Shards** - Build content network
6. **Track Status** - Use status field for review workflows
7. **Version Your Shards** - Increment version on significant changes
8. **Validate Metadata** - Check all references exist, no circular deps
9. **Keep Metadata Updated** - Update timestamps and version on edits
10. **Use Standard Types** - Stick to predefined shard_type values

---

**Shard Metadata Guide - Part of shard-document skill**
**Use this guide to create rich, discoverable shard metadata**
