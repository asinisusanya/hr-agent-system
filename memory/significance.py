PREFERENCE_WORDS = [
    "prefer",
    "preferred",
    "usually",
    "always",
    "typically",
    "favorite",
    "dislike",
    "never"
]

LONG_TERM_PATTERNS = [
    "i prefer",
    "i usually",
    "i always",
    "my preferred",
    "my favorite",
    "i dislike"
]


def calculate_significance(
    message: str
) -> float:
    """
    Calculate significance score
    for long-term memory storage.

    Scores are based on whether
    the message contains persistent
    preferences, habits, or recurring
    user characteristics.

    Returns:
        Score between 0.0 and 1.0
    """

    text = message.lower()

    score = 0.0

    for pattern in LONG_TERM_PATTERNS:

        if pattern in text:
            score += 0.5

    for word in PREFERENCE_WORDS:

        if word in text:
            score += 0.1

    return min(score, 1.0)