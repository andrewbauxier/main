/* 
 * Name:    Andrew B. Auxier
 * Class:   CMIS 242 6385
 * Date:    2023-02-16
 * Package Description: Main package for GUIConverter. Converts from miles to km and farenheit to celcius.
*/

/* TODO List [personal]: personal tasks to be done at a later date
 * check to see if converters returned Double.NaN, does not look like they did.
*/
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUIConverter {//begin program
    GUIConverter() { //creates windows and framework for conversion operations
        JFrame framework = new JFrame("Welcome to Converter");
        framework.setSize(1200, 600); //size of window
        JPanel panelMain = new JPanel(new BorderLayout()); // create a main panel and set its layout
        JPanel panelCenter = new JPanel(new GridLayout()); // create a nested panel for the center buttons
        JButton buttonLeft = new JButton("Distance Converter");    //
        JButton buttonRight = new JButton("Temperature Converter");  //
        JButton buttonBottom = new JButton("Exit Program"); // 
        panelCenter.add(buttonLeft); //add left button to center panel
        panelCenter.add(buttonRight); //add right button to center panel
        panelMain.add(panelCenter, BorderLayout.CENTER); //add center panel to main panel
        panelMain.add(buttonBottom, BorderLayout.SOUTH); //add bottom button to main panel        
        framework.add(panelMain); // add main panel to frame
        framework.setVisible(true); //enable main panel visibility
        framework.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //clicking X closes program
        //action listeners begin
        buttonLeft.addActionListener(new ActionListener() {//left button [distance] action listener
            @Override
            public void actionPerformed(ActionEvent e) {
                String distanceInputString = JOptionPane.showInputDialog("Enter Distance In Miles:"); //grab input from user, has to be string
                Double distanceInputDouble = Double.parseDouble(distanceInputString); //converts string to double for further processing
                DistanceConverter distanceResult = new DistanceConverter(distanceInputDouble); //new instance of distconv for processing
                JOptionPane.showMessageDialog(framework,"Distance in KM is " + distanceResult.convert()); //outputs result
            }
        });
        buttonRight.addActionListener(new ActionListener() {//left button [distance] action listener
            @Override
            public void actionPerformed(ActionEvent e) {
                String temperatureInputString = JOptionPane.showInputDialog("Enter Temperature In Fahrenheit :"); //grab input from user, has to be string
                Double temperatureInputDouble = Double.parseDouble(temperatureInputString); //converts string to double for further processing
                TemperatureConverter temperatureResult = new TemperatureConverter(temperatureInputDouble); //new instance of tempconv for processing
                JOptionPane.showMessageDialog(framework,"Temperature in Celsius is " + temperatureResult.convert()); //outputs result
            }
        });
        buttonBottom.addActionListener(new ActionListener() { //exit button
            @Override
            public void actionPerformed(ActionEvent e) {
                framework.dispose();//We dispose the frame f
            }
        }); //action listeners begin
    } //end GUIConverter method
    public static void main(String[] args) { //begin main
        new GUIConverter();//We call the constructor to create the GUI
    }//end main
}//end program