def handle(message: str) -> str:
    """
    Handle low-confidence or unclear requests.

    Args:
        message: User's natural language request.

    Returns:
        A clarification request response.
    """
    return (
        "I'm not sure what you need. "
        "Could you clarify whether this relates to "
        "leave, scheduling, or compliance?"
    )