# DEPRECATED: use orchestrator.py + flight_server.py + calendar_server.py

#!/usr/bin/env python3
"""
A2A (Agent-to-Agent) demo: Orchestrator + Flight Agent + Calendar Agent.

Использует OpenAI Python SDK + бесплатный OpenRouter API (как в Lesson_8_My_own_agent).
Оркестратор делегирует задачи через Function Calling (call_flight_agent, call_calendar_agent).
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
CALENDAR_FILE = BASE_DIR / "calendar.json"
LESSON8_ENV = BASE_DIR.parent / "Lesson_8_My_own_agent" / ".env"

DEFAULT_USER_PROMPT = (
    "Я лечу в Москву 25 мая рейсом SU-123. "
    "Найди информацию о рейсе и занеси мне это в календарь."
)


def load_environment() -> None:
    load_dotenv(BASE_DIR / ".env")
    if LESSON8_ENV.exists():
        load_dotenv(LESSON8_ENV, override=False)


def create_client() -> OpenAI:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY не найден. Скопируйте .env.example в .env "
            "или используйте ключ из Lesson_8_My_own_agent/.env"
        )
    return OpenAI(
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        api_key=api_key,
    )


def get_model() -> str:
    return os.getenv("OPENROUTER_MODEL", "openrouter/free")


def log(agent: str, message: str) -> None:
    print(f"[{agent}]: {message}")


# ---------------------------------------------------------------------------
# Flight Agent — mock API (без авторизации), имитирует публичный сервис рейсов
# ---------------------------------------------------------------------------

MOCK_FLIGHTS: dict[str, dict[str, str]] = {
    "SU-123": {
        "airline": "Аэрофлот",
        "route": "Санкт-Петербург (LED) → Москва (SVO)",
        "status": "По расписанию",
        "departure_time": "10:30",
        "arrival_time": "12:15",
        "terminal": "B",
        "gate": "12",
    },
    "SU-456": {
        "airline": "Аэрофлот",
        "route": "Москва (SVO) → Казань (KZN)",
        "status": "Задержан на 45 мин",
        "departure_time": "14:00",
        "arrival_time": "15:50",
        "terminal": "D",
        "gate": "7",
    },
}


def mock_flight_api_lookup(flight_number: str, date: str) -> dict[str, Any]:
    """Имитация HTTP-запроса к бесплатному API авиарейсов."""
    normalized = flight_number.strip().upper().replace(" ", "")
    log("Flight API (mock)", f"GET /flights/{normalized}?date={date}")

    record = MOCK_FLIGHTS.get(normalized)
    if not record:
        return {
            "found": False,
            "flight_number": normalized,
            "date": date,
            "message": f"Рейс {normalized} на {date} не найден в mock-базе.",
        }

    return {
        "found": True,
        "flight_number": normalized,
        "date": date,
        **record,
    }


def run_flight_agent(flight_number: str, date: str) -> str:
    """Flight Agent: получает номер рейса и дату, возвращает структурированный ответ."""
    log("Flight Agent", f"Получен запрос: рейс {flight_number}, дата {date}")
    log("Flight Agent", "Обращаюсь к mock API авиарейсов...")

    raw = mock_flight_api_lookup(flight_number, date)

    if not raw.get("found"):
        result = (
            f"Рейс {raw['flight_number']} на {raw['date']}: данные не найдены. "
            f"{raw.get('message', '')}"
        )
    else:
        result = (
            f"Рейс: {raw['flight_number']}\n"
            f"Дата: {raw['date']}\n"
            f"Авиакомпания: {raw['airline']}\n"
            f"Маршрут: {raw['route']}\n"
            f"Статус: {raw['status']}\n"
            f"Вылет: {raw['departure_time']}\n"
            f"Прилёт: {raw['arrival_time']}\n"
            f"Терминал: {raw['terminal']}, гейт: {raw['gate']}"
        )

    log("Flight Agent", "Ответ сформирован, возвращаю оркестратору")
    return result


# ---------------------------------------------------------------------------
# Calendar Agent — «база данных» в calendar.json
# ---------------------------------------------------------------------------

def save_to_calendar(title: str, date: str, time: str, description: str) -> dict[str, Any]:
    """Mock open API: сохраняет событие в локальный JSON-файл."""
    log("Calendar API (mock)", f"POST /events -> {CALENDAR_FILE.name}")

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
    CALENDAR_FILE.write_text(
        json.dumps(events, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return {"success": True, "event": event}


def run_calendar_agent(title: str, date: str, time: str, description: str) -> str:
    """Calendar Agent: сохраняет событие и возвращает подтверждение."""
    log(
        "Calendar Agent",
        f"Получен запрос: «{title}» {date} {time}",
    )
    log("Calendar Agent", "Сохраняю событие в calendar.json...")

    payload = save_to_calendar(title, date, time, description)
    event = payload["event"]

    result = (
        f"Событие успешно добавлено в календарь (id={event['id']}).\n"
        f"Название: {event['title']}\n"
        f"Дата: {event['date']}, время: {event['time']}\n"
        f"Описание: {event['description']}"
    )
    log("Calendar Agent", "Запись подтверждена, возвращаю оркестратору")
    return result


# ---------------------------------------------------------------------------
# Orchestrator — Function Calling через OpenRouter (OpenAI SDK)
# ---------------------------------------------------------------------------

ORCHESTRATOR_TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "name": "call_flight_agent",
        "description": (
            "Вызывает специализированного агента рейсов. "
            "Передай номер рейса и дату в формате YYYY-MM-DD."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "flight_number": {
                    "type": "string",
                    "description": "Номер рейса, например SU-123",
                },
                "date": {
                    "type": "string",
                    "description": "Дата рейса в формате YYYY-MM-DD",
                },
            },
            "required": ["flight_number", "date"],
        },
    },
    {
        "type": "function",
        "name": "call_calendar_agent",
        "description": (
            "Вызывает специализированного агента календаря для создания события. "
            "Используй данные из запроса пользователя и ответа flight agent."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Краткое название события",
                },
                "date": {
                    "type": "string",
                    "description": "Дата события YYYY-MM-DD",
                },
                "time": {
                    "type": "string",
                    "description": "Время события HH:MM",
                },
                "description": {
                    "type": "string",
                    "description": "Подробное описание события",
                },
            },
            "required": ["title", "date", "time", "description"],
        },
    },
]

ORCHESTRATOR_INSTRUCTIONS = """Ты — Orchestrator Agent в многоагентной системе A2A.

