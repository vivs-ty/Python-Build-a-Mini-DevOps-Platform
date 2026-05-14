# Task 124: Add an authorization decorator for role-based access checks.
from typing import Callable, Any

def authorize(allowed_roles: list):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            # Assuming the user object is passed as the first argument
            user = args[0] if args else None
            if not user:
                raise ValueError("User not found.")
            if user.role not in allowed_roles:
                raise PermissionError("Insufficient permissions.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
