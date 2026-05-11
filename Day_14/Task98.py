# Task 98: Fetch data from a public API and display selected fields.

import requests

def fetch_and_display_users(api_url: str) -> None:
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        
        # Requests natively parses JSON into Python dictionaries/lists
        users_data = response.json() 
        
        print(" Fetched User Directory:\n" + "="*30)
        for user in users_data[:5]: # Let's just grab the first 5 for the demo
            # Safe extraction using .get()
            name = user.get("name", "Unknown Name")
            email = user.get("email", "No Email provided")
            company = user.get("company", {}).get("name", "Independent")
            
            print(f" - {name} ({email}) | Company: {company}")
            
    except requests.exceptions.RequestException as e:
        print(f" API Request failed: {e}")

# --- Demonstration ---
# We use JSONPlaceholder, a free fake API for testing
fetch_and_display_users("https://jsonplaceholder.typicode.com/users")

print(f" \n Python 30 days Series - Day 14 Task 98\n")
print(f" \n Day 14 : Networking and APIs \n")
print(f" \n Have a good one! \n " + "-"*40)
