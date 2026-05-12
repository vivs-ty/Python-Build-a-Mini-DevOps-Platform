# Task 106: Download multiple files simultaneously with multithreading.

# Task 106: Master Version
import requests
import concurrent.futures
from pathlib import Path
import time

def download_file(url: str, output_dir: Path) -> str:
    """Downloads a file and returns a success message."""
    file_name = url.split("/")[-1] or "downloaded_file"
    file_path = output_dir / f"{file_name}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        file_path.write_bytes(response.content)
        return f"✅ Downloaded: {file_name}"
    except requests.RequestException as e:
        return f"❌ Failed to download {file_name}: {e}"

def main() -> None:
    # Dummy URLs for testing (JSONPlaceholder endpoints)
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
        "https://jsonplaceholder.typicode.com/posts/5"
    ]
    
    download_dir = Path("downloads")
    download_dir.mkdir(exist_ok=True)
    
    print(f"🚀 Starting concurrent downloads of {len(urls)} files...")
    start_time = time.perf_counter()

    # ThreadPoolExecutor automatically manages the pool of background threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks and collect the Future objects
        futures = {executor.submit(download_file, url, download_dir): url for url in urls}
        
        # as_completed yields results immediately as each thread finishes
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    duration = time.perf_counter() - start_time
    print(f"⏱️ All downloads finished in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()
    print("\nPython 30 days Series - Day 15 Task 106\nHave a good one!\n" + "-"*40)