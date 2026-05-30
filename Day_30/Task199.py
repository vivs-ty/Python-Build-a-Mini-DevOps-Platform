# Task 199: Log all access attempts to a secure resource.

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='access_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
def log_access_attempt(username, resource, success):
    status = 'SUCCESS' if success else 'FAILURE'
    logging.info(f"Access attempt by {username} to {resource}: {status}")
if __name__ == "__main__":
    # Simulate some access attempts
    log_access_attempt('alice', 'secure_resource', True)
    log_access_attempt('bob', 'secure_resource', False)
    log_access_attempt('charlie', 'secure_resource', True)
    log_access_attempt('dave', 'secure_resource', False)
    print("Access attempts have been logged to access_log.txt")
    