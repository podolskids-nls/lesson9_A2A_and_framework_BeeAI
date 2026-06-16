#!/usr/bin/env python3
"""A2A Flight Agent — mock API рейсов."""
from __future__ import annotations

import json
import re
import sys

from shared.a2a_app import run_server
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


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    run_server(
        port=port,
        name="Flight Agent",
        description="Информация о рейсах (mock API)",
        skill_id="get_flight",
        skill_name="Get Flight Info",
        skill_desc="Номер рейса и дата (JSON или текст)",
        handler=handle,
    )
