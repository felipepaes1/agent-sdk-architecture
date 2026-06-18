import asyncio
from typing import cast

import typer
from dotenv import load_dotenv
from rich.console import Console

from summit_agents.agents.factory import AgentName
from summit_agents.settings import get_settings
from summit_agents.workflows.single_turn import run_once


load_dotenv()

app = typer.Typer(no_args_is_help=True, help="CLI para o starter do OpenAI Agents SDK.")
console = Console()


@app.command()
def doctor() -> None:
    """Check local configuration before making API calls."""
    settings = get_settings()

    console.print(f"App: [bold]{settings.app_name}[/bold]")
    console.print(f"Model: [bold]{settings.openai_model}[/bold]")
    console.print(f"Prompts: {settings.prompts_dir}")
    console.print(f"Tracing: {settings.tracing_enabled}")

    if settings.openai_api_key:
        console.print("OPENAI_API_KEY: [green]configured[/green]")
    else:
        console.print("OPENAI_API_KEY: [red]missing[/red]")
        raise typer.Exit(code=1)


@app.command()
def ask(
    message: str = typer.Argument(..., help="Mensagem enviada ao agente."),
    agent: str = typer.Option("router", "--agent", "-a", help="router, assistant ou researcher."),
    session: str | None = typer.Option(None, "--session", "-s", help="ID de sessao SQLite."),
) -> None:
    """Run a single turn through the selected agent."""
    if agent not in {"router", "assistant", "researcher"}:
        raise typer.BadParameter("Use router, assistant ou researcher.")

    output = asyncio.run(
        run_once(message=message, agent_name=cast(AgentName, agent), session_id=session)
    )
    console.print(output)


if __name__ == "__main__":
    app()
