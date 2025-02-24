# Python Temp Converter

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
    entered_temp = get_float_input("Enter the current temperature: ")
    units = input("Is this in Fahrenheit or Celsius? (F or C): ").strip()

    if units.lower() == "q":
        print("Exiting calculator...")
        sys.exit()

    if units.lower() not in {'f', 'c'}:
        print(f'{units} is not a valid unit of measurement.')
        continue

    if units.lower() == "f":
        converted_temp = (entered_temp - 32.0) * (5/9)
        new_units = "C"
    else:
        converted_temp = (entered_temp * (9/5)) + 32
        new_units = 'F'

    print(f"Your entered temperature was {entered_temp} \u00B0{units.upper()}")
    print(f"The converted temperature is {round(converted_temp, 2)} \u00B0{new_units}")
    print("\nEnter 'Q' to exit or continue calculating...\n")