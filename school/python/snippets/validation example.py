# This code is being saved to serve of an example of a method to provide low to moderate
# validation depending on the needs of the user. pay attention to min_value and data_type
def calculate_percentage():
    numerator = get_valid_input("\nPlease enter the numerator: ", min_value=1)
    denominator = get_valid_input("\nPlease enter the denominator: ", min_value=1)
    decimal_points = get_valid_input("\nPlease enter the number of decimal points: ")
    formatted_percentage = percentage_calculation_formula(
        numerator, denominator, decimal_points
    )

    print(f"The calculated percentage is: {formatted_percentage}%\n")
    input("\nPress Enter to return to the main program.")


def get_valid_input(prompt):
    while True:
        try:
            user_input = data_type(input(prompt))
            if min_value is not None and user_input < min_value:
                raise ValueError
            return user_input
        except ValueError:
            print("\nOopsie Poopsie! Invalid input. Please try again.")


def percentage_calculation_formula(numerator, denominator, decimal_points):
    percentage = (numerator / denominator) * 100
    formatted_percentage = f"{percentage:.{decimal_points}f}"
    return formatted_percentage
