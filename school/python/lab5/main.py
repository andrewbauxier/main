"""
Project Name:   Lab 5
Module Name:    Main.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    <Start here>
"""
import anchan_analyzer


def main():
    while True:
        print("***************** Welcome to the Python Data Analysis App**********")
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")
        choice = input()

        match choice:
            case "1":
                print("You have entered Population Data.")
                anchan_analyzer.analyze_population_data()
            case "2":
                print("You have entered Housing Data.")
                anchan_analyzer.analyze_housing_data()
            case "3":
                print(
                    "*************** Thanks for using the Data Analysis App**********"
                )
                break
            case _:
                print("That is not a valid choice, please try again.")


if __name__ == "__main__":
    main()
