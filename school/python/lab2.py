"""
Title:          Lab 1
Name:           Andrew Auxier
Course:         SDEV 300 6383 Building Secure Python Applications (2235)
Description:    This project serves a multitude of functions as listed: Generate a secure password,\
    Calculate and Format a Percentage, determine number of Days until July 4, 2025, use the Law of \
    Cosines to calculate the leg of a triangle, calculate the volume of a Right Circular Cylinder, \
    and exit the program.
    
"""
import sys
import string
import secrets

def main_menu_loop():
    while True:
        print("Welcome to the Assorted Utility Program. Your options are as follows:\n")
        print("1: Secure Password Generation")
        print("2: Calculate and Format a Percentage")
        print("3: Determine the number of Days until July 4, 2025")
        print("4: Calculate the leg of a triangle")
        print("5: Calculate the volume of a Right Circular Cylinder")
        print("6: Exit the program\n")
        menu_option_selected = get_menu_option_validation()
        utility_function_switcher(menu_option_selected)

def get_menu_option_validation():
    while True:
        menu_option = input("\nWhich option would you like to choose? \n")
        try:
            menu_option = int(menu_option)
            return menu_option
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.\n")

def utility_function_switcher(menu_option_selected):
    match menu_option_selected:
        case 1:
            secure_password_generation()
        case 2:
            calculate_and_format_percentage()
        case 3:
            calculate_days_until_july_4_2025()
        case 4:
            calculate_triangle_leg()
        case 5:
            calculate_right_circular_cylinder_volume()
        case 6:
            exit_program()
        case _:
            print("\nInvalid option. Please choose a valid option.\n")

def secure_password_generation():
    print("\nYou have chosen the secure password generator.")
    print("Passwords must be between 8 and 30 characters long.\n")

    password_length = get_valid_password_length()
    character_pool = get_character_pool()

    if not character_pool:
        print("\nPlease select at least one option for password generation.\n")
        return

    password = generate_password(character_pool, password_length)
    print("\nYour generated password is:", password)


def get_character_pool():
    prompt_message_include_uppercase = get_yes_no_input("Include uppercase letters? (y/n):\t")
    prompt_message_lowercase = get_yes_no_input("Include lowercase letters? (y/n): \t")
    prompt_message_symbols = get_yes_no_input("Include special symbols? (y/n): \t")
    prompt_message_numbers = get_yes_no_input("Include numbers? (y/n): \t")

    return build_character_pool(prompt_message_include_uppercase, prompt_message_lowercase,
        prompt_message_numbers, prompt_message_symbols
    )


def get_valid_password_length():
    while True:
        try:
            password_length = int(input("How long would you like the password to be? (8-30): "))
            if 8 <= password_length <= 30:
                return password_length
            else:
                print("Sorry, the password must be between 8 and 30 characters.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_yes_no_input(prompt_messages):
    while True:
        user_input = input(prompt_messages).lower()
        if user_input == "y" or user_input == "n":
            return user_input
        print("Invalid input detected. Please enter 'y' or 'n' only.")

def build_character_pool(include_uppercase, include_lowercase, include_symbols, include_numbers):
    character_pool = ''
    if include_uppercase == 'y':
        character_pool += string.ascii_uppercase
    if include_lowercase == 'y':
        character_pool += string.ascii_lowercase
    if include_symbols == 'y':
        character_pool += string.punctuation
    if include_numbers == 'y':
        character_pool += string.digits
    return character_pool

def generate_password(character_pool, password_length):
    return ''.join(secrets.choice(character_pool) for _ in range(password_length))


## Calculate and format a percentage
def get_valid_input(prompt, data_type=int, min_value=None):
    while True:
        try:
            user_input = data_type(input(prompt))
            if min_value is not None and user_input < min_value:
                raise ValueError
            return user_input
        except ValueError:
            print("\nOopsie Poopsie! Invalid input. Please try again.")

def calculate_percentage(numerator, denominator, decimal_points):
    percentage = (numerator / denominator) * 100
    formatted_percentage = f"{percentage:.{decimal_points}f}"
    return formatted_percentage

def calculate_and_format_percentage():
    numerator = get_valid_input("\nPlease enter the numerator: ", min_value=1)
    denominator = get_valid_input("\nPlease enter the denominator: ", min_value=1)
    decimal_points = get_valid_input("\nPlease enter the number of decimal points: ", min_value=0)

    formatted_percentage = calculate_percentage(numerator, denominator, decimal_points)

    print(f"The calculated percentage is: {formatted_percentage}%\n")





## Calculate the number of days until July 4, 2025
def calculate_days_until_july_4_2025():
    print("Hellow World\n")
## Use the Law of Cosines to calculate the leg of a triangle
def calculate_triangle_leg():
    print("Hellow World\n")
## Calculate the volume of a Right Circular Cylinder
def calculate_right_circular_cylinder_volume():
    print("Hellow World\n")

## Exit the program
def exit_program():
    sys.exit()
### functions end ###
# Start the program
main_menu_loop()
secure_password_generation()
calculate_and_format_percentage()
