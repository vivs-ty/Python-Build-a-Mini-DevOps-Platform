# Task 123: Build a logging decorator that records function calls and results.

import time
from typing import Callable, Any
def log_calls(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
