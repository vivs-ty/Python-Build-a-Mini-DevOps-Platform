# Task 125: Create a caching decorator for expensive function calls.

from functools import wraps
from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache_dict = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # A tuple of (args, frozenset(kwargs)) creates a perfectly hashable, strict key
        key = (args, frozenset(kwargs.items()))
        
        if key in cache_dict:
            print(f"⚡ Cache HIT for {func.__name__}")
            return cache_dict[key]
            
        print(f"⏳ Cache MISS for {func.__name__}. Computing...")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
        
    return wrapper

# --- Demonstration ---
@cache
def expensive_calculation(x: int, y: int) -> int:
    import time
    time.sleep(1) # Simulate heavy work
    return x + y

print(expensive_calculation(5, 10)) # Takes 1 second
print(expensive_calculation(5, 10)) # Returns instantly!

print(" \n Python 30 days Series - Day 17 Task 125 \n"                                               )
print(" \n Day 17 : Decorators \n"                           )
print(" \n Have a good one! \n "                          + "-"*40)
