# Sharding Strategies

## Overview

Document sharding strategies determine how to break large documents into smaller pieces. The choice of strategy depends on document structure, use case, and audience needs.

---

## Strategy 1: Logical Sharding (Recommended)

### Description

Split document by logical boundaries such as sections, topics, or components. Maintains conceptual integrity of each shard.

### When to Use

- Document has clear structure (headings, sections)
- Topics are distinct and self-contained
- Users need to navigate by topic/feature
- Document is well-organized

### Characteristics

```
✅ Preserves semantic meaning
✅ Each shard is conceptually complete
✅ Natural navigation by topic
✅ Easy to understand organization
⚠️ Shards may vary in size (some large, some small)
```

### Example

```markdown
Original Document (3,500 lines):
# Product Requirements Document
## 1. Executive Summary (300 lines)
## 2. User Personas (500 lines)
## 3. Features (1,500 lines)
### 3.1 Authentication (200 lines)
### 3.2 Dashboard (300 lines)
### 3.3 Reporting (400 lines)
... (7 more features)
## 4. Technical Requirements (800 lines)
## 5. Success Metrics (400 lines)

Logical Sharding:
prd-shards/
├── index.md (navigation)
├── executive-summary.md (300 lines)
├── user-personas.md (500 lines)
├── features/
│   ├── authentication.md (200 lines)
│   ├── dashboard.md (300 lines)
│   ├── reporting.md (400 lines)
│   └── ... (7 more, 100-150 lines each)
├── technical-requirements.md (800 lines)
└── success-metrics.md (400 lines)

Result:
- 13 shards total
- Range: 100-800 lines per shard
- Avg: 270 lines per shard
- Each shard is complete topic
```

### Implementation

```
1. Parse document headings (H1, H2, H3)
2. Identify major sections (H1, H2)
3. Determine shard boundaries:
   - Top-level sections → separate shards
   - Large sections (>500 lines) → split by subsections
   - Related subsections → group together
4. Create shards with descriptive names
5. Maintain hierarchy in directory structure
```

---

## Strategy 2: Size-Based Sharding

### Description

Split document when size exceeds threshold (e.g., 500 lines). Finds nearest logical boundary (heading) to split.

### When to Use

- Document lacks clear structure
- Need consistent shard sizes
- Pagination-style reading preferred
- Document is continuous narrative

### Characteristics

```
✅ Predictable shard sizes
✅ Works with unstructured documents
✅ Easy to implement algorithmically
⚠️ May split mid-topic
⚠️ Less intuitive navigation
⚠️ Shard boundaries may feel arbitrary
```

### Example

```markdown
Original Document (2,500 lines, minimal structure):
# User Research Report
[Long narrative with few headings]
...

Size-Based Sharding (max: 500 lines):
report-shards/
├── index.md
├── part-01-introduction.md (450 lines, stops at heading)
├── part-02-methodology.md (520 lines, slightly over but at heading break)
├── part-03-findings-1.md (480 lines)
├── part-04-findings-2.md (510 lines)
└── part-05-conclusion.md (400 lines)

Result:
- 5 shards
- Range: 400-520 lines (close to 500 target)
- Sequential numbering
- Prev/next navigation
```

### Implementation

```
1. Set max_shard_size (default: 500 lines)
2. Scan document line by line
3. When approaching max size:
   - Look ahead for nearest heading (next 50 lines)
   - Split at heading boundary
   - If no heading, split at paragraph break
4. Name shards sequentially (part-01, part-02, etc.)
5. Add prev/next navigation links
```

---

## Strategy 3: Hierarchical Sharding

### Description

Create nested directory structure mirroring document hierarchy. Used for complex, multi-level documents.

### When to Use

- Document has deep hierarchy (H1 → H2 → H3 → H4)
- Many subsections under each section
- Need to maintain hierarchical relationships
- Large document (5,000+ lines)

### Characteristics

```
✅ Preserves document hierarchy
✅ Clear parent-child relationships
✅ Scales to very large documents
⚠️ More complex directory structure
⚠️ Deeper navigation required
⚠️ Harder to get overview
```

### Example

