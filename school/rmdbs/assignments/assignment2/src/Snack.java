//part of OrderSystem Project
// Snack class hierarchy
class Snack {
    protected String snackID;
    protected char sizeChoice;
    protected double price = calculatePrice();
    public Snack(String snackID, char sizeChoice, double price) {//constructor
        this.snackID = snackID;
        this.sizeChoice = sizeChoice;
        this.price = price;
    }
    //get methods begin
    public String getId() {
        return snackID;
    }
    public char getSize() {
        return sizeChoice;
    }

    public double getPrice() {
        return price;
    }
    //internal methods for calculating price and displaying snack info 
    protected double calculatePrice() {
        double sizeFee;
        switch (sizeChoice) {
            case 'S':
                return sizeFee = 19.99;
                
            case 'M':
                return sizeFee = 29.99;
                
            case 'L':
                return sizeFee = 39.99;
            default:
                sizeFee  = 0;
        }
        return sizeFee ;
    }
    public void displaySnack() { //display snack class info
        System.out.println("Snack type = " + getClass().getSimpleName() + " of size =" + getSize() + ", id = " + getId() + ", and price = $" + getPrice());
    }
}
class FruitSnack extends Snack {//begin subclass fruitsnack
    private boolean hasCitrus;
    public FruitSnack(String snackID, char sizeChoice, double price, boolean hasCitrus) {
        super(snackID, sizeChoice, price);
        this.hasCitrus = hasCitrus;
        this.price = calculatePrice();
    }
    public boolean getCitrusFruit() {//encapsulation
        return hasCitrus;
    }
    @Override //class override, add fruits
    protected double calculatePrice() {
        double flatFee = super.calculatePrice();
        if (hasCitrus) {
            flatFee += 5.99;
        }
        return flatFee;
    }
    @Override //class override, show fruitsnack instead 
    public void displaySnack() {
        System.out.println("Snack type = " + getClass().getSimpleName() + " of size =" + getSize() + ", id = " + getId() + ", and price = $" + getPrice());
    }
}//end subclass fruitsnack
class SaltySnack extends Snack {//begin subclass saltysnack
    private boolean hasNuts;
    public SaltySnack(String snackID, char sizeChoice, double price, boolean hasNuts) {
        super(snackID, sizeChoice, price);
        this.hasNuts = hasNuts;
        this.price = calculatePrice();
    }
    public boolean getNutSnack() {//encapsulation
        return hasNuts;
    }
    @Override //class override, add nuts
    protected double calculatePrice() {
        double flatFee = super.calculatePrice();
        if (hasNuts) {
            flatFee += 4.50;
        }
        return flatFee;
    }
    @Override //class override, show saltysnack instead
    public void displaySnack() {
        System.out.println("Snack type = " + getClass().getSimpleName() + " of size =" + getSize() + ", id = " + getId() + ", and price = $" + getPrice());
    }
    //looking back, was it even necessary to do these overrides? Wouldn't it show the class regardless? Done is done.
}//end subclass saltysnack