# Subagent — Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_age

_Дата: 2026-06-16 | Chat ID: `7edd91c8-1c2c-430d-8dc0-58a58c3cae74` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent thoroughly. I need to understand:
1. What tech stack is used (Python, Node, etc.)
2. What free APIs are used (flight, calendar, etc.)
3. How agents are structured
4. Any OpenAI SDK usage patterns
5. Key files and their purposes

Return a concise summary with file paths and relevant code patterns.

### Ассистент

I'll explore the Lesson_8 project structure and scan for tech stack, APIs, and agent patterns.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Glob`**

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

Checking Lesson 7 dependencies the agent bridges to for RAG and embeddings.

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\.env.example

- **Tool `Glob`**

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

# Lesson 8 Project Summary

`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent` is a **hybrid Node.js + Python** lesson project. It builds agents for analyzing a **technical specification (ТЗ)** using RAG, MCP, and Cursor-style skills. There are **no flight, calendar, or similar domain APIs** — only LLM providers and local infrastructure.

---

## 1. Tech Stack

| Layer | Technology |
|-------|------------|
| **Agent runtime** | Node.js (ES modules: `.mjs`) |
| **LLM client** | `openai` npm package `^6.42.0` (OpenAI-compatible API) |
| **Tool backends** | Python 3 (uses Lesson 7 venv at `Lesson_7_client_for_LLM_RAG\.venv`) |
| **Vector DB** | ChromaDB via Docker (`localhost:8000`) — from Lesson 7 |
| **MCP server** | Python `FastMCP` (SSE on port `8765`) |
| **Config** | `.env` via `process.loadEnvFile(".env")` |

**Dependency file:** `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json` — only `openai` as a Node dependency. Python deps live in Lesson 7 (`chromadb`, `mcp`, `python-dotenv`, etc.).

---

## 2. Free / External APIs Used

**No flight, calendar, weather, or similar APIs.** External services:

