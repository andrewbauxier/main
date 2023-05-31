def calculate_percentage():
    """Function prompts user by calling get_valid_input(prompt) on the variables listed then runs
    percentage_calculation_formula(numerator, denominator, decimal_points) to do the calculation
    and prints the result then prompts for exit. Raises error if value is not a positive integer.
    """
    numerator = get_valid_input("\nPlease enter the numerator: ")
    denominator = get_valid_input("\nPlease enter the denominator: ")
    decimal_points = get_valid_input("\nPlease enter the number of decimal points: ")
    formatted_percentage = percentage_calculation_formula(
        numerator, denominator, decimal_points
    )
    print(f"The calculated percentage is: {formatted_percentage}%\n")
    input("\nPress Enter to return to the main program.")


def get_valid_input(prompt):
    """Creates a while loop that analyzes above input, assigns to a variable, and checks to see
    if it follows validation protocol
    Args:
        prompt (string): numerator, denominator, decimal_points
    Raises:
        ValueError: value failed min (positive) value of integer only input
    Returns:
        float: formatted percentage of input provided numerator, denominator, and decimal.
    """
    while True:
        try:
            # prompt gathers numerator, denominator, and decimal position
            user_input = input(prompt)
            user_input_float = float(user_input)
            if user_input_float >= 1 and user_input_float.is_integer():
                return int(user_input_float)
            else:
                raise ValueError
        except ValueError:
            print("\nOopsie Poopsie! Invalid input. Please try again.")


def percentage_calculation_formula(numerator, denominator, decimal_points):
    """Runs calculation for main function. formula is to format a percentage.
    Args:
        numerator (float)
        denominator (float)
        decimal_points (int)
    Returns:
        string
    """
    percentage = (numerator / denominator) * 100
    formatted_percentage = f"{percentage:.{decimal_points}f}"
    return formatted_percentage
