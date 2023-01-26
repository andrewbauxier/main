/*
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
    
    private int OUNCES_IN_A_POUND = 16;//begin class attributes
    private int pounds;
    private double ounces; //end class attributes
    public Weight (int pounds, double ounces) { //begin constructor
        this.pounds=pounds;
        this.ounces=ounces;
        if (this.ounces>OUNCES_IN_A_POUND) {
            normalize();
        }
    }//end constructor

    //begin methods
    /* 
     * A private instance method called toOunces with a return type of double. This method
     * has no parameters and should return the total number of ounces. For full credit, reuse this method
     * across other methods when possible.
    */
    private double toOunces() { //converts from pounds and ounces to ounces
        return (this.pounds * OUNCES_IN_A_POUND) + this.ounces;
    }
    public void addTo (Weight weight){ //combines two weights
        this.ounces += weight.ounces; 
        this.normalize(); //converts from ounces to pounds and ounces
        this.pounds += weight.pounds; 
    }
    public void normalize() { //converts from ounces to pounds and ounces
        for (int i = 0; this.ounces>OUNCES_IN_A_POUND; i++) {//OUNCES_IN_A_POUND=16
                this.ounces -= OUNCES_IN_A_POUND; //converts ounces to pounds part1
                this.pounds += 1;                 //converts ounces to pounds part2
        }
    }
    public boolean lessThan(Weight weight) { //compare two values to find lesser value
        return this.toOunces()<weight.toOunces(); //returns true or false depending on values
    }
    public String toString() { //displays pounds and ounces(in .xx format)
        String stringToDisplayPoundsAndOunces = this.pounds + " pounds and " + String.format("%.2f", this.ounces) + " ounces";
        return stringToDisplayPoundsAndOunces;
    }
public void divide(int divisor) { //divides value that calls it
        double noOfOunces = this.toOunces(); //converts to ounces
        double averageOunces = noOfOunces / divisor; //divides the ounces
        int pounds = 0; //sets pounds variable
        if (averageOunces > OUNCES_IN_A_POUND) { //iterates until
            while (averageOunces > OUNCES_IN_A_POUND) {
                pounds += 1;
                averageOunces -= OUNCES_IN_A_POUND;
            }
        }
        this.pounds = pounds;
        this.ounces = averageOunces;
    }
    //end methods
}//end class