| Service | Purpose | Config |
|---------|---------|--------|
| **[OpenRouter](https://openrouter.ai/api/v1)** | Free LLM (`openrouter/free`), practices 1–2 default | `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL` |
| **[Groq](https://api.groq.com/openai/v1)** | Free LLM for practice 3 (`llama-3.3-70b-versatile` etc.) | `GROQ_API_KEY`, `GROQ_MODEL`, `LLM_PROVIDER=groq` |
| **[localhost.run](https://localhost.run)** | Free SSH tunnel so Groq can reach local MCP (Groq rejects `localhost`) | `ssh -R 80:localhost:8765 nokey@localhost.run` → `MCP_PUBLIC_URL` |
| **ChromaDB (local)** | Vector index for ТЗ documents | Docker from Lesson 7, `localhost:8000` |

**Via Lesson 7 RAG bridge** (`rag_search.py` → `Lesson_7_client_for_LLM_RAG\rag.py`):
- OpenRouter embeddings: `openai/text-embedding-3-large`
- OpenRouter rerank: `cohere/rerank-v3.5`
- Query rewrite through OpenRouter

**Local-only tools:** ChromaDB status, file listing in `input/`, reading `SKILL.md` — no external HTTP calls.

---

## 3. Agent Structure (3 Progressive Practices)

```mermaid
flowchart LR
  subgraph P1["Practice 1: agent.mjs"]
    A1[User input] --> A2[responses.create]
    A2 --> A3[JSON schema output]
  end

  subgraph P2["Practice 2: tools.mjs"]
    B1[User input] --> B2[responses.create + tools]
    B2 --> B3[function_call]
    B3 --> B4[Local checkIngredients]
    B4 --> B5[Second responses.create]
  end

  subgraph P3["Practice 3: full_agent.mjs"]
    C1[CLI mode: rag|mcp|skill|all] --> C2[Loop up to 10 steps]
    C2 --> C3{Tool type?}
    C3 -->|function_call| C4[exec Python bridge]
    C3 -->|mcp_call| C5[Native MCP server]
    C4 --> C2
    C5 --> C2
  end
```

| File | Practice | Pattern |
|------|----------|---------|
| `agent.mjs` | 1 | Single-shot **structured output** (JSON schema) |
| `tools.mjs` | 2 | **Function calling** — 2-step loop (coffee/barista demo) |
| `full_agent.mjs` | 3 | **Multi-step agent loop** — RAG + MCP + skill modes |

**Practice 3 modes** (`node full_agent.mjs <mode> "<query>"`):

| Mode | Tool mechanism | Tools |
|------|----------------|-------|
| `rag` | `function_call` | `search_knowledge_base` → `rag_search.py` |
| `mcp` | `mcp_call` (if `MCP_PUBLIC_URL`) or function fallback | `get_index_status`, `list_project_documents` |
| `skill` | `function_call` | `read_tz_skill` → reads `SKILL.md` |
| `all` | All function tools combined | All of the above |

**Agent loop pattern** in `full_agent.mjs`:
1. Build `input` with user message
2. Call `client.responses.create({ model, instructions, tools, input })`
3. Append `response.output` to `input`
4. Execute `function_call` items via Python subprocess
5. Push `{ type: "function_call_output", call_id, output }` back
6. Repeat until no more function calls (max 10 steps)
7. Duplicate tool calls are blocked via a `calledTools` Set

---

## 4. OpenAI SDK Usage Patterns

All agents use the **Responses API** (`client.responses.create`), not Chat Completions.

**Provider setup** — custom `baseURL` + `apiKey`:

```javascript
const client = new OpenAI({
  baseURL: "https://api.groq.com/openai/v1",  // or OpenRouter
  apiKey: process.env.GROQ_API_KEY,
});
```

**Practice 1 — JSON schema structured output:**

```javascript
await client.responses.create({
  model: "openrouter/free",
  instructions: "...",
  input: "Кто был последним императором России?",
  text: {
    format: {
      type: "json_schema",
      name: "emperor_info",
      strict: true,
      schema: { /* ... */ },
    },
  },
});
console.log(response.output_text);
```

**Practice 2/3 — Function tools:**

```javascript
tools: [{
  type: "function",
  name: "search_knowledge_base",
  strict: true,
  parameters: { type: "object", properties: { query: { type: "string" } }, ... },
}]
```

**Practice 3 — Native MCP tool** (when `MCP_PUBLIC_URL` is set):

```javascript
{
  type: "mcp",
  server_label: "tz-project",
  server_url: MCP_URL,
  require_approval: "never",
}
```

**Tool result feedback:**

```javascript
input.push({
  type: "function_call_output",
  call_id: toolCall.call_id,
  output: result,
});
```

**Output inspection:** `response.output` items have types like `reasoning`, `function_call`, `mcp_call`, `mcp_list_tools`, `message`; final text in `response.output_text`.

---

## 5. Key Files and Purposes

| File | Purpose |
|------|---------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Practice 1: structured JSON output demo |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Practice 2: function calling demo (`check_ingredients`) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | Practice 3: main agent — provider switch, tool builder, agent loop |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py` | CLI bridge to Lesson 7 RAG (`retrieve_chunks` → `rerank_chunks` → `format_context`) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py` | CLI for MCP/skill logic: ChromaDB status, list docs, read skill |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | Local MCP server (SSE `:8765`) — same tools + `filter_chunks_by_keyword` |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md` | Cursor-style skill: TZ analysis checklist |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example` | API keys, provider, MCP tunnel URL |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md` | Quick reference (Russian) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md` | Full setup: Docker, MCP, tunnel, run commands |

**Cross-project dependency:** RAG data and indexing live in `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG` (`input/`, `run_rag.py index`, `rag.py`, ChromaDB Docker).

---

## Quick Takeaway

This is a **learning sandbox for OpenAI Responses API agents** — structured output → function calling → RAG/MCP/skills — centered on **analyzing a website project spec**, not integrating third-party SaaS APIs. The main architectural pattern is **Node orchestrates the LLM loop; Python handles RAG/MCP backends via subprocess calls**.

---
