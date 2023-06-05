from anchan_state_database import us_states_dictionary


def start():
    find_state_by_name = input(
        "Enter the state name or two digit representation:\t"
    )  # Prompt state name
    selected_state = select_state(find_state_by_name)
    if selected_state:
        display_state(selected_state)
    else:
        print("oopsie poopsie.")


def select_state(find_state_by_name):
    for state, state_data_item in us_states_dictionary.items():
        if (
            find_state_by_name == state.lower()
            or find_state_by_name == state_data_item["state_code"]
        ):
            return find_state_by_name  # Return the lowercase state name if found
    return None  # Return None if state not found


def display_state(find_state_by_name):
    state_data_item = us_states_dictionary.get(find_state_by_name)
    if state_data_item:
        print()
        print(find_state_by_name.capitalize())
        print("Capital:", state_data_item["capital"])
        print("Population:", state_data_item["population"])
        print("Flower:", state_data_item["flower"])
        print()
    else:
        print("State not found.")
