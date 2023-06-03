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

import anchanmatchcase


def main_menu_loop():  #
    """provides menu loop functionality so tt program continuously returns here after operation.
    input options are printed, option chosen is accepted then run through validation, then gets
    passed to the match-case
    """
    while True:
        anchanmatchcase.main_menu_loop()


# Start the program
main_menu_loop()
# anchanpassword.secure_password_generator()
# anchanpercentage.calculate_percentage()
# anchandaysuntil.calculate_days_until_july_4_2025()
# anchantriangle.calculate_triangle_leg()
# anchancylinder.calculate_right_circular_cylinder_volume()
