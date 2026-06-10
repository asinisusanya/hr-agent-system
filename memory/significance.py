IMPORTANT_WORDS = [
    "always",
    "prefer",
    "important",
    "remember",
    "never",
    "usually",
    "typically",
    "like",
    "dislike",
    "favorite"
]


def calculate_significance(
    message: str
) -> float:
    """
    Calculate significance score for
    long-term memory storage.

    Preference-related statements receive
    higher scores.

    Args:
        message: User request.

    Returns:
        Significance score between 0.0 and 1.0.
    """

    score = 0.2

    text = message.lower()

    for word in IMPORTANT_WORDS:

        if word in text:
            score += 0.3

    return min(score, 1.0)