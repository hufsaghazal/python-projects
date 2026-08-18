# =================
# Simple Calculator
# =================


import math

# --------------------
# Arithmetic operations
# --------------------


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    # Prevent division by zero, which is undefined.
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(a: float, b: float) -> float:
    return (a + b) / 2


def modulo(a: float, b: float) -> float:
    # Prevent modulo by zero, which is undefined.
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


# ------------------------
# Single-number operations
# ------------------------


def square(a: float) -> float:
    return a**2


def square_root(a: float) -> float:
    # Square roots of negative real numbers are not supported by this calculator.
    if a < 0:
        raise ValueError("Square root of a negative number is not allowed")
    return math.sqrt(a)


def power(a: float, b: float) -> float:
    return a**b


def cube(a: float) -> float:
    return a**3


# --------------------
# User input
# --------------------


def get_user_input(operation):
    while True:
        try:
            if operation in (1, 2, 3, 4, 5, 6, 7):
                first_number = float(input("\nEnter the first number: "))
                second_number = float(input("Enter the second number: "))
                return first_number, second_number
            elif operation in (8, 9, 10):
                number = float(input("\nEnter the number: "))
                return number
        except ValueError:
            print("\nPlease enter a valid number.\n")


# --------------------
# Calculator interface
# --------------------


def calculator():
    while True:
        print("""Operations you can perform:\n 
1. Addition
2. Subtraction
3. Multiplication 
4. Division
5. Average
6. Modulus
7. Power
8. Square root
9. Square
10. Cube
or type 'exit' to quit.\n""")

        operation = (
            input("Enter the number of the operation from (1-10) or 'exit' to quit:  ")
            .lower()
            .strip()
        )

        if operation == "exit":
            print("\nGoodbye!\n")
            break

        try:
            operation = int(operation)
        except ValueError:
            print("\nPlease enter a valid number.\n")
            continue

        if operation in (1, 2, 3, 4, 5, 6, 7):
            first_number, second_number = get_user_input(operation)
            try:
                if operation == 1:
                    print(
                        f"\n{first_number} + {second_number} = {add(first_number, second_number)}\n"
                    )
                elif operation == 2:
                    print(
                        f"\n{first_number} - {second_number} = {subtract(first_number, second_number)}\n"
                    )
                elif operation == 3:
                    print(
                        f"\n{first_number} * {second_number} = {multiply(first_number, second_number)}\n"
                    )
                elif operation == 4:
                    print(
                        f"\n{first_number} / {second_number} = {divide(first_number, second_number)}\n"
                    )
                elif operation == 5:
                    print(
                        f"\n({first_number} + {second_number}) / 2 = {average(first_number, second_number)}\n"
                    )
                elif operation == 6:
                    print(
                        f"\n{first_number} % {second_number} = {modulo(first_number, second_number)}\n"
                    )
                elif operation == 7:
                    print(
                        f"\n{first_number} ^ {second_number} = {power(first_number, second_number)}\n"
                    )
            except ValueError as error:
                print(f"\nError: {error}\n")

        elif operation in (8, 9, 10):

            number = get_user_input(operation)
            try:
                if operation == 8:
                    print(f"\nSquare root of {number} = {square_root(number)}\n")
                elif operation == 9:
                    print(f"\nSquare of {number} = {square(number)}\n")
                elif operation == 10:
                    print(f"\nCube of {number} = {cube(number)}\n")

            except ValueError as error:
                print(f"\nError: {error}\n")

        else:
            print("\nPlease enter a valid operation.")


if __name__ == "__main__":
    calculator()
