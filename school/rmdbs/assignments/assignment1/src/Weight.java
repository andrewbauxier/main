/*
 * Name: Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date: 2023-01-10
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
    public void divideObject(int divisor) { //divides value that calls it//might be able to refactor and delete
        this.ounces = this.toOunces() / divisor; //converts pounds and ounces to ounces
        this.pounds = 0;//sets object's pounds to 0.
        normalize();
    }//end methods
}//end class
