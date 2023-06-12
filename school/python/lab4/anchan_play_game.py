"""
Project Name:   Lab 4
Module Name:    anchan_play_game.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import anchan_get_stuff

# import anchan_display


def run_zip_and_code():
    phone_number = anchan_get_stuff.get_phone_number()
    zip_code = anchan_get_stuff.get_zip_code()
    # anchan_display.display_phone_and_zip(phone_number, zip_code) - # when display is ready
    display_phone_and_zip(phone_number, zip_code)  # to display when we are ready


def run_matrix_operations():
    matrix_1 = anchan_get_stuff.generate_matrices("Matrix 1")
    matrix_2 = anchan_get_stuff.generate_matrices("Matrix 2")
    # the above functions run matrix creation and assign them to variables
    print("\nYour matrices are:")
    anchan_get_stuff.display_matrix("Matrix 1:", matrix_1)
    anchan_get_stuff.display_matrix("Matrix 2:", matrix_2)
    print(input("\nPress ENTER to continue...\t"))
    run_matrix_calculations(matrix_1, matrix_2)
    # this function takes the matrixes and runs them through a calculation such as
    # addition or multiplication


def run_matrix_calculations(matrix_1, matrix_2):
    operator = anchan_get_stuff.get_operator()
    matrix_results = anchan_get_stuff.get_calculation(matrix_1, matrix_2, operator)
    print_results(matrix_results)


def display_phone_and_zip(phone_number, zip_code):  # to display when we are ready
    print("\nYou have successfully enter your Phone Number and Zip Code:")
    print("Phone Number:\t", phone_number)
    print("Zip Code:\t", zip_code)
    print(input("Press ENTER to continue...\t"))


def print_results(matrix_results):
    print("The results are:\n")
    for row in matrix_results:
        print(" ".join(str(number) for number in row))
        # 'join'() is a map function. join combines everything into one string. the str portion
        # takes the original datatype and turns it into a string. the " " portion adds spaces
        # between the items. str is a builtin function and is applying the argument to the
        # numbers. altogether...
        # (" ".join(str(number) for number in row)
        # ==
        # apply str to number for each number in the row and and join the strings with a space
        # between them.
        # it does this so it can print the matrix correctly with little fuss.
    print(input("\nPress ENTER to continue...\t"))


# Testing
# run_program()
# run_matrix_operations()
