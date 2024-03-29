/* 
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-01-11
 * 
 * This program, including the files Doggo.java and Puppies.java, shows the initialization of the
 * 'doggo' object and allows the user to generate a 'puppy' instance from said object.
*/
public class Doggo {

    //class attritubutes
    public String doggoname;
    public String doggospeech;
    public int doggolegs;
    public int doggoeyes;
    public double doggofat;
    
    //constructor
    public Doggo(String name, String speech, int numlegs, int numeyes, double weight){
        doggoname = name;
        doggospeech = speech;
        doggolegs = numlegs;
        doggoeyes = numeyes;
        doggofat = weight; 
    }

    public void doggostatus() {
        System.out.println("New Doggo is " + doggoname);
        System.out.println(doggoname +" has " + doggolegs + " legs" );
        System.out.println(doggoname +" has " + doggoeyes + " eyes" );
        System.out.println(doggoname +" weighs " + doggofat + " kilograms" );
        System.out.println(doggoname + " says " + "'" + doggospeech + "'");   
    }
}
