# Task 146: Detect repository changes and commit them automatically.

import subprocess

def auto_commit(commit_message="Automatic commit"):
    # Check if there are any changes
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    
    if not status.stdout.strip():
        print("No changes to commit.")
        return

    # Add all files
    subprocess.run(["git", "add", "."])
    
    # Commit files
    result = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Changes committed successfully.")
    else:
        print(f"Error committing changes: {result.stderr}")

if __name__ == "__main__":
    auto_commit()

print(f" \n Python 30 days Series - Day 20 Task 146 \n")
print(f" \n Day 20 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)
