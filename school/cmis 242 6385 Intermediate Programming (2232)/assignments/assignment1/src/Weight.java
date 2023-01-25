/* TODO: alter this date before submitting
 * Name: Andrew B. Auxier
 * Date: 2023-01-10
 * todo: f this
 * Weight class should have three private variables, two private methods and four public methods.
 * 1. A private constant variable called OUNCES_IN_A_POUND that defines the number of
 * ounces in a pound (16).
 * 2. A private variable called pounds with a data type of integer.
 * 3. A private variable called ounces with a data type of double
*/
public class Weight {//begin class
    //class attributes
    private int OUNCES_IN_A_POUND = 16;
    private int pounds;
    private double ounces;
    public Weight (int pounds, double ounces) { //begin constructor
        this.pounds=pounds;
        this.ounces=ounces;
    }//end constructor

    //begin methods
    /* 
     * A private instance method called toOunces with a return type of double. This method
     * has no parameters and should return the total number of ounces. For full credit, reuse this method
     * across other methods when possible.
    */
    
    private double toOunces() { //TODO:fix this later
        double totalOunces= (pounds * OUNCES_IN_A_POUND) + ounces; //converts pounds to ounces
        //add existing ounces
        //System.out.println("total ounces: " + totalOunces);
        return totalOunces;
    }

    /* 
     * A public instance method called addTo with a return type of void. This method should
     * accept a Weight object as a parameter and add the object’s weight values to the initialized
     * values.
    */
    public void addTo (Weight weightToBeAdded){
        this.ounces += weightToBeAdded.toOunces();
        System.out.println("addTo complete. New ounces value is: " + this.ounces); //TODO: testing purposes. delete later
    }

    /*
     * A private instance method called normalize with a return type of void. This method has
     * no parameters and should ensure that the number of ounces is less than the number of ounces in a
     * pound. For full credit, reuse this method across other methods when possible.
    */
    private void normalize() {    
        for (int i = 0; this.ounces>OUNCES_IN_A_POUND/*16*/; i++) {//OUNCES_IN_A_POUND=16
                this.ounces = this.ounces-16;
                this.pounds = this.pounds+1;                
        }
        System.out.println("New pounds are : " + this.pounds); //TODO: testing purposes. delete later
        System.out.println("New ounces are : " + this.ounces); //TODO: testing purposes. delete later
    }

    /* 
     * A public instance method called lessThan with a return type of boolean. This method
     * should accept a Weight object as a parameter and determine if the object is greater or less than
     * the initialized values.
    */
    public boolean lessThan(Weight weight) { //value to be compared
        return this.toOunces()<weight.toOunces(); //returns true or false depending on values
    }
    
    /* 
     * public instance method called toString with a return type of String. This method has
     * no parameters and should have the following format: x pounds and y ounces
     * where x is the number of pounds and y the number of ounces. Ounces should be
     * displayed with two decimal places. 
    */
    public String toString() {    
        String stringToDisplayPoundsAndOunces = this.pounds + " pounds and " + String.format("%.2f", this.ounces) + " ounces";
        //System.out.println(stringToDisplayPoundsAndOunces); //for testing
        return stringToDisplayPoundsAndOunces;
    }

    /* 
     * public method that can be and do whatever it wants to be. ideally it combines private method
     * so that they can be used accordingly. 
    */
    public void toBeDetermined() {
        System.out.println("Hello World");
    }
    //end methods
}//end class
