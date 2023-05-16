/* Documentation 
 *  Name:    Andrew B. Auxier
 *  Class:   CMIS 242 6385
 *  Date:    2023-03-07
 *  Package Description: This package provides construction of and manipulation for child class(MovieDVD) of parent class(Media)
*/
public class MovieDVD extends Media {
    private double sizeInMegabytes = 0;
    public MovieDVD(int mediaID, String mediaTitle, int mediaYearPublished, double sizeInMegabytes, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.sizeInMegabytes=sizeInMegabytes;
    }
    // get method
		public double getSize() {
			return sizeInMegabytes;
		}

		// set method
		public void setSize(double sizeInMegabytes) {
			this.sizeInMegabytes = sizeInMegabytes;
		}
		public String toString() { //display stuff
			return "MovieDVD [ id=" + getID() + ", title=" + getTitle() + ", year=" + getYear() + ", size=" + getSize()
					+ "MB, available=" + this.isAvailable() + " ]";
		}
}
