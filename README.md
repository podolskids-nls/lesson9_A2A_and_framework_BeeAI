# Lesson 9 — A2A (Agent-to-Agent)

Три агента по протоколу **Google A2A** (`a2a-sdk`): оркестратор делегирует задачи по HTTP.

| Агент | Порт | Назначение |
|-------|------|------------|
| Flight Agent | 8001 | Mock API рейсов (SU-123, SU-456) |
| Calendar Agent | 8002 | События в `calendar.json` |
| Orchestrator | CLI | LLM (OpenRouter/Groq) + A2A client |

## Настройка

```bash
pip install -r requirements.txt
cp .env.example .env   # вписать ключи OpenRouter и/или Groq
```

`LLM_PROVIDER=openrouter` или `groq`. Платный OpenAI API не используется.

## Запуск

```bash
# Терминал 1
python start_agents.py

# Терминал 2
python orchestrator.py
```

Демо-промпт по умолчанию: рейс SU-123, 25 мая → календарь.

## A2A flow

1. `GET /.well-known/agent.json` — Agent Card
2. `sendMessage` (JSON-RPC) — Task + Artifact
