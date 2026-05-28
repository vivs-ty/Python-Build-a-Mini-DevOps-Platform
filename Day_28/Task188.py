# Task 188: Roll back a deployment automatically when a pipeline fails.

import time

def rollback_deployment():
    print("Rolling back deployment...")
    time.sleep(2)
    print("Deployment rolled back successfully.")
def run_pipeline():
    print("Running pipeline...")
    time.sleep(2)
    # Simulate a pipeline failure
    return False

# Example usage
if not run_pipeline():
    rollback_deployment()
    print("Pipeline execution completed.")
    
