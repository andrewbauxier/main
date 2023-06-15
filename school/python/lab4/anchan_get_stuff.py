"""
Project Name:   Lab 4
Module Name:    anchan_get_stuff.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import re
import numpy


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
    pattern = r"^\d{10}$"  # match 10 digits from the start (^) to end ($)
    if re.match(pattern, phone_number):
        return True


def valid_zip_code_entered(zip_code):
    pattern = r"\d{5}-\d{4}"
    if re.match(pattern, zip_code):
        return True


def get_operator():
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
