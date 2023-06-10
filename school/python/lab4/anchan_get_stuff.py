"""
Project Name:   Lab 4
Module Name:    anchan_get_stuff.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import re


def get_phone_number():  # receive input and loop until validation
    while True:
        phone_number = input(
            "\nPlease enter your phone number in this format: 1234567890"
            "\nOnly digits are allowed, no other characters. DO NOT ENTER HYPHENS.\t"
        )
        if not valid_phone_number_entered(phone_number):
            print("\nYour phone number was not entered correctly.")
            print("\nEnsure you enter the number with NO HYPHENS.")
        return phone_number


def get_zip_code():  # receive input and loop until validation
    while True:
        zip_code = input(
            "\nPlease enter your zip code in this format: 12345-6789"
            "\nEnsure you ENTER THE HYPHEN as well. Please try again now.\t"
        )
        if not valid_zip_code_entered(zip_code):
            print("\nYour zip code was not entered correctly.")
            print("\nPlease ensure you ENTER THE HYPHEN as well.")
        return zip_code


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


def test_module():
    phone_number = get_phone_number()
    zip_code = get_zip_code()
    print("\n the phone number is", phone_number, "\n the zipe code is")
    print("\n", zip_code, "\n")


# def func5():  #
#     print()
#
#
# test_module()
