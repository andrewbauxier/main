/* Documentation 
 *  Name:    Andrew B. Auxier
 *  Class:   CMIS 242 6385
 *  Date:    2023-03-07
 *  Package Description: This package provides a command line interface for main manager package
*/
import java.util.Scanner;

public class MediaRentalSystem {
    public static void main(String[] args) {
        // Set selection variable
        int menuInput = 0;
        Manager manager = new Manager(); // Create Manager object
        Scanner scanner = new Scanner(System.in); // Create Scanner object
        while (menuInput != 9) { // loop menu until user quits program
            runMenu();// Show menu for selection
            System.out.print("Enter your selection: ");// Display "Enter your selection"
            menuInput = scanner.nextInt();// Get selection
            System.out.println();
            switch (menuInput) {
            case 1:
                System.out.print("Enter path (directory) where to load from: ");
                //get user input
                scanner.nextLine();
                String path = scanner.nextLine();
                System.out.println();
                manager.LoadMedias(path);
                System.out.println("\n------------------");
                break;
            case 2:
                System.out.print("Enter the title: ");
                // get user input
                scanner.nextLine();
                String title = scanner.nextLine();
                System.out.println();
                manager.findMedia(title);
                System.out.println("\n------------------");
                break;
            case 3:
                System.out.print("Enter the id: ");
                int id = scanner.nextInt();
                System.out.println();
                manager.rentMedia(id);
                System.out.println("\n------------------");
                break;
            case 9:
                System.out.println("Thank you for using the program. Goodbye!");
                System.exit(0);
                break;
            } 

        }
    }//endmain

    private static void runMenu() {
        System.out.println("\nWelcome to Media Rental System");
        System.out.println("1: Load Media objects...");
        System.out.println("2: Find Media object...");
        System.out.println("3: Rent Media object...");
        System.out.println("9: Quit");
        System.out.println();
    }
}//end program