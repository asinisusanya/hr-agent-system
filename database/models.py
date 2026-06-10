from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime

from database.db import Base


class ShortTermMemory(Base):
    __tablename__ = "short_term_memory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    message = Column(Text)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)


class LongTermMemory(Base):
    __tablename__ = "long_term_memory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    memory_text = Column(Text)
    significance_score = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)

    request = Column(Text)
    intent = Column(String)
    confidence = Column(Float)
    agent = Column(String)

    response = Column(Text)
    status = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)