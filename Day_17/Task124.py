# Task 124: Add an authorization decorator for role-based access checks.

from functools import wraps
from typing import Callable, Any
from dataclasses import dataclass

@dataclass
class User:
    username: str
    role: str

def authorize(allowed_roles: list[str]):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Safely look for 'user' in kwargs, then args
            user = kwargs.get('user')
            if not user and args:
                user = args[0] if isinstance(args[0], User) else None
                
            if not isinstance(user, User):
                raise TypeError("A valid User object must be provided to this function.")
                
            if user.role not in allowed_roles:
                raise PermissionError(f"Access denied for role: '{user.role}'")
                
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Demonstration ---
@authorize(allowed_roles=["Admin", "SuperUser"])
def delete_database(user: User):
    return " Database deleted successfully."

admin_user = User("alice", "Admin")
guest_user = User("bob", "Guest")

print(delete_database(user=admin_user)) # Succeeds

try:
    print(delete_database(user=guest_user)) # Fails
except PermissionError as e:
    print(f" Caught Error: {e}")

print(f" \n Python 30 days Series - Day 17 Task 124 \n")
print(f" \n Day 17 : Decorators \n")
print(f" \n Have a good one! \n " + "-"*40)
