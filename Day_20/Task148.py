# Task 148: Print the status of a Git repository.

import subprocess

def print_git_status():
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error getting status: {result.stderr}")

if __name__ == "__main__":
    print_git_status()
    
print(f" \n Python 30 days Series - Day 20 Task 148 \n")
print(f" \n Day 20 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)
