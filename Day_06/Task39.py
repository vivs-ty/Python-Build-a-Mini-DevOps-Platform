# Task 39: Use *args to calculate the sum and average of values.

def calculate_sum_and_average(*args):
    if not args:
        return 0, 0  # Handle case with no arguments

    total_sum = sum(args)
    average = total_sum / len(args)
    return total_sum, average

# Example usage
print(calculate_sum_and_average(1, 2, 3, 4, 5))  # Output: (15, 3.0)
print(calculate_sum_and_average())  # Output: (0, 0)
print(f" \n Python 30 days Series - Day 6 Task 39 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
