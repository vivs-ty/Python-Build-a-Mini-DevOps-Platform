# Task 152: Simulate a simple workflow such as commit, test, and push.

import subprocess

def run_tests():
    print("Running tests...")
    # Simulate a test runner like pytest or unittest
    # For a real project, replace this with ["pytest"] or ["python", "manage.py", "test"]
    result = subprocess.run(["python", "-m", "unittest", "discover"], capture_output=True, text=True)
    return result.returncode == 0

def automated_workflow():
    print("Starting automated workflow...")
    
    # Step 1: Add and Commit
    subprocess.run(["git", "add", "."])
    commit_result = subprocess.run(["git", "commit", "-m", "Automated workflow commit"], capture_output=True, text=True)
    
    if commit_result.returncode != 0 and "nothing to commit" not in commit_result.stdout:
        print("Commit failed. Check repository status.")
        return
        
    print("Code committed.")
    
    # Step 2: Test
    if not run_tests():
        print("Tests failed. Workflow aborted. Code will not be pushed.")
        return
        
    print("Tests passed.")
    
    # Step 3: Push
    print("Pushing to remote...")
    push_result = subprocess.run(["git", "push"], capture_output=True, text=True)
    
    if push_result.returncode == 0:
        print("Workflow complete. Code pushed successfully.")
    else:
        print(f"Push failed: {push_result.stderr}")

if __name__ == "__main__":
    automated_workflow()

print(" \n Python 30 days Series - Day 20 Task 152 \n"                                               )
print(" \n Day 20 : SSH Automation \n"                               )
print(" \n Have a good one! \n "                          + "-"*40)