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


def get_matrices():
    matrix = []
    print("Enter your 3x3 matrix:")
    for value in range(3):  # for look to iterate through list
        valid_row = False
        while not valid_row:
            print(f"Enter values for row {value + 1}:")
            row = input().strip().split()
            # strip takes whitespace off of front and end
            # split takes the line and seperates the line into values after each space so
            ## that one line is now three different numbers instead of one string of numbers
            if len(row) != 3:
                print("Sorry, you did not enter 3 numbers per row. Please try again.")
                continue
            try:
                row = [int(number) for number in row]
                # validates numbers and ensures whole numbers only
            except ValueError:
                print("Sorry, only whole numbers are allowed. Please try again.")
                continue
            valid_row = True
            matrix.append(row)
    print("Final matrix (for testing purposes):")
    for row in matrix:
        print(*row)
    return matrix


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
# test_matrices
get_matrices()
