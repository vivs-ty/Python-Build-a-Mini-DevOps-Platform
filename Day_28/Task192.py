# Task 192: Send notifications when a pipeline succeeds or fails.

import time
import requests

def send_webhook_notification(webhook_url, status, pipeline_name):
    if status.upper() == "SUCCESS":
        color = "GREEN"
        message = f"Pipeline '{pipeline_name}' completed successfully."
    else:
        color = "RED"
        message = f"Pipeline '{pipeline_name}' FAILED. Immediate attention required."
        
    payload = {
        "text": message,
        "status": status,
        "color": color
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print(f"Notification sent: [{status}] {message}")
        else:
            print(f"Failed to send notification. HTTP Status: {response.status_code}")
    except Exception as e:
        print(f"Network error while sending notification: {e}")

def run_mock_pipeline():
    # Using httpbin.org to safely simulate a webhook endpoint
    mock_webhook_url = "https://httpbin.org/post"
    pipeline_name = "Backend-API-Deploy"
    
    print("Running pipeline...")
    # Simulate a pipeline failure
    pipeline_success = False 
    
    if pipeline_success:
        send_webhook_notification(mock_webhook_url, "SUCCESS", pipeline_name)
    else:
        send_webhook_notification(mock_webhook_url, "FAILURE", pipeline_name)

if __name__ == "__main__":
    run_mock_pipeline()
    
    print("\nPython 30 days Series - Day 28 : Task 192")
    print("Day 28 : CI/CD Automation")
    print("Have a good one!\n" + "-"*40)
    