import java.util.Scanner;

/* 
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-MM-DD 
 * This program provides proof of knowledge of concepts relating to encapsulation
 * and object-oriented program by performing calculations using Weight objects 
 * (instances of Weight class)
 * 
 * TODO List
 * [project]: tasks to be done before submitting
 * clean-up
 * 
 * [personal]: personal tasks to be done at a later date
 * refactor divide, maybe delete it. seems like it could be unneccessary.
*/
import java.util.Scanner;

public class OrderSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int customerSelectionInput = 0;

        while (customerSelectionInput != 2) {
            System.out.println("\nMENU\n1: Order a Snack\n2: Exit program\nEnter your selection: ");
            customerSelectionInput = scanner.nextInt();
            switch (customerSelectionInput) {
                case 1:
                    System.out.print("Do you want Fruit Snack (1) or Salty Snack (2): ");
                    int snackTypeInput = scanner.nextInt();

                    System.out.print("What size do you want: S, M, or L: ");
                    String snackSizeInput = scanner.next();

                    boolean isCitrusFruit = false;
                    boolean hasNutSnack = false;

                    if (snackTypeInput == 1) {
                        System.out.print("Do you want citrus fruit included? true/false: ");
                        isCitrusFruit = scanner.nextBoolean();
                    } else if (snackTypeInput == 2) {
                        System.out.print("Do you want nut snack included? true/false: ");
                        hasNutSnack = scanner.nextBoolean();
                    }

                    Snack snack;

                    if (snackTypeInput == 1) {
                        snack = new FruitSnack(snackSizeInput, isCitrusFruit);
                    } else {
                        snack = new SaltySnack(snackSizeInput, hasNutSnack);
                    }

                    System.out.println("You have chosen snack type = " + snack.getClass().getSimpleName()
                            + ", of type = " + snack.getSize() + ", id = " + snack.getId() + ", and price = $"
                            + snack.getPrice());
                    break;
                case 2:
                    System.out.println("Thank you for using the program. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid selection. Please try again.");
                    break;
            }
        }
        scanner.close();
    }
}