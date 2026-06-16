# A2A — три агента (оркестратор, рейсы, календарь)

_Дата: 2026-06-16 | Chat ID: `39235d22-fb08-40ba-ab49-fac8d8e518f9` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Надо сделать 3 агентов
Оркестратору пишешь задачу, он вызывает агента, вызывает агента, который пишет в календадь
Первый агент получает рейс
Без авторизации
Надо сделать A2A (agent to agent)
Используй бесплатные API, как в проекте C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent
Вопросы?

### Ассистент

Изучаю текущий проект и референс Lesson_8, чтобы спланировать A2A-систему с тремя агентами.

- **Tool `Glob`**

- **Tool `Glob`**

- **Tool `Task`**: Explore Lesson_8 APIs

- **Tool `Task`**: Explore Lesson_9 workspace

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\a2a_system.py

- **Tool `Grep`**: c:\Users\Irina\IT\AI_DRIVEN

- **Tool `Glob`**

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\requirements.txt

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\.env.example

- **Tool `Grep`**: c:\Users\Irina\IT\AI_DRIVEN

- **Tool `Read`**: C:\Users\Irina\.cursor\skills-cursor\plugins\cache\cursor-public\context7-plugin\58a36cea87ea887e7bb4850409f1f9ea58dae5e5\skills\context7-mcp\SKILL.md

---

### Ассистент

- **Tool `Glob`**

- **Tool `WebSearch`**

---

### Ассистент

- **Tool `WebFetch`**

- **Tool `Grep`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\agent-transcripts

---

### Ассистент

- **Tool `WebFetch`**

- **Tool `WebFetch`**

---

### Ассистент

- **Tool `WebFetch`**

---

### Ассистент

- **Tool `WebFetch`**

- **Tool `WebFetch`**

---

### Ассистент

В проекте уже есть прототип `a2a_system.py` (in-process function calling). По слайдам нужен реальный A2A wire protocol — планирую переход на `a2a-sdk` с отдельными HTTP-серверами.

- **Tool `AskQuestion`**

---

### Ассистент

- **Tool `CreatePlan`**

---

## 2. Пользователь

"OpenRouter/OpenAI SDK" - OpenAI платный его не использовать. К OpenRouter можешь добавить Groq
OPENROUTER_API_KEY=sk
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=openrouter/free

GROQ_API_KEY=gsk
GROQ_MODEL=llama-3.3-70b-versatile 
Эти данные в env файл размести и запрети себе их читать

### Ассистент

Обновляю план: только OpenRouter и Groq (без платного OpenAI API), конфиг в `.env`, без чтения секретов.

- **Tool `Read`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

- **Tool `Grep`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

---

### Ассистент

- **Tool `StrReplace`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

- **Tool `StrReplace`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

- **Tool `StrReplace`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

- **Tool `StrReplace`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

- **Tool `StrReplace`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

- **Tool `StrReplace`**: c:\Users\Irina\.cursor\plans\a2a_three_agents_2a532a50.plan.md

---

### Ассистент

План обновлён. Ключевые изменения:

**LLM — только бесплатные провайдеры**
- Платный OpenAI API (`api.openai.com`) **не используется**
- OpenAI Python SDK — только как клиент для **OpenRouter** (`openrouter/free`) и **Groq** (`llama-3.3-70b-versatile`)
- Переключение через `LLM_PROVIDER=openrouter|groq` (как в Lesson 8)

**Секреты**
- Реальные ключи — только в локальный `.env` проекта Lesson 9
- `.env.example` — плейсхолдеры без ключей
- `.env` в `.gitignore`
- **Я не буду читать `.env`** (Read/Grep) — ключи подхватываются только в runtime через `python-dotenv` в `shared/config.py`
- Правило в `.cursor/rules/`: не читать `.env`, не логировать ключи
- Fallback на `Lesson_8/.env` убран

При реализации создам `.env` с вашими значениями; ключи не буду читать и не буду выводить в лог.

