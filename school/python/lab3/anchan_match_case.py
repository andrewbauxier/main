"""
Project Name:   Lab 3
Module Name:    anchan_match_case.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module:
    
    Provides main menu prompt, main menu validation, match-case functionality to direct traffic
    flow for user input, and an exit program action.
    
"""
import sys
import anchan_state_functionality
import anchan_state_display_all
import anchan_popsort
import anchan_change_pop


def main_menu_loop():
    print("\nWelcome to Anchan's State Database. Here are your options\n")
    print(
        "1. Display all U.S. states in alphabetical order along with their capital, "
        "state population, and state flower"
    )
    print(
        "2. Search for a specific state and display the name of its capital, "
        "the size of the state's population, and an image of the State Flower."
    )
    print(
        "3. Provide a bar graph of the top 5 populated states showing their"
        "overall population."
    )
    print("4. Update the overall state population for a specific state.")
    print("5: Exit the program")
    menu_option_selected = get_menu_option_validation()  # feed to validation function
    utility_function_switcher(menu_option_selected)  # feed to traffic control


def get_menu_option_validation():  # validation function
    """provides validation for input import main menu loop. validation rules are: must be an integer
    between 1 and 6
    Returns:
        Integer: parameter returns as validated
    """
    while True:
        menu_option_input = input("\nWhich option would you like to choose? \n")
        if menu_option_input.isdigit():
            menu_option_input = int(menu_option_input)
            if menu_option_input >= 1 and menu_option_input <= 5:
                return menu_option_input
            else:
                print("\nInvalid input. Please enter a number between 1 and 6.")
                input("Press enter to try again.")
                break
        else:
            print("\nInvalid input. Please enter a number between 1 and 6.")
            input("Press enter to try again.")
            break


def utility_function_switcher(menu_option_selected):  # traffic control
    """match-case for input to direct traffic to approprate modules and functions
    Args:
        menu_option_selected (int)
    """
    match menu_option_selected:
        case 1:
            anchan_state_display_all.run_program()
        case 2:
            anchan_state_functionality.run_program()
        case 3:
            anchan_popsort.run_program()
            # anchan_state_database.start()
        case 4:
            anchan_change_pop.run_program()
            # anchan_state_database.start()
        case 5:
            exit_program()


## Exit the program
def exit_program():
    """exit function"""
    print("\nYou have chosen to exit the program. Goodbye!\n")
    sys.exit()
