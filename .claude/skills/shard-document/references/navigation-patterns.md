# Navigation Patterns

## Overview

Effective navigation is critical for sharded documents. This guide provides patterns for creating intuitive navigation systems that help users discover and traverse content.

---

## Pattern 1: Index-Based Navigation

### Description

Central index file (index.md) serves as primary navigation hub with links to all shards.

### Structure

```markdown
# Document Index

## Quick Navigation
- [Section 1](#section-1)
- [Section 2](#section-2)
- [Features](#features)

## Section 1
- [Subsection 1.1](section-1-1.md)
- [Subsection 1.2](section-1-2.md)

## Section 2
- [Subsection 2.1](section-2-1.md)
- [Subsection 2.2](section-2-2.md)

## Features
- [Feature A](features/feature-a.md)
- [Feature B](features/feature-b.md)
```

### Benefits
- ✅ Single point of entry
- ✅ Complete overview
- ✅ Easy to scan
- ⚠️ Can become long with many shards

---

## Pattern 2: Sequential Navigation

### Description

Previous/Next links at top and bottom of each shard for linear reading.

### Structure

```markdown
---
title: Feature: Authentication
---

[◄ Previous: Vision & Objectives](vision-objectives.md) | [Index](index.md) | [Next: Dashboard ►](feature-dashboard.md)

# Feature: Authentication

[Content...]

---

[◄ Previous: Vision & Objectives](vision-objectives.md) | [Index](index.md) | [Next: Dashboard ►](feature-dashboard.md)
```

### Benefits
- ✅ Clear reading order
- ✅ Always know what's next
- ✅ Book-like experience
- ⚠️ Requires defined sequence

---

## Pattern 3: Breadcrumb Navigation

### Description

Show hierarchy path from index to current shard.

### Structure

```markdown
---
title: GET /users/:id
---

[Home](../index.md) > [API Reference](index.md) > [Resources](resources/README.md) > [Users](users/README.md) > **GET /users/:id**

# GET /users/:id

[Content...]
```

### Benefits
- ✅ Shows context in hierarchy
- ✅ Easy to navigate up levels
- ✅ Clear document structure
- ⚠️ Takes more space

---

## Pattern 4: Tag-Based Navigation

### Description

Group shards by tags, enable topic-based discovery.

### Structure

```markdown
# Document Index

## Navigation by Tag

### #core-feature
- [Authentication](features/authentication.md)
- [Dashboard](features/dashboard.md)
- [Reporting](features/reporting.md)

### #security
- [Authentication](features/authentication.md)
- [Data Encryption](technical/encryption.md)
- [Access Control](technical/access-control.md)

### #user-facing
- [Dashboard](features/dashboard.md)
- [User Profile](features/user-profile.md)
- [Notifications](features/notifications.md)
```

### Benefits
- ✅ Topic-based discovery
- ✅ Cross-cutting navigation
- ✅ Multiple views of content
- ⚠️ Requires consistent tagging

---

## Pattern 5: Hierarchical Tree Navigation

### Description

Nested directory structure with README at each level.

### Structure

```
api-docs/
├── index.md (root navigation)
├── getting-started.md
├── authentication.md
└── resources/
    ├── README.md (resources navigation)
    ├── users/
    │   ├── README.md (users navigation)
    │   ├── get-user.md
    │   ├── create-user.md
    │   └── update-user.md
    └── products/
        ├── README.md (products navigation)
        ├── get-product.md
        └── create-product.md
```

**resources/README.md:**
```markdown
# API Resources

[◄ Back to API Docs](../index.md)

## Available Resources

### [Users](users/README.md)
Manage user accounts and profiles.
- [GET /users](users/get-user.md)
- [POST /users](users/create-user.md)
- [PUT /users/:id](users/update-user.md)

### [Products](products/README.md)
Manage product catalog.
- [GET /products](products/get-product.md)
- [POST /products](products/create-product.md)
```

### Benefits
- ✅ Mirrors content hierarchy
- ✅ Clear parent-child relationships
- ✅ Scalable to deep structures
- ⚠️ More files to maintain

---

## Pattern 6: Related Content Sidebar

### Description

Each shard includes "Related" section linking to relevant shards.

### Structure

```markdown
# Feature: Dashboard

## Overview
[Content...]

## Specification
[Content...]

---

## Related Documents

**Prerequisites:**
- [Authentication](authentication.md) - Must be logged in

**Related Features:**
- [Reporting](reporting.md) - Dashboard displays reports
- [Notifications](notifications.md) - Dashboard shows alerts

**Technical:**
- [Technical Requirements](../technical-requirements.md#dashboard)
- [Performance Metrics](../success-metrics.md#dashboard-performance)

**User Context:**
- [Persona: Sarah (Admin)](../personas.md#sarah-admin)
```

