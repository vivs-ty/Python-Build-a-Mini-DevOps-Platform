# Task 104: Monitor an API endpoint and alert when the response is not 200.

import requests
import time
import logging

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(message)s")

def monitor_endpoint(url: str, interval_seconds: int = 5, cycles: int = 3) -> None:
    print(f"👀 Monitoring {url} (Checking every {interval_seconds}s)")
    print("Press Ctrl+C to stop...\n")
    
    # NOTE: Changed from 'while True' to a limited 'for' loop just so it doesn't 
    # freeze your terminal during testing. In production, use 'while True'.
    for _ in range(cycles): 
        try:
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"✅ {time.strftime('%H:%M:%S')} - HTTP 200: OK")
            else:
                alert = f"🚨 ALERT: Unexpected Status Code {response.status_code}"
                print(alert)
                logging.warning(f"{url} returned {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            alert = f"🚨 ALERT: Connection completely failed!"
            print(f"{alert} ({e})")
            logging.error(f"Failed to reach {url}: {e}")
            
        time.sleep(interval_seconds)

# --- Demonstration ---
# Testing on an endpoint that returns a 404 Not Found
monitor_endpoint("https://httpstat.us/404", interval_seconds=2)

print("\nPython 30 days Series - Day 14 Task 104\nHave a good one!\n" + "-"*40)