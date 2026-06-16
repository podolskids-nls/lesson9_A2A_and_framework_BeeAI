"""BeeAI Runnable без LLM — детерминированный handler для A2A-сервера."""
from __future__ import annotations

from collections.abc import Callable

from beeai_framework.backend.message import AnyMessage, AssistantMessage, UserMessage
from beeai_framework.emitter import Emitter
from beeai_framework.runnable import Runnable, RunnableOutput, runnable_entry


class HandlerRunnable(Runnable[RunnableOutput]):
    def __init__(self, handler: Callable[[str], str]) -> None:
        super().__init__()
        self._handler = handler
        self._emitter = Emitter.root().child(namespace=["runnable", "handler"], creator=self)

    @property
    def emitter(self) -> Emitter:
        return self._emitter

    @runnable_entry
    async def run(self, input: list[AnyMessage], /, **kwargs) -> RunnableOutput:
        text = ""
        for msg in reversed(input):
            if isinstance(msg, UserMessage):
                text = msg.text
                break
        result = self._handler(text)
        return RunnableOutput(output=[AssistantMessage(result)])
