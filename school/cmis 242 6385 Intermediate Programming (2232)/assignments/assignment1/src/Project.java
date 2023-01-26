/* 
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-01-25 
 * This program provides proof of knowledge of concepts relating to encapsulation
 * and object-oriented program by performing calculations using Weight objects 
 * (instances of Weight class)
*/

/* TODO List [project]: tasks to be done before submitting
 * clean-up
 * 
*/
/* TODO List [personal]: personal tasks to be done at a later date
 * refactor divide, maybe delete it. seems like it could be unneccessary.
*/
public class Project {
    public static void main(String[] args) {
        Weight weight1 = new Weight(11, 3);
        Weight weight2 = new Weight(7, 20);
        Weight weight3 = new Weight(14, 6);
        Weight[] weightArray = {weight1, weight2, weight3};
        
        getMinMaxAvg(weightArray);
    }// end main
    //begin methods
    private static Weight findMinimum(Weight[] weightArray) { 
        Weight minValue = weightArray[0];
        for (int i = 0; i < weightArray.length; i++)
        if (weightArray[i].lessThan(minValue)) {
            minValue = weightArray[i]; //return the first weight as the smallest weight
        }
        minValue.normalize();
        System.out.println("\nThe minimum weight is " + minValue.toString());
        return minValue;
    }        
    private static Weight findMaximum(Weight[] weightArray) {
        Weight maxValue = weightArray[0];
        for (int i = 0; i < weightArray.length; i++) {
            if (maxValue.lessThan(weightArray[i])) {
                maxValue = weightArray[i];
            }
        }
        System.out.println("The maximum weight is " + maxValue.toString());
        return maxValue;
    }
    private static Weight findAverage(Weight[] weightArray) {
        Weight weightAverage = new Weight(0, 0);
        for (Weight weight : weightArray) {
            weightAverage.addTo(weight);
        }
        weightAverage.divideObject(weightArray.length);
        System.out.println("The average weight is " + weightAverage.toString() + "\n");
        return weightAverage;
    }
    public static void getMinMaxAvg(Weight[] weightArray) {
        findMinimum(weightArray);
        findMaximum(weightArray);
        findAverage(weightArray);
    }// end methods
}// end class