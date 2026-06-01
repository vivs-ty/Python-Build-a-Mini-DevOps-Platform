# Task 171: Scale a deployment up or down based on user input.

import subprocess

def scale_deployment():
    deployment_name = input("Enter the deployment name to scale: ").strip()
    replicas = input(f"Enter the desired number of replicas for '{deployment_name}': ").strip()
    
    try:
        # Validate that replicas is a positive integer
        replica_count = int(replicas)
        if replica_count < 0:
            print("Error: Replicas must be a non-negative number.")
            return
    except ValueError:
        print("Error: Replicas must be a valid integer.")
        return

    try:
        result = subprocess.run(
            ["kubectl", "scale", "deployment", deployment_name, f"--replicas={replica_count}"],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Deployment '{deployment_name}' scaled to {replica_count} replicas successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error scaling deployment '{deployment_name}': {e.stderr}")

if __name__ == "__main__":
    scale_deployment()
    
    print(" \n Python 30 days Series - Day 24 : Task 171 \n")
    print(" \n Day 24: Deployment and Kubernetes Basics \n")
    print(" \n Have a good one! " + "-"*40)
    