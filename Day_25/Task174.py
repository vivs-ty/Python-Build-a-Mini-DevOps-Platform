# Task 174: Deploy an application to Kubernetes from a YAML file.

import subprocess

def deploy_application(yaml_file):
    try:
        result = subprocess.run(
            ["kubectl", "apply", "-f", yaml_file],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Application deployed successfully:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying application from '{yaml_file}': {e.stderr}")

if __name__ == "__main__":
    # Ensure you have a valid YAML file for deployment before executing
    deploy_application("deployment.yaml")
    
    print("\nPython 30 days Series - Day 25 : Task 174")
    print("Day 25 : Kubernetes and Cloud Storage")
    print("Have a good one!\n" + "-"*40)
    