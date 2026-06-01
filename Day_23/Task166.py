# Task 166: Read a config file and start multiple containers from it.
#
# Required dependencies: pip install docker pyyaml

import docker
import yaml
from docker.errors import DockerException

def start_containers_from_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        
        client = docker.from_env()
        
        for container_config in config.get('containers', []):
            image = container_config.get('image')
            name = container_config.get('name')
            ports = container_config.get('ports', {})
            environment = container_config.get('environment', {})
            
            print(f"Starting container: {name} from image: {image}")
            client.containers.run(
                image, 
                name=name, 
                ports=ports, 
                environment=environment, 
                detach=True
            )
        
        print("All containers started successfully.")
        
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML config: {e}")
    except DockerException as e:
        print(f"An error occurred while interacting with Docker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure you create a config.yaml file before running this
    start_containers_from_config("config.yaml")
    
    print(" \n Python 30 days Series - Day 23 : Task 166 \n")
    print(" \n Day 23: Docker Automation \n")
    print(" \n Have a good one! " + "-"*40)
    