# Task 174: Deploy an application to Kubernetes from a YAML file.

import subprocess
import os
import yaml

def deploy_application(yaml_file):
    """Deploy an application to Kubernetes from a YAML file.
    
    Args:
        yaml_file: Path to the Kubernetes manifest YAML file
    """
    if not os.path.exists(yaml_file):
        print(f"Error: The file '{yaml_file}' does not exist.")
        return False

    # Validate YAML file format
    try:
        with open(yaml_file, 'r') as f:
            yaml_content = yaml.safe_load(f)
        if not yaml_content:
            print(f"Error: YAML file '{yaml_file}' is empty or invalid.")
            return False
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML format in '{yaml_file}': {e}")
        return False
    except IOError as e:
        print(f"Error reading file '{yaml_file}': {e}")
        return False

    try:
        result = subprocess.run(
            ["kubectl", "apply", "-f", yaml_file],
            check=True,
            capture_output=True,
            text=True
        )
        print("Application deployed successfully:\n")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error deploying application from '{yaml_file}': {e.stderr}")
        return False

if __name__ == "__main__":
    # Ensure you have a valid YAML file before executing
    deploy_application("deployment.yaml")
    
    print(" \n Python 30 days Series - Day 25 : Task 174 \n")
    print(" \n Day 25: Kubernetes Operations and Cloud Basics \n")
    print(" \n Have a good one! " + "-"*40)
    