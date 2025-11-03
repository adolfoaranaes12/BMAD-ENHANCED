#!/usr/bin/env python3
"""
Command: extract_adrs

Extracts Architecture Decision Records (ADRs) from architecture document.
Creates separate ADR files in standard format.
"""

import json
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path


def extract_adrs(architecture_path: str, output_dir: str) -> dict:
    """
    Extract ADRs from architecture document and save as separate files.

    Args:
        architecture_path: Path to architecture document
        output_dir: Directory to save extracted ADR files

    Returns:
        dict: Standard command response
    """
    start_time = datetime.now()

    try:
        # Validate input
        arch_file = Path(architecture_path)
        if not arch_file.exists():
            return {
                "success": False,
                "outputs": {},
                "telemetry": {
                    "command": "extract_adrs",
                    "duration_ms": int((datetime.now() - start_time).total_seconds() * 1000),
                    "timestamp": datetime.now().isoformat()
                },
                "errors": ["file_not_found"]
            }

        # Read architecture document
        content = arch_file.read_text()

        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # TODO: Implement actual ADR extraction logic
        # For now, use simple pattern matching for ADR sections

        # Look for ADR patterns (ADR-001, ADR-002, etc.)
        adr_pattern = r'(?:^|\n)(?:###|##)\s*ADR[-\s](\d+)[:\s]+(.+?)(?=\n(?:###|##)|$)'
        matches = re.finditer(adr_pattern, content, re.MULTILINE | re.DOTALL)

        extracted_adrs = []

        for match in matches:
            adr_number = match.group(1)
            adr_content = match.group(2).strip()

            # Extract title (first line)
            title_match = re.match(r'(.+?)(?:\n|$)', adr_content)
            title = title_match.group(1).strip() if title_match else f"ADR {adr_number}"

            # Create ADR filename
            adr_filename = f"ADR-{adr_number.zfill(3)}-{title.lower().replace(' ', '-')[:50]}.md"
            adr_path = output_path / adr_filename

            # Create ADR file content
            adr_file_content = f"""# ADR-{adr_number.zfill(3)}: {title}

**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Status:** Accepted

## Context

{adr_content}

---

*Extracted from: {architecture_path}*
*Extraction date: {datetime.now().isoformat()}*
"""

            # Write ADR file
            adr_path.write_text(adr_file_content)

            extracted_adrs.append({
                "number": adr_number,
                "title": title,
                "file": str(adr_path.absolute())
            })

        duration_ms = int((datetime.now() - start_time).total_seconds() * 1000)

        return {
            "success": True,
            "outputs": {
                "adrs_extracted": len(extracted_adrs),
                "adrs": extracted_adrs,
                "output_directory": str(output_path.absolute()),
                "architecture_source": architecture_path
            },
            "telemetry": {
                "command": "extract_adrs",
                "adrs_count": len(extracted_adrs),
                "duration_ms": duration_ms,
                "timestamp": datetime.now().isoformat()
            },
            "errors": []
        }

    except Exception as e:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "extract_adrs",
                "duration_ms": int((datetime.now() - start_time).total_seconds() * 1000),
                "timestamp": datetime.now().isoformat()
            },
            "errors": [f"unexpected_error: {str(e)}"]
        }


def main():
    parser = argparse.ArgumentParser(description="Extract ADRs from architecture document")
    parser.add_argument("--architecture", required=True, help="Path to architecture document")
    parser.add_argument("--output", default="docs/adrs", help="Output directory for ADR files")

    args = parser.parse_args()

    result = extract_adrs(args.architecture, args.output)

    print(json.dumps(result, indent=2))
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
