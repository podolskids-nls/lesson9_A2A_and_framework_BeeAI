"""BeeAI ChatModel из .env проекта (OpenRouter / Groq)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

# Python 3.14: обход pydantic TypedDict forward-ref bug в beeai-framework
import beeai_framework.backend.chat as _chat_module

_chat_module._ChatModelKwargsAdapter.validate_python = lambda kwargs, **_: dict(kwargs) if kwargs else {}

from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.adapters.openai import OpenAIChatModel
from beeai_framework.backend import ChatModel


def create_chat_model() -> ChatModel:
    provider = os.getenv("LLM_PROVIDER", "openrouter").lower()
    if provider == "groq":
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY не задан в .env")
        return GroqChatModel(
            model_id=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            api_key=key,
        )
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY не задан в .env")
    return OpenAIChatModel(
        model_id=os.getenv("OPENROUTER_MODEL", "openrouter/free"),
        api_key=key,
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
    )
