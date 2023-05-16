private static Weight findMinimum(Weight[] weightArray) { 
    Weight minValue = weightArray[0];
    // for (int i = 0; i < weightArray.length; i++)
    // if (weightArray[i].lessThan(minValue)) {
    //     minValue = weightArray[i]; //return the first weight as the smallest weight
    // }
    for (Weight weight : weightArray) {
        
        
        // if (minValue.lessThan(weight)) {
        //     return minValue;
        // } else {
        //     return minValue;
        // }
        // return minValue.lessThan(weight)
        // minValue.lessThan(weight);
        // System.out.println("weight " + weight);
        // System.out.println("minvalue " + minValue);

        //if (weight.lessThan(weight)==true) {
        //   minValue = weight;
        //     System.out.println(weight);
        //}
        
    }
    minValue.normalize();
    System.out.println("\nThe minimum weight is " + minValue.toString());
    return minValue;
}