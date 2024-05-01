/*
Project Name : Homework 1
Module Name : sdev425.java
Author : Andrew Auxier
contributors : Jim
Organization : N / A

Description :
This assignment includes code provided to me by the school, which I then turned around and modified to correct functionality and add additional security features.
The assignment calls for using C++ and an editor of your choice, so I went with Visual Studio. No other contributors were involved in this project.

Changelog:
1. Added Header information for project. It's mine, now. 
2. Since typing a letter is less intuitive than a number, I changed the switch-case to numbers instead of letters, which allowed me to get rid of all that case-sensitive nonesense. It's poor design to make it so complicated for little to no reason than to make it look pretty and match the theme of the subject.  
3. Added input error handling for menu selection using fgets. If the user enters an invalid input (non-numeric), the program displays an error message, clears the input buffer, and continues to prompt for valid input.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void fillPassword(size_t, char[]);
void showResults(int);
void showMenu(void);

// Define a variable to hold a password
// and the copy
char password[15];
char cpassword[15];

int main(void) {
    // Welcome the User
    printf("Welcome to the C Array Program!\n");

    // Variables
    int choice = 0; // To store user choice
    int cVar = 0; // process variable

    
    while (choice != 4) {
        // Display the Menu
        showMenu();

        // Get the user selection
        std::string input;
        std::getline(std::cin, input);

        // Convert string to integer
        try {
            choice = std::stoi(input);

            // Display the menu response
            showResults(choice);
        }
        catch (const std::invalid_argument& e) {
            // Handle conversion error
            std::cerr << "Invalid input. Please enter a valid number.\n";
            std::cin.clear(); // Clear error flags
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
        }
    }
    /*
    // Display menu and Get Selection
    while (choice != 4) {
        // Display the Menu
        showMenu();

        // Get the user selection
        char inputBuffer[5];  // Adjust the size based on your needs
        if (fgets(inputBuffer, sizeof(inputBuffer), stdin) != NULL) {
            // Convert string to integer
            choice = atoi(inputBuffer);
            // Display the menu response
            showResults(choice);
        }
        else {
            // Handle input error
            printf("Error reading user input.\n");
            return 1;
        }
    }
    */

    // Call the Copy routine
    fillPassword(sizeof(password), password);

    // Display variable values
    printf("password is %s\n", password);
    printf("cVar is %d\n", cVar);
    // Copy password
    memcpy(cpassword, password, sizeof(password));

    // Pause before exiting
    char confirm;
    printf("Confirm your exit!");
    confirm = getchar();  // Wait for any key
    
    return 0;
}

// Make a String of '1's
void fillPassword(size_t n, char dest[]) {
    // Should be n-1
    for (size_t j = 0; j < n - 1; j++) {
        dest[j] = '1';
    }
    // Null terminator for string
    dest[n - 1] = '\0';
}

/* Display the Results*/
void showResults(int value) {
    switch (value) {
    case 1:
        printf("Welcome to the Football season!\n");
        break;
    case 2:
        printf("Welcome to the Soccer season!\n");
        break;
    case 3:
        printf("Welcome to the Baseball season!\n");
        break;
    case 4:
        printf("Exiting the Menu system!\n");
        break;
    default:
        printf("Please enter a valid selection\n");
    }
}

/* Display the Menu*/
void showMenu(void) {
    printf("\nEnter a selection from the following menu.\n");
    printf("1. Football season.\n");
    printf("2. Soccer season.\n");
    printf("3. Baseball season.\n");
    printf("4. Exit the system.\n");

}