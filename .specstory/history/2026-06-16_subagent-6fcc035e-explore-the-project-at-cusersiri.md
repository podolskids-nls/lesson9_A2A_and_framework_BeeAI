# Subagent — Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_age

_Дата: 2026-06-16 | Chat ID: `6fcc035e-bff0-4014-b08f-220d83f06d77` | Workspace: Lesson_9_Agent2Agent (A2A)_

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

Exploring the Lesson_8 project structure and key patterns across the codebase.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

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

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Glob`**

---

### Ассистент

Checking Lesson 7 RAG dependencies referenced by this project.

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.gitignore

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py

- **Tool `UpdateCurrentStep`**

---

### Ассистент

# Lesson 8 — Project Summary

`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent` is a **lesson project** with three progressive agent examples (practices 1–3). It analyzes a **technical specification (ТЗ)** using RAG from Lesson 7, local MCP tools, and a Cursor-style skill file.

---

## 1. Tech Stack

| Layer | Technology |
|-------|------------|
| **Runtime (agents)** | Node.js (ES modules: `.mjs`) |
| **LLM client** | `openai` npm package v6.42 — used as OpenAI-compatible client |
| **LLM providers** | OpenRouter, Groq |
| **Bridge / tools** | Python 3 (via `child_process.execFile`) |
| **Vector DB** | ChromaDB (Docker, `localhost:8000`) — from Lesson 7 |
| **MCP server** | Python `FastMCP` (SSE on port 8765) |
| **RAG pipeline** | Lesson 7 (`C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG`) — Chonkie, chromadb, python-docx |
| **Config** | `.env` + `process.loadEnvFile(".env")` |

**No frontend, no TypeScript, no React.** Single npm dependency: `openai`.

---

## 2. Free / External APIs Used

**No flight, calendar, weather, or Google APIs** in this project. External services:

| Service | Purpose | Config |
|---------|---------|--------|
| **OpenRouter** | Free LLM (`openrouter/free`), embeddings/rerank via Lesson 7 | `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL` |
| **Groq** | Alternative LLM provider | `GROQ_API_KEY`, `GROQ_MODEL` |
| **ChromaDB** | Local vector store (Docker) | `localhost:8000` |
| **localhost.run** | Free SSH tunnel so Groq can reach local MCP | `ssh -R 80:localhost:8765 nokey@localhost.run` → `MCP_PUBLIC_URL` |

Practice 2 (`tools.mjs`) uses a **mock** `checkIngredients()` — no real inventory API.

---

## 3. Agent Structure

Three practices, increasing complexity:

```mermaid
flowchart LR
  subgraph P1["Practice 1: agent.mjs"]
    A1[Single Responses API call] --> A2[JSON schema output]
  end
  subgraph P2["Practice 2: tools.mjs"]
    B1[User query] --> B2[function_call]
    B2 --> B3[Local handler]
    B3 --> B4[Second Responses call]
  end
  subgraph P3["Practice 3: full_agent.mjs"]
    C1[User query + mode] --> C2[Multi-step loop max 10]
    C2 --> C3{Tool type}
    C3 -->|function_call| C4[Python bridge]
    C3 -->|mcp_call| C5[Native MCP server]
    C4 --> C2
    C5 --> C2
  end
```

### Practice 1 — Structured output
`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs`  
Single call, JSON schema via `text.format`, no tools.

### Practice 2 — Function calling
`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs`  
Two-turn loop: model calls `check_ingredients` → local handler → final answer.

### Practice 3 — Full agent
`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs`  
Multi-step agent with modes:

| Mode | Tools | Mechanism |
|------|-------|-----------|
| `rag` | `search_knowledge_base` | Python → Lesson 7 RAG |
| `mcp` | `get_index_status`, `list_project_documents` | Native MCP if `MCP_PUBLIC_URL` set, else Python fallback |
| `skill` | `read_tz_skill` | Reads `SKILL.md` via Python |
| `all` | All function tools combined | Default |

**Agent loop pattern** (lines 198–229 in `full_agent.mjs`):
1. `client.responses.create({ model, instructions, tools, input })`
2. Append `response.output` to `input`
3. Execute `function_call` items via Python
4. Push `function_call_output` back
5. Repeat until no more function calls (max 10 steps)
6. Duplicate tool calls are blocked via a `calledTools` Set

---

## 4. OpenAI SDK Usage Patterns

Uses the **Responses API** (`client.responses.create`), not Chat Completions.

### Client setup (OpenRouter / Groq as OpenAI-compatible)

```11:14:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs
const client = new OpenAI({
  baseURL: process.env.OPENROUTER_BASE_URL ?? "https://openrouter.ai/api/v1",
  apiKey,
});
```

### Structured JSON output (Practice 1)

```17:43:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs
  const response = await client.responses.create({
    model: "openrouter/free", 
    instructions: "Ты исторический агент. Отвечай строго в формате JSON.", 
    input: "Кто был последним императором России?", 
    text: {
      format: {
        type: "json_schema",
        name: "emperor_info",
        strict: true,
        schema: { /* ... */ }
      }
    }
  });
  console.log(response.output_text);
```

### Function calling (Practice 2 & 3)

```46:52:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs
  const response1 = await client.responses.create({
    model: "openrouter/free",
    instructions: "...",
    tools: coffeeTools,
    input,
  });
```

Tool result fed back:

```76:80:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs
  input.push({
    type: "function_call_output",
    call_id: toolCall.call_id,
    output: resultText,
  });
```

### Native MCP tool (Practice 3, when tunneled)

```95:101:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs
  const nativeMcp = {
    type: "mcp",
    server_label: "tz-project",
    server_description: "MCP проекта ТЗ (нужен публичный URL через ngrok).",
    server_url: MCP_URL,
    require_approval: "never",
  };
```

### Key SDK conventions across files
- `instructions` instead of system messages
- `input` as string or message array (multi-turn)
- `response.output` — typed items: `function_call`, `mcp_call`, `reasoning`, `message`
- `response.output_text` — final text
- `strict: true` on function tool schemas in `full_agent.mjs`

---

## 5. Key Files and Purposes

| File | Purpose |
|------|---------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Practice 1: JSON schema structured output |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Practice 2: function calling demo (barista/coffee) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | Practice 3: main agent — RAG + MCP + skill, provider switching, agent loop |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py` | CLI bridge: semantic search via Lesson 7 `retrieve_chunks` / `rerank_chunks` |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py` | CLI: ChromaDB status, list `input/` docs, read skill file |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | Local MCP server (SSE :8765): `get_index_status`, `list_project_documents`, `filter_chunks_by_keyword` |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md` | Checklist/rules for analyzing technical specs |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example` | API keys, provider, MCP tunnel URL |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md` | Quick reference and run commands |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md` | Full setup: Docker, MCP, tunnel, env |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json` | Node project metadata, `openai` dependency |

**External dependency:** `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG` — RAG index, ChromaDB, embeddings (OpenRouter), Python venv used by `full_agent.mjs`.

---

## Run Commands

```bash
node full_agent.mjs rag
node full_agent.mjs mcp
node full_agent.mjs skill
node full_agent.mjs all "Опиши структуру сайта и проверь по чеклисту"
```

---

**Bottom line:** This is a **Node.js agent + Python tool bridge** lesson focused on OpenAI SDK **Responses API** patterns (structured output, function calling, native MCP). Free APIs are **OpenRouter** and **Groq** for LLM inference; storage is **local ChromaDB**. There are no flight, calendar, or similar third-party integrations.

---
