# Task 111: Process a queue of tasks with multiple worker threads.

import threading
import queue
import time

# A thread-safe queue
task_queue = queue.Queue()

def worker(worker_id: int) -> None:
    """A worker thread that continuously pulls from the queue."""
    while True:
        task = task_queue.get()
        if task is None:  # The "Poison Pill" to shut down the thread
            break
            
        print(f" Worker {worker_id} processing: {task}")
        time.sleep(0.5) # Simulate work
        
        # Signal that the task is fully complete
        task_queue.task_done()

def main() -> None:
    # 1. Start 3 worker threads
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    # 2. Add 10 tasks to the queue (Producer)
    print(" Loading queue with 10 tasks...")
    for item in range(1, 11):
        task_queue.put(f"Document_{item}.pdf")

    # 3. Block main thread until the queue is empty
    task_queue.join()
    print(" All tasks in the queue have been processed.")

    # 4. Shut down workers securely using the "Poison Pill" method
    for _ in threads:
        task_queue.put(None)
    for t in threads:
        t.join()
        
    print(" All workers gracefully shut down.")

if __name__ == "__main__":
    main()

    print(" \n Python 30 days Series - Day 15 Task 111 \n"                                               )
    print(" \n Day 15 : Multithreading \n"                               )
    print(" \n Have a good one! \n "                          + "-"*40)
    