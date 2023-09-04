from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "session-key"  # Set a secret key for session management


# Index
@app.route("/")
def home():
    current_time = datetime.now()
    # Table for fish sizes
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

        # Validate password complexity
        if (
            len(password) >= 12
            and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in "!@#$%^&*()-_=+[]{};:,<.>/?`~" for char in password)
        ):
            # Save the user's registration details to session
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

        # Check if the username and password match the session data
        if session.get("username") == username and session.get("password") == password:
            # Perform login logic
            session["logged_in"] = True
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid username or password.")

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    # Check if the user is logged in using session data
    if session.get("logged_in"):
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # Clear session data and log out the user
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
