/* 
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-02-16 
 * This program implements a snack ordering system with a Snack class hierarchy and FruitSnack and SaltySnack subclasses as well 
 * as an OrderSystem class. The user inputs data and is given the details for a snack. Provides proof of knowledge of concepts such as 
 * encapsulation, polymorphism, and inheritance in Object Oriented Programming (Java).
*/
import java.util.Scanner;
public class OrderSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int menuSelectionInput = 0;
        while (menuSelectionInput != 2) { //while loop to kick back to menu until exit program
            System.out.print("\nMENU\n1: Order a Snack\n2: Exit program\nEnter your selection: ");
            menuSelectionInput = scanner.nextInt();
            switch (menuSelectionInput) { //begin switch operations to determine snack
                case 1: //Snack case
                    System.out.print("Do you want Fruit Snack (1) or Salty Snack (2): ");
                    int snackChoice = scanner.nextInt();
                    System.out.print("What size do you want: S, M, or L: ");
                    char sizeChoice = scanner.next().charAt(0);
                    boolean hasCitrus = false;
                    boolean hasNuts = false;
                    if (snackChoice == 1) { //fruit snack for snackChoice
                        System.out.print("Do you want citrus fruit included? true/false: ");
                        hasCitrus = scanner.nextBoolean();
                    } else if (snackChoice == 2) { //nut snack for snackChoice
                        System.out.print("Do you want nut snack included? true/false: ");
                        hasNuts = scanner.nextBoolean();
                    }
                    if (snackChoice == 1) {//fruit snack for snackChoice
                        String snackID = "fruitsnack" + sizeChoice + snackChoice;
                        FruitSnack fruitSnack = new FruitSnack(snackID, sizeChoice, snackChoice, hasCitrus);
                        fruitSnack.displaySnack();
                    } else {
                        String snackID = "nutsnack" + sizeChoice + snackChoice ;
                        SaltySnack saltySnack = new SaltySnack(snackID, sizeChoice, snackChoice, hasNuts);
                        saltySnack.displaySnack();
                    }
                    break;
                case 2: //exit program case
                    System.out.println("Thank you for using the program. Goodbye!");
                    break;
                default: //verification to get to right choice
                    System.out.println("Invalid selection. Please try again.");
                    break;
            }
        }
        scanner.close();
    }
}