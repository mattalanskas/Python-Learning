# Python Weight Converter

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


print("\nEnter 'Q' at any time to exit.")
while True:

    units = input("Kilograms or Pounds? (K or L): ").strip()

    if units.lower() == "q":
        print("Exiting calculator...")
        sys.exit()

    if units.lower() not in {'k', 'l'}:
        print(f'{units} is not a valid unit of measurements.')
        continue

    entered_weight = get_float_input("Enter your weight: ")

    if units.lower() == "k":
        units = "Kilograms"
        converted_weight = entered_weight * 2.20462
        new_units = "Pounds"
    else:
        units = "Pounds"
        converted_weight = entered_weight * 0.453592
        new_units = 'Kilograms'

    print(f"Your entered weight was {entered_weight} {units}")
    print(f"Your weight in {new_units} is {round(converted_weight, 3)}")
    print("\nEnter 'Q' to exit or continue calculating...\n")
