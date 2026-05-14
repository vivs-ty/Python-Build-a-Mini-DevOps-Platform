# Task 126: Limit how many times a function can be called in a time window.

import time
from functools import wraps
from typing import Callable, Any

def rate_limit(calls: int, period: float):
    def decorator(func: Callable) -> Callable:
        call_times = []
        
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.perf_counter()
            
            # Remove timestamps that fall outside the sliding window
            while call_times and call_times[0] < now - period:
                call_times.pop(0)
                
            if len(call_times) >= calls:
                raise PermissionError(f"Rate limit exceeded: Max {calls} calls per {period}s.")
                
            call_times.append(now)
            return func(*args, **kwargs)
            
        return wrapper
    return decorator

# --- Demonstration ---
@rate_limit(calls=3, period=2.0)
def api_request():
    return "Data fetched!"

for i in range(4):
    try:
        print(f"Call {i+1}: {api_request()}")
    except PermissionError as e:
        print(f"Call {i+1} Blocked: {e}")

print(f" \n Python 30 days Series - Day 17 Task 126 \n")
print(f" \n Day 17 : Decorators \n")
print(f" \n Have a good one! \n " + "-"*40)