# Task 168: Build a Docker deployment automation tool that builds an image and deploys a container.

import subprocess

def build_docker_image(image_name, dockerfile_path):
    """Build a Docker image.
    
    Args:
        image_name: Name of the image to build (e.g., 'my_nginx_image')
        dockerfile_path: Path to the directory containing the Dockerfile
        
    Returns:
        True if successful, False otherwise
    """
    try:
        result = subprocess.run(
            ["docker", "build", "-t", image_name, dockerfile_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Image '{image_name}' built successfully.")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error building image '{image_name}': {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: Docker is not installed or not added to your system PATH.")
        return False

if __name__ == "__main__":
    build_docker_image("my_nginx_image", ".")
    
    print(" \n Python 30 days Series - Day 24 : Task 168 \n")
    print(" \n Day 24: Deployment and Kubernetes Basics \n")
    print(" \n Have a good one! " + "-"*40)
    