"""
Project Name:   Lab 4
Module Name:    anchan_play_game.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import anchan_get_stuff


def run_program():
    phone_number = anchan_get_stuff.get_phone_number()
    zip_code = anchan_get_stuff.get_zip_code()
    print("\n", phone_number)
    print("\n", zip_code)
    play_game()


def play_game():
    print(f"Please enter the values for {matrix_name} now.")
    print("Enters the values with the number, followed by a space. Like so: 1 2 3")
    matrix_1 = anchan_get_stuff.get_matrices()
    print(matrix_1)


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


# Start the program
run_program()
