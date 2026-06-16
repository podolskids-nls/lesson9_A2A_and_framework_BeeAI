# Subagent — Explore the project at c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agen

_Дата: 2026-06-16 | Chat ID: `0b288652-e6c3-41eb-b8af-ae42256b8c09` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Explore the project at c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A) thoroughly. Find:
1. What already exists in the workspace
2. Any starter code, README, dependencies
3. Any references to A2A protocol

Return a concise summary of current state.

### Ассистент

I'll scan the project layout, docs, and dependencies first, then search for A2A protocol references.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

The path with parentheses may be causing issues — trying alternate path formats.

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

- **Tool `Glob`**

- **Tool `Glob`**

- **Tool `Grep`**

- **Tool `Glob`**

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

## Current State Summary

The workspace at `c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)` is **minimal and self-contained** — only **3 files**, no README, no git repo, no tests.

### 1. What Exists

| File | Purpose |
|------|---------|
| `a2a_system.py` | Full runnable demo (~375 lines) |
| `requirements.txt` | Python dependencies |
| `.env.example` | OpenRouter API config template |

**Not present:** README, `.git`, `.env`, `calendar.json` (created at runtime), tests, Docker, or other config files.

### 2. Starter Code & Dependencies

**Architecture (conceptual A2A, not a wire protocol):**

- **Orchestrator Agent** — LLM via OpenRouter (OpenAI SDK `responses.create`) with function calling
- **Flight Agent** — mock flight lookup (`SU-123`, `SU-456`) via in-process `run_flight_agent()`
- **Calendar Agent** — writes events to `calendar.json` via `run_calendar_agent()`

**Flow:** User prompt → Orchestrator plans → calls `call_flight_agent` / `call_calendar_agent` tools → agents run in-process → Orchestrator returns a final Russian-language answer.

**Default demo prompt:**
> «Я лечу в Москву 25 мая рейсом SU-123. Найди информацию о рейсе и занеси мне это в календарь.»

**Dependencies** (`requirements.txt`):
- `openai>=1.68.0`
- `python-dotenv>=1.0.0`

**Env vars** (`.env.example`):
- `OPENROUTER_API_KEY`
- `OPENROUTER_BASE_URL` (default: `https://openrouter.ai/api/v1`)
- `OPENROUTER_MODEL` (default: `openrouter/free`)

**Cross-lesson link:** Can reuse `OPENROUTER_API_KEY` from sibling project `Lesson_8_My_own_agent/.env`.

**Run:** `python a2a_system.py` (optional custom prompt as CLI args).

### 3. A2A Protocol References

**Naming only — not the official Google Agent2Agent protocol.**

References to "A2A" / "Agent-to-Agent" appear only in:
- Module docstring (line 3)
- Orchestrator system prompt (line 247)
- Startup banner (line 352)

**No implementation of the formal A2A protocol:**
- No `a2a-sdk`, Google ADK, Agent Cards, HTTP endpoints, or JSON-RPC
- No `protocol`, `AgentCard`, or similar terms in the codebase

**Actual pattern:** In-process multi-agent orchestration using **OpenAI Function Calling** — agents are Python functions invoked by the Orchestrator LLM, not separate network services.

---

**Bottom line:** This is a **lesson starter/demo** for the *idea* of agent-to-agent delegation (Orchestrator → Flight → Calendar), built on the same OpenRouter stack as Lesson 8. It is ready to run once dependencies are installed and an API key is configured, but it does not yet use the official A2A wire protocol.

---
