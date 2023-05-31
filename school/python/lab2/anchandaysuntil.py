import datetime

## Calculate the number of days until July 4, 2025
# Calling point from menu
def calculate_days_until_july_4_2025():
    targeting_july_4_2025 = datetime.datetime(2025, 7, 4).date()
    days_until_july_4_2025 = calculate_days(targeting_july_4_2025)
    print(f"\nThere are {days_until_july_4_2025} days until\
        {targeting_july_4_2025.strftime('%B %d, %Y')}")
    input("\nPress Enter to return to the main program.")

# Subodinate Function to calculate_days_until_july_4_2025
def calculate_days(target_date):
    current_date = datetime.datetime.now().date()
    remaining_days = (target_date - current_date).days
    return remaining_days
