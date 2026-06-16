#!/usr/bin/env python3
"""A2A Calendar Agent — события в calendar.json."""
from __future__ import annotations

import json
import sys

from shared.a2a_app import run_server
from shared.calendar_api import add_event


def handle(text: str) -> str:
    data = json.loads(text)
    return add_event(
        str(data.get("title", "")),
        str(data.get("date", "")),
        str(data.get("time", "")),
        str(data.get("description", "")),
    )


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8002
    run_server(
        port=port,
        name="Calendar Agent",
        description="Добавление событий в локальный календарь",
        skill_id="add_event",
        skill_name="Add Calendar Event",
        skill_desc="JSON: title, date, time, description",
        handler=handle,
    )
