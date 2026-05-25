# Task 187: Fetch logs from a pipeline execution.

import requests

def fetch_pipeline_logs(owner, repo, run_id, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/logs"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print(f"Fetching logs for pipeline run ID: {run_id}...")
    
    # allow_redirects=True is required because GitHub redirects the request to an AWS S3 download link
    response = requests.get(url, headers=headers, allow_redirects=True)
    
    if response.status_code == 200:
        log_filename = f"pipeline_logs_{run_id}.zip"
        with open(log_filename, "wb") as f:
            f.write(response.content)
        print(f"Logs successfully downloaded and saved as '{log_filename}'.")
    else:
        print(f"Failed to fetch logs. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    fetch_pipeline_logs("your_username", "your_repository", "123456789", "your_personal_access_token")
    
    print("\nPython 30 days Series - Day 27 : Task 187")
    print("Day 27 : Cloud Tagging and CI/CD Basics")
    print("Have a good one!\n" + "-"*40)
    