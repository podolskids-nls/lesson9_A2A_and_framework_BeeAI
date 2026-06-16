"""Загрузка .env и LLM-клиент (OpenRouter / Groq). Не читать .env вручную — только dotenv."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

FLIGHT_AGENT_URL = os.getenv("FLIGHT_AGENT_URL", "http://127.0.0.1:8001")
CALENDAR_AGENT_URL = os.getenv("CALENDAR_AGENT_URL", "http://127.0.0.1:8002")


def create_llm_client() -> tuple[OpenAI, str]:
    provider = os.getenv("LLM_PROVIDER", "openrouter").lower()
    if provider == "groq":
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY не задан в .env")
        return OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=key,
        ), os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY не задан в .env")
    return OpenAI(
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        api_key=key,
    ), os.getenv("OPENROUTER_MODEL", "openrouter/free")
