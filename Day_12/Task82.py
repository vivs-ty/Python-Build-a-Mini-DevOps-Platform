# Task 82: Build a CLI calculator that accepts two numbers and an operation.

# Task 82: Master Version
import argparse
import operator

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI Calculator")
    
    # Positional arguments for numbers
    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("num2", type=float, help="The second number")
    
    # Optional argument with strict choices
    parser.add_argument(
        "-o", "--operation", 
        choices=['add', 'sub', 'mul', 'div'], 
        default='add',
        help="The mathematical operation to perform (default: add)"
    )

    args = parser.parse_args()

    # Dictionary dispatch (cleaner than if/elif chains)
    ops = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
        'div': operator.truediv
    }

    try:
        result = ops[args.operation](args.num1, args.num2)
        print(f"🧮 Result: {result}")
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()

