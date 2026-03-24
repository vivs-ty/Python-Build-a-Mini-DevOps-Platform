# Task 1: Write a Python script that prints a welcome message for a DevOps engineer and includes the current date and time.

from datetime import datetime, timezone

name = input("What is your Name ? ").strip()
curr = datetime.now(timezone.utc)
utc_time = curr.strftime("%B %d %Y - %H:%M:%S")

print(f" Hello {name}, Glad to see you here! ")
print(f" \n Welcome to the World of DevOps Engineers! \n")
print(f" \n Python 30 days Series - Day 1 Task 1 \n")
print(f" Current date and time in UTC is : {utc_time}, \n Have a good one! ")
