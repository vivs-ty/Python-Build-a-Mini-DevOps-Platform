# Task 3: Take two numbers as input and print their sum, difference, product, and quotient.

number1 = float(input("Enter your First Number : ").strip())
number2 = float(input("Enter Your Second Number : ").strip())
total = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2 if number2 != 0 else "Undefined (division by zero)"

print(f" \n The sum of {number1} and {number2} is : {total} \n")
print(f" \n The difference of {number1} and {number2} is : {difference} \n")
print(f" \n The product of {number1} and {number2} is : {product} \n")
print(f" \n The quotient of {number1} and {number2} is :    {quotient} \n")
print(f" \n Welcome to the World of DevOps Engineers! \n")
print(f" \n Python 30 days Series - Day 1 Task 3 \n")
print(f" \n Day 1: Input, Output, and Variables \n")
print(f" \n Have a good one! ")
