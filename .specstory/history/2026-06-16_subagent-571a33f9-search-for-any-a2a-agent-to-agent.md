# Subagent — Search for any A2A (Agent to Agent) related code, agent-card, sendMess

_Дата: 2026-06-16 | Chat ID: `571a33f9-1d3f-43f6-a936-3e23d8d5e5dd` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Search for any A2A (Agent to Agent) related code, agent-card, sendMessage, orchestrator patterns in:
- C:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)
- C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent
- Parent folder C:\Users\Irina\IT\AI_DRIVEN if needed

Also search for any lesson materials about A2A protocol. Return what you find about A2A implementation approach expected.

### Ассистент

Searching the three directories for A2A-related code, agent-card, sendMessage, orchestrator patterns, and lesson materials.

- **Tool `UpdateCurrentStep`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

Narrowing searches to specific lesson folders and excluding node_modules.

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

- **Tool `Shell`**: List Lesson 9 and parent AI_DRIVEN dirs

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Glob`**

---

### Ассистент

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Glob`**

- **Tool `Glob`**

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Урок_8_Агенты Практика.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

---

### Ассистент

- **Tool `Shell`**: Find Lesson 9 and A2A materials in parent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\agent-transcripts

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_5_multiexpert

---

### Ассистент

Reading lesson slides and the full task description from agent transcripts.

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\agent-transcripts\39235d22-fb08-40ba-ab49-fac8d8e518f9\39235d22-fb08-40ba-ab49-fac8d8e518f9.jsonl

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\assets\c__Users_Irina_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_image-20352631-6080-4e04-bc24-401f7be5ec0f.png

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\assets\c__Users_Irina_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_image-213de904-777b-4bfb-9dc5-d3d9678fad33.png

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\agent-transcripts\39235d22-fb08-40ba-ab49-fac8d8e518f9\subagents\b9cdfc56-40d1-49cd-9b90-dff382cdf7f6.jsonl

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.venv\Lib\site-packages\vertexai\preview\reasoning_engines\templates\a2a.py

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Glob`**

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

## Search Results Summary

### `Lesson_9_Agent2Agent (A2A)` — **empty**

`C:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)` exists but contains **zero files** (no code, README, dependencies, or git repo). There is also **no** `Lesson_9_*.zip` in the parent folder (unlike Lessons 3, 5, 7, 8).

**No matches** for: `A2A`, `agent-card`, `sendMessage`, `orchestrator` in this folder.

---

### `Lesson_8_My_own_agent` — **single-agent patterns, not A2A**

No A2A-related code. This is Lesson 8’s **OpenAI Responses API** practice project:

| File | Purpose |
|------|---------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Structured JSON output |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Function calling (coffee demo) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | RAG + MCP + skill |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | Local MCP server (SSE :8765) |

**Free API pattern to reuse:** Groq / OpenRouter via the `openai` npm package (`^6.42.0`), configured in `.env` (`GROQ_API_KEY`, `OPENROUTER_API_KEY`, `LLM_PROVIDER`). No flight or calendar APIs — only LLM + RAG/MCP over project TZ documents.

Lesson materials: `C:\Users\Irina\IT\AI_DRIVEN\Урок_8_Агенты Практика.md` — covers Practices 1–3 (structured output, function calling, RAG/MCP/skills). **No A2A content.**

---

### Parent `C:\Users\Irina\IT\AI_DRIVEN` — **no official Lesson 9 materials**

Found lesson docs for earlier lessons only:

- `C:\Users\Irina\IT\AI_DRIVEN\Урок_8_Агенты Практика.md`
- `C:\Users\Irina\IT\AI_DRIVEN\Урок_8_[Агенты_в_разработке] - 09.06.pptx`
- Other pptx/docx for Lessons 1, 2, 5

**No** Lesson 9 pptx, docx, md, or zip with A2A protocol documentation.

---

### A2A lesson materials found (Cursor project assets / user slides)

The only A2A lesson content is in the current Cursor session — two slides attached to your task:

#### Slide 1 — Practice task (~20 min, OpenAI SDK)

- **Task:** Write **3 agents**
  1. **Orchestrator** — accepts a prompt, **registers agents**
  2. **Flight agent** — registers/fetches a flight
  3. **Calendar agent** — adds an event to a calendar

#### Slide 2 — A2A protocol (from webinar slide by Nikolay Baryshnikov)

| Concept | Expected implementation |
|---------|-------------------------|
| **Agent Card** | JSON self-description at `/.well-known/agent-card.json` — name, capabilities, skills, security schemes, supported interfaces |
| **Orchestrator (Client Agent)** | Entry point that discovers remote agents via Agent Cards and routes tasks (e.g. flight → calendar) |
| **Discovery** | `GET /.well-known/agent-card` → returns Agent Card |
| **Authentication** | JWT via `securitySchemes` in Agent Card (Auth Server flow) |
| **sendMessage** | `POST /sendMessage` with JWT → creates a **Task**, returns Task response |
| **sendMessageStream** | `POST /sendMessageStream` → SSE stream of `TaskStatusUpdateEvent`, `TaskArtifactUpdateEvent` |
| **Core entities** | **Task** (status, message history, artifacts), **Message** (Role + Parts: text/file/URL/JSON), **Artifact** (result) |
| **Transport** | JSON-RPC-style messages over HTTP |

#### Your explicit task constraints (from chat)

- Orchestrator receives a task, calls flight agent, then calendar agent
- **Without authentication** — simpler than the full JWT flow on the slide
- Use **free APIs** like Lesson 8 (Groq/OpenRouter for LLM)
- Build real **A2A** (not just in-process function calls)

---

### Other `orchestrator` / `sendMessage` hits (not A2A lesson code)

| Location | What it is |
|----------|------------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_5_multiexpert\openspec-propose\...` | `ConnectorOrchestrator` — hotel booking pipeline, unrelated to A2A |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.venv\...` | Google Vertex AI `a2a` Python SDK (`AgentCard`, `SendMessageRequest`, `RESTAdapter`) — dependency only, not lesson source |

Example of what the Vertex SDK expects (in venv, not your code):

```52:108:C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.venv\Lib\site-packages\vertexai\preview\reasoning_engines\templates\a2a.py
def create_agent_card(
    agent_name: Optional[str] = None,
    description: Optional[str] = None,
    skills: Optional[List["AgentSkill"]] = None,
    ...
) -> "AgentCard":
    ...
    return AgentCard(
        name=agent_name,
        description=description,
        url="http://localhost:9999/",
        ...
        preferred_transport=TransportProtocol.http_json,
        ...
    )
