# Task 177: Upload a file to cloud storage, or simulate cloud storage locally.

import os

def upload_to_cloud_storage(file_path, destination):
    # Simulating cloud storage upload by copying the file to a local directory
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination, file_name)
        
        with open(file_path, 'r') as src_file:
            content = src_file.read()
        
        with open(destination_path, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"File '{file_path}' successfully uploaded to '{destination_path}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    # Ensure you have a valid file to upload before executing
    upload_to_cloud_storage("example_file.txt", "cloud_storage_simulation")
    
    print("\nPython 30 days Series - Day 25 : Task 177")
    print("Day 25 : Kubernetes and Cloud Storage")
    print("Have a good one!\n" + "-"*40)
    