from database.db import engine, Base
from database.models import (
    ShortTermMemory,
    LongTermMemory,
    AuditLog
)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)