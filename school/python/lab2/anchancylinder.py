"""This module takes in input, validates the input, passes it to a formula and then calculates
the volume of a right circular cylinder, then passes that back
"""
import math


def calculate_right_circular_cylinder_volume():
    """function prompts the user for radius and height of cylinder, calculates volume,
    and then displays the result. After displaying the result, prompts user to exit to
    main program.
    """
    radius = get_cylinder_input("\nPlease enter the radius of the cylinder\n")
    height = get_cylinder_input("\nPlease enter the height of the cylinder\n")
    volume = calculate_volume(radius, height)
    print(f"\nThe volume of the cylinder is: {volume:.2f} cubic units.")
    prompt_to_exit()


def get_cylinder_input(prompt_for_measurements):
    """Gets input and runs validation
    Args:
        prompt_for_measurements (str): prompt message and validation for above inputs.
    Returns:
        float: value entered by the user.
    """
    while True:
        try:
            input_value = float(input(prompt_for_measurements))
            return input_value
        except ValueError:
            print("Sorry, the value entered must be a number")


def calculate_volume(radius, height):
    """right circular cylinder formula. runs calcs.
    Args:
        radius (float)
        height (float)
    Returns:
        float
    """
    return math.pi * (radius * radius) * height


def prompt_to_exit():
    """exit function"""
    input("Press Enter to return to the main program.")
