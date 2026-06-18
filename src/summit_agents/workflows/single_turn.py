from contextlib import nullcontext
from typing import Any

from agents import Runner, trace

from summit_agents.agents.factory import AgentName, build_agent
from summit_agents.integrations.storage import build_session
from summit_agents.settings import get_settings


async def run_once(
    message: str,
    agent_name: AgentName = "router",
    session_id: str | None = None,
) -> Any:
    settings = get_settings()
    agent = build_agent(agent_name, settings)
    session = build_session(session_id)

    trace_context = (
        trace(f"{settings.app_name}:{agent_name}") if settings.tracing_enabled else nullcontext()
    )

    with trace_context:
        run_options = {"session": session} if session else {}
        result = await Runner.run(agent, message, **run_options)

    return result.final_output
