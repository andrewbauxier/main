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
        System.out.println("MENU.\n1: Order Snack\n2. Exit Program");//begin program operation
        customerInput = scan1.nextInt();
        System.out.println("Thank you! You chose Number " + customerInput);
        switch (customerInput) {//begin switch operation
            case 1:
                System.out.println("This is number 1");

                return;
            case 2:
                System.out.println("This is number 2");    
                break;
        
            default:
                if (customerInput!=1 || customerInput!=2) {
                    System.out.println("Please enter 1 or 2 only");
                }
        }
    }
}