"""
Project Name:   Lab 3
Module Name:    anchan_state_display_all.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module:
    
    provides a simple function to display all entries in the custom dictionary us_states_dictionary
    located in the custom made anchan_state_database.py module
    
"""
from time import sleep
from anchan_state_database import us_states_dictionary


def run_program():  # pretty self-explanatory
    """Very simple function to display all the values in the dictionary"""
    print("\nHere is a list of all the US states:\n")
    for state, state_data_item in us_states_dictionary.items():  # access dict items
        print(state.title())
        print("Capital:", state_data_item["capital"])
        print("Population:", state_data_item["population"])
        print("Flower:", state_data_item["flower"])
        print()  # formatting
        sleep(0.25)  # formatting
