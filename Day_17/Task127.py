# Task 127: Validate function arguments with a decorator.

import time
from typing import Callable, Any
def validate_args(validator: Callable[[Any], bool]):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            if not validator(*args, **kwargs):
                raise ValueError("Invalid arguments provided.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
