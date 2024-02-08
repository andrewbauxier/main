/**
 * Project Name:    Homework 1
 * Module Name:     sdev425.java
 * Author:          Andrew Auxier
 * Contributors:    Jim
 * Organization:    N/A
 * Description:     
 * 
 * This is code provided to me by the school, which I then turned around and modified to add additional security features. The assignment calls for using JDK 8 and NetBeans. Jim provided modfied source code from Oracle's Login Tutorial Application @ https://docs.oracle.com/javafx/2/get_started/form.htm for the project base. Good job, Jim.
 * 
 * Modifications:
 *      AC-7 - UNSUCCESSFUL LOGON ATTEMPTS  Added lockout to suppress brute force attacks
 *      AC-8 - SYSTEM USE NOTIFICATION:     Added notification for successful login
*/

package assignment2;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.stage.Stage;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class App extends Application {
    // Class fields for unsuccessfulAttempts and MAX_ATTEMPTS
    private int unsuccessfulAttempts = 0; // Initialize lockout counter
    private final int MAX_ATTEMPTS = 3; // Define the maximum number of unsuccessful attempts

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("SDEV425 Login");
        // Grid Pane divides your window into grids
        GridPane grid = new GridPane();
        // Align to Center
        // Note Position is geometric object for alignment
        grid.setAlignment(Pos.CENTER);
        // Set gap between the components
        // Larger numbers mean bigger spaces
        grid.setHgap(10);
        grid.setVgap(10);

        // Create some text to place in the scene
        Text sceneTitle = new Text("Welcome. Login to continue.");
        // Add text to grid 0,0 span 2 columns, 1 row
        grid.add(sceneTitle, 0, 0, 2, 1);

        // Create Label
        Label userName = new Label("User Name:");
        // Add label to grid 0,1
        grid.add(userName, 0, 1);

        // Create Textfield
        TextField userTextField = new TextField();
        // Add textfield to grid 1,1
        grid.add(userTextField, 1, 1);

        // Create Label
        Label password = new Label("Password:");
        // Add label to grid 0,2
        grid.add(password, 0, 2);

        // Create Passwordfield
        PasswordField passwordBox = new PasswordField();
        // Add Password field to grid 1,2
        grid.add(passwordBox, 1, 2);

        // Create Login Button
        Button btn = new Button("Login");
        // Add button to grid 1,4
        grid.add(btn, 1, 4);

        final Text actiontarget = new Text();
        grid.add(actiontarget, 1, 6);

        // Set the Action when button is clicked
        btn.setOnAction(new EventHandler<ActionEvent>() {

            @Override
            public void handle(ActionEvent e) {

                // Authenticate the user
                boolean isValid = authenticate(userTextField.getText(), passwordBox.getText());
                // Record the attempt to log in
                logAuditRecord(userTextField.getText(), isValid);
                // If valid clear the grid and Welcome the user
                if (isValid) {
                    unsuccessfulAttempts = 0; // Reset unsuccessful attempts on successful login
                    grid.setVisible(false);
                    GridPane grid2 = new GridPane();
                    // Align to Center
                    // Note Position is geometric object for alignment
                    grid2.setAlignment(Pos.CENTER);
                    // Set gap between the components
                    // Larger numbers mean bigger spaces
                    grid2.setHgap(10);
                    grid2.setVgap(10);
                    Text sceneTitle = new Text("Welcome " + userTextField.getText() + "!");
                    // Add text to grid 0,0 span 2 columns, 1 row
                    grid2.add(sceneTitle, 0, 0, 2, 1);
                    Scene scene = new Scene(grid2, 500, 400);
                    primaryStage.setScene(scene);
                    primaryStage.show();
                    showSystemUseNotification("User " + userTextField.getText() + " logged in successfully.");

                    // If Invalid Ask user to try again
                } else {
                    unsuccessfulAttempts++;
                    if (unsuccessfulAttempts >= MAX_ATTEMPTS) {
                        // Implement account lock or introduce a delay here
                        // For example, disable the login button temporarily
                        btn.setDisable(true);
                    }
                    final Text actiontarget = new Text();
                    grid.add(actiontarget, 1, 6);
                    actiontarget.setFill(Color.FIREBRICK);
                    actiontarget.setText("Please try again.");
                }

            }
        });
        // Set the size of Scene
        Scene scene = new Scene(grid, 500, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }

    /**
     * @param user     the username entered
     * @param password the password entered
     * @return isValid true for authenticated
     */
    public boolean authenticate(String user, String password) {
        boolean isValid = false;
        // if (user.equalsIgnoreCase("sdevadmin")
        if (user.equalsIgnoreCase("pass") && password.equals("pass")) {
            isValid = true;
        }
        return isValid;
    }

    private void showSystemUseNotification(String message) {
        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setTitle("System Use Notification");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    // Audit Record Logging
    private void logAuditRecord(String username, boolean isValid) {
        String status = isValid ? "Success" : "Failure";
        String timestamp = java.time.LocalDateTime.now().toString();

        // Create a structured audit record format
        String auditRecord = String.format("Timestamp: %s | User: %s | Event: Login Attempt | Status: %s", timestamp,
                username, status);
        // Log the audit record to a file
        try (PrintWriter writer = new PrintWriter(new FileWriter("audit_log.txt", true))) {
            writer.println(auditRecord);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Log the audit record to the console for error checking
        System.out.println("Audit Record: " + auditRecord);
    }

}
