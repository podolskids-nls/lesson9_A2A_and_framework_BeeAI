#!/usr/bin/env python3
"""A2A Orchestrator: discovery агентов → sendMessage → LLM (OpenRouter/Groq)."""
from __future__ import annotations

import asyncio
import json
import sys
from typing import Any

import httpx
from a2a.client import A2ACardResolver, ClientConfig, create_client
from a2a.helpers import get_artifact_text, new_text_message
from a2a.types.a2a_pb2 import Role, SendMessageRequest

from shared.config import CALENDAR_AGENT_URL, FLIGHT_AGENT_URL, create_llm_client

DEFAULT_PROMPT = (
    "Я лечу в Москву 25 мая рейсом SU-123. "
    "Найди информацию о рейсе и занеси мне это в календарь."
)

TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "name": "call_flight_agent",
        "description": "A2A: запросить данные рейса. Дата YYYY-MM-DD.",
        "parameters": {
            "type": "object",
            "properties": {
                "flight_number": {"type": "string"},
                "date": {"type": "string"},
            },
            "required": ["flight_number", "date"],
        },
    },
    {
        "type": "function",
        "name": "call_calendar_agent",
        "description": "A2A: добавить событие в календарь.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "date": {"type": "string"},
                "time": {"type": "string"},
                "description": {"type": "string"},
            },
            "required": ["title", "date", "time", "description"],
        },
    },
]

INSTRUCTIONS = """Ты Orchestrator в A2A-системе.
1. Анализируй запрос, вызывай call_flight_agent и call_calendar_agent по порядку.
2. Не выдумывай данные рейса — только из ответа flight agent.
3. Дату в формат YYYY-MM-DD (25 мая → 2025-05-25 если год не указан).
4. Финальный ответ на русском, без новых вызовов инструментов."""


def log(who: str, msg: str) -> None:
    print(f"[{who}]: {msg}")


async def discover(url: str) -> Any:
    async with httpx.AsyncClient() as http:
        card = await A2ACardResolver(http, url).get_agent_card()
    log("Orchestrator", f"Зарегистрирован: {card.name} @ {url}")
    return card



def _a2a_event_text(event: Any) -> str | None:
    """Текст из A2A StreamResponse (Task/Artifact), не RAG."""
    task = getattr(event, "task", None)
    if task and task.artifacts:
        lines = [p.text for a in task.artifacts for p in a.parts if p.text]
        if lines:
            return "\n".join(lines)
    try:
        return get_artifact_text(event)
    except (AttributeError, TypeError):
        return None

async def a2a_send(card: Any, text: str) -> str:
    client = await create_client(agent=card, client_config=ClientConfig(streaming=False))
    req = SendMessageRequest(message=new_text_message(text, role=Role.ROLE_USER))
    parts: list[str] = []
    async for event in client.send_message(req):
        t = _a2a_event_text(event)
        if t:
            parts.append(t)
    await client.close()
    return "\n".join(parts) or "(пустой ответ агента)"


async def run_tool(name: str, args: dict[str, Any], cards: dict[str, Any]) -> str:
    if name == "call_flight_agent":
        text = json.dumps(args, ensure_ascii=False)
        log("Orchestrator", f">>> Flight Agent: {text}")
        out = await a2a_send(cards["flight"], text)
        log("Orchestrator", "<<< Flight Agent ответил")
        return out
    if name == "call_calendar_agent":
        text = json.dumps(args, ensure_ascii=False)
        log("Orchestrator", f">>> Calendar Agent: {text}")
        out = await a2a_send(cards["calendar"], text)
        log("Orchestrator", "<<< Calendar Agent ответил")
        return out
    return json.dumps({"error": f"unknown tool {name}"})


async def orchestrate(user_prompt: str) -> str:
    cards = {
        "flight": await discover(FLIGHT_AGENT_URL),
        "calendar": await discover(CALENDAR_AGENT_URL),
    }
    client, model = create_llm_client()
    log("Orchestrator", f"LLM: {model}")
    log("Пользователь", user_prompt)

    messages: list[Any] = [{"role": "user", "content": user_prompt}]
    for step in range(1, 11):
        log("Orchestrator", f"--- шаг {step} ---")
        response = client.responses.create(
            model=model,
            instructions=INSTRUCTIONS,
            tools=TOOLS,
            input=messages,
        )
        output = list(response.output)
        messages.extend(output)
        calls = [x for x in output if x.type == "function_call"]
        if not calls:
            return response.output_text or ""
        for call in calls:
            args = json.loads(call.arguments or "{}")
            result = await run_tool(call.name, args, cards)
            messages.append(
                {"type": "function_call_output", "call_id": call.call_id, "output": result}
            )
    raise RuntimeError("лимит 10 шагов")


def main() -> None:
    prompt = " ".join(sys.argv[1:]).strip() or DEFAULT_PROMPT
    print("=" * 60)
    print("A2A: Orchestrator + Flight + Calendar")
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
