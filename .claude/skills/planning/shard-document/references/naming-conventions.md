# Naming Conventions

## Overview

Consistent, descriptive naming improves discoverability and maintenance of sharded documents. This guide provides standards for naming files, directories, and metadata elements.

---

## File Naming

### General Principles

```
✅ DO:
- Use descriptive names (feature-authentication.md)
- Use kebab-case (lowercase-with-hyphens)
- Keep names concise (2-4 words ideal)
- Include content type if helpful (api-users-get.md)

❌ DON'T:
- Use generic names (document-1.md, shard-01.md)
- Use spaces (feature authentication.md)
- Use special characters (!@#$%^&*)
- Use overly long names (>50 characters)
```

---

### File Name Patterns

#### Pattern 1: Topic-Based

**Format:** `[topic].md`

**Examples:**
```
✅ Good:
- authentication.md
- dashboard.md
- user-personas.md
- market-analysis.md
- technical-requirements.md

❌ Avoid:
- auth.md (too abbreviated)
- the-authentication-feature.md (too verbose)
- Authentication.md (wrong case)
```

#### Pattern 2: Category-Topic

**Format:** `[category]-[topic].md`

**Examples:**
```
✅ Good:
- feature-authentication.md
- persona-sarah-admin.md
- metric-user-engagement.md
- api-users-list.md
- guide-getting-started.md

Benefits:
- Groups related shards
- Clear categorization
- Easy to scan in directory
```

#### Pattern 3: Hierarchical

**Format:** `[parent]-[child].md` or use directories

**Examples:**
```
Using filenames:
- api-users-get.md
- api-users-post.md
- api-products-get.md

Using directories (preferred):
api/
├── users/
│   ├── get.md
│   └── post.md
└── products/
    └── get.md
```

#### Pattern 4: Sequential (Size-Based Sharding)

**Format:** `part-[NN]-[topic].md`

**Examples:**
```
✅ Good:
- part-01-introduction.md
- part-02-methodology.md
- part-03-findings.md
- part-04-conclusion.md

⚠️ Acceptable (if no clear topics):
- part-01.md
- part-02.md
- part-03.md

Use when: Size-based sharding, continuous narrative
```

---

## Directory Naming

### Directory Structure Patterns

#### Pattern 1: Flat Structure (Simple)

```
prd-shards/
├── index.md
├── executive-summary.md
├── vision-objectives.md
├── user-personas.md
├── market-analysis.md
├── feature-authentication.md
├── feature-dashboard.md
├── feature-reporting.md
├── technical-requirements.md
└── success-metrics.md

Use when: <20 shards, simple organization
```

#### Pattern 2: Grouped by Category

```
prd-shards/
├── index.md
├── overview/
│   ├── executive-summary.md
│   └── vision-objectives.md
├── personas/
│   ├── sarah-admin.md
│   ├── mike-user.md
│   └── lisa-manager.md
├── features/
│   ├── authentication.md
│   ├── dashboard.md
│   └── reporting.md
└── technical/
    ├── requirements.md
    └── architecture.md

Use when: 20-50 shards, clear categories
```

#### Pattern 3: Deep Hierarchy

```
api-docs-shards/
├── index.md
├── getting-started/
│   ├── quickstart.md
│   └── authentication.md
├── resources/
│   ├── users/
│   │   ├── get.md
│   │   ├── post.md
│   │   └── put.md
│   ├── products/
│   │   ├── get.md
│   │   └── post.md
│   └── orders/
│       └── ...
└── guides/
    ├── pagination.md
    └── rate-limiting.md

Use when: 50+ shards, complex hierarchy
```

### Directory Names

**General Rules:**
```
✅ DO:
- Use plural for collections (features/, personas/, guides/)
- Use singular for single concept (overview/, authentication/)
- Use kebab-case (lowercase-with-hyphens)
- Keep names short and clear

❌ DON'T:
- Mix singular/plural inconsistently
- Use abbreviations (feat/, docs/)
- Use vague names (misc/, other/, stuff/)
```

