import pytest
from src.calculator import add, subtract, multiply, divide, power, sqrt


class TestAddSubtract:
    def test_add_positive(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(5, 3) == 2


class TestMultiplyDividePowerSqrt:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(0, 10) == 0

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6

    def test_multiply_validation(self):
        with pytest.raises(TypeError, match="must be a number"):
            multiply("5", 3)

    def test_divide_basic(self):
        assert divide(10, 2) == 5

    def test_divide_negative(self):
        assert divide(-12, -3) == 4

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_validation(self):
        with pytest.raises(TypeError, match="must be a number"):
            divide("10", 2)

    def test_power_basic(self):
        assert power(2, 3) == 8
        assert power(2, -1) == 0.5

    def test_power_validation(self):
        with pytest.raises(TypeError):
            power("2", 3)

    def test_sqrt_basic(self):
        assert sqrt(16) == 4

    def test_sqrt_negative(self):
        with pytest.raises(ValueError):
            sqrt(-1)
