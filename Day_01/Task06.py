# Task 6: Build a simple command-line calculator that supports +, -, *, and /.

def calculator():
    print("Welcome to the Simple Command-Line Calculator!")
    print("You can perform operations: +, -, *, /, %,")
    
    num1 = float(input("Enter the first number: ").strip())
    operator = input("Enter the operator (+, -, *, /): ").strip()
    num2 = float(input("Enter the second number: ").strip())
    
    if operator == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is undefined.")
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
            print(f"The result of {num1} % {num2} is: {result}")
        else:
            print("Error: Division by zero is undefined.")
    else:
        print("Invalid operator. Please use one of +, -, *, /, %.")
    
    print(f" \n Python 30 days Series - Day 1 Task 6 \n")
    print(f" \n Have a good one! ")


if __name__ == "__main__":
        calculator()
