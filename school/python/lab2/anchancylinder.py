import math

def calculate_right_circular_cylinder_volume():
    radius = get_cylinder_input("\nPlease enter the radius of the cylinder\n")
    height = get_cylinder_input("\nPlease enter the height of the cylinder\n")
    volume = calculate_volume(radius, height)
    print(f"\nThe volume of the cylinder is: {volume:.2f} cubic units.")
    prompt_to_exit()


def get_cylinder_input(prompt_for_measurements):
    while True:
        try:
            input_value = float(input(prompt_for_measurements))
            return input_value
        except ValueError:
            print("Sorry, the value entered must be an number")

def calculate_volume(radius, height):
    return math.pi * (radius*radius) * height

def prompt_to_exit():
    input("Press Enter to return to the main program.")
