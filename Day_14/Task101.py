# Task 101: Retry an API request up to three times on network failure.

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def resilient_api_call(url: str) -> None:
    # 1. Configure the retry strategy
    retry_strategy = Retry(
        total=3, # Total number of retries
        backoff_factor=1, # Wait 1s, 2s, 4s between retries
        status_forcelist=[429, 500, 502, 503, 504], # Which HTTP errors trigger a retry
    )
    
    # 2. Attach the strategy to a Session
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    print("🔄 Attempting to connect with automatic retries enabled...")
    try:
        # We will test this on a site that intentionally times out
        response = session.get(url, timeout=3)
        print(f"✅ Success! Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request ultimately failed after retries. Error: {e}")

# --- Demonstration ---
# We use httpstat.us to simulate a 503 Service Unavailable error
resilient_api_call("https://httpstat.us/503")

print("\nPython 30 days Series - Day 14 Task 101\nHave a good one!\n" + "-"*40)