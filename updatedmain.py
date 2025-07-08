def is_valid_expression(expr):
    allowed = "0123456789+-*/(). "
    for char in expr:
        if char not in allowed:
            return False
    return True

def calculator():
    print("Welcome to the Smart Python Calculator!")
    print("You can use numbers and operators: +  -  *  /  ( )")
    print("Example: (3 + 5) * 2 / 4")
    print("Do NOT use alphabets or symbols like $, &, %, etc.")

    while True:
        expr = input("Enter your math expression: ")

        if not expr:
            print("❌ You didn't type anything. Please enter a math expression like 2 + 3 * 4")
            continue

        # Check if expression has only valid characters
        if not is_valid_expression(expr):
            print(f"Invalid input: '{expr}' contains unsupported characters.")
            print(" Please use only digits, +, -, *, /, (, ), and spaces.")
            continue

        try:
            result = eval(expr)
            print(f"Result of '{expr}' is: {result}")
        except ZeroDivisionError:
            print(f"Error: Division by zero in expression: '{expr}'")
        except SyntaxError:
            print(f"Error: The expression '{expr}' is not mathematically correct.")
        except Exception as e:
            print(f"Error while evaluating '{expr}': {str(e)}")

        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the calculator")
            break

# Run it
calculator()