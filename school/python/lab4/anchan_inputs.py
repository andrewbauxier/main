"""
Project Name:   Lab 4
Module Name:    anchan_inputs.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
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
            print("\n")


# def func1():  #
#     print()
#
#


# Start the program
run_app()
