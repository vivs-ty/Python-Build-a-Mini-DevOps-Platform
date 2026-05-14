# Task 122: Create a retry decorator with a delay between retries.

import time
import logging
from functools import wraps
from typing import Callable, Any

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def retry(delay: float = 1.0, max_retries: int = 3):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.warning(f"Attempt {attempt}/{max_retries} failed for '{func.__name__}': {e}")
                    if attempt < max_retries:
                        logging.info(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        logging.error("Max retries reached. Aborting.")
                        raise # Re-raises the original exception natively
        return wrapper
    return decorator

# --- Demonstration ---
@retry(delay=0.5, max_retries=3)
def unstable_network_call():
    import random
    if random.random() < 0.7: # 70% chance to fail
        raise ConnectionError("Network timeout.")
    return " Data fetched successfully!"

try:
    print(unstable_network_call())
except ConnectionError:
    print(" Ultimate failure.")

print(f" \n Python 30 days Series - Day 17 Task 122 \n")
print(f" \n Day 17 : Decorators \n")
print(f" \n Have a good one! \n " + "-"*40)
