from datetime import datetime
import logging
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "session-key"

logging.basicConfig(
    filename="login_attempts.log", level=logging.INFO, format="%(asctime)s %(message)s"
)


# Index
@app.route("/")
def home():
    current_time = datetime.now()
    fish_list = [
        {"name": "Bass", "size": "medium"},
        {"name": "Bluegill", "size": "small"},
        {"name": "Catfish", "size": "medium"},
        {"name": "Cod", "size": "medium"},
        {"name": "Tuna", "size": "large"},
        {"name": "Pufferfish", "size": "small"},
    ]
    return render_template("index.html", current_time=current_time, fish_list=fish_list)


# Fish stuff page
@app.route("/fish")
def fish_stuff():
    current_time = datetime.now()
    return render_template("fish_stuff.html", current_time=current_time)


# Contact page
@app.route("/contact")
def contact():
    current_time = datetime.now()
    return render_template("contact.html", current_time=current_time)


# User registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if (
            len(password) >= 12
            and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in "!@#$%^&*()-_=+[]{};:,<.>/?`~" for char in password)
        ):
            session["username"] = username
            session["password"] = password
            return redirect(url_for("dashboard"))
        else:
            return render_template(
                "register.html", error="Password does not meet complexity requirements."
            )

    return render_template("register.html")


# User login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if session.get("username") == username and session.get("password") == password:
            session["logged_in"] = True
            return redirect(url_for("dashboard"))

        logging.info(
            f"Failed login attempt for username: {username}, IP: {request.remote_addr}"
        )
        return render_template("login.html", error="Invalid username or password.")

    return render_template("login.html")


# Update password
@app.route("/update_password", methods=["GET", "POST"])
def update_password():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":
        current_password = request.form["current_password"]
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        if session.get("password") != current_password:
            return render_template(
                "update_password.html", error="Invalid current password."
            )

        if (
            len(new_password) < 12
            or not any(char.isupper() for char in new_password)
            or not any(char.islower() for char in new_password)
            or not any(char.isdigit() for char in new_password)
            or not any(char in "!@#$%^&*()-_=+[]{};:,<.>/?`~" for char in new_password)
        ):
            return render_template(
                "update_password.html",
                error="New password does not meet complexity requirements.",
            )

        with open("common_passwords.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
            if new_password in common_passwords:
                return render_template(
                    "update_password.html", error="New password is commonly used."
                )

        session["password"] = new_password
        return redirect(url_for("dashboard"))

    return render_template("update_password.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if session.get("logged_in"):
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
