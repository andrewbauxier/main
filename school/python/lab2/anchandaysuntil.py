"""module used to calculate the number of days from the date of use until July 4, 2022
"""
import datetime


## Calculate the number of days until July 4, 2025
# Calling point from menu
def calculate_days_until_july_4_2025():
    """ok this ones a doozy. identifies a date based on first line then runs a formula to
    calculate days until the date on the next line. names are rough but hey its what I got.
    finally spits it back out to the user with super special formatting. also exits"""
    target_date_of_july_4_2025 = datetime.datetime(2025, 7, 4).date()
    days_until_target_date = calculate_days(target_date_of_july_4_2025)
    print(
        f"\nThere are {days_until_target_date} days until"
    )  # calculates number of days
    print(
        f"{target_date_of_july_4_2025.strftime('%B %d, %Y')}"
    )  # displays target date of days until
    input("\nPress Enter to return to the main program.")


# Subodinate Function to calculate_days_until_july_4_2025
def calculate_days(target_date):
    """used to calculte the days from the current date until the targeted date

    Args:
        target_date (datetime): a date imported from the datettime module

    Returns:
        int?: returns the number of days until targeted date from now
    """
    current_date = datetime.datetime.now().date()
    remaining_days = (target_date - current_date).days
    return remaining_days
