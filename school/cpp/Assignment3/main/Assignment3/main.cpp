#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>

// Function prototypes
void fillPassword(size_t, char[]);
bool showResults(int);
void showMenu();

// Define a variable to hold a password
// and the copy
char password[15];
char cpassword[15];

int main() {
    // Welcome the User
    std::cout << "Welcome to the C++ Array Program!\n";

    // Variables
    int choice = 0; // To store user choice
    int cVar = 0;   // process variable

    // Display menu and Get Selection
    while (true) {
        // Display the Menu
        showMenu();

        // Get the user selection
        std::string inputBuffer;
        std::getline(std::cin, inputBuffer);

        // Convert string to integer
        choice = std::stoi(inputBuffer);

        // If showResults returns false, break the loop
        if (!showResults(choice)) {
            break;
        }
    }

    // Call the Copy routine
    fillPassword(sizeof(password), password);

    // Display variable values
    std::cout << "password is " << password << std::endl;
    std::cout << "cVar is " << cVar << std::endl;

    // Pause before exiting
    char confirm;
    std::cout << "Confirm your exit!";
    std::cin.get(confirm); // Wait for any key

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

/* Display the Results and return true to continue or false to exit */
bool showResults(int value) {
    switch (value) {
    case 1:
        std::cout << "Welcome to the Football season!\n";
        break;
    case 2:
        std::cout << "Welcome to the Soccer season!\n";
        break;
    case 3:
        std::cout << "Welcome to the Baseball season!\n";
        break;
    case 4:
        std::cout << "Exiting the Menu system!\n";
        return false; // Signal to exit the loop
    default:
        std::cout << "Please enter a valid selection\n";
    }
    return true; // Continue the loop
}

/* Display the Menu */
void showMenu() {
    std::cout << "\nEnter a selection from the following menu.\n";
    std::cout << "1. Football season.\n";
    std::cout << "2. Soccer season.\n";
    std::cout << "3. Baseball season.\n";
    std::cout << "4. Exit the system.\n";
}
