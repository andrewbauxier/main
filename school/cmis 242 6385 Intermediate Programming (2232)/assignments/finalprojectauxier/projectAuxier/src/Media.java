/* Documentation 
 *  Name:    Andrew B. Auxier
 *  Class:   CMIS 242 6385
 *  Date:    2023-03-07
 *  Package Description: This package provides construction of and manipulation for parent class media
*/
public abstract class Media {
    private int mediaID;
    private String mediaTitle;
    private int mediaYearPublished;
    private boolean isAvailable;
    //private double rentalFee = 3.50;
        //maybe dont put this here
    public Media(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) { 
        this.mediaID = mediaID;
        this.mediaTitle = mediaTitle;
        this.mediaYearPublished = mediaYearPublished;
        this.isAvailable= isAvailable;
    }

    // getters and setters
    public int getID() {
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