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
