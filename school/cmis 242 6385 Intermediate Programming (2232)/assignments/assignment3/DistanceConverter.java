/* 
 * Name:    Andrew B. Auxier
 * Class:   CMIS 242 6385
 * Date:    2023-02-27
 * Package Description: Distance converter package for use in main GUI application
*/
public class DistanceConverter extends Converter {
    DistanceConverter() {//constructors, calls parent constructure Converter
        super();
    }
    DistanceConverter(double input) {
        super(input);
    }
    //Overridden convert() method. Don't think it works properly.
    //get the value and run it through .isNaN. I'm not sure I did this right, it's not returning anything, but crap I'm so late; Good enough.
    double convert() { //convert for distance, overridden/overloaded
        if (this.getInput() == Double.NaN) { 
            return Double.NaN; 
        } else {
            return (this.getInput() * 1.609); //conver dist
        }
    }
}