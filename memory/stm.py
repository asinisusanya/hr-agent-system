from database.db import SessionLocal
from database.models import ShortTermMemory


def save_stm(
    user_id: str,
    message: str,
    response: str
) -> None:
    """
    Store an interaction in short-term memory.

    Args:
        user_id: User identifier.
        message: User request.
        response: System response.
    """

    db = SessionLocal()

    memory = ShortTermMemory(
        user_id=user_id,
        message=message,
        response=response
    )

    db.add(memory)
    db.commit()
    db.close()


from typing import List

def get_recent_memories(
    user_id: str
) -> List[ShortTermMemory]:
    """
    Retrieve recent interactions for a user.

    Args:
        user_id: User identifier.

    Returns:
        Up to five recent STM entries.
    """

    db = SessionLocal()

    memories = (
        db.query(ShortTermMemory)
        .filter(ShortTermMemory.user_id == user_id)
        .order_by(ShortTermMemory.timestamp.desc())
        .limit(5)
        .all()
    )

    db.close()

    return memories