**Standard Directory Names:**
```
Common patterns:
- features/ - Product features
- personas/ - User personas
- api/ - API documentation
- guides/ - How-to guides
- technical/ - Technical specs
- resources/ - API resources
- examples/ - Code examples
- appendices/ - Supplementary material
- references/ - Reference docs
```

---

## Metadata Naming

### shard_id Conventions

**Format:** `[category]-[topic]-[subtopic]`

**Examples:**
```
✅ Good:
- feature-authentication
- feature-dashboard-analytics
- persona-sarah-saas-admin
- api-users-get-by-id
- metric-monthly-active-users
- guide-getting-started

❌ Avoid:
- auth-feature (inconsistent order)
- feature_authentication (wrong separator)
- feature-auth (too abbreviated)
- shard-001 (not descriptive)
```

**Rules:**
- Must be unique across all shards
- Use kebab-case (lowercase-with-hyphens)
- Match filename when possible (consistency)
- 2-4 segments (category-topic-subtopic)
- No file extensions (.md)

---

### shard_type Conventions

**Standard Types:**
```
overview          # High-level summary
feature           # Feature specification
persona           # User persona
technical         # Technical specification
analysis          # Market/competitive analysis
metrics           # Success metrics, KPIs
workflow          # Process or workflow
api-endpoint      # API endpoint documentation
component         # System component
decision-record   # Architecture decision record
guide             # How-to or tutorial
reference         # Reference material
```

**Custom Types:**
- Use lowercase
- Use singular (feature not features)
- Be specific (api-endpoint vs endpoint)
- Document custom types in index

---

### Tag Conventions

**Lowercase, hyphenated:**
```
✅ Good:
- core-feature
- user-facing
- must-have
- authentication
- high-priority

❌ Avoid:
- Core Feature (wrong case)
- user_facing (wrong separator)
- MustHave (wrong case)
```

**Standard Tag Categories:**

```yaml
# Priority
- critical
- high-priority
- medium-priority
- low-priority

# Feature Status
- core-feature
- secondary-feature
- legacy-feature
- experimental

# MoSCoW
- must-have
- should-have
- could-have
- wont-have

# Domain
- authentication
- authorization
- database
- api
- ui
- backend
- frontend

# Audience
- user-facing
- admin-only
- developer-facing
- internal

# Technology
- node.js
- react
- postgresql
- aws
- docker
```

---

## Index File Naming

### Standard Names

```
✅ Required:
- index.md (root navigation)
- README.md (directory navigation)

❌ Don't use:
- home.md
- contents.md
- toc.md (unless Table of Contents specifically)
```

### Index Hierarchy

```
Root:
prd-shards/
└── index.md (main navigation)

Subdirectories:
features/
└── README.md (features navigation)

Technical:
technical/
└── README.md (technical navigation)
```

---

## Naming by Document Type

### PRDs (Product Requirements)

```
Shards:
- executive-summary.md
- vision-objectives.md
- personas/
  - [name]-[role].md (sarah-admin.md)
- features/
  - [feature-name].md (authentication.md)
- market-analysis.md
- technical-requirements.md
- success-metrics.md

Metadata:
- shard_id: feature-[name], persona-[name], etc.
- shard_type: feature, persona, analysis, etc.
```

### API Documentation

```
Shards:
- getting-started.md
- authentication.md
- errors.md
- resources/
  - [resource]/
    - [method]-[endpoint].md (get-user.md, create-user.md)
- webhooks.md

Metadata:
- shard_id: api-[resource]-[method] (api-users-get)
- shard_type: api-endpoint
```

### Architecture Documentation

```
Shards:
- architecture-overview.md
- components/
  - [component-name].md (frontend.md, backend.md)
- decision-records/
  - adr-[NNN]-[title].md (adr-001-framework-choice.md)
- deployment.md

Metadata:
- shard_id: architecture-[component], adr-[NNN]
- shard_type: component, decision-record
```

