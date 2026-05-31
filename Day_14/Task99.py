# Task 99: Retrieve the HTTP status code and headers for a URL.

import requests

def get_headers_and_status(url: str) -> None:
    try:
        response = requests.get(url, timeout=5)
        
        print(f" URL: {url}")
        print(f" Status Code: {response.status_code} ({response.reason})")
        print(" Select Headers:")
        
        # Headers we specifically care about in production
        keys_to_check = ["Server", "Content-Type", "Date"]
        
        for key in keys_to_check:
            # response.headers is case-insensitive, which is a great feature of 'requests'
            value = response.headers.get(key, "Not Provided")
            print(f"   -> {key}: {value}")
            
    except requests.exceptions.RequestException as e:
        print(f" Failed to connect: {e}")

# --- Demonstration ---
get_headers_and_status("https://api.github.com")

print(" \n Python 30 days Series - Day 14 Task 99\n"                                             )
print(" \n Day 14 : Networking and APIs \n"                                    )
print(" \n Have a good one! \n "                          + "-"*40)
