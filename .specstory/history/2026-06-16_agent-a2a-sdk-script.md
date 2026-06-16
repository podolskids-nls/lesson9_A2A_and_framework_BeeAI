# A2A SDK — скрипт на Python

_Дата: 2026-06-16 | Chat ID: `3d5c7764-17fc-46ac-9e89-90bf29ea7152` | Workspace: Lesson_9_Agent2Agent (A2A)_

---

## 1. Пользователь

Напиши скрипт на Python с использованием SDK, реализующий паттерн A2A (Agent-to-Agent). 
Мне нужно создать систему из 3-х ИИ-агентов:

1. Orchestrator Agent (Оркестратор):
- Принимает комплексный промпт от пользователя (например: "Я лечу в Москву 25 мая рейсом SU-123. Найди информацию о рейсе и занеси мне это в календарь").
- Имеет в своем арсенале инструменты (tools) для вызова двух других специализированных агентов.
- Сам не ходит во внешние API, его задача — проанализировать запрос, построить план, вызвать нужных агентов по очереди и собрать финальный ответ для пользователя.

2. Flight Agent (Агент рейсов):
- Принимает от оркестратора данные о рейсе (номер, дата).
- Делает запрос к бесплатному публичному API погоды или авиарейсов (если реального API нет, используй mock-функцию, имитирующую успешный ответ от API без авторизации, возвращающую статус рейса, время вылета/прилета и терминал).
- Возвращает структурированный текстовый ответ оркестратору.

3. Calendar Agent (Агент календаря):
- Принимает от оркестратора структурированные данные о событии (название, дата, время, описание).
- Использует бесплатное/открытое API (или mock-функцию, имитирующую запись в JSON-файл `calendar.json` в качестве "базы данных" календаря) для успешного сохранения события.
- Возвращает подтверждение успешной записи.

Требования к коду:
- Используй бесплатный API из проекта C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent
- Реализуй механизм Function Calling (tools) у Оркестратора. Функциями для него должны являться вызовы функций `call_flight_agent` и `call_calendar_agent`.
- Код должен быть в одном файле (или аккуратно разделен на модули), с понятными логами в консоли, чтобы было видно, как Оркестратор передает управление Агенту 1, получает ответ, а затем вызывает Агента 2.
- Не используй сложные сторонние фреймворки вроде LangChain или CrewAI — только чистый SDK, функции и Python.

### Ассистент

Изучаю SDK и проект Lesson_8, чтобы подключить тот же бесплатный API и собрать A2A-скрипт.

- **Tool `Read`**: C:\Users\Irina\.cursor\skills-cursor\sdk\SKILL.md

- **Tool `Glob`**

- **Tool `Glob`**

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\full_agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\agent.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\README.md

- **Tool `Shell`**: List Lesson 9 project directory

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\tools.mjs

- **Tool `Read`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent\.env.example

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN\Lesson_8_My_own_agent

---

### Ассистент

- **Tool `Grep`**: C:\Users\Irina\IT\AI_DRIVEN

- **Tool `Read`**: C:\Users\Irina\.cursor\skills-cursor\sdk\SKILL.md

---

### Ассистент

Создаю Python-скрипт по образцу Lesson 8: OpenAI SDK + OpenRouter и function calling для оркестратора.

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\requirements.txt

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\.env.example

- **Tool `Write`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\a2a_system.py

---

### Ассистент

- **Tool `Shell`**: Install deps and run A2A demo script

---

### Ассистент

- **Tool `Await`**

---

### Ассистент

- **Tool `Read`**: C:\Users\Irina\.cursor\projects\c-Users-Irina-IT-AI-DRIVEN-Lesson-9-Agent2Agent-A2A/terminals/457446.txt

---

### Ассистент

- **Tool `Shell`**: Check if Lesson 8 .env exists

- **Tool `Await`**

---

### Ассистент

- **Tool `Shell`**: Run script with unbuffered output, limit lines

---

### Ассистент

Скрипт работает; исправляю кодировку вывода в консоли Windows.

- **Tool `StrReplace`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\a2a_system.py

- **Tool `Read`**: c:\Users\Irina\IT\AI_DRIVEN\Lesson_9_Agent2Agent (A2A)\calendar.json

---

### Ассистент

- **Tool `Shell`**: Re-run A2A script to verify UTF-8 fix

---

### Ассистент

Готова система A2A из трёх агентов в одном файле `a2a_system.py`.

## Архитектура

```mermaid
flowchart LR
    User[Пользователь] --> Orch[Orchestrator Agent]
    Orch -->|call_flight_agent| Flight[Flight Agent]
    Orch -->|call_calendar_agent| Cal[Calendar Agent]
    Flight --> MockAPI[Mock Flight API]
    Cal --> JSON[(calendar.json)]
    Flight --> Orch
    Cal --> Orch
    Orch --> User
```

| Агент | Роль |
|---|---|
| **Orchestrator** | Анализирует запрос, вызывает tools через OpenAI Responses API + OpenRouter |
| **Flight Agent** | Mock API рейсов (статус, время, терминал) |
| **Calendar Agent** | Сохраняет события в `calendar.json` |

## Файлы

- `a2a_system.py` — основной скрипт
- `requirements.txt` — `openai`, `python-dotenv`
- `.env.example` — шаблон ключей (как в Lesson 8)

Ключ `OPENROUTER_API_KEY` подхватывается автоматически из `Lesson_8_My_own_agent/.env`, если локального `.env` нет.

## Запуск

```bash
cd "Lesson_9_Agent2Agent (A2A)"
pip install -r requirements.txt
python a2a_system.py
```

Со своим промптом:

```bash
python a2a_system.py "Я лечу в Москву 25 мая рейсом SU-123. Найди информацию о рейсе и занеси мне это в календарь"
```

## Что видно в логах

При успешном прогоне в консоли видна цепочка:

1. `[Orchestrator]` → `function_call: call_flight_agent`
2. `[Orchestrator >>> Flight Agent]` → `[Flight API (mock)]` → ответ оркестратору
3. `[Orchestrator >>> Calendar Agent]` → запись в `calendar.json`
4. Финальный ответ пользователю

## Function Calling у оркестратора

Два инструмента, как в `tools.mjs` из Lesson 8:

- `call_flight_agent(flight_number, date)` — делегирует Flight Agent
- `call_calendar_agent(title, date, time, description)` — делегирует Calendar Agent

Оркестратор сам не ходит во внешние API — только вызывает эти функции в цикле до 10 шагов.

## Mock-данные

В mock-базе есть рейсы **SU-123** и **SU-456**. Чтобы добавить другие — расширьте словарь `MOCK_FLIGHTS` в начале файла.

---
