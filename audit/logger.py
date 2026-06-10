from database.db import SessionLocal
from database.models import AuditLog


def log_request(
    user_id: str,
    request: str,
    intent: str,
    confidence: float,
    agent: str,
    response: str,
    status: str
) -> None:
    """
    Create an append-only audit record.

    Args:
        user_id: User identifier.
        request: Original user request.
        intent: Classified intent.
        confidence: Classification confidence.
        agent: Selected agent.
        response: Agent response.
        status: Processing status.
    """

    db = SessionLocal()

    log = AuditLog(
        user_id=user_id,
        request=request,
        intent=intent,
        confidence=confidence,
        agent=agent,
        response=response,
        status=status
    )

    db.add(log)
    db.commit()
    db.close()