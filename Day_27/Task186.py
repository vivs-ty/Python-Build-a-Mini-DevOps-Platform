# Task 186: Check the status of a running pipeline and print progress updates.

import requests
import time

def monitor_pipeline_status(owner, repo, run_id, token, poll_interval=10):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print(f"Monitoring pipeline run ID: {run_id}...")
    
    # Loop 5 times for simulation. Use 'while True' for real monitoring.
    for _ in range(5):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            status = data.get("status")
            conclusion = data.get("conclusion")
            
            print(f"Status: {status} | Conclusion: {conclusion or 'Running...'}")
            
            if status == "completed":
                print(f"Pipeline finished with conclusion: {conclusion}")
                break
        else:
            print(f"Failed to fetch status: {response.status_code} - {response.text}")
            break
            
        time.sleep(poll_interval)

if __name__ == "__main__":
    monitor_pipeline_status("your_username", "your_repository", "123456789", "your_personal_access_token", poll_interval=5)
    
    print("\nPython 30 days Series - Day 27 : Task 186")
    print("Day 27 : Cloud Tagging and CI/CD Basics")
    print("Have a good one!\n" + "-"*40)
    