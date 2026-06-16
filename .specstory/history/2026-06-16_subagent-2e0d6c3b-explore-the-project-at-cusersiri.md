# Subagent — Explore the project at c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agen

_Дата: 2026-06-16 | Chat ID: `2e0d6c3b-95de-468f-9788-8c5aaafeef88` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Explore the project at c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A) thoroughly. Find:
1. What already exists in the workspace
2. Any starter code, README, dependencies
3. Any references to A2A protocol

Return a concise summary of current state.

### Ассистент

I'll scan the workspace structure, docs, dependencies, and any A2A-related references.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

Trying alternate paths — the workspace path may need different formatting.

- **Tool `Glob`**

- **Tool `Grep`**

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\a2a_system.py

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\requirements.txt

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\.env.example

- **Tool `Grep`**

---

### Ассистент

- **Tool `Grep`**

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

- **Tool `Glob`**

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

## Current State Summary

The workspace at `c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)` is **minimal and self-contained** — only **3 files**, no git repo, no README, no tests, no config beyond env vars.

### 1. What Exists

| File | Purpose |
|------|---------|
| `a2a_system.py` | Full runnable demo (~375 lines) |
| `requirements.txt` | Python dependencies |
| `.env.example` | OpenRouter API config template |

**Not present:** README, `calendar.json` (created at runtime), `.env`, git, Docker, tests, or other subfolders.

### 2. Starter Code & Dependencies

**Architecture** — a 3-agent pattern in one Python script:

- **Orchestrator Agent** — LLM via OpenRouter (OpenAI SDK `responses.create` + function calling)
- **Flight Agent** — mock flight lookup (`MOCK_FLIGHTS` for SU-123, SU-456)
- **Calendar Agent** — persists events to `calendar.json`

**Default scenario:** user asks to look up flight SU-123 to Moscow on May 25 and add it to the calendar.

**Dependencies** (`requirements.txt`):
- `openai>=1.68.0`
- `python-dotenv>=1.0.0`

**Config** (`.env.example`):
- `OPENROUTER_API_KEY`
- `OPENROUTER_BASE_URL` (default: `https://openrouter.ai/api/v1`)
- `OPENROUTER_MODEL` (default: `openrouter/free`)

**Cross-lesson link:** falls back to `../Lesson_8_My_own_agent/.env` for the API key if local `.env` is missing.

**Run:** `python a2a_system.py` (optional custom prompt as CLI args).

### 3. A2A Protocol References

**Conceptual only — not the official Google A2A protocol.**

"A2A" appears only in comments, orchestrator instructions, and a startup banner in `a2a_system.py`. There are **no** references to:

- Google ADK / A2A SDK
- Agent Cards (`/.well-known/agent.json`)
- JSON-RPC, `/tasks`, streaming task APIs
- HTTP agent-to-agent endpoints

**Actual delegation mechanism:** in-process function calling (`call_flight_agent`, `call_calendar_agent`) — the orchestrator invokes Python functions directly, not remote agents over a wire protocol.

### Bottom Line

This is a **Lesson 9 starter/demo** for multi-agent orchestration patterns, built on the same OpenRouter stack as Lesson 8. It teaches agent delegation conceptually but does **not** implement the formal [Google Agent2Agent (A2A) protocol](https://google.github.io/A2A/). To align with that protocol, you would need separate agent servers, discovery, and the A2A task/message API — none of which exist here yet.

---
