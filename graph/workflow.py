from langgraph.graph import StateGraph, END

from graph.state import AgentState

from utils.retry import execute_with_retry
from utils.timeout import execute_with_timeout

from router.intent_classifier import classify_intent
from router.router import route_to_agent

from memory.stm import (
    save_stm,
    get_recent_memories
)

from memory.ltm import (
    save_ltm,
    get_long_term_memories
)

from audit.logger import log_request


def classify_node(
    state: AgentState
) -> AgentState:
    """
    Classify user intent and attach confidence score
    to workflow state.
    """

    result = classify_intent(
        state["message"]
    )

    state["intent"] = result["intent"]
    state["confidence"] = result["confidence"]

    return state


def memory_retrieval_node(
    state: AgentState
) -> AgentState:
    """
    Retrieve STM and LTM records and inject
    contextual information into the workflow state.
    """

    stm = get_recent_memories(
        state["user_id"]
    )

    ltm = get_long_term_memories(
        state["user_id"]
    )

    context_parts = []

    for memory in stm:
        context_parts.append(
            f"Recent: {memory.message}"
        )

    for memory in ltm:
        context_parts.append(
            f"Preference: {memory.memory_text}"
        )

    state["context"] = "\n".join(
        context_parts
    )

    return state


def agent_node(
    state: AgentState
) -> AgentState:
    """
    Execute the selected agent using retry and
    timeout protection.
    """

    response = execute_with_retry(
        execute_with_timeout,
        route_to_agent,
        state["intent"],
        state["message"]
    )

    # Store clean response for memory
    state["raw_response"] = response

    # Add context only for API output
    if state.get("context"):

        response += (
            f"\n\nContext Found:\n"
            f"{state['context']}"
        )

    state["response"] = response

    return state


def memory_node(state: AgentState):
    """
    Persist interaction into STM and LTM stores.
    """

    save_stm(
        state["user_id"],
        state["message"],
        state["raw_response"]
    )

    save_ltm(
        state["user_id"],
        state["message"]
    )

    return state


def audit_node(
    state: AgentState
) -> AgentState:
    """
    Record workflow execution details in the
    append-only audit log.
    """

    log_request(
        user_id=state["user_id"],
        request=state["message"],
        intent=state["intent"],
        confidence=state["confidence"],
        agent=state["intent"],
        response=state["response"],
        status="SUCCESS"
    )

    return state


def build_graph():
    """
    Construct and compile the LangGraph workflow.

    Workflow:
        Classify
            ↓
        Retrieve Memory
            ↓
        Agent Execution
            ↓
        Memory Storage
            ↓
        Audit Logging
    """

    workflow = StateGraph(AgentState)

    workflow.add_node(
        "classify",
        classify_node
    )

    workflow.add_node(
        "retrieve_memory",
        memory_retrieval_node
    )

    workflow.add_node(
        "agent",
        agent_node
    )

    workflow.add_node(
        "memory",
        memory_node
    )

    workflow.add_node(
        "audit",
        audit_node
    )

    workflow.set_entry_point(
        "classify"
    )

    workflow.add_edge(
        "classify",
        "retrieve_memory"
    )

    workflow.add_edge(
        "retrieve_memory",
        "agent"
    )

    workflow.add_edge(
        "agent",
        "memory"
    )

    workflow.add_edge(
        "memory",
        "audit"
    )

    workflow.add_edge(
        "audit",
        END
    )

    return workflow.compile()


graph = build_graph()