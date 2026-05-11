# Task 103: Display API data in a formatted table.

import requests

def fetch_and_print_table(url: str) -> None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Define table headers and column widths
        header = f"{'ID':<5} | {'Username':<15} | {'Email':<25} | {'City':<15}"
        print(header)
        print("-" * len(header))
        
        for user in data[:8]: # Display the first 8 users
            user_id = str(user.get("id", ""))
            username = user.get("username", "")[:15] # Truncate if too long
            email = user.get("email", "")[:25]
            city = user.get("address", {}).get("city", "")[:15]
            
            # Use string interpolation with alignment
            print(f"{user_id:<5} | {username:<15} | {email:<25} | {city:<15}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")

# --- Demonstration ---
fetch_and_print_table("https://jsonplaceholder.typicode.com/users")

print("\nPython 30 days Series - Day 14 Task 103\nHave a good one!\n" + "-"*40)