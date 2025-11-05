#!/usr/bin/env python3
"""
Parse BMAD commands with type safety and validation.

Provides structured parsing for all BMAD Enhanced commands with:
- Type-safe parameter extraction
- Validation and error messages
- Default value handling
- Help text generation

Usage:
    python parse_command.py <command-name> [args...]

Examples:
    # Parse analyze-architecture command
    python parse_command.py analyze-architecture --depth quick --output json

    # Parse design-architecture command
    python parse_command.py design-architecture docs/prd.md --type fullstack

    # Get help for a command
    python parse_command.py analyze-architecture --help
"""

import sys
import json
import argparse
from typing import Dict, Any, List


def parse_analyze_architecture(args: List[str]) -> Dict[str, Any]:
    """
    Parse analyze-architecture command.

    Syntax:
        /analyze-architecture [codebase-path] [options]

    Options:
        --depth quick|standard|comprehensive  Analysis depth (default: comprehensive)
        --output markdown|json|both          Output format (default: markdown)
        --focus area                         Focus on specific area (default: all)
        --budget N                           Token budget (default: 120000)

    Examples:
        /analyze-architecture  # Comprehensive by default
        /analyze-architecture --depth quick
        /analyze-architecture packages/backend --output json
        /analyze-architecture . --depth standard --focus security
    """
    parser = argparse.ArgumentParser(
        prog='analyze-architecture',
        description='Analyze existing (brownfield) codebase architecture',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        'codebase_path',
        nargs='?',
        default='.',
        help='Path to codebase root (default: current directory)'
    )

    parser.add_argument(
        '--depth',
        choices=['quick', 'standard', 'comprehensive'],
        default='comprehensive',
        help='Analysis depth mode (default: comprehensive)'
    )

    parser.add_argument(
        '--output',
        choices=['markdown', 'json', 'both'],
        default='markdown',
        help='Output format (default: markdown)'
    )

    parser.add_argument(
        '--focus',
        choices=['architecture', 'security', 'performance', 'scalability', 'tech-debt', 'all'],
        default='all',
        help='Focus area for analysis (default: all)'
    )

    parser.add_argument(
        '--budget',
        type=int,
        default=120000,
        help='Token budget in tokens (default: 120000)'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'analyze-architecture',
        'codebase_path': parsed.codebase_path,
        'depth': parsed.depth,
        'output_format': parsed.output,
        'focus_area': parsed.focus,
        'token_budget': parsed.budget,
        'skill': 'analyze-architecture'
    }


def parse_design_architecture(args: List[str]) -> Dict[str, Any]:
    """
    Parse design-architecture command.

    Syntax:
        /design-architecture <requirements-file> [options]

    Options:
        --type frontend|backend|fullstack    System type (default: auto)
        --depth quick|standard|comprehensive Design depth (default: comprehensive)
        --complexity low|medium|high         Complexity level (default: auto)
        --existing <file>                    Existing architecture to extend

    Examples:
        /design-architecture docs/prd.md  # Comprehensive by default
        /design-architecture docs/requirements.md --type backend
        /design-architecture docs/epic.md --depth quick
    """
    parser = argparse.ArgumentParser(
        prog='design-architecture',
        description='Design system architecture from requirements'
    )

    parser.add_argument(
        'requirements_file',
        help='Path to requirements file (PRD, epic, or user story)'
    )

    parser.add_argument(
        '--type',
        choices=['auto', 'frontend', 'backend', 'fullstack'],
        default='auto',
        help='System type (default: auto)'
    )

    parser.add_argument(
        '--depth',
        choices=['quick', 'standard', 'comprehensive'],
        default='comprehensive',
        help='Design depth mode (default: comprehensive)'
    )

    parser.add_argument(
        '--complexity',
        choices=['auto', 'low', 'medium', 'high'],
        default='auto',
        help='System complexity (default: auto)'
    )

    parser.add_argument(
        '--existing',
        help='Path to existing architecture file to extend'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'design-architecture',
        'requirements_file': parsed.requirements_file,
        'system_type': parsed.type,
        'depth': parsed.depth,
        'complexity': parsed.complexity,
        'existing_architecture': parsed.existing,
        'skill': 'design-architecture'
    }


def parse_review_architecture(args: List[str]) -> Dict[str, Any]:
    """
    Parse review-architecture command.

    Syntax:
        /review-architecture <architecture-file> [options]

    Options:
        --focus <area>     Focus area (completeness, quality, security, etc.)
        --depth quick|standard|comprehensive    Review depth (default: comprehensive)

    Examples:
        /review-architecture docs/architecture.md  # Comprehensive by default
        /review-architecture docs/design.md --focus security
        /review-architecture docs/architecture.md --depth quick
    """
    parser = argparse.ArgumentParser(
        prog='review-architecture',
        description='Peer review system architecture'
    )

    parser.add_argument(
        'architecture_file',
        help='Path to architecture document'
    )

    parser.add_argument(
        '--focus',
        choices=['completeness', 'quality', 'security', 'scalability', 'performance', 'cost', 'all'],
        default='all',
        help='Focus area for review (default: all)'
    )

    parser.add_argument(
        '--depth',
        choices=['quick', 'standard', 'comprehensive'],
        default='comprehensive',
        help='Review depth mode (default: comprehensive)'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'review-architecture',
        'architecture_file': parsed.architecture_file,
        'focus_area': parsed.focus,
        'depth': parsed.depth,
        'skill': 'review-architecture'
    }


