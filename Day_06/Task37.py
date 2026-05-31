# Task 37: Divide two numbers and handle invalid input and division by zero.

import logging

# Configure basic logging (standard practice for production code)
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        return None
    except TypeError:
        logging.error(f"Invalid input types: {type(a).__name__} and {type(b).__name__}")
        return None

print(f"Valid Division (10 / 2): {safe_divide(10, 2)}")
print(f"Zero Division (10 / 0): {safe_divide(10, 0)}")    # Safely logs the error
print(f"Type Error Division (10 / 'a'): {safe_divide(10, 'a')}")
print(" \n Python 30 days Series - Day 6 Task 37 \n"                                             )
print(" \n Day 6: Functions and Error Handling \n"                                           )
print(" \n Have a good one! \n "                          + "-"*40)
