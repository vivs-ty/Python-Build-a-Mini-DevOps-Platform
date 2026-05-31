# Task 121: Write a decorator that measures function execution time.

import time
from functools import wraps
from typing import Callable, Any

def measure_time(func: Callable) -> Callable:
    @wraps(func) # CRITICAL: Preserves the original function's identity
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ '{func.__name__}' executed in {end - start:.6f} seconds.")
        return result
    return wrapper

# --- Demonstration ---
@measure_time
def heavy_computation(n: int) -> int:
    """Calculates the sum of squares up to n."""
    return sum(i * i for i in range(n))

print(f"Result: {heavy_computation(10_000_000)}")
print(f"Function Name: {heavy_computation.__name__}") # Without @wraps, this would print 'wrapper'

print(" \n Python 30 days Series - Day 17 Task 121 \n"                                               )
print(" \n Day 17 : Decorators \n"                           )
print(" \n Have a good one! \n "                          + "-"*40)
