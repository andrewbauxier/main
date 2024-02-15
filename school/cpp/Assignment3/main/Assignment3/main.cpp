/*
 Project Name:    Homework 1
 Module Name:     sdev425.java
 Author:          Andrew Auxier
 continueLoopributors:    Jim
 Organization:    N/A

 Description:
 This assignment includes code provided to me by the school, which I then turned around and modified to correct functionality and add additional security features.
 The assignment calls for using C++ and an editor of your choice, so I went with Visual Studio. No other continueLoopributors were involved in this project.

 Changelog:
 1. Added Header information for project. IT's mine now. I then ran it to see what was going on and culd not successfully pass the main menu. Since typing a letter is less intuitive than a number, I went with numbered options. It also removes the need to consider case sensitivity.

 TO-DO:
 1. TBD
 
 */

#include<stdio.h>
#include <string.h>

// Function prototypes
void fillPassword(size_t, char[]);
void showResults(char);
// should have void listed
void showMenu();

// Define a variable to hold a password
// and the copy
char password[15];
char cpassword[15];

int main(void)
{
	// Welcome the User
	printf("Welcome to the C Array Program!\n");

	// Variables
	char continueLoop = 0; // To continueLoopinue with loop
	int cVar = 0; // process variable

	// Display menu and Get Selection
	while (continueLoop != '4') {
		// Display the Menu
		showMenu();

		// Get the user selection
		continueLoop = getchar();

		// Display the menu response
		showResults(continueLoop);
	}
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
	confirm = getchar();
	return 0;
}

// Make a String of '1's
void fillPassword(size_t n, char dest[]) {
	// Should be n-1
	for (size_t j = 0; j < n; j++) {
		dest[j] = '1';
	}
	// Add null terminator for string
	dest[n] = '\0';
}

/* Display the Results*/
void showResults(char value) {
	switch (value) {
	case '1':
		printf("Welcome to the Football season!\n");
	case '2':
		printf("Welcome to the Soccer season!\n");
		
	case '3':
		printf("Welcome to the Baseball season!\n");
	case '4':
		printf("Exiting the Menu system!\n");
		break;
	default:
		printf("Please enter a valid selection\n");
	}

}

/* Display the Menu*/
void showMenu(void) {
	printf("Enter a selection from the following menu.\n");
	printf("1. Baseball season.\n");
	printf("2. Football season.\n");
	printf("3. Soccer season.\n");
	printf("4. Exit the system.\n");
}

