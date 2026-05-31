# Task 151: Tag a release version and push the tag.

import subprocess

def tag_and_push(version_tag):
    # Create the tag locally
    tag_result = subprocess.run(["git", "tag", version_tag], capture_output=True, text=True)
    
    if tag_result.returncode != 0:
        print(f"Failed to create tag: {tag_result.stderr}")
        return
        
    print(f"Created tag: {version_tag}")
    
    # Push the tag to the remote repository
    push_result = subprocess.run(["git", "push", "origin", version_tag], capture_output=True, text=True)
    
    if push_result.returncode == 0:
        print(f"Successfully pushed tag {version_tag} to origin.")
    else:
        print(f"Failed to push tag: {push_result.stderr}")

if __name__ == "__main__":
    version_tag = input("Enter the version tag to create and push: ").strip()
    tag_and_push(version_tag)

print(" \n Python 30 days Series - Day 20 Task 151 \n"                                               )
print(" \n Day 20 : SSH Automation \n"                               )
print(" \n Have a good one! \n "                          + "-"*40)
