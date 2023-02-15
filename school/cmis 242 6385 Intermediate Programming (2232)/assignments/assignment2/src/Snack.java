public class Snack {//begin snack class
    private String snackID;             //begin class attributes
    private char snackSize;
    private double snackPrice;        //end class attributes
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

    public Snack (String snackID, char sizeOfSnack, Double priceOfSnack) { //begin snack constructor
        this.snackID=snackID;
        this.snackSize=snackSize;
        this.snackPrice=snackPrice;    
    }//end snack constructor

    public class FruitSnack extends Snack { 
        private boolean hasCitrus = true;
        public FruitSnack (String snackID, char snackSize, Double snackPrice) {
            super(snackID, snackSize, snackPrice);
            this.hasCitrus = hasCitrus;
        }
    }
    public class SaltySnack extends Snack { 
        private boolean hasNuts = true;
        public SaltySnack (String snackID, char snackSize, Double snackPrice) {
            super(snackID, snackSize, snackPrice);
            this.hasNuts = hasNuts;
        }
    }

    //begin methods
    public void calculatePrice() { //calculate snack price based on size plus additives //TODO: Also add in fruit and nut prices
        if (snackSize == 's') {
            snackPrice = 19.99;
        } else if (snackSize == 'm') {
            snackPrice = 29.99;
        } else if (snackSize == 'l') {
            snackPrice = 39.99;
        }
    }
    //getters and setters
    public String getSnackID() {
        return snackID;
    }
    public void setSnackID(String snackID) {
        this.snackID=snackID;
    }
    public String getSnackSize() {
        return snackID;
    }
    public void setSnackSize(char snackSize) {
        this.snackSize=snackSize;
    }
    // Display the snack's attributes
    public void display() {
        System.out.println("Snack ID: " + snackID);
        System.out.println("Snack size: " + snackSize);
        System.out.println("Snack price: $" + snackPrice);
        
    }

    //end methods
}//end snack class    
