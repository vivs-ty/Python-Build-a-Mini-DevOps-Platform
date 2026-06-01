# Task 185: Trigger a CI/CD pipeline by API call.
#
# Required dependencies: pip install requests

import requests

def trigger_github_pipeline(owner, repo, workflow_id, token, branch="main"):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "ref": branch
    }
    
    try:
        print(f"Triggering pipeline for {owner}/{repo} on branch '{branch}'...")
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        if response.status_code == 204:
            print("Pipeline triggered successfully.")
        else:
            print(f"Failed to trigger pipeline. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.Timeout:
        print("Error: Request timed out while triggering the pipeline.")
    except requests.RequestException as e:
        print(f"Error: Failed to trigger pipeline: {e}")

if __name__ == "__main__":
    # Replace these variables with your actual GitHub details and Personal Access Token (PAT)
    owner = "your_username"
    repo = "your_repository"
    workflow_id = "main.yml"
    token = "your_personal_access_token"
    
    if token == "your_personal_access_token":
        print("Please set your GitHub credentials:")
        print(f"  owner = '{owner}'")
        print(f"  repo = '{repo}'")
        print(f"  token = 'your_personal_access_token'")
    else:
        trigger_github_pipeline(owner, repo, workflow_id, token)
    
    print(" \n Python 30 days Series - Day 27 : Task 185 \n")
    print(" \n Day 27: Cloud Tagging and CI/CD Basics \n")
    print(" \n Have a good one! " + "-"*40)
    