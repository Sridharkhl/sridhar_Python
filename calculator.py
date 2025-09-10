#!/usr/bin/env python3
"""Simple command-line calculator."""

def add(x: float, y: float) -> float:
    """Return the sum of two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Return the difference of two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Return the product of two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main() -> None:
    """Run the calculator application."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "*"),
        "4": (divide, "/"),
    }

    if choice not in operations:
        print("Invalid choice")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        func, symbol = operations[choice]
        result = func(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
