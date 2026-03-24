#  Task 16: Generate the Fibonacci sequence up to `N` terms.
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_term = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_term)
        return sequence
print(f" \n Python 30 days Series - Day 3 Task 16 \n")
print(f" \n Have a good one! \n")
