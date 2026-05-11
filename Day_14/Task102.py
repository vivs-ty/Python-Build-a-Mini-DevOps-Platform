# Task 102: Measure API response time and log it.

import requests
import logging

# Configure production-style auditing
logging.basicConfig(
    filename="api_latency.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def benchmark_endpoint(url: str) -> None:
    try:
        response = requests.get(url, timeout=10)
        
        # response.elapsed returns a timedelta object of exactly how long the request took
        duration_ms = response.elapsed.total_seconds() * 1000
        status = response.status_code
        
        log_msg = f"Endpoint: {url} | Status: {status} | Latency: {duration_ms:.2f} ms"
        logging.info(log_msg)
        print(f"⏱️ {log_msg}")
        print("📝 Logged to api_latency.log")
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to reach {url}: {e}")
        print(f"❌ Benchmark failed: {e}")

# --- Demonstration ---
benchmark_endpoint("https://api.github.com")

print("\nPython 30 days Series - Day 14 Task 102\nHave a good one!\n" + "-"*40)