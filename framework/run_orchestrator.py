#!/usr/bin/env python3
"""CLI entry: BeeAI orchestrator harness."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    cmd = [sys.executable, str(ROOT / "agents" / "orchestrator.py"), *sys.argv[1:]]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
