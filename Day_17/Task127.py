# Task 127: Validate function arguments with a decorator.

from functools import wraps
from typing import Callable, Any

def validate_args(validator_func: Callable[[tuple, dict], bool], error_msg: str):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if not validator_func(args, kwargs):
                raise ValueError(error_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Demonstration ---
# Validator checks that all positional args are integers greater than 0
def all_positive_ints(args: tuple, kwargs: dict) -> bool:
    return all(isinstance(a, int) and a > 0 for a in args)

@validate_args(all_positive_ints, error_msg="All inputs must be positive integers.")
def multiply(*numbers):
    import math
    return math.prod(numbers)

print(multiply(2, 4, 5)) # Succeeds

try:
    print(multiply(2, -4, 5)) # Fails validation
except ValueError as e:
    print(f" Validation Error: {e}")

print(" \n Python 30 days Series - Day 17 Task 127 \n"                                               )
print(" \n Day 17 : Decorators \n"                           )
print(" \n Have a good one! \n "                          + "-"*40)