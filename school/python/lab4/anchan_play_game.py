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


def run_program():
    phone_number = anchan_get_stuff.get_phone_number()
    zip_code = anchan_get_stuff.get_zip_code()
    # anchan_display.display_phone_and_zip(phone_number, zip_code) - # when display is ready
    display_phone_and_zip(phone_number, zip_code)  # to display when we are ready
    run_matrices()


def run_matrices():
    matrix_1 = anchan_get_stuff.generate_matrices("Matrix 1")
    matrix_2 = anchan_get_stuff.generate_matrices("Matrix 2")
    print("\nYour matrices are:")
    anchan_get_stuff.display_matrix("Matrix 1:", matrix_1)
    anchan_get_stuff.display_matrix("Matrix 2:", matrix_2)


def display_phone_and_zip(phone_number, zip_code):  # to display when we are ready
    print("\nYou have successfully enter your Phone Number and Zip Code:")
    print("Phone Number:\t", phone_number)
    print("Zip Code:\t", zip_code)
    print(input("Press ENTER to continue...\t"))


# def func1():  #
#     print()


# def func2():  #
#     print()


# def func3():  #
#     print()


# def func4():  #
#     print()


# def func5():  #
#     print()


# Testing
# run_program()
# run_matrices()
