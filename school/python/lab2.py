"""
Title:          Lab 1
Name:           Andrew Auxier
Course:         SDEV 300 6383 Building Secure Python Applications (2235)
Description:    This project serves a multitude of functions as listed: Generate a secure password,\
    Calculate and Format a Percentage, determine number of Days until July 4, 2025, use the Law of \
    Cosines to calculate the leg of a triangle, calculate the volume of a Right Circular Cylinder, \
    and exit the program.
    
"""
import sys
## menu loop to receive user input
def main_menu_loop():
    """Create a main menu loop to receive user input and direct traffic    
    """
    while True:
        print("Welcome to the Assorted Utility Program. You options are as follows: \n")
        print("1: Secure Password Generation\n2:Calculate and Format a Percentage\n \
            3: Determine the number of Days until July 4, 2025\n4: Calculate the leg of a triangle \
            \n5: Calculate the volume of a Right Circular Cylinder\n6: Exit the program\n")
        traffic_signal = int(input("Which option would you like to choose?"))
## switch case to direct traffic
def traffic_cop(traffic_signal):
    match traffic_signal:
        case 1:
            secure_password_generation()
## Generate a secure password
def secure_password_generation():    
    print("Hellow World\n")
## Calculate and Format a Percentage
def calculate_format_percentage():
    print("Hellow World\n")
## Determine number of Days until July 4, 2025
def Determine_days_until_date_2025_07_04():
    print("Hellow World\n")
## Use the Law of Cosines to calculate the leg of a triangle
def calculate_leg_of_triangle():
    print("Hellow World\n")
## Calculate the volume of a Right Circular Cylinder
def calculate_right_circular_cylinder_volume():
    print("Hellow World\n")

## Exit the program
    sys.exit()
### functions end ###

main_menu_loop()
