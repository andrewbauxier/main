/* 
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-01-25 
 * This program provides proof of knowledge of concepts relating to encapsulation
 * and object-oriented program by performing calculations using Weight objects 
 * (instances of Weight class)
*/

/* TODO List [project]: tasks to be done before submitting
 * alter date
 * 
*/
/* TODO List [personal]: personal tasks to be done at a later date
 * Ask Luke if there's a better way to reactor those ugly if/else statements
*/
public class Project {
    public static void main(String[] args) {
        Weight weight1 = new Weight(11, 3);
        Weight weight2 = new Weight(7, 20);
        Weight weight3 = new Weight(14, 6);
        Weight[] weightArray = {weight1, weight2, weight3};
        getMinMaxAvg(weightArray);

        // Test Code Blocks Begin
        // System.out.println(weight1.lessThan(weight2));
        // System.out.println(weight1.toOunces()); // switch normalize to public first
        // weight2.normalize(); // switch normalize to public first
        // weight2.normalize(); // switch normalize to public first
        // System.out.println(weight1.lessThan(weight2));
        // weight1.addTo(weight2);
        // System.out.println(weight1.toString());
        // weight2.normalize();
        // Test Code Blocks End //

    }// end main
    // begin methods
    // finished
    // A private class method named findMinimum with a return type of Weight. This
    // method
    // should accept three Weight objects as parameters and compare each Weight
    // object’s
    // weight values to find the minimum. The Weight object with the minimum weight
    // value
    // should be returned and then printed using toString in the following format:
    // The minimum weight is x pounds and y ounces
    // where x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.
    
    private static Weight findMinimum(Weight[] weightArray) {
    //weight1.normalize(); shouldn't I do this?
        Weight minValue = weightArray[0];
        for (int i = 0; i < weightArray.length; i++)
        if (weightArray[i].lessThan(minValue)) {
            minValue = weightArray[i]; //return the first weight as the smallest weight
        }
        minValue.normalize();
        System.out.println("\nThe minimum weight is " + minValue.toString());
        return minValue;
    }        

    // A private class method named findMaximum with a return type of Weight. This
    // method
    // should accept three Weight objects as parameters and compare each Weight
    // object’s weight
    // values to find the maximum. The Weight object with the maximum weight value
    // should be
    // returned and then printed using toString in the following format:
    // The maximum weight is x pounds and y ounceswhere x is the number of pounds
    // and y the number of ounces. Ounces should be
    // displayed with two decimal places.

    private static Weight findMaximum(Weight[] weightArray) {
    //weight1.normalize(); shouldn't I do this?
        Weight maxValue = weightArray[0];
        for (int i = 0; i < weightArray.length; i++) {
            if (maxValue.lessThan(weightArray[i])) {
                maxValue = weightArray[i];
            }
        }
        System.out.println("\nThe maximum weight is " + maxValue.toString());
        return maxValue;
    }

    // A private class method named findAverage with a return type of Weight. This
    // method should accept three Weight objects as parameters and calculate the average
    // weight value. A new Weight object with the average weight values should be returned and then
    // printed using toString in the following format:
    // "The average weight is x pounds and y ounces"
    // where x is the number of pounds and y the number of ounces. Ounces should be
    // displayed with two decimal places.
    private static Weight findAverage(Weight[] weightArray) {
        Weight weightAverage = new Weight(0, 0);
        // for (int j = 0; j < weightArray.length; j++) {
        //     weightAverage.addTo(weightArray[j]);
        // } 
        //keeping just in case
        for (Weight weight : weightArray) {
            weightAverage.addTo(weight);
        }
        weightAverage.divide(3);
        System.out.println("\nThe average weight is " + weightAverage.toString());
        return weightAverage;
    }

    // A public method named main with a return type of void. This method should
    // exercise the
    // correct functionality of findMinimum, findMaximum and findAverage by creating
    // three
    // Weight objects using the hardcoded values below:
    // Weight weight1 = new Weight(11, 3);
    // Weight weight2 = new Weight(7, 20); // Hint: normalize method should be
    // used to translate into 8 pounds and 4 ounces
    // Weight weight3 = new Weight(14, 6);
    public static void getMinMaxAvg(Weight[] weightArray) {
        findMinimum(weightArray);
        findMaximum(weightArray);
        findAverage(weightArray);
    }
    // end methods
}// end class