"""Register project-specific tools here.

Example:

from agents import function_tool


@function_tool
def lookup_order(order_id: str) -> str:
    \"\"\"Return public order status for a known order id.\"\"\"
    return f"Order {order_id} is in progress."


CUSTOM_TOOLS = {"lookup_order": lookup_order}
"""

CUSTOM_TOOLS = {}
