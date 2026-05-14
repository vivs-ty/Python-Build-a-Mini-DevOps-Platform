# Task 125: Create a caching decorator for expensive function calls.
from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache_dict = {}
    def wrapper(*args, **kwargs) -> Any:
        key = str(args) + str(sorted(kwargs.items()))
        if key in cache_dict:
            print(f"Retrieving {func.__name__} result from cache.")
            return cache_dict[key]
        result = func(*args, **kwargs)
        cache_dict[key] = result
        print(f"Caching {func.__name__} result.")
        return result
    return wrapper
