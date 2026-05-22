# Task 168: Build a Docker deployment automation tool that builds an image and deploys a container.

import subprocess

def build_docker_image(image_name, dockerfile_path):
    try:
        result = subprocess.run(
            ["docker", "build", "-t", image_name, dockerfile_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Image '{image_name}' built successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error building image '{image_name}': {e.stderr}")

if __name__ == "__main__":
    build_docker_image("my_nginx_image", ".")
    
    print("\nPython 30 days Series - Day 24 : Task 168")
    print("Day 24 : Deployment and Kubernetes Basics")
    print("Have a good one!\n" + "-"*40)
    