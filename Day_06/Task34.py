# Task 34: Write a function that returns the maximum, minimum, and average of a list without using max() or min().

def calculate_stats(numbers):
    if not numbers:
        return None, None, None  # Handle empty list case

    max_num = numbers[0]
    min_num = numbers[0]
    total = 0

    for num in numbers:
        total += num
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    average = total / len(numbers)
    return max_num, min_num, average
print(calculate_stats([3, 1, 4, 1, 5, 9]))  # Example usage
print(f" \n Python 30 days Series - Day 6 Task 34 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
