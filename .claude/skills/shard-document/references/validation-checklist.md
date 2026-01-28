# Validation Checklist

## Overview

Comprehensive validation ensures sharded documents maintain integrity, with working links, complete metadata, and logical organization. This checklist covers all validation steps.

---

## Pre-Sharding Validation

### Source Document Check

- [ ] Source document exists and is readable
- [ ] Source document has clear structure (headings)
- [ ] Source document size justifies sharding (>1,000 lines recommended)
- [ ] Source document can be parsed successfully
- [ ] Output directory exists or can be created
- [ ] Permission to write to output directory

---

## Sharding Validation

### Shard Creation

- [ ] All expected shards created
- [ ] Shard count matches sharding plan
- [ ] Each shard has meaningful content (not empty)
- [ ] Shard sizes within acceptable range (50-1,000 lines)
- [ ] Directory structure matches plan
- [ ] File naming follows conventions

### Content Integrity

- [ ] All content from source document included
- [ ] No content duplicated across shards
- [ ] No content lost during sharding
- [ ] Code blocks preserved intact
- [ ] Tables preserved intact
- [ ] Lists preserved intact
- [ ] Formatting preserved (bold, italic, etc.)
- [ ] Images/media references preserved

### Heading Hierarchy

- [ ] Heading levels adjusted correctly (if needed)
- [ ] Each shard starts with H1 heading
- [ ] No orphaned headings (H3 without H2)
- [ ] Heading hierarchy logical within each shard

---

## Metadata Validation

### Required Fields

- [ ] All shards have YAML frontmatter
- [ ] `shard_id` present in all shards
- [ ] `shard_type` present in all shards
- [ ] `parent` present in all shards
- [ ] `section` present in all shards
- [ ] `created_from` present in all shards

### Field Validity

- [ ] All `shard_id` values are unique
- [ ] All `shard_type` values use standard types
- [ ] All `parent` values reference valid documents
- [ ] All `created_from` paths are valid
- [ ] Timestamps in ISO 8601 format (if present)
- [ ] Version numbers follow semver (if present)

### Relationships

- [ ] All `related` shards exist
- [ ] All `dependencies` shards exist
- [ ] No circular dependencies
- [ ] Dependency graph is acyclic
- [ ] Related links include proper paths
- [ ] Tags are lowercase and consistent

---

## Link Validation

### Internal Links

- [ ] All `[text](filename.md)` links point to existing files
- [ ] All `[text](filename.md#anchor)` anchors exist in target files
- [ ] All relative paths are correct (`../parent/file.md`)
- [ ] Links from subdirectories use correct relative paths
- [ ] No broken links to non-existent files
- [ ] No broken links to non-existent anchors

### Cross-References

- [ ] All cross-references from original preserved
- [ ] Cross-reference formats updated (relative paths)
- [ ] Cross-shard references work correctly
- [ ] References to external URLs still valid

### Navigation Links

- [ ] Index links to all shards
- [ ] All "Back to Index" links work
- [ ] Sequential prev/next links work
- [ ] Breadcrumb links work
- [ ] Related document links work
- [ ] Parent section links work

---

## Navigation Validation

### Index File

- [ ] index.md exists in root directory
- [ ] Index lists all shards
- [ ] Index has table of contents
- [ ] Index has reading paths (if applicable)
- [ ] Index has tag-based navigation (if applicable)
- [ ] Index provides overview of shards

### Directory Navigation

- [ ] README.md exists in each subdirectory
- [ ] Directory READMEs list contained shards
- [ ] Directory READMEs link back to parent
- [ ] Directory structure is intuitive

### Sequential Navigation

- [ ] First shard identified
- [ ] Last shard identified
- [ ] All middle shards have prev/next
- [ ] Reading order is logical
- [ ] No gaps in sequence

---

## Content Validation

### Completeness

- [ ] Each shard is self-contained (understandable alone)
- [ ] No dangling references (context missing)
- [ ] All acronyms defined or linked to glossary
- [ ] All technical terms explained or referenced
- [ ] Prerequisites clearly stated

### Consistency

- [ ] Terminology consistent across shards
- [ ] Formatting style consistent
- [ ] Heading style consistent
- [ ] Navigation pattern consistent
- [ ] Metadata format consistent

### Readability

- [ ] Shard sizes manageable (100-500 lines ideal)
- [ ] Each shard has clear purpose
- [ ] Shard titles are descriptive
- [ ] Content flows logically within shard
- [ ] No abrupt starts or endings

