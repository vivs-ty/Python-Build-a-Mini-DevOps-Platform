# Task 122: Create a retry decorator with a delay between retries.

import time
from typing import Callable, Any

def retry(delay: float = 1.0, max_retries: int = 3):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error occurred: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise Exception("Function failed after maximum retries.")
        return wrapper
    return decorator
