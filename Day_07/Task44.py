# Task 44: Append user activity logs with timestamps to a file.

import os
from datetime import datetime

log_file = 'user_activity.log'

with open(log_file, 'a') as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_action = input("Enter the user action: ")
    file.write(f"[{timestamp}] {user_action}\n")
    