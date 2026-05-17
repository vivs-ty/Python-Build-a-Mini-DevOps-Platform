# Task 150: Pull the latest changes and handle merge conflicts gracefully.

import subprocess

def pull_with_conflict_handling(remote="origin", branch="main"):
    print(f"Pulling latest changes from {remote}/{branch}...")
    result = subprocess.run(["git", "pull", remote, branch], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Pull successful.")
    else:
        print("Pull failed. A merge conflict or network issue occurred.")
        print("Aborting the merge to keep local files safe...")
        
        # Abort the merge to return to a clean state
        subprocess.run(["git", "merge", "--abort"])
        print("Merge aborted. Please resolve the issue manually.")

if __name__ == "__main__":
    pull_with_conflict_handling()

print(f" \n Python 30 days Series - Day 20 Task 150 \n")
print(f" \n Day 20 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)