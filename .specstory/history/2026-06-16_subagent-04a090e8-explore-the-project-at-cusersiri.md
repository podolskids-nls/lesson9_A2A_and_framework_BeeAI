# Subagent — Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_age

_Дата: 2026-06-16 | Chat ID: `04a090e8-f3ed-4990-8afe-bd98f16017b2` | Workspace: Lesson_9_Agent2Agent (A2A)_

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

Exploring the Lesson_8 project structure and searching for APIs, agent patterns, and dependencies.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

- **Tool `UpdateCurrentStep`**

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Glob`**

---

### Ассистент

Checking Lesson 7 dependencies the agent bridges to for RAG and embeddings.

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

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.env.example

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

## Lesson 8 — Project Summary

**Path:** `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent`

This is a **technical-spec (ТЗ) analysis agent** built in three progressive practices. It does **not** use flight, calendar, weather, or similar domain APIs.

---

### 1. APIs & endpoints used

| Service | Endpoint | Purpose | Free tier? |
|---------|----------|---------|------------|
| **OpenRouter** | `https://openrouter.ai/api/v1` | LLM (`openrouter/free`), embeddings, rerank (via Lesson 7 RAG) | Yes (free model + key) |
| **Groq** | `https://api.groq.com/openai/v1` | Alternative LLM provider (`llama-3.3-70b-versatile`, etc.) | Yes (with API key) |
| **ChromaDB** | `http://localhost:8000` | Vector index for ТЗ documents | Local (Docker) |
| **Local MCP (SSE)** | `http://127.0.0.1:8765/sse` | Project tools over MCP | Local |
| **localhost.run tunnel** | `https://xxxxx.lhr.life/sse` | Public MCP URL for Groq (no localhost) | Free SSH tunnel |

**Config:** `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example`

**No flight/calendar APIs** — the only “calendar” mention is in the skill checklist text (`skills\tz-helper\SKILL.md`), not an API integration.

---

### 2. Agent structure (frameworks)

- **Framework:** Node.js **`openai` npm SDK v6.42.0** only — no LangChain, no OpenAI Agents SDK, no A2A framework.
- **API surface:** OpenAI **Responses API** — `client.responses.create({ model, instructions, tools, input })`.
- **Providers:** OpenRouter (default) or Groq, switched via `LLM_PROVIDER` in `.env`.
- **Three practice levels:**

| Practice | File | Pattern |
|----------|------|---------|
| 1 | `agent.mjs` | Structured JSON output (`text.format.type: "json_schema"`) |
| 2 | `tools.mjs` | Function calling — 2-step loop (call → `function_call_output` → final answer) |
| 3 | `full_agent.mjs` | Multi-step agent (up to 10 iterations) with RAG + MCP + skill tools |

- **Tool types in practice 3:**
  - `function` — RAG search, ChromaDB status, skill reader
  - `mcp` — native MCP when `MCP_PUBLIC_URL` is set
  - Python subprocess bridge via `execFile` to `rag_search.py` / `project_tools.py`

---

### 3. Key files & implementation patterns

| File | Role |
|------|------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Practice 1: JSON schema structured output |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Practice 2: coffee-shop function-calling demo |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | Practice 3: main agent — modes `rag` / `mcp` / `skill` / `all` |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py` | CLI bridge → Lesson 7 RAG (`retrieve_chunks`, rerank) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py` | ChromaDB status, file listing, skill file reader |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | FastMCP server (SSE on port 8765) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md` | Cursor-style skill checklist for ТЗ analysis |

**Core agent loop pattern** (`full_agent.mjs`):
1. Build tools by mode (`buildTools(mode)`)
2. Call `responses.create` with `input` history
3. Append `response.output` to `input`
4. Execute `function_call` items → push `function_call_output`
5. Block duplicate tool calls via `calledTools` Set
6. Exit when no more function calls → print `response.output_text`

**External dependency:** RAG/ChromaDB lives in sibling project  
`C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG`

---

### 4. Dependencies

**Node (`package.json`):**
```json
"dependencies": { "openai": "^6.42.0" }
```
No `requirements.txt` in Lesson 8 itself.

**Python (via Lesson 7 venv, used by bridges + MCP):**  
`C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt`
- `httpx`, `python-dotenv`, `openai`, `chromadb`, `chonkie`, `python-docx`, `ragas`, `datasets`, `langchain-openai`

**MCP server additionally uses:** `mcp.server.fastmcp` (Python `mcp` package — not listed in Lesson 8’s own deps).

---

### 5. A2A / agent card patterns

**None found.** Grep found no matches for `A2A`, `AgentCard`, `agent card`, or `.well-known`.

What *is* present instead:
- **MCP server card pattern** — `FastMCP("tz-project")` with `@mcp.tool()` decorators
- **Native MCP tool registration** in Responses API:
  ```js
  { type: "mcp", server_label: "tz-project", server_url: MCP_URL, require_approval: "never" }
  ```
- **Cursor skill pattern** — YAML frontmatter in `skills/tz-helper/SKILL.md` (`name`, `description`)

This project is a **single-agent + tools** setup, not multi-agent A2A communication.

---

### Quick run reference

```bash
node full_agent.mjs rag      # RAG function tool
node full_agent.mjs mcp      # native MCP (needs MCP_PUBLIC_URL) or function fallback
node full_agent.mjs skill    # read_tz_skill
node full_agent.mjs all "..."  # all function tools combined
```

Docs: `README.md`, `SETUP.md` (both at project root).

---
