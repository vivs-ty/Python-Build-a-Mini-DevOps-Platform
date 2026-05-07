#  Task 16: Generate the Fibonacci sequence up to N terms.

n = int(input("Enter the number of terms for Fibonacci sequence: ").strip())
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence of 1 terms: [0]")
else:
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
    print(f"Fibonacci sequence of {n} terms: {sequence[:n]}")

print(f" \n Python 30 days Series - Day 3 Task 16 \n")
print(f" \n Day 3: Loops \n")
print(f" \n Have a good one! \n " + "-"*40)
