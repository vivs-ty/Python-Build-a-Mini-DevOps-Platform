# Task 105: Run multiple functions concurrently with threads.

# Task 105: Master Version
import threading
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(threadName)s] %(message)s")

def task_a(delay: int) -> None:
    logging.info(f"Task A started. Working for {delay} seconds...")
    time.sleep(delay)
    logging.info("Task A completed!")

def task_b(delay: int) -> None:
    logging.info(f"Task B started. Working for {delay} seconds...")
    time.sleep(delay)
    logging.info("Task B completed!")

def main() -> None:
    logging.info("Main program started.")
    
    # Initialize threads, passing arguments via 'args' tuple
    thread1 = threading.Thread(target=task_a, args=(3,), name="Worker-A")
    thread2 = threading.Thread(target=task_b, args=(2,), name="Worker-B")

    # Start the threads (they run simultaneously)
    thread1.start()
    thread2.start()

    # Join blocks the main program until both threads finish
    thread1.join()
    thread2.join()
    
    logging.info("Main program finished. All threads closed.")

if __name__ == "__main__":
    main()
    print("\nPython 30 days Series - Day 15 Task 105\nHave a good one!\n" + "-"*40)