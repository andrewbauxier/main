def get_valid_string():
    """input validation to ensure the password entry is a number amd is between 8-30"""
    goodlength = False
    wholenumber = False
    while not goodlength and not wholenumber:
        string_input = input("How long is your string to be? (8-30): ")
        if string_input.isdigit():
            wholenumber = True
            string_input = int(string_input)
            if 8 <= string_input <= 30:
                print("Good string, program ends")
                goodlength = True
            else:
                print("Sorry, the string must be between 8 and 30 characters.\n")
        else:
            print("Sorry, the string must be a whole number.\n")
