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
# loop to introduce program and provide ability to exit program. also performs validation of options
def exitAtAnyJunction():
  exitVariable = input("\nDo you wish to continue with registration? Type 'yes' or 'no'.\n").lower()
  if exitVariable == "no":
    exit(0)

def enterExitLoop():
  while True:
    enterExitLoopInput = input("\nWelcome to the Python Voter Registration Application. Do you want to continue with Voter Registration? Type 'yes' or 'no'\n").lower()
    if enterExitLoopInput == "yes":
        #userBool = True
        enterUserFirstAndLastName()
    elif enterExitLoopInput == "no":
        #userBool = False
        print("\nExiting the program.\n")
        exit(0)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    #print("The boolean value is:", userBool) #
      
## function to acquire first and last name of registrant
def enterUserFirstAndLastName():
    userFirstName = input("\nPlease enter your first name now\n")
    userLastName = input("\nPlease enter your last name now\n")
    print("\nThe name you entered is:\n", userFirstName, userLastName)

    exitAtAnyJunction()
    enterUserAgeAndValidate()
    return userFirstName, userLastName

## function to gather user age input and validate age
def enterUserAgeAndValidate():
  userAge = int(input("\nBe advised, only individuals 18 years of age or older are allowed to register.\nPlease input your age now\n"))
  if userAge > 17 and userAge < 130:
    print("\nThe age you entered is: ",  userAge)
    exitAtAnyJunction()
    isUSCitizenCheck()
    return userAge
  else:
    print("You must be 18 or older to register to vote. Goodbye.")
    exit(0)
    
def isUSCitizenCheck():
  while True:
    isUserUSCitizen = input("\nAre you a U.S. citizen? Please enter 'yes' or 'no' now.\n")
    if isUserUSCitizen.isalpha:
      isUserUSCitizen = isUserUSCitizen.lower()
      if isUserUSCitizen == "yes":
        enterUserState()
        return isUserUSCitizen
      elif isUserUSCitizen == "no":
        print("You must be a U.S. Citizen to register to vote. Goodbye.\n")
        exit(0) 
    else:
      print("\nInvalid input. Please enter 'yes' or 'no'.")

def enterUserState():
  while True:
    userStateLivingIn = input("\nWhat State do you live in? Please enter the 2 digit representation of your state, such as FL.\n").upper()
    if userStateLivingIn.isalpha() and len(userStateLivingIn) == 2:
      print("The state you entered is: ", userStateLivingIn)
      enterUserZipCode()
      return userStateLivingIn
    else:
      print("Invalid input. Please enter the 2 digit representation of your state, such as FL.")
      
def stateValidation(string):
  validStateCodes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 
    'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
  return string in validStateCodes
    
def enterUserZipCode():
  while True:
    userZipCode = input("\nPlease enter your zip code now. it must be numeric and contain only 5 digits\n")
    if userZipCode.isnumeric and len(userZipCode) == 5: 
      print ("The zip code you entered is ", userZipCode)
      return userZipCode
      displayUserInformationAndExitProgram()
    else:
      print("\nInvalid input. Please enter a numeric 5-digit zip code such as 12345.") 
      
def displayUserInformationAndExitProgram(string userFirstName, int):
  print("Thanks for registering to vote. Here is the information we received: ")
  print("Name: ", string userFirstName)


        
##################### functions end

#######################################################################################################################

#main program 
#enterExitLoop()
#enterUserFirstAndLastName()
#enterUserAgeAndValidate()
#isUSCitizenCheck()
#enterUserState()
enterUserZipCode()
displayUserInformationAndExitProgram()