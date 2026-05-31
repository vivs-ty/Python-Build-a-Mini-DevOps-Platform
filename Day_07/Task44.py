# Task 44: Append user activity logs with timestamps to a file.

import logging

# Configures the logger to automatically add timestamps and append to the file
logging.basicConfig(
    filename='user_activity.log',
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

user_action = input("Enter the user action: ").strip()
if user_action:
    logging.info(user_action)
    print(" Action logged.")

print(" \n Python 30 days Series - Day 7 Task 44 \n"                                             )
print(" \n Day 7: File Handling \n"                            )
print(" \n Have a good one! \n "                          + "-"*40)
