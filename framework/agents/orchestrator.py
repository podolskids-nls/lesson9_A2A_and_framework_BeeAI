#!/usr/bin/env python3
"""BeeAI Orchestrator: RequirementAgent + A2AAgent clients (OpenRouter/Groq)."""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from beeai_framework.adapters.a2a.agents import A2AAgent
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.tools import tool
from beeai_framework.tools.types import StringToolOutput

from framework.shared.llm import create_chat_model
from shared.config import CALENDAR_AGENT_URL, FLIGHT_AGENT_URL

DEFAULT_PROMPT = (
    "Я лечу в Москву 25 мая рейсом SU-123. "
    "Найди информацию о рейсе и занеси мне это в календарь."
)

INSTRUCTIONS = """Ты Orchestrator в A2A-системе.
1. Анализируй запрос, вызывай call_flight_agent и call_calendar_agent по порядку.
2. Не выдумывай данные рейса — только из ответа flight agent.
3. Дату в формат YYYY-MM-DD (25 мая → 2025-05-25 если год не указан).
4. Финальный ответ на русском, без новых вызовов инструментов."""


def log(who: str, msg: str) -> None:
    print(f"[{who}]: {msg}")


@tool
async def call_flight_agent(flight_number: str, date: str) -> StringToolOutput:
    """A2A: запросить данные рейса. Дата YYYY-MM-DD."""
    payload = json.dumps({"flight_number": flight_number, "date": date}, ensure_ascii=False)
    log("Orchestrator", f">>> Flight Agent: {payload}")
    client = A2AAgent(url=FLIGHT_AGENT_URL, memory=UnconstrainedMemory())
    response = await client.run(payload)
    log("Orchestrator", "<<< Flight Agent ответил")
    return StringToolOutput(response.last_message.text)


@tool
async def call_calendar_agent(
    title: str,
    date: str,
    time: str,
    description: str,
) -> StringToolOutput:
    """A2A: добавить событие в календарь."""
    payload = json.dumps(
        {"title": title, "date": date, "time": time, "description": description},
        ensure_ascii=False,
    )
    log("Orchestrator", f">>> Calendar Agent: {payload}")
    client = A2AAgent(url=CALENDAR_AGENT_URL, memory=UnconstrainedMemory())
    response = await client.run(payload)
    log("Orchestrator", "<<< Calendar Agent ответил")
    return StringToolOutput(response.last_message.text)


async def orchestrate(user_prompt: str) -> str:
    log("Orchestrator", f"Flight URL: {FLIGHT_AGENT_URL}")
    log("Orchestrator", f"Calendar URL: {CALENDAR_AGENT_URL}")
    log("Пользователь", user_prompt)

    agent = RequirementAgent(
        llm=create_chat_model(),
        tools=[call_flight_agent, call_calendar_agent],
        memory=UnconstrainedMemory(),
        instructions=INSTRUCTIONS,
    )
    response = await agent.run(user_prompt, total_max_retries=10)
    return response.last_message.text


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    prompt = " ".join(sys.argv[1:]).strip() or DEFAULT_PROMPT
    print("=" * 60)
    print("BeeAI A2A: Orchestrator + Flight + Calendar")
    print("=" * 60)
    try:
        answer = asyncio.run(orchestrate(prompt))
    except Exception as exc:
        print(f"\n[Ошибка]: {exc}", file=sys.stderr)
        sys.exit(1)
    print("\n" + "=" * 60)
    print("[Итог]")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()
