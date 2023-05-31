import math

def calculate_right_circular_cylinder_volume():
    radius = get_cylinder_input("\nPlease enter the radius of the cylinder\n")
    height = get_cylinder_input("\nPlease enter the height of the cylinder\n")
    volume = calculate_volume(radius, height)
    print(f"The volume of the cylinder is: {volume:.2f} cubic units.")

def get_cylinder_input(prompt):
    while True:
        try:
            input_value = float(input(prompt))
            return input_value
        except ValueError:
            print("Sorry, the value entered must be an number")

def calculate_volume(radius, height):
    return math.pi * (radius*radius) * height

def exit_prompt():
    input("\nPress Enter to return to the main program.")
