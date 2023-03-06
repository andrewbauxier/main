import java.util.*;

public class Ebook extends Media {
    private int numberOfChapters = 0;
    public Ebook(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.numberOfChapters = numberOfChapters; //Error: has no effect; may be redundant
    }
    // get method
    public int getNumChapters() {
        return numberOfChapters;
    }
    // set method
    public void setNumChapters(int numChapters) {
        this.numberOfChapters = numberOfChapters;
    }
    @Override //adding base fee and new release fee
    public double totalPrice() {
        double rentalFee = numberOfChapters * 0.10; // basic fee
        int currentYear = Calendar.getInstance().get(Calendar.YEAR); //adjusting year to find if needs new release fee
        if (this.getYear() == currentYear)
        rentalFee += 1; //applied new release fee
        return rentalFee;
    }
    @Override //display stuff
    public String toString() {
        return "EBook [ id=" + getId() + ", title=" + getTitle() + ", year=" + getYear() + ", chapters="
                + numberOfChapters + ", available=" + this.isAvailable() + " ]";
    }
}
