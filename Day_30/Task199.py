# Task 199: Log all access attempts to a secure resource.

import logging

# Configure logging for security auditing
logging.basicConfig(
    filename='security_audit.log',
    level=logging.INFO,
    format='%(asctime)s - AUDIT - %(levelname)s - %(message)s'
)

def secure_resource_access(username, has_valid_token):
    resource_name = "Financial_Records_DB"
    
    if has_valid_token:
        # Log successful access
        log_message = f"Access GRANTED to user '{username}' for resource '{resource_name}'"
        logging.info(log_message)
        print(f"Success: {log_message}")
        return "Sensitive Data Payload"
    else:
        # Log failed access attempt
        log_message = f"Access DENIED to user '{username}' for resource '{resource_name}'. Invalid token."
        logging.warning(log_message)
        print(f"Security Alert: {log_message}")
        raise PermissionError("Access Denied.")

if __name__ == "__main__":
    print("Attempting to access resources. Check 'security_audit.log' for the audit trail.\n")
    
    # Authorized access
    try:
        secure_resource_access(username="admin_sarah", has_valid_token=True)
    except PermissionError:
        pass

    # Unauthorized access
    try:
        secure_resource_access(username="guest_user", has_valid_token=False)
    except PermissionError:
        pass

    print("\nPython 30 days Series - Day 30 : Task 199")
    print("Day 30 : Security Review and Compliance")
    print("Have a good one!\n" + "-"*40)
    