import javax.swing.*;
import java.awt.*;

//public class GUIConverter {
public class GUIConverter {

    public static void main(String[] args) {

        // create a JFrame and set its size
        JFrame frame = new JFrame("Welcome to Converter, comrade");
        frame.setSize(600, 300); //size for program
        
        JPanel panelMain = new JPanel(new BorderLayout()); // create a main panel and set its layout
        JPanel panelCenter = new JPanel(new GridLayout()); // create a nested panel for the center buttons
        JButton button1 = new JButton("Left Button"); 
        JButton button2 = new JButton("Right Button");
        JButton button3 = new JButton("Bottom Button");
        panelCenter.add(button1);
        panelCenter.add(button2);
        panelMain.add(panelCenter, BorderLayout.CENTER); //add center panel to main panel
        panelMain.add(button3, BorderLayout.SOUTH);
        // create a third button and add it to the bottom of the main panel
        

        // add the panel to the frame and set it to visible
        frame.add(panelMain);
        frame.setVisible(true);
    }
}
