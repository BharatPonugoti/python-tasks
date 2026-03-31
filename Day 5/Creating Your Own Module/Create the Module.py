#Create a Python module named calculator.py#
# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

#Then write another Python program that imports this module and performs calculations based on user input.#
# main.py

import calculator

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if choice == '1':
        result = calculator.add(num1, num2)
    elif choice == '2':
        result = calculator.subtract(num1, num2)
    elif choice == '3':
        result = calculator.multiply(num1, num2)
    elif choice == '4':
        result = calculator.divide(num1, num2)
    else:
        print("Invalid choice!")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()