"""
Project Name:   Lab 3
Module Name:    anchan_popsort.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module: retrieves the top 5 most populated states from the dictionary (custom dictionary 
    us_states_dictionary located in the custom made anchan_state_database.py module), sorts
    them into population amounts in descending form, displays said values on the CLI,
    then generates a bargraph for visual representation
    
    
"""
from anchan_state_database import us_states_dictionary
import matplotlib.pyplot as plot


def run_program():
    # get items from dict
    state_data_items = us_states_dictionary.items()
    # get the top 5
    top_states = get_top_5(state_data_items, max_states=5)
    generate_bar_graph(top_states)


def get_top_5(states_data_all_five, max_states=5):
    """Get the top 5 states with the highest population."""
    sorted_states_data = sort_states_by_population(  # sort in descending order
        states_data_all_five
    )
    top_states = sorted_states_data[:max_states]  # gets top 5 from the list
    # :max_states - the : splices the list to keep only the top five
    for state, states_data_item in top_states:  # goes through list
        population = states_data_item[
            "population"
        ]  # sets reuseable variable to run func
        print_state_population(state, population)  # runs func each time through list
    return top_states


def sort_states_by_population(states_data):
    """Sort states data based on population in descending order."""
    return sorted(states_data, key=get_population, reverse=True)


def print_state_population(state, population):
    """Print formatted state name and population."""
    capitalized_state = state.capitalize()
    print(f"State: {capitalized_state}\t\t Population: {population}")
    # this is called multiple times; it iterates through a list.


def get_population(state_data_item):
    """Retrieve the population value from the state data item."""
    return state_data_item[1]["population"]
    # item[1] points to the state_data_items as a whole. the state name is actually [0],
    # and all other information is [1]. ["population"] specifically points to the area in [1]
    # for the program to continue looking and then grab that item, which is our pop. this
    # was hard to understand, so I am specifying it here as my initial thought was that
    # each state_data_item was its own thing. No, its all one block


def generate_bar_graph(top_states):
    """Generate a bar graph of the top 5 populated states."""
    states = []  # creates empty list
    populations = []  # creates empty list
    for state, states_data_item in top_states:  # populates the lists
        states.append(state.capitalize())
        populations.append(states_data_item["population"])
    # now begin plotting graph
    plot.bar(states, populations)  # retrieves lists for use
    plot.xlabel("States")
    plot.ylabel("Population")
    plot.title("Top 5 Populated States")
    plot.show()


# Call the run function to execute the code
# run_program()
