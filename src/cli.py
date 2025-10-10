import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1")
@click.argument("num2", required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        # Convert inputs to numbers
        num1 = float(num1)
        if num2 is not None:
            num2 = float(num2)

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        click.echo(str(result))
        sys.exit(0)

    except ValueError as e:
        click.echo(str(e))
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
