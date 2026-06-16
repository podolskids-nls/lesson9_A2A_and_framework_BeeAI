# Lesson 9 — A2A через BeeAI Framework

Параллельная реализация в подпапке `framework/`: тот же протокол Google A2A, но runtime — **BeeAI Framework** (`A2AServer` / `A2AAgent` / `RequirementAgent`).

| Агент | Порт | Harness |
|-------|------|---------|
| Flight Agent | 8001 | `HandlerRunnable` + `A2AServer` |
| Calendar Agent | 8002 | `HandlerRunnable` + `A2AServer` |
| Orchestrator | CLI | `RequirementAgent.run()` + `A2AAgent` clients |

## Отличия от корневой версии

| | Корень (`orchestrator.py`) | `framework/` (BeeAI) |
|---|---|---|
| A2A server | ручной `a2a-sdk` wrapper | `A2AServer.register(...).serve()` |
| A2A client | `a2a.client.create_client` | `A2AAgent(url=...).run()` |
| Orchestrator LLM | OpenAI SDK + function tools | `RequirementAgent` + `@tool` |
| Server agents | plain Python handlers | `HandlerRunnable` (без LLM на сервере) |

Протокол сохранён: `GET /.well-known/agent-card.json`, JSON-RPC `message/send`, skills `get_flight` / `add_event`.

## Настройка

```bash
pip install -r framework/requirements.txt
cp .env.example .env   # ключи OpenRouter и/или Groq — из корня проекта
```

Важно: `starlette>=0.52.1,<0.53` (BeeAI несовместим со Starlette 1.x). На Python 3.14 в `framework/shared/llm.py` есть обход pydantic-бага BeeAI.

## Запуск

```bash
# Терминал 1 — из корня проекта
python framework/start_agents.py

# Терминал 2
python framework/run_orchestrator.py
```

Демо-промпт по умолчанию: рейс SU-123, 25 мая → календарь.

## Структура

```
framework/
├── agents/
│   ├── flight_server.py      # A2AServer + mock flights
│   ├── calendar_server.py    # A2AServer + calendar.json
│   └── orchestrator.py       # RequirementAgent harness
├── shared/
│   ├── handler_runnable.py   # Runnable без LLM для server agents
│   └── llm.py                # OpenRouter / Groq для orchestrator
├── start_agents.py
├── run_orchestrator.py
└── requirements.txt
```

Бизнес-логика переиспользуется из `shared/flight_api.py`, `shared/calendar_api.py`, `shared/config.py` (корень проекта).
