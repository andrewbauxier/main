"""
Project Name:   
Module Name:    
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from anchan_loader import load_population_data, load_housing_data


def calculate_statistics(column_data):
    count = column_data.count()
    mean = column_data.mean()
    std = column_data.std()
    minimum = column_data.min()
    maximum = column_data.max()
    return count, mean, std, minimum, maximum


def plot_histogram(column_data):
    plt.hist(column_data, bins="auto")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()


def analyze_population_data():
    pop_data = load_population_data()

    while True:
        print("Select the Column you want to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")

        column_choice = input()

        if column_choice == "a":
            print("You selected Pop Apr 1")
            column_data = pop_data["Pop Apr 1"]
            analyze_column(column_data)
        elif column_choice == "b":
            print("You selected Pop Jul 1")
            column_data = pop_data["Pop Jul 1"]
            analyze_column(column_data)
        elif column_choice == "c":
            print("You selected Change Pop")
            column_data = pop_data["Change Pop"]
            analyze_column(column_data)
        elif column_choice == "d":
            print("You selected to exit the column menu")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def analyze_housing_data():
    housing_data = load_housing_data()

    while True:
        print("Select the Column you want to analyze:")
        print("a. AGE")
        print("b. BEDRMS")
        print("c. BUILT")
        print("d. ROOMS")
        print("e. UTILITY")
        print("f. Exit Column")

        column_choice = input()

        if column_choice == "a":
            print("You selected AGE")
            column_data = housing_data["AGE"]
            analyze_column(column_data)
        elif column_choice == "b":
            print("You selected BEDRMS")
            column_data = housing_data["BEDRMS"]
            analyze_column(column_data)
        elif column_choice == "c":
            print("You selected BUILT")
            column_data = housing_data["BUILT"]
            analyze_column(column_data)
        elif column_choice == "d":
            print("You selected ROOMS")
            column_data = housing_data["ROOMS"]
            analyze_column(column_data)
        elif column_choice == "e":
            print("You selected UTILITY")
            column_data = housing_data["UTILITY"]
            analyze_column(column_data)
        elif column_choice == "f":
            print("You selected to exit the column menu")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def analyze_column(column_data):
    count, mean, std, minimum, maximum = calculate_statistics(column_data)
    print(f"Count = {count}")
    print(f"Mean = {mean}")
    print(f"Standard Deviation = {std}")
    print(f"Min = {minimum}")
    print(f"Max = {maximum}")
    plot_histogram(column_data)
