#!/usr/bin/env python3
"""
Validate architecture metrics for accuracy.

Prevents overcounting issues by precisely identifying:
- CQRS handlers vs command/query definitions
- Domain entities vs value objects
- Repositories vs interfaces
- Test files vs source files

Usage:
    python validate_metrics.py --codebase <path> --metric <type> --output <format>

Examples:
    # Count CQRS handlers accurately
    python validate_metrics.py --codebase packages/backend/src --metric cqrs --output json

    # Count domain entities
    python validate_metrics.py --codebase src --metric entities --output json

    # Count all metrics
    python validate_metrics.py --codebase src --metric all --output json
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List


def count_cqrs_handlers(codebase_path: Path) -> Dict[str, Any]:
    """
    Accurately count CQRS handlers and definitions.

    Distinguishes between:
    - Command definitions (application/commands/*.ts)
    - Command handlers (application/handlers/commands/*Handler.ts)
    - Query definitions (application/queries/*.ts)
    - Query handlers (application/handlers/queries/*Handler.ts)

    Returns:
        {
            'command_files': int,       # Command definitions
            'query_files': int,         # Query definitions
            'command_handlers': int,    # Command handler implementations
            'query_handlers': int,      # Query handler implementations
            'total_files': int,         # All command/query definitions
            'total_handlers': int       # All handler implementations
        }
    """
    handlers_path = codebase_path / "application" / "handlers"
    commands_path = codebase_path / "application" / "commands"
    queries_path = codebase_path / "application" / "queries"

    # Count handler implementations (not definitions)
    command_handlers = list(handlers_path.glob("commands/*CommandHandler.ts")) if handlers_path.exists() else []
    query_handlers = list(handlers_path.glob("queries/*QueryHandler.ts")) if handlers_path.exists() else []

    # Count command and query definitions
    command_files = list(commands_path.glob("**/*Command.ts")) if commands_path.exists() else []
    query_files = list(queries_path.glob("**/*Query.ts")) if queries_path.exists() else []

    # Remove index files from counts
    command_files = [f for f in command_files if f.name != "index.ts"]
    query_files = [f for f in query_files if f.name != "index.ts"]

    return {
        'command_files': len(command_files),
        'query_files': len(query_files),
        'command_handlers': len(command_handlers),
        'query_handlers': len(query_handlers),
        'total_files': len(command_files) + len(query_files),
        'total_handlers': len(command_handlers) + len(query_handlers),
        'command_handler_list': [f.name for f in command_handlers[:10]],  # Sample
        'query_handler_list': [f.name for f in query_handlers[:10]]        # Sample
    }


def count_entities(codebase_path: Path) -> Dict[str, Any]:
    """
    Count domain entities accurately.

    Returns:
        {
            'count': int,
            'entity_list': List[str]  # First 20 entity names
        }
    """
    entities_path = codebase_path / "domain" / "entities"

    if not entities_path.exists():
        return {'count': 0, 'entity_list': []}

    # Find all .ts files, exclude index.ts
    entities = [f for f in entities_path.glob("*.ts") if f.name != "index.ts"]

    return {
        'count': len(entities),
        'entity_list': [f.stem for f in entities[:20]]  # First 20
    }


def count_value_objects(codebase_path: Path) -> Dict[str, Any]:
    """
    Count value objects accurately.

    Returns:
        {
            'count': int,
            'value_object_list': List[str]  # First 20 VO names
        }
    """
    vo_path = codebase_path / "domain" / "value-objects"

    if not vo_path.exists():
        return {'count': 0, 'value_object_list': []}

    # Find all .ts files, exclude index.ts
    value_objects = [f for f in vo_path.glob("*.ts") if f.name != "index.ts"]

    return {
        'count': len(value_objects),
        'value_object_list': [f.stem for f in value_objects[:20]]  # First 20
    }


def count_domain_events(codebase_path: Path) -> Dict[str, Any]:
    """
    Count domain events accurately.

    Returns:
        {
            'count': int,
            'event_list': List[str]
        }
    """
    events_path = codebase_path / "domain" / "events"

    if not events_path.exists():
        return {'count': 0, 'event_list': []}

    # Find all .ts files, exclude index.ts
    events = [f for f in events_path.glob("*.ts") if f.name != "index.ts"]

    return {
        'count': len(events),
        'event_list': [f.stem for f in events]
    }


def count_repositories(codebase_path: Path) -> Dict[str, Any]:
    """
    Count repository implementations accurately.

    Distinguishes between:
    - Repository interfaces (domain/)
    - Repository implementations (infrastructure/database/repositories/)

    Returns:
        {
            'implementation_count': int,
            'interface_count': int,
            'repository_list': List[str]
        }
    """
    repo_impl_path = codebase_path / "infrastructure" / "database" / "repositories"
    repo_interface_path = codebase_path / "domain" / "repositories"

    implementations = []
    if repo_impl_path.exists():
        implementations = [f for f in repo_impl_path.glob("*Repository.ts") if f.name != "index.ts"]

    interfaces = []
    if repo_interface_path.exists():
        interfaces = [f for f in repo_interface_path.glob("*Repository.ts") if f.name != "index.ts"]

    return {
        'implementation_count': len(implementations),
        'interface_count': len(interfaces),
        'repository_list': [f.stem for f in implementations[:20]]
    }


def count_controllers(codebase_path: Path) -> Dict[str, Any]:
    """
    Count controllers accurately.

    Returns:
        {
            'count': int,
            'controller_list': List[str]
        }
    """
    controllers_path = codebase_path / "presentation" / "controllers"

    if not controllers_path.exists():
        return {'count': 0, 'controller_list': []}

    controllers = [f for f in controllers_path.glob("*Controller.ts") if f.name != "index.ts"]

    return {
        'count': len(controllers),
        'controller_list': [f.stem for f in controllers[:20]]
    }


def count_routes(codebase_path: Path) -> Dict[str, Any]:
    """
    Count route files accurately.

    Returns:
        {
            'count': int,
            'route_list': List[str]
        }
    """
    routes_path = codebase_path / "presentation" / "routes"

    if not routes_path.exists():
        return {'count': 0, 'route_list': []}

    routes = [f for f in routes_path.glob("*.ts") if f.name not in ["index.ts", "routes.ts"]]

    return {
        'count': len(routes),
        'route_list': [f.stem for f in routes]
    }


def count_tests(codebase_path: Path) -> Dict[str, Any]:
    """
    Count test files accurately.

    Returns:
        {
            'unit_tests': int,
            'integration_tests': int,
            'e2e_tests': int,
            'total_tests': int
        }
    """
    test_path = codebase_path / "test"

    if not test_path.exists():
        # Try src/__tests__ or src/**/*.test.ts pattern
        src_path = codebase_path
        test_files = list(src_path.glob("**/*.test.ts")) + list(src_path.glob("**/*.spec.ts"))
        return {
            'unit_tests': len([f for f in test_files if '/unit/' in str(f)]),
            'integration_tests': len([f for f in test_files if '/integration/' in str(f)]),
            'e2e_tests': len([f for f in test_files if '/e2e/' in str(f)]),
            'total_tests': len(test_files)
        }

    unit_tests = list(test_path.glob("unit/**/*.test.ts"))
    integration_tests = list(test_path.glob("integration/**/*.test.ts"))
    e2e_tests = list(test_path.glob("e2e/**/*.test.ts"))

    return {
        'unit_tests': len(unit_tests),
        'integration_tests': len(integration_tests),
        'e2e_tests': len(e2e_tests),
        'total_tests': len(unit_tests) + len(integration_tests) + len(e2e_tests)
    }


def count_all_metrics(codebase_path: Path) -> Dict[str, Any]:
    """
    Count all architecture metrics.

    Returns comprehensive metrics dictionary.
    """
    return {
        'cqrs': count_cqrs_handlers(codebase_path),
        'entities': count_entities(codebase_path),
        'value_objects': count_value_objects(codebase_path),
        'domain_events': count_domain_events(codebase_path),
        'repositories': count_repositories(codebase_path),
        'controllers': count_controllers(codebase_path),
        'routes': count_routes(codebase_path),
        'tests': count_tests(codebase_path)
    }


def format_output(data: Dict[str, Any], output_format: str) -> str:
    """
    Format output based on requested format.

    Args:
        data: Metrics dictionary
        output_format: 'json' or 'text'

    Returns:
        Formatted string
    """
    if output_format == 'json':
        return json.dumps(data, indent=2)

    # Text format
    lines = []

    if 'total_handlers' in data:  # CQRS metrics
        lines.append("CQRS Metrics:")
        lines.append(f"  Command Definitions: {data['command_files']}")
        lines.append(f"  Query Definitions: {data['query_files']}")
        lines.append(f"  Command Handlers: {data['command_handlers']}")
        lines.append(f"  Query Handlers: {data['query_handlers']}")
        lines.append(f"  Total Definitions: {data['total_files']}")
        lines.append(f"  Total Handlers: {data['total_handlers']}")

    elif 'count' in data:  # Entity/VO metrics
        lines.append(f"Count: {data['count']}")
        if 'entity_list' in data and data['entity_list']:
            lines.append(f"Sample: {', '.join(data['entity_list'][:5])}")

    elif 'cqrs' in data:  # All metrics
        lines.append("=== Architecture Metrics ===")
        lines.append(f"\nCQRS Handlers: {data['cqrs']['total_handlers']}")
        lines.append(f"  Commands: {data['cqrs']['command_handlers']}")
        lines.append(f"  Queries: {data['cqrs']['query_handlers']}")
        lines.append(f"\nDomain Model:")
        lines.append(f"  Entities: {data['entities']['count']}")
        lines.append(f"  Value Objects: {data['value_objects']['count']}")
        lines.append(f"  Domain Events: {data['domain_events']['count']}")
        lines.append(f"\nInfrastructure:")
        lines.append(f"  Repositories: {data['repositories']['implementation_count']}")
        lines.append(f"  Controllers: {data['controllers']['count']}")
        lines.append(f"  Routes: {data['routes']['count']}")
        lines.append(f"\nTesting:")
        lines.append(f"  Total Tests: {data['tests']['total_tests']}")
        lines.append(f"  Unit: {data['tests']['unit_tests']}")
        lines.append(f"  Integration: {data['tests']['integration_tests']}")
        lines.append(f"  E2E: {data['tests']['e2e_tests']}")

    return '\n'.join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate architecture metrics with precision',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Count CQRS handlers
  python validate_metrics.py --codebase src --metric cqrs --output json

  # Count domain entities
  python validate_metrics.py --codebase src --metric entities

  # Count all metrics
  python validate_metrics.py --codebase src --metric all --output json
        """
    )

    parser.add_argument(
        '--codebase',
        required=True,
        help='Path to codebase root (e.g., packages/backend/src)'
    )

    parser.add_argument(
        '--metric',
        required=True,
        choices=['cqrs', 'entities', 'value_objects', 'domain_events', 'repositories', 'controllers', 'routes', 'tests', 'all'],
        help='Metric type to validate'
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

    # Count metrics based on type
    metric_functions = {
        'cqrs': count_cqrs_handlers,
        'entities': count_entities,
        'value_objects': count_value_objects,
        'domain_events': count_domain_events,
        'repositories': count_repositories,
        'controllers': count_controllers,
        'routes': count_routes,
        'tests': count_tests,
        'all': count_all_metrics
    }

    result = metric_functions[args.metric](codebase_path)

    # Format and print output
    output = format_output(result, args.output)
    print(output)

    return 0


if __name__ == '__main__':
    sys.exit(main())
