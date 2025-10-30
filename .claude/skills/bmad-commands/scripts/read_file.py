#!/usr/bin/env python3
"""
BMAD Command: read_file
Read file contents with metadata and return structured JSON output
"""

import json
import sys
import time
from pathlib import Path
from datetime import datetime


def read_file(path: str):
    """Read file and return contents with metadata"""
    start_time = time.time()

    try:
        # Validate path
        file_path = Path(path)

        if not file_path.exists():
            return {
                "success": False,
                "outputs": {},
                "telemetry": {
                    "command": "read_file",
                    "duration_ms": int((time.time() - start_time) * 1000),
                    "timestamp": datetime.now().isoformat()
                },
                "errors": ["file_not_found"]
            }

        if not file_path.is_file():
            return {
                "success": False,
                "outputs": {},
                "telemetry": {
                    "command": "read_file",
                    "duration_ms": int((time.time() - start_time) * 1000),
                    "timestamp": datetime.now().isoformat()
                },
                "errors": ["path_is_not_file"]
            }

        # Read file
        content = file_path.read_text()
        line_count = len(content.splitlines())
        size_bytes = file_path.stat().st_size

        duration_ms = int((time.time() - start_time) * 1000)

        return {
            "success": True,
            "outputs": {
                "content": content,
                "line_count": line_count,
                "size_bytes": size_bytes,
                "path": str(file_path.absolute())
            },
            "telemetry": {
                "command": "read_file",
                "duration_ms": duration_ms,
                "timestamp": datetime.now().isoformat(),
                "path": str(file_path),
                "line_count": line_count
            },
            "errors": []
        }

    except PermissionError:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "read_file",
                "duration_ms": int((time.time() - start_time) * 1000),
                "timestamp": datetime.now().isoformat()
            },
            "errors": ["permission_denied"]
        }
    except Exception as e:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "read_file",
                "duration_ms": int((time.time() - start_time) * 1000),
                "timestamp": datetime.now().isoformat()
            },
            "errors": [f"unexpected_error: {str(e)}"]
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Read file with structured output")
    parser.add_argument("--path", required=True, help="Path to file to read")
    parser.add_argument("--output", default="json", choices=["json"], help="Output format (json only)")

    args = parser.parse_args()

    result = read_file(args.path)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["success"] else 1)
