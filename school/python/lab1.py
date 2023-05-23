# Prompt the user for their 
#   first name, last name,          Check!
#   age,                            
#   country of citizenship,         
#   state of residence              
#   zipcode                         
#   *all fields must be entered     
# 
# 18 years old and a U.S citizen, they can move forward and be prompted 
#     for the remaining questions and register to vote
# 
# If not, they should not be presented with the additional questions.
# error checking logicon the input statements to make sure the age numbers entered seem reasonable 
#     (e.g. a person is probably not > 120 years)
# 
# States should be 2 letters representing only valid U.S. States.
# 
# Application should prompt the user for the needed questions to complete the registration 
#     and reprompt when data is invalid giving the user the opportunity to retry.
# 
# output should summarize the input data and congratulate the user if they are 
#     eligible to vote and entered all of the data
#     The user should be given options to exit the program at any time to cancel the registration process

# Title:    Lab 1
# Name:     Andrew Auxier
# Class:    SDEV 300 6383 Building Secure Python Applications (2235)
# Date:     2023-05-17

##################### functions begin
## function introduces program, performs validation of options
def enterExitLoop():
    while True:
        enterExitLoopInput = input("\nWelcome to the Python Voter Registration Application. To exit the program at any time, type 'exit'. \nDo you want to continue with Voter Registration? Type 'yes' or 'no'. \n").lower()
        if enterExitLoopInput == "yes":
            enterUserFirstAndLastName()
        elif enterExitLoopInput == "no":
            print("\nExiting the program.\n")
            exit(0)
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
## function to acquire first and last name of registrant
def enterUserFirstAndLastName():
    userFirstName = input("\nPlease enter your first name now. To exit, type 'exit'.\n")
    if userFirstName.lower() == "exit":
        print("\nExiting the program.\n")
        exit(0)
    userLastName = input("\nPlease enter your last name now. To exit, type 'exit'.\n")
    if userLastName.lower() == "exit":
        print("\nExiting the program.\n")
        exit(0)
    print("\nThe name you entered is:\t", userFirstName, userLastName)
    enterUserAgeAndValidate(userFirstName, userLastName)
## function to gather user age input and validate age
def enterUserAgeAndValidate(userFirstName, userLastName):
    while True:
        print("\nBe advised, only individuals 18 years of age or older are allowed to register.")
        userAge = input("Please input your age now. To exit, type 'exit'.\n")
        if userAge.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if userAge.isdigit():
            userAge = int(userAge)
            if userAge > 17 and userAge < 130:
                print("\nThe age you entered is:\t", userAge)
                isUSCitizenCheck(userFirstName, userLastName, userAge)
                break
            else:
                print("You must be 18 or older to register to vote. Please try again.")
        else:
            print("Invalid input. Please enter a valid age.")
## function to validate us citizenship
def isUSCitizenCheck(userFirstName, userLastName, age):
    while True:
        isUserUSCitizen = input("\nAre you a U.S. citizen? Please enter 'yes' or 'no' now. To exit, type 'exit'.\n")
        if isUserUSCitizen.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if isUserUSCitizen.isalpha():
            isUserUSCitizen = isUserUSCitizen.lower()
            if isUserUSCitizen == "yes":
                enterUserState(userFirstName, userLastName, age)
            elif isUserUSCitizen == "no":
                print("You must be a U.S. Citizen to register to vote. Goodbye.\n")
                exit(0)
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
## function to gather us state and validate length
def enterUserState(userFirstName, userLastName, age):
    while True:
        userStateLivingIn = input("\nPlease enter the 2 digit representation of your state, such as FL. To exit, type 'exit'.\n").upper()
        if userStateLivingIn.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if userStateLivingIn.isalpha() and len(userStateLivingIn) == 2 and stateValidation(userStateLivingIn):
            print("The state you entered is: ", userStateLivingIn)
            enterUserZipCode(userFirstName, userLastName, age, userStateLivingIn)
        else:
            print("Invalid input. That is not a valid state choice.")
## function validates that state entered is an actual state            
def stateValidation(string):
  validStateCodes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 
    'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
  return string in validStateCodes
## function to gather zip code information and validate
def enterUserZipCode(userFirstName, userLastName, age, state):
    while True:
        userZipCode = input("\nPlease enter your zip code now. It must be numeric and contain only 5 digits. To exit, type 'exit'.\n")
        if userZipCode.lower() == "exit":
            print("\nExiting the program.\n")
            exit(0)
        if userZipCode.isnumeric() and len(userZipCode) == 5:
            print("The zip code you entered is ", userZipCode)
            displayUserInformationAndExitProgram(userFirstName, userLastName, age, state, userZipCode)
        else:
            print("\nInvalid input. Please enter a numeric 5-digit zip code such as 12345.")
## function to display all gather information and end program
def displayUserInformationAndExitProgram(userFirstName, userLastName, age, state, userZipCode):
    print("\nThanks for registering to vote. Here is the information we received:")
    print("Name:", userFirstName, userLastName)
    print("Age:", age)
    print("State:", state)
    print("Zip Code:", userZipCode)
    print("Thanks for using the Voter Registration Application. Your voter registration card should be shipped within 3 weeks.\n")
    exit(0)
##################### functions end #####################
# Call the main function to start the program
enterExitLoop()