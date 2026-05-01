# Task 12: Build a grading system for marks from 0 to 100.

marks = int(input("Enter Your Marks in range of 0 to 100: ").strip())
if marks < 0 or marks > 100:
    print("Invalid marks entered. Please enter a value between 0 and 100.")
elif marks >= 90:
    print(f"Your marks {marks} is Grade A \n keep up the good work! \n")
elif marks >= 80:
    print(f"Your marks {marks} is Grade B \n good job! \n")
elif marks >= 70:
    print(f"Your marks {marks} is Grade C \n you can do better! \n")
elif marks >= 60:
    print(f"Your marks {marks} is Grade D \n needs improvement! \n")
elif marks >= 50:
    print(f"Your marks {marks} is Grade E \n almost there! \n")
else:
    print(f"Your marks {marks} is Grade F \n better luck next time! \n")

print(f" \n Python 30 days Series - Day 2 Task 12 \n")
print(f" \n Day 2: Conditional Logic \n")
print(f" \n Have a good one! ")
