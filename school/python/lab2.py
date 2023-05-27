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
## menu loop to receive user input
def main_menu_loop():
    """Create a main menu loop to receive user input and direct traffic    
    """
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

#menu option validation
def get_menu_option_validation():
    while True:
        menu_option = input("Which option would you like to choose? ")
        try:
            menu_option = int(menu_option)
            return menu_option
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
# switch case to direct traffic
def utility_function_switcher(menu_option_selected):
    match menu_option_selected:
        case 1:
            secure_password_generation()
        case 2:
            calculate_format_percentage()
        case 3:
            calculate_days_until_july_4_2025()
        case 4:
            calculate_triangle_leg()
        case 5:
            calculate_right_circular_cylinder_volume()
        case 6:
            exit_program()
        case _:
            print("Invalid option. Please choose a valid option.\n")
## Generate a secure password
def secure_password_generation():
    print("\nYou have chosen the secure password generator.\n"
          "Be advised, passwords will only be generated for up to 30 characters.\n"
          "In the event that you enter invalid input, the program will enforce valid entry.")

    password_length = get_valid_password_length()
    include_uppercase = get_yes_no_input("Include uppercase letters? (y/n): ")
    include_lowercase = get_yes_no_input("Include lowercase letters? (y/n): ")
    include_symbols = get_yes_no_input("Include special symbols? (y/n): ")
    include_numbers = get_yes_no_input("Include numbers? (y/n): ")

    character_pool = build_character_pool(include_uppercase, include_lowercase, include_symbols, include_numbers)
    if not character_pool:
        print("Please select at least one option for password generation.")
        return

    password = generate_password(character_pool, password_length)
    print("\nYour generated password is:", password, "\n")


def get_valid_password_length():
    while True:
        try:
            password_length = int(input("How long would you like the password to be?\n"
                                        "Please enter a number now: \n"))
            while password_length > 30:
                print("Sorry, the password can only be up to 30 characters.")
                password_length = int(input("Please enter a number now: \n"))
            return password_length
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
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
def calculate_format_percentage():
    print("Hellow World\n")
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

main_menu_loop()
