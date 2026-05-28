# Task 190: Build a CI automation tool that performs code pull, test execution, and deployment.

import time

def pull_code():
    print("Pulling code from version control...")
    time.sleep(2)
    print("Code pulled successfully.")
def run_tests():
    print("Running tests...")
    time.sleep(2)
    # Simulate test execution
    return True

def deploy_code():
    print("Deploying code...")
    time.sleep(2)
    print("Code deployed successfully.")
def run_pipeline():
    pull_code()
    if run_tests():
        deploy_code()
    else:
        print("Tests failed. Deployment aborted.")
# Example usage
if __name__ == "__main__":
    run_pipeline()
    