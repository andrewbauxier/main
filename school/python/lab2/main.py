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

def main_menu_loop(): #TODO break menu up into its own module, finish cylinder
    while True:
        print("\nWelcome to the Assorted Utility Program. Your options are as follows:\n")
        print("1: Secure Password Generation")
        print("2: Calculate and Format Percentages")
        print("3: Determine the number of Days until July 4, 2025")
        print("4: Calculate the leg of a triangle")
        print("5: Calculate the volume of a Right Circular Cylinder")
        print("6: Exit the program\n")
        menu_option_selected = get_menu_option_validation()
        utility_function_switcher(menu_option_selected)

def get_menu_option_validation():
    while True:
        menu_option_input = input("\nWhich option would you like to choose? \n")
        try:
            menu_option_input = int(menu_option_input)
            return menu_option_input
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.\n")

def utility_function_switcher(menu_option_selected):
    match menu_option_selected:
        case 1:
            anchanpassword.secure_password_generation()
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
        case _:
            print("\nInvalid option. Please choose a valid option.")


## Exit the program
def exit_program():
    sys.exit()
### functions end ###
# Start the program
main_menu_loop()
