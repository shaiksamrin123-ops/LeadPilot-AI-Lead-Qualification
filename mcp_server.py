from fastmcp import FastMCP
from lead_logic import qualify_lead_logic

mcp = FastMCP("LeadPilot")


@mcp.tool
def qualify_lead(
    customer_name: str,
    budget: float,
    interest_level: str,
    urgency: str
) -> dict:
    """Qualify a sales lead and recommend a follow-up action."""
    return qualify_lead_logic(
        customer_name=customer_name,
        budget=budget,
        interest_level=interest_level,
        urgency=urgency
    )
