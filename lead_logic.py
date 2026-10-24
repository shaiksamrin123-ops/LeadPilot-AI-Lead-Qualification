def qualify_lead_logic(
    customer_name: str,
    budget: float,
    interest_level: str,
    urgency: str
) -> dict:
    """Score a sales lead and recommend a follow-up action."""

    if not customer_name.strip():
        raise ValueError("Customer name cannot be empty.")

    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    interest_level = interest_level.lower().strip()
    urgency = urgency.lower().strip()

    if interest_level not in ["hot", "warm", "cold"]:
        raise ValueError("Interest must be hot, warm, or cold.")

    if urgency not in ["high", "medium", "low"]:
        raise ValueError("Urgency must be high, medium, or low.")

    score = 0

    if budget >= 50000:
        score += 30
    elif budget >= 20000:
        score += 20
    else:
        score += 10

    score += {"hot": 40, "warm": 25, "cold": 10}[interest_level]
    score += {"high": 30, "medium": 20, "low": 10}[urgency]

    if score >= 80:
        priority = "High"
        action = "Contact the customer as soon as possible."
    elif score >= 60:
        priority = "Medium"
        action = "Follow up with the customer soon."
    else:
        priority = "Low"
        action = "Send more information and nurture the lead."

    return {
        "customer_name": customer_name,
        "lead_score": score,
        "priority": priority,
        "recommended_action": action
    }