### User Guides

```
Shards:
- getting-started.md
- guides/
  - [action].md (create-account.md, send-email.md)
- troubleshooting.md
- faq.md

Metadata:
- shard_id: guide-[action] (guide-create-account)
- shard_type: guide
```

---

## Version Naming

### File Versions

```
Option 1: Version in directory
prd-shards-v1/
prd-shards-v2/

Option 2: Version in filename
prd-v1-shards/
prd-v2-shards/

Option 3: Git tags (preferred)
Use git tags: v1.0, v2.0
Keep directory name constant
```

### Metadata Versions

```yaml
version: 1.0  # Initial
version: 1.1  # Minor update
version: 2.0  # Major revision

# Semantic versioning:
# MAJOR.MINOR.PATCH
# MAJOR: Breaking changes
# MINOR: New features, backward compatible
# PATCH: Bug fixes
```

---

## Special File Names

### Reserved Names

```
✅ Standard Files:
- index.md (root navigation)
- README.md (directory navigation)
- CHANGELOG.md (version history)
- glossary.md (terminology)
- references.md (external links)

⚠️ Avoid overwriting:
- LICENSE.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
```

### Temporary Files

```
Pattern: .tmp.[name].md or [name].tmp.md

Examples:
- .tmp.draft-feature.md
- authentication.tmp.md

Use for: Work in progress, not yet validated
Note: Add to .gitignore
```

---

## Naming Checklist

Before finalizing names:

- [ ] File names are descriptive (not generic)
- [ ] File names use kebab-case
- [ ] File names match content
- [ ] Directory names use consistent plural/singular
- [ ] shard_id matches filename (when possible)
- [ ] shard_id is unique
- [ ] shard_type uses standard values
- [ ] Tags use lowercase-hyphenated format
- [ ] No special characters (except hyphens)
- [ ] Names are concise (<50 chars)
- [ ] Naming is consistent across all shards
- [ ] index.md and README.md in correct locations

---

## Naming Examples by Scenario

### Scenario 1: E-Commerce PRD

```
ecommerce-prd-shards/
├── index.md
├── executive-summary.md
├── personas/
│   ├── customer-end-user.md
│   ├── merchant-store-owner.md
│   └── admin-platform-operator.md
├── features/
│   ├── product-catalog.md
│   ├── shopping-cart.md
│   ├── checkout-process.md
│   ├── order-management.md
│   └── payment-processing.md
├── market-analysis.md
├── technical-requirements.md
└── success-metrics.md

Metadata examples:
- shard_id: feature-shopping-cart
- shard_id: persona-merchant-store-owner
- shard_type: feature, persona
- tags: [core-feature, ecommerce, user-facing]
```

### Scenario 2: REST API Docs

```
api-docs-shards/
├── index.md
├── getting-started.md
├── authentication.md
├── resources/
│   ├── README.md
│   ├── users/
│   │   ├── list-users.md
│   │   ├── get-user.md
│   │   ├── create-user.md
│   │   ├── update-user.md
│   │   └── delete-user.md
│   └── products/
│       ├── list-products.md
│       └── get-product.md
├── errors.md
└── rate-limiting.md

Metadata examples:
- shard_id: api-users-get-user
- shard_id: api-products-list
- shard_type: api-endpoint
- tags: [api, rest, users, read-operation]
```

---

## Best Practices

1. **Be Descriptive** - Names should indicate content
2. **Be Consistent** - Use same patterns throughout
3. **Be Concise** - Short but clear (2-4 words)
4. **Use kebab-case** - Lowercase with hyphens
5. **Match Metadata** - shard_id should match filename
6. **Avoid Abbreviations** - auth → authentication
7. **Use Standards** - index.md, README.md
8. **Document Conventions** - Explain custom patterns
9. **Test Readability** - Can users guess content from name?
10. **Refactor if Needed** - Fix inconsistent names early

---

**Naming Conventions - Part of shard-document skill**
**Use these conventions to create clear, consistent, discoverable names**
