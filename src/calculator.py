"""Simple calculator helpers."""

import math
from typing import Union

Number = Union[int, float]


def _ensure_number(x, name="value"):
    """Internal check to ensure a value is numeric."""
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number")


def add(a: Number, b: Number) -> Number:
    """Return a + b."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return a - b."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return a * b."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return a / b, raising on divide-by-zero."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a: Number, b: Number) -> float:
    """Return a ** b."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a**b


def sqrt(x: Number) -> float:
    """Return √x."""
    _ensure_number(x, "x")
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

square_root = sqrt
