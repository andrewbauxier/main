module loginapp {
    requires javafx.controls;
    requires javafx.fxml;

    opens Main to javafx.fxml;
    opens LoginScreen to javafx.fxml;
    opens WelcomeScreen to javafx.fxml;

    exports Main;
    exports LoginScreen;
    exports WelcomeScreen;
}
