"""
Project Name:   Lab 3
Module Name:    anchan_state_functionality.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module:
    
    prompts for user input to determine what state to lookup, validates the state's existence
    in the dictionary (by state name or 2-digit code), and pulls and displays the states info
    and image of the state flower from the dictionary entry.
    
"""
import matplotlib.pyplot as plot
import matplotlib.image as plotimage
from anchan_state_database import us_states_dictionary


def run_program():
    """prompts and reprompts user to enter a state or a two-digit code of a state
    until valid state is entered. displays infon about the state then breaks loop.
    """
    while True:
        find_state_by_name = input(  # prompt state name
            "Enter the state name or two digit representation:    "
        )
        selected_state = select_state(find_state_by_name.lower())
        # runs func to pass parameter and confirm in case user entered 2 digit id or some
        # wierd variation that causes issues due to case sensitivity
        if selected_state:
            display_state(selected_state)
            break

        # calls the display function with confirmed user input to display state info
        # else:
        #     print("oopsie poopsie.")


def select_state(find_state_by_name):
    """searches for state in the dict based on state name or two-dig code. if found,
    returns lowercase state name. If not found, prints an error message and returns None.
    """
    for state, state_data_item in us_states_dictionary.items():
        # above code activates dictionary and items
        if (  # identifies either state name or state 2 digit id
            find_state_by_name == state.lower()
            or find_state_by_name == state_data_item["state_code"]
        ):
            return state  # return lowercase state name if either are found
    print("That is not a valid selection. Enter the state name or 2-digit code.\n")
    return None
    # apparently all should return or none should. Here's your None, pylint, ya jerk


def display_state(find_state_by_name):
    """provides info about state based on given state name or two-digit code. retrieves data
    from dict, including the state capital, pop, and flower. Displays image of the state flower.
    """
    state_data_item = us_states_dictionary.get(find_state_by_name)
    # important: this code assigns the items from the dictionary to a variable.
    # if the variable is not assigned, the state_data_item's within the dictionary
    # are not accessible even though the dictionary is imported.
    # this code is neccessary.
    if state_data_item:  # if the user input and verified value is found
        print()
        print(find_state_by_name.capitalize())
        print("Capital:", state_data_item["capital"])
        print("Population:", state_data_item["population"])
        print("Flower:", state_data_item["flower"])
        display_state_image(find_state_by_name)
        print()

    else:
        print("State not found.")


def display_state_image(find_state_by_name):
    """displays image of state flower based on given state name or two-digit code. retrieves
    image path from dict and shows the image using matplotlib. If no image path is found,
    prints an error message. if no data is found, it prints a different message.
    """
    state_data_item = us_states_dictionary.get(find_state_by_name)  # get for image url
    if state_data_item:
        image_path = state_data_item.get("image_path")  # url for image stored in dict
        if image_path:  # plotting behavior below
            image = plotimage.imread(image_path)
            plot.imshow(image)
            plot.show()
        else:
            print(f"No image path found for {find_state_by_name}.")
    else:
        print(f"No data found for {find_state_by_name}.")


# testing purpposes
# run_program()
