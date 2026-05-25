# Task 185: Trigger a CI/CD pipeline by API call.

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
    
    print(f"Triggering pipeline for {owner}/{repo} on branch '{branch}'...")
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 204:
        print("Pipeline triggered successfully.")
    else:
        print(f"Failed to trigger pipeline. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    # Replace these variables with your actual GitHub details and Personal Access Token (PAT)
    trigger_github_pipeline("your_username", "your_repository", "main.yml", "your_personal_access_token")
    
    print("\nPython 30 days Series - Day 27 : Task 185")
    print("Day 27 : Cloud Tagging and CI/CD Basics")
    print("Have a good one!\n" + "-"*40)
    