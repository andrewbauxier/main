/* 
 * Name:    Andrew B. Auxier
 * Class:   CMIS 242 6385
 * Date:    2023-02-27
 * Package Description: main converter package to provide structure for classes in
 *  following children packages of TemperatureConverter.java and DistanceConverter.java
*/
public class Converter {
    private double input; //user input
    Converter() { //Default input value, Double.NaN
        this.input=Double.NaN;
    }
    //Overloaded constructor with input for parameter
    Converter(double input) {
        this.input = input;
    }
    //Get and set methods for input attribute
    double getInput() { //input private, gets input
        return this.input;
    }
    void setInput(double input) { //input private, sets input
        this.input = input;
    }
    double convert() { //convert method, returns input
        return this.input;
    }
} //end class