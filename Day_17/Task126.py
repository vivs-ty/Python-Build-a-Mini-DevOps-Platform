# Task 126: Limit how many times a function can be called in a time window.

import time
from typing import Callable, Any
def rate_limit(calls: int, period: float):
    def decorator(func: Callable) -> Callable:
        call_times = []
        def wrapper(*args, **kwargs) -> Any:
            nonlocal call_times
            current_time = time.time()
            call_times = [t for t in call_times if current_time - t < period]
            if len(call_times) >= calls:
                raise Exception(f"Rate limit exceeded: {calls} calls in {period} seconds.")
            call_times.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator
