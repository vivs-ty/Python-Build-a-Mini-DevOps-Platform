# Task 177: Upload a file to cloud storage, or simulate cloud storage locally.

import os
import shutil

def upload_to_cloud_storage(file_path, destination):
    if not os.path.exists(file_path):
        print(f"Error: Source file '{file_path}' does not exist.")
        return

    # Simulating cloud storage upload by copying the file to a local directory
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        # shutil.copy2 handles both text and binary files securely
        shutil.copy2(file_path, destination)
        
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination, file_name)
        
        print(f"File '{file_path}' successfully uploaded to simulated cloud '{destination_path}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    # Create a dummy file to test the upload
    if not os.path.exists("example_file.txt"):
        with open("example_file.txt", "w") as f:
            f.write("Dummy content")

    upload_to_cloud_storage("example_file.txt", "cloud_storage_simulation")
    
    print("\nPython 30 days Series - Day 25 : Task 177")
    print("Day 25 : Kubernetes Operations and Cloud Basics")
    print("Have a good one!\n" + "-"*40)