### Benefits
- ✅ Contextual navigation
- ✅ Discover related content
- ✅ Builds content network
- ⚠️ Requires manual curation

---

## Combined Navigation Pattern (Recommended)

### Description

Combine multiple patterns for comprehensive navigation.

### Implementation

```markdown
---
shard_id: feature-dashboard
---

<!-- Breadcrumbs -->
[Home](../index.md) > [Features](README.md) > **Dashboard**

<!-- Sequential Navigation -->
[◄ Previous: Authentication](authentication.md) | [Index](../index.md) | [Next: Reporting ►](reporting.md)

# Feature: Dashboard

## Overview
[Content...]

---

## Related Documents

<!-- Related Content Sidebar -->
**Prerequisites:**
- [Authentication](authentication.md)

**Related Features:**
- [Reporting](reporting.md)
- [Notifications](notifications.md)

---

<!-- Sequential Navigation (bottom) -->
[◄ Previous: Authentication](authentication.md) | [Index](../index.md) | [Next: Reporting ►](reporting.md)

<!-- Tags -->
**Tags:** #core-feature #ui #dashboard #user-facing
```

### Benefits
- ✅ Multiple navigation methods
- ✅ Suits different user needs
- ✅ Comprehensive coverage
- ⚠️ More complex to maintain

---

## Reading Path Patterns

### Linear Reading Path

```markdown
## Recommended Reading Order

1. [Getting Started](getting-started.md) (5 min)
2. [Authentication](authentication.md) (10 min)
3. [Core Features](features/README.md) (30 min)
4. [Advanced Topics](advanced/README.md) (20 min)

**Total Reading Time:** ~65 minutes
```

### Role-Based Reading Paths

```markdown
## Reading Paths by Role

### For Product Managers (30 min)
1. [Executive Summary](executive-summary.md)
2. [Vision & Objectives](vision-objectives.md)
3. [User Personas](personas.md)
4. [Feature Overview](features/README.md)

### For Engineers (45 min)
1. [Technical Requirements](technical-requirements.md)
2. [Architecture](architecture.md)
3. [Feature Specifications](features/)
4. [API Reference](api/)

### For Designers (20 min)
1. [User Personas](personas.md)
2. [User Flows](user-flows.md)
3. [UI Features](features/?tags=ui)
```

### Goal-Based Reading Paths

```markdown
## Reading Paths by Goal

### "I want to understand authentication"
1. [Feature: Authentication](features/authentication.md)
2. [Technical: Auth Implementation](technical/authentication.md)
3. [Security Considerations](security.md#authentication)
4. [User Flow: Login](user-flows.md#login)

### "I want to implement reporting"
1. [Feature: Reporting](features/reporting.md)
2. [Data Model](technical/data-model.md#reports)
3. [API: Reports Endpoints](api/reports/)
4. [Success Metrics](metrics.md#reporting)
```

---

## Navigation Component Templates

### Template 1: Top Navigation Bar

```markdown
[🏠 Home](index.md) | [📖 Features](features/README.md) | [🔧 Technical](technical/README.md) | [📊 Metrics](metrics.md) | [🔍 Search](search.md)
```

### Template 2: Footer Navigation

```markdown
---

**Navigation:**
- [◄ Previous](previous.md) • [📑 Index](index.md) • [Next ►](next.md)
- [⬆ Back to Top](#)
- [📂 Parent Section](../README.md)

**Quick Links:**
[Features](features/) • [API](api/) • [Glossary](glossary.md)

**Document Info:**
Last Updated: 2025-01-04 | Version: 1.0 | [View Source](../original.md)
```

### Template 3: Sidebar Table of Contents

```markdown
## Table of Contents

- [Overview](#overview)
- [Specification](#specification)
  - [Requirements](#requirements)
  - [Acceptance Criteria](#acceptance-criteria)
- [Technical Details](#technical-details)
- [Examples](#examples)
- [Related Documents](#related-documents)
```

---

## Best Practices

1. **Always Provide Way Back** - Every shard links to index
2. **Multiple Navigation Methods** - Sequential + hierarchical + tag-based
3. **Clear Current Location** - Breadcrumbs or highlighted nav
4. **Predictable Structure** - Consistent navigation across shards
5. **Mobile-Friendly** - Keep navigation compact for small screens
6. **Keyboard Accessible** - Use standard markdown links
7. **Visual Hierarchy** - Use headings and spacing effectively
8. **Reading Time Estimates** - Help users plan their time
9. **Cross-Reference Liberally** - Link to related content
10. **Test Navigation Paths** - Verify all links work

---

**Navigation Patterns - Part of shard-document skill**
**Use these patterns to create intuitive, discoverable navigation**
