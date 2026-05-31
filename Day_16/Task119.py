# Task 119: Simulate concurrent users with multiple processes.

import multiprocessing
import time
import random

def simulate_user_session(user_id: int) -> None:
    """Simulates a user logging in, doing work, and logging out."""
    print(f" [User {user_id}] Logged in.")
    
    # Simulate variable active session time
    work_time = random.uniform(1.0, 3.0)
    time.sleep(work_time)
    
    # Simulate a heavy transaction
    _ = [x**2 for x in range(1_000_000)]
    
    print(f" [User {user_id}] Completed transaction and logged out ({work_time:.1f}s).")

def main() -> None:
    user_count = 5
    processes = []
    
    print(f" Simulating {user_count} concurrent user sessions...\n" + "-"*40)
    
    # Spawn a completely isolated process for each simulated user
    for i in range(1, user_count + 1):
        p = multiprocessing.Process(target=simulate_user_session, args=(i,))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    print("-" * 40)
    print(" Load test complete. System stable.")

if __name__ == "__main__":
    main()
    print(" \n Python 30 days Series - Day 16 Task 119 \n"                                               )
    print(" \n Day 16 : Multiprocessing \n"                                )
    print(" \n Have a good one! \n "                          + "-"*40)
    