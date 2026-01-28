#!/usr/bin/env python3
"""
BMAD Enhanced - Skill Loading Monitor

Monitor and validate that all skills are properly loaded and accessible.
Provides visibility into skill loading status, errors, and diagnostics.
"""

import os
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import re


@dataclass
class SkillInfo:
    """Information about a skill"""
    name: str
    category: str
    path: str
    exists: bool
    valid: bool
    has_frontmatter: bool
    frontmatter: Dict
    size_bytes: int
    line_count: int
    errors: List[str]


class SkillMonitor:
    """Monitor skill loading and validation"""

    def __init__(self, skills_dir: str = ".claude/skills"):
        self.skills_dir = Path(skills_dir)
        self.skills: List[SkillInfo] = []
        self.categories: Dict[str, List[str]] = {}

    def discover_skills(self) -> int:
        """Discover all skills in the skills directory"""
        print(f"🔍 Discovering skills in {self.skills_dir}...")

        if not self.skills_dir.exists():
            print(f"❌ Skills directory not found: {self.skills_dir}")
            return 0

        skill_files = list(self.skills_dir.rglob("SKILL.md"))
        print(f"📁 Found {len(skill_files)} skill definition files\n")

        for skill_file in sorted(skill_files):
            skill_info = self._analyze_skill(skill_file)
            self.skills.append(skill_info)

            # Organize by category
            if skill_info.category not in self.categories:
                self.categories[skill_info.category] = []
            self.categories[skill_info.category].append(skill_info.name)

        return len(self.skills)

    def _analyze_skill(self, skill_file: Path) -> SkillInfo:
        """Analyze a single skill file"""
        # Extract category and name from path
        # Expected: .claude/skills/category/skill-name/SKILL.md
        parts = skill_file.parts
        try:
            skills_idx = parts.index("skills")
            category = parts[skills_idx + 1]
            skill_name = parts[skills_idx + 2]
        except (ValueError, IndexError):
            category = "unknown"
            skill_name = skill_file.parent.name

        errors = []
        frontmatter = {}
        has_frontmatter = False

        # Read and analyze file
        try:
            content = skill_file.read_text(encoding='utf-8')
            size_bytes = skill_file.stat().st_size
            line_count = len(content.splitlines())

            # Extract YAML frontmatter
            if content.startswith('---'):
                match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                if match:
                    try:
                        frontmatter = yaml.safe_load(match.group(1))
                        has_frontmatter = True

                        # Validate required fields
                        required_fields = ['name', 'description', 'category']
                        for field in required_fields:
                            if field not in frontmatter:
                                errors.append(f"Missing required field: {field}")

                    except yaml.YAMLError as e:
                        errors.append(f"Invalid YAML frontmatter: {e}")
                else:
                    errors.append("Frontmatter markers found but content invalid")
            else:
                errors.append("No YAML frontmatter found")

            # Check for workflow steps
            if "## Workflow Steps" not in content and "## Workflow" not in content:
                errors.append("No workflow steps section found")

        except Exception as e:
            errors.append(f"Error reading file: {e}")
            size_bytes = 0
            line_count = 0

        valid = len(errors) == 0

        # Get relative path, handling any path issues
        try:
            rel_path = str(skill_file.relative_to(Path.cwd()))
        except ValueError:
            rel_path = str(skill_file)

        return SkillInfo(
            name=skill_name,
            category=category,
            path=rel_path,
            exists=skill_file.exists(),
            valid=valid,
            has_frontmatter=has_frontmatter,
            frontmatter=frontmatter,
            size_bytes=size_bytes,
            line_count=line_count,
            errors=errors
        )

    def print_summary(self):
        """Print summary of skill loading status"""
        total = len(self.skills)
        valid = sum(1 for s in self.skills if s.valid)
        invalid = total - valid
        with_frontmatter = sum(1 for s in self.skills if s.has_frontmatter)

        print("=" * 70)
        print("📊 SKILL LOADING SUMMARY")
        print("=" * 70)
        print()
        print(f"Total Skills Discovered:  {total}")
        print(f"Valid Skills:             {valid} ✅")
        print(f"Invalid Skills:           {invalid} {'❌' if invalid > 0 else '✅'}")
        print(f"With YAML Frontmatter:    {with_frontmatter}")
        print(f"Categories:               {len(self.categories)}")
        print()

        if invalid > 0:
            print(f"⚠️  {invalid} skills have issues that need attention")
        else:
            print("✅ All skills are valid and properly formatted!")
        print()

    def print_by_category(self):
        """Print skills organized by category"""
        print("=" * 70)
        print("📁 SKILLS BY CATEGORY")
        print("=" * 70)
        print()

        for category in sorted(self.categories.keys()):
            skills = self.categories[category]
            print(f"📂 {category.upper()} ({len(skills)} skills)")

            # Get skill details for this category
            category_skills = [s for s in self.skills if s.category == category]

            for skill in sorted(category_skills, key=lambda s: s.name):
                status = "✅" if skill.valid else "❌"
                size_kb = skill.size_bytes / 1024
                print(f"  {status} {skill.name:<30} ({skill.line_count:>4} lines, {size_kb:>6.1f} KB)")

                if not skill.valid:
                    for error in skill.errors:
                        print(f"      ⚠️  {error}")

            print()

    def print_invalid_skills(self):
        """Print details of invalid skills"""
        invalid = [s for s in self.skills if not s.valid]

        if not invalid:
            return

        print("=" * 70)
        print("❌ INVALID SKILLS - DETAILS")
        print("=" * 70)
        print()

        for skill in invalid:
            print(f"Skill: {skill.name}")
            print(f"Path:  {skill.path}")
            print(f"Category: {skill.category}")
            print(f"Errors:")
            for error in skill.errors:
                print(f"  • {error}")
            print()

    def print_statistics(self):
        """Print detailed statistics"""
        if not self.skills:
            return

        total_lines = sum(s.line_count for s in self.skills)
        total_size = sum(s.size_bytes for s in self.skills)
        avg_lines = total_lines / len(self.skills)
        avg_size = total_size / len(self.skills)

        print("=" * 70)
        print("📈 STATISTICS")
        print("=" * 70)
        print()
        print(f"Total Lines:        {total_lines:,}")
        print(f"Total Size:         {total_size / 1024:.1f} KB")
        print(f"Average Lines:      {avg_lines:.0f} lines/skill")
        print(f"Average Size:       {avg_size / 1024:.1f} KB/skill")
        print()

        # Largest skills
        print("Largest Skills:")
        largest = sorted(self.skills, key=lambda s: s.line_count, reverse=True)[:5]
        for skill in largest:
            print(f"  • {skill.name:<30} {skill.line_count:>4} lines")
        print()

    def export_json(self, output_file: str):
        """Export skill information to JSON"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_skills": len(self.skills),
                "valid_skills": sum(1 for s in self.skills if s.valid),
                "invalid_skills": sum(1 for s in self.skills if not s.valid),
                "categories": len(self.categories)
            },
            "categories": self.categories,
            "skills": [asdict(s) for s in self.skills]
        }

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"📄 Exported skill information to {output_file}")

    def validate_all(self) -> bool:
        """Validate all skills and return True if all valid"""
        invalid = [s for s in self.skills if not s.valid]
        return len(invalid) == 0

    def get_skill_by_name(self, name: str) -> Optional[SkillInfo]:
        """Get skill by name"""
        for skill in self.skills:
            if skill.name == name:
                return skill
        return None


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Monitor and validate BMAD Enhanced skill loading"
    )
    parser.add_argument(
        "--skills-dir",
        default=".claude/skills",
        help="Skills directory (default: .claude/skills)"
    )
    parser.add_argument(
        "--json",
        metavar="FILE",
        help="Export results to JSON file"
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate, exit 0 if all valid, 1 if any invalid"
    )
    parser.add_argument(
        "--category",
        help="Filter by category"
    )
    parser.add_argument(
        "--skill",
        help="Show details for specific skill"
    )

    args = parser.parse_args()

    # Initialize monitor
    monitor = SkillMonitor(args.skills_dir)

    # Discover skills
    count = monitor.discover_skills()

    if count == 0:
        print("❌ No skills found!")
        return 1

    # If specific skill requested
    if args.skill:
        skill = monitor.get_skill_by_name(args.skill)
        if skill:
            print(f"\n📋 Skill Details: {skill.name}")
            print(f"Category:     {skill.category}")
            print(f"Path:         {skill.path}")
            print(f"Valid:        {'✅ Yes' if skill.valid else '❌ No'}")
            print(f"Frontmatter:  {'✅ Yes' if skill.has_frontmatter else '❌ No'}")
            print(f"Size:         {skill.size_bytes / 1024:.1f} KB")
            print(f"Lines:        {skill.line_count}")

            if skill.has_frontmatter and skill.frontmatter:
                print(f"\nFrontmatter:")
                for key, value in skill.frontmatter.items():
                    print(f"  {key}: {value}")

            if skill.errors:
                print(f"\nErrors:")
                for error in skill.errors:
                    print(f"  • {error}")
        else:
            print(f"❌ Skill not found: {args.skill}")
            return 1
        return 0

    # Filter by category if requested
    if args.category:
        monitor.skills = [s for s in monitor.skills if s.category == args.category]
        if not monitor.skills:
            print(f"❌ No skills found in category: {args.category}")
            return 1

    # Validate only mode
    if args.validate_only:
        valid = monitor.validate_all()
        if valid:
            print("✅ All skills are valid")
            return 0
        else:
            invalid_count = sum(1 for s in monitor.skills if not s.valid)
            print(f"❌ {invalid_count} invalid skills found")
            return 1

    # Print reports
    monitor.print_summary()
    monitor.print_by_category()
    monitor.print_invalid_skills()
    monitor.print_statistics()

    # Export JSON if requested
    if args.json:
        monitor.export_json(args.json)

    # Exit with error if any skills invalid
    return 0 if monitor.validate_all() else 1


if __name__ == "__main__":
    sys.exit(main())
