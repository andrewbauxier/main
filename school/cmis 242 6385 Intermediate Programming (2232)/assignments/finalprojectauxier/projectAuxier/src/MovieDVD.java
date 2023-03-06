public class MovieDVD extends Media {
    private double sizeInMegabytes = 0;
    public MovieDVD(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) {
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

		// inherits calculate rental fee method and no different calculation so should
		// not override
		@Override
		public String toString() { //display stuff
			return "MovieDVD [ id=" + getId() + ", title=" + getTitle() + ", year=" + getYear() + ", size=" + getSize()
					+ "MB, available=" + this.isAvailable() + " ]";
		}
}
