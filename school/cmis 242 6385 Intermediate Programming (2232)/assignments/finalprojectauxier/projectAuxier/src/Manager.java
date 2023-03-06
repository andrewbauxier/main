import java.util.Scanner;

public class Manager {
    public static void main(String[] args) {
        runMenu();
    }

    public static void runMenu() {
        Scanner scanner1 = new Scanner(System.in);
        System.out.print("Welcome to Media Rental System.\n1: Load Media objects..."
            + "2: Find Media object...\n3: Rent Media object...\n9: Quit\n\nEnter your selection:\t");
        int menuInput = scanner1.nextInt();
        menuSwitching(menuInput);
    }
    public static void menuSwitching(int menuInput) {
        switch (menuInput) {
            case 1: //Load meadia objects method
                
                break;
            case 2: //Find media object method
                
                break;
            case 3: //Rent Media object
                
                break; 
            case 9: //end program
            
            break;   
            default:
                break;
        }
    }
}
