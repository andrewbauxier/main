/* Documentation 
 *  Name:    Andrew B. Auxier
 *  Class:   CMIS 242 6385
 *  Date:    2023-03-07
 *  Package Description: This package provides construction of and manipulation for child class(MusicCD) of parent class(Media)
*/
import java.util.*;
public class MusicCD extends Media {
    private int lengthInMinutes = 0;
    public MusicCD(int mediaID, String mediaTitle, int mediaYearPublished, int lengthInMinutes, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.lengthInMinutes = lengthInMinutes;
    }
    // get method
    public int getLength() {
        return lengthInMinutes;
    }

    // set method
    public void setLength(int lengthInMinutes) {
        this.lengthInMinutes = lengthInMinutes;
    }

    // override parent's
    @Override
    public double totalPrice() {
        double fee = lengthInMinutes * 0.02; // basic fee
        int currYear = Calendar.getInstance().get(Calendar.YEAR);
        if (this.getYear() == currYear)
            fee += 1; // add $1.00 fee
        return fee;
    }

    @Override
    public String toString() {
        return "MusicCD [ id=" + getID() + ", title=" + getTitle() + ", year=" + getYear() + ", length="
                + getLength() + "min, available=" + this.isAvailable() + " ]";
    }
}