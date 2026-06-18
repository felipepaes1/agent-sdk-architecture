from dataclasses import dataclass
from typing import Any

from agents import HostedMCPTool


@dataclass(frozen=True)
class HostedMCPServerConfig:
    server_label: str
    server_url: str
    require_approval: str = "never"
    server_description: str | None = None


def build_hosted_mcp_tool(config: HostedMCPServerConfig) -> HostedMCPTool:
    tool_config: dict[str, Any] = {
        "type": "mcp",
        "server_label": config.server_label,
        "server_url": config.server_url,
        "require_approval": config.require_approval,
    }

    if config.server_description:
        tool_config["server_description"] = config.server_description

    return HostedMCPTool(tool_config=tool_config)


def build_hosted_mcp_tools(configs: list[HostedMCPServerConfig]) -> list[HostedMCPTool]:
    return [build_hosted_mcp_tool(config) for config in configs]
