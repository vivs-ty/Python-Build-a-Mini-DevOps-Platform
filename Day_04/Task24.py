# Task 24: Build a password strength checker based on length, uppercase letters, digits, and special characters.

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-+" for char in password):
        strength += 1

    return strength
input_password = input("Enter a password to check its strength: ").strip()
strength = check_password_strength(input_password)
strength_levels = {
    0: "Very Weak",
    1: "Weak",
    2: "Moderate",
    3: "Strong",
    4: "Very Strong"
}
print(f"Password strength: {strength_levels.get(strength, 'Unknown')}")
print(f" \n Python 30 days Series - Day 4 Task 24 \n")
print(f" \n Day 4: Strings \n")
print(f" \n Have a good one! \n")