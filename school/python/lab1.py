# functions begin
# function introduces program, performs validation of options
def enter_exit_loop():
    while True:
        print("\nWelcome to the Python Voter Registration Application.")
        print("\nTo exit the program at any time, type 'exit'.")
        print(
            "\nDo you want to continue with Voter Registration? Type 'yes' or 'no'. \n"
        )
        enter_exit_loop_input = input().lower()
        if enter_exit_loop_input == "yes":
            enter_user_first_and_last_name()
        elif enter_exit_loop_input == "no":
            print("\nExiting the program.\n")
            exit(0)
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")


# function to acquire first and last name of registrant
def enter_user_first_and_last_name():
    user_first_name = input(
        "\nPlease enter your first name now. To exit, type 'exit'.\n"
    )
    if user_first_name.lower() == "exit":
        print("\nExiting the program.\n")
        exit(0)
    user_last_name = input("\nPlease enter your last name now. To exit, type 'exit'.\n")
    if user_last_name.lower() == "exit":
        print("\nExiting the program.\n")
        exit(0)
    print("\nThe name you entered is:\t", user_first_name, user_last_name)
    enter_user_age_and_validate(user_first_name, user_last_name)


# function to gather user age input and validate age
def enter_user_age_and_validate(user_first_name, user_last_name):
    while True:
        print(
            "\nBe advised, only individuals 18 years of age or older are allowed to register."
        )
        user_age = input("Please input your age now. To exit, type 'exit'.\n")
        if user_age.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if user_age.isdigit():
            user_age = int(user_age)
            if 17 < user_age < 130:
                print("\nThe age you entered is:\t", user_age)
                is_us_citizen_check(user_first_name, user_last_name, user_age)
                break
            else:
                print("You must be 18 or older to register to vote. Please try again.")
        else:
            print("Invalid input. Please enter a valid age.")


# function to validate US citizenship
def is_us_citizen_check(user_first_name, user_last_name, age):
    while True:
        is_user_us_citizen = input(
            "\nAre you a U.S. citizen? Please enter 'yes' or 'no' now. To exit, type 'exit'.\n"
        )
        if is_user_us_citizen.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if is_user_us_citizen.isalpha():
            is_user_us_citizen = is_user_us_citizen.lower()
            if is_user_us_citizen == "yes":
                enter_user_state(user_first_name, user_last_name, age)
            elif is_user_us_citizen == "no":
                print("You must be a U.S. Citizen to register to vote. Goodbye.\n")
                exit(0)
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")


def enter_user_state(user_first_name, user_last_name, age):
    while True:
        user_state_living_in = input(
            "\nPlease enter the 2 digit representation of your state, such as FL. To exit, type 'exit'.\n"
        ).upper()
        if user_state_living_in.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if (
            user_state_living_in.isalpha()
            and len(user_state_living_in) == 2
            and state_validation(user_state_living_in)
        ):
            print("The state you entered is: ", user_state_living_in)
            enter_user_zip_code(
                user_first_name, user_last_name, age, user_state_living_in
            )
        else:
            print("Invalid input. That is not a valid state choice.")


# function validates that state entered is an actual state
def state_validation(string):
    valid_state_codes = [
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ]
    return string in valid_state_codes


# function to gather zip code information and validate
def enter_user_zip_code(user_first_name, user_last_name, age, state):
    while True:
        user_zip_code = input(
            "\nPlease enter your zip code now. \nIt must be numeric and contain only 5 digits. To exit, type 'exit'.\n"
        )
        if user_zip_code.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if user_zip_code.isnumeric() and len(user_zip_code) == 5:
            print("The zip code you entered is ", user_zip_code)
            display_user_information_and_exit_program(
                user_first_name, user_last_name, age, state, user_zip_code
            )
        else:
            print(
                "\nInvalid input. Please enter a numeric 5-digit zip code such as 12345."
            )


# function to display all gathered information and end program
def display_user_information_and_exit_program(
    user_first_name, user_last_name, age, state, user_zip_code
):
    print("\nThanks for registering to vote. Here is the information we received:")
    print("Name:", user_first_name, user_last_name)
    print("Age:", age)
    print("State:", state)
    print("Zip Code:", user_zip_code)
    print(
        "Thanks for using the Voter Registration Application. \
            \nYour voter registration card should be shipped within 3 weeks.\n"
    )
    exit(0)


# Call the main function to start the program
enter_exit_loop()
