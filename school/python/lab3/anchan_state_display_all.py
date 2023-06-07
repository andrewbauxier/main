from time import sleep
from anchan_state_database import us_states_dictionary


def run_program():
    """Very simple function to display all the values in the dictionary"""
    print("\nHere is a list of all the US states:\n")
    for state, state_data_item in us_states_dictionary.items():
        print(state.title())
        print("Capital:", state_data_item["capital"])
        print("Population:", state_data_item["population"])
        print("Flower:", state_data_item["flower"])
        print()
        sleep(0.25)
