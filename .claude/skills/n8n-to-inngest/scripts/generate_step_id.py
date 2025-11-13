#!/usr/bin/env python3
"""
Generate valid, deterministic Inngest step IDs from n8n node names.

Inngest step IDs must:
- Use kebab-case (lowercase with hyphens)
- Be deterministic (same input -> same output)
- Be URL-safe
- Be meaningful and readable

Usage:
    python generate_step_id.py "HTTP Request 1"
    # Output: http-request-1

    python generate_step_id.py "Send Email to Customer"
    # Output: send-email-to-customer
"""

import re
import sys
from typing import List


def generate_step_id(node_name: str) -> str:
    """
    Generate a valid Inngest step ID from an n8n node name.

    Args:
        node_name: The n8n node name (e.g., "HTTP Request 1", "Send Email")

    Returns:
        A valid kebab-case step ID (e.g., "http-request-1", "send-email")

    Examples:
        >>> generate_step_id("HTTP Request 1")
        'http-request-1'
        >>> generate_step_id("Send Email to Customer")
        'send-email-to-customer'
        >>> generate_step_id("If/Else Conditional")
        'if-else-conditional'
        >>> generate_step_id("Create User (Admin)")
        'create-user-admin'
    """
    # Convert to lowercase
    step_id = node_name.lower()

    # Replace special characters with hyphens
    step_id = re.sub(r'[^a-z0-9]+', '-', step_id)

    # Remove leading/trailing hyphens
    step_id = step_id.strip('-')

    # Remove consecutive hyphens
    step_id = re.sub(r'-+', '-', step_id)

    return step_id


def generate_multiple_step_ids(node_names: List[str]) -> dict:
    """
    Generate step IDs for multiple node names.

    Args:
        node_names: List of n8n node names

    Returns:
        Dictionary mapping node names to step IDs
    """
    return {name: generate_step_id(name) for name in node_names}


def validate_step_id(step_id: str) -> bool:
    """
    Validate that a step ID follows Inngest conventions.

    Args:
        step_id: The step ID to validate

    Returns:
        True if valid, False otherwise
    """
    # Must be lowercase with hyphens only
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', step_id):
        return False

    # Must not be empty
    if not step_id:
        return False

    return True


def suggest_improvements(step_id: str) -> List[str]:
    """
    Suggest improvements for a step ID.

    Args:
        step_id: The step ID to analyze

    Returns:
        List of improvement suggestions
    """
    suggestions = []

    if len(step_id) > 50:
        suggestions.append(f"Step ID is long ({len(step_id)} chars). Consider shortening for readability.")

    if re.search(r'\d+$', step_id):
        suggestions.append("Step ID ends with number. Consider using more descriptive suffix.")

    parts = step_id.split('-')
    if len(parts) > 6:
        suggestions.append(f"Step ID has many parts ({len(parts)}). Consider simplifying.")

    # Check for common abbreviation opportunities
    replacements = {
        'request': 'req',
        'response': 'resp',
        'customer': 'cust',
        'database': 'db',
        'message': 'msg',
        'configuration': 'config',
    }

    for long, short in replacements.items():
        if long in step_id and len(step_id) > 30:
            suggestions.append(f"Consider abbreviating '{long}' to '{short}' to shorten ID.")

    return suggestions


def batch_convert_from_file(file_path: str) -> dict:
    """
    Read node names from a file and generate step IDs.

    Args:
        file_path: Path to file with one node name per line

    Returns:
        Dictionary mapping node names to step IDs
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            node_names = [line.strip() for line in f if line.strip()]

        return generate_multiple_step_ids(node_names)
    except FileNotFoundError:
        return {'error': f'File not found: {file_path}'}
    except Exception as e:
        return {'error': f'Error reading file: {str(e)}'}


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print('Usage: python generate_step_id.py <node_name> [--validate] [--suggest]')
        print('')
        print('Examples:')
        print('  python generate_step_id.py "HTTP Request 1"')
        print('  python generate_step_id.py "Send Email" --validate')
        print('  python generate_step_id.py "Create User Account" --suggest')
        sys.exit(1)

    node_name = sys.argv[1]
    validate = '--validate' in sys.argv
    suggest = '--suggest' in sys.argv

    # Generate step ID
    step_id = generate_step_id(node_name)

    # Output
    if validate or suggest:
        print(f'Node Name: {node_name}')
        print(f'Step ID:   {step_id}')
        print('')

        if validate:
            is_valid = validate_step_id(step_id)
            print(f'Valid: {"✓ Yes" if is_valid else "✗ No"}')

        if suggest:
            suggestions = suggest_improvements(step_id)
            if suggestions:
                print('\nSuggestions:')
                for suggestion in suggestions:
                    print(f'  - {suggestion}')
            else:
                print('\nNo improvements needed ✓')
    else:
        # Simple output for piping
        print(step_id)


if __name__ == '__main__':
    main()
