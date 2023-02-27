/* 
 * Name:    Andrew B. Auxier
 * Class:   CMIS 242 6385
 * Date:    2023-02-16
 * Package Description:
*/

/* TODO List [project]: tasks to be done before submitting
 * Finish description
 * 
*/

/* TODO List [personal]: personal tasks to be done at a later date
 * 
*/

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class GUIConverter {
    GUIConverter() {
        
        JFrame framework = new JFrame("Welcome to Converter, comrade");
        framework.setSize(1200, 600); //size for program
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
        

        /* 
        JFrame framework= new JFrame("Converter");//Implement GUIConverter class using JFrame and JPanel
        framework.setLayout (new BorderLayout());
        JPanel centerPanel=new JPanel();
        centerPanel.setLayout(new GridLayout());
        JPanel bottomPanel=new JPanel();
        centerPanel.setLayout(new GridLayout());
        
        JButton buttonLeft=new JButton("Distance Converter");//GUI will have 3 buttons: “Distance Converter”, “Temperature Converter”, and “Exit”.
        JButton buttonRight=new JButton("Temperature Converter");
        JButton buttonBottom=new JButton("Exit");
        centerPanel.add(buttonLeft);//We add them to the Panel, add panel to frame and set size and layout of frame.
        centerPanel.add(buttonRight);
        framework.add(centerPanel);
        framework.add(buttonBottom);
        //framework.setLayout(new BorderLayout());
        framework.setSize(450,80);
        framework.setVisible(true);
        framework.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        */
        
        
        
        //Adding ActionListener to buttons
        //When user clicks Distance Converter, an input dialog will pop up where user can type value and click OK. Once user clicks OK, message dialog will pop up with converted result.
        buttonLeft.addActionListener(new ActionListener() {
        @Override
            public void actionPerformed(ActionEvent e) {
                String str = JOptionPane.showInputDialog("Enter Distance In Miles:"); //str will store input string from JOptionPane.showInputDialog()
                Double miles = Double.parseDouble(str);//Conversion to Double and storing in miles variable
                Converter obj = new Converter(miles);//Creation of new DistanceConverter obj using miles
                JOptionPane.showMessageDialog(framework,"Distance in KM is "+obj.convert());//Calling convert() of obj and displaying result in JOptionPane.showMessageDialog
            }    
        });
        //When user clicks on Temperature button, an input dialog will pop up to input value and then when clicks OK, the message dialog with pop up with converted result
        buttonRight.addActionListener(new ActionListener() {
        @Override
            public void actionPerformed(ActionEvent e) {
            String str = JOptionPane.showInputDialog("Enter Temperature In Fahrenheit :"); //str will store input string from JOptionPane.showInputDialog()
            Double far = Double.parseDouble(str);//Conversion to Double and storing in far variable
            Converter obj = new Converter(far);//Creation of new TemperatureConverter obj using far
            JOptionPane.showMessageDialog(framework,"Temperature in Celsius is "+obj.convert());
            }
        });
        //When user clicks Exit, the program will terminate
        buttonBottom.addActionListener(new ActionListener() {
        @Override
            public void actionPerformed(ActionEvent e) {
                framework.dispose();//We dispose the frame f
            }
        });
    }
    public static void main(String[] args) {
        new GUIConverter();//We call the constructor to create the GUI
    }
}