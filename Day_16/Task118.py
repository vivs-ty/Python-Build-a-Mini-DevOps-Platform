# Task 118: Demonstrate inter-process communication with queues.
import multiprocessing

def worker(queue, result_queue):
    while True:
        item = queue.get()
        if item is None:
            break
        # Process the item
        processed_item = item * 2
        result_queue.put(processed_item)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    # Start worker processes
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=worker, args=(queue, result_queue))
        p.start()
        processes.append(p)

    # Put items in the queue
    for i in range(10):
        queue.put(i)

    # Signal workers to stop
    for _ in range(4):
        queue.put(None)

    # Collect results
    results = []
    for _ in range(10):
        results.append(result_queue.get())

    print(results)

    # Wait for all processes to finish
    for p in processes:
        p.join()
        