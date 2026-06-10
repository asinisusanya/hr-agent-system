from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from database.init_db import init_db
from database.db import SessionLocal
from database.models import AuditLog

from app.schemas import RequestModel

from memory.delete_memory import (
    clear_user_memory,
    clear_stm,
    clear_ltm
)

from memory.stm import get_recent_memories
from memory.ltm import get_long_term_memories


from graph.workflow import graph


app = FastAPI(
    title="HR Multi-Agent System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup() -> None:
    """
    Initialize database tables during application startup.
    """
    init_db()


@app.get("/")
def root() -> dict:
    """
    Root endpoint used to verify service availability.
    """
    return {
        "message": "HR Multi-Agent System Running"
    }


@app.get("/health")
def health() -> dict:
    """
    Health check endpoint.

    Returns:
        Current application status.
    """
    return {
        "status": "healthy"
    }


@app.post("/request")
def process_request(
    request: RequestModel
) -> dict:
    """
    Process a user request through the LangGraph
    orchestration workflow.
    """

    try:

        start_time = time.time()

        result = graph.invoke(
            {
                "user_id": request.user_id,
                "message": request.message
            }
        )

        elapsed_time = round(
            time.time() - start_time,
            2
        )

        return {
            "intent": result["intent"],
            "confidence": result["confidence"],
            "response": result["response"],
            "time_taken": elapsed_time
        }

    except TimeoutError:

        return {
            "status": "error",
            "message": "Request timed out. Please try again."
        }

    except Exception:

        return {
            "status": "error",
            "message": (
                "Unable to process request "
                "at the moment."
            )
        }

@app.get("/memory/{user_id}")
def get_memory(
    user_id: str
) -> dict:
    """
    Retrieve STM and LTM records for a user.
    """

    stm = get_recent_memories(user_id)

    ltm = get_long_term_memories(user_id)

    return {
        "short_term_memory": [
            {
                "message": memory.message,
                "response": memory.response
            }
            for memory in stm
        ],
        "long_term_memory": [
            {
                "memory": memory.memory_text,
                "score": memory.significance_score
            }
            for memory in ltm
        ]
    }


@app.get("/audit")
def get_audit() -> list:
    """
    Retrieve append-only audit log entries.
    """

    db = SessionLocal()

    logs = db.query(AuditLog).all()

    audit_data = []

    for log in logs:
        # audit_data.append(
        #     {
        #         "user_id": log.user_id,
        #         "request": log.request,
        #         "intent": log.intent,
        #         "confidence": log.confidence,
        #         "agent": log.agent,
        #         "response": log.response,
        #         "status": log.status
        #     }
        # )
        audit_data.append(
            {
                "id": log.id,
                "timestamp": log.timestamp,

                "user_id": log.user_id,

                "request": log.request,

                "intent": log.intent,
                "confidence": log.confidence,

                "agent": log.agent,

                "response": log.response,

                "status": log.status
            }
        )

    db.close()

    return audit_data

@app.delete("/memory/stm/{user_id}")
def delete_stm(
    user_id: str
) -> dict:
    """
    Clear only short-term memory.
    """

    clear_stm(user_id)

    return {
        "message":
        f"STM cleared for user {user_id}"
    }


@app.delete("/memory/ltm/{user_id}")
def delete_ltm(
    user_id: str
) -> dict:
    """
    Clear only long-term memory.
    """

    clear_ltm(user_id)

    return {
        "message":
        f"LTM cleared for user {user_id}"
    }


@app.delete("/memory/{user_id}")
def delete_memory(
    user_id: str
) -> dict:
    """
    Clear all memory records for a user.
    """

    clear_user_memory(user_id)

    return {
        "message":
        f"Memory cleared for user {user_id}"
    }