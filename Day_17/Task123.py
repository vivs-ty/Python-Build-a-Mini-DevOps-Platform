# Task 123: Build a logging decorator that records function calls and results.

import logging
from functools import wraps
from typing import Callable, Any

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")

def log_calls(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # repr() safely limits output for massive objects
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        logging.debug(f"Calling -> {func.__name__}({signature})")
        
        try:
            result = func(*args, **kwargs)
            logging.debug(f"Result  <- {func.__name__} returned {repr(result)}")
            return result
        except Exception as e:
            logging.error(f"Error   <- {func.__name__} raised {type(e).__name__}: {e}")
            raise
    return wrapper

# --- Demonstration ---
@log_calls
def calculate_discount(price: float, discount: float = 0.1) -> float:
    return price * (1 - discount)

calculate_discount(100.0, discount=0.2)

print(" \n Python 30 days Series - Day 17 Task 123 \n"                                               )
print(" \n Day 17 : Decorators \n"                           )
print(" \n Have a good one! \n "                          + "-"*40)
