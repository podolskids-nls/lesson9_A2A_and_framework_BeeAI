#!/usr/bin/env python3
"""BeeAI A2A Flight Agent — mock API рейсов (порт 8001)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import a2a.types as a2a_types
from beeai_framework.adapters.a2a.serve.server import A2AServer, A2AServerConfig
from beeai_framework.serve.utils import LRUMemoryManager

from framework.shared.handler_runnable import HandlerRunnable
from shared.flight_api import lookup


def handle(text: str) -> str:
    try:
        data = json.loads(text)
        return lookup(str(data.get("flight_number", "")), str(data.get("date", "")))
    except json.JSONDecodeError:
        pass
    fn = re.search(r"[A-Z]{2}-\d{3}", text.upper())
    dt = re.search(r"\d{4}-\d{2}-\d{2}", text)
    return lookup(fn.group(0) if fn else text, dt.group(0) if dt else "")


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    url = f"http://127.0.0.1:{port}"
    runnable = HandlerRunnable(handle)
    A2AServer(
        config=A2AServerConfig(host="127.0.0.1", port=port, protocol="jsonrpc"),
        memory_manager=LRUMemoryManager(maxsize=100),
    ).register(
        runnable,
        name="Flight Agent",
        description="Информация о рейсах (mock API)",
        url=url,
        version="1.0.0",
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        capabilities=a2a_types.AgentCapabilities(streaming=False),
        skills=[
            a2a_types.AgentSkill(
                id="get_flight",
                name="Get Flight Info",
                description="Номер рейса и дата (JSON или текст)",
                tags=["a2a"],
            )
        ],
    ).serve()


if __name__ == "__main__":
    main()
