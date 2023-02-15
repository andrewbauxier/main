/**
 * This program implements a snack ordering system with a Snack class hierarchy and an OrderSystem class.
 * The program calculates the price of a snack based on its size and additional attributes.
 *
 * @author John Doe
 * @date 2023-02-15
 */

 import java.util.Scanner;

 // Snack class hierarchy
 class Snack {
     private String id;
     private char size;
     private double price;
 
     public Snack(String id, char size) {
         this.id = id;
         this.size = size;
         this.price = calculatePrice();
     }
 
     public String getId() {
         return id;
     }
 
     public char getSize() {
         return size;
     }
 
     public double getPrice() {
         return price;
     }
 
     protected double calculatePrice() {
         double flatFee;
         switch (size) {
             case 'S':
                 flatFee = 19.99;
                 break;
             case 'M':
                 flatFee = 29.99;
                 break;
             case 'L':
                 flatFee = 39.99;
                 break;
             default:
                 flatFee = 0;
         }
         return flatFee;
     }
 
     public void displaySnack() {
         System.out.println("Snack type = Snack, of type = " + size + ", id = " + id + ", and price = $" + price);
     }
 }
 
 class FruitSnack extends Snack {
     private boolean citrusFruit;
 
     public FruitSnack(String id, char size, boolean citrusFruit) {
         super(id, size);
         this.citrusFruit = citrusFruit;
         this.calculatePrice();
     }
 
     public boolean getCitrusFruit() {
         return citrusFruit;
     }
 
     @Override
     protected double calculatePrice() {
         double flatFee = super.calculatePrice();
         if (citrusFruit) {
             flatFee += 5.99;
         }
         return flatFee;
     }
 
     @Override
     public void displaySnack() {
         System.out.println("Snack type = Fruit Snack, of type = " + getSize() + ", id = " + getId() + ", and price = $" + getPrice());
     }
 }
 
 class SaltySnack extends Snack {
     private boolean nutSnack;
 
     public SaltySnack(String id, char size, boolean nutSnack) {
         super(id, size);
         this.nutSnack = nutSnack;
         this.calculatePrice();
     }
 
     public boolean getNutSnack() {
         return nutSnack;
     }
 
     @Override
     protected double calculatePrice() {
         double flatFee = super.calculatePrice();
         if (nutSnack) {
             flatFee += 4.50;
         }
         return flatFee;
     }
 
     @Override
     public void displaySnack() {
         System.out.println("Snack type = Salty Snack, of type = " + getSize() + ", id = " + getId() + ", and price = $" + getPrice());
     }
 }
 
 // OrderSystem class
 public class OrderSystem {
     public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);
         int choice = 0;
 
         while (choice != 2) {
             System.out.println("MENU");
             System.out.println("1: Order a Snack");
             System.out.println("2: Exit program");
             System.out.print("Enter your selection: ");
             choice = scanner.nextInt();
 
             if (choice == 1) {
                 System.out.print("Do you want Fruit Snack (1) or Sal
 