import time
import os
from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = int(
    os.getenv("MAX_RETRIES", 3)
)


from typing import Any, Callable

def execute_with_retry(
    func: Callable,
    *args: Any,
    **kwargs: Any
) -> Any:
    """
    Execute a function with retry support.

    Args:
        func: Function to execute.
        *args: Positional arguments.
        **kwargs: Keyword arguments.

    Returns:
        Function result.

    Raises:
        Last exception if all retries fail.
    """

    last_exception = None

    for attempt in range(MAX_RETRIES):

        try:
            return func(
                *args,
                **kwargs
            )

        except Exception as e:

            last_exception = e

            print(
                f"Retry {attempt + 1} failed"
            )

            time.sleep(1)

    raise last_exception