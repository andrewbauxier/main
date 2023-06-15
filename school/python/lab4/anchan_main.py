"""
Project Name:   Lab 4
Module Name:    main.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below: 
    
    Get a phone number and zip code from the user and validate that they are in the correct
        phone number format and length
    Gather input from the user to generate matrices and then use those matrices to perform addition,
        subtraction, multiplication in whole, and multiplcation by element operations on the 
        matrices
    Print the results of the calculations, the transpose, and mean of the resulting matrix
    
        
"""
import anchan_play_game


def run_app():
    """this function runs the main program. it prompts the user to play the game or no, and if no,
    gracefully exits
    """
    # starts the program. yes plays game, no kills program
    run_program = True
    while run_program:
        print("\nWelcome to the Python Matrix Application")
        play_game = input(
            "Do you want to play the Matrix Game?\nEnter 'y' for Yes or 'n' for No: "
        ).lower()
        if play_game == "n":
            print("\nHave a good day!\n")
            run_program = False
        elif play_game == "y":
            anchan_play_game.run_program()
        else:
            print("\nSorry, only 'y' and 'n' is allowed. Please try again.")
            input("\nPress ENTER to continue...")


# Start the program
run_app()
