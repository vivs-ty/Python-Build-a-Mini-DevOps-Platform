# Task 177: Upload a file to cloud storage, or simulate cloud storage locally.

import os
import shutil

def upload_to_cloud_storage(file_path, destination):
    """Upload a file to cloud storage (simulated locally).
    
    Args:
        file_path: Path to the source file to upload
        destination: Destination directory for the file
        
    Returns:
        True if successful, False otherwise
    """
    if not os.path.exists(file_path):
        print(f"Error: Source file '{file_path}' does not exist.")
        return False

    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination, file_name)
        
        # shutil.copy2 handles both text and binary files securely
        shutil.copy2(file_path, destination_path)
        
        print(f"File '{file_path}' successfully uploaded to simulated cloud '{destination_path}'.")
        return True
    except OSError as e:
        print(f"Error uploading file: {e}")
        return False

if __name__ == "__main__":
    # Create a dummy file to test the upload
    if not os.path.exists("example_file.txt"):
        with open("example_file.txt", "w") as f:
            f.write("Dummy content")

    upload_to_cloud_storage("example_file.txt", "cloud_storage_simulation")
    
    print(" \n Python 30 days Series - Day 25 : Task 177 \n")
    print(" \n Day 25: Kubernetes Operations and Cloud Basics \n")
    print(" \n Have a good one! " + "-"*40)
