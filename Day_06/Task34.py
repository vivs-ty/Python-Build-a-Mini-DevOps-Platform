# Task 34: Write a function that returns the maximum, minimum, and average of a list without using max() or min().

from typing import List, Tuple, Optional

def calculate_stats(numbers: List[float]) -> Optional[Tuple[float, float, float]]:
    if not numbers: return None
    
    max_num = min_num = numbers[0]
    total = 0.0

    for num in numbers:
        total += num
        if num > max_num: max_num = num
        if num < min_num: min_num = num

    return max_num, min_num, total / len(numbers)

stats = calculate_stats([3, 1, 4, 1, 5, 9])
if stats:
    mx, mn, avg = stats
    print(f"Max: {mx}, Min: {mn}, Average: {avg:.2f}")
print(f" \n Python 30 days Series - Day 6 Task 34 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n " + "-"*40)
