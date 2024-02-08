// LoginScreen.java
package LoginScreen;

import WelcomeScreen.WelcomeScreen;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class LoginScreen {

    private final Stage primaryStage;

    public LoginScreen(Stage primaryStage) {
        this.primaryStage = primaryStage;
    }

    public void show() {
        primaryStage.setTitle("SDEV425 Login");

        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);

        Text sceneTitle = new Text("Welcome. Login to continue.");
        grid.add(sceneTitle, 0, 0, 2, 1);

        Label userName = new Label("User Name:");
        grid.add(userName, 0, 1);

        TextField userTextField = new TextField();
        grid.add(userTextField, 1, 1);

        Label password = new Label("Password:");
        grid.add(password, 0, 2);

        PasswordField passwordBox = new PasswordField();
        grid.add(passwordBox, 1, 2);

        Button btn = new Button("Login");
        grid.add(btn, 1, 4);

        final Text actiontarget = new Text();
        grid.add(actiontarget, 1, 6);

        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent e) {
                boolean isValid = authenticate(userTextField.getText(), passwordBox.getText());
                if (isValid) {
                    switchToWelcomeScreen(userTextField.getText());
                } else {
                    showErrorMessage(actiontarget);
                }
            }
        });

        Scene scene = new Scene(grid, 500, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private boolean authenticate(String user, String password) {
        return user.equalsIgnoreCase("sdevadmin") && password.equals("425!pass");
    }

    private void switchToWelcomeScreen(String username) {
        primaryStage.hide();
        WelcomeScreen welcomeScreen = new WelcomeScreen(primaryStage, username);
        welcomeScreen.show();
    }

    private void showErrorMessage(Text actiontarget) {
        actiontarget.setFill(Color.FIREBRICK);
        actiontarget.setText("Please try again.");
    }
}
