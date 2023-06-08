"""
Project Name:   Lab 3
Module Name:    anchan_change_pop.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module:
    
    receives input from user to select a state to edit, then allows for user to edit state 
    population and save it back to the custom dictionary us_states_dictionary
    located in the custom made anchan_state_database.py module
    
    
"""
from anchan_state_database import us_states_dictionary
from anchan_state_functionality import select_state


def run_program():
    """receives input and selects stat to edit then passes it to subordinate function"""
    state_to_edit = select_state(input("\nEnter the state you want to edit:\t"))
    state_data_get = us_states_dictionary.get(state_to_edit)  # retrieve state data
    print("\n", state_data_get, "\n")  # display data of selected state
    change_state_value(state_to_edit)  # call function to change the states value


def change_state_value(state_to_edit):
    """takes state from previous function. validates state existence, then gets the informaton.
    takes input to change value, validates number, then changes value and saves it to the dict
    """
    if state_to_edit in us_states_dictionary:  # check state exists
        state_data_get = us_states_dictionary.get(state_to_edit)
        # retrieve data of the selected state
        new_state_pop = input("\nEnter the new value for population: \t")
        if new_state_pop.isnumeric():  # check if new pop value is numc
            state_data_get["population"] = int(new_state_pop)
            # update the population value of the selected state
            us_states_dictionary[state_to_edit] = state_data_get
            # update the dictionary with the new population value
            print(f"\nValue updated successfully! The new value is {new_state_pop}\n")
            # print("Updated state population:", state_data_get)
            # print("Updated dictionary:", us_states_dictionary)
            #   the two lines above are verification lines, uncomment to verify change
        else:
            print("\nSorry, population value must be a whole number only.\n")
    else:
        print("Key does not exist in the dictionary.")


# test line
# run_program()
