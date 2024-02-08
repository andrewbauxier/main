module LoginScreen {
    requires javafx.controls;
    requires javafx.fxml;

    opens LoginScreen to javafx.fxml;

    exports LoginScreen;
}
