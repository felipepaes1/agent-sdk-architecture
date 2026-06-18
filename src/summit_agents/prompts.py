from collections.abc import Mapping
from pathlib import Path
from string import Template

from summit_agents.settings import get_settings


def load_prompt(
    name: str,
    variables: Mapping[str, object] | None = None,
    prompts_dir: Path | None = None,
) -> str:
    """Load a Markdown prompt and safely substitute `$variables`."""
    root = (prompts_dir or get_settings().prompts_dir).resolve()
    path = _resolve_prompt_path(name, root)
    text = path.read_text(encoding="utf-8").strip()

    if not variables:
        return text

    string_variables = {key: str(value) for key, value in variables.items()}
    return Template(text).safe_substitute(string_variables)


def _resolve_prompt_path(name: str, root: Path) -> Path:
    relative_name = name if name.endswith(".md") else f"{name}.md"
    candidate = (root / relative_name).resolve()

    if candidate != root and root not in candidate.parents:
        raise ValueError(f"Prompt path escapes prompts directory: {name}")

    if not candidate.exists():
        raise FileNotFoundError(f"Prompt not found: {candidate}")

    return candidate
