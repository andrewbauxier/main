"""
Title:          Lab 1
Name:           Andrew Auxier
Course:         SDEV 300 6383 Building Secure Python Applications (2235)
Description:    

    This project serves a multitude of functions as listed: Generate a secure password,
    Calculate and Format a Percentage, determine number of Days until July 4, 2025, use the Law of
    Cosines to calculate the leg of a triangle, calculate the volume of a Right Circular Cylinder,
    and exit the program.
    
"""
import sys
import anchanpassword
import anchanpercentage
import anchandaysuntil
import anchantriangle
import anchancylinder


def main_menu_loop():  # TODO break menu up into its own module, finish cylinder
    """provides menu loop functionality so tt program continuously returns here after operation.
    input options are printed, option chosen is accepted then run through validation, then gets
    passed to the match-case
    """
    while True:
        print(
            "\nWelcome to the Assorted Utility Program. Your options are as follows:\n"
        )
        print("1: Secure Password Generation")
        print("2: Calculate and Format Percentages")
        print("3: Determine the number of Days until July 4, 2025")
        print("4: Calculate the leg of a triangle")
        print("5: Calculate the volume of a Right Circular Cylinder")
        print("6: Exit the program")
        menu_option_selected = get_menu_option_validation()
        utility_function_switcher(menu_option_selected)


def get_menu_option_validation():
    """provides validation for input from main menu loop. validation rules are: must be an integer
    between 1 and 6
    Returns:
        Integer: parameter returns as validated
    """
    while True:
        menu_option_input = input("\nWhich option would you like to choose? \n")
        if menu_option_input.isdigit():
            menu_option_input = int(menu_option_input)
            if menu_option_input > 1 and menu_option_input < 7:
                return menu_option_input
        else:
            print("\nInvalid input. Please enter a number between 1 and 6.")
            input("Press enter to try again.")
            break


def utility_function_switcher(menu_option_selected):
    match menu_option_selected:
        case 1:
            anchanpassword.secure_password_generator()
        case 2:
            anchanpercentage.calculate_percentage()
        case 3:
            anchandaysuntil.calculate_days_until_july_4_2025()
        case 4:
            anchantriangle.calculate_triangle_leg()
        case 5:
            anchancylinder.calculate_right_circular_cylinder_volume()
        case 6:
            exit_program()


## Exit the program
def exit_program():
    print("\nYou have chosen to exit the program. Goodbye!\n")
    sys.exit()


# Start the program
main_menu_loop()
