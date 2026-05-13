# Task 118: Demonstrate inter-process communication with queues.

import multiprocessing
import time

def producer(queue: multiprocessing.Queue) -> None:
    """Generates data and puts it into the queue."""
    for item in ["Task 1", "Task 2", "Task 3"]:
        print(f" Producer: Sent '{item}' to queue.")
        queue.put(item)
        time.sleep(0.5)
    
    # Send a "Poison Pill" to tell the consumer to stop
    queue.put(None)
    print(" Producer: Finished sending tasks.")

def consumer(queue: multiprocessing.Queue) -> None:
    """Reads data from the queue until it finds the Poison Pill."""
    while True:
        task = queue.get()
        if task is None: # The Poison Pill
            print(" Consumer: Received shutdown signal.")
            break
        print(f" Consumer: Processed '{task}'.")
        time.sleep(1)

def main() -> None:
    # A thread/process-safe queue
    shared_queue = multiprocessing.Queue()
    
    # Initialize the raw processes
    p1 = multiprocessing.Process(target=producer, args=(shared_queue,))
    p2 = multiprocessing.Process(target=consumer, args=(shared_queue,))
    
    # Start them
    p1.start()
    p2.start()
    
    # Wait for them to finish
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
    print(f" \n Python 30 days Series - Day 16 Task 118 \n")
    print(f" \n Day 16 : Multiprocessing \n")
    print(f" \n Have a good one! \n " + "-"*40)
    