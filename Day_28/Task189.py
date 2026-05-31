# Task 189: Validate code before triggering a pipeline by simulating lint and test checks.

import subprocess

def run_linter():
    print("Step 1: Running code linter...")
    # Using Python's built-in syntax checker to simulate a linter
    result = subprocess.run(["python", "-m", "py_compile", __file__], capture_output=True)
    if result.returncode == 0:
        print("Linting passed. No syntax errors.")
        return True
    else:
        print("Linting failed.")
        return False

def run_tests():
    print("Step 2: Running unit tests...")
    # Simulating a passing test suite
    print("All 45 tests passed successfully.")
    return True

def validate_and_trigger():
    print("Starting pre-pipeline validation...")
    
    if run_linter() and run_tests():
        print("Validation complete. Triggering the main CI/CD pipeline...")
    else:
        print("Validation failed. Pipeline trigger aborted to prevent broken builds.")

if __name__ == "__main__":
    validate_and_trigger()
    
    print("\nPython 30 days Series - Day 28 : Task 189")
    print("Day 28 : CI/CD Automation")
    print("Have a good one!\n" + "-"*40)
    