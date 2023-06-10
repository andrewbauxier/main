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
            continue
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
            continue
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


def generate_matrices(matrix_name):
    matrix = []
    print(f"\nPlease enter the values for {matrix_name} now.")
    print("Enters the values with the number, followed by a space. Like so: 1 2 3")
    print("Begin matrix:")
    for value in range(3):  # for look to iterate through list
        valid_row = False
        while not valid_row:
            print(f"Enter three values for row {value + 1}:\t")
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
    # print("Final matrix (for testing purposes):")
    # for row in matrix:
    #     print(*row)
    return matrix


def display_matrix(matrix_name, matrix):
    print(f"{matrix_name} ")
    for row in matrix:
        print(*row)
        # the * in this is iteral unpacking. it unpacks the values and print thems with whitespace
        ## without it, each row would print like this [1, 1, 1] instead of 1 1 1
    return matrix


def test_matrix_generation():
    matrix_1 = generate_matrices("Matrix 1")
    matrix_2 = generate_matrices("Matrix 2")
    display_matrix(matrix_1, "Matrix 1:\n")
    display_matrix(matrix_2, "Matrix 2:\n")


#
# generate_matrices("Matrix 1")
# generate_matrices("Matrix 2")
# display_matrix("Matrix 1:\n", matrix_1)
# display_matrix("Matrix 2:\n", matrix_2)
# test_matrix_generation()
