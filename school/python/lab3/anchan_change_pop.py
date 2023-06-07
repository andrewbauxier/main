from anchan_state_database import us_states_dictionary
from anchan_state_functionality import select_state


def run_program():
    state_to_edit = select_state(input("\nEnter the state you want to edit:\t"))
    state_data_get = us_states_dictionary.get(state_to_edit)  # retrieve state data
    print("\n", state_data_get, "\n")  # Display the data of the selected state
    change_state_value(state_to_edit)  # Call the function to change the state's value


def change_state_value(state_to_edit):
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
