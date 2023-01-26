/* TODO: alter this date before submitting
 * Name: Andrew B. Auxier
 * Date: 2023-01-10
 * 
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
    
    private double toOunces() { //TODO: fix this later
        return (this.pounds * OUNCES_IN_A_POUND) + this.ounces;
    }
    public void addTo (Weight weight){
        this.ounces += weight.ounces;
        this.normalize();
        this.pounds += weight.pounds;
    }
    public void normalize() {    
        for (int i = 0; this.ounces>OUNCES_IN_A_POUND/*16*/; i++) {//OUNCES_IN_A_POUND=16
                // this.ounces = this.ounces-OUNCES_IN_A_POUND;
                // this.pounds += this.pounds+1;
                this.ounces -= OUNCES_IN_A_POUND;
                this.pounds += 1;                
        }
        System.out.println("Normalization has occured. The new weight values are : " + toString()); //TODO: testing purposes. delete later
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
    public void divide(int divisor) {
        double noOfOunces = this.toOunces();
        double averageOunces = noOfOunces / divisor;
        int pounds = 0;
        System.out.println(noOfOunces);
        System.out.println(averageOunces);
        System.out.println(pounds);
        if (averageOunces > OUNCES_IN_A_POUND) {
            while (averageOunces > OUNCES_IN_A_POUND) {
                pounds += 1;
                averageOunces = averageOunces - OUNCES_IN_A_POUND;
            }
        }
        this.pounds = pounds;
        this.ounces = averageOunces;
    }
    //end methods
}//end class
