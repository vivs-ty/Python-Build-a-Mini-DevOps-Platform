# Task 186: Check the status of a running pipeline and print progress updates.

import time

# Simulate checking pipeline status
def check_pipeline_status(pipeline_id):
    # Simulated pipeline statuses
    statuses = ["queued", "running", "success", "failed"]
    for status in statuses:
        print(f"Pipeline {pipeline_id} status: {status}")
        time.sleep(1)  # Simulate time delay for status updates
# Example usage
check_pipeline_status("pipeline-123")
print("Pipeline execution completed.")