```markdown
Original Document (8,000 lines):
# API Documentation
## 1. Getting Started (200 lines)
## 2. Authentication (300 lines)
## 3. Resources (6,000 lines)
### 3.1 Users
#### 3.1.1 Get User
#### 3.1.2 Create User
#### 3.1.3 Update User
#### 3.1.4 Delete User
### 3.2 Products
#### 3.2.1 Get Product
... (50 more endpoints)
## 4. Webhooks (500 lines)
## 5. Errors (1,000 lines)

Hierarchical Sharding:
api-docs-shards/
├── index.md
├── getting-started.md
├── authentication.md
├── resources/
│   ├── README.md (overview of all resources)
│   ├── users/
│   │   ├── README.md (users resource overview)
│   │   ├── get-user.md
│   │   ├── create-user.md
│   │   ├── update-user.md
│   │   └── delete-user.md
│   ├── products/
│   │   ├── README.md
│   │   ├── get-product.md
│   │   └── ... (10 more)
│   └── ... (10 more resources)
├── webhooks.md
└── errors.md

Result:
- 80+ shards
- 3-level directory depth
- Each endpoint is separate file
- README at each level for overview
```

### Implementation

```
1. Identify hierarchy levels (H1, H2, H3, H4)
2. Create directory for each H2 section
3. Create subdirectory for each H3 section (if >3 subsections)
4. Create individual shards for H4 sections
5. Add README.md at each directory level
6. Maintain breadcrumb navigation
```

---

## Strategy 4: Semantic Sharding (Advanced)

### Description

Group content by semantic similarity, even if in different sections. Requires content analysis.

### When to Use

- Document has scattered related content
- Need topic-based reorganization
- Advanced use case (AI-powered analysis)
- Document structure doesn't match logical grouping

### Characteristics

```
✅ Groups truly related content
✅ May improve organization over original
✅ Topic-focused navigation
⚠️ Requires NLP/AI analysis
⚠️ May deviate from original structure
⚠️ More complex to implement
```

### Example

```markdown
Original Document (scattered topics):
# Engineering Handbook
## Section 1: Development Process
... mentions testing best practices
... mentions code review guidelines
## Section 5: Quality Assurance
... more testing best practices
... mentions code review tools
## Section 8: Team Guidelines
... code review workflow
... testing responsibilities

Semantic Sharding (by topic):
handbook-shards/
├── index.md
├── topics/
│   ├── testing-guide.md (combines content from Sections 1, 5, 8)
│   ├── code-review-guide.md (combines content from Sections 1, 5, 8)
│   ├── deployment-guide.md
│   └── ... (10 more topics)
└── original-structure/
    └── ... (preserve original for reference)

Result:
- Content reorganized by topic
- More coherent than original
- May confuse users expecting original structure
```

### Implementation

```
1. Extract all content segments
2. Analyze semantic similarity (NLP embeddings)
3. Cluster related segments
4. Create topic-based shards
5. Preserve original structure in separate directory
6. Document reorganization rationale
```

---

## Strategy 5: Feature-Based Sharding

### Description

Specific to product documents (PRDs, specs). One shard per feature or component.

### When to Use

- Product/feature documentation
- Each feature is independent
- Need per-feature navigation
- Features will evolve independently

### Characteristics

```
✅ Clear feature boundaries
✅ Easy to update individual features
✅ Parallel team work (one feature per team)
✅ Scalable (add features = add shards)
⚠️ Requires clear feature definitions
⚠️ Cross-feature dependencies need careful tracking
```

### Example

```markdown
Original PRD (4,000 lines):
# Product Requirements Document
## Features
### Authentication (400 lines)
### Dashboard (600 lines)
### Reporting (800 lines)
### User Management (300 lines)
### Notifications (200 lines)
... (15 more features)

Feature-Based Sharding:
prd-shards/
├── index.md
├── overview.md (executive summary, vision)
├── features/
│   ├── README.md (feature index)
│   ├── authentication.md (400 lines)
│   ├── dashboard.md (600 lines)
│   ├── reporting.md (800 lines)
│   ├── user-management.md (300 lines)
│   ├── notifications.md (200 lines)
│   └── ... (15 more)
├── technical/
│   ├── architecture.md
│   ├── security.md
│   └── performance.md
└── metrics/
    └── success-metrics.md

Result:
- 20+ feature shards
- Features isolated (easy to update)
- Clear ownership (team per feature)
```

### Implementation

```
1. Identify all features in document
2. Extract each feature to separate shard
3. Create features/ directory
4. Add feature index (README.md)
5. Track cross-feature dependencies in metadata
6. Create separate directories for non-feature content
```

---

## Strategy Comparison Matrix

| Strategy | Best For | Pros | Cons | Complexity |
|----------|----------|------|------|------------|
| **Logical** | Structured documents | Semantic integrity, intuitive | Variable shard sizes | LOW |
| **Size-Based** | Unstructured documents | Consistent sizes, simple | May split topics | LOW |
| **Hierarchical** | Deep, nested documents | Preserves hierarchy | Complex structure | MEDIUM |
| **Semantic** | Scattered related content | Optimal grouping | Requires AI, complex | HIGH |
| **Feature-Based** | Product/feature docs | Clear boundaries, scalable | Needs clear features | LOW-MEDIUM |

