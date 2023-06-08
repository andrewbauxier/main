"""
Project Name:   Lab 4
Module Name:    anchan_get_stuff.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import re


def run_module():
    print("\n", get_phone_number())
    print("\n", get_zip_code())


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
            "Ensure you enter the number with NO HYPHENS"
        )


def get_zip_code():  #
    zip_code = input(
        "\nPlease enter your zip code in this format: 12345-6789"
        "\nEnsure you ENTER THE HYPHEN as well. Please try again now.\n"
    )
    if valid_zip_code_entered(zip_code):
        return zip_code
    else:
        print(
            "Your zip code was not entered correctly. This is the correct format:"
            "\n12345-6789"
            "\nEnsure you ENTER THE HYPHEN as well. Please try again now.\n"
        )


def valid_phone_number_entered(phone_number):
    pattern = r"\d{10}"
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def valid_zip_code_entered(zip_code):
    pattern = r"\d{5}-\d{4}"
    if re.match(pattern, zip_code):
        return True
    else:
        return False


# def func5():  #
#     print()
#
#

# Start the program
run_module()
