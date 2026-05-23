# Task 174: Deploy an application to Kubernetes from a YAML file.

import subprocess
import os

def deploy_application(yaml_file):
    if not os.path.exists(yaml_file):
        print(f"Error: The file '{yaml_file}' does not exist.")
        return

    try:
        result = subprocess.run(
            ["kubectl", "apply", "-f", yaml_file],
            check=True,
            capture_output=True,
            text=True
        )
        print("Application deployed successfully:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error deploying application from '{yaml_file}': {e.stderr}")

if __name__ == "__main__":
    # Ensure you have a valid YAML file before executing
    deploy_application("deployment.yaml")
    
    print("\nPython 30 days Series - Day 25 : Task 174")
    print("Day 25 : Kubernetes Operations and Cloud Basics")
    print("Have a good one!\n" + "-"*40)
    