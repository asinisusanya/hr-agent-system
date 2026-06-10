from router.llm_classifier import (
    classify_with_llm
)


def classify_intent(message: str) -> dict:
    """
    Classify a request using Gemini with
    rule-based fallback.
    """

    try:

        result = classify_with_llm(
            message
        )

        print(
            "Intent classified by Gemini:",
            result
        )

        return result

    except Exception as e:

        print(
            "Gemini failed. Using fallback:",
            e
        )

        text = message.lower()

        if any(word in text for word in [
            "policy",
            "compliance",
            "rule",
            "regulation",
            "guideline"
        ]):
            return {
                "intent": "compliance",
                "confidence": 0.90
            }

        if any(word in text for word in [
            "leave",
            "vacation",
            "day off",
            "off today",
            "time off",
            "sick"
        ]):
            return {
                "intent": "leave",
                "confidence": 0.90
            }

        if any(word in text for word in [
            "meeting",
            "meet",
            "schedule",
            "appointment",
            "interview",
            "discussion"
        ]):
            return {
                "intent": "scheduling",
                "confidence": 0.90
            }

        return {
            "intent": "clarification",
            "confidence": 0.50
        }