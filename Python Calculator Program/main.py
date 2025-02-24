import sys


def get_float_input(prompt):
    """Prompt user until they enter a valid float, or exit if they enter 'Q'."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "q":
            print("Exiting calculator...")
            sys.exit()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
    print("\nEnter 'Q' at any time to exit.")

    operator = input("Enter an operator (+ - * /): ").strip()

    if operator.lower() == "q":
        print("Exiting calculator...")
        sys.exit()

    if operator not in {"+", "-", "*", "/"}:
        print(f"{operator} is not a valid operator.")
        continue

    num1 = get_float_input("Enter the 1st number: ")
    num2 = get_float_input("Enter the 2nd number: ")

    if operator == "/" and num2 == 0:
        print("Cannot divide by zero. Please enter a new number.")
        continue

    result = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }[operator]

    print("Result:", round(result, 3))
    print("\nEnter 'Q' to exit or continue calculating...\n")
