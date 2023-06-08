"""
Project Name:   Lab 4
Module Name:    anchan_get_stuff.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
# import something


def get_phone_number():  #
    phone_number = input(
        "\nPlease enter your phone number in this format: 1234567890"
        "\nOnly digits are allowed, no other characters. DO NOT ENTER HYPHENS."
    )
    if valid_phone_number_entered(phone_number):
        return phone_number
    else:
        print(
            "Your phone number was not entered correctly. This is the correct format:"
            "1234567890"
            "Ensure you enter the number with no hyphens"
        )


def get_zip_code():  #
    if valid_zip_code_entered(zip_code):
        return zip_code
    else:
        print(
            "Your zip code was not entered correctly. This is the correct format:"
            "\n12345-6789"
            "\nEnsure you enter the hypen as well. Please try again now.\n"
        )

def valid_phone_number_entered(phone_number):
    


def valid_zip_code_entered(zip_code):
    
    
    
    
# def func5():  #
#     print()
#
#

# Start the program
func1()
