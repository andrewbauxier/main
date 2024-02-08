/**
 * Project Name:    Homework 1
 * Module Name:     sdev425.java
 * Author:          Andrew Auxier
 * Contributors:    Jim
 * Organization:    N/A
 * Description:     
 * 
 * This is code provided to me by the school, which I then turned around and modified to add additional security features. The assignment calls for using JDK 8 and NetBeans. Jim provided modfied source code from Oracle's Login Tutorial Application @ https://docs.oracle.com/javafx/2/get_started/form.htm for the project base. Good job, Jim.
*/

// LoginApp.java
package Main;

import LoginScreen;
import javafx.application.Application;
import javafx.stage.Stage;

public class Main extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        LoginScreen loginScreen = new LoginScreen(primaryStage);
        loginScreen.show();
    }
}
