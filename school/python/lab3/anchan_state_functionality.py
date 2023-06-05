from anchan_state_database import us_states_dictionary


def start():
    find_state_by_name = input(
        "Enter the state name or two digit representation:\t"
    )  # Prompt state name
    return find_state_by_name


def select_state(find_state_by_name):
    for state, state_data_item in us_states_dictionary.items():
        state_data_lookup_results = us_states_dictionary.get(
            find_state_by_name.lower()
        )  # Retrieve state info
        if (
            state.lower() == find_state_by_name  # find state by name
            or state_data_item["state_code"] == find_state_by_name  # find state by code
        ):
            state_data_lookup_results = state_data_item  # changes state target to code
            break

    if state_data_lookup_results:
        print()
        print(state.capitalize())
        print("Capital:", state_data_lookup_results["capital"])
        print("Population:", state_data_lookup_results["population"])
        print("Flower:", state_data_lookup_results["flower"])
        print()
    else:
        print("State not found.")
