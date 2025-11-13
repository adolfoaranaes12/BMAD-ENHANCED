#!/usr/bin/env python3
"""
Parse n8n workflow JSON to extract structure, nodes, connections, and generate dependency graph.

Usage:
    python parse_n8n_workflow.py <workflow.json>

Output:
    JSON structure with nodes, triggers, credentials, and dependency information.
"""

import json
import sys
from typing import Dict, List, Set, Any
from collections import defaultdict


class N8nWorkflowParser:
    """Parser for n8n workflow JSON files."""

    def __init__(self, workflow_data: Dict[str, Any]):
        self.workflow_data = workflow_data
        self.nodes = workflow_data.get('nodes', [])
        self.connections = workflow_data.get('connections', {})
        self.settings = workflow_data.get('settings', {})

    def parse(self) -> Dict[str, Any]:
        """Parse the workflow and extract all relevant information."""
        return {
            'metadata': self._extract_metadata(),
            'triggers': self._extract_triggers(),
            'nodes': self._extract_node_info(),
            'dependencies': self._build_dependency_graph(),
            'credentials': self._extract_credentials(),
            'statistics': self._calculate_statistics(),
        }

    def _extract_metadata(self) -> Dict[str, Any]:
        """Extract workflow metadata."""
        return {
            'name': self.workflow_data.get('name', 'Unnamed Workflow'),
            'active': self.workflow_data.get('active', False),
            'createdAt': self.workflow_data.get('createdAt'),
            'updatedAt': self.workflow_data.get('updatedAt'),
            'settings': self.settings,
        }

    def _extract_triggers(self) -> List[Dict[str, Any]]:
        """Extract all trigger nodes from the workflow."""
        triggers = []

        for node in self.nodes:
            node_type = node.get('type', '')

            # Identify trigger nodes
            if 'trigger' in node_type.lower() or node_type.endswith('.webhook'):
                trigger_info = {
                    'id': node.get('id'),
                    'name': node.get('name'),
                    'type': node_type,
                    'typeGroup': self._get_trigger_type(node_type),
                    'parameters': node.get('parameters', {}),
                }
                triggers.append(trigger_info)

        return triggers

    def _get_trigger_type(self, node_type: str) -> str:
        """Determine the trigger type category."""
        type_lower = node_type.lower()

        if 'webhook' in type_lower:
            return 'webhook'
        elif 'cron' in type_lower or 'schedule' in type_lower:
            return 'schedule'
        elif 'manual' in type_lower:
            return 'manual'
        elif 'email' in type_lower:
            return 'email'
        else:
            return 'other'

    def _extract_node_info(self) -> List[Dict[str, Any]]:
        """Extract information about all nodes."""
        node_info = []

        for node in self.nodes:
            info = {
                'id': node.get('id'),
                'name': node.get('name'),
                'type': node.get('type'),
                'typeVersion': node.get('typeVersion'),
                'position': node.get('position', []),
                'parameters': node.get('parameters', {}),
                'credentials': node.get('credentials', {}),
                'disabled': node.get('disabled', False),
                'nodeType': self._categorize_node(node.get('type', '')),
            }
            node_info.append(info)

        return node_info

    def _categorize_node(self, node_type: str) -> str:
        """Categorize node by function."""
        type_lower = node_type.lower()

        if 'trigger' in type_lower or 'webhook' in type_lower:
            return 'trigger'
        elif 'if' in type_lower or 'switch' in type_lower:
            return 'conditional'
        elif 'loop' in type_lower or 'split' in type_lower:
            return 'loop'
        elif 'wait' in type_lower or 'delay' in type_lower:
            return 'wait'
        elif 'http' in type_lower or 'request' in type_lower:
            return 'http'
        elif 'function' in type_lower or 'code' in type_lower:
            return 'code'
        elif 'set' in type_lower or 'merge' in type_lower:
            return 'data-transform'
        elif 'database' in type_lower or 'postgres' in type_lower or 'mysql' in type_lower:
            return 'database'
        elif 'email' in type_lower or 'sendgrid' in type_lower:
            return 'email'
        elif 'execute' in type_lower and 'workflow' in type_lower:
            return 'workflow-call'
        else:
            return 'other'

    def _build_dependency_graph(self) -> Dict[str, Any]:
        """Build a dependency graph showing node connections."""
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        for source_node, connections in self.connections.items():
            if 'main' in connections:
                for output_index, outputs in enumerate(connections['main']):
                    if outputs:
                        for connection in outputs:
                            target_node = connection.get('node')
                            graph[source_node].append({
                                'target': target_node,
                                'outputIndex': output_index,
                                'targetIndex': connection.get('index', 0),
                            })
                            reverse_graph[target_node].append(source_node)

        # Calculate execution order
        execution_order = self._topological_sort(dict(graph))

        return {
            'forward': dict(graph),
            'reverse': dict(reverse_graph),
            'executionOrder': execution_order,
        }

    def _topological_sort(self, graph: Dict[str, List[Any]]) -> List[str]:
        """Perform topological sort to determine execution order."""
        # Calculate in-degrees
        in_degree = defaultdict(int)
        all_nodes = set(graph.keys())

        for node in graph:
            for connection in graph[node]:
                target = connection['target']
                all_nodes.add(target)
                in_degree[target] += 1

        # Find nodes with no incoming edges (triggers)
        queue = [node for node in all_nodes if in_degree[node] == 0]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)

            if node in graph:
                for connection in graph[node]:
                    target = connection['target']
                    in_degree[target] -= 1
                    if in_degree[target] == 0:
                        queue.append(target)

        return result

    def _extract_credentials(self) -> List[Dict[str, Any]]:
        """Extract all credentials used in the workflow."""
        credentials_map = {}

        for node in self.nodes:
            node_credentials = node.get('credentials', {})
            for cred_type, cred_info in node_credentials.items():
                cred_id = cred_info.get('id')
                if cred_id and cred_id not in credentials_map:
                    credentials_map[cred_id] = {
                        'id': cred_id,
                        'name': cred_info.get('name'),
                        'type': cred_type,
                        'usedByNodes': [],
                    }
                if cred_id:
                    credentials_map[cred_id]['usedByNodes'].append(node.get('name'))

        return list(credentials_map.values())

    def _calculate_statistics(self) -> Dict[str, Any]:
        """Calculate workflow statistics."""
        node_types = defaultdict(int)
        node_categories = defaultdict(int)

        for node in self.nodes:
            node_type = node.get('type', 'unknown')
            node_types[node_type] += 1
            category = self._categorize_node(node_type)
            node_categories[category] += 1

        return {
            'totalNodes': len(self.nodes),
            'totalConnections': sum(
                len(outputs)
                for connections in self.connections.values()
                for output_list in connections.get('main', [])
                for outputs in [output_list] if outputs
            ),
            'nodesByType': dict(node_types),
            'nodesByCategory': dict(node_categories),
            'hasCredentials': len(self._extract_credentials()) > 0,
            'triggerCount': len(self._extract_triggers()),
        }


def parse_workflow_file(file_path: str) -> Dict[str, Any]:
    """Parse an n8n workflow JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)

        parser = N8nWorkflowParser(workflow_data)
        return parser.parse()
    except FileNotFoundError:
        return {'error': f'File not found: {file_path}'}
    except json.JSONDecodeError as e:
        return {'error': f'Invalid JSON: {str(e)}'}
    except Exception as e:
        return {'error': f'Error parsing workflow: {str(e)}'}


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print('Usage: python parse_n8n_workflow.py <workflow.json>')
        sys.exit(1)

    file_path = sys.argv[1]
    result = parse_workflow_file(file_path)

    # Pretty print the result
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