---

## Technical Validation

### File System

```bash
# Check all files exist
find . -name "*.md" -type f

# Check for empty files
find . -name "*.md" -empty

# Check file permissions
ls -la *.md

# Check directory structure
tree -L 3
```

### Link Validation Script

```bash
# Find all markdown links
grep -roh '\[.*\](.*\.md[^)]*)' *.md

# Check each link target exists
for link in $(grep -roh '(.*\.md[^)]*)' *.md | tr -d '()'); do
  if [ ! -f "$link" ]; then
    echo "Broken link: $link"
  fi
done

# Check anchors exist
# (requires parsing markdown headings)
```

### Metadata Extraction

```bash
# Extract all shard_ids
grep -rh "^shard_id:" *.md | sort

# Check for duplicates
grep -rh "^shard_id:" *.md | sort | uniq -d

# Extract all tags
grep -rA 10 "^tags:" *.md
```

---

## User Acceptance Validation

### Test Navigation Paths

**Path 1: Index to Shard**
- [ ] Click link from index
- [ ] Reaches correct shard
- [ ] Content loads properly

**Path 2: Sequential Reading**
- [ ] Start at first shard
- [ ] Click "Next" repeatedly
- [ ] Reaches all shards in order
- [ ] Ends at last shard

**Path 3: Related Content**
- [ ] Click "Related" link
- [ ] Reaches related shard
- [ ] Content is actually related
- [ ] Can return to original shard

**Path 4: Search by Tag**
- [ ] Find tag in index
- [ ] Click tagged shard
- [ ] Shard has correct tag
- [ ] Related shards share tag

### Test Edge Cases

- [ ] Navigate from deeply nested shard to root
- [ ] Navigate between different subdirectories
- [ ] Open shard directly (not from index)
- [ ] Follow dependency chain
- [ ] Test circular navigation (index → shard → index)

---

## Quality Validation

### Documentation Quality

- [ ] Each shard has clear title
- [ ] Purpose stated at beginning
- [ ] Examples included (where applicable)
- [ ] Code examples formatted correctly
- [ ] Tables formatted correctly
- [ ] Lists formatted correctly

### Metadata Quality

- [ ] Tags are specific and useful
- [ ] Dependencies are necessary (not over-specified)
- [ ] Related links add value
- [ ] Status reflects current state
- [ ] Version incremented appropriately

---

## Validation Report Template

```markdown
# Shard Validation Report

**Document:** [Original Document Name]
**Sharding Date:** [Date]
**Strategy:** [Logical/Size-Based/etc.]

---

## Summary

**Total Shards:** [N]
**Validation Status:** ✅ PASSED / ⚠️ WARNINGS / ❌ FAILED

---

## Validation Results

### Shard Creation
- ✅ [N] shards created (expected: [N])
- ✅ All shards have content
- ✅ Shard sizes: [min]-[max] lines (avg: [avg])

### Metadata
- ✅ Required fields: [N]/[N] complete
- ✅ shard_id uniqueness: No duplicates
- ⚠️ Tags: 2 shards missing tags

### Links
- ✅ Internal links: [N]/[N] valid
- ❌ Broken links: [N] found
  - [file.md]: Link to [missing.md] not found
- ✅ Cross-references: [N]/[N] valid

### Navigation
- ✅ Index links: [N]/[N] working
- ✅ Sequential navigation: Complete chain
- ✅ Breadcrumbs: All valid

### Content
- ✅ Content integrity: 100% preserved
- ✅ Formatting: All preserved
- ✅ Completeness: All shards self-contained

---

## Issues Found

### Critical (Must Fix)
1. ❌ Broken link in authentication.md → missing.md
2. ❌ Circular dependency: A → B → A

### Warnings (Should Fix)
1. ⚠️ personas.md has only 1 tag (recommend 3-5)
2. ⚠️ Large shard: technical-requirements.md (1,200 lines)

### Suggestions (Nice to Have)
1. 💡 Add glossary shard for technical terms
2. 💡 Add reading time estimates
3. 💡 Consider splitting large shards

---

## Recommendations

1. **Fix broken link** in authentication.md before publishing
2. **Resolve circular dependency** between A and B
3. **Add tags** to personas.md for better discovery
4. **Consider splitting** technical-requirements.md (>1,000 lines)
5. **Add glossary** for technical terminology

---

## Sign-Off

**Validated By:** [Name]
**Date:** [Date]
**Status:** [Ready for Use / Needs Fixes]
```

