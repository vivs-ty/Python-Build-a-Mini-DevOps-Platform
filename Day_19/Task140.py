# Task 140: Download log files from a remote server.

import paramiko

def download_file(hostname, username, password, remote_path, local_path):
    transport = paramiko.Transport((hostname, 22))
    
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        
        sftp.get(remote_path, local_path)
        print(f"Successfully downloaded {remote_path} to {local_path}")
        
    except Exception as e:
        print(f"Download failed: {e}")
    finally:
        if 'sftp' in locals(): 
            sftp.close()
        transport.close()

# Example usage:
# download_file("192.168.1.10", "admin", "secretpass", "/var/log/syslog", "server_syslog.txt")