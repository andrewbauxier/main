/* TODO: alter this before submitting
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-01-10 
 * This program does stuff
 * 
*/
public class Project {
    public static void main(String[] args) {
        Weight weight1 = new Weight(11, 3);
        Weight weight2 = new Weight(7, 20);
        Weight weight3 = new Weight(14, 6);        
        
        
        
        System.out.println(weight1.toOunces());
        // Test Code Blocks Begin
        // System.out.println(weight1.lessThan(weight2));
        // weight2.toOunces();    // test toOunces method - switch normalize to public first
        // weight2.normalize();   // test normalize method - switch normalize to public first
        // System.out.println( weight1.lessThan(weight2));
        // weight1.addTo(weight2);

        //Test Code Blocks End        // test normalize method - switch normalize to public first
        // weight2.normalize();
    }//end main

    //begin methods
    
    //TODO: Fix this later
    //a sysout display of current objects and their values
    // public void instanceDisplay() {
    //     this.weight1=weight1;
    //     this.weight2=weight2;
    //     this.weight3=weight3;
    //     System.out.println("Weight1 is " + weight1);
    //     System.out.println("Weight2 is " + weight2);
    //     System.out.println("Weight3 is " + weight3);
    // }


    // A private class method named findMinimum with a return type of Weight. This method
    // should accept three Weight objects as parameters and compare each Weight object’s
    // weight values to find the minimum. The Weight object with the minimum weight value
    // should be returned and then printed using toString in the following format:
    // The minimum weight is x pounds and y ounces
    // where x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.

    // A private class method named findMaximum with a return type of Weight. This method
    // should accept three Weight objects as parameters and compare each Weight object’s weight
    // values to find the maximum. The Weight object with the maximum weight value should be
    // returned and then printed using toString in the following format:
    // The maximum weight is x pounds and y ounceswhere x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.

    // A private class method named findAverage with a return type of Weight. This method
    // should accept three Weight objects as parameters and calculate the average weight value. A new
    // Weight object with the average weight values should be returned and then printed using toString
    // in the following format:
    // The average weight is x pounds and y ounces
    // where x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.
    
    // A public method named main with a return type of void. This method should exercise the
    // correct functionality of findMinimum, findMaximum and findAverage by creating three
    // Weight objects using the hardcoded values below:
    // Weight weight1 = new Weight(11, 3);
    // Weight weight2 = new Weight(7, 20); // Hint: normalize method should be
    // used to translate into 8 pounds and 4 ounces
    // Weight weight3 = new Weight(14, 6);
    
    //end methods
}//end class
