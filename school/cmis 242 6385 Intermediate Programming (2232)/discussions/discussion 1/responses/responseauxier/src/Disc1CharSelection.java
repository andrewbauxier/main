class Disc1CharSelection {
	//stating variable types and initial value
	public static void main(String[] args) {
		String charname = null;
		String chartype = null;
		int age = 0;
		int exp = 0;
		String inventory = "nothing";

		//display welcome message
		System.out.println("Welcome to Character Creation.\n");
		System.out.println("Please enter data below\n");
		
		//Main method, create new character with listed attributes
		//Call methods from CharCreate java
		CharCreate firstChar = new CharCreate(charname, chartype, age, exp, inventory);
		firstChar.charMake();
		firstChar.charDisplay();
		firstChar.initialStart();
		firstChar.starterLayout();
		firstChar.charDisplay();
	}
}