Если всё ок — напишите «выполни план» / «go ahead», и начну реализацию.

---

## 3. Пользователь

A2A - это от Google будет использоваться? Это библиотека или что?!

### Ассистент

## A2A — что это

**A2A (Agent-to-Agent)** — открытый протокол для общения между AI-агентами. Инициатор — **Google** (вместе с партнёрами), спецификация: [a2a-protocol.org](https://a2a-protocol.org).

Это **не** ChatGPT/OpenAI API и **не** платный сервис. Это **стандарт обмена сообщениями** между агентами по сети.

## Библиотека или что?

Два уровня:

| Уровень | Что это |
|--------|---------|
| **Протокол** | Как агенты находят друг друга и обмениваются сообщениями (Agent Card, `sendMessage`, Task, Artifact) |
| **Библиотека** | **`a2a-sdk`** (Python) — официальная реализация от [a2aproject/a2a-python](https://github.com/a2aproject/a2a-python) |

В плане мы используем **`a2a-sdk`**:

```bash
pip install "a2a-sdk[http-server]"
```

Она даёт:
- **Сервер** — Starlette/uvicorn, Agent Card на `/.well-known/agent.json`, endpoint `sendMessage` (JSON-RPC)
- **Клиент** — discovery карточки агента и отправка сообщений

## Как это выглядит в нашем проекте

```mermaid
flowchart LR
    subgraph orchestrator [Orchestrator CLI]
        LLM["OpenRouter / Groq"]
        A2AClient["a2a-sdk client"]
    end
    subgraph flight [Flight Agent :8001]
        Card1["Agent Card"]
        Server1["a2a-sdk server"]
    end
    subgraph calendar [Calendar Agent :8002]
        Card2["Agent Card"]
        Server2["a2a-sdk server"]
    end
    LLM --> A2AClient
    A2AClient -->|"GET agent card"| Card1
    A2AClient -->|"sendMessage"| Server1
    A2AClient -->|"sendMessage"| Server2
```

- **Flight Agent** и **Calendar Agent** — отдельные HTTP-серверы на `a2a-sdk`
- **Оркестратор** — `a2a-sdk` client + LLM (OpenRouter/Groq) для планирования

## Отличие от текущего `a2a_system.py`

Сейчас в файле агенты вызываются **внутри одного Python-процесса** (function calling). Это идея A2A, но **не протокол**.

По слайдам урока и по плану — **реальный A2A**: агенты как отдельные сервисы, общение по HTTP.

## Связь с другими технологиями

| Технология | Связь с A2A |
|-----------|-------------|
| **OpenAI SDK** | Только клиент для LLM (OpenRouter/Groq) в оркестраторе |
| **MCP** (Lesson 8) | Другой протокол: агент ↔ инструменты |
| **A2A** | Агент ↔ агент |

Если нужно — могу добавить в план короткий блок «Что такое A2A» в README, или перейти к реализации.

---

## 4. Пользователь

Делай (просьба код не раздувать, чтобы не был слишком большим - вроде простая задача)

### Ассистент

Реализую компактную версию: три отдельные файлы серверов + общие модули, без раздувания структуры.

- **Tool `TodoWrite`**

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\a2a_system.py

- **Tool `Shell`**: Install a2a-sdk and verify imports

---

### Ассистент

- **Tool `Await`**

- **Tool `Shell`**: Verify a2a-sdk after install

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\terminals\722140.txt

---

### Ассистент

- **Tool `Shell`**: Install dependencies with longer timeout

---

### Ассистент

- **Tool `Shell`**: Test all a2a-sdk imports needed

---

### Ассистент

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\config.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\flight_api.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\calendar_api.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\a2a_app.py

---

### Ассистент

- **Tool `SwitchMode`**

---

### Ассистент

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\config.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\flight_api.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\calendar_api.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\a2a_app.py

---

### Ассистент

- **Tool `Shell`**: Inspect a2a helpers for response parsing

---

### Ассистент

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\flight_server.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\calendar_server.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\start_agents.py

---

### Ассистент

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\flight_server.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\calendar_server.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\start_agents.py

---

### Ассистент

- **Tool `Shell`**: Write flight and calendar server files via Python

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\flight_server.py

- **Tool `Shell`**: Write orchestrator and start_agents files

---

### Ассистент

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\__init__.py

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\requirements.txt

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\.env.example

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\.gitignore

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\.cursor\rules\no-read-env.mdc

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\README.md

---

### Ассистент

- **Tool `Shell`**: Write requirements, gitignore, env example, cursor rule

- **Tool `Shell`**: Start flight server in background

---

### Ассистент

- **Tool `Shell`**: Start calendar server in background

- **Tool `Await`**

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\terminals\937636.txt

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\terminals\367236.txt

---

### Ассистент

- **Tool `StrReplace`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\shared\a2a_app.py

---

### Ассистент

- **Tool `Shell`**: Fix unicode arrow in a2a_app.py

---

### Ассистент

- **Tool `Shell`**: Start flight server

- **Tool `Shell`**: Start calendar server

---

### Ассистент

- **Tool `Await`**

- **Tool `Shell`**: Test A2A flight agent sendMessage

---

### Ассистент

- **Tool `Shell`**: Inspect A2A response chunk structure

---

### Ассистент

- **Tool `Shell`**: List all fields in A2A stream chunks

---

### Ассистент

- **Tool `Shell`**: Find artifact in stream chunks

---

### Ассистент

- **Tool `Shell`**: Read artifacts from task in response

---

### Ассистент

- **Tool `Shell`**: Fix artifact extraction and flight_api unicode

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

---

### Ассистент

- **Tool `Shell`**: Patch orchestrator chunk text extraction

---

### Ассистент

- **Tool `Shell`**: Run full orchestrator end-to-end test

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

---

### Ассистент

- **Tool `Shell`**: Fix broken newline in orchestrator.py

---

### Ассистент

- **Tool `Shell`**: Verify orchestrator.py syntax

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

---

### Ассистент

- **Tool `Shell`**: Run full orchestrator with LLM

---

### Ассистент

- **Tool `Shell`**: Test calendar A2A agent

- **Tool `Shell`**: Mark legacy a2a_system.py as deprecated

---

### Ассистент

- **Tool `TodoWrite`**

- **Tool `Glob`**

---

### Ассистент

Готово — компактная A2A-система на **Google `a2a-sdk`**.

## Структура (~10 файлов)

| Файл | Роль |
|------|------|
| `flight_server.py` | A2A-сервер рейсов (порт 8001) |
| `calendar_server.py` | A2A-сервер календаря (порт 8002) |
| `orchestrator.py` | CLI: discovery + `sendMessage` + LLM |
| `start_agents.py` | Запуск двух серверов |
| `shared/` | `config`, `flight_api`, `calendar_api`, `a2a_app` |

## Что проверено

- Agent Card discovery работает
- `sendMessage` на Flight и Calendar — OK
- Оркестратор регистрирует агенты, LLM падает с **401** — в `.env` стоят плейсхолдеры, нужны реальные ключи

## Запуск

```bash
pip install -r requirements.txt

# 1. Вписать ключи в .env (не коммитить)
# 2. Терминал 1
python start_agents.py

# 3. Терминал 2
python orchestrator.py
```

**`.env`** — скопирован из `.env.example`. Впишите полные `OPENROUTER_API_KEY` и `GROQ_API_KEY`. Переключение: `LLM_PROVIDER=openrouter` или `groq`.

Платный OpenAI API не используется — только OpenRouter/Groq через OpenAI Python SDK.

## A2A flow

1. `GET /.well-known/agent.json` — Agent Card  
2. `sendMessage` (JSON-RPC) — Task + Artifact  

`a2a_system.py` помечен как deprecated — используйте `orchestrator.py`.

---

## 5. Пользователь

Briefly inform the user about the task result and perform any follow-up actions (if needed). If there's no follow-ups needed, don't explicitly say that.

## 6. Пользователь

Briefly inform the user about the task result and perform any follow-up actions (if needed). If there's no follow-ups needed, don't explicitly say that.

### Ассистент

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\terminals\367236.txt

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\terminals\103662.txt

---

### Ассистент

Кратко по фоновым задачам:

**`a2a-sdk` установлен** — зависимости и импорты работают.

**Calendar server упал** при первом запуске: `UnicodeEncodeError` на символ `→` в `shared/a2a_app.py` (Windows cp1251). Это уже исправлено (`->` вместо `→`). Flight server после этого запустился нормально.

Для запуска сейчас:

```bash
python start_agents.py
python orchestrator.py
```

И не забудьте вписать реальные ключи в `.env` — без них оркестратор получит 401 от OpenRouter.

---

## 7. Пользователь

1. Заполнил env. Протестируй
2. Зачем ты RAG в оркестратор добавил?

### Ассистент

Проверяю оркестратор на RAG и запускаю тест с вашим `.env` (файл не читаю).

- **Tool `Grep`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

- **Tool `Glob`**

---

### Ассистент

- **Tool `Grep`**: C:/Users/Irina/IT/AI_DRIVEN/Lesson_9_Agent2Agent (A2A)

- **Tool `Shell`**: Start flight A2A server

- **Tool `Shell`**: Start calendar A2A server

---

### Ассистент

- **Tool `Await`**

- **Tool `Await`**

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A\terminals\614111.txt

---

### Ассистент

- **Tool `Shell`**: Run full orchestrator end-to-end test

---

### Ассистент

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\calendar.json

---

### Ассистент

## 1. Тест — OK

Оркестратор отработал за 3 шага:

1. Discovery Flight + Calendar (Agent Cards)
2. A2A → Flight Agent (SU-123, 2025-05-25) — данные рейса получены
3. A2A → Calendar Agent — событие записано

`calendar.json` — новая запись id=4 с корректными данными рейса.

LLM: `openrouter/free`, ключи из `.env` подхватились (401 больше нет).

---

## 2. RAG — не добавлял

В `orchestrator.py` и во всём проекте Lesson 9 **нет RAG**: ни ChromaDB, ни `search_knowledge_base`, ни векторного поиска.

Оркестратор делает только:
- LLM (OpenRouter/Groq) + function calling
- два tools: `call_flight_agent` и `call_calendar_agent` → A2A `sendMessage`

RAG есть в **Lesson 8** (`full_agent.mjs`) — это другой проект. Возможно, вы перепутали или видели это в слайдах/плане как сравнение с Lesson 8. Если RAG где-то отображается в UI Cursor — это не из этого кода.

---

## 8. Пользователь

def _chunk_text(chunk: Any) - вот чанк = RAG

### Ассистент

`chunk` здесь — не RAG, а кусок потока ответа A2A (`sendMessage`). Переименую для ясности.

- **Tool `StrReplace`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\orchestrator.py

---

### Ассистент

**Нет, это не RAG.**

В RAG «chunk» — фрагмент документа из векторной базы (ChromaDB, `retrieve_chunks` в Lesson 7/8).

Здесь `chunk` / `event` — **событие из потока A2A** при `client.send_message()`:

```python
async for event in client.send_message(req):  # каждый event = StreamResponse
    # внутри: Task со статусом WORKING → COMPLETED и Artifact с текстом ответа
```

Это стандартный A2A SDK: агент не отдаёт всё одним JSON, а шлёт несколько событий (статус задачи, артефакт с результатом). Функция просто **достаёт текст из `task.artifacts`** — ответ Flight/Calendar агента.

Переименовал `_chunk_text` → `_a2a_event_text` и добавил комментарий, чтобы не путать с RAG.

---
