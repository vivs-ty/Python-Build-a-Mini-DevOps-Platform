# Task 169: Retrieve and display the status of all Kubernetes pods.

import subprocess

def get_pod_status():
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Pod Status:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr if e.stderr else "Unknown error"
        print(f"Error retrieving pod status: {stderr}")
    except FileNotFoundError:
        print("Error: kubectl is not installed or not in your system PATH.")

if __name__ == "__main__":
    get_pod_status()
    
    print(" \n Python 30 days Series - Day 24 : Task 169 \n")
    print(" \n Day 24: Deployment and Kubernetes Basics \n")
    print(" \n Have a good one! " + "-"*40)
    