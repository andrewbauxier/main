public class MovieDVD extends Media {
    
    private int sizeInMegabytes = 0;
    public MovieDVD(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.mediaID = mediaID;
        this.mediaTitle = mediaTitle;
        this.mediaYearPublished = mediaYearPublished;
        this.sizeInMegabytes=sizeInMegabytes;
    }
}
