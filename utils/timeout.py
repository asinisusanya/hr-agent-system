import os
import time

from dotenv import load_dotenv

load_dotenv()

TIMEOUT_SECONDS = int(
    os.getenv(
        "REQUEST_TIMEOUT",
        5
    )
)


from typing import Any, Callable

def execute_with_timeout(
    func: Callable,
    *args: Any,
    **kwargs: Any
) -> Any:
    """
    Execute a function while monitoring execution time.

    Args:
        func: Function to execute.
        *args: Positional arguments.
        **kwargs: Keyword arguments.

    Returns:
        Function result.

    Raises:
        TimeoutError if execution exceeds configured limit.
    """

    start = time.time()

    result = func(
        *args,
        **kwargs
    )

    elapsed = time.time() - start

    if elapsed > TIMEOUT_SECONDS:

        raise TimeoutError(
            "Request exceeded timeout"
        )

    return result