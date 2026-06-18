from datetime import UTC, datetime

from agents import function_tool


@function_tool
def event_context() -> str:
    """Return public context about this demo repository and its intended audience."""
    return (
        "Este repositorio e um starter Python para uma palestra sobre OpenAI Agents SDK. "
        "Ele prioriza prompts editaveis, tools registraveis, integracoes plugaveis, "
        "sessoes opcionais e tracing para depuracao."
    )


@function_tool
def list_extension_points() -> list[str]:
    """List the main extension points available in the starter project."""
    return [
        "prompts/: edite instrucoes em Markdown",
        "src/summit_agents/tools/custom.py: registre function tools",
        "src/summit_agents/integrations/: conecte MCP, APIs e storage",
        "src/summit_agents/agents/factory.py: componha agentes e handoffs",
        "src/summit_agents/workflows/: ajuste execucao, streaming e estado",
        "src/summit_agents/guardrails/: adicione validacoes e politicas",
    ]


@function_tool
def utc_now() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(UTC).isoformat()
