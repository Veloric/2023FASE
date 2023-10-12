# Team 3's Python driver
# This is the main driver for the project; hosts all methods, calls to database, as well as functionally runs the website.

from flask import Flask as fl
from flask import url_for, request, render_template, redirect
from markupsafe import escape
import MySQLdb.cursors

#Initialize FLASK
app = fl(__name__, static_url_path='/static')
app.secret_key = "Team3Project"

#Database connection set up
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "bakery"

mysql = MySQL(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/order", methods=("GET", "POST"))
def order():
    msg = ""
    if request.method == "POST":
        if "flavor" in request.form and "size" in request.form and "quantity" in request.form and "decor" in request.form:
            flavor = request.form.get("flavor")
            size = request.form.get("size")
            quantity = request.form.get("quantity")
            decor = request.form.get("decor")
        else:
            msg = "There was an error handling your request, please try again!"
        pass
    #TODO: Send data to database
    #TODO: Actually set up database

    return render_template("order.html", msg=msg)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/register")
def register():
    return render_template("register.html")

# We don't have a login.html in templates/ yet
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()