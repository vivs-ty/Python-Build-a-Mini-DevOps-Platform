#  Task 14: Generate a multiplication table for a user-provided number.

number = int(input("Enter a number to generate it's multiplication table: ").strip())
print(f"\n You have entered {number} \n Multiplication Table for {number}:\n")
for i in range(1, 21):
    print(f"{number} x {i} = {number * i}")
print(f" \n Python 30 days Series - Day 3 Task 14 \n")
print(f" \n Day 3: Loops \n")
print(f" \n Have a good one! \n " + "-"*40)
