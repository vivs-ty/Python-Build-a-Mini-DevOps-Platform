# Task 192: Send notifications when a pipeline succeeds or fails.

import time

def send_notification(status):
    print(f"Sending notification: Pipeline {status}...")
    time.sleep(2)
    print("Notification sent successfully.")
def run_pipeline():
    print("Running pipeline...")
    time.sleep(2)
    # Simulate a pipeline failure
    return False
def deploy_code():
    print("Deploying code...")
    time.sleep(2)
    print("Code deployed successfully.")
if __name__ == "__main__":
    deploy_code()
    if not run_pipeline():
        send_notification("failed")
        print("Pipeline execution completed with errors.")
    else:
        send_notification("succeeded")
        print("Pipeline executed successfully.")
        