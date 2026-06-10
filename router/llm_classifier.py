import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_with_llm(message: str) -> dict:
    """
    Classify HR requests using Gemini.

    Args:
        message: User request.

    Returns:
        Dictionary containing intent and confidence.
    """

    prompt = f"""
You are an HR intent classifier.

Classify the employee request into EXACTLY ONE category.

Categories:

1. leave
Examples:
- Can I take leave tomorrow?
- I need a day off.
- I need off today.
- Vacation request.
- Sick leave request.

2. scheduling
Examples:
- Schedule a meeting.
- Arrange an interview.
- Need to meet HR.
- Can I meet HR?
- Need to meet the boss.
- Arrange a discussion with the manager.
- Book an appointment.

3. compliance
Examples:
- What is the remote work policy?
- What are company regulations?
- Explain leave policy.
- What are the compliance requirements?

4. clarification
Examples:
- Help me.
- I have a problem.
- Can you assist me?
- I need support.

Return ONLY valid JSON.

Example:

{{
    "intent": "scheduling",
    "confidence": 0.95
}}

Request:
{message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown fences if Gemini adds them
    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    result = json.loads(text)

    if result["confidence"] < 0.60:
        result["intent"] = "clarification"

    return result