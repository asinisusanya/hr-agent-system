from typing import List

from database.db import SessionLocal
from database.models import LongTermMemory

from memory.significance import (
    calculate_significance
)


def save_ltm(
    user_id: str,
    message: str
) -> None:
    """
    Store significant user information
    in long-term memory.

    Args:
        user_id: User identifier.
        message: User request.
    """

    score = calculate_significance(
        message
    )

    print(
        f"LTM Score for '{message}': {score}"
    )

    if score < 0.5:
        return

    db = SessionLocal()

    existing = (
        db.query(LongTermMemory)
        .filter(
            LongTermMemory.user_id == user_id,
            LongTermMemory.memory_text == message
        )
        .first()
    )

    if existing:
        db.close()
        return

    memory = LongTermMemory(
        user_id=user_id,
        memory_text=message,
        significance_score=score
    )

    db.add(memory)

    db.commit()

    db.close()


def get_long_term_memories(
    user_id: str
) -> List[LongTermMemory]:
    """
    Retrieve long-term memories
    for a user.

    Args:
        user_id: User identifier.

    Returns:
        Stored long-term memory entries.
    """

    db = SessionLocal()

    memories = (
        db.query(LongTermMemory)
        .filter(
            LongTermMemory.user_id == user_id
        )
        .order_by(
            LongTermMemory.significance_score.desc()
        )
        .all()
    )

    db.close()

    return memories