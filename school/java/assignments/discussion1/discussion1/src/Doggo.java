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
