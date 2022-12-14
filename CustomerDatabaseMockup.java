//Name: Andrew Auxier
//Date: 2022-12-13
// Write a Java program that displays a menu to allow the user the following functionality:
// 1. Add multiple new customers - prompt user for the number of customers to be loaded and then
// prompts for each customer's name, customer id (5 digit number), and total sales
// 2. Add single new customer - prompts the user for customer data: customer name, customer id, and total
// sales
// 3. Display all customers - displays each customer's data to the console, one customer per line
// 4. Retrieve specific customer's data - prompts the user for the customer id and displays the
// corresponding customer's data: customer id, customer name, and total sales
// 5. Retrieve customers with total sales based on the range - prompts the user for the lowest and highest
// total sales and displays all customers with total sales in that range. Display each customer on a separate
// line with all information – Customer Name, Customer ID, and Total Sales
// 6. Exit
import java.lang.reflect.Array;
import java.util.*;
public class CustomerDatabaseMockup {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args){
        //array list
        String[] customerName = new String[100];
        int[] customerID = new int[100];
        double[] customerTotalSales = new double[100];
        //global variables
        boolean menuLoop = true; //TODO: Test removing this later, it says the variable is unneccessary
        int menuInput = 0;
        //Step 0.2. - while loop to keep kicking user back to menu for more inputs
        while (menuLoop = true ) {
            System.out.println("\n\tMENU\n1: Add multiple new customers\n2: Add single new customer\n3: Display all customers");
            System.out.println("4: Retrieve specific customer's data\n5: Retrieve customer's with orders based on range");
            System.out.print("9: Exit Program");
            System.out.println(); //clear buffer
            do {
                System.out.print("\nEnter your selection:\t");
                while (!scanner.hasNextInt()) {
                    System.out.println("\nThat's not a number, please enter a number as listed on the menu.\n\nEnter your selection:\t");
                    scanner.next(); // this is important!
                }
                menuInput = scanner.nextInt();
            } while (menuInput <= 0);
            switch(menuInput) {
                case 1: // method 1. Add multiple new customers
                    //1.1 generate array based on user input
                    addMultipleNewCustomers(customerName, customerID, customerTotalSales, menuInput);
                    promptEnterKey();
                    break;

                case 2: //method 2. Add single new customer 
                    addSingleNewCustomer(customerName, customerID, customerTotalSales);
                    promptEnterKey();
                    break;
                case 3: //method 3. Display all customers
                    callCustomerList(customerName, customerID, customerTotalSales);
                    promptEnterKey();
                    break;
                case 4: //method 4. Retrieve specific customer's data
                    callSpecificCustomersData(customerName, customerID, customerTotalSales);
                    promptEnterKey();
                    break;
                case 5: //method 5. Retrieve customers with total sales based on the range
                    callCustomerDataBySales(customerName, customerID, customerTotalSales);
                    promptEnterKey();
                    break;
                case 9: //method 6. JAILBREAK!!
                    //menuLoop = false;
                    System.out.println("Have a nice day!\n");
                    return; 
                default:
                    System.out.println("\nThat choice is not a valid option, please enter a number as listed on the menu.\n");
            }//end method switch ops
        }//end while loop for menu
    }//end main
    ///-----------------methods begin here-----------------///  
    // 0. utility methods
    //finds first empty index to keep from overwriting values
    public static int findFirstEmptyIndex(String[] customerName) { 
        for(int i = 0;i<customerName.length;i++) {
            if(customerName[i]==null)
                return i;
        }
        return -1;
    }
    //to keep menu from popping up too fast so reader can actually read the information presented
    public static void promptEnterKey(){
        System.out.println("\nPress 'ENTER' key to continue.");
        scanner.nextLine();
        scanner.nextLine();
    }
    // method 1. Add multiple new customers - prompt user for the number of customers to be loaded and then
    public static void addMultipleNewCustomers(String[] customerName, int[] customerID, double[] customerTotalSales, int menuInput) {
        int firstEmptyIndex = findFirstEmptyIndex(customerName);
        System.out.print("\nPlease enter the number of customers you wish to add:\t");
        int numCustomersToAdd = (scanner.nextInt());
        for (int i = firstEmptyIndex; i < firstEmptyIndex + numCustomersToAdd; i++) {
            scanner.nextLine(); //clear buffer for scanner
            System.out.print("\nPlease enter the customers name:\t");
            customerName[i]=(scanner.nextLine());
            System.out.print("\nPlease enter the customers ID number:\t");
            customerID[i]=(scanner.nextInt());
            System.out.print("\nPlease enter the customers Total Sales:\t");
            customerTotalSales[i]=(scanner.nextDouble());
            System.out.println("Index # " + (i));
            System.out.println(customerName[i]);
            System.out.println(customerID[i]);
            System.out.println(customerTotalSales[i]);
        }
    }//end addMultipleNewCustomers
    // method 2. Add single new customer - prompts the user for customer data: customer name, customer id, and total sales
    public static void addSingleNewCustomer(String[] customerName, int[] customerID, double[] customerTotalSales) {
        int firstEmptyIndex = findFirstEmptyIndex(customerName);
        for (int i = firstEmptyIndex; i == firstEmptyIndex; i++) {
            scanner.nextLine(); //clear scanner buffer
            System.out.print("\nPlease enter the customers name:\t");
            customerName[i]=(scanner.nextLine());
            System.out.print("\nPlease enter the customers ID number:\t");
            customerID[i]=(scanner.nextInt());
            System.out.print("\nPlease enter the customers Total Sales:\t");
            customerTotalSales[i]=(scanner.nextDouble());
            System.out.println("Index # " + (i));
            System.out.println(customerName[i]);
            System.out.println(customerID[i]);
            System.out.println(customerTotalSales[i]);
        }
    }//end addSingleNewCustomer
    // method 3. Display all customers - displays each customer's data to the console, one customer per line
    public static void callCustomerList(String[] customerName, int[] customerID, double[] customerTotalSales) {   
        for (int i = 0; i < customerName.length; i++) {
            if (customerName[i] == null) {
                break;
            } else if (customerID[i]>=0){
                System.out.print("\nIndex #: " + (i)+ ";     ");
                System.out.print("Name: " + customerName[i]+ ";     ");
                System.out.print("ID: " + customerID[i]+ ";     ");
                System.out.println("Sales: " + customerTotalSales[i]+ ";     ");
            } 
        }
    }//end callCustomerList
    // method 4. Retrieve specific customer's data - prompts the user for the customer id and displays the
    // corresponding customer's data: customer id, customer name, and total sales
    public static void callSpecificCustomersData(String[] customerName, int[] customerID, double[] customerTotalSales) {
        int customerIDNumberToSearchFor = 0;
        System.out.println("\nPlease enter the customers ID number: ");
        customerIDNumberToSearchFor=(scanner.nextInt());
        for (int i = 0; i<99; i++) {
            if (customerIDNumberToSearchFor == customerID[i]) {
                System.out.println("\nName:" + customerName[i] + "     " + "ID Number: " + customerID[i] + "     " +"Total Sales: "+ customerTotalSales[i]);       
            }
        }
    }
    // method 5. Retrieve customers with total sales based on the range - prompts the user for the lowest and highest
    // total sales and displays all customers with total sales in that range. Display each customer on a separate
    // line with all information – Customer Name, Customer ID, and Total Sales
    public static void callCustomerDataBySales (String[] customerName, int[] customerID, double[] customerTotalSales) {
        System.out.println("\nPlease enter the Total Sales range to find customers data from. Enter the values with a space between them (eg. 500 700):");
        int customerSearchRangeLow = (scanner.nextInt());
        int customerSearchRangeHigh = (scanner.nextInt());
        for (int i = 0; i<99; i++) {
            if (customerTotalSales[i] >= customerSearchRangeLow && customerTotalSales[i] <= customerSearchRangeHigh) {
                System.out.println("\nName: " + customerName[i] + "     " + "ID Number: " + customerID[i] + "     " +"Total Sales: "+ customerTotalSales[i]);
            }
        }
    }
    // 6. Exit method not neccessary
    ///-----------------methods end here-----------------///
}//end class