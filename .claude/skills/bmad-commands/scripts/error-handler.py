#!/usr/bin/env python3
"""
BMAD Enhanced - Improved Error Message System
Provides helpful, actionable error messages with remediation guidance.
"""

import sys
import json
from enum import Enum
from typing import List, Optional, Dict
from datetime import datetime


class ErrorCategory(Enum):
    """Error categories for classification"""
    VALIDATION = "validation"
    CONFIGURATION = "configuration"
    GUARDRAIL = "guardrail"
    EXECUTION = "execution"
    DEPENDENCY = "dependency"
    TIMEOUT = "timeout"
    QUALITY_GATE = "quality_gate"
    COMPLEXITY = "complexity"
    FILE_NOT_FOUND = "file_not_found"
    PERMISSION = "permission"


class ErrorSeverity(Enum):
    """Error severity levels"""
    CRITICAL = "critical"   # Blocks all operations
    ERROR = "error"         # Blocks current operation
    WARNING = "warning"     # Allows continuation with caution
    INFO = "info"          # Informational only


class Colors:
    """ANSI color codes"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = '\033[2m'


class BMADError:
    """Structured error with remediation guidance"""

    def __init__(self,
                 category: ErrorCategory,
                 severity: ErrorSeverity,
                 message: str,
                 context: Optional[Dict] = None,
                 remediation_steps: Optional[List[str]] = None,
                 documentation_links: Optional[List[str]] = None,
                 related_errors: Optional[List[str]] = None):
        self.category = category
        self.severity = severity
        self.message = message
        self.context = context or {}
        self.remediation_steps = remediation_steps or []
        self.documentation_links = documentation_links or []
        self.related_errors = related_errors or []
        self.timestamp = datetime.now().isoformat()

    def format(self) -> str:
        """Format error for display"""
        output = []

        # Header
        severity_color = self._get_severity_color()
        severity_icon = self._get_severity_icon()
        output.append(f"\n{severity_color}{Colors.BOLD}{'=' * 70}{Colors.ENDC}")
        output.append(f"{severity_color}{Colors.BOLD}{severity_icon} {self.severity.value.upper()}: {self.category.value.replace('_', ' ').title()}{Colors.ENDC}")
        output.append(f"{severity_color}{Colors.BOLD}{'=' * 70}{Colors.ENDC}\n")

        # Error message
        output.append(f"{Colors.BOLD}Message:{Colors.ENDC}")
        output.append(f"  {self.message}\n")

        # Context
        if self.context:
            output.append(f"{Colors.BOLD}Context:{Colors.ENDC}")
            for key, value in self.context.items():
                output.append(f"  • {key}: {Colors.CYAN}{value}{Colors.ENDC}")
            output.append("")

        # Remediation steps
        if self.remediation_steps:
            output.append(f"{Colors.BOLD}{Colors.GREEN}How to Fix:{Colors.ENDC}")
            for i, step in enumerate(self.remediation_steps, 1):
                output.append(f"  {i}. {step}")
            output.append("")

        # Documentation links
        if self.documentation_links:
            output.append(f"{Colors.BOLD}Related Documentation:{Colors.ENDC}")
            for link in self.documentation_links:
                output.append(f"  • {Colors.CYAN}{link}{Colors.ENDC}")
            output.append("")

        # Related errors
        if self.related_errors:
            output.append(f"{Colors.BOLD}Related Issues:{Colors.ENDC}")
            for error in self.related_errors:
                output.append(f"  • {error}")
            output.append("")

        # Footer
        output.append(f"{Colors.DIM}Timestamp: {self.timestamp}{Colors.ENDC}")
        output.append(f"{severity_color}{Colors.BOLD}{'=' * 70}{Colors.ENDC}\n")

        return "\n".join(output)

    def _get_severity_color(self) -> str:
        """Get color for severity level"""
        if self.severity == ErrorSeverity.CRITICAL:
            return Colors.RED
        elif self.severity == ErrorSeverity.ERROR:
            return Colors.RED
        elif self.severity == ErrorSeverity.WARNING:
            return Colors.YELLOW
        else:
            return Colors.BLUE

    def _get_severity_icon(self) -> str:
        """Get icon for severity level"""
        if self.severity == ErrorSeverity.CRITICAL:
            return "🚨"
        elif self.severity == ErrorSeverity.ERROR:
            return "✗"
        elif self.severity == ErrorSeverity.WARNING:
            return "⚠"
        else:
            return "ℹ"

    def to_dict(self) -> Dict:
        """Convert error to dictionary for logging"""
        return {
            "category": self.category.value,
            "severity": self.severity.value,
            "message": self.message,
            "context": self.context,
            "remediation_steps": self.remediation_steps,
            "documentation_links": self.documentation_links,
            "related_errors": self.related_errors,
            "timestamp": self.timestamp
        }

    def to_json(self) -> str:
        """Convert error to JSON"""
        return json.dumps(self.to_dict(), indent=2)


# Predefined error templates
ERROR_TEMPLATES = {
    "missing_task_spec": {
        "category": ErrorCategory.FILE_NOT_FOUND,
        "severity": ErrorSeverity.ERROR,
        "message": "Task specification file not found",
        "remediation_steps": [
            "Create a task specification using: *create-task-spec --title='Your Task'",
            "Ensure the file path is correct and the file exists",
            "Check that the file is in the .claude/tasks/ directory",
            "Verify file permissions allow reading"
        ],
        "documentation_links": [
            "docs/quickstart-alex.md#1-create-task-spec",
            "docs/V2-ARCHITECTURE.md#task-specifications"
        ]
    },
    "complexity_too_high": {
        "category": ErrorCategory.COMPLEXITY,
        "severity": ErrorSeverity.WARNING,
        "message": "Task complexity exceeds recommended threshold",
        "remediation_steps": [
            "Review the complexity factors contributing to the high score",
            "Consider breaking down the task into smaller subtasks",
            "Use *breakdown-epic to decompose large features",
            "Confirm you want to proceed with this complex task"
        ],
        "documentation_links": [
            "docs/V2-ARCHITECTURE.md#complexity-assessment",
            "docs/quickstart-alex.md#2-breakdown-epic"
        ]
    },
    "guardrail_violation": {
        "category": ErrorCategory.GUARDRAIL,
        "severity": ErrorSeverity.ERROR,
        "message": "Guardrail violation detected - operation blocked",
        "remediation_steps": [
            "Review the specific guardrail that was violated",
            "Check if sensitive files are being accessed",
            "Verify test coverage meets minimum threshold",
            "Ensure code meets quality standards",
            "Review .claude/config.yaml for guardrail configuration"
        ],
        "documentation_links": [
            "docs/V2-ARCHITECTURE.md#guardrails-framework",
            "docs/PRODUCTION-SECURITY-REVIEW.md"
        ]
    },
    "quality_gate_failed": {
        "category": ErrorCategory.QUALITY_GATE,
        "severity": ErrorSeverity.ERROR,
        "message": "Quality gate validation failed",
        "remediation_steps": [
            "Review the quality gate report for specific issues",
            "Address failing tests or low test coverage",
            "Fix code quality issues (complexity, duplication, style)",
            "Use *apply-qa-fixes to address review comments",
            "Re-run *validate-quality-gate after fixes"
        ],
        "documentation_links": [
            "docs/quickstart-quinn.md#3-validate-quality-gate",
            "docs/V2-ARCHITECTURE.md#quality-gates"
        ]
    },
    "test_failure": {
        "category": ErrorCategory.EXECUTION,
        "severity": ErrorSeverity.ERROR,
        "message": "Tests failed during execution",
        "remediation_steps": [
            "Review test output for specific failures",
            "Use *debug to investigate failing tests",
            "Check if tests are flaky or have dependencies",
            "Verify test environment is set up correctly",
            "Run tests locally: *test --scope=unit"
        ],
        "documentation_links": [
            "docs/quickstart-james.md#3-test",
            "docs/quickstart-james.md#6-debug"
        ]
    },
    "missing_dependency": {
        "category": ErrorCategory.DEPENDENCY,
        "severity": ErrorSeverity.ERROR,
        "message": "Required dependency not found",
        "remediation_steps": [
            "Install required dependencies: pip install -r requirements.txt",
            "Check package.json or requirements.txt for dependencies",
            "Verify virtual environment is activated",
            "Run dependency installation for your package manager"
        ],
        "documentation_links": [
            "docs/PRODUCTION-DEPLOYMENT-GUIDE.md#prerequisites",
            "README.md#installation"
        ]
    },
    "timeout_exceeded": {
        "category": ErrorCategory.TIMEOUT,
        "severity": ErrorSeverity.ERROR,
        "message": "Operation exceeded maximum allowed time",
        "remediation_steps": [
            "Check if operation is stuck or slow",
            "Increase timeout in .claude/config.yaml if needed",
            "Break down operation into smaller steps",
            "Review logs for performance bottlenecks"
        ],
        "documentation_links": [
            "docs/V2-ARCHITECTURE.md#timeouts",
            "docs/PRODUCTION-MONITORING-GUIDE.md#performance-metrics"
        ]
    },
    "configuration_error": {
        "category": ErrorCategory.CONFIGURATION,
        "severity": ErrorSeverity.ERROR,
        "message": "Configuration error detected",
        "remediation_steps": [
            "Verify .claude/config.yaml exists and is valid YAML",
            "Check for required configuration fields",
            "Compare with config.yaml.template",
            "Validate configuration: python scripts/validate-config.py"
        ],
        "documentation_links": [
            "docs/PRODUCTION-DEPLOYMENT-GUIDE.md#configuration",
            ".claude/config.yaml.template"
        ]
    },
    "permission_denied": {
        "category": ErrorCategory.PERMISSION,
        "severity": ErrorSeverity.ERROR,
        "message": "Permission denied accessing file or directory",
        "remediation_steps": [
            "Check file/directory permissions: ls -la",
            "Ensure you have read/write access to the path",
            "Verify workspace directory is writable",
            "Check if files are locked by another process"
        ],
        "documentation_links": [
            "docs/PRODUCTION-SECURITY-REVIEW.md#file-permissions",
            "docs/PRODUCTION-DEPLOYMENT-GUIDE.md#system-requirements"
        ]
    },
    "validation_error": {
        "category": ErrorCategory.VALIDATION,
        "severity": ErrorSeverity.ERROR,
        "message": "Input validation failed",
        "remediation_steps": [
            "Check command syntax and required parameters",
            "Verify input files exist and are readable",
            "Ensure parameter values are within valid ranges",
            "Review command documentation for correct usage"
        ],
        "documentation_links": [
            "docs/quickstart-alex.md",
            "docs/quickstart-james.md",
            "docs/quickstart-quinn.md"
        ]
    }
}


class ErrorHandler:
    """Main error handler for BMAD operations"""

    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file

    def create_error(self,
                     template_name: str,
                     context: Optional[Dict] = None,
                     additional_remediation: Optional[List[str]] = None) -> BMADError:
        """Create error from template"""
        if template_name not in ERROR_TEMPLATES:
            # Return generic error
            return BMADError(
                category=ErrorCategory.EXECUTION,
                severity=ErrorSeverity.ERROR,
                message=f"Unknown error: {template_name}",
                context=context or {}
            )

        template = ERROR_TEMPLATES[template_name]
        remediation = template.get("remediation_steps", []).copy()
        if additional_remediation:
            remediation.extend(additional_remediation)

        error = BMADError(
            category=template["category"],
            severity=template["severity"],
            message=template["message"],
            context=context or {},
            remediation_steps=remediation,
            documentation_links=template.get("documentation_links", []),
            related_errors=template.get("related_errors", [])
        )

        return error

    def handle_error(self, error: BMADError, exit_on_error: bool = False):
        """Handle and display error"""
        # Print formatted error
        print(error.format(), file=sys.stderr)

        # Log to file if configured
        if self.log_file:
            try:
                with open(self.log_file, 'a') as f:
                    f.write(error.to_json() + "\n")
            except Exception as e:
                print(f"Warning: Could not write to error log: {e}", file=sys.stderr)

        # Exit if critical or requested
        if exit_on_error or error.severity == ErrorSeverity.CRITICAL:
            sys.exit(1)


def demo_errors():
    """Demo the error handling system"""
    handler = ErrorHandler()

    # Demo 1: Missing task spec
    print("DEMO 1: Missing Task Specification")
    error = handler.create_error(
        "missing_task_spec",
        context={
            "command": "*implement",
            "spec_file": ".claude/tasks/task-001-spec.md",
            "cwd": "/home/user/project"
        }
    )
    handler.handle_error(error)

    # Demo 2: Complexity warning
    print("\nDEMO 2: High Complexity Warning")
    error = handler.create_error(
        "complexity_too_high",
        context={
            "command": "*implement",
            "complexity_score": 85,
            "threshold": 70,
            "factors": "Unknown domain (40), Large scope (25), Missing tests (20)"
        }
    )
    handler.handle_error(error)

    # Demo 3: Quality gate failure
    print("\nDEMO 3: Quality Gate Failure")
    error = handler.create_error(
        "quality_gate_failed",
        context={
            "command": "*validate-quality-gate",
            "decision": "FAIL",
            "score": 45,
            "threshold": 60,
            "issues": "3 failing tests, 55% coverage (target: 80%)"
        },
        additional_remediation=[
            "Focus on increasing test coverage in src/payment/ module",
            "Fix failing integration tests in tests/test_checkout.py"
        ]
    )
    handler.handle_error(error)

    # Demo 4: Guardrail violation
    print("\nDEMO 4: Guardrail Violation")
    error = handler.create_error(
        "guardrail_violation",
        context={
            "command": "*implement",
            "violation": "Attempting to access sensitive file",
            "file": ".env",
            "guardrail": "block_sensitive_files"
        }
    )
    handler.handle_error(error)


if __name__ == "__main__":
    demo_errors()
