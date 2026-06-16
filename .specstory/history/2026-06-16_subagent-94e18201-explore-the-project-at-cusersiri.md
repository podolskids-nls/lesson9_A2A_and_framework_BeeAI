# Subagent — Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_age

_Дата: 2026-06-16 | Chat ID: `94e18201-5e3f-40d5-8303-583a257db6c1` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Explore the project at C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent. Find how free APIs are used - especially for flights and calendar. List relevant files, API endpoints, dependencies (requirements.txt, package.json), agent structure, OpenAI SDK usage. Report specific code patterns and API URLs used.

### Ассистент

I'll explore the Lesson_8 project structure and search for flight, calendar, and API usage patterns.

- **Tool `UpdateCurrentStep`**

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

Searching more specifically for flight/calendar APIs and reading core project files.

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\SETUP.md

- **Tool `Glob`**

---

### Ассистент

Reading all source files and checking related lessons for flight/calendar references.

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

---

### Ассистент

Checking Lesson 7 (dependency) and the broader course for flight/calendar APIs.

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md

- **Tool `Glob`**

---

### Ассистент

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.specstory

---

### Ассистент

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG

---

### Ассистент

- **Tool `Glob`**

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py

---

### Ассистент

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_6

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_5

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\client.py

---

### Ассистент

- **Tool `Glob`**

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.specstory

---

### Ассистент

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.gitignore

---

### Ассистент

- **Tool `UpdateCurrentStep`**

---

### Ассистент

## Executive summary

**`C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent` does not implement flight or calendar APIs.** There are no HTTP calls to aviation or calendar services in project source. The only “calendar” mention is in the TZ checklist skill (`календарный план` = project timeline in a spec document), not a Google/Outlook Calendar integration.

The project is a **3-practice agent course** focused on **OpenAI Responses API** patterns, **RAG over Lesson 7’s ChromaDB index**, and a **local MCP server** for project document tools.

---

## Relevant files (absolute paths)

| File | Role |
|------|------|
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs` | Practice 1 — structured JSON output |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs` | Practice 2 — function calling (mock coffee barista) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs` | Practice 3 — full agent (RAG + MCP + skill) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\rag_search.py` | Python bridge to Lesson 7 RAG |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\project_tools.py` | ChromaDB status, file list, skill reader |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\mcp_server\tz_project_mcp.py` | Local MCP server (SSE on port 8765) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\skills\tz-helper\SKILL.md` | Agent skill / TZ analysis checklist |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\package.json` | Node deps |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example` | API keys & URLs |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md` / `SETUP.md` | Docs & run instructions |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\requirements.txt` | Python deps (used via Lesson 7 venv) |
| `C:\Users\Irina\IT\AI_DRIVEN\Lesson_7_client_for_LLM_RAG\rag.py` | RAG backend called by `rag_search.py` |

---

## Flights & calendar — not found

Searched all project `.mjs`, `.py`, `.md`, and `.env.example` files for `flight`, `calendar`, `amadeus`, `aviation`, etc. **No matches in application code.**

- **Flights:** not implemented anywhere.
- **Calendar:** only this text in the skill checklist — “Сроки и этапы — календарный план, приёмка” — meaning a project schedule section in a technical spec, not a calendar API.

If you expected flight/calendar integrations, they may belong to another lesson (e.g. Lesson 9 A2A) or were planned but not built in Lesson 8.

---

## APIs & URLs actually used

### 1. OpenRouter (free LLM tier)

- **URL:** `https://openrouter.ai/api/v1`
- **Model:** `openrouter/free` (Practice 1–2; default in Practice 3)
- **Auth:** `OPENROUTER_API_KEY`
- **Used in:** `agent.mjs`, `tools.mjs`, `full_agent.mjs`

### 2. Groq (free LLM tier)

- **URL:** `https://api.groq.com/openai/v1`
- **Model:** `GROQ_MODEL` (default `openai/gpt-oss-120b` or `llama-3.3-70b-versatile` per SETUP)
- **Auth:** `GROQ_API_KEY`
- **Used in:** `full_agent.mjs` when `LLM_PROVIDER=groq`

### 3. ChromaDB (local vector DB)

- **URL:** `http://localhost:8000` (via `chromadb.HttpClient`)
- **Collection:** `rag_documents`
- **Used in:** `project_tools.py`, `mcp_server/tz_project_mcp.py`
- **Data source:** Lesson 7 RAG index (`Lesson_7_client_for_LLM_RAG/input/`)

### 4. Local MCP server (SSE)

- **URL:** `http://127.0.0.1:8765/sse` (default)
- **Public tunnel (optional):** `https://xxxxx.lhr.life/sse` via `localhost.run` SSH tunnel
- **Env:** `MCP_PUBLIC_URL`
- **Used in:** `full_agent.mjs` (`mode === "mcp"` with native MCP when public URL is set)

### 5. Lesson 7 RAG (indirect, via Python subprocess)

- **Bridge:** `rag_search.py` → `Lesson_7_client_for_LLM_RAG/rag.py`
- **OpenRouter again** for embeddings (`openai/text-embedding-3-large`), rerank (`cohere/rerank-v3.5`), query rewrite
- **Not HTTP from Node** — spawned as: `Lesson_7/.venv/Scripts/python.exe rag_search.py "<query>"`

### 6. Mock “backend” (Practice 2 only)

- `check_ingredients()` in `tools.mjs` — **local in-memory function**, no external API (coffee barista demo).