```

---

## Expected A2A Implementation Approach

Based on slides + your task + Lesson 8 patterns:

1. **Three separate HTTP services** (or three processes), each exposing A2A endpoints:
   - Orchestrator (client agent)
   - Flight agent (remote agent)
   - Calendar agent (remote agent)

2. **Each remote agent publishes an Agent Card** at `/.well-known/agent-card.json` describing its skills and API URL.

3. **Orchestrator discovers and registers agents** by fetching their Agent Cards, then routes work via **`POST /sendMessage`** (skip JWT since you asked for no auth).

4. **Task lifecycle:** submitted → working → completed, with **Messages** and **Artifacts** passed between agents.

5. **LLM layer:** reuse Lesson 8’s OpenAI SDK + Groq/OpenRouter for agent reasoning inside each service.

6. **Domain APIs:** flight and calendar integrations are **not** in Lesson 8 — you’ll need mocks or free APIs (e.g. OpenSky for flights, local `.ics` file for calendar).

7. **Suggested structure** (nothing exists yet):

```
Lesson_9_Agent2Agent (A2A)/
├── orchestrator/orchestrator.mjs
├── agents/flight/server.mjs + agent-card.json
├── agents/calendar/server.mjs + agent-card.json
└── shared/a2a-types.mjs
```

---

## Bottom Line

- **No A2A implementation exists** in any of the searched lesson folders.
- **Lesson 9 is a blank workspace** — everything must be built from scratch.
- **Lesson 8** provides the **LLM/tooling pattern** (OpenAI Responses API + free providers), not A2A.
- **A2A requirements** come from the **practice slides** (3 agents + orchestrator) and the **protocol slide** (Agent Card, `sendMessage`, Task/Message/Artifact model), with your simplification of **no authentication**.

---
