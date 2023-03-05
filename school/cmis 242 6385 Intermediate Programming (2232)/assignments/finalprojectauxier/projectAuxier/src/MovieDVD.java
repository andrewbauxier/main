public class MovieDVD extends Media {
    private int sizeInMegabytes = 0;
    public MovieDVD(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.sizeInMegabytes=sizeInMegabytes;
    }
}
