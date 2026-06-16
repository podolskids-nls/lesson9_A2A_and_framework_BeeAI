#!/usr/bin/env python3
"""Запуск BeeAI A2A Flight (8001) и Calendar (8002)."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AGENTS = ROOT / "agents"


def main() -> None:
    procs = [
        subprocess.Popen([sys.executable, str(AGENTS / "flight_server.py")]),
        subprocess.Popen([sys.executable, str(AGENTS / "calendar_server.py")]),
    ]
    print("BeeAI A2A агенты запущены (8001, 8002). Ctrl+C для остановки.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for p in procs:
            p.terminate()


if __name__ == "__main__":
    main()
