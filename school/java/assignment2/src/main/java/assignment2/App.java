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
 *  AC-7 - UNSUCCESSFUL LOGON ATTEMPTS: Added lockout to suppress brute force attacks
 * 
 *  AC-8 - SYSTEM USE NOTIFICATION:     Added notification for successful login.
 *  
 *  AU-3 - CONTENT OF AUDIT RECORDS:    Added logging function to record login attempts.
 *  Added a logging function to the program that logs the the date and time, username, event, and pass or fail. Since it records the date and time, there's no need to add further date and time on here. 
 * IA-2(1) IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS) | NETWORK ACCESS TO PRIVILEGED ACCOUNTS:                              
 * 
 * 
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
    // Class fields for unsuccessfulAttempts, MAX_ATTEMPTS, and mfaCode
    private int unsuccessfulAttempts = 0; // Initialize lockout counter
    private final int MAX_ATTEMPTS = 3; // Define the maximum number of unsuccessful attempts
    private String mfaCode = "pass";

    // Declare mfaTextField as a class-level field
    private TextField mfaTextField;

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
        grid.add(sceneTitle, 0, 0, 2, 1); // span 2 columns, 1 row

        // Create Label for UserName
        Label userName = new Label("User Name:");
        grid.add(userName, 0, 1);

        // Create UserName TextField
        TextField userTextField = new TextField();
        grid.add(userTextField, 1, 1);

        // Create Label for Password
        Label password = new Label("Password:");
        grid.add(password, 0, 2);

        // Create Password TextField
        PasswordField passwordBox = new PasswordField();
        grid.add(passwordBox, 1, 2);

        // Create Label for MFA
        Label mfaLabel = new Label("One-Time Code:");
        grid.add(mfaLabel, 0, 3);

        // Create MFA Text Field
        mfaTextField = new TextField();
        grid.add(mfaTextField, 1, 3);

        // Create Login Button
        Button btn = new Button("Login");
        grid.add(btn, 1, 6);

        final Text actiontarget = new Text();
        grid.add(actiontarget, 1, 6);

        // Set the Action when the button is clicked
        btn.setOnAction(new EventHandler<ActionEvent>() {

            @Override
            public void handle(ActionEvent e) {

                // Authenticate the user
                boolean isValid = authenticate(userTextField.getText(), passwordBox.getText());

                // Record the attempt to log in
                logAuditRecord(userTextField.getText(), isValid);

                // If valid, clear the grid and welcome the user
                if (isValid) {
                    unsuccessfulAttempts = 0; // Reset unsuccessful attempts on successful login

                    // Create grid for the welcome message
                    GridPane grid2 = new GridPane();
                    grid2.setAlignment(Pos.CENTER);
                    grid2.setHgap(10);
                    grid2.setVgap(10);

                    // Add text to grid 0,0 span 2 columns, 1 row
                    Text sceneTitle = new Text("Welcome " + userTextField.getText() + "!");
                    grid2.add(sceneTitle, 0, 1);

                    // Set up the scene with grid2
                    Scene scene = new Scene(grid2, 500, 400);
                    primaryStage.setScene(scene);
                    primaryStage.show();

                    // Show system use notification
                    showSystemUseNotification("User " + userTextField.getText() + " logged in successfully.");

                } else {
                    unsuccessfulAttempts++;
                    if (unsuccessfulAttempts >= MAX_ATTEMPTS) {
                        // Implement account lock or introduce a delay here
                        // For example, disable the login button temporarily
                        btn.setDisable(true);

                        // Create a stage for the security question
                        Stage securityQuestionStage = new Stage();
                        securityQuestionStage.setTitle("Security Question");
                        GridPane securityQuestionGrid = new GridPane();
                        securityQuestionGrid.setAlignment(Pos.CENTER);
                        securityQuestionGrid.setHgap(10);
                        securityQuestionGrid.setVgap(10);

                        Label securityQuestionLabel = new Label("What is 2 + 2?");
                        securityQuestionGrid.add(securityQuestionLabel, 0, 0);

                        TextField answerTextField = new TextField();
                        securityQuestionGrid.add(answerTextField, 0, 1);

                        Button answerButton = new Button("Submit Answer");
                        securityQuestionGrid.add(answerButton, 0, 2);

                        Scene securityQuestionScene = new Scene(securityQuestionGrid, 300, 200);
                        securityQuestionStage.setScene(securityQuestionScene);
                        securityQuestionStage.show();

                        // Check the answer when the button is clicked
                        answerButton.setOnAction(event -> {
                            boolean isCorrectAnswer = checkSecurityQuestion(answerTextField.getText());
                            if (isCorrectAnswer) {
                                // Re-enable the button when answered
                                btn.setDisable(false);
                                securityQuestionStage.close(); // Close the security question window
                            } else {
                                // Show an error message
                                System.out.println("Incorrect answer. Please try again.");
                            }
                        });
                    }

                    final Text actiontarget = new Text();
                    grid.add(actiontarget, 1, 8);
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
    public boolean authenticate(String username, String password) {
        // Simulated MFA code validation (TODO: Replace with actual implementation)
        boolean isValidMFA = mfaTextField.getText().equals(mfaCode);
        // Log-in Credentials
        boolean isValidCredentials = validateCredentials(username, password);

        // Return true only if both MFA and credentials are valid
        return isValidMFA && isValidCredentials;
    }

    private boolean validateCredentials(String username, String password) {
        // Replace with your actual username and password validation logic
        // For example, check against a database or external authentication service
        return "pass".equalsIgnoreCase(username) && "pass".equals(password);
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
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        // Log the audit record to the console for error checking
        System.out.println("Audit Record: " + auditRecord);
    }

    // Add a method to check the security question
    private boolean checkSecurityQuestion(String answer) {
        // Security question answer
        return "4".equals(answer);
    }
}
