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
public class OrderSystem {
    public static void main(String[] args) {
        //global variables begin
        int customerMenuInput; //choose snack or exit program
        int customerFruitOrSalt;
        String customerSizeChoice;
        double customerTotalPrice = 0;

        Scanner scanner = new Scanner(System.in); 
        //global variables end
        System.out.print("MENU\n1: Order Snack\n2. Exit Program\nEnter your selection: ");//begin program operation
        customerMenuInput = scanner.nextInt();
        scanner.nextLine();
        //System.out.println("Thank you! You chose Number " + customerMenuInput);
        System.out.println("What size do you want (S, M, L): ");
        customerSizeChoice = scanner.nextLine();
        System.out.println("Do you want Fruit Snack (1) or Salty Snack (2): ");
        customerFruitOrSalt = scanner.nextInt();
        ///code///
        customerSizePricing(customerSizeChoice, customerTotalPrice);
        helloworld();
        /* 
         * Fruit snack only
         * System.out.println("Do you want citrus fruit included? true/false: ");
         * 
         * Salt Snack only
         * System.out.println("Do you want nuts included? true/false: ");
        */
    }
}