---

## Dependencies

### `package.json` (Lesson 8)

```json
"dependencies": {
  "openai": "^6.42.0"
}
```

No `requirements.txt` in Lesson 8. Python runs through **Lesson 7’s venv** (`Lesson_7_client_for_LLM_RAG/.venv`).

### `requirements.txt` (Lesson 7, used by Lesson 8 Python scripts)

```
httpx>=0.27.0
python-dotenv>=1.0.0
openai>=1.40.0
chromadb>=0.5.0
chonkie>=1.0.0
python-docx>=1.1.0
ragas==0.2.14
datasets>=2.19.0
langchain-openai>=0.2.0
```

MCP server additionally uses `mcp` / `FastMCP` (installed in Lesson 7 venv, not listed in Lesson 8).

---

## Agent structure

```mermaid
flowchart TD
    subgraph practice1 [Practice 1 - agent.mjs]
        A1[User input] --> A2[responses.create]
        A2 --> A3[JSON schema output]
    end

    subgraph practice2 [Practice 2 - tools.mjs]
        B1[User input] --> B2[responses.create + tools]
        B2 --> B3{function_call?}
        B3 -->|yes| B4[check_ingredients local]
        B4 --> B5[Second responses.create]
        B3 -->|no| B6[Direct answer]
    end

    subgraph practice3 [Practice 3 - full_agent.mjs]
        C1[CLI mode: rag/mcp/skill/all] --> C2[Agent loop up to 10 steps]
        C2 --> C3[responses.create]
        C3 --> C4{function_call or mcp_call?}
        C4 -->|function| C5[Python: rag_search / project_tools]
        C4 -->|mcp| C6[Native MCP tz-project server]
        C5 --> C2
        C6 --> C2
        C4 -->|message only| C7[Final output_text]
    end
```

### Modes in `full_agent.mjs`

| Mode | Tools | Backend |
|------|-------|---------|
| `rag` | `search_knowledge_base` | `rag_search.py` → ChromaDB + OpenRouter embeddings |
| `mcp` | Native MCP or fallback functions | `tz_project_mcp.py` or `project_tools.py` |
| `skill` | `read_tz_skill` | Reads `skills/tz-helper/SKILL.md` |
| `all` | All function tools combined | Mixed |

### MCP tools (`tz_project_mcp.py`)

- `get_index_status` — ChromaDB chunk count
- `list_project_documents` — files in `Lesson_7/.../input/`
- `filter_chunks_by_keyword` — keyword scan over stored chunks

---

## OpenAI SDK usage patterns

All three `.mjs` agents use the **OpenAI Node SDK v6** pointed at OpenRouter/Groq via compatible base URLs.

### Client initialization

```javascript
import OpenAI from "openai";
process.loadEnvFile(".env");

const client = new OpenAI({
  baseURL: process.env.OPENROUTER_BASE_URL ?? "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});
```

### Responses API — structured output (`agent.mjs`)

```javascript
const response = await client.responses.create({
  model: "openrouter/free",
  instructions: "Ты исторический агент...",
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

### Function calling — two-step loop (`tools.mjs`)

```javascript
// Step 1: model decides to call tool
const response1 = await client.responses.create({
  model: "openrouter/free",
  instructions: "...",
  tools: coffeeTools,  // type: "function"
  input: [{ role: "user", content: userInput }],
});

// Find function_call in response1.output
const toolCall = response1.output.find(item => item.type === "function_call");

// Step 2: feed function_call_output back
input.push({
  type: "function_call_output",
  call_id: toolCall.call_id,
  output: resultText,
});

const response2 = await client.responses.create({ model, instructions, tools, input });
```

### Full agent loop (`full_agent.mjs`)

```javascript
const client = new OpenAI({ baseURL: provider.baseURL, apiKey: provider.apiKey });

for (let step = 1; step <= 10; step++) {
  const response = await client.responses.create({
    model: provider.model,
    instructions: getInstructions(mode),
    tools,  // function tools and/or native MCP
    input,
  });

  input = input.concat(response.output);

  const functionCalls = response.output.filter(item => item.type === "function_call");
  if (functionCalls.length === 0) break;  // final message

  for (const toolCall of functionCalls) {
    const result = await executeFunctionCall(toolCall);  // spawns Python
    input.push({ type: "function_call_output", call_id: toolCall.call_id, output: result });
  }
}
```

### Native MCP tool definition

```javascript
{
  type: "mcp",
  server_label: "tz-project",
  server_description: "MCP проекта ТЗ...",
  server_url: MCP_URL,  // http://127.0.0.1:8765/sse or tunneled URL
  require_approval: "never",
}
```

When `MCP_PUBLIC_URL` is set, Groq/OpenRouter receive `mcp_call` items in `response.output` (logged in `logOutputTypes`).

---

## “Free API” summary

| Service | Free tier? | Purpose in Lesson 8 |
|---------|------------|---------------------|
| OpenRouter `openrouter/free` | Yes | LLM for all practices |
| Groq | Yes (with API key) | Alternative LLM provider |
| ChromaDB (Docker local) | Self-hosted | Vector search over TZ docs |
| localhost.run | Free SSH tunnel | Expose MCP to cloud LLMs |
| Coffee ingredients | Mock local | Teaching function calling only |

---

If you want flight/calendar API patterns, say which lesson or repo to check next — they are not in Lesson 8’s codebase. I can also compare this structure to your current Lesson 9 A2A project if that helps.

---
