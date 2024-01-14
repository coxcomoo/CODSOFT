# Define a function for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Prompt the user for input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)
else:
    raise ValueError("Invalid operation!")

# Display the result
print(f"{a} {operation} {b} = {result}")
