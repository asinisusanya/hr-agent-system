from typing import TypedDict


class AgentState(TypedDict):
    user_id: str
    message: str
    intent: str
    confidence: float
    response: str
    raw_response: str
    context: str