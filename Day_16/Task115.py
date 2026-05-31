# Task 115: Use a process pool to compute values and collect results.

import concurrent.futures

def compute_heavy_math(number: int) -> dict:
    """Worker function returning a structured dictionary of results."""
    # Simulate heavy computation
    square = number ** 2
    cube = number ** 3
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        
    # Returning a dictionary makes parsing results much easier later
    return {"number": number, "square": square, "cube": cube}

def main() -> None:
    numbers = [10, 20, 30, 40, 50]
    
    print(" Submitting tasks to the Process Pool...")
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_heavy_math, numbers))
        
    print("\n Computation Results:")
    print("-" * 35)
    for res in results:
        print(f"Number: {res['number']:<3} | Square: {res['square']:<4} | Cube: {res['cube']}")

if __name__ == "__main__":
    main()
    print(" \n Python 30 days Series - Day 16 Task 115 \n"                                               )
    print(" \n Day 16 : Multiprocessing \n"                                )
    print(" \n Have a good one! \n "                          + "-"*40)
