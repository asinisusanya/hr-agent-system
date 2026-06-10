# from router.llm_classifier import (
#     classify_with_llm
# )


# def classify_intent(message: str) -> dict:
#     """
#     Classify a request using Gemini with
#     rule-based fallback.
#     """

#     try:

#         result = classify_with_llm(
#             message
#         )

#         print(
#             "Intent classified by Gemini:",
#             result
#         )

#         return result

#     except Exception as e:

#         print(
#             "Gemini failed. Using fallback:",
#             e
#         )

#         text = message.lower()

#         if any(word in text for word in [
#             "policy",
#             "compliance",
#             "rule",
#             "regulation",
#             "guideline"
#         ]):
#             return {
#                 "intent": "compliance",
#                 "confidence": 0.90
#             }

#         if any(word in text for word in [
#             "leave",
#             "vacation",
#             "day off",
#             "off today",
#             "time off",
#             "sick"
#         ]):
#             return {
#                 "intent": "leave",
#                 "confidence": 0.90
#             }

#         if any(word in text for word in [
#             "meeting",
#             "meet",
#             "schedule",
#             "appointment",
#             "interview",
#             "discussion"
#         ]):
#             return {
#                 "intent": "scheduling",
#                 "confidence": 0.90
#             }

#         return {
#             "intent": "clarification",
#             "confidence": 0.50
#         }

import time

from router.llm_classifier import (
    classify_with_llm
)

import time


def classify_intent(message: str) -> dict:
    """
    Classify a request using Gemini with
    retry logic and rule-based fallback.
    """

    MAX_RETRIES = 3

    for attempt in range(MAX_RETRIES):

        try:

            result = classify_with_llm(
                message
            )

            print(
                f"Gemini success on attempt {attempt + 1}"
            )

            return result

        except Exception as e:

            print(
                f"Gemini failed on attempt {attempt + 1}:",
                e
            )

            if attempt < MAX_RETRIES - 1:

                print(
                    f"Retrying Gemini ({attempt + 2}/{MAX_RETRIES})"
                )

                time.sleep(1)

    print(
        "All Gemini retries failed. Using fallback."
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