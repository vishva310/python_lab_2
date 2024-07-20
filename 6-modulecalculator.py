def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def percentage(a, b):
    return (a * b) / 100

# Example usage:
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    percentage_value = 20
    
    # Addition
    result_add = add(num1, num2)
    print(f"{num1} + {num2} = {result_add}")
    
    # Subtraction
    result_subtract = subtract(num1, num2)
    print(f"{num1} - {num2} = {result_subtract}")
    
    # Multiplication
    result_multiply = multiply(num1, num2)
    print(f"{num1} * {num2} = {result_multiply}")
    
    # Division
    result_divide = divide(num1, num2)
    print(f"{num1} / {num2} = {result_divide}")
    
    # Percentage
    result_percentage = percentage(num1, percentage_value)
    print(f"{percentage_value}% of {num1} = {result_percentage}")
