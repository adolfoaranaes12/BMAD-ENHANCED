#!/usr/bin/env python3
"""
Extract technology stack from codebase package.json files.

Automatically discovers:
- Frontend frameworks and libraries
- Backend frameworks and libraries
- Database ORMs and clients
- Testing frameworks
- Build tools
- DevOps tools

Usage:
    python extract_tech_stack.py --codebase <path> --output <format>

Examples:
    # Extract tech stack from monorepo
    python extract_tech_stack.py --codebase . --output json

    # Extract from specific package
    python extract_tech_stack.py --codebase packages/backend --output text
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List


def parse_package_json(package_json_path: Path) -> Dict[str, Any]:
    """
    Parse package.json file and extract dependencies.

    Returns:
        {
            'dependencies': {...},
            'devDependencies': {...},
            'name': '...',
            'version': '...'
        }
    """
    try:
        with open(package_json_path, 'r') as f:
            data = json.load(f)
            return {
                'name': data.get('name', 'unknown'),
                'version': data.get('version', 'unknown'),
                'dependencies': data.get('dependencies', {}),
                'devDependencies': data.get('devDependencies', {})
            }
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return {
            'name': 'unknown',
            'version': 'unknown',
            'dependencies': {},
            'devDependencies': {},
            'error': str(e)
        }


def categorize_dependencies(dependencies: Dict[str, str]) -> Dict[str, List[Dict[str, str]]]:
    """
    Categorize dependencies by technology type.

    Returns:
        {
            'frontend_frameworks': [...],
            'ui_libraries': [...],
            'state_management': [...],
            'backend_frameworks': [...],
            'database': [...],
            'testing': [...],
            ...
        }
    """
    categories = {
        'frontend_frameworks': [],
        'ui_libraries': [],
        'state_management': [],
        'data_fetching': [],
        'routing': [],
        'styling': [],
        'backend_frameworks': [],
        'database': [],
        'caching': [],
        'job_queues': [],
        'authentication': [],
        'validation': [],
        'testing': [],
        'build_tools': [],
        'type_checking': [],
        'linting': [],
        'other': []
    }

    # Frontend frameworks
    frontend_frameworks = ['react', 'vue', 'angular', 'svelte', 'next', 'remix', 'nuxt', 'sveltekit']
    # UI libraries
    ui_libraries = ['@mui/material', 'antd', 'chakra-ui', 'shadcn', '@radix-ui', 'mantine']
    # State management
    state_management = ['redux', 'zustand', 'recoil', 'jotai', 'mobx', 'pinia', 'vuex']
    # Data fetching
    data_fetching = ['@tanstack/react-query', 'swr', '@apollo/client', 'axios', 'ky']
    # Routing
    routing = ['react-router', 'react-router-dom', 'vue-router', '@angular/router']
    # Styling
    styling = ['tailwindcss', '@emotion/react', 'styled-components', 'sass']
    # Backend frameworks
    backend_frameworks = ['express', '@nestjs/core', 'fastify', 'koa', 'hapi']
    # Database
    database = ['@prisma/client', 'prisma', 'typeorm', 'mongoose', 'sequelize', 'drizzle-orm', 'pg', 'mysql2']
    # Caching
    caching = ['redis', 'ioredis', 'memcached']
    # Job queues
    job_queues = ['bull', 'inngest', 'agenda', 'bee-queue']
    # Authentication
    authentication = ['@clerk/nextjs', 'passport', 'jsonwebtoken', 'auth0', '@supabase/supabase-js']
    # Validation
    validation = ['zod', 'joi', 'yup', 'ajv', 'class-validator']
    # Testing
    testing = ['vitest', 'jest', '@playwright/test', 'cypress', 'mocha', 'chai']
    # Build tools
    build_tools = ['vite', 'webpack', 'rollup', 'esbuild', 'turbopack', '@swc/core']
    # Type checking
    type_checking = ['typescript', '@types/node', '@types/react']
    # Linting
    linting = ['eslint', 'prettier', '@typescript-eslint/parser']

    for dep, version in dependencies.items():
        dep_lower = dep.lower()
        added = False

        # Check each category
        if any(fw in dep_lower for fw in frontend_frameworks):
            categories['frontend_frameworks'].append({'name': dep, 'version': version})
            added = True
        if any(ui in dep_lower for ui in ui_libraries):
            categories['ui_libraries'].append({'name': dep, 'version': version})
            added = True
        if any(sm in dep_lower for sm in state_management):
            categories['state_management'].append({'name': dep, 'version': version})
            added = True
        if any(df in dep_lower for df in data_fetching):
            categories['data_fetching'].append({'name': dep, 'version': version})
            added = True
        if any(r in dep_lower for r in routing):
            categories['routing'].append({'name': dep, 'version': version})
            added = True
        if any(s in dep_lower for s in styling):
            categories['styling'].append({'name': dep, 'version': version})
            added = True
        if any(bf in dep_lower for bf in backend_frameworks):
            categories['backend_frameworks'].append({'name': dep, 'version': version})
            added = True
        if any(db in dep_lower for db in database):
            categories['database'].append({'name': dep, 'version': version})
            added = True
        if any(c in dep_lower for c in caching):
            categories['caching'].append({'name': dep, 'version': version})
            added = True
        if any(jq in dep_lower for jq in job_queues):
            categories['job_queues'].append({'name': dep, 'version': version})
            added = True
        if any(a in dep_lower for a in authentication):
            categories['authentication'].append({'name': dep, 'version': version})
            added = True
        if any(v in dep_lower for v in validation):
            categories['validation'].append({'name': dep, 'version': version})
            added = True
        if any(t in dep_lower for t in testing):
            categories['testing'].append({'name': dep, 'version': version})
            added = True
        if any(bt in dep_lower for bt in build_tools):
            categories['build_tools'].append({'name': dep, 'version': version})
            added = True
        if any(tc in dep_lower for tc in type_checking):
            categories['type_checking'].append({'name': dep, 'version': version})
            added = True
        if any(l in dep_lower for l in linting):
            categories['linting'].append({'name': dep, 'version': version})
            added = True

        if not added:
            categories['other'].append({'name': dep, 'version': version})

    # Remove empty categories
    return {k: v for k, v in categories.items() if v}


def extract_tech_stack(codebase_path: Path) -> Dict[str, Any]:
    """
    Extract complete tech stack from codebase.

    Returns:
        {
            'packages': [...],  # List of found packages
            'tech_stack': {...},  # Categorized dependencies
            'summary': {...}  # High-level summary
        }
    """
    # Find all package.json files
    package_files = list(codebase_path.glob('**/package.json'))

    # Exclude node_modules
    package_files = [p for p in package_files if 'node_modules' not in str(p)]

    if not package_files:
        return {
            'packages': [],
            'tech_stack': {},
            'summary': {'error': 'No package.json files found'},
            'package_count': 0
        }

    packages = []
    all_dependencies = {}
    all_dev_dependencies = {}

    for pkg_file in package_files:
        pkg_data = parse_package_json(pkg_file)
        packages.append({
            'path': str(pkg_file.relative_to(codebase_path)),
            'name': pkg_data['name'],
            'version': pkg_data['version']
        })

        # Merge dependencies
        all_dependencies.update(pkg_data['dependencies'])
        all_dev_dependencies.update(pkg_data['devDependencies'])

    # Categorize all dependencies
    categorized = categorize_dependencies({**all_dependencies, **all_dev_dependencies})

    # Create summary
    summary = {
        'package_count': len(packages),
        'total_dependencies': len(all_dependencies),
        'total_dev_dependencies': len(all_dev_dependencies),
        'frontend_detected': len(categorized.get('frontend_frameworks', [])) > 0,
        'backend_detected': len(categorized.get('backend_frameworks', [])) > 0,
        'database_detected': len(categorized.get('database', [])) > 0,
        'testing_detected': len(categorized.get('testing', [])) > 0
    }

    return {
        'packages': packages,
        'tech_stack': categorized,
        'summary': summary,
        'package_count': len(packages)
    }


def format_output(data: Dict[str, Any], output_format: str) -> str:
    """
    Format output based on requested format.

    Args:
        data: Tech stack data
        output_format: 'json' or 'text'

    Returns:
        Formatted string
    """
    if output_format == 'json':
        return json.dumps(data, indent=2)

    # Text format
    lines = []
    lines.append("=== Technology Stack ===")
    lines.append(f"\nPackages Found: {data['package_count']}")

    # Handle error case
    if 'error' in data.get('summary', {}):
        lines.append(f"\nError: {data['summary']['error']}")
        return '\n'.join(lines)

    for pkg in data['packages']:
        lines.append(f"  - {pkg['name']} ({pkg['path']})")

    lines.append(f"\n=== Summary ===")
    summary = data['summary']
    lines.append(f"Total Dependencies: {summary.get('total_dependencies', 0)}")
    lines.append(f"Total Dev Dependencies: {summary.get('total_dev_dependencies', 0)}")
    lines.append(f"Frontend: {'✅' if summary.get('frontend_detected', False) else '❌'}")
    lines.append(f"Backend: {'✅' if summary.get('backend_detected', False) else '❌'}")
    lines.append(f"Database: {'✅' if summary.get('database_detected', False) else '❌'}")
    lines.append(f"Testing: {'✅' if summary.get('testing_detected', False) else '❌'}")

    lines.append(f"\n=== Tech Stack by Category ===")
    for category, items in data['tech_stack'].items():
        category_name = category.replace('_', ' ').title()
        lines.append(f"\n{category_name}:")
        for item in items[:10]:  # Limit to 10 per category
            lines.append(f"  - {item['name']} ({item['version']})")
        if len(items) > 10:
            lines.append(f"  ... and {len(items) - 10} more")

    return '\n'.join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Extract technology stack from codebase',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract tech stack from monorepo
  python extract_tech_stack.py --codebase . --output json

  # Extract from specific package
  python extract_tech_stack.py --codebase packages/backend --output text
        """
    )

    parser.add_argument(
        '--codebase',
        required=True,
        help='Path to codebase root'
    )

    parser.add_argument(
        '--output',
        choices=['json', 'text'],
        default='text',
        help='Output format (default: text)'
    )

    args = parser.parse_args()

    codebase_path = Path(args.codebase).resolve()

    if not codebase_path.exists():
        print(f"Error: Codebase path does not exist: {codebase_path}", file=sys.stderr)
        sys.exit(1)

    # Extract tech stack
    result = extract_tech_stack(codebase_path)

    # Format and print output
    output = format_output(result, args.output)
    print(output)

    return 0


if __name__ == '__main__':
    sys.exit(main())
