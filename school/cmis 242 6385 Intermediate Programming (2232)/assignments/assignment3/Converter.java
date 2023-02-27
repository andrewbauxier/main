/* 
 * Name:    Andrew B. Auxier
 * Class:   CMIS 242 6385
 * Date:    2023-02-16
 * Package Description: Temperature converter package for use in main GUI application
*/
/**
 * Converter
 */
public class Converter {

    private double input; //Private attribute for input of data type double
    //Default constructor with no parameter which sets input to Double.NaN
    Converter() {
        this.input=Double.NaN;
    }
    //Overloaded constructor with input for parameter
    Converter(double input) {
        this.input = input;
    }
    //Get and set methods for input attribute
    double getInput() {
        return this.input;
    }
    void setInput(double input) {
        this.input = input;
    }
    //Method convert() which returns input value
    double convert() {
        return this.input;
    }
    
    class TemperatureConverter extends Converter {
        //Constructors which call parent constructors
        TemperatureConverter() {
            super();
        }
        TemperatureConverter(double input) {
            super(input);
        }
        //Overridden convert() method to convert input (Fahrenheit temperature) to Celsius and returns the value. If the instance has no input value, it should return Double.NaN
        double convert() {
            if(super.getInput(input) == Double.NaN) {//We use getter method of super class to get input value and check if it has default value. If yes, we return same as result, otherwise we calculate temperature in Celsius
                return Double.NaN;
            } else {
                return ((super.getInput()-32.0)*5.0)/9.0;
            }
        }
    }

    class DistanceConverter extends Converter {
        //Constructors which call parent constructors
        DistanceConverter() {
        super();
        }
        DistanceConverter(double input) {
        super(input);
        }
        //Overridden convert() method to convert input (distance in miles) to distance in kilometers and returns the value. If the instance has no input value, it should return Double.NaN
            double convert() {
            if(super.getInput() == Double.NaN) //We use getter method of super class to get input value and check if it has default value. If yes, we return same as result, otherwise we calculate distance in KM
            {
                return Double.NaN;
            } else {
                return super.getInput() * 1.609;
            }
        }
    }
}