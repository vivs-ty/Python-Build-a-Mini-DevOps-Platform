# Task 190: Build a CI automation tool that performs code pull, test execution, and deployment.

import time
import subprocess

def run_command(command, step_name):
    print(f"--- Running: {step_name} ---")
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Success.")
        return True
    else:
        # Ignore "not a git repository" errors for the sake of local testing
        if "not a git repository" in result.stderr:
            print("Skipped (Not a git repository).")
            return True
            
        print(f"Failed:\n{result.stderr}")
        return False

def run_ci_tool():
    print("Initializing CI Automation Tool...\n")
    
    # Step 1: Pull code
    if not run_command(["git", "pull"], "Source Code Pull"):
        return
        
    # Step 2: Run tests (Discover and run standard python unittests)
    if not run_command(["python", "-m", "unittest", "discover"], "Test Execution"):
        print("Pipeline halted due to test failure.")
        return
        
    # Step 3: Deploy (Simulated)
    if not run_command(["echo", "Deploying application to production server..."], "Deployment"):
        return
        
    print("\nCI Pipeline completed successfully.")

if __name__ == "__main__":
    run_ci_tool()
    
    print("\nPython 30 days Series - Day 28 : Task 190")
    print("Day 28 : CI/CD Automation")
    print("Have a good one!\n" + "-"*40)
    