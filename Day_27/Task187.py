# Task 187: Fetch logs from a pipeline execution.

# Simulate fetching logs from a pipeline execution
def fetch_pipeline_logs(pipeline_id):
    # Simulated logs for the pipeline execution
    logs = [
        "Step 1: Cloning repository...",
        "Step 2: Installing dependencies...",
        "Step 3: Running tests...",
        "Step 4: Building application...",
        "Step 5: Deploying application...",
        "Pipeline execution completed successfully."
    ]
    print(f"Logs for pipeline {pipeline_id}:")
    for log in logs:
        print(log)
        