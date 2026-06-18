from typing import Literal

from agents import Agent

from summit_agents.prompts import load_prompt
from summit_agents.settings import Settings, get_settings
from summit_agents.tools.registry import get_tools


AgentName = Literal["router", "assistant", "researcher"]


def build_assistant(settings: Settings | None = None) -> Agent:
    resolved = settings or get_settings()
    return Agent(
        name="summit_assistant",
        handoff_description="Especialista para duvidas gerais e exemplos praticos do starter.",
        instructions=load_prompt("assistant", {"app_name": resolved.app_name}),
        model=resolved.openai_model,
        tools=get_tools(["event_context", "list_extension_points", "utc_now"]),
    )


def build_researcher(settings: Settings | None = None) -> Agent:
    resolved = settings or get_settings()
    return Agent(
        name="implementation_researcher",
        handoff_description="Especialista para arquitetura, tradeoffs e extensoes do starter.",
        instructions=load_prompt("researcher"),
        model=resolved.openai_model,
        tools=get_tools(["event_context", "list_extension_points"]),
    )


def build_router(settings: Settings | None = None) -> Agent:
    resolved = settings or get_settings()
    assistant = build_assistant(resolved)
    researcher = build_researcher(resolved)

    return Agent(
        name="summit_router",
        instructions=load_prompt("router"),
        model=resolved.openai_model,
        handoffs=[assistant, researcher],
        tools=get_tools(["event_context"]),
    )


def build_agent(agent_name: AgentName = "router", settings: Settings | None = None) -> Agent:
    if agent_name == "assistant":
        return build_assistant(settings)
    if agent_name == "researcher":
        return build_researcher(settings)
    if agent_name == "router":
        return build_router(settings)

    raise ValueError(f"Unknown agent: {agent_name}")
