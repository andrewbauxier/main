import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


//public class GUIConverter {
public class GUIConverter {

    public static void main(String[] args) {
        // create a JFrame and set its size
        JFrame frame = new JFrame("Welcome to Converter, comrade");
        frame.setSize(1200, 600); //size for program
        JPanel panelMain = new JPanel(new BorderLayout()); // create a main panel and set its layout
        JPanel panelCenter = new JPanel(new GridLayout()); // create a nested panel for the center buttons
        JButton buttonLeft = new JButton("Left Button"); 
        JButton buttonRight = new JButton("Right Button");
        JButton buttonBottom = new JButton("Bottom Button"); 
        panelCenter.add(buttonLeft); //add left button to center panel
        panelCenter.add(buttonRight); //add right button to center panel
        panelMain.add(panelCenter, BorderLayout.CENTER); //add center panel to main panel
        panelMain.add(buttonBottom, BorderLayout.SOUTH); //add bottom button to main panel        
        frame.add(panelMain); // add main panel to frame
        frame.setVisible(true); //enable main panel visibility
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //clicking X closes program
        
        /* Begin Listeners */
        // ButtonListener listener = new ButtonListener();
        // buttonBottom.addActionListener(listener);
        /* End Listeners */
    }//end main

    /* Begin methods */
    public class ButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Code to handle button click event
        }
    }

    /* End Methods */

}//end GUIConverter



