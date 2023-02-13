public class Snack {//begin snack class
    protected String snackID;             //begin class attributes
    protected String sizeOfSnack;
    protected double priceOfSnack;        //end class attributes
    /* 
     *  (1) There will be a Snack class with following attributes: id (combination of numbers and letters), 
        size (values S, M, or L), and price
    */

    public Snack (String snackID, String sizeOfSnack, Double priceOfSnack) { //begin snack constructor
        this.snackID=snackID;
        this.sizeOfSnack=sizeOfSnack;
        this.priceOfSnack=priceOfSnack;    
    }//end snack constructor

    public class FruitSnack extends Snack { 
        private boolean hasFruit = true;
        public FruitSnack (String snackID, String sizeOfSnack, Double priceOfSnack) {
            super(snackID, sizeOfSnack, priceOfSnack)
        }
    }
// //begin methods
// private void exampleMethod() { //converts from pounds and ounces to ounces
// }//end methods
}//end snack class    