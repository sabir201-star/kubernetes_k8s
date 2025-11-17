def add(a, b): ...
def subtract(a, b): ...
def multiply(a, b): ...

def divide(a, b):
    """Return a / b. Raise error if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

