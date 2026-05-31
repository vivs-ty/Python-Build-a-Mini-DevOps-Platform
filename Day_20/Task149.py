# Task 149: Switch branches based on user input.

import subprocess

def switch_branch():
    branch_name = input("Enter the branch name to switch to: ").strip()
    
    result = subprocess.run(["git", "checkout", branch_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Switched to branch: {branch_name}")
    else:
        print(f"Failed to switch branch. Error: {result.stderr}")

if __name__ == "__main__":
    switch_branch()

print(" \n Python 30 days Series - Day 20 Task 149 \n"                                               )
print(" \n Day 20 : SSH Automation \n"                               )
print(" \n Have a good one! \n "                          + "-"*40)
