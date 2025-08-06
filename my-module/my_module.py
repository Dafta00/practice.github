# my_module.py

def reverse_text(text):
    """
    Reverses the given string.
    """
    return text[::-1]

def simple_calculator(a, b, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"
