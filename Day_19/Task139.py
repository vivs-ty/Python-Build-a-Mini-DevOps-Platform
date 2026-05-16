# Task 139: Upload a file to a remote server securely.

import paramiko

def upload_file(hostname, username, password, local_path, remote_path):
    transport = paramiko.Transport((hostname, 22))
    
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        
        sftp.put(local_path, remote_path)
        print(f"Successfully uploaded {local_path} to {remote_path}")
        
    except Exception as e:
        print(f"Upload failed: {e}")
    finally:
        if 'sftp' in locals(): 
            sftp.close()
        transport.close()

print(f" \n Python 30 days Series - Day 19 Task 139 \n")
print(f" \n Day 19 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)

# Example usage:
# upload_file("192.168.1.10", "admin", "secretpass", "local_script.py", "/home/admin/remote_script.py")