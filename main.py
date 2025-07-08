def get_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter operator (+, -, *, /): ")
        if op in valid_operators:
            return op
        else:
            print("Please choose from +, -, *, or /.")


def calculator():
    print("Welcome to the Python Calculator!")

    num1 = get_number("Enter first number: ")
    operator = get_operator()
    num2 = get_number("Enter second number: ")

    if operator == '/' and num2 == 0:
        print("Error: Division by zero is not valid.")
        return

    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    print(f" Result: {num1} {operator} {num2} = {result}")


calculator()

