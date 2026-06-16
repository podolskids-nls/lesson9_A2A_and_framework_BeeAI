# Subagent — Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_age

_Дата: 2026-06-16 | Chat ID: `a1e4c699-82f7-4139-9b77-373e14a695c1` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent thoroughly. Find:
1. What free APIs are used (flight, calendar, etc.)
2. How agents are structured (OpenAI SDK, frameworks)
3. Key files and patterns for agent implementation
4. Dependencies (requirements.txt, package.json)
5. Any A2A or agent card patterns

Return a concise summary with file paths and API endpoints used.

### Ассистент

Exploring the Lesson_8 project structure, dependencies, and agent/API patterns.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

- **Tool `UpdateCurrentStep`**

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Glob`**

---

### Ассистент

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.gitignore

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Glob`**

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.env.example

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\client.py

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

# Lesson 8 — Project Summary

**Path:** `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent`

This is a **technical-specification (TZ) agent** lesson with three progressive practices. It does **not** use flight, calendar, weather, or similar domain APIs.

---

## 1. APIs & Endpoints Used

| Service | Endpoint | Purpose | Free tier? |
|---------|----------|---------|------------|
| **OpenRouter** | `https://openrouter.ai/api/v1` | LLM via Responses API; model `openrouter/free` | Yes (free model) |
| **Groq** | `https://api.groq.com/openai/v1` | Alternative LLM provider (e.g. `llama-3.3-70b-versatile`) | Yes (with API key) |
| **ChromaDB** (local) | `localhost:8000` | Vector store for RAG (via Lesson 7) | Local/Docker |
| **MCP server** (local) | `http://127.0.0.1:8765/sse` | SSE MCP for index status & docs | Local |
| **localhost.run** (tunnel) | `https://xxxxx.lhr.life/sse` | Exposes MCP to Groq (no localhost) | Free SSH tunnel |

**Indirect (via Lesson 7 RAG bridge):**
- OpenRouter embeddings: `openai/text-embedding-3-large`
- OpenRouter rerank: `cohere/rerank-v3.5`
- ChromaDB at `localhost:8000`

**Not present:** flight APIs, Google Calendar, OpenWeather, etc. The coffee demo in `tools.mjs` uses a **mock local function** (`checkIngredients`), not an external API.

---

## 2. Agent Structure

**Framework:** Direct **OpenAI Node SDK** (`openai` v6.42) — **no** LangChain, CrewAI, AutoGen, or similar.

**API surface:** OpenAI **Responses API** (`client.responses.create`), not Chat Completions.

**Three practice levels:**

| File | Practice | Pattern |
|------|----------|---------|
| `agent.mjs` | 1 | Structured JSON output (`text.format.type: "json_schema"`) |
| `tools.mjs` | 2 | Function calling loop (barista + mock `check_ingredients`) |
| `full_agent.mjs` | 3 | Multi-tool agent: RAG + MCP + skill, up to 10 steps |

**Providers** (`full_agent.mjs`): OpenRouter (default) or Groq via `LLM_PROVIDER` env var.

**Tool types in practice 3:**

| Mode | Tool type | Tools |
|------|-----------|-------|
| `rag` | `function_call` | `search_knowledge_base` |
| `mcp` | `mcp_call` (if `MCP_PUBLIC_URL` set) or function fallback | `get_index_status`, `list_project_documents` |
| `skill` | `function_call` | `read_tz_skill` |
| `all` | All function tools combined | All of the above |

---

## 3. Key Files & Implementation Patterns

| File | Role |
|------|------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Minimal structured-output demo |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Two-step function-calling loop |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | Main agent: tool building, loop, Python bridges |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py` | CLI bridge → Lesson 7 RAG (`retrieve_chunks`, `rerank_chunks`) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py` | ChromaDB status, file listing, skill reader |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | FastMCP server (SSE on port 8765) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md` | Cursor-style skill checklist for TZ analysis |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example` | API keys & MCP tunnel config |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md` | Quick reference |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md` | Full setup (ChromaDB, MCP, tunnel) |

**Core agent loop** (`full_agent.mjs`):
1. Load `.env` → create `OpenAI` client
2. `responses.create({ model, instructions, tools, input })`
3. Parse `response.output` for `function_call` / `mcp_call`
4. Execute tools (Python via `execFile`, or native MCP when tunneled)
5. Append `function_call_output` → repeat (max 10 steps)
6. Duplicate tool calls blocked via `calledTools` Set

**Cross-project dependency:** Python uses Lesson 7 venv at  
`C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.venv\Scripts\python.exe`

---

## 4. Dependencies

**Node (`package.json`):**
```json
"dependencies": { "openai": "^6.42.0" }
```
No `requirements.txt` in Lesson 8.

**Python (via Lesson 7 venv — `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt`):**
- `httpx`, `python-dotenv`, `openai`, `chromadb`, `chonkie`, `python-docx`, `ragas`, `datasets`, `langchain-openai`
- MCP/FastMCP installed in venv (used by `tz_project_mcp.py`, not listed in Lesson 8)

---

## 5. A2A / Agent Card Patterns

**None found.** No references to:
- A2A (Agent-to-Agent protocol)
- Agent cards / `.well-known/agent.json`
- Google A2A SDK

**Closest related pattern:** **MCP (Model Context Protocol)** — native `type: "mcp"` tool in Responses API pointing at the local FastMCP server. This is MCP client/server, not A2A.

**Skill pattern:** Cursor-style `SKILL.md` with YAML frontmatter (`name`, `description`) — used as agent knowledge, not as an A2A agent card.

---

## Quick Architecture

```
User → full_agent.mjs (OpenAI Responses API)
         ├─ function_call → rag_search.py → Lesson 7 RAG → ChromaDB :8000
         ├─ function_call → project_tools.py → ChromaDB / SKILL.md
         ├─ mcp_call → tz_project_mcp.py :8765/sse (via localhost.run tunnel)
         └─ LLM → OpenRouter or Groq
```

If you need flight/calendar-style patterns for Lesson 9 A2A, they likely live in a different lesson or repo — this one is focused on TZ analysis with RAG + MCP + skills.

---
