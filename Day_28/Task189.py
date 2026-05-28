# Task 189: Validate code before triggering a pipeline by simulating lint and test checks.

import time

def run_pipeline():
    print("Running pipeline...")
    time.sleep(2)
    # Simulate a pipeline failure
    return False

def rollback_deployment():
    print("Rolling back deployment...")
    time.sleep(2)
    print("Deployment rolled back successfully.")

def deploy_code():
    print("Deploying code...")
    time.sleep(2)
    print("Code deployed successfully.")


def pull_code():
    print("Pulling code from version control...")
    time.sleep(2)
    print("Code pulled successfully.")

def validate_code():
    print("Validating code...")
    time.sleep(2)
    # Simulate lint and test checks
    return True

if validate_code():
    pull_code()
    deploy_code()
    if not run_pipeline():
        rollback_deployment()
        