def parse_validate_story(args: List[str]) -> Dict[str, Any]:
    """
    Parse validate-story command.

    Syntax:
        /validate-story <story-file> [options]

    Options:
        --mode full|quick    Validation depth (default: full)

    Examples:
        /validate-story docs/user-story.md
        /validate-story docs/story-123.md --mode quick
    """
    parser = argparse.ArgumentParser(
        prog='validate-story',
        description='Validate user story specification'
    )

    parser.add_argument(
        'story_file',
        help='Path to user story file'
    )

    parser.add_argument(
        '--mode',
        choices=['full', 'quick'],
        default='full',
        help='Validation mode (default: full)'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'validate-story',
        'story_file': parsed.story_file,
        'validation_mode': parsed.mode,
        'skill': 'validate-story'
    }


def parse_implement(args: List[str]) -> Dict[str, Any]:
    """
    Parse implement command (James).

    Syntax:
        @james *implement <task-spec-file> [options]

    Options:
        --test-first       Write tests before implementation
        --skip-tests       Skip test creation

    Examples:
        @james *implement docs/tasks/task-001.md
        @james *implement docs/story.md --test-first
    """
    parser = argparse.ArgumentParser(
        prog='implement',
        description='Implement feature from task specification'
    )

    parser.add_argument(
        'task_spec_file',
        help='Path to task specification file'
    )

    parser.add_argument(
        '--test-first',
        action='store_true',
        help='Write tests before implementation (TDD)'
    )

    parser.add_argument(
        '--skip-tests',
        action='store_true',
        help='Skip test creation'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'implement',
        'task_spec_file': parsed.task_spec_file,
        'test_first': parsed.test_first,
        'skip_tests': parsed.skip_tests,
        'skill': 'implement-feature',
        'subagent': 'james'
    }


def parse_create_task_spec(args: List[str]) -> Dict[str, Any]:
    """
    Parse create-task-spec command (Alex).

    Syntax:
        @alex *create-task-spec <requirements-file> [options]

    Options:
        --complexity auto|low|medium|high    Complexity assessment (default: auto)

    Examples:
        @alex *create-task-spec docs/user-story.md
        @alex *create-task-spec docs/feature.md --complexity high
    """
    parser = argparse.ArgumentParser(
        prog='create-task-spec',
        description='Create detailed task specification from requirements'
    )

    parser.add_argument(
        'requirements_file',
        help='Path to requirements file'
    )

    parser.add_argument(
        '--complexity',
        choices=['auto', 'low', 'medium', 'high'],
        default='auto',
        help='Complexity assessment (default: auto)'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'create-task-spec',
        'requirements_file': parsed.requirements_file,
        'complexity': parsed.complexity,
        'skill': 'create-task-spec',
        'subagent': 'alex'
    }


def parse_review_code(args: List[str]) -> Dict[str, Any]:
    """
    Parse review-code command (Quinn).

    Syntax:
        @quinn *review-code [file-or-directory] [options]

    Options:
        --focus quality|security|performance|all    Focus area (default: all)
        --depth quick|standard|thorough            Review depth (default: standard)

    Examples:
        @quinn *review-code
        @quinn *review-code src/features/auth
        @quinn *review-code src/api --focus security
    """
    parser = argparse.ArgumentParser(
        prog='review-code',
        description='Code quality and standards review'
    )

    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to file or directory to review (default: current directory)'
    )

    parser.add_argument(
        '--focus',
        choices=['quality', 'security', 'performance', 'all'],
        default='all',
        help='Review focus area (default: all)'
    )

    parser.add_argument(
        '--depth',
        choices=['quick', 'standard', 'thorough'],
        default='standard',
        help='Review depth (default: standard)'
    )

    parsed = parser.parse_args(args)

    return {
        'command': 'review-code',
        'path': parsed.path,
        'focus_area': parsed.focus,
        'review_depth': parsed.depth,
        'skill': 'review-code',
        'subagent': 'quinn'
    }


# Command registry
COMMAND_PARSERS = {
    'analyze-architecture': parse_analyze_architecture,
    'design-architecture': parse_design_architecture,
    'review-architecture': parse_review_architecture,
    'validate-story': parse_validate_story,
    'implement': parse_implement,
    'create-task-spec': parse_create_task_spec,
    'review-code': parse_review_code,
}


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Error: Command name required", file=sys.stderr)
        print("\nAvailable commands:", file=sys.stderr)
        for cmd in COMMAND_PARSERS.keys():
            print(f"  - {cmd}", file=sys.stderr)
        sys.exit(1)

    command_name = sys.argv[1]
    command_args = sys.argv[2:]

    if command_name not in COMMAND_PARSERS:
        print(f"Error: Unknown command: {command_name}", file=sys.stderr)
        print("\nAvailable commands:", file=sys.stderr)
        for cmd in COMMAND_PARSERS.keys():
            print(f"  - {cmd}", file=sys.stderr)
        sys.exit(1)

    try:
        # Parse command
        parser_func = COMMAND_PARSERS[command_name]
        result = parser_func(command_args)

        # Output as JSON
        print(json.dumps(result, indent=2))

        return 0

    except SystemExit as e:
        # argparse calls sys.exit on --help or errors
        # Let it propagate
        raise

    except Exception as e:
        print(f"Error parsing command: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    sys.exit(main())
