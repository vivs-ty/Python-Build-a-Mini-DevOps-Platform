# Task 66: Read a specific environment variable and handle missing values.

import os

def get_config_value(key: str, default_value: str = "Unset") -> str:
    # os.getenv safely returns None (or a specified default) if the key isn't found
    value = os.getenv(key, default_value)
    
    if value == default_value:
        print(f" Warning: Environment variable '{key}' not found. Using default.")
    else:
        print(f" Found '{key}'.")
        
    return value

# --- Demonstration ---
# 1. Reading an existing, standard system variable
user = get_config_value("USER", "UnknownUser") # 'USER' works on Linux/Mac. Windows uses 'USERNAME'
if user == "UnknownUser":
    user = get_config_value("USERNAME", "UnknownUser")
print(f"Current User: {user}")

# 2. Reading a missing variable
api_key = get_config_value("DATABASE_URL", "sqlite:///local.db")
print(f"Database URL: {api_key}")

print(" \n Python 30 days Series - Day 10 Task 66 \n"                                              )
print(" \n Day 10: OS Interaction and Environment \n"                                              )
print(" \n Have a good one! \n "                          + "-"*40)
