def get_valid_string():
    """input validation to ensure the string entere is a number and is between 8-30"""
    goodlength = False
    wholenumber = False
    while not goodlength or not wholenumber:
        string_input = input("\nHow long is your string to be? (8-30): ")
        if string_input.isdigit():
            wholenumber = True
            string_input = int(string_input)
            if 8 <= string_input <= 30:
                print("\nGood string, program ends")
                goodlength = True
            else:
                print("Sorry, the string must be between 8 and 30 characters.")
        else:
            print("Sorry, the string must be a whole number.")


get_valid_string()
