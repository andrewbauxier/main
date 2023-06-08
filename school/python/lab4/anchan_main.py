"""
Project Name:   Lab 4
Module Name:    main.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
# part 1
# enter and validate phone number and zip+4.

# user enters values of two 3x3 matrices
# select from options including addition, subtraction, matrix multiplication, and
#     element by element multiplication
#     should use numpy.matmul() for matrix multiplication (e.g. np.matmul(a, b) )
# program should:
#   compute the appropriate results
#   return the results and the transpose of the results, the mean of the rows for the results,
#       and the mean of the columns for the results
# steps
#   make skeletons for modules
#   make skeletons for functions
#   work on functions seperately
#   oh jeez
#
#
#
# import something
import anchan_get_stuff


def run_app():  #
    run_program = True
    while run_program:
        print("\nWelcome to the Python Matrix Application")
        play_game = input(
            "Do you want to play the Matrix Game?\nEnter 'y' for Yes or 'n' for No: "
        ).lower()
        if play_game == "n":
            run_program = False
        elif play_game == "y":
            phone_number = anchan_get_stuff.get_phone_number()
            zip_code = anchan_get_stuff.get_zip_code()
            print("\n", phone_number)
            print("\n", zip_code)


# def func1():  #
#     print()
#
#


# Start the program
run_app()
