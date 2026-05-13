# Task 119: Simulate concurrent users with multiple processes.
import multiprocessing
import time

def simulate_user(user_id):
    print(f"User {user_id} started")
    time.sleep(2)  # Simulate some work
    print(f"User {user_id} finished")

if __name__ == "__main__":
    user_ids = range(10)
    
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(simulate_user, user_ids)