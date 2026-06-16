"""Минимальная обёртка a2a-sdk для запуска A2A-сервера."""
from __future__ import annotations

from collections.abc import Callable

import uvicorn
from a2a.helpers import (
    get_message_text,
    new_task_from_user_message,
    new_text_message,
    new_text_part,
)
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.routes import create_agent_card_routes, create_jsonrpc_routes
from a2a.server.tasks import InMemoryTaskStore, TaskUpdater
from a2a.types import AgentCapabilities, AgentCard, AgentInterface, AgentSkill
from a2a.types.a2a_pb2 import TaskState
from starlette.applications import Starlette


def run_server(
    port: int,
    name: str,
    description: str,
    skill_id: str,
    skill_name: str,
    skill_desc: str,
    handler: Callable[[str], str],
) -> None:
    url = f"http://127.0.0.1:{port}"
    skill = AgentSkill(
        id=skill_id,
        name=skill_name,
        description=skill_desc,
        input_modes=["text/plain"],
        output_modes=["text/plain"],
        tags=["a2a"],
    )
    card = AgentCard(
        name=name,
        description=description,
        version="1.0.0",
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        capabilities=AgentCapabilities(streaming=False),
        supported_interfaces=[
            AgentInterface(protocol_binding="JSONRPC", url=url),
        ],
        skills=[skill],
    )

    class Executor(AgentExecutor):
        async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
            task = context.current_task or new_task_from_user_message(context.message)
            if not context.current_task:
                await event_queue.enqueue_event(task)
            updater = TaskUpdater(event_queue=event_queue, task_id=task.id, context_id=task.context_id)
            await updater.update_status(
                state=TaskState.TASK_STATE_WORKING,
                message=new_text_message("Обработка..."),
            )
            text = get_message_text(context.message) or ""
            result = handler(text)
            await updater.add_artifact(parts=[new_text_part(text=result, media_type="text/plain")])
            await updater.update_status(
                state=TaskState.TASK_STATE_COMPLETED,
                message=new_text_message("Готово"),
            )

        async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
            raise NotImplementedError("cancel not supported")

    request_handler = DefaultRequestHandler(
        agent_executor=Executor(),
        task_store=InMemoryTaskStore(),
        agent_card=card,
    )
    routes = create_agent_card_routes(card) + create_jsonrpc_routes(request_handler, "/")
    print(f"[A2A] {name} -> {url}")
    uvicorn.run(Starlette(routes=routes), host="127.0.0.1", port=port, log_level="warning")
