# Task 145: Clone a remote Git repository.

import subprocess

def clone_repository(repo_url, destination=""):
    command = ["git", "clone", repo_url]
    if destination:
        command.append(destination)
        
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Successfully cloned {repo_url}")
    else:
        print(f"Error cloning repository: {result.stderr}")

if __name__ == "__main__":
    repo_url = input("Enter the Git repository URL to clone: ").strip()
    destination = input("Enter the destination folder (leave blank for current directory): ").strip()
    clone_repository(repo_url, destination)


# Example usage:
# clone_repository("https://github.com/user/repo.git", "my_folder")

print(f" \n Python 30 days Series - Day 20 Task 145 \n")
print(f" \n Day 20 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)
