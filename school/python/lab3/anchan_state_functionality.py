from anchan_state_database import us_states_dictionary


def start():
    find_state_by_name = input(  # Prompt state name
        "Enter the state name or two digit representation:\t"
    )
    selected_state = select_state(find_state_by_name)
    # runs func to pass parameter and confirm in case user entered 2 digit id or some
    #   wierd variation that causes issues due to case sensitivity
    if selected_state:
        display_state(selected_state)
    # calls the display function with confirmed user input to display state info
    else:
        print("oopsie poopsie.")


def select_state(find_state_by_name):
    for state, state_data_item in us_states_dictionary.items():
        # above code activates dictionary and items
        if (  # identifies either state name or state 2 digit id
            find_state_by_name == state.lower()
            or find_state_by_name == state_data_item["state_code"]
        ):
            return state  # Return the lowercase state name if either are found
    print("we could not find the 2d b")


def display_state(find_state_by_name):
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
        print()
    else:
        print("State not found.")
