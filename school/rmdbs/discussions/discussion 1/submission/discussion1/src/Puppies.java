/* 
 * Name:    Andrew B. Auxier
 * Class:   Class:CMIS 242 6385
 * Date:    2023-01-11
 * 
 * This program, including the files Doggo.java and Puppies.java, shows the initialization of the
 * 'doggo' object and allows the user to generate a 'puppy' instance from said object.
*/
public class Puppies {
    public static void main(String[] args) { //inputs = (String n, String speech, int numlegs, int numeyes, double weight)
        System.out.println("Name:\tAndrew Auxier\nClass:\tCMIS 242 6385\nDate:\t1/9/2023\n");
        Doggo doggo1 = new Doggo(null, null, 0, 0, 0);
        Doggo doggo2 = new Doggo("Mr. Cuddlesworth", "Seize the means of production!", 10, 4, 22.5);
        doggo1.doggostatus();
        System.out.println("");
        doggo2.doggostatus();
        
        
    }
}