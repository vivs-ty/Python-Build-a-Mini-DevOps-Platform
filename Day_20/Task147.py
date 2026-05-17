# Task 147: Push local changes to a remote repository.

import subprocess

def push_changes(remote="origin", branch="main"):
    print(f"Pushing to {remote} {branch}...")
    result = subprocess.run(["git", "push", remote, branch], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Push successful.")
    else:
        print(f"Push failed: {result.stderr}")

print(f" \n Python 30 days Series - Day 20 Task 147 \n")
print(f" \n Day 20 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)
