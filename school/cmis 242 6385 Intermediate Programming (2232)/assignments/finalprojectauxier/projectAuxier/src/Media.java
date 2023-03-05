public class Media {
    /* Member variables (attributes): id (integer), title (string), year published (integer)
    Functionality: constructor with all the attribute values, calculate rental fee ($3.50 flat
fee), change title, change year published, and get each attribute value.
 The class should be declared abstract as it represents a generic media and we do not
want to allow a creation of this class directly
 Note that id value cannot be changed after creation.
     * 
    */
    int mediaID;
    String mediaTitle;
    int mediaYearPublished;
    double rentalFee = 3.50;
    boolean isAvailable;
    public Media(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) { //needs get,
        this.mediaID = mediaID;
        this.mediaTitle = mediaTitle;
        this.mediaYearPublished = mediaYearPublished;
        this.isAvailable= isAvailable;
    }

}
