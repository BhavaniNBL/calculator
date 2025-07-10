import re

def is_valid_expression(expr):
    allowed = "0123456789+-*/(). "

    # Check for unsupported characters
    for char in expr:
        if char not in allowed:
            return False, f"Invalid input: '{expr}' contains unsupported character: '{char}'\nPlease use only digits, +, -, *, /, (, ), and spaces."

    # Check that no number in the expression is longer than 9 digits
    numbers = re.findall(r'\d+', expr)
    for number in numbers:
        if len(number) > 9:
            return False, f"Invalid input: number '{number}' exceeds 9 digits. The number should be 9 or less than 9 digits in length"

    return True, ""


def calculator():
    print("Welcome to the Smart Python Calculator!")
    print("You can use numbers and operators: +  -  *  /  ( )")
    print("Each number must be 9 digits or fewer.")
    print("Example: (3 + 5) * 2 / 4")
    print("Do NOT use alphabets or symbols like $, &, %, etc.")

    while True:
        expr = input("\nEnter your math expression: ").strip()

        if not expr:
            print("You didn't type anything. Please enter a math expression like 2 + 3 * 4")
            continue

        # Validate input and get specific error message if any
        is_valid, error_msg = is_valid_expression(expr)
        if not is_valid:
            print(error_msg)
            continue

        # Safe to evaluate now
        try:
            result = eval(expr)
            print(f"Result of '{expr}' is: {result}")
        except ZeroDivisionError:
            print(f"Error: Division by zero in expression: '{expr}'")
        except SyntaxError:
            print(f"Error: The expression '{expr}' looks incomplete or broken.")
            print("Try something like '5 + 2' or '3 * (2 + 1)'")
        except TypeError as e:
            if "'int' object is not callable" in str(e):
                print(f"Oops! You're using a number like a function in '{expr}'.")
                print("Did you mean to multiply? Try: (3) * (3) instead of (3)(3)")
            else:
                print(f"Type Error: {e}")
        except Exception as e:
            print(f"Error while evaluating '{expr}': {str(e)}")

        again = input("\n Do you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the calculator!")
            break

# Run the calculator
calculator()
