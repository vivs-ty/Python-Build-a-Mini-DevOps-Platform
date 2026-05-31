# Task 112: Perform parallel API requests and aggregate the results.

import requests
import concurrent.futures
import time

def fetch_user_data(user_id: int) -> dict:
    """Fetches data from an API for a specific user ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {"id": user_id, "name": data.get("name"), "status": "Success"}
    except Exception as e:
        return {"id": user_id, "name": "Unknown", "status": f"Failed: {e}"}

def main() -> None:
    user_ids = list(range(1, 11)) # Fetch users 1 through 10
    aggregated_data = []
    
    print(f" Fetching {len(user_ids)} users from API concurrently...")
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # execute tasks and aggregate into a list
        for result in executor.map(fetch_user_data, user_ids):
            aggregated_data.append(result)

    # Display the aggregated report
    print("\n Aggregated Results:")
    print("-" * 40)
    for user in aggregated_data:
        icon = "" if user["status"] == "Success" else ""
        print(f"{icon} ID: {user['id']:<2} | Name: {user['name']:<20}")

    duration = time.perf_counter() - start
    print(f"\n Aggregated {len(aggregated_data)} records in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()

    print(" \n Python 30 days Series - Day 15 Task 112 \n"                                               )
    print(" \n Day 15 : Multithreading \n"                               )
    print(" \n Have a good one! \n "                          + "-"*40)
    