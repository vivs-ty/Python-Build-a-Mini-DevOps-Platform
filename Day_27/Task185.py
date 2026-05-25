# Task 185: Trigger a CI/CD pipeline by API call.

import requests

# Simulate triggering a CI/CD pipeline via API
def trigger_pipeline(pipeline_url, payload):
    try:
        response = requests.post(pipeline_url, json=payload)
        if response.status_code == 200:
            print("Pipeline triggered successfully.")
        else:
            print(f"Failed to trigger pipeline. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        