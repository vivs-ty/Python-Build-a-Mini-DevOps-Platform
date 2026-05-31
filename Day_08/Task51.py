# Task 51: Create LinuxServer and WindowsServer classes that inherit from Server.

class Server:
    def __init__(self, hostname: str, ip_address: str):
        self.hostname = hostname
        self.ip_address = ip_address

# LinuxServer inherits from Server
class LinuxServer(Server):
    def __init__(self, hostname: str, ip_address: str, distro: str):
        super().__init__(hostname, ip_address) # Call parent constructor
        self.distro = distro

# WindowsServer inherits from Server
class WindowsServer(Server):
    def __init__(self, hostname: str, ip_address: str, license_key: str):
        super().__init__(hostname, ip_address)
        self.license_key = license_key

# Demonstration
ubuntu_node = LinuxServer("worker-1", "192.168.1.50", "Ubuntu 22.04")
win_node = WindowsServer("ad-primary", "192.168.1.100", "WIN-XYZ-123")

print(f"Linux Node: {ubuntu_node.hostname} running {ubuntu_node.distro}")
print(f"Windows Node: {win_node.hostname} with IP {win_node.ip_address}")
print(" \n Python 30 days Series - Day 8 Task 51 \n"                                             )
print(" \n Day 8: OOPs \n"                   )
print(" \n Have a good one! \n "                          + "-"*40)
