import string
import secrets

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
    input("\nPress Enter to return to the main program.")

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
