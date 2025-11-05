"""
BMAD Framework Adapters

Provides pluggable test framework adapters for bmad-commands.
"""

from .base import TestFrameworkAdapter, TestResult

__all__ = ["TestFrameworkAdapter", "TestResult"]
