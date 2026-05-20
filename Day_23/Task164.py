# Task 164: Pull a Docker image and run it with specified parameters.

import docker
from docker.errors import DockerException

def pull_and_run_docker_image(image_name, container_name, ports=None):
    try:
        client = docker.from_env()
        
        # Pull the Docker image
        print(f"Pulling Docker image: {image_name}")
        client.images.pull(image_name)
        print(f"Successfully pulled image: {image_name}")
        
        # Run the Docker container
        print(f"Running container: {container_name} from image: {image_name}")
        container = client.containers.run(
            image_name,
            name=container_name,
            ports=ports,
            detach=True
        )
        
        print(f"Container '{container_name}' is running successfully with ID: {container.id}")
            
    except DockerException as e:
        print(f"An error occurred while interacting with Docker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    image_name = "nginx:latest"
    container_name = "my_nginx_container"
    # In the docker library, port mapping is {'container_port/tcp': host_port}
    ports_mapping = {'80/tcp': 8080} 
    
    pull_and_run_docker_image(image_name, container_name, ports_mapping)
    
    print("\nPython 30 days Series - Day 23 : Task 164")
    print("Day 23 : Docker Automation")
    print("Have a good one!\n" + "-"*40)
    