#!/usr/bin/env python3
"""BeeAI A2A Calendar Agent — события в calendar.json (порт 8002)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import a2a.types as a2a_types
from beeai_framework.adapters.a2a.serve.server import A2AServer, A2AServerConfig
from beeai_framework.serve.utils import LRUMemoryManager

from framework.shared.handler_runnable import HandlerRunnable
from shared.calendar_api import add_event


def handle(text: str) -> str:
    data = json.loads(text)
    return add_event(
        str(data.get("title", "")),
        str(data.get("date", "")),
        str(data.get("time", "")),
        str(data.get("description", "")),
    )


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8002
    url = f"http://127.0.0.1:{port}"
    runnable = HandlerRunnable(handle)
    A2AServer(
        config=A2AServerConfig(host="127.0.0.1", port=port, protocol="jsonrpc"),
        memory_manager=LRUMemoryManager(maxsize=100),
    ).register(
        runnable,
        name="Calendar Agent",
        description="Добавление событий в локальный календарь",
        url=url,
        version="1.0.0",
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        capabilities=a2a_types.AgentCapabilities(streaming=False),
        skills=[
            a2a_types.AgentSkill(
                id="add_event",
                name="Add Calendar Event",
                description="JSON: title, date, time, description",
                tags=["a2a"],
            )
        ],
    ).serve()


if __name__ == "__main__":
    main()