---

## Automated Validation Script Example

```python
import os
import re
import yaml
from pathlib import Path

class ShardValidator:
    def __init__(self, shards_dir):
        self.shards_dir = Path(shards_dir)
        self.shards = list(self.shards_dir.glob('**/*.md'))
        self.errors = []
        self.warnings = []

    def validate_all(self):
        """Run all validation checks"""
        self.validate_metadata()
        self.validate_links()
        self.validate_navigation()
        self.generate_report()

    def validate_metadata(self):
        """Check metadata completeness"""
        required_fields = ['shard_id', 'shard_type', 'parent', 'section', 'created_from']
        shard_ids = set()

        for shard in self.shards:
            metadata = self.extract_metadata(shard)

            if not metadata:
                self.errors.append(f"{shard.name}: Missing metadata")
                continue

            # Check required fields
            for field in required_fields:
                if field not in metadata:
                    self.errors.append(f"{shard.name}: Missing required field '{field}'")

            # Check uniqueness
            shard_id = metadata.get('shard_id')
            if shard_id in shard_ids:
                self.errors.append(f"{shard.name}: Duplicate shard_id '{shard_id}'")
            shard_ids.add(shard_id)

            # Check tags
            tags = metadata.get('tags', [])
            if len(tags) < 1:
                self.warnings.append(f"{shard.name}: No tags defined")

    def validate_links(self):
        """Check all markdown links"""
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

        for shard in self.shards:
            with open(shard, 'r') as f:
                content = f.read()

            links = re.findall(link_pattern, content)

            for text, target in links:
                # Skip external links
                if target.startswith('http'):
                    continue

                # Check file exists
                target_file = target.split('#')[0]
                if target_file:
                    full_path = (shard.parent / target_file).resolve()
                    if not full_path.exists():
                        self.errors.append(f"{shard.name}: Broken link to {target}")

    def validate_navigation(self):
        """Check index.md exists"""
        index_path = self.shards_dir / 'index.md'
        if not index_path.exists():
            self.errors.append("Missing index.md in root directory")

    def extract_metadata(self, file_path):
        """Extract YAML frontmatter"""
        with open(file_path, 'r') as f:
            content = f.read()

        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None

        return yaml.safe_load(match.group(1))

    def generate_report(self):
        """Print validation report"""
        print("=" * 60)
        print("SHARD VALIDATION REPORT")
        print("=" * 60)
        print(f"\nTotal Shards: {len(self.shards)}")
        print(f"Errors: {len(self.errors)}")
        print(f"Warnings: {len(self.warnings)}")

        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ ALL CHECKS PASSED")

        status = "FAILED" if self.errors else ("WARNINGS" if self.warnings else "PASSED")
        print(f"\nValidation Status: {status}")
        print("=" * 60)

# Usage
validator = ShardValidator('prd-shards/')
validator.validate_all()
```

---

## Quick Validation Commands

```bash
# Count shards
find . -name "*.md" -type f | wc -l

# Find empty files
find . -name "*.md" -empty

# Check for duplicate shard_ids
grep -rh "^shard_id:" **/*.md | sort | uniq -d

# Find broken links (simple check)
grep -roh '](.*\.md[^)]*)' **/*.md | tr -d '()' | while read link; do
  [ ! -f "$link" ] && echo "Broken: $link"
done

# Verify index exists
[ -f index.md ] && echo "✅ Index exists" || echo "❌ Index missing"

# Check metadata presence
find . -name "*.md" -exec grep -L "^---$" {} \; | head
```

---

## Best Practices

1. **Validate Early** - Check during sharding, not just at end
2. **Automate Checks** - Use scripts for repeatable validation
3. **Test Navigation** - Actually click through links
4. **Verify Metadata** - Don't assume it's correct
5. **Check Edge Cases** - Deeply nested paths, special characters
6. **Generate Reports** - Document validation results
7. **Fix Errors First** - Address critical issues before warnings
8. **Re-Validate After Fixes** - Ensure fixes didn't break anything
9. **Version Control** - Track validation results over time
10. **User Test** - Have someone unfamiliar navigate

---

**Validation Checklist - Part of shard-document skill**
**Use this checklist to ensure sharded documents maintain integrity**
