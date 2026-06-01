# Task 163: Remove stopped containers and unused images.
# 
# Required dependencies: pip install docker

import docker
from docker.errors import DockerException

def cleanup_docker_resources():
    try:
        client = docker.from_env()
        
        # Remove stopped containers
        stopped_containers = client.containers.list(all=True, filters={"status": "exited"})
        for container in stopped_containers:
            print(f"Removing stopped container: {container.name} ({container.id})")
            container.remove()
        
        # Remove unused images (dangling)
        unused_images = client.images.list(filters={"dangling": True})
        for image in unused_images:
            print(f"Removing unused image: {image.tags} ({image.id})")
            client.images.remove(image.id)
        
        print("Cleanup completed successfully.")
        
    except DockerException as e:
        print(f"An error occurred while interacting with Docker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    cleanup_docker_resources()
    
    print(" \n Python 30 days Series - Day 23 : Task 163 \n")
    print(" \n Day 23: Docker Automation \n")
    print(" \n Have a good one! " + "-"*40)
    