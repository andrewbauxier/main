"""This module takes in input, validates the input, builds a character pool from said
input, then assigns the character pool to a formula that then generates a secure, complex 
password
"""
import string
import secrets


def get_yes_no_input(prompt_messages):
    """input validation for 'y' or 'n'"""
    while True:
        user_input = input(prompt_messages).lower()
        if user_input == "y" or user_input == "n":
            return user_input
        print("Invalid input detected. Please enter 'y' or 'n' only.")


def get_valid_password_length():
    """input validation to ensure the password entry is a number amd is between 8-30"""
    while True:
        password_length = input("How long would you like the password to be? (8-30): ")
        if password_length.isdigit():
            password_length = int(password_length)
            if 8 <= password_length <= 30:
                return password_length
            else:
                print("Sorry, the password must be between 8 and 30 characters.\n")
        else:
            print("Sorry, the password must be a whole number.\n")


def get_character_pool():
    """gets and validates input to build character pool"""
    prompt_message_include_uppercase = get_yes_no_input(
        "Do you want to include uppercase letters? (y/n):\t"
    )
    prompt_message_lowercase = get_yes_no_input(
        "Do you want to include lowercase letters? (y/n): \t"
    )
    prompt_message_symbols = get_yes_no_input(
        "Do you want to include special symbols? (y/n): \t\t"
    )
    prompt_message_numbers = get_yes_no_input(
        "Do you want to include numbers? (y/n): \t\t\t"
    )
    # there's a more elegant solution to the tabs but it's a lot of work and not a requirement
    # TODO: do the work later
    return build_character_pool(
        prompt_message_include_uppercase,
        prompt_message_lowercase,
        prompt_message_numbers,
        prompt_message_symbols,
    )


def build_character_pool(
    include_uppercase, include_lowercase, include_symbols, include_numbers
):
    """uses input from previous function to build character pool for special characters to
    increase password complexity then sends it back"""
    character_pool = ""
    if include_uppercase == "y":
        character_pool += string.ascii_uppercase
    if include_lowercase == "y":
        character_pool += string.ascii_lowercase
    if include_symbols == "y":
        character_pool += string.punctuation
    if include_numbers == "y":
        character_pool += string.digits
    return character_pool


def generate_password(character_pool, password_length):
    """actually makes the password based on secrets module imported voodo then pastes it together
    and spits it back out to the user
    """
    return "".join(secrets.choice(character_pool) for _ in range(password_length))


def secure_password_generator():
    """enter and exit message input getter and giver"""
    print("\nYou have chosen the secure password generator.")
    print("Passwords must be between 8 and 30 characters long.\n")
    password_length = get_valid_password_length()
    character_pool = get_character_pool()
    if not character_pool:
        print("\nPlease select at least one option for password generation.\n")
        return
    password = generate_password(character_pool, password_length)
    print("\nYour generated password is:", password)
    input("\nPress Enter to return to the main program.")
    # this looks so sloppy for some reason. too complex?
