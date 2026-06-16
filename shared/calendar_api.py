"""Локальный календарь (calendar.json), без авторизации."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from shared.config import BASE_DIR

CALENDAR_FILE = BASE_DIR / "calendar.json"


def add_event(title: str, date: str, time: str, description: str) -> str:
    events: list[dict[str, Any]] = []
    if CALENDAR_FILE.exists():
        try:
            events = json.loads(CALENDAR_FILE.read_text(encoding="utf-8"))
            if not isinstance(events, list):
                events = []
        except json.JSONDecodeError:
            events = []

    event = {
        "id": len(events) + 1,
        "title": title,
        "date": date,
        "time": time,
        "description": description,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    events.append(event)
    CALENDAR_FILE.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
    return (
        f"Событие добавлено (id={event['id']}).\n"
        f"Название: {title}\nДата: {date}, время: {time}\nОписание: {description}"
    )
