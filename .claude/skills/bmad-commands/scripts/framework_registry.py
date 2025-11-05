"""
Framework Registry

Loads and manages test framework adapters from configuration.
"""

import sys
import importlib
from pathlib import Path
from typing import Optional, Dict, List
import yaml


class FrameworkRegistry:
    """Registry for test framework adapters"""

    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize registry and load adapters from config.

        Args:
            config_path: Path to .claude/config.yaml (auto-detected if None)
        """
        if config_path is None:
            config_path = self._find_config()

        self.config_path = config_path
        self.adapters: Dict[str, any] = {}
        self.config = self._load_config()
        self._register_builtin_adapters()
        self._register_custom_adapters()

    def _find_config(self) -> Path:
        """Find .claude/config.yaml in current or parent directories"""
        current = Path.cwd()

        # Search up to 5 levels
        for _ in range(5):
            config = current / ".claude" / "config.yaml"
            if config.exists():
                return config
            parent = current.parent
            if parent == current:  # Reached root
                break
            current = parent

        # Default path
        return Path(".claude/config.yaml")

    def _load_config(self) -> dict:
        """Load configuration file"""
        if not self.config_path.exists():
            print(f"Warning: Config not found at {self.config_path}, using defaults", file=sys.stderr)
            return {"testing": {"frameworks": {}}}

        try:
            with open(self.config_path) as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Warning: Failed to load config: {e}", file=sys.stderr)
            return {"testing": {"frameworks": {}}}

    def _register_builtin_adapters(self):
        """Register built-in adapters (Jest, Pytest)"""
        builtins = {
            "jest": {
                "name": "jest",
                "adapter": "adapters.jest_adapter.JestAdapter",
                "command": ["npm", "test", "--", "--json"]
            },
            "pytest": {
                "name": "pytest",
                "adapter": "adapters.pytest_adapter.PytestAdapter",
                "command": ["pytest", "--json-report"]
            }
        }

        for name, config in builtins.items():
            try:
                self._load_adapter(name, config)
            except Exception as e:
                print(f"Warning: Failed to load built-in adapter {name}: {e}", file=sys.stderr)

    def _register_custom_adapters(self):
        """Register adapters from config file"""
        frameworks = self.config.get("testing", {}).get("frameworks", {})

        for name, config in frameworks.items():
            if name in self.adapters:
                # Override built-in with custom config
                continue

            try:
                config["name"] = name
                self._load_adapter(name, config)
            except Exception as e:
                print(f"Warning: Failed to load custom adapter {name}: {e}", file=sys.stderr)

    def _load_adapter(self, name: str, config: dict):
        """Load a single adapter"""
        adapter_class_path = config.get("adapter")
        if not adapter_class_path:
            return

        try:
            # Handle relative imports (e.g., "adapters.jest_adapter.JestAdapter")
            # and absolute imports (e.g., ".claude.custom_adapters.my_framework.MyAdapter")
            if adapter_class_path.startswith("."):
                # Absolute path from project root
                module_path, class_name = adapter_class_path.rsplit(".", 1)
                module = importlib.import_module(module_path)
            else:
                # Relative to current package
                module_path, class_name = adapter_class_path.rsplit(".", 1)
                module = importlib.import_module(f".{module_path}", package=__package__ or "adapters")

            adapter_cls = getattr(module, class_name)

            # Instantiate adapter
            self.adapters[name] = adapter_cls(config)

        except Exception as e:
            print(f"Warning: Failed to instantiate adapter {name}: {e}", file=sys.stderr)
            raise

    def detect_framework(self, path: Path) -> Optional[str]:
        """
        Auto-detect test framework in project.

        Args:
            path: Project root path

        Returns:
            Framework name if detected, None otherwise
        """
        # Try each adapter's detect method
        for name, adapter in self.adapters.items():
            try:
                if adapter.detect(path):
                    return name
            except Exception as e:
                print(f"Warning: Detection failed for {name}: {e}", file=sys.stderr)

        return None

    def get_adapter(self, framework: str):
        """
        Get adapter for specified framework.

        Args:
            framework: Framework name

        Returns:
            Adapter instance or None
        """
        return self.adapters.get(framework)

    def list_frameworks(self) -> List[str]:
        """
        List all registered frameworks.

        Returns:
            List of framework names
        """
        return list(self.adapters.keys())

    def list_frameworks_detailed(self) -> Dict[str, dict]:
        """
        List all frameworks with details.

        Returns:
            Dict mapping framework name to config
        """
        return {
            name: {
                "name": name,
                "adapter_class": adapter.__class__.__name__,
                "command": adapter.command
            }
            for name, adapter in self.adapters.items()
        }
