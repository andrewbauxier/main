"""
Project Name:   Lab 3
Module Name:    main.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
    
    Display all U.S. states in alphabetical order along with their capital, state population, and 
    state flower.
    
    Search for a specific state and display the name of its capital, the size of the state's 
    population, and an image of the State Flower.
    
    Provide a bar graph of the top 5 populated states showing their overall population.
    
    Update the overall state population for a specific state.
    
"""
import anchan_match_case


def main_menu_loop():  #
    """provides menu loop functionality so the program continuously returns here after operation.
    input options are printed, option chosen is accepted then run through validation, then gets
    passed to the match-case
    """
    while True:
        anchan_match_case.main_menu_loop()


# Start the program
main_menu_loop()
