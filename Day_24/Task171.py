# Task 171: Scale a deployment up or down based on user input.

import subprocess

def scale_deployment():
    deployment_name = input("Enter the deployment name to scale: ").strip()
    replicas = input(f"Enter the desired number of replicas for '{deployment_name}': ").strip()
    
    if not replicas.isdigit():
        print("Error: Replicas must be a valid number.")
        return

    try:
        result = subprocess.run(
            ["kubectl", "scale", "deployment", deployment_name, f"--replicas={replicas}"],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Deployment '{deployment_name}' scaled to {replicas} replicas successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error scaling deployment '{deployment_name}': {e.stderr}")

if __name__ == "__main__":
    scale_deployment()
    
    print("\nPython 30 days Series - Day 24 : Task 171")
    print("Day 24 : Deployment and Kubernetes Basics")
    print("Have a good one!\n" + "-"*40)
    