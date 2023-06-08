"""
Project Name:   Lab 4
Module Name:    main.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
# TODO: finish main desc
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
