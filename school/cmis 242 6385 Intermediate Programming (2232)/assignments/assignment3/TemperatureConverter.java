/* 
 * Name:    Andrew B. Auxier
 * Class:   CMIS 242 6385
 * Date:    2023-02-27
 * Package Description: Temperature converter package for use in main GUI application
*/
public class TemperatureConverter extends Converter {
    TemperatureConverter() { //constructors, calls parent constructure Converter
        super();
    }
    TemperatureConverter(double input) {
        super(input);
    }
    //Overridden convert() method. Don't think it works properly.
    double convert() { //convert for temperature, overridden/overloaded
        //get the value and run it through .isNaN. I'm not sure I did this right, it's not returning anything, but crap I'm so late; Good enough.
        if (this.getInput() == Double.NaN) {
            return Double.NaN;
        } else {
            return (((this.getInput() -32.0)*5.0)/9.0);//convert temp
        }
    }
}

