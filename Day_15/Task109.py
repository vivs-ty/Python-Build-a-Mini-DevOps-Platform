# Task 109: Monitor multiple servers concurrently by pinging them in parallel.

import requests
import concurrent.futures

def ping_server(url: str) -> str:
    """Sends a lightweight HTTP HEAD request to check server status."""
    try:
        response = requests.head(url, timeout=3, allow_redirects=True)
        status = " ONLINE" if response.status_code < 400 else f" HTTP {response.status_code}"
        return f"{status:<12} | {url}"
    except requests.RequestException:
        return f"{' OFFLINE':<12} | {url}"

def main() -> None:
    servers = [
        "https://www.google.com",
        "https://api.github.com",
        "https://this-site-is-fake.org",
        "https://cloudflare.com",
        "http://httpstat.us/503"
    ]
    
    print(f" Pinging {len(servers)} servers concurrently...\n" + "-"*40)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Using map guarantees the output stays in the original list order
        results = executor.map(ping_server, servers)
        
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
      
    print(" \n Python 30 days Series - Day 15 Task 109 \n"                                               )
    print(" \n Day 15 : Multithreading \n"                               )
    print(" \n Have a good one! \n "                          + "-"*40)
