# Task 128: Combine multiple decorators and show their execution order.

import time
from typing import Callable, Any
def combine_decorators(*decorators: Callable) -> Callable:
    def decorator(func: Callable) -> Callable:
        for dec in reversed(decorators):
            func = dec(func)
        return func
    return decorator