Твоя роль:
1. Проанализировать комплексный запрос пользователя.
2. Построить план: какие специализированные агенты нужно вызвать и в каком порядке.
3. Вызывать инструменты call_flight_agent и call_calendar_agent — сам ты не ходишь во внешние API.
4. После получения результатов от агентов — собрать понятный финальный ответ на русском.

Правила:
- Если пользователь просит информацию о рейсе — сначала вызови call_flight_agent.
- Если просит занести в календарь — вызови call_calendar_agent с данными из запроса и ответа flight agent.
- Не выдумывай статус рейса, время и терминал — только факты из ответа call_flight_agent.
- Дату переводи в формат YYYY-MM-DD (например, «25 мая» -> 2025-05-25, если год не указан — текущий или из контекста).
- Вызывай агентов по очереди: сначала рейс, потом календарь (если нужны оба).
- Когда все нужные инструменты вызваны — дай итоговый ответ без новых вызовов инструментов."""


def execute_orchestrator_tool(name: str, arguments: dict[str, Any]) -> str:
    if name == "call_flight_agent":
        log("Orchestrator", ">>> Передаю управление Flight Agent")
        result = run_flight_agent(
            flight_number=arguments.get("flight_number", ""),
            date=arguments.get("date", ""),
        )
        log("Orchestrator", "<<< Получен ответ от Flight Agent")
        return result

    if name == "call_calendar_agent":
        log("Orchestrator", ">>> Передаю управление Calendar Agent")
        result = run_calendar_agent(
            title=arguments.get("title", ""),
            date=arguments.get("date", ""),
            time=arguments.get("time", ""),
            description=arguments.get("description", ""),
        )
        log("Orchestrator", "<<< Получен ответ от Calendar Agent")
        return result

    return json.dumps({"error": f"Неизвестный инструмент: {name}"}, ensure_ascii=False)


def log_response_output(output: list[Any], step: int) -> None:
    types = [getattr(item, "type", type(item).__name__) for item in output]
    log("Orchestrator", f"Шаг {step}: типы ответа модели — {', '.join(types) or '(пусто)'}")
    for item in output:
        if getattr(item, "type", None) == "function_call":
            log(
                "Orchestrator",
                f"  function_call: {item.name}({item.arguments})",
            )


def run_orchestrator(client: OpenAI, user_prompt: str) -> str:
    log("Orchestrator", "Старт обработки запроса пользователя")
    log("Пользователь", user_prompt)

    model = get_model()
    log("Orchestrator", f"Модель: {model}")

    input_messages: list[Any] = [{"role": "user", "content": user_prompt}]

    for step in range(1, 11):
        log("Orchestrator", f"--- Шаг {step}: запрос к LLM ---")
        response = client.responses.create(
            model=model,
            instructions=ORCHESTRATOR_INSTRUCTIONS,
            tools=ORCHESTRATOR_TOOLS,
            input=input_messages,
        )

        output = list(response.output)
        log_response_output(output, step)
        input_messages.extend(output)

        function_calls = [item for item in output if item.type == "function_call"]
        if not function_calls:
            final_text = response.output_text or ""
            log("Orchestrator", "Финальный ответ сформирован")
            return final_text

        for tool_call in function_calls:
            args = json.loads(tool_call.arguments or "{}")
            log(
                "Orchestrator",
                f"Вызов инструмента «{tool_call.name}» с аргументами: {args}",
            )
            tool_result = execute_orchestrator_tool(tool_call.name, args)
            input_messages.append(
                {
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": tool_result,
                }
            )

    raise RuntimeError("Превышен лимит шагов оркестратора (10)")


def configure_console_encoding() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")


def main() -> None:
    configure_console_encoding()
    load_environment()

    user_prompt = " ".join(sys.argv[1:]).strip() or DEFAULT_USER_PROMPT
    client = create_client()

    print("=" * 60)
    print("A2A System: Orchestrator + Flight Agent + Calendar Agent")
    print("=" * 60)

    try:
        final_answer = run_orchestrator(client, user_prompt)
    except Exception as exc:
        print(f"\n[Ошибка]: {exc}", file=sys.stderr)
        sys.exit(1)

    print("\n" + "=" * 60)
    print("[Итог для пользователя]")
    print("=" * 60)
    print(final_answer)

    if CALENDAR_FILE.exists():
        print("\n" + "-" * 60)
        print(f"[calendar.json] Содержимое файла {CALENDAR_FILE.name}:")
        print("-" * 60)
        print(CALENDAR_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
