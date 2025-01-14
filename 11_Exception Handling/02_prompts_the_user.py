"""
Write a function that prompts the user for a valid integer within a specified
range and handles invalid inputs gracefully with error messages.
"""

def get_valid_integer(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

number = get_valid_integer("Enter an integer (1-100): ", 1, 100)
print(f"You entered: {number}")