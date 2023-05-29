import math

def calculate_triangle_leg():
    print("\nYou have chosen to calculate the side of a triangle using the Law of Cosines.")
    side_a = get_positive_float("Enter the length of side A: ")
    side_b = get_positive_float("Enter the length of side B: ")
    angle_c = get_angle("Enter the measure of angle C in degrees: ")

    leg_c = math.sqrt(side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(math.radians(angle_c)))
    print(f"The length of leg C is: {leg_c:.3f}")
    input("\nPress Enter to return to the main menu\n")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")


def get_angle(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0 or value >= 180:
                raise ValueError("Angle must be between 0 and 180 degrees.")
            return value
        except ValueError:
            print("Invalid input. Please enter a valid angle between 0 and 180.")
