public abstract class Media {
    /* Member variables (attributes): id (integer), title (string), year published (integer)
    Functionality: constructor with all the attribute values, calculate rental fee ($3.50 flat
fee), change title, change year published, and get each attribute value.
 The class should be declared abstract as it represents a generic media and we do not
want to allow a creation of this class directly
 Note that id value cannot be changed after creation.
     * 
    */
    private int mediaID;
    private String mediaTitle;
    private int mediaYearPublished;
    private boolean isAvailable;
    //private double rentalFee = 3.50;
        //maybe dont put this here
    public Media(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) { //needs get,
        this.mediaID = mediaID;
        this.mediaTitle = mediaTitle;
        this.mediaYearPublished = mediaYearPublished;
        this.isAvailable= isAvailable;
    }

    // getters and setters
    public int getId() {
        return this.mediaID;
    }
    public String getTitle() {
        return this.mediaTitle;
    }
    public int getYear() {
        return this.mediaYearPublished;
    }
    public boolean isAvailable() {
        return isAvailable;
    }
    protected void setTitle(String title) {
        this.mediaTitle = mediaTitle;
    }
    protected void setYear(int year) {
        this.mediaYearPublished = mediaYearPublished;
    }
    protected void setAvailable(boolean available) {
        this.isAvailable = isAvailable;
    }
    public double totalPrice() {
        return 3.50;
    }
}
