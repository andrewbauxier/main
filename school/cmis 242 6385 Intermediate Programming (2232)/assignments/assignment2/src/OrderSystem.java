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
        int customerInput; //global variables begin
        Scanner scan1 = new Scanner(System.in); //global variables end
        int snackCountToGenerateID = 0;
        System.out.print("MENU.\n1: Order Snack\n2. Exit Program\nEnter your selection: ");//begin program operation
        customerInput = scan1.nextInt();
        System.out.println("\nThank you! You chose Number " + customerInput);        
        System.out.println("Do you want Fruit Snack (1) or Salty Snack (2): ");
        
        
        
        switch (customerInput) {//begin switch operation
            case 1:
                //local variables
                snackCountToGenerateID++;    
                String initialSnackSize;
                double priceOfSnack = 0;
                double snackSmall = 19.99;
                double snackMedium = 29.99;
                double snackLarge = 39.99;
                double citrusSnackCharge = 5.99;
                double nutSnackCharge = 4.50;
                

                //format: Snack(String:snackID, String:sizeOfSnack, Double:priceOfSnack)
                Snack baseSnack = new Snack( "snack"+snackCountToGenerateID, "no size selected", priceOfSnack);
                System.out.println(baseSnack.snackID);
                System.out.println(baseSnack.sizeOfSnack);
                System.out.println(baseSnack.priceOfSnack);
                System.out.println(snackCountToGenerateID);
                
                case 2:
                System.out.println("Thank you for using the program. Goodbye!");    
                break;        
        }
    }
}