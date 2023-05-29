import datetime

## Calculate the number of days until July 4, 2025
# Calling point from menu
def calculate_days_until_july_4_2025():
    target_date = datetime.datetime(2025, 7, 4).date()
    days_until_target = calculate_days(target_date)
    print(f"\nThere are {days_until_target} days until {target_date.strftime('%B %d, %Y')}")
    input("\nPress Enter to return to the main program.")

# Subodinate Function to calculate_days_until_july_4_2025
def calculate_days(target_date):
    current_date = datetime.datetime.now().date()
    remaining_days = (target_date - current_date).days
    return remaining_days
