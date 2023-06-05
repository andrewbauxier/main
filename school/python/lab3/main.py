"""
Title:          Lab 3
Name:           Andrew Auxier
Course:         SDEV 300 6383 Building Secure Python Applications (2235)
Description:    

    This project serves a multitude of functions as listed: 
    
"""
# TODO: finish module description
import anchanmatchcase


def main_menu_loop():  #
    """provides menu loop functionality so the program continuously returns here after operation.
    input options are printed, option chosen is accepted then run through validation, then gets
    passed to the match-case
    """
    while True:
        anchanmatchcase.main_menu_loop()


# Start the program
main_menu_loop()
