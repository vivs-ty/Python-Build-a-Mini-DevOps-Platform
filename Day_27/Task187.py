# Task 187: Fetch logs from a pipeline execution.
#
# Required dependencies: pip install requests

import requests
import os

def fetch_pipeline_logs(owner, repo, run_id, token, output_dir='.'):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/logs"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print(f"Fetching logs for pipeline run ID: {run_id}...")
    
    try:
        # allow_redirects=True is required because GitHub redirects the request to an AWS S3 download link
        response = requests.get(url, headers=headers, allow_redirects=True, timeout=30)
        
        if response.status_code == 200:
            log_filename = os.path.join(output_dir, f"pipeline_logs_{run_id}.zip")
            
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            try:
                with open(log_filename, "wb") as f:
                    f.write(response.content)
                print(f"Logs successfully downloaded and saved as '{log_filename}'.")
            except IOError as io_error:
                print(f"Error writing to file '{log_filename}': {io_error}")
        else:
            print(f"Failed to fetch logs. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.Timeout:
        print("Error: Request timed out while fetching pipeline logs.")
    except requests.RequestException as e:
        print(f"Error: Failed to fetch logs: {e}")

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
        fetch_pipeline_logs(owner, repo, run_id, token)
    
    print(" \n Python 30 days Series - Day 27 : Task 187 \n")
    print(" \n Day 27: Cloud Tagging and CI/CD Basics \n")
    print(" \n Have a good one! " + "-"*40)
    