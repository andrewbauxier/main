"""
Project Name:   
Module Name:    
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""

import matplotlib.pyplot as plot
from anchan_loader import load_population_data, load_housing_data


def calculate_statistics(column_data):
    """Calculates count, mean, standard deviation, minimum, and maximum values of a column."""
    count = column_data.count()
    mean = column_data.mean()
    std = column_data.std()
    minimum = column_data.min()
    maximum = column_data.max()
    return count, mean, std, minimum, maximum


def plot_histogram(column_data):
    """This function makes up the histogram"""
    plot.hist(column_data, bins="auto")
    plot.xlabel("Values")
    plot.ylabel("Frequency")
    plot.title("Histogram")
    plot.show()


def analyze_population_data():
    """This function analyzes population data by offering a menu for selecting and analyzing
    various columns."""
    pop_data = load_population_data()
    while True:  # provides menu functionality to insert choice
        print("Select the Column you want to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")

        column_choice = input()
        match column_choice:
            case "a":
                print("\nNow loading Pop Apr 1")
                column_data = pop_data["Pop Apr 1"]
                analyze_column(column_data)
            case "b":
                print("\nNow loading Pop Jul 1")
                column_data = pop_data["Pop Jul 1"]
                analyze_column(column_data)
            case "c":
                print("\nNow loading Change Pop")
                column_data = pop_data["Change Pop"]
                analyze_column(column_data)
            case "d":
                print("\nNow exiting the program. Goodbye.\n")
                break
            case _:
                input(
                    "\nInvalid choice. Please select a valid option. Press enter to try again\n"
                )


def analyze_housing_data():
    """This function oads dats columns from the CSV to present to the user and allows user to
    select data based on user input.
    """
    housing_data = load_housing_data()

    while True:
        print("Select the Column you want to analyze:")
        print("1. Age")
        print("2. Bedrooms")
        print("3. Built")
        print("4. Rooms")
        print("5. Utility")
        print("6. EXIT")

        column_choice = input()
        match column_choice:
            case "1":
                print("You selected Age")
                column_data = housing_data["AGE"]
                analyze_column(column_data)
            case "2":
                print("You selected 'Bedrooms'")
                column_data = housing_data["BEDRMS"]
                analyze_column(column_data)
            case "3":
                print("You selected Built")
                column_data = housing_data["BUILT"]
                analyze_column(column_data)
            case "4":
                print("You selected Rooms")
                column_data = housing_data["ROOMS"]
                analyze_column(column_data)
            case "5":
                print("You selected Utility")
                column_data = housing_data["UTILITY"]
                analyze_column(column_data)
            case "6":
                print("You selected to exit the menu. Goodbye")
                break
            case _:
                print("Invalid choice. Please select a valid option.")


def analyze_column(column_data):
    """Displays  data to user based on selection"""
    count, mean, std, minimum, maximum = calculate_statistics(column_data)
    print(f"Count = {count}")
    print(f"Mean = {mean}")
    print(f"Standard Deviation = {std}")
    print(f"Min = {minimum}")
    print(f"Max = {maximum}")
    plot_histogram(column_data)
