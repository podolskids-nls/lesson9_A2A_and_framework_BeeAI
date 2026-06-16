# Subagent — Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_age

_Дата: 2026-06-16 | Chat ID: `c742a15a-a600-4cca-8e80-7fb57a7d5385` | Workspace: Lesson_9_Agent2Agent (A2A)_

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

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

- **Tool `UpdateCurrentStep`**

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

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

Checking Lesson 7 integration and scanning for any remaining project files.

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.gitignore

---

### Ассистент

- **Tool `Glob`**

- **Tool `Glob`**

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\client.py

- **Tool `UpdateCurrentStep`**

---

### Ассистент

## Lesson 8 Project Summary

**`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent`** is a small hybrid **Node.js + Python** tutorial for building LLM agents around a **technical specification (ТЗ) analysis** use case. It builds on **Lesson 7** (`Lesson_7_client_for_LLM_RAG`) for RAG/ChromaDB.

---

### 1. Tech Stack

| Layer | Technology |
|-------|------------|
| **Agent runtime** | Node.js (`.mjs` ES modules), single npm dep: `openai@^6.42.0` |
| **Tool backends** | Python 3 scripts + Lesson 7 `.venv` |
| **Vector DB** | ChromaDB (Docker, port 8000) |
| **MCP server** | Python `FastMCP` (SSE on `:8765`) |
| **Tunnel** | `localhost.run` SSH tunnel (for Groq native MCP) |
| **Config** | `.env` via `process.loadEnvFile(".env")` |

No frontend, no TypeScript, no separate web framework.

---

### 2. Free APIs Used

**No flight, calendar, or weather APIs.** External services are LLM providers and infrastructure:

| Service | Purpose | Config |
|---------|---------|--------|
| **[OpenRouter](https://openrouter.ai)** | Free LLM (`openrouter/free`), embeddings/rerank via Lesson 7 | `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL` |
| **[Groq](https://groq.com)** | Free LLM alternative (`llama-3.3-70b-versatile`, etc.) | `GROQ_API_KEY`, `GROQ_MODEL` |
| **ChromaDB** | Local vector index (not cloud) | `localhost:8000` |
| **localhost.run** | Public HTTPS tunnel for MCP | `MCP_PUBLIC_URL` |

The coffee demo in `tools.mjs` uses a **mock local function** (`checkIngredients`), not a real API.

Lesson 7 RAG (used by `rag_search.py`) also calls OpenRouter for embeddings (`openai/text-embedding-3-large`) and reranking (`cohere/rerank-v3.5`).

---

### 3. Agent Structure (3 Progressive Practices)

```
Practice 1: agent.mjs       → Structured JSON output (single call)
Practice 2: tools.mjs       → Function calling (2-turn loop, coffee demo)
Practice 3: full_agent.mjs  → Full agent: RAG + MCP + Skill
```

**`full_agent.mjs` modes** (CLI: `node full_agent.mjs <mode> [query]`):

| Mode | Tool type | Tools |
|------|-----------|-------|
| `rag` | `function_call` | `search_knowledge_base` → Python RAG |
| `mcp` | `mcp_call` (if `MCP_PUBLIC_URL`) or `function_call` fallback | `get_index_status`, `list_project_documents` |
| `skill` | `function_call` | `read_tz_skill` → reads `SKILL.md` |
| `all` | All function tools combined | RAG + status + docs + skill |

**Agent loop pattern** (`full_agent.mjs`):

```186:229:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs
async function runAgent(userInput, providerName, mode) {
  // ...
  for (let step = 1; step <= 10; step++) {
    const response = await client.responses.create({ model, instructions, tools, input });
    input = input.concat(response.output);
    const functionCalls = response.output.filter((item) => item.type === "function_call");
    if (functionCalls.length === 0) { /* final answer */ return; }
    for (const toolCall of functionCalls) {
      // execute Python bridge, push function_call_output back
    }
  }
}
```

Node orchestrates the LLM; Python handles RAG/MCP/skill via `child_process.execFile`.

---

### 4. OpenAI SDK Usage Patterns

All agents use the **OpenAI JS SDK** as a **compatible client** for OpenRouter/Groq (custom `baseURL` + `apiKey`).

**Pattern A — Structured output** (`agent.mjs`):

```17:46:C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs
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

**Pattern B — Function calling (2-turn)** (`tools.mjs`):
- Define `tools: [{ type: "function", name, description, parameters }]`
- Append `response1.output` to `input`
- Find `function_call`, run handler, push `{ type: "function_call_output", call_id, output }`
- Second `responses.create()` for final answer

**Pattern C — Multi-provider + native MCP** (`full_agent.mjs`):
- `PROVIDERS` map for OpenRouter vs Groq
- Tool types: `function`, `mcp` (native MCP server URL), and unused `shell` skill config
- Loop up to 10 steps with duplicate-call guard (`calledTools` Set)
- Reads `response.output_text` and logs `function_call` / `mcp_call` types

**Key API surface used:** `client.responses.create()` (Responses API, not Chat Completions), fields `instructions`, `input`, `tools`, `text.format`, `output_text`, `response.output`.

---

### 5. Key Files

| File | Purpose |
|------|---------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Practice 1: JSON schema structured output |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Practice 2: function calling demo (barista/coffee) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | Practice 3: main agent orchestrator (RAG/MCP/skill) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py` | CLI bridge → Lesson 7 `retrieve_chunks` / `rerank_chunks` |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py` | ChromaDB status, list `input/` docs, read skill file |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | Local MCP server (SSE `:8765`) exposing same project ops |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md` | Agent skill: TZ analysis checklist/rules |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example` | API keys, provider, MCP tunnel URL |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md` | Quick reference |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md` | Full setup (Docker, MCP, tunnel, run commands) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json` | Node deps (`openai` only) |

**External dependency (Lesson 7):**
- `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py` — RAG pipeline (ChromaDB, embeddings, rerank)
- `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\input\` — indexed TZ documents

---

### Architecture (concise)

```
User query
    ↓
full_agent.mjs (OpenAI SDK → Groq/OpenRouter)
    ↓ responses.create + tools
    ├─ function_call → rag_search.py → Lesson 7 RAG → ChromaDB
    ├─ function_call → project_tools.py → ChromaDB / SKILL.md
    └─ mcp_call → tz_project_mcp.py (via public tunnel) → ChromaDB / input/
    ↓
Final answer (response.output_text)
```

**Bottom line:** This is an educational agent stack focused on **TZ document analysis**, using **free LLM tiers** (OpenRouter/Groq), **local RAG** (ChromaDB from Lesson 7), **MCP protocol**, and a **Cursor-style skill file** — not domain APIs like flights or calendars.

---
