/* Documentation 
 *  Name:    Andrew B. Auxier
 *  Class:   CMIS 242 6385
 *  Date:    2023-03-07
 *  Package Description: This package provides construction of and manipulation for child class(Ebook) of parent class(Media)
*/
import java.util.*;

public class Ebook extends Media {
    private int numberOfChapters = 0;
    public Ebook(int mediaID, String mediaTitle, int mediaYearPublished, int numberOfChapters, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.numberOfChapters = numberOfChapters; 
    }
    // get method
    public int getNumChapters() {
        return numberOfChapters;
    }
    // set method
    public void setNumChapters(int numChapters) {
        //his.numberOfChapters = numberOfChapters;
    }
    @Override //adding base fee and new release fee
    public double totalPrice() {
        double rentalFee = numberOfChapters * 0.10; // basic fee
        int currentYear = Calendar.getInstance().get(Calendar.YEAR); //adjusting year to find if needs new release fee
        if (this.getYear() == currentYear)
        rentalFee += 1; //applied new release fee
        return rentalFee; //
    }
    @Override //display stuff
    public String toString() {
        return "EBook [ id=" + getID() + ", title=" + getTitle() + ", year=" + getYear() + ", chapters="
                + numberOfChapters + ", available=" + this.isAvailable() + " ]";
    }
}
