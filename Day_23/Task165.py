# Task 165: Monitor running containers and report their status.

import docker
from docker.errors import DockerException

def monitor_containers():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        
        if not containers:
            print("No running containers found.")
            return
        
        print("Running Containers:")
        for container in containers:
            print(f"Name: {container.name}, ID: {container.id}, Status: {container.status}")
        
    except DockerException as e:
        print(f"An error occurred while interacting with Docker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    monitor_containers()
    
    print("\nPython 30 days Series - Day 23 : Task 165")
    print("Day 23 : Docker Automation")
    print("Have a good one!\n" + "-"*40)
    