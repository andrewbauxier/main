import sys
import anchan_state_database


def main_menu_loop():
    print("\nWelcome to Anchan's State Database. Here are your options\n")
    print(
        "1. Display all U.S. States in Alphabetical order along with the Capital, "
        "State Population, and Flower"
    )
    print(
        "2. Search for a specific state and display the appropriate Capital"
        "name, State Population, and an image of the associated State Flower."
    )
    print(
        "3. Provide a Bar graph of the top 5 populated States showing their"
        "overall population."
    )
    print("4. Update the overall state population for a specific state.")
    print("5: Exit the program")
    menu_option_selected = get_menu_option_validation()
    utility_function_switcher(menu_option_selected)


def get_menu_option_validation():
    """provides validation for input from main menu loop. validation rules are: must be an integer
    between 1 and 6
    Returns:
        Integer: parameter returns as validated
    """
    while True:
        menu_option_input = input("\nWhich option would you like to choose? \n")
        if menu_option_input.isdigit():
            menu_option_input = int(menu_option_input)
            if menu_option_input >= 1 and menu_option_input <= 5:
                return menu_option_input
            else:
                print("\nInvalid input. Please enter a number between 1 and 6.")
                input("Press enter to try again.")
                break
        else:
            print("\nInvalid input. Please enter a number between 1 and 6.")
            input("Press enter to try again.")
            break


def utility_function_switcher(menu_option_selected):
    """match-case for input to direct traffic to approprate modules and functions
    Args:
        menu_option_selected (int)
    """
    match menu_option_selected:
        case 1:
            anchan_state_database.start()
        case 2:
            anchan_state_database.start()
        case 3:
            anchan_state_database.start()
        case 4:
            anchan_state_database.start()
        case 5:
            exit_program()


## Exit the program
def exit_program():
    """exit function"""
    print("\nYou have chosen to exit the program. Goodbye!\n")
    sys.exit()
