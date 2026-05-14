# Task 121: Write a decorator that measures function execution time.
import time
from typing import Callable, Any

def measure_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to execute.")
        return result
    return wrapper
