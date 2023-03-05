public class MusicCD extends Media {
    private int lengthInMinutes = 0;
    public MusicCD(int mediaID, String mediaTitle, int mediaYearPublished, boolean isAvailable) {
        super(mediaID, mediaTitle, mediaYearPublished, isAvailable);
        this.lengthInMinutes = lengthInMinutes;
    }
}