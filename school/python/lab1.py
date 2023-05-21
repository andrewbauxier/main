# Prompt the user for their first name, last name, age, country of citizenship, state of residence and zipcode
#     all fields must be entered
# 18 years old and a U.S citizen, they can move forward and be prompted 
#     for the remaining questions and register to vote
# If not, they should not be presented with the additional questions.
# error checking logicon the input statements to make sure the age numbers entered seem reasonable 
#     (e.g. a person is probably not > 120 years)
# States should be 2 letters representing only valid U.S. States.
# Application should prompt the user for the needed questions to complete the registration 
#     and reprompt when data is invalid giving the user the opportunity to retry.
# output should summarize the input data and congratulate the user if they are 
#     eligible to vote and entered all of the data
#     The user should be given options to exit the program at any time to cancel the registration process

# Title:    Lab 1
# Name:     Andrew Auxier
# Class:    SDEV 300 6383 Building Secure Python Applications (2235)
# Date:     2023-05-17

# methods
# menu looping
def enterExitLoop():
  while True:
    enterExitLoopInput = input("\nWelcome to the Python Voter Registration Application. Do you want to continue with Voter Registration? Type 'yes' or 'no'\n")
    enterExitLoopInput = enterExitLoopInput.lower()
    if enterExitLoopInput == "yes":
        userBool = True
        enterUserFirstAndLastName()
        #break
    elif enterExitLoopInput == "no":
        userBool = False
        print("\nExiting the program.\n")
        exit(0)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
  print("The boolean value is:", userBool)    
      
def enterUserFirstAndLastName():
    userFirstName = input("\nPlease enter your first name now\n")
    print("\nThe name you entered is:", userFirstName, )
    userLastName = input("\nPlease enter your last name now\n")
    print
    


####################################################################################################################################

#main
enterExitLoop()




