public class Snack {//begin snack class
    protected String snackID;             //begin class attributes
    protected String sizeOfSnack;
    protected double priceOfSnack;        //end class attributes
    //maybe switch to private latr
    
    /* 
     * (1) There will be a Snack class with following attributes: id (combination of numbers and letters), 
     * size (values S, M, or L), and price
     * (2) On creation, a snack instance must be given all attribute values except its price, which must be calculated
     * (3) Price is calculated as follows:
     *      (a) There is a flat fee of $19.99 for S snack, $29.99 for M snack, and $39.99 for L snack.
     *      (b) FruitSnack has an additional fee of $5.99 when it has a citrus fruit. Please add
     *          only a single citrus fruit, and no preventing coding is required to limit adding more
     *          than one.
     *      (c) SaltySnack has an additional fee of $4.50 when it has a nut snack. Please add
     *          only a single nut snack no preventing coding is required to limit adding more than
     *          one.
     * (4) Each class must have a method to return or display the class’s values to the console
    */

    public Snack (String snackID, String sizeOfSnack, Double priceOfSnack) { //begin snack constructor
        this.snackID=snackID;
        this.sizeOfSnack=sizeOfSnack;
        this.priceOfSnack=priceOfSnack;    
    }//end snack constructor

    public class FruitSnack extends Snack { 
        private boolean hasCitrusFruit = true;
        public FruitSnack (String snackID, String sizeOfSnack, Double priceOfSnack) {
            super(snackID, sizeOfSnack, priceOfSnack);
            this.hasCitrusFruit = hasCitrusFruit;
        }
    }
    public class SaltySnack extends Snack { 
        private boolean hasNuts = true;
        public SaltySnack (String snackID, String sizeOfSnack, Double priceOfSnack) {
            super(snackID, sizeOfSnack, priceOfSnack);
            this.hasNuts = hasNuts;
        }
    }
    //begin methods
    public static double customerSizePricing(String customerSizeChoice, double customerTotalPrice) { //switch case to figure out price
        customerSizeChoice.toUpperCase();
        switch (customerSizeChoice) {
            case "S":
            return customerTotalPrice = 19.99;
            
            case "M":                
            return customerTotalPrice = 29.99;
            
            case "L":                
            return customerTotalPrice = 39.99;
    
        // default:
        //     System.out.println( "That is not an appropriate choice, try again");
        //     break;
        }
        return customerTotalPrice;
    
    }//end methods
    public static void helloworld() {
        System.out.println("Hello World");
    }
}//end snack class    
public static void helloworld() {
    System.out.println("Hello World");
}