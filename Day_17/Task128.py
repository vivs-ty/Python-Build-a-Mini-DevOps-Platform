# Task 128: Combine multiple decorators and show their execution order.

from functools import wraps

# Mock decorators for demonstration
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("1. [Authenticate] Checking user credentials...")
        return func(*args, **kwargs)
    return wrapper

def validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("2. [Validate] Checking payload format...")
        return func(*args, **kwargs)
    return wrapper

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("3. [Log Action] Logging request to database...")
        result = func(*args, **kwargs)
        print("4. [Log Action] Request completed.")
        return result
    return wrapper

# --- Demonstration ---
# Python executes these strictly from BOTTOM to TOP during creation, 
# meaning execution flows from TOP to BOTTOM when called.
@authenticate
@validate
@log_action
def process_payment(amount: int):
    print(f"   -> [Execution] Processing ${amount} payment...")
    return True

print("Starting process:\n")
process_payment(500)

print(f" \n Python 30 days Series - Day 17 Task 128 \n")
print(f" \n Day 17 : Decorators \n")
print(f" \n Have a good one! \n " + "-"*40)