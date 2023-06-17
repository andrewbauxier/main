"""
Project Name:   Lab 4
Module Name:    anchan_get_stuff.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module contains functions related to user input validation and operator selection for 
    the project. It provides functions to validate phone numbers and zip codes, retrieve 
    the operator for matrix calculations, and perform the matrix calculations based on the 
    selected operator.
"""
import re
import numpy


def get_phone_number():  # receive input and loop until validation
    """prompts the user to enter a phone number and validates it. returns the validated phone
    number.

    Returns:
        int: validated phone number
    """
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
    """prompts the user to enter a zip code and validates it, returns the validated zip code.

    Returns:
        int: validated zip code
    """
    while True:
        zip_code = input("\nPlease enter your zip code in this format: 12345-6789\t")
        if not valid_zip_code_entered(zip_code):
            print("\nYour zip code was not entered correctly. ")
            print("Ensure you ENTER THE HYPHEN as well.")
            continue
        return zip_code


def valid_phone_number_entered(phone_number):
    """validates the entered phone number using a regular expression pattern, returns true if
    the phone number is valid, otherwise false.

      Args:
        phone_number (int): phone number passed for validation

      Returns:
        boolean: validates the phone number, true if good false if not
    """
    pattern = r"^\d{10}$"  # match 10 digits from the start (^) to end ($)
    return bool(re.match(pattern, phone_number))


def valid_zip_code_entered(zip_code):
    """validates the entered zip code using a regular expression pattern, returns true if the zip
    code is valid, otherwise false.

    Args:
        zip_code int: zip code input for validation

    Returns:
        boolean: validates the phone number, true if good false if not
    """
    pattern = r"\d{5}-\d{4}"
    return bool(re.match(pattern, zip_code))


def get_operator():
    """prompts the user to choose an operator for matrix calculations, validates the input, and
    returns the selected operator as an integer.

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    operator_validation = True
    while operator_validation:
        print(
            "\nChoose an operator to run the calculations with. Pick a number from this list:"
        )
        print("1: Addition")
        print("2: Subtraction")
        print("3: Matrix Multiplication")
        print("4: Element by Element Multiplication")
        try:
            operator = int(input("\nChoose the number now.\t"))
            if operator < 1 or operator > 4:
                raise ValueError
            operator_validation = False
        except ValueError:
            input("\nThat is not an acceptable answer, press enter to try again.")
    return operator


def get_calculation(matrix_1, matrix_2, operator):
    """performs matrix calculations based on the selected operator, returns the resulting matrix.

    Args:
        matrix_1 (numpy list): generated matrix from user input
        matrix_2 (numpy list): generated matrix from user input
        operator: operator chosen by user input

    Returns:
        matrix_results (numpy list): generated matrix from calculations ran by machine
    """
    match operator:
        case 1:
            matrix_results = numpy.add(matrix_1, matrix_2)
        case 2:
            matrix_results = numpy.subtract(matrix_1, matrix_2)
        case 3:
            matrix_results = numpy.matmul(matrix_1, matrix_2)
        case 4:
            matrix_results = numpy.multiply(matrix_1, matrix_2)
    return matrix_results


#
# generate_matrices("Matrix 1")
# generate_matrices("Matrix 2")
# display_matrix("Matrix 1:\n", matrix_1)
# display_matrix("Matrix 2:\n", matrix_2)
# test_matrix_generation()
