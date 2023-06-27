from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    current_time = datetime.now()
    return render_template("index.html", current_time=current_time)


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


if __name__ == "__main__":
    app.run(debug=True)
