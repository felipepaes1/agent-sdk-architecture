from collections.abc import Iterable
from typing import Any

from summit_agents.tools.custom import CUSTOM_TOOLS
from summit_agents.tools.examples import event_context, list_extension_points, utc_now


TOOL_REGISTRY: dict[str, Any] = {
    "event_context": event_context,
    "list_extension_points": list_extension_points,
    "utc_now": utc_now,
    **CUSTOM_TOOLS,
}


def get_tools(names: Iterable[str] | None = None) -> list[Any]:
    if names is None:
        return list(TOOL_REGISTRY.values())

    selected = []
    missing = []
    for name in names:
        tool = TOOL_REGISTRY.get(name)
        if tool is None:
            missing.append(name)
        else:
            selected.append(tool)

    if missing:
        available = ", ".join(sorted(TOOL_REGISTRY))
        raise KeyError(f"Unknown tools: {', '.join(missing)}. Available: {available}")

    return selected
