def calculate(operation, num1, num2=None):
 """Simple calculator CLI"""
 try:
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
 elif operation == "square_root" or operation
== "sqrt":
 result = square_root(num1)
else:
 click.echo(f"Unknown operation:
{operation}")
 sys.exit(1) 