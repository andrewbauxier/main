public class Ebook extends Media {
    private int numberOfChapters = 0;
    public Ebook(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.mediaID = mediaID;
        this.mediaTitle = mediaTitle;
        this.mediaYearPublished = mediaYearPublished;
        this.numberOfChapters = numberOfChapters;
    }
}