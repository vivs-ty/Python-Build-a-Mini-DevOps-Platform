# Task 88: Accept a URL and print the HTTP status code and response time.

# Task 88: Master Version
import argparse
import urllib.request
import urllib.error
import time

def main() -> None:
    parser = argparse.ArgumentParser(description="URL Status and Ping CLI")
    parser.add_argument("url", type=str, help="The URL to check (e.g., https://google.com)")
    
    args = parser.parse_args()
    
    # Ensure URL is formatted correctly
    url = args.url if args.url.startswith("http") else f"https://{args.url}"

    print(f"📡 Pinging {url} ...")
    
    start_time = time.perf_counter() # High resolution timer
    
    try:
        # Prevent the tool from hanging forever with a 5-second timeout
        with urllib.request.urlopen(url, timeout=5) as response:
            status = response.getcode()
            reason = response.reason
            
    except urllib.error.HTTPError as e:
        status = e.code
        reason = e.reason
    except urllib.error.URLError as e:
        print(f"❌ Failed to connect: {e.reason}")
        return
        
    duration = (time.perf_counter() - start_time) * 1000 # Convert to milliseconds

    # Format output
    color_prefix = "✅" if str(status).startswith("2") else "⚠️"
    print(f"{color_prefix} Status: {status} {reason}")
    print(f"⏱️ Time:   {duration:.2f} ms")

if __name__ == "__main__":
    main()

