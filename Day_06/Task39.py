# Task 39: Use *args to calculate the sum and average of values.

def calculate_sum_and_average(*args: float) -> tuple[float, float]:
    if not args:
        return 0.0, 0.0 
    total = sum(args)
    return total, total / len(args)

total, avg = calculate_sum_and_average(1, 2, 3, 4, 5)
print(f"Sum: {total}, Average: {avg}")
print(" \n Python 30 days Series - Day 6 Task 39 \n"                                             )
print(" \n Day 6: Functions and Error Handling \n"                                           )
print(" \n Have a good one! \n "                          + "-"*40)
