from anchan_state_database import us_states_dictionary


def run_program():
    # Get the items from the dictionary
    state_data_items = us_states_dictionary.items()
    # Get the top 5 states with the highest population
    get_top_5(state_data_items, max_states=5)


def get_top_5(states_data, max_states=5):
    """Get the top 5 states with the highest population."""
    sorted_states_data = sort_states_by_population(  # sort in descending order
        states_data
    )
    top_states = sorted_states_data[:max_states]  # gets top 5 from the list
    for state, states_data_item in top_states:  # goes through list
        population = states_data_item[
            "population"
        ]  # sets reuseable variable to run func
        print_state_population(state, population)  # runs func


def sort_states_by_population(states_data):
    """Sort states data based on population in descending order."""
    return sorted(states_data, key=get_population, reverse=True)


def print_state_population(state, population):
    """Print formatted state name and population."""
    formatted_state = state.capitalize()
    print(f"State: {formatted_state}\t\t Population: {population}")


def get_population(state_data_item):
    """Retrieve the population value from the state data item."""
    return state_data_item[1]["population"]


# Call the run function to execute the code
# run()
