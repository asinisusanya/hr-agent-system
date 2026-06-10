from database.db import SessionLocal
from database.models import (
    ShortTermMemory,
    LongTermMemory
)


def clear_stm(
    user_id: str
) -> None:
    """
    Remove only STM records for a user.
    """

    db = SessionLocal()

    db.query(
        ShortTermMemory
    ).filter(
        ShortTermMemory.user_id == user_id
    ).delete()

    db.commit()

    db.close()


def clear_ltm(
    user_id: str
) -> None:
    """
    Remove only LTM records for a user.
    """

    db = SessionLocal()

    db.query(
        LongTermMemory
    ).filter(
        LongTermMemory.user_id == user_id
    ).delete()

    db.commit()

    db.close()


def clear_user_memory(
    user_id: str
) -> None:
    """
    Remove all STM and LTM records associated with a user.
    """

    db = SessionLocal()

    db.query(
        ShortTermMemory
    ).filter(
        ShortTermMemory.user_id == user_id
    ).delete()

    db.query(
        LongTermMemory
    ).filter(
        LongTermMemory.user_id == user_id
    ).delete()

    db.commit()

    db.close()