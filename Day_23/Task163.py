# Task 163: Remove stopped containers and unused images.

import docker from docker.errors import DockerException

def cleanup_docker_resources():
    try:
        client = docker.from_env()
        
        # Remove stopped containers
        stopped_containers = client.containers.list(all=True, filters={"status": "exited"})
        for container in stopped_containers:
            print(f"Removing stopped container: {container.name} ({container.id})")
            container.remove()
        
        # Remove unused images
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
    
    print("\nPython 30 days Series - Day 23 : Task 163")
    print("Day 23 : Docker Automation")
    print("Have a good one!\n" + "-"*40)