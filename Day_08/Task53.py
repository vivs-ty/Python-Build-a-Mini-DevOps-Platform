# Task 53: Use encapsulation with private attributes and getter or setter methods.

class Server:
    def __init__(self, hostname: str, ip_address: str):
        self.hostname = hostname
        self._ip_address = ip_address # The underscore indicates it is private

    # Getter
    @property
    def ip_address(self) -> str:
        return self._ip_address

    # Setter with validation
    @ip_address.setter
    def ip_address(self, new_ip: str):
        if new_ip.count('.') == 3: # Simple IPv4 validation check
            self._ip_address = new_ip
            print(f" IP for {self.hostname} updated to {new_ip}")
        else:
            print(f" Error: '{new_ip}' is an invalid IP format.")

# Demonstration
secure_server = Server("proxy-01", "10.0.0.1")
print(f"Current IP: {secure_server.ip_address}")

secure_server.ip_address = "10.0.0.2" # Valid update
secure_server.ip_address = "999.invalid.ip" # Invalid update attempt
print(f" \n Python 30 days Series - Day 8 Task 53 \n")
print(f" \n Day 8: OOPs \n")
print(f" \n Have a good one! \n " + "-"*40)