---

## Strategy Selection Decision Tree

```
START: What type of document?

├─ Product/Feature Documentation?
│  └─ YES → Use Feature-Based Sharding
│  └─ NO → Continue
│
├─ Document has clear structure (headings)?
│  └─ YES → Use Logical Sharding
│  └─ NO → Continue
│
├─ Document has deep hierarchy (3+ levels)?
│  └─ YES → Use Hierarchical Sharding
│  └─ NO → Continue
│
├─ Content scattered across sections (related topics apart)?
│  └─ YES → Consider Semantic Sharding (advanced)
│  └─ NO → Continue
│
└─ Default: Use Size-Based Sharding
```

---

## Hybrid Strategies

### Logical + Size-Based

```
Apply logical sharding first, then:
- If shard exceeds max_size (e.g., 1,000 lines)
- Apply size-based sub-sharding
- Create subdirectory for sub-shards

Example:
features/
├── authentication.md (300 lines) ✅ Fits
├── reporting/
│   ├── README.md (overview)
│   ├── reporting-part-01.md (500 lines)
│   ├── reporting-part-02.md (500 lines)
│   └── reporting-part-03.md (400 lines)
└── dashboard.md (450 lines) ✅ Fits
```

### Hierarchical + Feature-Based

```
Combine hierarchy for structure, features for organization:

api-docs/
├── authentication/ (hierarchical)
│   ├── oauth.md
│   └── api-keys.md
├── resources/ (feature-based)
│   ├── users/
│   │   ├── endpoints.md
│   │   └── examples.md
│   └── products/
│       ├── endpoints.md
│       └── examples.md
└── webhooks/ (hierarchical)
    ├── setup.md
    └── events.md
```

---

## Strategy Recommendations by Document Type

### PRDs (Product Requirements Documents)
**Recommended:** Feature-Based + Logical
```
- Logical sharding for: Executive, Personas, Market Analysis
- Feature-based for: All features (one shard per feature)
- Result: Clean separation, easy feature updates
```

### API Documentation
**Recommended:** Hierarchical + Feature-Based
```
- Hierarchical for: Resource organization (users, products, orders)
- Feature-based within resources (GET/POST/PUT/DELETE as separate files if large)
- Result: Clear API structure, easy endpoint discovery
```

### Architecture Docs
**Recommended:** Logical + Hierarchical
```
- Logical for: Top-level (Overview, Components, Deployment)
- Hierarchical for: Components (Frontend, Backend, Database as subdirs)
- Result: Mirrors actual system architecture
```

### User Manuals / Guides
**Recommended:** Logical + Size-Based
```
- Logical for: Major sections (Getting Started, Features, Troubleshooting)
- Size-based for: Long narrative sections (if exceed 500 lines)
- Result: Easy chapter-based navigation
```

### Research Reports
**Recommended:** Logical or Size-Based
```
- Logical if: Clear sections (Introduction, Methods, Findings, Conclusion)
- Size-based if: Continuous narrative with few headings
- Result: Readable chunks, clear progression
```

---

## Implementation Guidelines

### For Each Strategy

**Logical Sharding:**
```python
def logical_shard(document):
    sections = parse_headings(document, levels=[1, 2])
    shards = []
    for section in sections:
        if section.line_count > 500:
            # Large section, split by subsections
            subsections = parse_headings(section, levels=[3])
            for subsection in subsections:
                shards.append(create_shard(subsection))
        else:
            shards.append(create_shard(section))
    return shards
```

**Size-Based Sharding:**
```python
def size_based_shard(document, max_size=500):
    shards = []
    current_shard = []
    for line in document.lines:
        current_shard.append(line)
        if len(current_shard) >= max_size:
            # Find nearest heading within next 50 lines
            split_point = find_nearest_heading(document, line_num, lookahead=50)
            shards.append(create_shard(current_shard[:split_point]))
            current_shard = current_shard[split_point:]
    if current_shard:
        shards.append(create_shard(current_shard))
    return shards
```

---

## Best Practices

1. **Start with Logical** - Default to logical sharding if document is structured
2. **Consistent Naming** - Use descriptive names, not generic (part-01, part-02)
3. **Preserve Context** - Each shard should make sense standalone
4. **Balance Sizes** - Aim for 100-500 lines per shard (sweet spot)
5. **Document Strategy** - Note which strategy used in index.md
6. **Test Navigation** - Ensure users can find content easily
7. **Validate Links** - All cross-references must work after sharding
8. **Consider Audience** - Choose strategy based on how users will navigate

---

**Sharding Strategies - Part of shard-document skill**
**Use this guide to select the optimal sharding approach for your document**
