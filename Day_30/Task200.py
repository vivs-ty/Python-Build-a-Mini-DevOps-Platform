# Task 200: Create a compliance checker for rules such as no plaintext passwords and proper permissions.

def check_compliance(system_configuration):
    violations = []

    print("Running compliance checks...\n")

    # Rule 1: No plaintext passwords
    for user in system_configuration.get("users", []):
        username = user.get("username")
        password = user.get("password", "")
        
        # A proper hash usually starts with specific identifiers like $2b$ (bcrypt) or $argon2
        if not password.startswith("$"):
            violations.append(f"COMPLIANCE FAILURE: Plaintext password detected for user '{username}'.")

    # Rule 2: No overly permissive file permissions (e.g., 777 in Linux)
    for file in system_configuration.get("files", []):
        filename = file.get("filename")
        permissions = file.get("permissions")
        
        if permissions == "777":
            violations.append(f"COMPLIANCE FAILURE: File '{filename}' has overly permissive access ({permissions}).")

    return violations

if __name__ == "__main__":
    # Mock system configuration data
    mock_system_state = {
        "users": [
            {"username": "admin", "password": "$2b$12$SecureHashedPasswordStringHere"},
            {"username": "developer", "password": "password123"}  # Violation
        ],
        "files": [
            {"filename": "/etc/config", "permissions": "644"},
            {"filename": "/var/www/html/upload", "permissions": "777"}  # Violation
        ]
    }

    report = check_compliance(mock_system_state)

    if report:
        print("System is NON-COMPLIANT. The following issues were found:")
        for issue in report:
            print(f" - {issue}")
    else:
        print("System is COMPLIANT. No violations found.")

    print("\nPython 30 days Series - Day 30 : Task 200")
    print("Day 30 : Security Review and Compliance")
    print("Have a good one!\n" + "-"*40)
    