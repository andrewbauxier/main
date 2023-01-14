//Don Quinn			CMIS 242 6385		 13 Jan 2023

import java.util.Scanner;
//main method, creating character object and character attributes
public class CharCreate {
	String charName;
	String charType;
	int charAge;
	int charExp;
	String charInventory;
	
	//Assigning values to constructor
	public CharCreate(String name, String type, int age, int exp, String inventory) {
		
		charName = name;
		charType = type;
		charAge = age;
		charExp = exp;
		charInventory = inventory;
	}
	
	//Display questions, enable user data inputs, displays data inputs
	public void charMake() {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter your character name:");
		charName = scan.nextLine();
		System.out.println("\nEnter your class(Warrior, Knight, Thief, Hunter, Mage)");
		charType = scan.nextLine();
		System.out.println("\nEnter your character age:");
		charAge = scan.nextInt();
		scan.close();
		
	}

	//Display text after data inputs, change value of initial variable exp from 0 to 5,000
	public void initialStart() {
		System.out.println("\nCongratulations on creating your first character!");
		System.out.println("\nYou have gained 5,000 exp.");
		charExp = 5000;
	}
	//Displays character information along with new exp value
	public void charDisplay() {
		System.out.println("\nName: \t\t" + charName);
		System.out.println("Class: \t\t" + charType);
		System.out.println("Age: \t\t" + charAge);
		System.out.println("Exp: \t\t" + charExp);
		System.out.println("Inventory: \t" + charInventory);
	}
	//gives the PC a sword, because it's dangerous to go alone, yo.
	public void starterLayout() {
		System.out.println("\nIt's dangerous to go alone, take this!");
		charInventory = "Sword";
		System.out.println("Your inventory: " + charInventory);
	}
	
}
