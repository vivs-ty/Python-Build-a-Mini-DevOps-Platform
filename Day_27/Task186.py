# Task 186: Check the status of a running pipeline and print progress updates.
#
# Required dependencies: pip install requests

import requests
import time

def monitor_pipeline_status(owner, repo, run_id, token, poll_interval=10, max_checks=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print(f"Monitoring pipeline run ID: {run_id}...")
    
    # Use a counter for real monitoring, or set max_checks for testing
    check_count = 0
    max_checks = max_checks or float('inf')
    
    try:
        while check_count < max_checks:
            check_count += 1
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                status = data.get("status")
                conclusion = data.get("conclusion")
                
                print(f"Check {check_count}: Status: {status} | Conclusion: {conclusion or 'Running...'}")
                
                if status == "completed":
                    print(f"Pipeline finished with conclusion: {conclusion}")
                    break
            else:
                print(f"Failed to fetch status: {response.status_code} - {response.text}")
                break
                
            time.sleep(poll_interval)
    except requests.Timeout:
        print("Error: Request timed out while monitoring pipeline status.")
    except requests.RequestException as e:
        print(f"Error: Failed to monitor pipeline: {e}")

if __name__ == "__main__":
    owner = "your_username"
    repo = "your_repository"
    run_id = "123456789"
    token = "your_personal_access_token"
    
    if token == "your_personal_access_token":
        print("Please set your GitHub credentials and run ID:")
        print(f"  owner = '{owner}'")
        print(f"  repo = '{repo}'")
        print(f"  run_id = '{run_id}'")
        print(f"  token = 'your_personal_access_token'")
    else:
        monitor_pipeline_status(owner, repo, run_id, token, poll_interval=5, max_checks=5)
    
    print(" \n Python 30 days Series - Day 27 : Task 186 \n")
    print(" \n Day 27: Cloud Tagging and CI/CD Basics \n")
    print(" \n Have a good one! " + "-"*40)
    