/* Documentation 
 *  Name:    Andrew B. Auxier
 *  Class:   CMIS 242 6385
 *  Date:    2023-03-07
 *  Package Description: This program loada a media object from a file, finds a media objec by title, and rents 
 *      a media object out if available. 
 *
 *  File Legend:
 *    EBook.txt 
 *      101,SampleBook1,2001,110,true
 *    MovieDVD.txt
 *      201,SampleDVD1,2004,140,true
 *    MusicCD.txt
 *      301,SampleCD1,2007,170,false
 * 
 *  TO-DO:
 *      Figure out why I could not get it to load mutliple objects at once. It appears like it did not, but maybe it did.
*/


import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Manager {
    // attribute
    List<Media> mediaObjects;
    // constructor
    public Manager() {
        mediaObjects = new ArrayList<Media>();
    }
    public void LoadMedias(String directory) { //begin load medias. starts process to load medias, switch case 1 in MRS
        // initialize empty medias list
        this.mediaObjects = new ArrayList<Media>();
        // Create a File object for directory
        File directoryPath = new File(directory);
        // Get list of all files and directories
        File files[] = directoryPath.listFiles();
        if (files == null) {
            System.out.println("File cannot be opened: Could not load, no such directory.");
            return;
        }
        // begin local variables
        Media media = null;
        String line = null;
        String[] fileIterator = null;
        int mediaID;
        String mediaTitle = null;
        int mediaYearPublished;
        boolean isAvailable;
        Scanner scanner = null;
        // end local variables
        for (File file : files) { //begin loading objects
            if (file.getName().contains("EBook") || file.getName().contains("MovieDVD") // parse files depending on type
                    || file.getName().contains("MusicCD")) {
                try { //tries to open file and read lines based on type
                        scanner = new Scanner(file); //initiate scanner
                        line = scanner.nextLine(); 
                        fileIterator = line.split(","); //decided what to enter as what
                        mediaID = Integer.parseInt(fileIterator[0]);
                        mediaTitle = fileIterator[1];
                        mediaYearPublished = Integer.parseInt(fileIterator[2]);
                        isAvailable = Boolean.parseBoolean(fileIterator[4]);
                            if (file.getName().contains("EBook")) { //calls Ebook constructor
                                int numberOfChapters = Integer.parseInt(fileIterator[3]);
                                media = new Ebook(mediaID, mediaTitle, mediaYearPublished, numberOfChapters, isAvailable);
                            }
                            if (file.getName().contains("MovieDVD")) { //calls MusicDVD constructor
                                double sizeInMegabytes = Double.parseDouble(fileIterator[3]);
                                media = new MovieDVD(mediaID, mediaTitle, mediaYearPublished, sizeInMegabytes, isAvailable);
                            }
                            if (file.getName().contains("MusicCD")) { //calls MusicCD constructor
                                int lengthInMinutes = Integer.parseInt(fileIterator[3]);
                                media = new MusicCD(mediaID, mediaTitle, mediaYearPublished, lengthInMinutes, isAvailable);
                            } 
                    this.addMedia(media); //add to attribute
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } 
            } 
        }displayAllMedias();// display all media loaded, end loading objects
    }//end loading media
    public void findMedia(String mediaTitle) { //begin finding media
        boolean found = false; //
        for (Media media : mediaObjects) {
            if (media.getTitle().equals(mediaTitle)) {
                System.out.println(media.toString());
                found = true;
            }
        }
        if (!found)
            System.out.println("There is no media with this title: " + mediaTitle);
    } //end finding media
    public void rentMedia(int mediaID) { //begin renting media
        boolean found = false;
        for (Media media : mediaObjects) {
            if (media.getID() == mediaID) {
                found = true;
                if (media.isAvailable()) {
                    media.setAvailable(false); //checkout media
                    String formattedRentalFee = String.format("%.2f", media.totalPrice()); //rental fee
                    System.out.println(
                            "Media was successfully rented out. Rental fee = $" + formattedRentalFee);
                } else {
                    System.out.println("Media with mediaID=" + mediaID + " is not available for rent.");
                    
                }
                break;
            }
        }
        if (!found) {
            System.out.println("The media object mediaID=" + mediaID + " is not found.");
        }
    }
    public void displayAllMedias() { //display all media
        for (Media media : mediaObjects) {
            System.out.println(media.toString());
        }
    }
    public void addMedia(Media media) { //add media
        this.mediaObjects.add(media);
    }
}

