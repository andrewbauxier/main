/* TODO: alter this before submitting
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-01-10 
 * This program does stuff
 * 
*/

/* TODO List
 * Ask luke if there's a better way to reactor those ugly if/else statements
*/
public class Project {
    public static void main(String[] args) {
        Weight weight1 = new Weight(11, 3);
        Weight weight2 = new Weight(7, 20);
        Weight weight3 = new Weight(14, 6);        
        findMinimum(weight1, weight2, weight3); //TODO: Works, but looks sloppy. refactor later.
        
        //instanceDisplay(weight1);
        // Test Code Blocks Begin
        
        // System.out.println(weight1.lessThan(weight2));
        // System.out.println(weight1.toOunces()); // switch normalize to public first
        // weight2.normalize(); // switch normalize to public first
        // weight2.normalize(); // switch normalize to public first
        // System.out.println(weight1.lessThan(weight2));
        // weight1.addTo(weight2);
        // System.out.println(weight1.toString());
        
        // Test Code Blocks End //
        
    }//end main

    //begin methods
    
    //TODO: Fix this later
    //a sysout display of current objects and their values
    // public static void instanceDisplay(Weight weight) {
    //     System.out.println("The weight is " + weight);
    // }

    // A private class method named findMinimum with a return type of Weight. This method
    // should accept three Weight objects as parameters and compare each Weight object’s
    // weight values to find the minimum. The Weight object with the minimum weight value
    // should be returned and then printed using toString in the following format:
    // The minimum weight is x pounds and y ounces
    // where x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.
    //TODO: refactor all of these methods late. they look sloppy
    public static Weight findMinimum(Weight weight1, Weight weight2, Weight weight3) { 
      //weight1.normalize(); shouldn't I do this?
      Weight minValue;
      if(weight1.lessThan(weight2) && weight1.lessThan(weight3)){
        minValue = weight1; //return the first weight as the smallest weight
        } else if (weight2.lessThan(weight1) && weight2.lessThan(weight3)){//else if the second weight is smaller than the first & third weight
          //return the second weight as the smallest weight
            minValue = weight2;
          } else {//else the third weight is smaller than the first & second weight
              minValue = weight3;// return the third weight as the smallest weight
            }
      System.out.println("\nThe minimum weight is " + minValue.toString());
      return minValue;
    }

    // A private class method named findMaximum with a return type of Weight. This method
    // should accept three Weight objects as parameters and compare each Weight object’s weight
    // values to find the maximum. The Weight object with the maximum weight value should be
    // returned and then printed using toString in the following format:
    // The maximum weight is x pounds and y ounceswhere x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.
    public static Weight findMaximum(Weight weight1, Weight weight2, Weight weight3) {
      //weight1.normalize(); shouldn't I do this?
      Weight maxValue;
      if(weight1.lessThan(weight2) && weight1.lessThan(weight3)){
        maxValue = weight1; //return the first weight as the smallest weight
      } else if (weight2.lessThan(weight1) && weight2.lessThan(weight3)){//else if the second weight is smaller than the first & third weight
          //return the second weight as the smallest weight
          maxValue = weight2;
        } else {//else the third weight is smaller than the first & second weight
            maxValue = weight3;// return the third weight as the smallest weight
          }
    }
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
