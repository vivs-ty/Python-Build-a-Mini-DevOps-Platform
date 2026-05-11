# Task 97: Check whether a website is reachable with an HTTP request.

import requests
from requests.exceptions import RequestException

def is_reachable(url: str, timeout: int = 5) -> bool:
    print(f" Pinging {url}...")
    try:
        # We use .head() instead of .get() because it only asks for the headers.
        # This saves bandwidth and time by not downloading the page content.
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        # raise_for_status() throws an error for 4xx and 5xx status codes
        response.raise_for_status() 
        print(" Website is reachable and healthy!")
        return True
    except RequestException as e:
        print(f" Website is unreachable. Reason: {e}")
        return False

# --- Demonstration ---
is_reachable("https://www.google.com")
is_reachable("https://this-site-is-fake-and-will-fail.com")

print(f" \n Python 30 days Series - Day 14 Task 97\n")
print(f" \n Day 14 : Networking and APIs \n")
print(f" \n Have a good one! \n " + "-"*40)
